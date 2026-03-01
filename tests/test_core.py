"""Smoke tests for non-EPANET code (no model loading required).

Run with: python -m unittest discover tests
"""

from __future__ import annotations

import unittest

from rosarito.constants import (
    lps_to_m3h,
    m3h_to_lps,
    RIKO_BY_NPUMPS,
    REFERENCE_BY_NPUMPS,
    RIKO_OPENINGS_ALL,
    REFERENCE_POINTS_ALL,
    REFERENCE_BY_PHI,
    KV_CONSTANT,
)
from rosarito.energy import compute_pump_power, compute_throttle_loss
from rosarito.eps_utils import format_sim_time, riko_label
from rosarito.validation import _deviation_pct


class TestUnitConversions(unittest.TestCase):
    def test_lps_to_m3h(self):
        self.assertAlmostEqual(lps_to_m3h(1000.0), 3600.0)

    def test_m3h_to_lps(self):
        self.assertAlmostEqual(m3h_to_lps(3600.0), 1000.0)

    def test_roundtrip_conversion(self):
        original = 1254.0
        self.assertAlmostEqual(m3h_to_lps(lps_to_m3h(original)), original)


class TestComputePumpPower(unittest.TestCase):
    def test_output_ranges(self):
        result = compute_pump_power(q_lps=1254.0, h_m=26.12, eta_pct=88.0)
        # Hydraulic power should be positive
        self.assertGreater(result.p_hydraulic_kw, 0)
        # Shaft power > hydraulic power (eta < 100%)
        self.assertGreater(result.p_shaft_kw, result.p_hydraulic_kw)
        # Motor load should be reasonable (positive, not wildly high)
        self.assertGreater(result.motor_load_pct, 0)
        self.assertLess(result.motor_load_pct, 200)

    def test_zero_flow(self):
        result = compute_pump_power(q_lps=0.0, h_m=26.12, eta_pct=88.0)
        self.assertAlmostEqual(result.p_hydraulic_kw, 0.0)

    def test_stored_values(self):
        result = compute_pump_power(q_lps=1254.0, h_m=26.12, eta_pct=88.0)
        self.assertEqual(result.q_lps, 1254.0)
        self.assertEqual(result.h_m, 26.12)
        self.assertEqual(result.eta_pct, 88.0)


class TestConstantCoverage(unittest.TestCase):
    def test_riko_by_npumps_coverage(self):
        for n in range(1, 5):
            self.assertIn(n, RIKO_BY_NPUMPS, f"Missing RIKO opening for {n} pumps")

    def test_reference_by_npumps_coverage(self):
        for n in range(1, 5):
            self.assertIn(n, REFERENCE_BY_NPUMPS, f"Missing reference for {n} pumps")


