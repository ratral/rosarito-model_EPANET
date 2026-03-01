Within EPANET’s limitations, you can represent several real-world strategies, first the traditional, mechanical approaches:

- **Constant-speed pump + PRV/PSV**
    - Pump runs at fixed speed; downstream PRV controls maximum pressure, or upstream PSV maintains minimum suction pressure.​
    - PRV/PSV setpoints are static during a run (unless switched via rules by changing valve status or swapping links).
- **Throttle control valve (TCV) on pump discharge**
    - TCV uses a loss coefficient as its setting; you can change this with rules to emulate valve throttling (more loss when “more closed”).
    - Combine with a constant-speed pump when you explicitly want to model energy loss due to throttling.

Both of these strategies represent traditional, mechanical approaches to flow and pressure control. My primary engineering stance is that while these methods are reliable and still common, they are fundamentally inefficient compared to using Variable Frequency Drives (VFDs) on pumps (high confidence). Both strategies rely on adding artificial friction to the system to force the pump back along its performance curve, which deliberately wastes electrical energy.

- **Variable-speed pump for pressure control (recommended instead of throttling)**
    - Use a VSP and control its **SETTING** based on a monitored pressure:
        - IF node pressure > target, reduce pump speed (SETTING = 0.9, 0.8, etc.).
        - IF node pressure < lower band, increase speed.openepanet+1
    - EPANET rescales the pump curve according to affinity laws (flow ∝ speed, head ∝ speed²).
    - This is often a better representation of real pressure management than a throttle control valve.

# Pump + Control Valve Strategies: Real-World Behavior and EPANET Representation

However, they are necessary to model accurately when analyzing existing infrastructure or systems where VFDs are prohibitively expensive or technically unsuitable.
## Key Distinction

**The fundamental difference between these strategies is their purpose:** PRV/PSV exist to regulate pressure at specific locations in your network, while TCV exists to deliberately dissipate energy through throttling. Understanding this distinction is critical for correct EPANET implementation.

---
## Strategy 1: Constant-Speed Pump + PRV/PSV

### Real-World Behavior

A constant-speed pump operates at fixed rotational speed, delivering head according to its H-Q curve. Without control, this can create two problems:

**PRV (Pressure Reducing Valve)** — installed downstream:
- Maintains a **downstream pressure ceiling** by throttling when upstream pressure would force downstream pressure above the setpoint
- Protects downstream zones from over-pressurization (pipe bursts, fixture damage)
- If upstream pressure is already below the setpoint, the PRV opens fully and acts as an open pipe
- The PRV cannot add pressure—it can only limit it

**PSV (Pressure Sustaining Valve)** — installed upstream:
- Maintains an **upstream pressure floor** by throttling to prevent upstream pressure from dropping below the setpoint
- Protects pump suction conditions or maintains minimum pressure in upstream zones
- If upstream pressure naturally exceeds the setpoint, the PSV opens fully

In both cases, the valve responds continuously and automatically to pressure variations in real installations.

### EPANET Representation

**1. Pump modeling:**
Model the pump as a PUMP link with a fixed pump curve (H-Q relationship). EPANET treats this as constant-speed for the entire simulation unless you change speed/status via controls.

**2. PRV/PSV modeling:**
EPANET models these as pressure-controlled valve links. Each operates in three internal hydraulic states:
- **ACTIVE:** Valve is throttling to maintain its pressure setpoint (PRV holds downstream pressure; PSV holds upstream pressure)
- **OPEN:** Valve is fully open because the pressure constraint is already satisfied without throttling
- **CLOSED:** Acts as a check valve against reverse flow

Place a PRV or PSV link in your network where the physical regulator exists. **Critical topology requirement:** You must have a junction node between the pump discharge and the valve inlet—EPANET links always connect at nodes.

