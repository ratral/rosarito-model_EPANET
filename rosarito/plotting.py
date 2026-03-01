"""Matplotlib figures for the Quarto engineering report.

Four publication-quality figures with consistent styling:
serif fonts, subtle grid, VAG-inspired color palette.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import pandas as pd

from rosarito.constants import (
    H_SHUTOFF_M,
    Q_RATED_LPS,
    H_RATED_M,
    Q_MIN_STABLE_LPS,
    Q_BEP_BOWL_LPS,
    PUMP_IDS,
    RIKO_CSV,
    RIKO_OPENINGS_ALL,
)
from rosarito.model import SteadyStateResult, EPSResult
from rosarito.energy import ScenarioEnergyResult
from rosarito.validation import ScenarioValidation

# ---------------------------------------------------------------------------
# VAG-inspired color palette
# ---------------------------------------------------------------------------
VAG_GREEN = "#009D30"
VAG_DARK_GREEN = "#007025"
VAG_BLUE = "#1965A3"
VAG_GRAY = "#808080"
VAG_DARK = "#333333"

SCENARIO_COLORS = [VAG_DARK_GREEN, VAG_GREEN, VAG_BLUE, "#E8A317"]

# Color map: n_pumps → color for valve operating point markers
_NPUMPS_COLORS = {4: VAG_DARK_GREEN, 3: VAG_GREEN, 2: VAG_BLUE, 1: "#E8A317"}


def _apply_style(ax: plt.Axes) -> None:
    """Apply consistent professional styling to an axes."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.3, linewidth=0.5)
    ax.tick_params(labelsize=9)


# ---------------------------------------------------------------------------
# Figure 1: Pump H-Q curve with operating points
# ---------------------------------------------------------------------------

def _solve_pump_curve() -> tuple[float, float]:
    """Solve H = H_shutoff - B * Q^C using the 3-point EPANET fit.

    Points: (0, 46.54), (1256, 26.07), (1700, 14.50)
    At Q=0: H = H_shutoff, so we solve for B, C from the other two points.
    """
    q1, h1 = Q_RATED_LPS, H_RATED_M       # (1256, 26.07)
    q2, h2 = 1700.0, 14.50                 # shutoff extrapolation point

    dh1 = H_SHUTOFF_M - h1  # 46.54 - 26.07 = 20.47
    dh2 = H_SHUTOFF_M - h2  # 46.54 - 14.50 = 32.04

    # dh1 = B * q1^C  and  dh2 = B * q2^C
    # => dh2/dh1 = (q2/q1)^C  => C = ln(dh2/dh1) / ln(q2/q1)
    C = np.log(dh2 / dh1) / np.log(q2 / q1)
    B = dh1 / (q1 ** C)
    return float(B), float(C)


def plot_pump_hq(staging_results: list[SteadyStateResult]) -> Figure:
    """Pump H-Q characteristic curve with operating points marked."""
    B, C = _solve_pump_curve()
    q_range = np.linspace(0, 1800, 300)
    h_curve = H_SHUTOFF_M - B * np.power(np.maximum(q_range, 1e-6), C)

    fig, ax = plt.subplots(figsize=(8, 5))
    _apply_style(ax)

    # H-Q curve
    ax.plot(q_range, h_curve, color=VAG_DARK_GREEN, linewidth=2,
            label="Pump H-Q curve")

    # Operating points
    for i, r in enumerate(staging_results):
        ax.plot(r.q_per_pump_lps, r.h_pump_m, "o", color=SCENARIO_COLORS[i],
                markersize=9, zorder=5)
        ax.annotate(
            f"{r.n_active_pumps}P",
            (r.q_per_pump_lps, r.h_pump_m),
            textcoords="offset points", xytext=(10, 8),
            fontsize=9, fontweight="bold", color=SCENARIO_COLORS[i],
        )

    # Vertical reference lines
    ax.axvline(Q_MIN_STABLE_LPS, color=VAG_GRAY, linestyle="--",
               linewidth=0.8, alpha=0.7)
    ax.text(Q_MIN_STABLE_LPS + 15, H_SHUTOFF_M - 2, "Q_min_stable",
            fontsize=8, color=VAG_GRAY, rotation=90, va="top")

    ax.axvline(Q_BEP_BOWL_LPS, color=VAG_BLUE, linestyle="--",
               linewidth=0.8, alpha=0.7)
    ax.text(Q_BEP_BOWL_LPS + 15, H_SHUTOFF_M - 2, "Q_BEP",
            fontsize=8, color=VAG_BLUE, rotation=90, va="top")

    ax.set_xlabel("Flow per pump, Q (l/s)", fontsize=10)
    ax.set_ylabel("Pump head, H (m)", fontsize=10)
    ax.set_title("Ruhrpumpen 35WX — H-Q Characteristic with Operating Points",
                 fontsize=11, fontweight="bold", color=VAG_DARK)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_xlim(0, 1850)
    ax.set_ylim(0, 50)

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Figure 2: Energy comparison bar chart
# ---------------------------------------------------------------------------

