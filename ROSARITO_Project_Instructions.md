# PROJECT INSTRUCTIONS: Rosarito Desalination Plant — Seawater Intake EPANET Model

**Client:** CONAGUA / AYESA S.A. de C.V.
**Location:** Rosarito, Baja California, México
**Engineer:** Dr. Raúl Trujillo (VAG GmbH)
**Project start:** February 2026
**Document version:** v2 — 28/02/2026
**Current EPANET file:** `ROSARITO_EPANET_Rev2.inp` (617 lines)

---

## 1. PURPOSE OF THIS DOCUMENT

This document is the persistent briefing for every conversation in this project.
Do not re-explain background already covered here. Start each session from the current
state of the model. Reference the uploaded files directly when needed. When a value here
conflicts with an older file, this document takes precedence.

---

## 2. SYSTEM DESCRIPTION

Seawater intake and transfer system for the Rosarito Desalination Plant. Five vertical
centrifugal pumps draw seawater from the Pacific Ocean (MSL datum = 0 m) and discharge
through a single VAG RIKO DN1800 plunger control valve into the plant forebay.

**Confirmed topology:**

```
SEA (H = 0.00 m, MSL)
  → P_INTAKE  [DN2500, L=10 m, HDPE/concrete, ε=0.10 mm, K_minor=0.50]
  → J_SUCTION (common suction header)
  → PUMP_1 … PUMP_5  (5 × Ruhrpumpen 35WX, parallel)
  → J_MANIFOLD (common discharge header)
  → P_US      [DN1800, L=80 m, Carbon Steel, ε=0.046 mm]
  → J_RIKO_IN
  → RIKO_44 / RIKO_38 / RIKO_30 / RIKO_22  (4 parallel GPV — only ONE open at a time)
  → J_RIKO_OUT
  → P_DS      [DN1800, L=303 m, GRP/PRFV, ε=0.030 mm]
  → PLANT     (H = 18.17 m — desalination forebay, back-calculated)
```

---

## 3. EQUIPMENT PARAMETERS — CONFIRMED AND CONTROLLED

### 3.1 Pumps — Ruhrpumpen 35WX PB0 Vertical

**Source:** Hoja de datos características de la bomba, Quote 2583323 Rev5, 35WX-011-8, 01/16/2026

| Parameter | Value | Confidence |
|---|---|---|
| Quantity | 5 (4 duty + 1 standby) | Confirmed datasheet |
| Q nominal (per pump) | 1,256.0 l/s | Confirmed datasheet |
| H rated required | 26.00 m | Confirmed datasheet |
| H rated effective | **26.07 m** | Confirmed datasheet |
| H shutoff (20.63 in impeller) | **46.54 m** | Confirmed datasheet |
| Speed | 885 rpm (60 Hz) | Confirmed datasheet |
| Impeller diameter — nominal | 20.63 in (≈ 524 mm) | Confirmed datasheet |
| Impeller diameter — maximum | 22.75 in | Confirmed datasheet |
| Impeller diameter — minimum | 19.50 in | Confirmed datasheet |
| Efficiency at BEP | **89.0 %** | Confirmed datasheet |
| Q at BEP — bowl / pump | 1,237.0 / 1,199.9 l/s | Confirmed datasheet |
| Min. stable continuous flow | **845.4 l/s** | Confirmed datasheet (ANSI/HI 9.6.3) |
| NPSH required | 24.34 ft **(7.42 m)** | Confirmed datasheet |
| NPSH at duty (curve read) | ~22 ft **(~6.71 m)** | Read from H-Q curve image |
| NPSHA (from sea at MSL) | ~10.09 m | Calculated: P_atm − P_vap − hf_intake |
| NPSH margin at duty | ~3.38 m | OK ✓ |
| Motor rating | **600 hp / 447 kW** | Confirmed datasheet |
| Service factor | 1.15 | Confirmed datasheet |
| P hydraulic at duty (SG=1.025) | 329 kW (442 hp) | Calculated |
| P shaft at duty (η=88%) | 374 kW (502 hp) | Calculated |
| Motor load factor | **83.7 %** | OK ✓ |
| Fluid — datasheet | Water, SG=1.000 | Ruhrpumpen standard (curves on fresh water) |
| Fluid — actual | Seawater, SG=1.025 | Apply SG in EPANET [OPTIONS] |
| Temperature max | 68°F **(20°C)** | Confirmed datasheet |
| Vapor pressure at 20°C | 0.34 psi.a **(0.234 m)** | Confirmed datasheet |
| Selection status | Aceptable | ANSI/HI 9.6.7-2010 |

