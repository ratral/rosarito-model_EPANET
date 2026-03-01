"""Tests for VFD comparison module."""

from __future__ import annotations

import unittest

from rosarito.constants import ReferenceOperatingPoint
from rosarito.optimization import compute_vfd_comparison


def _make_ref(n: int, phi: int, q: float, h: float, dh: float) -> ReferenceOperatingPoint:
    """Build a minimal ReferenceOperatingPoint for testing."""
    return ReferenceOperatingPoint(
        phi_pct=phi, n_pumps=n,
        q_total_lps=q, q_total_m3h=q * 3.6,
        q_per_pump_lps=q / n, h_pump_m=h,
        dh_riko_m=dh, v_pipe_ms=0.0,
    )


# Shared test cases: (n_pumps, phi%, Q_total, H_pump, dH_RIKO)
_CASES = [
    (4, 44, 5017, 26.12, 7.52),
    (3, 38, 3664, 26.90, 8.50),
    (2, 30, 2221, 29.48, 11.22),
    (1, 22, 1014, 31.63, 13.44),
]


class TestVFDComparison(unittest.TestCase):
    def test_4pump_speed_ratio_below_one(self):
        """At 4-pump design, pump is overpowered -> speed ratio < 1.0."""
        r = compute_vfd_comparison(_make_ref(4, 44, 5017, 26.12, 7.52))
        self.assertLess(r.speed_ratio, 1.0)

    def test_saving_positive(self):
        """Power saving must be positive for all scenarios."""
        for n, phi, q, h, dh in _CASES:
            r = compute_vfd_comparison(_make_ref(n, phi, q, h, dh))
            self.assertGreater(
                r.saving_total_kw, 0, f"phi={phi}%: saving must be positive"
            )

    def test_speed_ratio_above_minimum(self):
        """Speed ratio should never drop below 0.7 (practical VFD limit)."""
        for n, phi, q, h, dh in _CASES:
            r = compute_vfd_comparison(_make_ref(n, phi, q, h, dh))
            self.assertGreaterEqual(
                r.speed_ratio, 0.7, f"phi={phi}%: speed ratio below 0.7"
            )

    def test_affinity_law_consistency(self):
        """Verify speed_ratio = sqrt(H_required / H_pump)."""
        r = compute_vfd_comparison(_make_ref(4, 44, 5017, 26.12, 7.52))
        expected = ((26.12 - 7.52) / 26.12) ** 0.5
        self.assertAlmostEqual(r.speed_ratio, expected, places=4)


if __name__ == "__main__":
    unittest.main()
