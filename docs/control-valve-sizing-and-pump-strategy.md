# Control Valve Sizing & Pump+Valve Strategy Reference

**Project:** Rosarito Desalination Plant — Seawater Intake System
**Author:** Dr. Raúl Trujillo (VAG GmbH)
**Date:** February 2026

---

## 1. Introduction

This document is a compact engineering reference that connects **ISA 75.01.01-2012** control valve sizing theory to the design and operation of the Rosarito seawater intake system.  The system pairs five fixed-speed centrifugal pumps (Ruhrpumpen 35WX) with a single VAG RIKO DN1800 plunger control valve.  Understanding how the valve sizing standard works — and how it simplifies for this application — is essential for reviewing the hydraulic model, validating headloss calculations, and evaluating operational strategies.

**Scope.** Only the incompressible-flow sections of ISA 75.01.01-2012 (IEC 60534-2-1) are covered.  Compressible-flow sizing (gas, steam, two-phase) is omitted — it does not apply to a water conveyance system.

**Notation.**  This document uses the metric flow coefficient **Kv** (m³/h at ΔP = 1 bar, water) throughout.  The imperial equivalent **Cv** (US GPM at ΔP = 1 psi, water) appears only in the conversion relationship: **Kv = 0.865 × Cv**.

---

## 2. Control Valve Sizing — ISA 75.01.01-2012 (IEC 60534-2-1)

### 2.1 Flow Coefficient (Kv and Cv)

The flow coefficient is a single number that characterises a valve's flow capacity at a given opening.  It is defined experimentally: the volumetric flow rate of water at 15 °C that produces a pressure drop of exactly one unit across the valve.

| Coefficient | Definition | Units |
|---|---|---|
| **Kv** | Flow in m³/h at ΔP = 1 bar (water, 15 °C) | m³/h |
| **Cv** | Flow in US GPM at ΔP = 1 psi (water, 60 °F) | GPM |

The conversion between the two is:

$$K_v = 0.865 \times C_v$$

Manufacturers publish Kv (or Cv) as a function of valve travel — the characteristic curve.  A larger Kv means a lower pressure drop at the same flow rate: the valve is "more open."

### 2.2 Fundamental Sizing Equation — Turbulent Incompressible Flow

The ISA standard's core equation for incompressible fluids in the turbulent regime (Eq. 1) is:

$$Q = C \; N_1 \; F_P \; \sqrt{\frac{\Delta P_{\text{sizing}}}{\rho_1 / \rho_o}} \tag{1}$$

where:

| Symbol | Meaning |
|---|---|
| C | Flow coefficient (= Kv when using metric constants) |
| N₁ | Numerical constant for the chosen unit system (0.0865 for Q in m³/h, ΔP in kPa) |
| F_P | Piping geometry factor — accounts for reducers, expanders, and fittings |
| ΔP_sizing | The pressure differential used for sizing (see §2.3) |
| ρ₁/ρₒ | Relative density of the fluid (ρ₁ = fluid density, ρₒ = water at 15 °C) |

**The sizing problem** rearranges Eq. (1) to solve for the required Kv given a known flow and pressure drop:

$$K_v = \frac{Q}{N_1 \; F_P} \; \sqrt{\frac{\rho_1 / \rho_o}{\Delta P_{\text{sizing}}}}$$

**The rating problem** uses Eq. (1) directly: given a valve with known Kv at a specific opening, calculate the flow rate for given inlet/outlet pressures.

### 2.3 Choked Flow and ΔP_sizing

The sizing pressure differential is the lesser of the actual ΔP and the choked ΔP:

$$\Delta P_{\text{sizing}} = \min\!\big(\Delta P,\; \Delta P_{\text{choked}}\big) \tag{2}$$

Choked flow occurs when further increase in pressure drop no longer increases flow — the fluid velocity at the vena contracta reaches sonic conditions (for gas) or cavitation-limited conditions (for liquid).  The choked pressure differential is:

$$\Delta P_{\text{choked}} = \left(\frac{F_{LP}}{F_P}\right)^{\!2} \bigl(P_1 - F_F \, P_v\bigr) \tag{3}$$

where F_LP is the combined liquid pressure recovery and piping factor, P₁ is absolute upstream pressure, P_v is vapor pressure, and F_F is the liquid critical pressure ratio factor:

