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
)
from rosarito.energy import compute_pump_power
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


if __name__ == "__main__":
    unittest.main()