def plot_energy_comparison(energy: list[ScenarioEnergyResult]) -> Figure:
    """Grouped bar chart of total shaft power per scenario."""
    fig, ax = plt.subplots(figsize=(8, 5))
    _apply_style(ax)

    labels = [f"{e.n_pumps}-pump" for e in energy]
    p_total = [e.p_total_shaft_kw for e in energy]
    x = np.arange(len(labels))

    bars = ax.bar(x, p_total, width=0.5, color=SCENARIO_COLORS[:len(energy)],
                  edgecolor="white", linewidth=0.5)

    # Annotate each bar with E_24h and motor load
    for i, (bar, e) in enumerate(zip(bars, energy)):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 15,
                f"{e.energy_kwh:,.0f} kWh/day\n"
                f"Motor: {e.pump.motor_load_pct:.0f}%",
                ha="center", va="bottom", fontsize=8, color=VAG_DARK)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylabel("Total shaft power, P_total (kW)", fontsize=10)
    ax.set_title("Station Power Consumption by Staging Scenario",
                 fontsize=11, fontweight="bold", color=VAG_DARK)

    ax.set_ylim(0, max(p_total) * 1.35)
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Figure 3: EPS time-series (3-panel)
# ---------------------------------------------------------------------------

def plot_eps_timeseries(eps: EPSResult) -> Figure:
    """3-panel time series: flow, head, and pump status bars."""
    time_h = [t / 3600.0 for t in eps.time_s]
    q_ds = eps.flows["P_DS"]
    h_manifold = eps.heads["J_MANIFOLD"]
    h_suction = eps.heads["J_SUCTION"]
    h_pump = [hm - hs for hm, hs in zip(h_manifold, h_suction)]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8),
                                         sharex=True,
                                         gridspec_kw={"height_ratios": [2, 2, 1.5]})

    # Trip/restore times for vertical dashed lines
    trip_times = [6, 8, 12, 14, 18, 20]

    # --- Top panel: Flow ---
    _apply_style(ax1)
    ax1.plot(time_h, q_ds, color=VAG_BLUE, linewidth=1.5)
    ax1.set_ylabel("Q_DS (l/s)", fontsize=10)
    ax1.set_title("24-Hour Extended Period Simulation",
                  fontsize=11, fontweight="bold", color=VAG_DARK)
    for t in trip_times:
        ax1.axvline(t, color=VAG_GRAY, linestyle=":", linewidth=0.6, alpha=0.5)

    # --- Middle panel: Pump head ---
    _apply_style(ax2)
    ax2.plot(time_h, h_pump, color=VAG_GREEN, linewidth=1.5)
    ax2.set_ylabel("H_pump (m)", fontsize=10)
    for t in trip_times:
        ax2.axvline(t, color=VAG_GRAY, linestyle=":", linewidth=0.6, alpha=0.5)

    # --- Bottom panel: Pump status ---
    _apply_style(ax3)
    pump_colors = [VAG_DARK_GREEN, VAG_GREEN, VAG_BLUE, "#E8A317", VAG_GRAY]
    for j, pid in enumerate(PUMP_IDS):
        statuses = eps.statuses[pid]
        y_vals = [j + 0.8 if s != 0 else j for s in statuses]
        ax3.fill_between(time_h, j, y_vals, step="post",
                         color=pump_colors[j], alpha=0.7, linewidth=0)
        ax3.text(-0.8, j + 0.4, pid.replace("PUMP_", "P"),
                 fontsize=8, ha="right", va="center", color=VAG_DARK)

    ax3.set_ylim(-0.2, len(PUMP_IDS) + 0.2)
    ax3.set_yticks([])
    ax3.set_xlabel("Time (hours)", fontsize=10)
    ax3.set_ylabel("Pump status", fontsize=10)
    for t in trip_times:
        ax3.axvline(t, color=VAG_GRAY, linestyle=":", linewidth=0.6, alpha=0.5)

    ax3.set_xlim(0, 24)

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Figure 4: Validation deviations
# ---------------------------------------------------------------------------