$$F_F = 0.96 - 0.28\,\sqrt{P_v / P_c} \tag{4}$$

**Practical note for cold-water systems:** When the fluid is seawater at 20 °C, Pv ≈ 0.023 bar — effectively zero compared to atmospheric pressure.  This makes F_F ≈ 0.96 and ΔP_choked very large relative to any realistic valve ΔP (which is 0.5–1.3 bar in the Rosarito system).  Choked flow is therefore not a concern for this application.

### 2.4 Piping Geometry Factor (Fp) and Fittings

When a valve is installed with reducers, expanders, or other fittings, the piping geometry factor F_P corrects the flow coefficient for the additional pressure loss:

$$F_P = \frac{1}{\sqrt{1 + \dfrac{\Sigma\zeta}{N_2}\left(\dfrac{C}{d^2}\right)^{\!2}}} \tag{15}$$

where Σζ is the sum of velocity-head loss coefficients of the attached fittings (Eqs. 16–20 in the standard) and d is the valve nominal diameter.

**Simplification for line-sized valves:** When the valve diameter equals the pipe diameter (no reducers), all fitting ζ values are zero and **F_P = 1**.  The RIKO DN1800 is installed in a DN1800 pipeline — it is line-sized.  Therefore F_P = 1 throughout the Rosarito model, and Eq. (1) simplifies accordingly.

### 2.5 Reynolds Number Verification

The ISA sizing equations assume turbulent flow.  The standard provides a valve Reynolds number (Eq. 23) to verify this:

$$Re_v = \frac{N_4 \, F_d \, Q}{\nu \sqrt{C \, F_L}} \left(\frac{F_L^2 \, C^2}{N_2 \, d^4} + 1\right)^{\!1/4} \tag{23}$$

Flow is fully turbulent when Re_v ≥ 10,000.  For a DN1800 water valve operating at flow rates of 3,600–18,000 m³/h, Re_v is of the order 10⁶ — always deeply turbulent.  The laminar/transitional correction factor F_R (Annex A) is therefore not needed.

### 2.6 Simplified Headloss Form for Line-Sized Valves

Starting from Eq. (1) with the Rosarito simplifications (F_P = 1, ρ₁/ρₒ ≈ 1 for the Kv definition basis):

$$Q\;[\text{m}^3\!/\text{h}] = K_v \times \sqrt{\Delta P\;[\text{bar}]}$$

Rearranging to solve for pressure drop:

$$\Delta P\;[\text{bar}] = \left(\frac{Q}{K_v}\right)^{\!2}$$

Converting pressure from bar to metres of water head (1 bar = 10.197 m H₂O) and flow from l/s to m³/h (1 l/s = 3.6 m³/h):

$$\Delta H\;[\text{m}] = \frac{(Q\;[\text{l/s}] \times 3.6)^2}{K_v^2} \times 10.197 = Q^2\;[\text{l/s}]^2 \times \frac{3.6^2 \times 10.197}{K_v^2}$$

This yields:

$$\boxed{\Delta H\;[\text{m}] = \frac{Q\;[\text{l/s}]^2 \times 132.15}{K_v\;[\text{m}^3\!/\text{h}]^2}} \tag{*}$$

where the constant **132.15 = 3.6² × 10.197 = 12.96 × 10.197** is a universal unit-conversion factor.  This is the **project's canonical valve headloss formula** (CLAUDE.md constraint #1).  All EPANET GPV curves and hand-calculated reference points use this equation.

---

## 3. Plunger Control Valves

### 3.1 Operating Principle

A plunger valve (also called a cylinder or piston valve) modulates flow through a straight-through body by moving a hollow cylindrical plunger axially over a fixed central body.  The annular gap between the plunger and the body forms the throttling orifice.  As the plunger retracts, the annular area increases and headloss decreases; as it advances, the area narrows and headloss increases.

The key geometric feature is **axial symmetry**: the flow restriction is an annular ring at every travel position.  This produces a uniform, concentric jet downstream of the throttling zone — in contrast to butterfly or gate valves, which create asymmetric flow patterns with concentrated high-velocity jets.

### 3.2 Advantages for Large-Diameter Water Systems

