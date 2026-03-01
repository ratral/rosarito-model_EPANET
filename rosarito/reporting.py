"""Formatted console tables for engineering review."""

from __future__ import annotations

from rosarito.constants import lps_to_m3h
from rosarito.model import SteadyStateResult, EPSResult
from rosarito.energy import ScenarioEnergyResult, ThrottleLoss
from rosarito.optimization import VFDResult
from rosarito.validation import ScenarioValidation
from rosarito.eps_utils import iter_eps_events


# ---------------------------------------------------------------------------
# Staging table
# ---------------------------------------------------------------------------

def print_staging_table(results: list[SteadyStateResult]) -> None:
    """Print the steady-state staging comparison table."""
    print()
    print("=" * 100)
    print("  STEADY-STATE STAGING SCENARIOS — ROSARITO SEAWATER INTAKE")
    print("=" * 100)
    print(
        f"{'phi%':>6}  {'N_pump':>6}  {'Q_total':>10}  {'Q_total':>10}  "
        f"{'Q/pump':>8}  {'H_pump':>8}  {'dH_RIKO':>8}  {'v_DS':>8}"
    )
    print(
        f"{'':>6}  {'':>6}  {'(l/s)':>10}  {'(m3/h)':>10}  "
        f"{'(l/s)':>8}  {'(m)':>8}  {'(m)':>8}  {'(m/s)':>8}"
    )
    print("-" * 100)

    for r in results:
        q_m3h = lps_to_m3h(r.q_total_lps)
        v_ds = r.pipe_velocities.get("P_DS", 0.0)
        print(
            f"{r.riko_opening_pct:>5}%  {r.n_active_pumps:>6}  "
            f"{r.q_total_lps:>10.1f}  {q_m3h:>10.0f}  "
            f"{r.q_per_pump_lps:>8.1f}  {r.h_pump_m:>8.2f}  "
            f"{r.dh_riko_m:>8.2f}  {v_ds:>8.3f}"
        )

    print("=" * 100)
    print()


# ---------------------------------------------------------------------------
# Validation report
# ---------------------------------------------------------------------------

def print_validation_report(validations: list[ScenarioValidation]) -> None:
    """Print per-parameter pass/FAIL report with deviation %."""
    print()
    print("=" * 90)
    print("  VALIDATION vs HAND-CALCULATED REFERENCE (Section 5)")
    print("=" * 90)

    for val in validations:
        status = "PASS" if val.all_passed else "FAIL"
        print(f"\n  {val.n_pumps}-pump (phi={val.phi_pct}%)  [{status}]")
        print(f"  {'Parameter':<12}  {'Computed':>10}  {'Reference':>10}  "
              f"{'Dev%':>8}  {'Result':>6}")
        print(f"  {'-'*60}")

        for c in val.checks:
            tag = "OK" if c.passed else "FAIL"
            print(
                f"  {c.name:<12}  {c.computed:>10.2f}  {c.reference:>10.2f}  "
                f"{c.deviation_pct:>7.2f}%  {tag:>6}"
            )

        for w in val.warnings:
            print(f"  WARNING: {w}")

    print()
    print("=" * 90)
    print()


# ---------------------------------------------------------------------------
# Energy table
# ---------------------------------------------------------------------------

def print_energy_table(energy_results: list[ScenarioEnergyResult]) -> None:
    """Print energy summary for all staging scenarios."""
    print()
    print("=" * 100)
    print("  ENERGY POST-PROCESSING — PUMP POWER AND 24h CONSUMPTION")
    print("=" * 100)
    print(
        f"{'N_pump':>6}  {'Q/pump':>8}  {'H_pump':>8}  {'eta':>6}  "
        f"{'P_hyd':>8}  {'P_shaft':>8}  {'Motor%':>8}  "
        f"{'P_total':>10}  {'E_24h':>12}"
    )
    print(
        f"{'':>6}  {'(l/s)':>8}  {'(m)':>8}  {'(%)':>6}  "
        f"{'(kW)':>8}  {'(kW)':>8}  {'':>8}  "
        f"{'(kW)':>10}  {'(kWh)':>12}"
    )
    print("-" * 100)

    for e in energy_results:
        p = e.pump
        print(
            f"{e.n_pumps:>6}  {p.q_lps:>8.1f}  {p.h_m:>8.2f}  "
            f"{p.eta_pct:>5.1f}%  {p.p_hydraulic_kw:>8.1f}  "
            f"{p.p_shaft_kw:>8.1f}  {p.motor_load_pct:>7.1f}%  "
            f"{e.p_total_shaft_kw:>10.1f}  {e.energy_kwh:>12.0f}"
        )

    print("=" * 100)
    print()


# ---------------------------------------------------------------------------
# EPS event summary
# ---------------------------------------------------------------------------