**EPANET pump head curve — `PC_35WX` (Rev2):**

| Q (l/s) | H (m) | Source |
|---|---|---|
| 0 | 46.54 | Confirmed datasheet |
| 1,256 | 26.07 | Confirmed datasheet |
| **1,700** | **14.50** | **Read from H-Q curve image (28/02/2026)** |

Fitted equation: `H = 46.54 − 5.300×10⁻⁴ × Q^1.480`
Curve exponent C = 1.48 — correct for vertical turbine pump (non-parabolic, non-overloading).
Fit accuracy in operating range (Q = 845–1,260 l/s): ±0.5 m.

> ⚠️ **Open item #1:** Ruhrpumpen has not provided tabulated H-Q data.
> The runout point is read from the graphical curve image (±1 m accuracy).
> Update `PC_35WX` when tabulated data is received.

**EPANET efficiency curve — `EFF_35WX` (Rev2, 13-point):**

| Q (l/s) | η (%) | Note |
|---|---|---|
| 400 | 32 | |
| 600 | 52 | |
| 800 | 68 | |
| 845 | 71 | Min stable flow |
| 1,000 | 79 | |
| 1,100 | 84 | |
| 1,200 | 87 | |
| 1,237 | 89 | BEP bowl — confirmed datasheet |
| **1,256** | **88** | Duty point |
| 1,400 | 85 | |
| 1,500 | 79 | |
| 1,600 | 70 | |
| 1,700 | 58 | |

**NPSHR (read from curve, ft → m):**

| Q (l/s) | NPSHR (ft) | NPSHR (m) |
|---|---|---|
| 800 | 14 | 4.27 |
| 1,000 | 18 | 5.49 |
| 1,256 | ~22 | ~6.71 |
| 1,500 | 29 | 8.84 |
| 1,700 | 40 | 12.19 |

**Power (read from curve — nearly flat, non-overloading):**

| Q (l/s) | Power (hp) | Power (kW) |
|---|---|---|
| 0–800 | 420–450 | 313–335 |
| 1,256 | ~442 | ~330 (SG=1.000) → ~338 (SG=1.025) |
| 1,600 | 465 | 347 |

---

### 3.2 Control Valve — VAG RIKO DN1800 PN16 Plunger Valve

**Sources:** VAG RIKO sizing report ROSARITO 27/02/2026 | VAG questionnaire | `riko_cylinder_e_dn1800.csv`

| Parameter | Value | Source |
|---|---|---|
| DN / PN | 1,800 mm / 16 bar | VAG sizing |
| Outlet type | E | VAG sizing |
| Max working pressure | 2.16 bar | VAG questionnaire |
| Static P upstream | 0.80 bar (8.16 m) | VAG questionnaire |
| Static P downstream | 0.28 bar (2.85 m) | VAG questionnaire |
| Static ΔP available | 0.52 bar (5.31 m) | VAG questionnaire |
| Qmin operating | 4,500 m³/h at 22% | VAG sizing |
| Qmax operating | 18,000 m³/h at 44% | VAG sizing |
| Upstream pipe | DN1800, L=80 m, Carbon Steel | VAG questionnaire |
| Downstream pipe | DN1800, L=303 m, GRP/PRFV | VAG questionnaire |
| Cavitation | Safe across full operating range | VAG CSV + sigma calculation |

**Kv values — exact, from `riko_cylinder_e_dn1800.csv` (50 rows, 2% steps):**

| Opening φ (%) | Kv (m³/h) | σ_critical | σ_constant | Used for |
|---|---|---|---|---|
| 22 | **3,179.78** | 0.63 | 0.84 | 1-pump |
| 30 | **7,621.47** | 0.86 | 1.15 | 2-pump |
| 38 | **14,444.21** | 1.04 | 1.38 | 3-pump |
| 44 | **21,038.45** | 1.14 | 1.52 | 4-pump (design) |