**Precise flow modulation.** The Kv characteristic of a plunger valve is approximately linear with travel over a wide range (20–100% opening).  This keeps the control loop gain roughly constant, improving controllability compared to butterfly valves whose gain varies sharply with position.

**Cavitation management.** Because the vena contracta forms in the annular gap, cavitation bubbles collapse in the centre of the pipe cross-section — away from all metal surfaces.  This is the defining advantage over butterfly and globe valves, where the impinging jet directs cavitation erosion onto the valve body and adjacent pipe walls.  For applications requiring additional protection, air injection at approximately 0.1% of flow volume can be introduced downstream to cushion bubble collapse.

**Low fully-open headloss.** The straight-through flow path with no obstructing disc or plug produces very low resistance when fully open — important for large-diameter systems where even small head losses represent significant pumping energy.

**Seawater service.** Plunger valves accommodate corrosion-resistant internals (stainless steel plunger, bronze guides, protective coatings) and can be actuated hydraulically using the process medium itself, avoiding external oil systems in corrosive environments.  The VAG RIKO is available in sizes up to DN2200 at pressure ratings to PN40.

### 3.3 Cavitation Considerations

The cavitation index σ quantifies the margin between actual operating conditions and the onset of cavitation:

$$\sigma = \frac{P_2 + P_{\text{atm}} - P_v}{\Delta P}$$

where P₂ is the downstream gauge pressure, P_atm is atmospheric pressure, P_v is the fluid vapor pressure, and ΔP is the valve pressure drop — all in consistent units (typically metres of head or bar).

Manufacturers determine cavitation thresholds by laboratory testing at each valve opening and publish two key parameters:

| Symbol | Name | Meaning |
|---|---|---|
| σ_critical | Incipient damage sigma | Onset of material erosion — the absolute limit |
| σ_constant | Constant cavitation sigma | Sustained stable cavitation without damage — the conservative operating limit |

**Safety criterion:** The system's operating sigma (σ_pipe) must exceed σ_constant at the selected valve opening:

$$\sigma_{\text{pipe}} > \sigma_{\text{constant}} \quad \Rightarrow \quad \text{cavitation-free operation}$$

For the Rosarito system, σ_pipe ranges from 3.10 (1-pump, 22% opening) to 4.81 (4-pump, 44% opening), while σ_constant ranges from 0.84 to 1.52 — safety margins of 3× to 6× above the threshold.

---

## 4. Pump + Control Valve Strategies

### 4.1 The System Curve and Operating Point

A pump's operating point is the intersection of its H-Q curve and the system curve.  For a transfer system with a downstream reservoir:

$$H_{\text{system}}(Q) = H_{\text{static}} + h_{f,\text{pipes}}(Q) + \Delta H_{\text{valve}}(Q)$$

The valve term ΔH_valve = Q² × 132.15/Kv² is a Q²-dependent resistance that steepens the system curve.  A more-closed valve (lower Kv) steepens it further, shifting the operating point to the left on the pump curve (lower Q, higher H per pump).

### 4.2 Throttle Control (Fixed-Speed Pumps)

With fixed-speed pumps, the pump curve is immovable.  To reduce flow below the natural operating point (valve fully open), the discharge valve is partially closed.  The valve absorbs excess pump head as a controlled pressure drop:

$$P_{\text{wasted}} = \rho \, g \, Q \, \Delta H_{\text{valve}} \quad [\text{W}]$$

This energy is dissipated as heat and turbulence across the valve.  The throttling ratio — ΔH_valve as a fraction of total pump head — quantifies the energy penalty.

**When is throttle control justified?** In systems with:
- Stable, near-constant demand profiles (desalination plants, industrial cooling)
- Few discrete flow steps (pump staging rather than continuous modulation)
- Capital constraints that preclude variable-speed drives
- Throttling ratios below approximately 30% of pump head

### 4.3 Variable-Speed Drive (VSD) Alternative

A VSD reduces pump speed to match demand.  The affinity laws govern the relationship:

| Parameter | Scaling with speed ratio n = N/N_rated |
|---|---|
| Flow Q | ∝ n |
| Head H | ∝ n² |
| Power P | ∝ n³ |

