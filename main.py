"""Rosarito Desalination Plant — EPANET hydraulic model automation.

Usage:
    python main.py              # Run all analyses
    python main.py staging      # Steady-state staging only
    python main.py energy       # Energy post-processing only
    python main.py eps          # 24h EPS with pump trips only
    python main.py report       # Generate Markdown report → reports/scenarios_report.md
    python main.py report path  # Generate report to custom path
    python main.py quarto       # Render Quarto PDF report → reports/report.pdf
"""

from __future__ import annotations

import subprocess
import sys

from rosarito.constants import INP_FILE
from rosarito.scenarios import run_staging_scenarios, run_eps_with_trips
from rosarito.energy import compute_all_scenario_energies
from rosarito.validation import validate_all_scenarios
from rosarito.reporting import (
    print_staging_table,
    print_validation_report,
    print_energy_table,
    print_eps_summary,
)
from rosarito.report import generate_report


def run_staging() -> None:
    """Run steady-state staging scenarios with validation."""
    print(f"\nLoading model: {INP_FILE}")
    results = run_staging_scenarios()
    print_staging_table(results)

    validations = validate_all_scenarios(results)
    print_validation_report(validations)


def run_energy() -> None:
    """Run energy post-processing based on staging results."""
    print(f"\nLoading model: {INP_FILE}")
    results = run_staging_scenarios()

    print_energy_table(compute_all_scenario_energies(results))


def run_eps() -> None:
    """Run 24h EPS with scheduled pump trips."""
    print(f"\nLoading model: {INP_FILE}")
    eps = run_eps_with_trips()
    print_eps_summary(eps)


def run_report() -> None:
    """Generate Markdown report with all analyses."""
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    generate_report(output_path)


def run_quarto() -> None:
    """Render the Quarto PDF report."""
    from pathlib import Path

    qmd = Path(__file__).resolve().parent / "reports" / "report.qmd"
    if not qmd.exists():
        print(f"Error: {qmd} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Rendering Quarto report: {qmd}")
    result = subprocess.run(
        ["quarto", "render", str(qmd)],
        cwd=str(qmd.parent),
    )
    if result.returncode != 0:
        print("Quarto render failed.", file=sys.stderr)
        sys.exit(result.returncode)
    print(f"Report written to: {qmd.with_suffix('.pdf')}")


def main() -> None:
    commands = {
        "staging": run_staging,
        "energy": run_energy,
        "eps": run_eps,
        "report": run_report,
        "quarto": run_quarto,
    }

    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd in commands:
            try:
                commands[cmd]()
            except Exception as exc:
                print(f"\nError running '{cmd}': {exc}", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Unknown command: {cmd}")
            print(f"Available: {', '.join(commands)} (or no argument for all)")
            sys.exit(1)
    else:
        # Run all analyses
        try:
            run_staging()
            run_energy()
            run_eps()
        except Exception as exc:
            print(f"\nError: {exc}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
