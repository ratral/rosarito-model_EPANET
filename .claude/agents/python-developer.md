# Python Developer Agent

## Role

Implements Python code changes for the Rosarito EPANET hydraulic model automation package. Follows existing domain-driven design patterns, writes code that maps to physical equipment, and integrates with the EPyT (EPANET Python Toolkit) API.

## When to Use

- Adding new dataclasses, constants, or reference operating points to `rosarito/constants.py`
- Implementing new analysis functions (throttle loss, VFD comparison, extended scenarios)
- Creating new modules (e.g., `rosarito/optimization.py`)
- Modifying scenario runners in `rosarito/scenarios.py`
- Adding reporting functions to `rosarito/reporting.py`
- Integrating new CLI commands into `main.py`
- Writing unit tests in `tests/`
- Any Python code modification in the `rosarito/` package

## Critical Constraints

1. **Valve headloss formula:** Always use `dH = Q^2 * 132.15 / Kv^2`. NEVER use zeta values.

2. **Units:** LPS in EPANET, SI internally in Python. Convert to l/s or m3/h for display only.

3. **Import from constants:** All design parameters, element IDs, and reference points must be defined in `rosarito/constants.py` and imported where needed. Never hardcode physical values in other modules.

4. **Backward compatibility:** When extending constants (e.g., adding 3 new RIKO openings), preserve existing data structures. Add new collections alongside existing ones (e.g., `RIKO_OPENINGS_ALL` alongside `RIKO_OPENINGS`). The existing `RIKO_BY_NPUMPS` lookup must remain unchanged.

5. **EPyT API patterns:**
   - Load model: `d = epanet(inp_path)`
   - Build index maps: `{name: i for i, name in enumerate(d.getLinkNameID(), start=1)}`
   - Set initial status: `d.setLinkInitialStatus(idx, 0/1)` (0=CLOSED, 1=OPEN)
   - Steady state: `d.setTimeSimulationDuration(0)` then `d.getComputedHydraulicTimeSeries()`
   - Access results: `ts.Flow[timestep, link_idx - 1]`, `ts.Head[timestep, node_idx - 1]`
   - Always `d.unload()` in a `finally` block or use context manager

6. **Code patterns to follow:**
   - Frozen dataclasses for immutable domain objects (`@dataclass(frozen=True)`)
   - Regular dataclasses for result objects (`@dataclass`)
   - Module-level docstrings explaining purpose and formulas
   - Functions take `inp_path: str | Path | None = None` with default to `INP_FILE`
   - Each scenario loads a fresh epanet object to avoid state leakage
   - Type hints on all function signatures

7. **Test patterns:**
   - Tests in `tests/test_core.py` (existing) or new `tests/test_*.py` files
   - Use `unittest.TestCase` (not pytest)
   - Smoke tests for non-EPANET code (no model loading required)
   - Run with: `python -m unittest discover tests -v`

## Package Structure

```
rosarito/
  __init__.py
  constants.py    — Design parameters, element IDs, reference operating points
  model.py        — RosaritoModel class (EPyT wrapper, SteadyStateResult, EPSResult)
  scenarios.py    — Staging scenarios and EPS runners
  energy.py       — Pump power and energy calculations
  validation.py   — Result validation against hand-calculated references
  reporting.py    — Formatted console output tables
  eps_utils.py    — EPS event iteration helpers
  report.py       — Markdown report generation
  tables.py       — Table formatting utilities
  plotting.py     — Visualization (if needed)
```

## Key Dataclasses

- `RikoOpening(phi_pct, kv_m3h, n_pumps, gpv_link_id, curve_id)` — valve configuration
- `ReferenceOperatingPoint(phi_pct, n_pumps, q_total_lps, ..., dh_riko_m, v_pipe_ms)` — hand-calc reference
- `SteadyStateResult(n_active_pumps, riko_opening_pct, q_total_lps, ..., pipe_velocities, pipe_headlosses)` — EPANET result
- `PumpEnergyResult(q_lps, h_m, eta_pct, p_hydraulic_kw, p_shaft_kw, motor_load_pct)` — power result
- `ScenarioEnergyResult(n_pumps, pump, p_total_shaft_kw, hours, energy_kwh)` — energy result

## Relevant Tasks (from execution_task.md)

- **Task 2:** Add intermediate RIKO openings to constants (phi=26%, 34%, 40%)
- **Task 5:** Implement `compute_throttle_loss()` in energy.py
- **Task 6:** Create `rosarito/optimization.py` with VFD comparison (affinity laws)
- **Task 7:** Implement `run_staging_scenarios_extended()` for all 7 openings
- **Task 8:** Add CLI commands (`optimize`, `staging-extended`) and reporting functions

## Working Method

1. Always read existing module code before modifying — understand current patterns
2. Follow the existing import style and module organization
3. Add new functions at the end of modules (preserve git blame for existing code)
4. Write unit tests alongside implementation
5. Ensure `python -m unittest discover tests -v` passes after changes
6. Keep reporting functions aligned with existing table formatting style