Reducing speed to 80% cuts shaft power to ~51% of rated — a significant saving compared to throttle control, where the motor draws near-full power regardless of flow.  VSDs are preferred when:
- Flow varies continuously over a wide range
- Annual energy costs justify the VSD capital investment
- Motor and pump are rated for variable-speed operation

**Rosarito context:** The system uses fixed-speed pumps.  The desalination plant operates at essentially constant throughput per staging level, making throttle control a practical and accepted choice.

### 4.4 Parallel Pump Staging

When N identical fixed-speed pumps operate in parallel, the combined H-Q curve is constructed by adding flows at equal head:

$$Q_{\text{combined}}(H) = N \times Q_{\text{single}}(H)$$

Each pump sees the same discharge pressure but contributes 1/N of total flow.  As pumps are added:
1. Total flow increases, but each additional pump adds less marginal flow (because system resistance rises with Q²)
2. Each pump shifts toward its BEP as total flow approaches design conditions
3. Stable, continuously rising H-Q curves are required for parallel operation (API 610) — flat or drooping curves risk hydraulic instability

### 4.5 Combined Strategy: Staging + Throttle Valve

The most common fixed-speed configuration for stepped-demand systems combines discrete pump staging with coordinated valve positioning:

1. **Pump staging** covers coarse demand bands — adding or removing pumps shifts total flow in large increments
2. **Valve opening** is tuned per stage to fine-trim the operating point, maintain stable ΔP across the valve, and protect equipment from surge