> ⚠️ **CRITICAL NOTE — VAG ζ column:**
> The CSV contains a `zeta_value` column but `Kv × √ζ ≈ 130,000 = constant` across all rows.
> VAG's ζ is an **internal parameter**, not the standard Darcy-Weisbach loss coefficient.
> **NEVER use** `dH = ζ × v²/(2g)` for this valve. Use the Kv formula only.

**Correct headloss formula (ISO 5167 / IEC 60534, SG cancels):**

```
ΔH [m] = Q [l/s]² × 132.15 / Kv [m³/h]²
```

where `K_coeff = 3.6² × 10.197 = 132.15` is a universal constant.

**Per-opening K constants for EPANET:**

| Curve ID | φ (%) | Kv (m³/h) | K = 132.15/Kv² |
|---|---|---|---|
| `RIKO_22pct` | 22 | 3,179.78 | 1.307×10⁻⁵ |
| `RIKO_30pct` | 30 | 7,621.47 | 2.275×10⁻⁶ |
| `RIKO_38pct` | 38 | 14,444.21 | 6.334×10⁻⁷ |
| `RIKO_44pct` | 44 | 21,038.45 | 2.986×10⁻⁷ |

---

## 4. HYDRAULIC BOUNDARY CONDITIONS

| Node | Type | Head (m) | Basis |
|---|---|---|---|
| `SEA` | Reservoir | 0.00 | MSL datum |
| `PLANT` | Reservoir | **18.17** | Back-calculated (Kv formula) |

**H_PLANT derivation at rated point (Q = 4 × 1,256 = 5,024 l/s):**

```
H_pump    = 26.07 m   (Ruhrpumpen rated)
− hf_US   =  0.09 m   (DN1800 steel, 80 m, f=0.01055, v=1.97 m/s, Re=3.38×10⁶)
− ΔH_RIKO =  7.54 m   (Kv=21,038 m³/h, φ=44%, Q=5,024 l/s)
− hf_DS   =  0.34 m   (DN1800 GRP, 303 m, f=0.01022)
─────────────────────
H_PLANT   = 18.10 m   → rounded to 18.17 m in INP (balanced Q differs slightly)
```

> ⚠️ **Open item #4:** H_PLANT is back-calculated, not field-measured.
> Must be confirmed against civil drawings or plant intake forebay pressure specification.

**Fluid properties (EPANET [OPTIONS]):**

| Property | Value | Basis |
|---|---|---|
| Specific gravity | 1.025 | Seawater at 20°C |
| Relative kinematic viscosity | 1.050 | ν_seawater/ν_water = 1.05×10⁻⁶/1.004×10⁻⁶ |
| Friction method | Darcy-Weisbach | Correct for large-diameter pipes at high Re |

**Pipe summary:**

| ID | DN (mm) | L (m) | Material | ε (mm) | f (at Qmax) | hf at Qmax (m) |
|---|---|---|---|---|---|---|
| P_INTAKE | 2,500 | 10 | HDPE/concrete | 0.10 | 0.01129 | 0.002 |
| P_US | 1,800 | 80 | Carbon Steel | 0.046 | 0.01055 | 0.093 |
| P_DS | 1,800 | 303 | GRP/PRFV | 0.030 | 0.01022 | 0.341 |

---

## 5. PUMP STAGING — CONTROLLED OPERATING POINTS

All points computed by Newton iteration on pump curve vs. system curve.
H_PLANT = 18.17 m | Rev2 pump curve (C = 1.480) | Kv-based valve headloss.

| φ (%) | N pumps | Q total (l/s) | Q total (m³/h) | Q/pump (l/s) | H_pump (m) | ΔH_RIKO (m) | v pipe (m/s) | σ_pipe | Cav. |
|---|---|---|---|---|---|---|---|---|---|
| **44%** | **4** | **5,016** | **18,059** | **1,254** | **26.12** | **7.51** | **1.971** | **4.81** | **OK ✓** |
| 38% | 3 | 3,664 | 13,189 | 1,221 | 26.90 | 8.50 | 1.440 | 4.35 | OK ✓ |
| 30% | 2 | 2,221 | 7,996 | 1,111 | 29.48 | 11.22 | 0.873 | 3.52 | OK ✓ |
| 22% | 1 | 1,014 | 3,651 | 1,014 | 31.63 | 13.44 | 0.398 | 3.10 | OK ✓ |

**Consistency check results:**

