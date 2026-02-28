# Formulas from ISA-75.01.01-2012.md

Total formulas: 102


## 1 Scope

> At very low ratios of pressure differential to absolute inlet pressure (ΔP / P₁), compressible fluids behave similarly to incompressible fluids. Under such conditions, the sizing equations for compressible flow can be traced to the standard hydrodynamic equations for Newtonian incompressible fluids. However, increasing values of ΔP / P₁ result in compressibility effects which require that the basic equations be modified by appropriate correction factors. The equations for compressible fluids are for use with ideal gas or vapor and are not intended for use with multiphase streams such as gas-liquid, vapor-liquid or gas-solid mixtures. Reasonable accuracy can only be maintained when the specific heat ratio, γ, is restricted to the range 1.08 < γ < 1.65. Refer to Clause 7.2 for more information. For compressible fluid applications, this standard is valid for valves with x_T ≤ 0.84 (see Table D.2). For valves with x_T > 0.84 (e.g. some multistage valves), greater inaccuracy of flow prediction can be expected. Reasonable accuracy can only be maintained for control valves if:

$$\frac{C}{N_{18} d^2} < 0.047$$


## 6.1 Turbulent flow

> The fundamental flow model for incompressible fluids in the turbulent flow regime is given as:

$$Q = C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}} \tag{1}$$


## 6.2.1 Sizing pressure differential, ΔP_sizing

> The value of the pressure differential used in Equation (1) to predict flow rate or compute a required flow coefficient is the lesser of the actual pressure differential or the choked pressure differential:

$$\Delta P_{sizing} = \begin{cases} \Delta P & \text{if } \Delta P < \Delta P_{choked} \\ \Delta P_{choked} & \text{if } \Delta P \geq \Delta P_{choked} \end{cases} \tag{2}$$


## 6.2.2 Choked pressure differential, ΔP_choked

> The condition where further increase in pressure differential at constant upstream pressure no longer produces a corresponding increase in flow through the control valve is designated 'choked flow'. The pressure drop at which this occurs is known as the choked pressure differential and is given by the following equation:

$$\Delta P_{choked} = \left(\frac{F_{LP}}{F_P}\right)^2 (P_1 - F_F P_v) \tag{3}$$


## 6.2.3 Liquid critical pressure ratio factor, F_F

> F_F is the liquid critical pressure ratio factor. This factor is the ratio of the apparent *vena contracta* pressure at choked flow conditions to the vapor pressure of the liquid at inlet temperature. At vapor pressures near zero, this factor is 0.96. Values of F_F may be supplied by the user if known. For single component fluids it may be determined from the curve in Figure D.3 or approximated from the following equation:

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} \tag{4}$$


## 7.1 General

> The fundamental flow model for compressible fluids in the turbulent flow regime is given as:

$$W = C N_6 F_P Y \sqrt{x_{sizing} P_1 \rho_1} \tag{5}$$

> This model establishes the relationship between flow rates, flow coefficients, fluid properties, related installation factors and pertinent service conditions for control valves handling compressible fluids. Two equivalent forms of Equation (5) are presented to accommodate conventional available data formats:

$$W = C N_8 F_P P_1 Y \sqrt{\frac{x_{sizing} M}{T_1 Z_1}} \tag{6}$$

$$Q_s = C N_9 F_P P_1 Y \sqrt{\frac{x_{sizing}}{M T_1 Z_1}} \tag{7}$$


## 7.2.1 Sizing pressure drop ratio, x_sizing

> The value of the pressure drop ratio used in Equations (5) through (7) to predict flow rate or compute a required flow coefficient is the lesser of the actual pressure drop ratio or the choked pressure drop ratio:

$$x_{sizing} = \begin{cases} x & \text{if } x < x_{choked} \\ x_{choked} & \text{if } x \geq x_{choked} \end{cases} \tag{8}$$

> where

$$x = \frac{\Delta P}{P_1} \tag{9}$$


## 7.2.2 Choked pressure drop ratio, x_choked

> The pressure drop ratio at which flow no longer increases with increased value in pressure drop ratio, is the choked pressure drop ratio, given by the following equation:

