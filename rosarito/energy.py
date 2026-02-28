"""Pump power and energy calculations.

Uses the Kv-based headloss and pump efficiency from Project Instructions.
P_hyd = rho × g × Q(m³/s) × H / 1000  [kW]
"""

from __future__ import annotations

from dataclasses import dataclass

from rosarito.constants import (
    RHO_SEAWATER,
    G,
    MOTOR_POWER_KW,
    ETA_DUTY_PCT,
)
from rosarito.model import SteadyStateResult


@dataclass
class PumpEnergyResult:
    """Power results for a single pump at one operating point."""
    q_lps: float
    h_m: float
    eta_pct: float
    p_hydraulic_kw: float
    p_shaft_kw: float
    motor_load_pct: float


@dataclass
class ScenarioEnergyResult:
    """Energy results for one staging scenario over a period."""
    n_pumps: int
    pump: PumpEnergyResult
    p_total_shaft_kw: float
    hours: float
    energy_kwh: float


def compute_pump_power(
    q_lps: float, h_m: float, eta_pct: float,
) -> PumpEnergyResult:
    """Compute hydraulic and shaft power for one pump.

    Args:
        q_lps: Flow per pump in l/s
        h_m: Pump head in m
        eta_pct: Pump efficiency in %
    """
    q_m3s = q_lps / 1000.0
    p_hyd = RHO_SEAWATER * G * q_m3s * h_m / 1000.0  # kW
    p_shaft = p_hyd / (eta_pct / 100.0)
    motor_load = p_shaft / MOTOR_POWER_KW * 100.0

    return PumpEnergyResult(
        q_lps=q_lps,
        h_m=h_m,
        eta_pct=eta_pct,
        p_hydraulic_kw=p_hyd,
        p_shaft_kw=p_shaft,
        motor_load_pct=motor_load,
    )


def compute_scenario_energy(
    n_pumps: int,
    q_per_pump_lps: float,
    h_m: float,
    eta_pct: float = ETA_DUTY_PCT,
    hours: float = 24.0,
) -> ScenarioEnergyResult:
    """Compute total energy for a staging scenario over a given period."""
    pump = compute_pump_power(q_per_pump_lps, h_m, eta_pct)
    p_total = pump.p_shaft_kw * n_pumps
    energy = p_total * hours

    return ScenarioEnergyResult(
        n_pumps=n_pumps,
        pump=pump,
        p_total_shaft_kw=p_total,
        hours=hours,
        energy_kwh=energy,
    )


def compute_all_scenario_energies(
    results: list[SteadyStateResult],
    eta_pct: float = ETA_DUTY_PCT,
) -> list[ScenarioEnergyResult]:
    """Compute energy for all staging scenarios in one call."""
    return [
        compute_scenario_energy(r.n_active_pumps, r.q_per_pump_lps, r.h_pump_m, eta_pct)
        for r in results
    ]