| Check | Result |
|---|---|
| 4-pump Q vs VAG Qmax (18,000 m³/h) | +59 m³/h (+0.3%) ✓ |
| Q/pump at 4-pump vs rated (1,256 l/s) | −0.2% ✓ |
| Q/pump at 3-pump vs rated | −2.8% ✓ |
| Q/pump at 2-pump vs rated | −11.6% — expected (restrictive valve) |
| Q/pump at 1-pump vs rated | −19.3% — expected (system limited) |
| All Q/pump > 845 l/s (min stable) | ✓ All safe |
| All σ_pipe > σ_constant | ✓ All safe |
| NPSHA > NPSHR at duty | 10.09 m > 6.71 m, margin = 3.38 m ✓ |
| Motor load factor (4-pump) | 83.7% ✓ |

> ⚠️ **1-pump caution:** Q = 3,651 m³/h is below VAG Qmin (4,500 m³/h).
> This is a system characteristic: the pump is too strong for this valve position.
> All pumps remain above the 845 l/s minimum stable flow — no cavitation or mechanical risk.
> Avoid sustained 1-pump operation in field.

> ⚠️ **2-pump note:** Q/pump = 1,111 l/s (−11.6% from rated). This deviation is expected
> because the RIKO at 30% is significantly more restrictive than at 44%. The pump operates
> safely within its acceptable operating region (AOR per ANSI/HI 9.6.3).

---

## 6. EPANET MODELING DECISIONS — DO NOT RE-DEBATE UNLESS FLAGGED

| Decision | Choice | Reason |
|---|---|---|
| Units | LPS | Metric industrial standard |
| Friction formula | Darcy-Weisbach | Correct for large-diameter pipes, Re > 10⁶ |
| Valve element type | GPV | Plunger valve ≠ PRV; GPV allows custom ΔH(Q) curve |
| Valve staging strategy | 4 parallel GPV links, only ONE open per timestep | EPANET cannot swap curve IDs via rules; parallel links is standard workaround |
| Headloss formula | `dH = Q²×132.15/Kv²` | ISO 5167 Kv equation; VAG ζ column is non-standard |
| Pump curve type | HEAD (3-point) | Standard EPANET definition |
| Pump curve anchor | Shutoff + duty (confirmed) + runout (curve read) | Best available data |
| Standby pump | PUMP_5, initial CLOSED | Activated by PRIORITY 10 rules on any duty pump trip |
| Hydraulic timestep | 5 min (EPS) | Adequate for large-inertia system |
| Demand model | Reservoir-to-reservoir | Pure transfer system, no distribution |
| SG in [OPTIONS] | 1.025 | Seawater; required for accurate power output |
| Viscosity in [OPTIONS] | 1.050 (relative) | ν_seawater/ν_water at 20°C |
| Rule priority order | 10=standby ON, 5=standby OFF, 4=4p-valve, 3=3p, 2=2p, 1=1p | Georgescu et al. CCWI 2015 |
| H_PLANT | 18.17 m | Back-calculated with Kv formula at rated point |

---

## 7. RULE LOGIC SUMMARY

13 rule blocks in `[RULES]`. All operate on pump `STATUS` (OPEN/CLOSED).

**Valve position (9 rules, PRIORITY 4):**
- 4 duty pumps running OR standby substituting any single duty pump → `RIKO_44` OPEN
- 3 pumps, no standby → `RIKO_38` OPEN
- 2 pumps → `RIKO_30` OPEN
- 1 pump → `RIKO_22` OPEN
- Each rule also explicitly closes the other 3 RIKO links.

**Standby activation (4 rules, PRIORITY 10 — highest):**
- Any single duty pump (PUMP_1–4) trips → `PUMP_5` STATUS = OPEN

**Standby deactivation (1 rule, PRIORITY 5):**
- All 4 duty pumps OPEN and PUMP_5 OPEN → `PUMP_5` STATUS = CLOSED

**To simulate a pump trip in EPS** — add to `[CONTROLS]`, do not modify `[RULES]`:
```epanet
LINK PUMP_4 CLOSED AT TIME 6:00    ; trip at hour 6
LINK PUMP_4 OPEN   AT TIME 8:00    ; restore at hour 8
```

---

## 8. MODEL REVISION HISTORY