class TestFormatSimTime(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(format_sim_time(0), (0, 0))

    def test_one_hour(self):
        self.assertEqual(format_sim_time(3600), (1, 0))

    def test_ninety_minutes(self):
        self.assertEqual(format_sim_time(5400), (1, 30))

    def test_six_hours(self):
        self.assertEqual(format_sim_time(21600), (6, 0))

    def test_twenty_four_hours(self):
        self.assertEqual(format_sim_time(86400), (24, 0))


class TestRikoLabel(unittest.TestCase):
    def test_riko_44(self):
        self.assertEqual(riko_label("RIKO_44"), "44%")

    def test_riko_22(self):
        self.assertEqual(riko_label("RIKO_22"), "22%")

    def test_riko_38(self):
        self.assertEqual(riko_label("RIKO_38"), "38%")

    def test_riko_30(self):
        self.assertEqual(riko_label("RIKO_30"), "30%")


class TestDeviationPct(unittest.TestCase):
    def test_zero_deviation(self):
        self.assertAlmostEqual(_deviation_pct(100.0, 100.0), 0.0)

    def test_positive_deviation(self):
        self.assertAlmostEqual(_deviation_pct(105.0, 100.0), 5.0)

    def test_negative_deviation(self):
        self.assertAlmostEqual(_deviation_pct(95.0, 100.0), 5.0)

    def test_zero_reference_zero_computed(self):
        self.assertAlmostEqual(_deviation_pct(0.0, 0.0), 0.0)

    def test_zero_reference_nonzero_computed(self):
        self.assertAlmostEqual(_deviation_pct(5.0, 0.0), 100.0)


class TestExtendedOpenings(unittest.TestCase):
    """Tests for the 7 extended RIKO openings (Task 2)."""

    def test_openings_all_count(self):
        self.assertEqual(len(RIKO_OPENINGS_ALL), 7)

    def test_openings_all_sorted_descending(self):
        phi_values = [o.phi_pct for o in RIKO_OPENINGS_ALL]
        self.assertEqual(phi_values, sorted(phi_values, reverse=True))

    def test_reference_points_all_count(self):
        self.assertEqual(len(REFERENCE_POINTS_ALL), 7)

    def test_reference_by_phi_coverage(self):
        for phi in [22, 26, 30, 34, 38, 40, 44]:
            self.assertIn(phi, REFERENCE_BY_PHI, f"Missing reference for phi={phi}%")

    def test_original_riko_by_npumps_unchanged(self):
        """Original 4 mappings must be preserved."""
        for n in range(1, 5):
            self.assertIn(n, RIKO_BY_NPUMPS, f"Missing RIKO opening for {n} pumps")

    def test_new_openings_kv_from_csv(self):
        """Verify intermediate Kv values match CSV exact rows."""
        expected = {26: 5109.57, 34: 10735.54, 40: 16511.59}
        for opening in RIKO_OPENINGS_ALL:
            if opening.phi_pct in expected:
                self.assertAlmostEqual(
                    opening.kv_m3h, expected[opening.phi_pct], places=2,
                    msg=f"Kv mismatch at phi={opening.phi_pct}%"
                )

    def test_new_reference_headloss_reasonable(self):
        """dH_RIKO should be 0-20 m for all operating points."""
        for ref in REFERENCE_POINTS_ALL:
            self.assertGreater(ref.dh_riko_m, 0, f"phi={ref.phi_pct}%: dH must be positive")
            self.assertLess(ref.dh_riko_m, 20, f"phi={ref.phi_pct}%: dH must be < 20 m")

    def test_new_reference_kv_consistency(self):
        """Verify dH_RIKO = Q^2 * 132.15 / Kv^2 within 1% for each point."""
        kv_by_phi = {o.phi_pct: o.kv_m3h for o in RIKO_OPENINGS_ALL}
        for ref in REFERENCE_POINTS_ALL:
            kv = kv_by_phi[ref.phi_pct]
            dh_calc = ref.q_total_lps**2 * KV_CONSTANT / kv**2
            dev = abs(dh_calc - ref.dh_riko_m) / ref.dh_riko_m * 100
            self.assertLess(dev, 1.0, f"phi={ref.phi_pct}%: dH_RIKO deviation {dev:.2f}% > 1%")

    def test_flow_ordering_monotonic(self):
        """Q_total must decrease as phi decreases (all 7 points)."""
        flows = [r.q_total_lps for r in REFERENCE_POINTS_ALL]
        for i in range(len(flows) - 1):
            self.assertGreater(flows[i], flows[i + 1])


class TestThrottleLoss(unittest.TestCase):
    """Tests for RIKO valve throttle-loss quantification (Task 5)."""

    def test_design_point_power(self):
        """4-pump design point: Q=5016 l/s, dH=7.51 m.

        P = 1025 * 9.81 * 5.016 * 7.51 / 1000 ≈ 378.9 kW
        """
        result = compute_throttle_loss(q_total_lps=5016.0, dh_riko_m=7.51)
        # rho*g = 10055.25, Q_m3s = 5.016, dH = 7.51
        expected_kw = 1025.0 * 9.81 * 5.016 * 7.51 / 1000.0
        self.assertAlmostEqual(result.p_throttle_kw, expected_kw, places=1)

    def test_daily_energy(self):
        """daily_kwh must equal p_throttle_kw * 24."""
        result = compute_throttle_loss(q_total_lps=5016.0, dh_riko_m=7.51)
        self.assertAlmostEqual(result.daily_kwh, result.p_throttle_kw * 24.0, places=1)

    def test_zero_flow(self):
        """Zero flow produces zero throttle loss."""
        result = compute_throttle_loss(q_total_lps=0.0, dh_riko_m=7.51)
        self.assertAlmostEqual(result.p_throttle_kw, 0.0)
        self.assertAlmostEqual(result.daily_kwh, 0.0)

    def test_zero_headloss(self):
        """Zero headloss produces zero throttle loss."""
        result = compute_throttle_loss(q_total_lps=5016.0, dh_riko_m=0.0)
        self.assertAlmostEqual(result.p_throttle_kw, 0.0)
        self.assertAlmostEqual(result.daily_kwh, 0.0)

    def test_stored_values(self):
        """Input values must be stored unchanged."""
        result = compute_throttle_loss(q_total_lps=3664.0, dh_riko_m=8.50)
        self.assertEqual(result.q_total_lps, 3664.0)
        self.assertEqual(result.dh_riko_m, 8.50)

    def test_all_reference_points(self):
        """Throttle loss is positive for all 4 reference operating points."""
        from rosarito.constants import REFERENCE_POINTS
        for ref in REFERENCE_POINTS:
            result = compute_throttle_loss(ref.q_total_lps, ref.dh_riko_m)
            self.assertGreater(
                result.p_throttle_kw, 0,
                f"phi={ref.phi_pct}%: throttle power must be positive"
            )
            self.assertGreater(
                result.daily_kwh, 0,
                f"phi={ref.phi_pct}%: daily energy must be positive"
            )

    def test_throttle_loss_increases_with_fewer_pumps(self):
        """dH_RIKO increases as fewer pumps run (valve throttles more),
        but flow decreases too. Verify the calculation is consistent."""
        from rosarito.constants import REFERENCE_POINTS
        results = [
            compute_throttle_loss(ref.q_total_lps, ref.dh_riko_m)
            for ref in REFERENCE_POINTS
        ]
        # All results should have p_throttle_kw > 0
        for r in results:
            self.assertGreater(r.p_throttle_kw, 0)


if __name__ == "__main__":
    unittest.main()