def plot_validation_deviations(
    validations: list[ScenarioValidation],
) -> Figure:
    """Horizontal bar chart of deviation (%) per parameter per scenario."""
    fig, ax = plt.subplots(figsize=(8, 5))
    _apply_style(ax)

    # Gather all unique parameter names (in order from first scenario)
    param_names = []
    for c in validations[0].checks:
        if c.name not in param_names:
            param_names.append(c.name)

    n_params = len(param_names)
    n_scenarios = len(validations)
    bar_height = 0.8 / n_scenarios
    y_base = np.arange(n_params)

    for i, val in enumerate(validations):
        devs = []
        for pname in param_names:
            check = next((c for c in val.checks if c.name == pname), None)
            devs.append(check.deviation_pct if check else 0.0)

        y_pos = y_base + i * bar_height
        color = SCENARIO_COLORS[i] if i < len(SCENARIO_COLORS) else VAG_GRAY
        ax.barh(y_pos, devs, height=bar_height * 0.9, color=color,
                label=f"{val.n_pumps}-pump", alpha=0.85)

    # 5% tolerance line
    ax.axvline(5.0, color="#b91c1c", linestyle="--", linewidth=1.2,
               label="5% tolerance")

    ax.set_yticks(y_base + bar_height * (n_scenarios - 1) / 2)
    ax.set_yticklabels(param_names, fontsize=9)
    ax.set_xlabel("Deviation (%)", fontsize=10)
    ax.set_title("Validation Deviations — Computed vs Reference",
                 fontsize=11, fontweight="bold", color=VAG_DARK)
    ax.legend(loc="lower right", fontsize=8)
    ax.invert_yaxis()

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Valve characteristic data loader
# ---------------------------------------------------------------------------

def _load_riko_csv() -> pd.DataFrame:
    """Load and parse the RIKO DN1800 valve characteristic CSV.

    Strips '%' from positions and removes commas from Kv numbers.
    """
    df = pd.read_csv(RIKO_CSV)
    df["position"] = df["valve_position"].str.rstrip("%").astype(int)
    df["kv"] = df["kv_value"].astype(str).str.replace(",", "").astype(float)
    df["zeta"] = df["zeta_value"].astype(float)
    return df


# ---------------------------------------------------------------------------
# Figure 5: Valve Kv curve with operating points
# ---------------------------------------------------------------------------

def plot_valve_kv() -> Figure:
    """Kv vs opening % with 7 operating points color-coded by pump count."""
    df = _load_riko_csv()

    fig, ax = plt.subplots(figsize=(8, 5))
    _apply_style(ax)

    # Full Kv curve
    ax.plot(df["position"], df["kv"], color=VAG_DARK_GREEN, linewidth=2,
            label="Kv characteristic")

    # Operating range shading (22%–44%)
    ax.axvspan(22, 44, color=VAG_GREEN, alpha=0.10, label="Operating range (22–44%)")

    # Operating points from RIKO_OPENINGS_ALL
    for op in RIKO_OPENINGS_ALL:
        color = _NPUMPS_COLORS[op.n_pumps]
        ax.plot(op.phi_pct, op.kv_m3h, "o", color=color, markersize=9, zorder=5)
        ax.annotate(
            f"{op.n_pumps}P @ {op.phi_pct}%",
            (op.phi_pct, op.kv_m3h),
            textcoords="offset points", xytext=(10, 6),
            fontsize=8, fontweight="bold", color=color,
        )

    ax.set_xlabel("Valve opening (%)", fontsize=10)
    ax.set_ylabel("Flow coefficient, Kv (m³/h)", fontsize=10)
    ax.set_title("VAG RIKO DN1800 — Kv Characteristic",
                 fontsize=11, fontweight="bold", color=VAG_DARK)
    ax.legend(loc="upper left", fontsize=9)
    ax.set_xlim(0, 105)
    ax.set_ylim(0, None)

    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Figure 6: Valve zeta curve (log scale)
# ---------------------------------------------------------------------------

def plot_valve_zeta() -> Figure:
    """Zeta vs opening % with logarithmic y-axis and operating range shaded."""
    df = _load_riko_csv()

    fig, ax = plt.subplots(figsize=(8, 5))
    _apply_style(ax)

    # Full zeta curve (log scale)
    ax.semilogy(df["position"], df["zeta"], color=VAG_BLUE, linewidth=2,
                label="ζ characteristic")

    # Operating range shading (22%–44%)
    ax.axvspan(22, 44, color=VAG_GREEN, alpha=0.10, label="Operating range (22–44%)")

    ax.set_xlabel("Valve opening (%)", fontsize=10)
    ax.set_ylabel("Loss coefficient, ζ (—)", fontsize=10)
    ax.set_title("VAG RIKO DN1800 — ζ Characteristic (Log Scale)",
                 fontsize=11, fontweight="bold", color=VAG_DARK)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_xlim(0, 105)

    fig.tight_layout()
    return fig
