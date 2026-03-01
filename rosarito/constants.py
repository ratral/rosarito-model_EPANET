"""Design parameters and EPANET element IDs for the Rosarito intake system.

All values sourced from ROSARITO_Project_Instructions.md (v2, 28/02/2026).
Section references noted inline.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
INP_FILE = _PROJECT_ROOT / "inp_files" / "ROSARITO_EPANET_Rev2.inp"
INP_FILE_REV3 = _PROJECT_ROOT / "inp_files" / "ROSARITO_EPANET_Rev3.inp"
RIKO_CSV = _PROJECT_ROOT / "data" / "riko_cylinder_e_dn1800.csv"

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------
RHO_SEAWATER = 1025.0       # kg/m³  — seawater at 20 °C
G = 9.81                    # m/s²
KV_CONSTANT = 132.15        # 3.6² × 10.197 — ISO 5167 Kv headloss constant
SG = 1.025                  # specific gravity
RELATIVE_VISCOSITY = 1.050  # ν_seawater / ν_water

# ---------------------------------------------------------------------------
# Pump parameters — Ruhrpumpen 35WX (Section 3.1)
# ---------------------------------------------------------------------------
N_TOTAL_PUMPS = 5           # 4 duty + 1 standby
N_DUTY_PUMPS = 4
Q_RATED_LPS = 1256.0        # l/s per pump
H_RATED_M = 26.07           # m — effective rated head
H_SHUTOFF_M = 46.54         # m — shutoff head
ETA_BEP_PCT = 89.0          # % — efficiency at BEP
ETA_DUTY_PCT = 88.0         # % — efficiency at duty point
Q_BEP_BOWL_LPS = 1237.0     # l/s — BEP bowl flow
Q_MIN_STABLE_LPS = 845.4    # l/s — min stable continuous flow (ANSI/HI 9.6.3)
MOTOR_POWER_KW = 447.0      # kW — motor nameplate
MOTOR_SERVICE_FACTOR = 1.15
PUMP_SPEED_RPM = 885        # rpm at 60 Hz

# ---------------------------------------------------------------------------
# Valve parameters — VAG RIKO DN1800 (Section 3.2)
# ---------------------------------------------------------------------------
VAG_QMIN_M3H = 4500.0       # m³/h — minimum operating flow per VAG sizing
VAG_QMAX_M3H = 18000.0      # m³/h — maximum operating flow per VAG sizing


@dataclass(frozen=True)
class RikoOpening:
    """Operating point for a specific RIKO valve opening."""
    phi_pct: int             # valve opening %
    kv_m3h: float            # flow coefficient Kv (m³/h)
    n_pumps: int             # number of active pumps
    gpv_link_id: str         # EPANET GPV link ID
    curve_id: str            # EPANET GPV curve ID


# ---------------------------------------------------------------------------
# RIKO openings — all 7 points (original 4 + 3 intermediate: phi=40%, 34%, 26%)
# Kv values: exact rows from riko_cylinder_e_dn1800.csv (2% steps)
# Intermediate openings allow finer throttling control per pump count.
# ---------------------------------------------------------------------------
RIKO_OPENINGS_ALL: list[RikoOpening] = [
    RikoOpening(phi_pct=44, kv_m3h=21038.45, n_pumps=4,
                gpv_link_id="RIKO_44", curve_id="RIKO_44pct"),
    RikoOpening(phi_pct=40, kv_m3h=16511.59, n_pumps=4,
                gpv_link_id="RIKO_40", curve_id="RIKO_40pct"),
    RikoOpening(phi_pct=38, kv_m3h=14444.21, n_pumps=3,
                gpv_link_id="RIKO_38", curve_id="RIKO_38pct"),
    RikoOpening(phi_pct=34, kv_m3h=10735.54, n_pumps=3,
                gpv_link_id="RIKO_34", curve_id="RIKO_34pct"),
    RikoOpening(phi_pct=30, kv_m3h=7621.47,  n_pumps=2,
                gpv_link_id="RIKO_30", curve_id="RIKO_30pct"),
    RikoOpening(phi_pct=26, kv_m3h=5109.57,  n_pumps=2,
                gpv_link_id="RIKO_26", curve_id="RIKO_26pct"),
    RikoOpening(phi_pct=22, kv_m3h=3179.78,  n_pumps=1,
                gpv_link_id="RIKO_22", curve_id="RIKO_22pct"),
]

# Original 4 openings (one per pump count) — derived from canonical list
_ORIGINAL_PHI = {44, 38, 30, 22}
RIKO_OPENINGS: list[RikoOpening] = [
    o for o in RIKO_OPENINGS_ALL if o.phi_pct in _ORIGINAL_PHI
]

# Lookup by n_pumps for convenience
RIKO_BY_NPUMPS: dict[int, RikoOpening] = {r.n_pumps: r for r in RIKO_OPENINGS}

# ---------------------------------------------------------------------------
# EPANET element IDs
# ---------------------------------------------------------------------------
PUMP_IDS = ["PUMP_1", "PUMP_2", "PUMP_3", "PUMP_4", "PUMP_5"]
DUTY_PUMP_IDS = ["PUMP_1", "PUMP_2", "PUMP_3", "PUMP_4"]
STANDBY_PUMP_ID = "PUMP_5"

RIKO_IDS = ["RIKO_44", "RIKO_38", "RIKO_30", "RIKO_22"]
RIKO_IDS_ALL = ["RIKO_44", "RIKO_40", "RIKO_38", "RIKO_34", "RIKO_30", "RIKO_26", "RIKO_22"]

PIPE_IDS = ["P_INTAKE", "P_US", "P_DS_1", "P_DS_2", "P_DS_3", "P_DS_4"]
PIPE_IDS_REV2 = ["P_INTAKE", "P_US", "P_DS"]
PIPE_DS_IDS = ["P_DS_1", "P_DS_2", "P_DS_3", "P_DS_4"]

JUNCTION_IDS = ["J_SUCTION", "J_MANIFOLD", "J_RIKO_IN", "J_RIKO_OUT",
                "J_DS_1", "J_DS_2", "J_DS_3"]
JUNCTION_IDS_REV2 = ["J_SUCTION", "J_MANIFOLD", "J_RIKO_IN", "J_RIKO_OUT"]
JUNCTION_DS_IDS = ["J_DS_1", "J_DS_2", "J_DS_3"]
RESERVOIR_IDS = ["SEA", "PLANT"]

# Reservoirs
H_SEA = 0.0                 # m — MSL datum
H_PLANT = 18.17             # m — back-calculated forebay head

# Pipe diameters for velocity calculation
PIPE_DN_MM = {
    "P_INTAKE": 2500.0,
    "P_US": 1800.0,
    "P_DS_1": 1800.0,
    "P_DS_2": 1800.0,
    "P_DS_3": 1800.0,
    "P_DS_4": 1800.0,
}

# ---------------------------------------------------------------------------
# Reference operating points — Section 5, hand-calculated (Newton iteration)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ReferenceOperatingPoint:
    """Hand-calculated operating point for validation."""
    phi_pct: int
    n_pumps: int
    q_total_lps: float
    q_total_m3h: float
    q_per_pump_lps: float
    h_pump_m: float
    dh_riko_m: float
    v_pipe_ms: float


# ---------------------------------------------------------------------------
# Reference operating points — hand-calculated (Newton iteration)
# All 7 points (Section 5 + 3 intermediate openings).
# Pump curve: H = 46.54 - 5.300e-4 * Q^1.480 (Ruhrpumpen 35WX, Rev2)
# Pipe friction: Darcy-Weisbach with Colebrook-White, nu=1.05e-6 m^2/s
# ---------------------------------------------------------------------------
REFERENCE_POINTS_ALL: list[ReferenceOperatingPoint] = [
    ReferenceOperatingPoint(
        phi_pct=44, n_pumps=4,
        q_total_lps=5016.0, q_total_m3h=18059.0,
        q_per_pump_lps=1254.0, h_pump_m=26.12,
        dh_riko_m=7.51, v_pipe_ms=1.971,
    ),
    ReferenceOperatingPoint(
        phi_pct=40, n_pumps=4,
        q_total_lps=4577.5, q_total_m3h=16479.0,
        q_per_pump_lps=1144.4, h_pump_m=28.72,
        dh_riko_m=10.16, v_pipe_ms=1.799,
    ),
    ReferenceOperatingPoint(
        phi_pct=38, n_pumps=3,
        q_total_lps=3664.0, q_total_m3h=13189.0,
        q_per_pump_lps=1221.0, h_pump_m=26.90,
        dh_riko_m=8.50, v_pipe_ms=1.440,
    ),
    ReferenceOperatingPoint(
        phi_pct=34, n_pumps=3,
        q_total_lps=3224.8, q_total_m3h=11609.0,
        q_per_pump_lps=1074.9, h_pump_m=30.30,
        dh_riko_m=11.92, v_pipe_ms=1.267,
    ),
    ReferenceOperatingPoint(
        phi_pct=30, n_pumps=2,
        q_total_lps=2221.0, q_total_m3h=7996.0,
        q_per_pump_lps=1111.0, h_pump_m=29.48,
        dh_riko_m=11.22, v_pipe_ms=0.873,
    ),
    ReferenceOperatingPoint(
        phi_pct=26, n_pumps=2,
        q_total_lps=1779.3, q_total_m3h=6405.0,
        q_per_pump_lps=889.7, h_pump_m=34.26,
        dh_riko_m=16.03, v_pipe_ms=0.699,
    ),
    ReferenceOperatingPoint(
        phi_pct=22, n_pumps=1,
        q_total_lps=1014.0, q_total_m3h=3651.0,
        q_per_pump_lps=1014.0, h_pump_m=31.63,
        dh_riko_m=13.44, v_pipe_ms=0.398,
    ),
]

# Original 4 reference points (one per pump count) — derived from canonical list
REFERENCE_POINTS: list[ReferenceOperatingPoint] = [
    r for r in REFERENCE_POINTS_ALL if r.phi_pct in _ORIGINAL_PHI
]

REFERENCE_BY_NPUMPS: dict[int, ReferenceOperatingPoint] = {
    r.n_pumps: r for r in REFERENCE_POINTS
}

REFERENCE_BY_PHI: dict[int, ReferenceOperatingPoint] = {
    r.phi_pct: r for r in REFERENCE_POINTS_ALL
}

# ---------------------------------------------------------------------------
# Unit conversion helpers
# ---------------------------------------------------------------------------

def lps_to_m3h(q_lps: float) -> float:
    """Convert liters/second to m³/hour."""
    return q_lps * 3.6


def m3h_to_lps(q_m3h: float) -> float:
    """Convert m³/hour to liters/second."""
    return q_m3h / 3.6
