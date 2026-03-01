"""VFD comparison: theoretical pump speed reduction to eliminate RIKO throttling.

Compares fixed-speed pump + throttling valve vs variable-frequency drive (VFD)
operating the pump at reduced speed. Uses affinity laws:
  Q ~ N/N_rated,  H ~ (N/N_rated)^2,  P ~ (N/N_rated)^3
"""

from __future__ import annotations

from dataclasses import dataclass

from rosarito.constants import (
    RHO_SEAWATER,
    G,
    H_PLANT,
    MOTOR_POWER_KW,
    ETA_DUTY_PCT,
    H_RATED_M,
    Q_RATED_LPS,
    H_SHUTOFF_M,
)


@dataclass
class VFDResult:
    """VFD comparison for one operating point."""

    n_pumps: int
    phi_pct: int
    q_total_lps: float
    q_per_pump_lps: float
    # Throttled (fixed speed)
    h_pump_throttled_m: float
    p_shaft_throttled_kw: float  # per pump
    # VFD (variable speed, no valve loss)
    speed_ratio: float  # N/N_rated (< 1.0 means slower)
    h_pump_vfd_m: float
    p_shaft_vfd_kw: float  # per pump
    # Savings
    saving_per_pump_kw: float
    saving_total_kw: float
    saving_pct: float


def compute_vfd_comparison(
    n_pumps: int,
    phi_pct: int,
    q_total_lps: float,
    h_pump_m: float,
    dh_riko_m: float,
    eta_pct: float = ETA_DUTY_PCT,
) -> VFDResult:
    """Compare throttled vs VFD operation at one operating point.

    Without the RIKO valve, the pump only needs to overcome:
        H_required = H_pump - dH_RIKO
    Using the simple affinity law approximation (valid near BEP):
        speed_ratio = sqrt(H_required / H_pump)

    Args:
        n_pumps: Number of active pumps.
        phi_pct: RIKO valve opening (%).
        q_total_lps: Total system flow in l/s.
        h_pump_m: Pump head at this operating point in m.
        dh_riko_m: Head loss across the RIKO valve in m.
        eta_pct: Pump efficiency in %.
    """
    q_per_pump = q_total_lps / n_pumps

    # --- Throttled shaft power per pump ---
    q_m3s = q_per_pump / 1000.0
    p_hyd_throttled = RHO_SEAWATER * G * q_m3s * h_pump_m / 1000.0
    p_shaft_throttled = p_hyd_throttled / (eta_pct / 100.0)

    # --- H_required without valve = H_pump - dH_RIKO ---
    h_required = h_pump_m - dh_riko_m

    # --- Affinity law: speed ratio = sqrt(H_required / H_pump) ---
    # At rated speed, the pump delivers (q_per_pump, h_pump_m).
    # At speed ratio r, the same dimensionless point maps to
    # (q_per_pump*r, h_pump_m*r^2).
    # We want to find r such that at flow q_per_pump the pump delivers h_required.
    # Simple approximation (valid when operating near BEP):
    speed_ratio = (h_required / h_pump_m) ** 0.5
    h_pump_vfd = h_required

    # --- VFD shaft power: P_hyd_vfd = rho * g * Q * H_required / 1000 ---
    p_hyd_vfd = RHO_SEAWATER * G * q_m3s * h_required / 1000.0
    p_shaft_vfd = p_hyd_vfd / (eta_pct / 100.0)

    saving_per_pump = p_shaft_throttled - p_shaft_vfd
    saving_total = saving_per_pump * n_pumps
    saving_pct = (
        saving_per_pump / p_shaft_throttled * 100.0
        if p_shaft_throttled > 0
        else 0.0
    )

    return VFDResult(
        n_pumps=n_pumps,
        phi_pct=phi_pct,
        q_total_lps=q_total_lps,
        q_per_pump_lps=q_per_pump,
        h_pump_throttled_m=h_pump_m,
        p_shaft_throttled_kw=p_shaft_throttled,
        speed_ratio=speed_ratio,
        h_pump_vfd_m=h_pump_vfd,
        p_shaft_vfd_kw=p_shaft_vfd,
        saving_per_pump_kw=saving_per_pump,
        saving_total_kw=saving_total,
        saving_pct=saving_pct,
    )
