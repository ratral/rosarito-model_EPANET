# Test & Validation Agent

## Role

Runs tests, executes EPANET simulations, and validates results against the acceptance criteria defined in `execution_task.md`. Ensures that code changes do not break existing functionality and that new features meet engineering tolerances.

## When to Use

- Running the test suite: `python -m unittest discover tests -v`
- Running EPANET simulations via CLI: `python main.py staging`, `python main.py energy`, etc.
- Verifying that an INP file loads without parse errors
- Checking that steady-state results match hand-calculated references within tolerances
- Validating acceptance criteria for any task in execution_task.md
- Performing regression checks (existing 4-pump results unchanged after modifications)
- Verifying mutual exclusion of GPV valves (only one OPEN at any timestep)
- Checking that computed values are physically reasonable (headloss 0-20m, flow positive, etc.)

## Validation Tolerances

| Check | Tolerance | Source |
|-------|-----------|--------|
| EPANET vs hand-calc reference | 5% | CLAUDE.md review standard |
| New reference operating points | 0.5% | Task 2 acceptance criteria |
| GPV curve headloss vs hand-calc | 1% | Task 3 acceptance criteria |
| Backward compatibility (Q_total) | 0.1% | Task 3, 4 acceptance criteria |
| Pipe subdivision (friction loss) | 0.01 m | Task 4 acceptance criteria |
| Node head unchanged | 0.01 m | Task 4 acceptance criteria |
| Throttle power at design point | 0.5% | Task 5 acceptance criteria |
| VFD speed ratio minimum | >= 0.7 | Task 6 acceptance criteria |

## Key Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Run unit tests (non-EPANET, fast)
python -m unittest discover tests -v

# Run staging scenarios with validation
python main.py staging

# Run energy post-processing
python main.py energy

# Run 24h EPS with pump trips
python main.py eps

# Run all analyses
python main.py

# Check EPANET file loads (via EPyT)
python -c "from epyt import epanet; d = epanet('inp_files/ROSARITO_EPANET_Rev3.inp'); print('OK'); d.unload()"
```

## Physical Reasonableness Checks

Results should satisfy these physical constraints:
- All flows are positive (direction: SEA -> PLANT)
- Pump head: 20-47 m (between duty point and shutoff)
- RIKO headloss: 0-20 m (positive, not exceeding pump head)
- Pipe velocity P_DS: 0.3-2.5 m/s (reasonable for DN1800)
- Q per pump >= 845.4 l/s (min stable, except known 1-pump exception)
- Q_total for 1-pump < 4500 m3/h (known system characteristic, not an error)
- Motor load: 50-115% (within service factor)
- Energy balance: H_pump = H_PLANT + hf_pipes + dH_RIKO (within 0.5 m)

## Acceptance Criteria by Task

### Task 1 — Kv Extraction
- [ ] Kv values are exact CSV rows (not interpolated) if CSV has 2% steps
- [ ] `dH = Q^2 * 132.15 / Kv^2` produces headloss in 0-20 m range
- [ ] Values documented with source row reference

### Task 2 — Constants Update
- [ ] `RIKO_BY_NPUMPS` unchanged (original 4 mappings preserved)
- [ ] `RIKO_OPENINGS_ALL` contains exactly 7 entries sorted by phi descending
- [ ] `python -m unittest discover tests -v` passes
- [ ] Each new `ReferenceOperatingPoint` has Q_total, Q/pump, H_pump, dH_RIKO within 0.5%

### Task 3 — INP Rev3
- [ ] EPANET 2.2 loads without parse errors
- [ ] 4-pump/RIKO_44 produces same Q, H, dH as Rev2 (within 0.1%)
- [ ] Each new GPV curve produces correct dH at expected flow (within 1%)
- [ ] Only ONE GPV is OPEN at any timestep

### Task 4 — Pipe Subdivision
- [ ] Total friction across 4 segments equals single-pipe loss (within 0.01 m)
- [ ] Head at J_RIKO_OUT and PLANT unchanged (within 0.01 m)
- [ ] All existing staging scenarios unchanged (within 0.1% on Q_total)

### Task 5 — Throttle Loss
- [ ] Design point (Q=5017 l/s, dH=7.52 m): P_throttle ~ 75.7 kW
- [ ] 1-pump (Q=1043 l/s, dH=14.23 m): P_throttle ~ 149.3 kW
- [ ] Unit test validates against hand-calc at design point (within 0.5%)

### Task 6 — VFD Comparison
- [ ] At 4-pump design: speed ratio < 1.0
- [ ] Power saving = P_shaft_throttled - P_shaft_vfd is positive for all scenarios
- [ ] At 4-pump: saving ~ 75-80 kW (matches throttle loss from Task 5)
- [ ] Speed ratio never below 0.7
- [ ] Unit tests validate affinity-law calculations at 2 known operating points

### Task 7 — Extended Scenarios
- [ ] Returns 7 SteadyStateResult objects
- [ ] Original 4 results match `run_staging_scenarios()` exactly
- [ ] New 3 results have Q_total between neighboring original scenarios
- [ ] All Q/pump > 845 l/s (min stable flow)
- [ ] EPANET solver converges without warnings for all 7

### Task 8 — Reporting & CLI
- [ ] `python main.py optimize` runs without error, prints both tables
- [ ] `python main.py staging-extended` prints 7-row table + validation
- [ ] All existing CLI commands unchanged
- [ ] Tables are well-formatted with aligned columns and engineering units

## Working Method

1. Run existing tests FIRST to establish baseline (before any changes)
2. After code changes, run tests again to check for regressions
3. For EPANET validation, compare results against `REFERENCE_POINTS` in constants.py
4. Report pass/fail with actual deviation percentages
5. If a check fails, report the computed value, expected value, and deviation clearly
6. Never mark a task as complete if any acceptance criterion is not met
