"""Generate Markdown report of pump operation scenarios.

Runs all EPANET analyses via EPyT and writes a formatted Markdown report
with staging scenarios, energy summary, validation, and EPS event log.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from rosarito.constants import (
    INP_FILE,
    RIKO_BY_NPUMPS,
    H_PLANT,
    VAG_QMIN_M3H,
    lps_to_m3h,
)
from rosarito.model import SteadyStateResult, EPSResult
from rosarito.scenarios import (
    run_staging_scenarios,
    run_eps_with_trips,
    DEFAULT_PUMP_TRIPS,
)
from rosarito.energy import (
    compute_all_scenario_energies,
    ScenarioEnergyResult,
)
from rosarito.validation import validate_all_scenarios, ScenarioValidation
from rosarito.eps_utils import iter_eps_events


_DEFAULT_OUTPUT = Path(__file__).resolve().parent.parent / "reports" / "scenarios_report.md"


def generate_report(output_path: str | Path | None = None) -> Path:
    """Run all analyses and write Markdown report.

    Returns the path to the generated report file.
    """
    out = Path(output_path or _DEFAULT_OUTPUT)
    out.parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading model: {INP_FILE}")

    # 1. Steady-state staging
    print("Running staging scenarios...")
    staging_results = run_staging_scenarios()

    # 2. Energy calculations
    print("Computing energy...")
    energy_results = compute_all_scenario_energies(staging_results)

    # 3. Validation
    print("Validating against reference...")
    validations = validate_all_scenarios(staging_results)

    # 4. EPS with pump trips
    print("Running 24h EPS with pump trips...")
    eps = run_eps_with_trips()

    # 5. Build report
    print("Writing report...")
    md = _build_markdown(staging_results, energy_results, validations, eps)
    out.write_text(md, encoding="utf-8")

    print(f"Report written to: {out}")
    return out


# ---------------------------------------------------------------------------
# Markdown builders
# ---------------------------------------------------------------------------

def _build_markdown(
    staging: list[SteadyStateResult],
    energy: list[ScenarioEnergyResult],
    validations: list[ScenarioValidation],
    eps: EPSResult,
) -> str:
    sections = [
        _header(),
        _system_overview(),
        _staging_table(staging),
        _energy_table(energy),
        _validation_section(validations),
        _eps_event_log(eps),
        _notes(),
    ]
    return "\n\n".join(sections) + "\n"


def _header() -> str:
    today = date.today().strftime("%Y-%m-%d")
    return (
        "# Rosarito Desalination Plant — Pump Operation Scenarios Report\n\n"
        "| Field | Value |\n"
        "|-------|-------|\n"
        "| **Project** | Rosarito Desalination Plant — Seawater Intake System |\n"
        "| **Client** | CONAGUA / AYESA S.A. de C.V. |\n"
        "| **Engineer** | Dr. Raul Trujillo (VAG GmbH) |\n"
        "| **Model** | ROSARITO_EPANET_Rev2.inp |\n"
        f"| **Date** | {today} |\n"
        "| **Software** | EPANET 2.2 via EPyT |"
    )


def _system_overview() -> str:
    return (
        "## System Overview\n\n"
        "### Topology\n\n"
        "```\n"
        "SEA (H=0m) -> P_INTAKE -> J_SUCTION -> PUMP_1..5 (parallel) -> J_MANIFOLD\n"
        "-> P_US -> J_RIKO_IN -> RIKO valve (GPV) -> J_RIKO_OUT\n"
        "-> P_DS -> PLANT (H=18.17m)\n"
        "```\n\n"
        "### Equipment\n\n"
        "| Equipment | Specification |\n"
        "|-----------|---------------|\n"
        "| Pumps | 5x Ruhrpumpen 35WX vertical centrifugal (4 duty + 1 standby) |\n"
        "| Control valve | VAG RIKO DN1800 plunger valve |\n"
        "| Configuration | N+1 redundancy, rule-based staging |\n"
        "| Pipe material | DN2500 (intake), DN1800 (upstream/downstream) |\n"
        "| Friction model | Darcy-Weisbach |"
    )


def _staging_table(results: list[SteadyStateResult]) -> str:
    lines = [
        "## Steady-State Staging Scenarios",
        "",
        "| Pumps | RIKO phi (%) | Kv (m3/h) | Q_total (l/s) | Q_total (m3/h) "
        "| Q/pump (l/s) | H_pump (m) | dH_RIKO (m) | v_DS (m/s) "
        "| hf_INTAKE (m) | hf_US (m) | hf_DS (m) |",
        "|------:|-------------:|----------:|--------------:|---------------:"
        "|-------------:|-----------:|------------:|-----------:"
        "|--------------:|----------:|----------:|",
    ]

    for r in results:
        riko = RIKO_BY_NPUMPS[r.n_active_pumps]
        q_m3h = lps_to_m3h(r.q_total_lps)
        v_ds = r.pipe_velocities.get("P_DS", 0.0)
        hf_intake = r.pipe_headlosses.get("P_INTAKE", 0.0)
        hf_us = r.pipe_headlosses.get("P_US", 0.0)
        hf_ds = r.pipe_headlosses.get("P_DS", 0.0)

        lines.append(
            f"| {r.n_active_pumps} | {r.riko_opening_pct} "
            f"| {riko.kv_m3h:,.2f} | {r.q_total_lps:.1f} | {q_m3h:.0f} "
            f"| {r.q_per_pump_lps:.1f} | {r.h_pump_m:.2f} | {r.dh_riko_m:.2f} "
            f"| {v_ds:.3f} | {hf_intake:.3f} | {hf_us:.3f} | {hf_ds:.3f} |"
        )

    return "\n".join(lines)


def _energy_table(energy: list[ScenarioEnergyResult]) -> str:
    lines = [
        "## Energy Summary",
        "",
        "| Pumps | Q/pump (l/s) | H_pump (m) | eta (%) "
        "| P_hyd (kW) | P_shaft (kW) | Motor load (%) "
        "| P_total (kW) | E_24h (kWh) |",
        "|------:|-------------:|-----------:|--------:"
        "|-----------:|-------------:|---------------:"
        "|-------------:|------------:|",
    ]

    for e in energy:
        p = e.pump
        lines.append(
            f"| {e.n_pumps} | {p.q_lps:.1f} | {p.h_m:.2f} | {p.eta_pct:.1f} "
            f"| {p.p_hydraulic_kw:.1f} | {p.p_shaft_kw:.1f} | {p.motor_load_pct:.1f} "
            f"| {e.p_total_shaft_kw:.1f} | {e.energy_kwh:.0f} |"
        )

    return "\n".join(lines)


def _validation_section(validations: list[ScenarioValidation]) -> str:
    lines = [
        "## Validation — Computed vs Hand-Calculated Reference",
        "",
        "Tolerance: 5%. Reference values from Project Instructions Section 5.",
        "",
    ]

    for val in validations:
        status = "PASS" if val.all_passed else "**FAIL**"
        lines.append(f"### {val.n_pumps}-pump scenario (phi={val.phi_pct}%) — {status}")
        lines.append("")
        lines.append(
            "| Parameter | Computed | Reference | Deviation (%) | Result |"
        )
        lines.append(
            "|-----------|--------:|---------:|--------------:|:------:|"
        )

        for c in val.checks:
            tag = "OK" if c.passed else "**FAIL**"
            lines.append(
                f"| {c.name} | {c.computed:.2f} | {c.reference:.2f} "
                f"| {c.deviation_pct:.2f} | {tag} |"
            )

        if val.warnings:
            lines.append("")
            for w in val.warnings:
                lines.append(f"> **Warning:** {w}")

        lines.append("")

    return "\n".join(lines)


def _eps_event_log(eps: EPSResult) -> str:
    lines = [
        "## 24h Extended Period Simulation — Event Log",
        "",
        "Pump trips scheduled at:",
    ]
    for trip in DEFAULT_PUMP_TRIPS:
        lines.append(
            f"- **{trip.pump_id}**: trip at hour {trip.trip_hour:.0f}, "
            f"restore at hour {trip.restore_hour:.0f}"
        )
    lines.append("")
    lines.append(
        "| Time | P1 | P2 | P3 | P4 | P5 | Active | RIKO "
        "| Q_DS (l/s) | Q_DS (m3/h) | H_pump (m) |"
    )
    lines.append(
        "|-----:|:--:|:--:|:--:|:--:|:--:|-------:|-----:"
        "|-----------:|------------:|-----------:|"
    )

    for row in iter_eps_events(eps):
        time_str = f"{row.hours}:{row.minutes:02d}"
        status_strs = ["ON" if on else "OFF" for on in row.pump_on]
        lines.append(
            f"| {time_str} "
            f"| {status_strs[0]} | {status_strs[1]} | {status_strs[2]} "
            f"| {status_strs[3]} | {status_strs[4]} "
            f"| {row.n_active} | {row.riko_opening} "
            f"| {row.q_ds_lps:.1f} | {row.q_ds_m3h:.0f} | {row.h_pump_m:.2f} |"
        )

    return "\n".join(lines)


def _notes() -> str:
    return (
        "## Notes and Warnings\n\n"
        f"1. **H_PLANT = {H_PLANT} m** is back-calculated from system data, "
        "not field-measured. All operating points shift if this value changes.\n"
        f"2. **1-pump scenario** produces Q_total < VAG Qmin ({VAG_QMIN_M3H:.0f} m3/h). "
        "This is a known system characteristic, not a modeling error.\n"
        "3. Valve headloss uses ISO 5167 Kv method: dH = Q^2 x 132.15 / Kv^2. "
        "VAG's internal zeta values are **not** used.\n"
        "4. Pump efficiency is fixed at the duty-point value for energy calculations. "
        "Actual efficiency varies with operating point.\n"
        "5. EPS rule-based controls handle standby pump activation (PUMP_5) and "
        "RIKO valve position changes automatically per Georgescu et al. (CCWI 2015)."
    )
