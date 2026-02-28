"""DataFrame builders for Quarto report tables.

Converts existing domain dataclasses into pandas DataFrames suitable
for rendering via ``df.to_markdown(index=False)`` in Quarto/Jupyter cells.
"""

from __future__ import annotations

import pandas as pd

from rosarito.constants import RIKO_BY_NPUMPS, lps_to_m3h
from rosarito.model import SteadyStateResult, EPSResult
from rosarito.energy import ScenarioEnergyResult
from rosarito.validation import ScenarioValidation
from rosarito.eps_utils import iter_eps_events


def staging_dataframe(results: list[SteadyStateResult]) -> pd.DataFrame:
    """Build the steady-state staging comparison table."""
    rows = []
    for r in results:
        riko = RIKO_BY_NPUMPS[r.n_active_pumps]
        rows.append({
            "Pumps": r.n_active_pumps,
            "RIKO (%)": r.riko_opening_pct,
            "Kv (m³/h)": f"{riko.kv_m3h:,.2f}",
            "Q_total (l/s)": f"{r.q_total_lps:.1f}",
            "Q_total (m³/h)": f"{lps_to_m3h(r.q_total_lps):.0f}",
            "Q/pump (l/s)": f"{r.q_per_pump_lps:.1f}",
            "H_pump (m)": f"{r.h_pump_m:.2f}",
            "dH_RIKO (m)": f"{r.dh_riko_m:.2f}",
            "v_DS (m/s)": f"{r.pipe_velocities.get('P_DS', 0.0):.3f}",
            "hf_INTAKE (m)": f"{r.pipe_headlosses.get('P_INTAKE', 0.0):.3f}",
            "hf_US (m)": f"{r.pipe_headlosses.get('P_US', 0.0):.3f}",
            "hf_DS (m)": f"{r.pipe_headlosses.get('P_DS', 0.0):.3f}",
        })
    return pd.DataFrame(rows)


def energy_dataframe(energy: list[ScenarioEnergyResult]) -> pd.DataFrame:
    """Build the energy summary table."""
    rows = []
    for e in energy:
        p = e.pump
        rows.append({
            "Pumps": e.n_pumps,
            "Q/pump (l/s)": f"{p.q_lps:.1f}",
            "H_pump (m)": f"{p.h_m:.2f}",
            "η (%)": f"{p.eta_pct:.1f}",
            "P_hyd (kW)": f"{p.p_hydraulic_kw:.1f}",
            "P_shaft (kW)": f"{p.p_shaft_kw:.1f}",
            "Motor load (%)": f"{p.motor_load_pct:.1f}",
            "P_total (kW)": f"{e.p_total_shaft_kw:.1f}",
            "E_24h (kWh)": f"{e.energy_kwh:,.0f}",
        })
    return pd.DataFrame(rows)


def validation_dataframe(val: ScenarioValidation) -> pd.DataFrame:
    """Build the validation comparison table for one scenario."""
    rows = []
    for c in val.checks:
        rows.append({
            "Parameter": c.name,
            "Computed": f"{c.computed:.2f}",
            "Reference": f"{c.reference:.2f}",
            "Deviation (%)": f"{c.deviation_pct:.2f}",
            "Result": "OK" if c.passed else "FAIL",
        })
    return pd.DataFrame(rows)


def eps_events_dataframe(eps: EPSResult) -> pd.DataFrame:
    """Build the EPS event log table."""
    rows = []
    for row in iter_eps_events(eps):
        status_strs = ["ON" if on else "OFF" for on in row.pump_on]
        rows.append({
            "Time": f"{row.hours}:{row.minutes:02d}",
            "P1": status_strs[0],
            "P2": status_strs[1],
            "P3": status_strs[2],
            "P4": status_strs[3],
            "P5": status_strs[4],
            "Active": row.n_active,
            "RIKO": row.riko_opening,
            "Q_DS (l/s)": f"{row.q_ds_lps:.1f}",
            "Q_DS (m³/h)": f"{row.q_ds_m3h:.0f}",
            "H_pump (m)": f"{row.h_pump_m:.2f}",
        })
    return pd.DataFrame(rows)