**3. Setting the valve:**
The PRV/PSV "Setting" parameter is the target pressure (in your project's pressure units). EPANET's solver will add whatever head loss is needed (within hydraulic feasibility) to maintain this pressure.

**4. Changing setpoints during simulation:**
Setpoints are static during each hydraulic time step. To emulate operational changes, use EPANET's Rules or Controls:

```
RULE 1
IF TANK T1 LEVEL BELOW 3.0
THEN VALVE PRV1 SETTING IS 35.0
ELSE VALVE PRV1 SETTING IS 45.0
```

This provides discrete, stepwise approximation of setpoint adjustment—not continuous feedback control.

### Critical Limitations and Edge Cases

**Convergence issues:** When a PRV is tightly coupled with a pump (short connecting pipe, high pressure differential), EPANET's solver can experience status oscillation (Warning 04). The PRV tries to throttle, flow drops, pump head rises, and the solver oscillates between valve states. **Fix:** Ensure the PRV setpoint is realistically lower than the pump's shutoff head, or add a short realistic pipe between pump and PRV to improve numerical conditioning.

**PSV and cavitation:** EPANET's PSV maintains upstream pressure by adding throttling loss—it does **not** model suction-side cavitation or NPSH limits. It's a steady-state hydraulic constraint, not a physical cavitation model.

**Over-constrained systems:** If multiple PRVs/PSVs create conflicting pressure requirements, you may see convergence failures or unrealistic status toggling. Simplify control logic and tighten the hydraulic time step if this occurs.

---

## Strategy 2: Throttle Control Valve (TCV) on Pump Discharge

### Real-World Behavior

A TCV is a manually or automatically adjusted valve (butterfly, globe, gate) placed on the pump discharge to control flow by deliberately increasing system resistance. As you close the valve:
- Head loss across the valve increases
- Flow decreases (pump moves left along its H-Q curve)
- Energy is dissipated as heat and turbulence

This strategy is used when you lack variable-speed drives or need simple flow control, but **it is inherently energy-inefficient**—you're converting electrical energy to pump head, then immediately dissipating that head as valve loss.

### EPANET Representation

**1. Model the valve as a TCV link:**
EPANET's TCV (Throttle Control Valve) uses a minor loss coefficient **K** as its setting parameter. Head loss follows:

$h_L = K · V²/(2g)$  or in EPANET's flow formulation:  $h_L = K · Q²$

Higher $K = more throttling = more head loss = less flow$.

**2. Controlling throttling via Rules:**
To emulate valve adjustment over time, use Rules to change the TCV's K-value based on system conditions:

```
RULE 2
IF NODE N5 PRESSURE ABOVE 55.0
THEN VALVE TCV1 SETTING IS 80.0

RULE 3
IF TANK T2 LEVEL BELOW 2.5
THEN VALVE TCV1 SETTING IS 5.0
```

**Critical non-linearity issue:** The relationship between valve position and K-value is **highly non-linear**. A butterfly valve at 50% closed does not have 50% of its maximum K-value; the loss coefficient increases exponentially in the final 20-30% of closure. You must map manufacturer Cv curves or valve performance data to discrete K-values for your rules—EPANET will not do this mapping for you.

**3. Why use TCV instead of PRV?**
When your objective is to explicitly model and quantify energy waste due to throttling, TCV is the correct choice. The head loss across the TCV directly represents wasted kilowatt-hours, which you can calculate using EPANET's energy reporting. A PRV, by contrast, is intended for pressure regulation and may obscure the energy implications of throttling control.

### Critical Limitations

**No automatic control:** A TCV in EPANET imposes only a fixed (or rule-changed) loss coefficient. It does not self-regulate like a PRV. Any "control" behavior comes from your rules, not the valve element itself.

**Solver shock from abrupt changes:** EPANET rules execute instantaneously. If a rule changes K from 5 to 500 at hour 12:00, the solver experiences a mathematical shock that can cause convergence failure in the subsequent time step. **Best practice:** Change K in smaller increments, or use multiple rules with intermediate steps.

**No transient effects:** EPANET does not model valve actuator speed, hysteresis, or water hammer. The TCV represents steady-state head loss only.

---

## Summary Comparison

| Feature | PRV/PSV | TCV |
|---------|---------|-----|
| **Real-world purpose** | Automatic pressure regulation | Manual/controlled flow throttling |
| **EPANET setting** | Pressure setpoint (m or psi) | Loss coefficient K (dimensionless) |
| **Control mechanism** | Self-regulating (three solver states) | Passive resistance (requires rules for control) |
| **Energy modeling** | Implicit (via head loss when active) | Explicit (K × Q² energy dissipation) |
| **Typical use case** | Pressure zone boundaries, suction protection | Oversized pump correction, flow matching |
| **Implementation complexity** | Moderate (setpoint selection, convergence) | High (K-value mapping, rule logic) |

---

## Practical Guidance for EPANET Implementation

**Before building your model:**
1. Identify whether your objective is pressure regulation (use PRV/PSV) or flow control with energy accounting (use TCV)
2. Verify physical valve locations and obtain setpoints or valve performance curves
3. For TCV: Map valve positions to K-values using manufacturer data—do not assume linearity

**During model setup:**
1. Always place a junction node between pump discharge and any valve link
2. Start with static setpoints/K-values and validate steady-state behavior before adding rules
3. For PRV near pumps: ensure setpoint < pump shutoff head by at least 10-15%
4. For TCV: begin with low K-values and increment gradually in rules

**Validation and troubleshooting:**
1. If you see Warning 04 (status oscillation): tighten hydraulic time step, check for over-constrained pressure requirements, or add realistic pipe resistance between pump and valve
2. Use EPANET's energy report to quantify pumping costs and throttling losses
3. Test extreme scenarios (peak demand, minimum demand, fire flow) to ensure valves behave realistically
4. Remember: EPANET provides discrete-time, rule-based approximation—not continuous feedback control

**What EPANET cannot do:**
- Model transient/water hammer effects
- Simulate valve actuator dynamics (opening speed, response time)
- Represent true PID control loops or continuous feedback
- Model cavitation, wear, or mechanical valve failure modes

For most water distribution planning, design, and extended-period simulation purposes, EPANET's representation of these strategies is adequate. For detailed control system design or transient analysis, you will need specialized software (HAMMER, InfoWorks, or control system simulators).