| Rev | Date | Changes |
|---|---|---|
| 0 | 27/02/2026 | Initial model — graphically-read ζ values, 3-point EFF, H_PLANT=20.30 m |
| 1 | 28/02/2026 | **CRITICAL:** RIKO headloss switched to Kv formula (CSV data). H_PLANT revised to 18.17 m. All GPV curves replaced. |
| 2 | 28/02/2026 | Pump curve runout corrected (14.50 m vs 8.00 m estimated). EFF_35WX expanded to 13-point. |

---

## 9. UPLOADED REFERENCE FILES

| File | Contents | Status |
|---|---|---|
| `CURVA_BOMBA_RUHRPUMPEN.pdf` | Ruhrpumpen 35WX datasheet — Hoja de datos características | ✓ Fully extracted |
| `riko_cylinder_e_dn1800.csv` | VAG RIKO Kv(φ), ζ(φ), σ_critical, σ_constant — exact data | ✓ Fully incorporated |
| `RIKO_DN1800_E_ROSARITO.pdf` | VAG RIKO sizing — flow diagram, cavitation, noise | ✓ Used for context |
| `VAG_Questionaire_for_RIKO_new_sp_1.pdf` | System boundaries, pipe geometry, pressures | ✓ Fully extracted |
| `EPANET-control-centrifugal-pumps.pdf` | Georgescu et al. CCWI 2015 — rule-based control reference | ✓ Applied |
| `ROSARITO_EPANET_Rev2.inp` | **Current model** — 617 lines, Rev2 | ✓ Active |

---

## 10. OPEN ITEMS AND KNOWN LIMITATIONS

| # | Item | Impact | Priority | Action |
|---|---|---|---|---|
| 1 | Pump runout Q=1,700 l/s, H=14.5 m is read from graphical curve image (±1 m) | Low — operating range is 845–1,260 l/s, far from runout | Low | Request tabulated H-Q from Ruhrpumpen |
| 2 | H_PLANT = 18.17 m is back-calculated, not field-confirmed | Moderate — affects all operating points if forebay head differs | High | Confirm from civil drawings or plant P&ID |
| 3 | 1-pump scenario Q = 3,651 m³/h < VAG Qmin 4,500 m³/h | System characteristic; all safety checks pass | Medium | Confirm with VAG acceptable short-term flow; or accept that 1-pump is not a valid steady-state scenario |
| 4 | Transient/surge analysis not performed | RIKO fast-close = water hammer risk on pump trip | High | Commission SIR 3S or AFT Impulse study |
| 5 | P_DS (303 m GRP) has no intermediate nodes | Adequate for steady state; insufficient for transient | Low (steady), High (transient) | Add nodes before transient study |
| 6 | Efficiency curve read from graphical image (±2%) | Small effect on EPANET energy calculations | Low | Accept unless precise energy billing is required |

---

## 11. WORKING CONVENTIONS

**Language:** English. Spanish technical labels from source documents are kept as-is (e.g., "aguas arriba", "Qmax requerido", "Válvula de control").

**Code environment:** Python (Google Colab). Use WNTR for programmatic model manipulation. Always use SI units internally; convert to l/s or m³/h for display. Apply domain-driven design — model objects map to physical equipment.

**Review standard:** Flag any calculated result deviating more than 5% from a confirmed manufacturer reference. State confidence level for every significant claim. Challenge assumptions.

**Output files:** `.inp` files with inline comments. Every non-obvious parameter must cite its source (CSV row, datasheet field, calculated, or estimated). Revision number and date in `[TITLE]`.

**Decisions log:** Append new modeling decisions to Section 6 before closing a session. Mark superseded decisions as `[SUPERSEDED — date]`. Never delete.

---

## 12. NEXT STEPS (BACKLOG)

| Priority | Task |
|---|---|
| 1 | Confirm H_PLANT from civil drawings or plant forebay elevation |
| 2 | Run EPANET 2.2 GUI — verify solver convergence for all 4 staging scenarios |
| 3 | Run 24-hour EPS with scheduled pump trips at hours 6, 12, 18 — verify rule logic |
| 4 | Commission transient surge analysis (SIR 3S or AFT Impulse) |
| 5 | Build Python/WNTR wrapper for automated staging scenario comparison |
| 6 | Add energy post-processing: daily kWh per staging scenario |
| 7 | Request tabulated H-Q data from Ruhrpumpen |
| 8 | Add intermediate nodes on 303 m GRP pipe before transient study |