$$x_{choked} = F_\gamma \, x_{TP} \tag{10}$$


## 7.3 Specific heat ratio factor, F_γ

> The factor x_T is based on air near atmospheric pressure as the flowing fluid with a specific heat ratio of 1.40. If the specific heat ratio for the flowing fluid is not 1.40, the factor F_γ is used to adjust x_T. Use the following equation to calculate the specific heat ratio factor:

$$F_\gamma = \frac{\gamma}{1.4} \tag{11}$$


## 7.4 Expansion factor, Y

> The Reynolds number is the ratio of inertial to viscous forces at the control valve orifice. In the case of compressible flow, its value is beyond the range of influence since turbulent flow almost always exists. The pressure differential ratio x_T is influenced by the specific heat ratio of the fluid. Y shall be calculated using Equation (12).

$$Y = 1 - \frac{x_{sizing}}{3 \, x_{choked}} \tag{12}$$


## 7.5 Compressibility factor, Z

> Several of the sizing equations do not contain a term for the actual density of the fluid at upstream conditions. Instead, the density is inferred from the inlet pressure and temperature based on the laws of ideal gases. Under some conditions, real gas behavior can deviate markedly from the ideal. In these cases, the compressibility factor Z shall be introduced to compensate for the discrepancy. Z is a function of both the reduced pressure and reduced temperature. Reduced pressure P_r is defined as the ratio of the actual inlet absolute pressure to the absolute thermodynamic critical pressure for the fluid in question. The reduced temperature T_r is defined similarly. That is:

$$P_r = \frac{P_1}{P_c} \tag{13}$$

$$T_r = \frac{T_1}{T_c} \tag{14}$$


## 8.2 Estimated piping geometry factor, F_P

> The F_P factor is the ratio of the flow rate through a control valve installed with attached fittings to the flow rate that would result if the control valve was installed without attached fittings and tested under identical conditions which will not produce choked flow in either installation (see Figure 1). When estimated values are permissible, the following equation shall be used:

$$F_P = \frac{1}{\sqrt{1 + \frac{\Sigma\zeta}{N_2} \left(\frac{C}{d^2}\right)^2}} \tag{15}$$

> In this equation, the factor Σζ is the algebraic sum of all of the effective velocity head loss coefficients of all fittings attached to the control valve. The velocity head loss coefficient of the control valve itself is not included.

$$\Sigma\zeta = \zeta_1 + \zeta_2 + \zeta_{B1} - \zeta_{B2} \tag{16}$$

> In cases where the piping diameters approaching and leaving the control valve are different, the ζ_B coefficients are calculated as follows:

$$\zeta_B = 1 - \left(\frac{d}{D}\right)^4 \tag{17}$$

> If the inlet and outlet fittings are short-length, commercially available, concentric reducers, the ζ₁ and ζ₂ coefficients may be approximated as follows: Inlet reducer:

$$\zeta_1 = 0.5 \left[1 - \left(\frac{d}{D_1}\right)^2\right]^2 \tag{18}$$

> Outlet reducer (expander):

$$\zeta_2 = 1.0 \left[1 - \left(\frac{d}{D_2}\right)^2\right]^2 \tag{19}$$

> Inlet and outlet reducers of equal size:

$$\zeta_1 + \zeta_2 = 1.5 \left[1 - \left(\frac{d}{D}\right)^2\right]^2 \tag{20}$$


## 8.3 Estimated combined liquid pressure recovery factor and piping geometry factor with attached fittings, F_LP

> F_L is the liquid pressure recovery factor of the valve without attached fittings. This factor accounts for the influence of the valve internal geometry on the valve capacity at choked flow. It is defined as the ratio of the actual maximum flow rate under choked flow conditions to a theoretical, non-choked flow rate which would be calculated if the pressure differential used was the difference between the valve inlet pressure and the apparent *vena contracta* pressure at choked flow conditions. The factor F_L may be determined from tests in accordance with IEC 60534-2-3. Typical values of F_L versus percent of rated flow coefficient are shown in Figure D.3. F_LP is the combined liquid pressure recovery factor and piping geometry factor for a control valve with attached fittings. It is obtained in the same manner as F_L. To meet a deviation of ±5% for F_LP, F_LP shall be determined by testing. When estimated values are permissible, Equation (21) shall be used:

$$F_{LP} = \frac{F_L}{\sqrt{1 + \frac{F_L^2}{N_2} (\Sigma\zeta_1) \left(\frac{C}{d^2}\right)^2}} \tag{21}$$


## 8.4 Estimated pressure differential ratio factor with attached fittings, x_TP

> NOTE 1 Representative values of x_T for several types of control valves with full size trim and at full rated openings are given in Table D.1. Caution should be exercised in the use of this information. When precise values are required, they should be obtained by test. If a control valve is installed with attached fittings, the value of x_T will be affected. x_TP is the pressure differential ratio factor of a control valve with attached fittings at choked flow. To meet a deviation of ±5% for x_TP, the valve and attached fittings shall be tested as a unit. When estimated values are permissible, Equation (22) shall be used:

$$x_{TP} = \frac{\dfrac{x_T}{F_P^2}}{1 + \dfrac{x_T \, \Sigma\zeta_i}{N_5} \left(\dfrac{C}{d^2}\right)^2} \tag{22}$$


## 9 Reynolds Number, Re_V

> The incompressible and compressible flow models presented in the preceding clauses are for fully developed turbulent flow. When non-turbulent flow conditions are established through a control valve because of a low pressure differential, a high viscosity, a very small flow coefficient, or a combination thereof, a different flow model is required. The valve Reynolds Number, Re_V, is employed to determine whether the flow is fully turbulent. Tests show that flow is fully turbulent when the valve Re_V ≥ 10,000. The valve Reynolds Number is given by Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left(\frac{F_L^2 C^2}{N_2 d^4} + 1\right)^{1/4} \tag{23}$$


## A.3 Discerning a non-turbulent flow condition

> As stated in Clause 9 of the main body of this standard, the valve Reynolds Number, Re_v, is employed to determine whether fully developed turbulent flow exists. The valve Reynolds Number is given by Equation (23) and repeated here for convenience:

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left(\frac{F_L^2 C^2}{N_2 d^4} + 1\right)^{1/4} \tag{A.1}$$


## A.5 Sizing equations for incompressible fluids

> The fundamental flow model for incompressible fluids in the non-turbulent flow regime is given as:

$$Q = C N_1 F_R \sqrt{\frac{\Delta P_{actual}}{\rho_1 / \rho_o}} \tag{A.2}$$


## A.6 Sizing equations for compressible fluids

> The fundamental flow model for compressible fluids in the non-turbulent flow regime is given as:

$$W = C N_{27} F_R Y \sqrt{\frac{\Delta P (P_1 + P_2) M}{T_1}} \tag{A.3}$$

> This model establishes the relationship between flow rates, flow coefficients, fluid properties and pertinent service conditions for control valves handling compressible fluids. An alternate form of Equation (A.3) is presented to accommodate conventional available data formats:

$$Q_s = C N_{22} F_R Y \sqrt{\frac{\Delta P (P_1 + P_2)}{M T_1}} \tag{A.4}$$

> NOTE See Annex D for values of M. where

$$Y = \begin{cases} \dfrac{Re_v - 1{,}000}{9{,}000} \left(1 - \dfrac{x_{sizing}}{3 \cdot x_{choked}} - \sqrt{1 - \dfrac{x}{2}}\right) + \sqrt{1 - \dfrac{x}{2}} & \text{if } 10{,}000 > Re_v \geq 1{,}000 \\[10pt] \sqrt{1 - \dfrac{x}{2}} & \text{if } Re_v < 1{,}000 \end{cases} \tag{A.5}$$


## A.7 Equations for Reynolds Number factor, F_R

> The Reynolds Number factor, F_R, is evaluated from the following equations: If flow is laminar (Re_v < 10),

$$F_R = \operatorname{Min} \begin{bmatrix} \dfrac{0.026}{F_L} \sqrt{n \, Re_v} \\[6pt] 1.00 \end{bmatrix} \tag{A.6}$$

