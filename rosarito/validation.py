"""Validation of computed results vs hand-calculated reference points.

Compares EPANET solver output against Section 5 of Project Instructions.
Flags deviations > 5% per review standard (Section 11).
"""

from __future__ import annotations

from dataclasses import dataclass, field

from rosarito.constants import (
    Q_MIN_STABLE_LPS,
    VAG_QMIN_M3H,
    REFERENCE_BY_NPUMPS,
    REFERENCE_BY_PHI,
    ReferenceOperatingPoint,
    lps_to_m3h,
)
from rosarito.model import SteadyStateResult


TOLERANCE_PCT = 5.0  # Flag deviations > 5%


@dataclass
class ParameterCheck:
    """Result of comparing one parameter against its reference."""
    name: str
    computed: float
    reference: float
    deviation_pct: float
    passed: bool
    unit: str = ""


@dataclass
class ScenarioValidation:
    """Validation results for one staging scenario."""
    n_pumps: int
    phi_pct: int
    checks: list[ParameterCheck] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def all_passed(self) -> bool:
        return all(c.passed for c in self.checks)


def _deviation_pct(computed: float, reference: float) -> float:
    if reference == 0:
        return 0.0 if computed == 0 else 100.0
    return abs(computed - reference) / abs(reference) * 100.0


def _check(
    name: str, computed: float, reference: float, unit: str = "",
) -> ParameterCheck:
    dev = _deviation_pct(computed, reference)
    return ParameterCheck(
        name=name,
        computed=computed,
        reference=reference,
        deviation_pct=dev,
        passed=dev <= TOLERANCE_PCT,
        unit=unit,
    )


def validate_steady_state(
    result: SteadyStateResult,
    ref: ReferenceOperatingPoint | None = None,
) -> ScenarioValidation:
    """Validate one computed scenario against a hand-calculated reference.

    If *ref* is not provided, looks up by n_active_pumps in REFERENCE_BY_NPUMPS.
    """
    if ref is None:
        ref = REFERENCE_BY_NPUMPS.get(result.n_active_pumps)
    if ref is None:
        return ScenarioValidation(
            n_pumps=result.n_active_pumps,
            phi_pct=result.riko_opening_pct,
            warnings=[f"No reference point for {result.n_active_pumps}-pump scenario"],
        )

    val = ScenarioValidation(
        n_pumps=result.n_active_pumps,
        phi_pct=result.riko_opening_pct,
    )

    val.checks.append(_check("Q_total", result.q_total_lps, ref.q_total_lps, "l/s"))
    val.checks.append(_check("Q/pump", result.q_per_pump_lps, ref.q_per_pump_lps, "l/s"))
    val.checks.append(_check("H_pump", result.h_pump_m, ref.h_pump_m, "m"))
    val.checks.append(_check("dH_RIKO", result.dh_riko_m, ref.dh_riko_m, "m"))

    # Check minimum stable flow
    if result.q_per_pump_lps < Q_MIN_STABLE_LPS:
        val.warnings.append(
            f"Q/pump = {result.q_per_pump_lps:.1f} l/s < min stable "
            f"({Q_MIN_STABLE_LPS} l/s)"
        )

    # Check VAG Qmin
    q_total_m3h = lps_to_m3h(result.q_total_lps)
    if q_total_m3h < VAG_QMIN_M3H:
        val.warnings.append(
            f"Q_total = {q_total_m3h:.0f} m3/h < VAG Qmin ({VAG_QMIN_M3H:.0f} m3/h) "
            f"— known system characteristic for {result.n_active_pumps}-pump"
        )

    return val


def validate_all_scenarios(
    results: list[SteadyStateResult],
) -> list[ScenarioValidation]:
    """Validate all staging scenarios."""
    return [validate_steady_state(r) for r in results]


def validate_all_extended(
    results: list[SteadyStateResult],
) -> list[ScenarioValidation]:
    """Validate all 7 extended staging scenarios (lookup by phi%)."""
    return [
        validate_steady_state(r, ref=REFERENCE_BY_PHI.get(r.riko_opening_pct))
        for r in results
    ]