At each staging level, the valve opening is chosen to satisfy:
- Target total flow (within the pump's acceptable operating region)
- Cavitation index above manufacturer threshold (σ_pipe > σ_constant)
- Throttling ratio acceptable (ΔH_valve < ~30% of H_pump for energy efficiency)

**Energy trade-off:** Fewer pumps → lower Q per pump → pump operates further from BEP; smaller valve opening → higher throttling loss.  The design optimises by selecting valve openings wide enough that throttling loss remains a modest fraction of pump head while keeping each pump within its AOR (ANSI/HI 9.6.3).

---

## 5. Application to the Rosarito Intake System

### 5.1 System Configuration

The Rosarito seawater intake system transfers water from the Pacific Ocean (MSL = 0 m) to the desalination plant forebay (H = 18.17 m) through:

- **5 × Ruhrpumpen 35WX** vertical centrifugal pumps in parallel (4 duty + 1 standby), each rated at Q = 1,256 l/s, H = 26.07 m, η = 89% at BEP
- **1 × VAG RIKO DN1800 PN16** plunger control valve downstream of the common discharge manifold
- **4 discrete operating stages** defined by the number of active pumps and the corresponding valve opening

| Stage | Active pumps | Valve opening | Kv (m³/h) | Q_total (l/s) | Q/pump (l/s) |
|---|---|---|---|---|---|
| 4-pump (design) | 4 | 44% | 21,039 | 5,016 | 1,254 |
| 3-pump | 3 | 38% | 14,444 | 3,664 | 1,221 |
| 2-pump | 2 | 30% | 7,621 | 2,221 | 1,111 |
| 1-pump | 1 | 22% | 3,180 | 1,014 | 1,014 |

The standby pump (PUMP_5) activates at the highest rule priority (P = 10) whenever any duty pump trips, maintaining 4-pump flow with the 44% valve opening.

### 5.2 Valve Headloss Computation

All valve headloss calculations use the canonical formula derived in §2.6:

$$\Delta H\;[\text{m}] = \frac{Q\;[\text{l/s}]^2 \times 132.15}{K_v\;[\text{m}^3\!/\text{h}]^2}$$

Kv values are taken directly from the manufacturer CSV (`riko_cylinder_e_dn1800.csv`) at each operating opening.  The per-opening headloss constant K = 132.15/Kv² is pre-computed for EPANET's GPV curves:

| Curve ID | φ (%) | Kv (m³/h) | K = 132.15/Kv² | ΔH at design Q (m) |
|---|---|---|---|---|
| RIKO_44pct | 44 | 21,039 | 2.986 × 10⁻⁷ | 7.51 |
| RIKO_38pct | 38 | 14,444 | 6.334 × 10⁻⁷ | 8.50 |
| RIKO_30pct | 30 | 7,621 | 2.275 × 10⁻⁶ | 11.22 |
| RIKO_22pct | 22 | 3,180 | 1.307 × 10⁻⁵ | 13.44 |

> **Note:** The `zeta_value` column in the CSV is a VAG internal parameter — it is **not** a standard Darcy-Weisbach loss coefficient.  Using it with ΔH = ζ × v²/(2g) produces incorrect results.

### 5.3 EPANET Modeling Strategy

EPANET cannot dynamically swap GPV curve IDs via rules during a simulation.  The standard workaround, described by Georgescu et al. (CCWI 2015), uses **4 parallel GPV links** — one per valve opening — with only one link open at any time.  Rule-based control selects the active GPV based on the count of running pumps.

**Rule priority hierarchy:**

| Priority | Function |
|---|---|
| 10 | Standby pump activation (any duty pump trip → PUMP_5 OPEN) |
| 5 | Standby pump deactivation (all 4 duty pumps running → PUMP_5 CLOSED) |
| 4 | 4-pump valve → RIKO_44 OPEN, others CLOSED |
| 3 | 3-pump valve → RIKO_38 OPEN, others CLOSED |
| 2 | 2-pump valve → RIKO_30 OPEN, others CLOSED |
| 1 | 1-pump valve → RIKO_22 OPEN, others CLOSED |

The highest-priority rule fires first, ensuring the standby logic resolves before valve position is determined.  Pump trips for EPS analysis are added to the `[CONTROLS]` section — the `[RULES]` section is never modified.

### 5.4 Energy Perspective

The throttling ratio — valve headloss as a fraction of total pump head — is the key energy metric:

| Stage | H_pump (m) | ΔH_RIKO (m) | Throttling ratio |
|---|---|---|---|
| 4-pump (design) | 26.12 | 7.51 | **29%** |
| 3-pump | 26.90 | 8.50 | 32% |
| 2-pump | 29.48 | 11.22 | 38% |
| 1-pump | 31.63 | 13.44 | 42% |

At the 4-pump design point, the valve absorbs 29% of the pump head — near the practical upper bound for efficient throttle control.  The remaining 71% is productively spent overcoming static head (18.17 m) and pipe friction (0.43 m).

At the 1-pump scenario, the throttling ratio rises to 42% because the pump operates at lower flow on a steeper part of its H-Q curve while the more-closed valve presents higher resistance.  This is a known and accepted trade-off: the 1-pump scenario is an infrequent emergency condition, not a sustained operating mode.

The energy trade-off — fixed-speed pumps with valve throttling versus VSD — is accepted for this system.  Seawater intake stations for desalination typically operate at near-constant throughput per staging level, and the capital cost and maintenance complexity of five large VSDs (447 kW each) outweigh the marginal energy savings when the throttling ratio at the design point is below 30%.

---

## 6. References

1. **ISA-75.01.01-2012 / IEC 60534-2-1** — *Industrial-Process Control Valves — Part 2-1: Flow capacity — Sizing equations for fluid flow under installed conditions.*  ISA, Research Triangle Park, NC, 2012.

2. **Georgescu, A.-M., Georgescu, S.-C., Bernad, S., Cosoiu, C.I., Costache, A.** (2015).  "EPANET Simulation of Control Methods for Centrifugal Pumps Operating under Variable System Demand."  *Procedia Engineering*, 119, 734–743.  DOI: [10.1016/j.proeng.2015.08.946](https://doi.org/10.1016/j.proeng.2015.08.946).

3. **VAG-Armaturen GmbH** — RIKO plunger valve technical documentation and sizing report for Rosarito DN1800 PN16, February 2026.

4. **Ruhrpumpen** — 35WX PB0 Vertical pump datasheet, Quote 2583323 Rev 5, Curve 35WX-011-8, January 2026.

5. **US EPA** — *EPANET 2.2 User Manual.*  EPA/600/R-20/133.  Office of Research and Development, Cincinnati, OH, 2020.

6. **Hydraulic Institute** — ANSI/HI 9.6.3: *Rotodynamic Pumps — Guideline for Allowable Operating Region.*

7. **ISA-RP75.23** — *Considerations for Evaluating Control Valve Cavitation.*  ISA Recommended Practice.