> NOTE The 'Min' function returns the smallest value of the expressions contained in the argument. If flow is transitional (Re_v ≥ 10),

$$F_R = \operatorname{Min} \begin{bmatrix} 1 + \left(\dfrac{0.33 F_L^{1/2}}{n^{1/4}}\right) \log_{10}\left(\dfrac{Re_v}{10{,}000}\right) \\[6pt] \dfrac{0.026}{F_L} \sqrt{n \cdot Re_v} \\[6pt] 1.00 \end{bmatrix} \tag{A.7}$$

> The value of the constant, n, is determined on the basis of trim style. For "full size" trim (C_rated / (d² N₁₈) ≥ 0.016),

$$n = \frac{N_2}{\left(C / d^2\right)^2} \tag{A.8a}$$

> For "reduced trim" (C_rated / (d² N₁₈) < 0.016),

$$n = 1 + N_{32} \left(\frac{C}{d^2}\right)^{2/3} \tag{A.8b}$$


## B.3.3 Multistage multipath control valves

> Globe control valve where the trim has multiple flow passages having several stages which are separated by a gap (see Figure B.1). To ensure the validity of the prediction equations of this annex, the gap should conform to the values calculated from the following equation with a tolerance of +15% and −10% (see Figures B.1 and B.2).

$$gap = A_{HT} \left(\frac{1}{l}\right) \left(\frac{1.6}{\sqrt{D_s}}\right) \tag{B.1}$$


## B.3.5 Continuous resistance trim control valves

> Globe valve where the trim consists of a multistage non-interconnecting multipath throttling restriction of the continuous resistance type, generally referred to as labyrinth valves (see Figures B.3 and B.4). The flow paths should be geometrically similar and should not interconnect but may at some point divide into multiple paths. For incompressible fluids, the cross sectional area of each flow path may be constant but in the case of very high pressure reduction, the area of each flow path may increase to ensure a low exit velocity. For compressible fluids, the area should increase in the direction of flow. The increase should be within these limits:

$$A_1 \times (1.12)^n \leq A_0 \leq A_1 \times (1.23)^n \tag{B.2}$$


## B.4 Expansion factor, Y

> The expansion factor term and function is described in 7.4. For multistage valves, the following expression should be used to evaluate the expansion factor to account for the effects of reheat between stages.

$$Y = \left[1 - \frac{1 - \left(1 - k \dfrac{x}{x_T}\right)^{\beta_1}}{1.212 \, F_\gamma^{\beta_2}}\right] \left(1 + r \, \frac{x^{\beta_3}}{F_\gamma}\right) \tag{B.3}$$


## C.2.2 Step 1 — Define flow function

> All of the flow equations presented in the main body of this document can be rewritten in the following functional form with the flow coefficient, C, as the independent variable:

$$F(C) = [\text{flow rate}] - [\text{defining flow equation}] \tag{C.1}$$

> For example, Equation (1), the incompressible flow equation, may be rewritten in the following functional form:

$$F(C) = Q - C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}} \tag{C.2}$$

> It should be noted that certain terms in the functional expression are dependent on the flow coefficient, C. For the example shown, these terms include the piping correction term, F_P, and the sizing pressure differential, ΔP_sizing. The flow coefficient associated with a given set of service conditions is determined by finding the root of the function, i.e., the value of C such that

$$F(C) = 0 \tag{C.3}$$


## C.2.4 Step 3 — Set upper interval limit

> Setting the initial upper limit of the solution interval must take certain matters into consideration. First, the upper limit should be set to a sufficiently large value to ensure that the interval contains a root. An arbitrarily large value of

$$C_{Upper} = 0.075 \, d^2 \, N_{18} \tag{C.4}$$

> is suggested. This actually corresponds to a value outside the scope of the standard, but should be sufficiently large to capture meaningful real roots. The second issue concerns large values of the flow coefficient, C. Very large values of the flow coefficient in combination with large downstream expansions can potentially result in mathematical singularities associated with Equation (15). To prevent this from occurring, the expression under the radical in Equation (15) can be used to set an upper bound:

$$C_{Upper} = 0.99 \, d^2 \sqrt{-\frac{N_2}{\Sigma\zeta}} \tag{C.5}$$


## C.2.7 Step 6 — Check for convergence

> The root is evaluated and iteration may be discontinued when the upper and lower limits of the interval containing the root are suitably close to each other, i.e., when

$$\left| C_{Upper} - C_{Lower} \right| \leq \varepsilon \tag{C.6}$$

> A suggested value for the convergence tolerance, ε, is 0.00001. When the process has suitably converged, the final value should be set to the mid-point of the interval:

$$C = \frac{C_{Upper} + C_{Lower}}{2} \tag{C.7}$$


## Table C.1 — Incompressible flow

> **Non-choked flow** (x_F,actual < x_F,choked): x_F,choked is to be calculated from Equation (4) with F_P and F_LP under non-choked flow conditions (see this table)

$$F_P = \sqrt{1 - \frac{\Sigma\zeta}{N_2} \left(\frac{C}{d^2}\right)^2}$$

$$F_{LP} = \frac{F_L}{\sqrt{1 + \frac{\zeta_1 + \zeta_{B1}}{N_2} \left(\frac{C}{d^2}\right)^2 \frac{F_L^2}{F_P^2}}}$$

> **Choked flow** (x_F,actual ≥ x_F,choked):

$$F_P = \frac{1 - \dfrac{\Delta P}{P_1 - F_F \cdot P_v} \cdot \dfrac{\zeta_1 + \zeta_{B1}}{N_2} \left(\dfrac{C}{d^2}\right)^2}{\sqrt{1 + \dfrac{\Delta P}{P_1 - F_F \cdot P_v} \cdot \dfrac{1}{N_2} \left(\dfrac{\Sigma\zeta}{F_L^2} - (\zeta_1 + \zeta_{B1})\right) \left(\dfrac{C}{d^2}\right)^2}}$$

$$F_{LP} = F_L \cdot \sqrt{1 - \frac{\Delta P}{P_1 - F_F \cdot P_v} \cdot \frac{\zeta_1 + \zeta_{B1}}{N_2} \left(\frac{C}{d^2}\right)^2}$$


## Table C.2 — Compressible flow

> **Non-choked flow** (x_actual < x_choked): x_choked is to be calculated from Equation (11) with F_P and x_TP under non-choked flow conditions (see this table)

$$F_P = \sqrt{1 - \frac{\Sigma\zeta}{N_2} \left(\frac{C}{d^2}\right)^2}$$

$$x_{TP} = \frac{x_T}{F_P^2 + x_T \cdot \dfrac{\zeta_1 + \zeta_{B1}}{N_5} \left(\dfrac{C}{d^2}\right)^2}$$

> **Choked flow** (x_actual ≥ x_choked):

$$F_P = \sqrt{\frac{1 - \dfrac{9}{4} \cdot \dfrac{\Delta P}{F_\gamma \cdot P_1} \cdot Y^2 \cdot \dfrac{\zeta_1 + \zeta_{B1}}{N_5} \left(\dfrac{C}{d^2}\right)^2}{1 + \dfrac{9}{4} \cdot \dfrac{\Delta P}{F_\gamma \cdot P_1} \cdot Y^2 \cdot \dfrac{1}{N_5} \left(\dfrac{\Sigma\zeta}{x_T} - (\zeta_1 + \zeta_{B1})\right) \left(\dfrac{C}{d^2}\right)^2}}$$

$$x_{TP} = x_T \cdot \left(1 + \frac{\Delta P}{F_\gamma \cdot P_1} \cdot Y^2 \cdot \frac{\zeta_1 + \zeta_{B1}}{N_5} \left(\frac{C}{d^2}\right)^2\right)$$


## Example 1: Incompressible flow — non-choked turbulent flow without attached fittings, solve for K_v

> | Valve style modifier | F_d = 0.46 (from Table D.2) | **Calculations:** The applicable flow model for incompressible fluids in the turbulent flow regime is given in Equation (1):

$$Q = C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}}$$

> - N₄ = 7.07 × 10⁻² - N₁₈ = 8.65 × 10⁻¹ The liquid critical pressure ratio factor, F_F, should be determined using Equation (4):

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} = 0.944$$

