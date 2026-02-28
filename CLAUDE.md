# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hydraulic model of the Rosarito Desalination Plant seawater intake system (Baja California, México). Models the interaction between 5 vertical centrifugal pumps (Ruhrpumpen 35WX), a VAG RIKO DN1800 plunger control valve, and the piping system using EPANET 2.2.

**Client:** CONAGUA / AYESA S.A. de C.V.
**Engineer:** Dr. Raúl Trujillo (VAG GmbH)

## Setup and Commands

```bash
# Python version
python --version  # Requires >= 3.11 (see .python-version)

# Install (creates venv + installs epyt dependency)
uv venv && source .venv/bin/activate && uv pip install -e .

# Run all analyses (staging + energy + EPS)
python main.py

# Run individual analyses
python main.py staging      # Steady-state staging scenarios with validation
python main.py energy       # Energy post-processing (power, kWh)
python main.py eps          # 24h EPS with scheduled pump trips
```

No test suite or linter configured. The project uses `pyproject.toml` (uv/pip compatible). Automation toolkit: **EPyT** (EPANET Python Toolkit by OpenWaterAnalytics).

## Architecture

### Repository Layout

- `ROSARITO_Project_Instructions.md` — **Master specification.** All confirmed parameters, modeling decisions, and open items. This document takes precedence when values conflict with other files.
- `inp_files/` — EPANET `.inp` model files (Rev0, Rev1, Rev2). `ROSARITO_EPANET_Rev2.inp` is the current production model. **Never modified by Python code.**
- `data/` — Supporting data: `riko_cylinder_e_dn1800.csv` (valve Kv values), `ruhrpumpen_35wx_characteristics.md` (pump datasheet extraction), `report_2.md` (engineering report).
- `docs/` — Reference PDFs (pump datasheet, valve sizing report, CCWI 2015 control paper, system questionnaire).
- `main.py` — Entry point for automated analyses (staging, energy, EPS).
- `rosarito/` — Python package (EPyT-based automation):
  - `constants.py` — All design parameters, element IDs, reference operating points from Project Instructions.
  - `model.py` — `RosaritoModel` class wrapping EPyT; domain accessors and result dataclasses.
  - `scenarios.py` — Steady-state staging (4 scenarios) and 24h EPS with pump trips.
  - `energy.py` — Pump power (P_hyd, P_shaft, motor load%) and 24h energy calculations.
  - `validation.py` — Compares EPANET results vs hand-calculated reference (Section 5); flags >5% deviations.
  - `reporting.py` — Formatted console tables for engineering review.

### System Topology (EPANET Network)

```
SEA (H=0m) → P_INTAKE → J_SUCTION → PUMP_1..5 (parallel) → J_MANIFOLD
→ P_US → J_RIKO_IN → RIKO_44/38/30/22 (4 parallel GPV) → J_RIKO_OUT
→ P_DS → PLANT (H=18.17m)
```

- **Pumps:** 4 duty + 1 standby (N+1). Rule-based staging with PRIORITY 10 standby activation.
- **Valve:** 4 parallel GPV links model different RIKO openings (22%, 30%, 38%, 44%). Only one GPV is open at a time — this is the standard EPANET workaround because rules cannot swap curve IDs dynamically.
- **Control logic:** 13 rule blocks in `[RULES]` section, priority-ordered per Georgescu et al. (CCWI 2015).

## Critical Technical Constraints

1. **Valve headloss formula:** Always use `ΔH = Q²×132.15/Kv²` (ISO 5167 Kv method). **Never** use the `zeta_value` column from the CSV with Darcy-Weisbach `ΔH = ζ×v²/(2g)` — VAG's ζ is a non-standard internal parameter.

2. **Units:** LPS (liters per second) in EPANET. SI internally in Python; convert to l/s or m³/h for display.

3. **Friction:** Darcy-Weisbach only (large-diameter pipes, Re > 10⁶).

4. **H_PLANT = 18.17 m** is back-calculated, not field-measured. All operating points shift if this value changes.

5. **1-pump scenario** produces Q < VAG Qmin (4,500 m³/h). This is a known system characteristic, not a modeling error.

6. **Modeling decisions in Section 6 of `ROSARITO_Project_Instructions.md` are locked.** Do not re-debate unless explicitly flagged as superseded.

## Working Conventions

- **Language:** English. Spanish technical labels from source documents are kept as-is.
- **Code style:** Domain-driven design — model objects map to physical equipment.
- **INP files:** Include inline comments citing sources (CSV row, datasheet field, calculated, or estimated). Revision number and date in `[TITLE]`.
- **Review standard:** Flag calculated results deviating >5% from manufacturer data. State confidence levels.
- **Decisions log:** Append new modeling decisions to Section 6 of `ROSARITO_Project_Instructions.md`. Mark superseded decisions with `[SUPERSEDED — date]`. Never delete.
- **Pump trips in EPS:** Add to `[CONTROLS]` section, never modify `[RULES]`.