def print_eps_summary(eps: EPSResult) -> None:
    """Print event-driven EPS summary — rows where pump count or valve changes."""
    print()
    print("=" * 110)
    print("  24h EPS — EVENT SUMMARY (pump trips and valve position changes)")
    print("=" * 110)
    print(
        f"{'Time':>8}  {'P1':>4}  {'P2':>4}  {'P3':>4}  {'P4':>4}  "
        f"{'P5':>4}  {'N_act':>5}  {'RIKO':>8}  "
        f"{'Q_DS':>10}  {'Q_DS':>10}  {'H_pump':>8}"
    )
    print(
        f"{'(h:mm)':>8}  {'':>4}  {'':>4}  {'':>4}  {'':>4}  "
        f"{'':>4}  {'':>5}  {'(open)':>8}  "
        f"{'(l/s)':>10}  {'(m3/h)':>10}  {'(m)':>8}"
    )
    print("-" * 110)

    for row in iter_eps_events(eps):
        status_chars = ["ON" if on else "OFF" for on in row.pump_on]
        print(
            f"{row.hours:>5}:{row.minutes:02d}  "
            f"{status_chars[0]:>4}  {status_chars[1]:>4}  "
            f"{status_chars[2]:>4}  {status_chars[3]:>4}  "
            f"{status_chars[4]:>4}  {row.n_active:>5}  {row.riko_opening:>8}  "
            f"{row.q_ds_lps:>10.1f}  {row.q_ds_m3h:>10.0f}  {row.h_pump_m:>8.2f}"
        )

    print("=" * 110)
    print()


# ---------------------------------------------------------------------------
# Throttling analysis
# ---------------------------------------------------------------------------

def print_throttling_analysis(
    throttle_results: list[ThrottleLoss],
    phi_labels: list[int] | None = None,
) -> None:
    """Print throttle-loss table: phi, Q, dH_RIKO, P_throttle, daily_kWh."""
    print()
    print("=" * 90)
    print("  RIKO VALVE THROTTLING LOSS ANALYSIS")
    print("=" * 90)
    print(
        f"{'phi%':>6}  {'Q_total':>10}  {'Q_total':>10}  "
        f"{'dH_RIKO':>8}  {'P_throttle':>12}  {'E_24h':>10}"
    )
    print(
        f"{'':>6}  {'(l/s)':>10}  {'(m3/h)':>10}  "
        f"{'(m)':>8}  {'(kW)':>12}  {'(kWh)':>10}"
    )
    print("-" * 90)

    for i, t in enumerate(throttle_results):
        q_m3h = lps_to_m3h(t.q_total_lps)
        phi_str = f"{phi_labels[i]:>4}%" if phi_labels else ""
        print(
            f"{phi_str:>6}  {t.q_total_lps:>10.1f}  {q_m3h:>10.0f}  "
            f"{t.dh_riko_m:>8.2f}  {t.p_throttle_kw:>12.1f}  {t.daily_kwh:>10.0f}"
        )

    print("=" * 90)
    print()


# ---------------------------------------------------------------------------
# VFD comparison
# ---------------------------------------------------------------------------

def print_vfd_comparison(vfd_results: list[VFDResult]) -> None:
    """Print VFD vs throttled comparison table."""
    print()
    print("=" * 110)
    print("  VFD COMPARISON — THROTTLED (FIXED SPEED) vs VARIABLE FREQUENCY DRIVE")
    print("=" * 110)
    print(
        f"{'phi%':>6}  {'N':>3}  {'Q_total':>8}  {'H_pump':>7}  {'dH_RIKO':>7}  "
        f"{'N/N_r':>6}  {'P_throttle':>11}  {'P_VFD':>8}  "
        f"{'Save/pump':>10}  {'Save_tot':>9}  {'Save':>6}"
    )
    print(
        f"{'':>6}  {'':>3}  {'(l/s)':>8}  {'(m)':>7}  {'(m)':>7}  "
        f"{'':>6}  {'(kW/pump)':>11}  {'(kW/p)':>8}  "
        f"{'(kW)':>10}  {'(kW)':>9}  {'(%)':>6}"
    )
    print("-" * 110)

    for v in vfd_results:
        print(
            f"{v.phi_pct:>5}%  {v.n_pumps:>3}  {v.q_total_lps:>8.1f}  "
            f"{v.h_pump_throttled_m:>7.2f}  {v.h_pump_throttled_m - v.h_pump_vfd_m:>7.2f}  "
            f"{v.speed_ratio:>6.3f}  {v.p_shaft_throttled_kw:>11.1f}  "
            f"{v.p_shaft_vfd_kw:>8.1f}  {v.saving_per_pump_kw:>10.1f}  "
            f"{v.saving_total_kw:>9.1f}  {v.saving_pct:>5.1f}%"
        )

    print("=" * 110)
    print()
