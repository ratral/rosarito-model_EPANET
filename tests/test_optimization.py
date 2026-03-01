"""Tests for VFD comparison module."""

from __future__ import annotations

import unittest

from rosarito.optimization import compute_vfd_comparison


class TestVFDComparison(unittest.TestCase):
    def test_4pump_speed_ratio_below_one(self):
        """At 4-pump design, pump is overpowered -> speed ratio < 1.0."""
        r = compute_vfd_comparison(
            n_pumps=4, phi_pct=44, q_total_lps=5017, h_pump_m=26.12, dh_riko_m=7.52
        )
        self.assertLess(r.speed_ratio, 1.0)

    def test_saving_positive(self):
        """Power saving must be positive for all scenarios."""
        cases = [
            (4, 44, 5017, 26.12, 7.52),
            (3, 38, 3664, 26.90, 8.50),
            (2, 30, 2221, 29.48, 11.22),
            (1, 22, 1014, 31.63, 13.44),
        ]
        for n, phi, q, h, dh in cases:
            r = compute_vfd_comparison(
                n_pumps=n, phi_pct=phi, q_total_lps=q, h_pump_m=h, dh_riko_m=dh
            )
            self.assertGreater(
                r.saving_total_kw, 0, f"phi={phi}%: saving must be positive"
            )

    def test_speed_ratio_above_minimum(self):
        """Speed ratio should never drop below 0.7 (practical VFD limit)."""
        cases = [
            (4, 44, 5017, 26.12, 7.52),
            (3, 38, 3664, 26.90, 8.50),
            (2, 30, 2221, 29.48, 11.22),
            (1, 22, 1014, 31.63, 13.44),
        ]
        for n, phi, q, h, dh in cases:
            r = compute_vfd_comparison(
                n_pumps=n, phi_pct=phi, q_total_lps=q, h_pump_m=h, dh_riko_m=dh
            )
            self.assertGreaterEqual(
                r.speed_ratio, 0.7, f"phi={phi}%: speed ratio below 0.7"
            )

    def test_affinity_law_consistency(self):
        """Verify speed_ratio = sqrt(H_required / H_pump)."""
        r = compute_vfd_comparison(
            n_pumps=4, phi_pct=44, q_total_lps=5017, h_pump_m=26.12, dh_riko_m=7.52
        )
        expected = ((26.12 - 7.52) / 26.12) ** 0.5
        self.assertAlmostEqual(r.speed_ratio, expected, places=4)


if __name__ == "__main__":
    unittest.main()