> Since the valve is line-sized, F_P = 1 and F_LP = F_L. The choked pressure differential, ΔP_choked, should be determined using Equation (3):

$$\Delta P_{choked} = \left(\frac{F_{LP}}{F_P}\right)^2 (P_1 - F_F P_v) = 497 \text{ kPa}$$

> Next, the sizing pressure differential, ΔP_sizing, should be determined using Equation (2):

$$\Delta P = P_1 - P_2 = 460 \text{ kPa}$$

$$\Delta P_{sizing} = \begin{cases} \Delta P & \text{if } \Delta P < \Delta P_{choked} \\ \Delta P_{choked} & \text{if } \Delta P \geq \Delta P_{choked} \end{cases}$$

$$\Delta P_{sizing} = 460 \text{ kPa}$$

> It should be solved for K_v after rearranging Equation (1):

$$C = K_v = \frac{Q}{N_1 F_P} \sqrt{\frac{\rho_1 / \rho_o}{\Delta P_{sizing}}}$$

> where ρ_o is the density of water at 15 °C

$$K_v = 165 \text{ m}^3/\text{h}$$

> Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 2.97 \times 10^6$$

> Since Re_v > 10,000, the flow is turbulent. It should be verified that the result is within the applicable scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.0085 < 0.047$$


## Example 2: Incompressible flow — choked flow without attached fittings, solve for K_v

> | Valve style modifier | F_d = 0.98 (from Table D.2) | **Calculations:** The applicable flow model for incompressible fluids in the turbulent flow regime is given in Equation (1):

$$Q = C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}}$$

> - N₄ = 7.07 × 10⁻² - N₁₈ = 8.65 × 10⁻¹ The liquid critical pressure ratio factor, F_F, should be determined using Equation (4):

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} = 0.944$$

> Since the valve is line-sized, F_P = 1 and F_LP = F_L. The choked pressure differential, ΔP_choked, should be determined using Equation (3):

$$\Delta P_{choked} = \left(\frac{F_{LP}}{F_P}\right)^2 (P_1 - F_F P_v) = 221 \text{ kPa}$$

> Next, the sizing pressure differential, ΔP_sizing, should be determined using Equation (2):

$$\Delta P = P_1 - P_2 = 460 \text{ kPa}$$

$$\Delta P_{sizing} = \begin{cases} \Delta P & \text{if } \Delta P < \Delta P_{choked} \\ \Delta P_{choked} & \text{if } \Delta P \geq \Delta P_{choked} \end{cases}$$

$$\Delta P_{sizing} = 221 \text{ kPa}$$

> It should be solved for K_v after rearranging Equation (1):

$$C = K_v = \frac{Q}{N_1 F_P} \sqrt{\frac{\rho_1 / \rho_o}{\Delta P_{sizing}}}$$

> where ρ_o is the density of water at 15 °C

$$K_v = 238 \text{ m}^3/\text{h}$$

> Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 6.60 \times 10^6$$

> Since Re_v > 10,000, the flow is turbulent. It should be verified that the result is within the scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.028 < 0.047$$


## Example 3: Compressible flow — non-choked flow, solve for K_v

> | Valve style modifier | F_d = 0.42 (from Table D.2) | **Calculations:** The applicable flow model for compressible fluids in the turbulent flow regime with the dataset given is found in Equation (7):

$$Q_s = C N_9 F_P P_1 Y \sqrt{\frac{x_{sizing}}{M T_1 Z_1}}$$

> - N₁₈ = 8.65 × 10⁻¹ Since the valve is line-sized, F_P = 1 and x_TP = x_T. The specific heat ratio factor, F_γ, should be calculated using Equation (11):

$$F_\gamma = \frac{\gamma}{1.40} = 0.929$$

> The choked pressure drop ratio, x_choked, should be determined using Equation (10):

$$x_{choked} = F_\gamma x_{TP} = 0.557$$

> Next, the sizing pressure drop ratio, x_sizing, should be determined using Equations (8) and (9):

$$x = \frac{P_1 - P_2}{P_1} = 0.338$$

$$x_{sizing} = \begin{cases} x & \text{if } x < x_{choked} \\ x_{choked} & \text{if } x \geq x_{choked} \end{cases}$$

$$x_{sizing} = 0.338$$

> The expansion factor, Y, should be calculated using Equation (12):

$$Y = 1 - \frac{x_{sizing}}{3 \, x_{choked}} = 0.798$$

> It should be solved for K_v after rearranging Equation (7):

$$C = K_v = \frac{Q_s}{N_9 F_P P_1 Y} \sqrt{\frac{M T_1 Z_1}{x_{sizing}}}$$

$$K_v = 67.2 \text{ m}^3/\text{h}$$

> The actual volumetric flow rate should be found:

$$Q = Q_s \frac{P_s T_1 Z_1}{P_1 T_s Z_s} = 895.4 \text{ m}^3/\text{h}$$

> Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 1.40 \times 10^6$$

> Since Re_v > 10,000, the flow is turbulent. It should be verified that the result is within the scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.0078 < 0.047$$


## Example 4: Compressible flow — choked flow, solve for K_v

> | Valve style modifier | F_d = 0.42 (from Table D.2) | **Calculations:** The applicable flow model for compressible fluids in the turbulent flow regime with the dataset given is found in Equation (7):

$$Q_s = C N_9 F_P P_1 Y \sqrt{\frac{x_{sizing}}{M T_1 Z_1}}$$

> - N₁₈ = 8.65 × 10⁻¹ Since the valve is line-sized, F_P = 1 and x_TP = x_T. The specific heat ratio factor, F_γ, should be calculated using Equation (11):

$$F_\gamma = \frac{\gamma}{1.40} = 0.929$$

> The choked pressure drop ratio, x_choked, should be determined using Equation (10):

$$x_{choked} = F_\gamma x_{TP} = 0.557$$

> Next, the sizing pressure drop ratio, x_sizing, should be determined using Equations (8) and (9):

$$x = \frac{P_1 - P_2}{P_1} = 0.632$$

$$x_{sizing} = \begin{cases} x & \text{if } x < x_{choked} \\ x_{choked} & \text{if } x \geq x_{choked} \end{cases}$$

$$x_{sizing} = 0.557$$

> The expansion factor, Y, should be calculated using Equation (12):

$$Y = 1 - \frac{x_{sizing}}{3 \, x_{choked}} = 0.667$$

> It should be solved for K_v after rearranging Equation (7):

$$C = K_v = \frac{Q_s}{N_9 F_P P_1 Y} \sqrt{\frac{M T_1 Z_1}{x_{sizing}}}$$

$$K_v = 62.6 \text{ m}^3/\text{h}$$

> The actual volumetric flow rate should be found:

$$Q = Q_s \frac{P_s T_1 Z_1}{P_1 T_s Z_s} = 895.4 \text{ m}^3/\text{h}$$

> Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 1.45 \times 10^6$$

> Since Re_v > 10,000, the flow is turbulent. It should be verified that the result is within the scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.0073 < 0.047$$


## Example 5: Incompressible fluid — choked flow with attached fittings

> - N₁ = 0.0865 - N₂ = 0.00214 - N₁₈ = 1.00

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} = 0.956$$

$$\zeta_1 = 0.5 \left[1 - \left(\frac{d}{D_1}\right)^2\right]^2 = 0.160$$

$$\zeta_2 = \left[1 - \left(\frac{d}{D_2}\right)^2\right]^2 = 0.561$$

$$\zeta_{B1} = 1 - \left(\frac{d}{D_1}\right)^4 = 0.811$$

$$\zeta_{B2} = 1 - \left(\frac{d}{D_2}\right)^4 = 0.937$$

> **Step 1:** A flow function per Equation (C.2) should be defined:

$$F(C) = 750 - C \cdot N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}}$$

> **Final Value: C = 183.7** **Step 7:** The solution should be confirmed: Calculate the predicted flow rate using the computed value of the flow coefficient and compare to given value of flow rate:

$$Q_{predicted} = C \cdot N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}} = 749$$

