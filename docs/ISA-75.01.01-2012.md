# ANSI/ISA-75.01.01-2012 (60534-2-1 MOD)

## Industrial-Process Control Valves — Part 2-1: Flow capacity — Sizing equations for fluid flow under installed conditions

**Approved 27 August 2012 — Second Printing 2 October 2013**

ISBN: 978-1-937560-61-4

Copyright 2012 by IEC and ISA. All rights reserved. Not for resale. Printed in the United States of America. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means (electronic, mechanical, photocopying, recording, or otherwise), without the prior written permission of the Publisher.

ISA 67 Alexander Drive P. O. Box 12277 Research Triangle Park, North Carolina 27709

---

## Preface

This preface, as well as all footnotes and annexes, is included for information purposes and is not part of ANSI/ISA-75.01.01-2012 (60534-2-1 MOD).

This Standard has been prepared as part of the service of ISA toward a goal of uniformity in the field of instrumentation. To be of real value, this document should not be static but should be subject to periodic review. Toward this end, the Society welcomes all comments and criticisms and asks that they be addressed to the Secretary, Standards and Practices Board; ISA; 67 Alexander Drive; P. O. Box 12277; Research Triangle Park, NC 27709; Telephone (919) 549-8411; Fax (919) 549-8288; E-mail: standards@isa.org.

The ISA Standards and Practices Department is aware of the growing need for attention to the metric system of units in general, and the International System of Units (SI) in particular, in the preparation of instrumentation standards. The Department is further aware of the benefits to USA users of ISA standards of incorporating suitable references to the SI (and the metric system) in their business and professional dealings with other countries. Toward this end, this Department will endeavour to introduce SI-acceptable metric units in all new and revised standards, recommended practices, and technical reports to the greatest extent possible. IEEE/ASTM SI 10, American National Standard for Metric Practice, and future revisions, will be the reference guide for definitions, symbols, abbreviations, and conversion factors.

It is the policy of ISA to encourage and welcome the participation of all concerned individuals and interests in the development of ISA standards, recommended practices, and technical reports. Participation in the ISA standards-making process by an individual in no way constitutes endorsement by the employer of that individual, of ISA, or of any of the standards, recommended practices, and technical reports that ISA develops.

CAUTION — ISA DOES NOT TAKE ANY POSITION WITH RESPECT TO THE EXISTENCE OR VALIDITY OF ANY PATENT RIGHTS ASSERTED IN CONNECTION WITH THIS DOCUMENT, AND ISA DISCLAIMS LIABILITY FOR THE INFRINGEMENT OF ANY PATENT RESULTING FROM THE USE OF THIS DOCUMENT. USERS ARE ADVISED THAT DETERMINATION OF THE VALIDITY OF ANY PATENT RIGHTS, AND THE RISK OF INFRINGEMENT OF SUCH RIGHTS, IS ENTIRELY THEIR OWN RESPONSIBILITY.

PURSUANT TO ISA'S PATENT POLICY, ONE OR MORE PATENT HOLDERS OR PATENT APPLICANTS MAY HAVE DISCLOSED PATENTS THAT COULD BE INFRINGED BY USE OF THIS DOCUMENT AND EXECUTED A LETTER OF ASSURANCE COMMITTING TO THE GRANTING OF A LICENSE ON A WORLDWIDE, NON-DISCRIMINATORY BASIS, WITH A FAIR AND REASONABLE ROYALTY RATE AND FAIR AND REASONABLE TERMS AND CONDITIONS. FOR MORE INFORMATION ON SUCH DISCLOSURES AND LETTERS OF ASSURANCE, CONTACT ISA OR VISIT WWW.ISA.ORG/STANDARDSPATENTS.

OTHER PATENTS OR PATENT CLAIMS MAY EXIST FOR WHICH A DISCLOSURE OR LETTER OF ASSURANCE HAS NOT BEEN RECEIVED. ISA IS NOT RESPONSIBLE FOR IDENTIFYING PATENTS OR PATENT APPLICATIONS FOR WHICH A LICENSE MAY BE REQUIRED, FOR CONDUCTING INQUIRIES INTO THE LEGAL VALIDITY OR SCOPE OF PATENTS, OR DETERMINING WHETHER ANY LICENSING TERMS OR CONDITIONS PROVIDED IN CONNECTION WITH SUBMISSION OF A LETTER OF ASSURANCE, IF ANY, OR IN ANY LICENSING AGREEMENTS ARE REASONABLE OR NON-DISCRIMINATORY.

ISA REQUESTS THAT ANYONE REVIEWING THIS DOCUMENT WHO IS AWARE OF ANY PATENTS THAT MAY IMPACT IMPLEMENTATION OF THE DOCUMENT NOTIFY THE ISA STANDARDS AND PRACTICES DEPARTMENT OF THE PATENT AND ITS OWNER.

ADDITIONALLY, THE USE OF THIS DOCUMENT MAY INVOLVE HAZARDOUS MATERIALS, OPERATIONS OR EQUIPMENT. THE DOCUMENT CANNOT ANTICIPATE ALL POSSIBLE APPLICATIONS OR ADDRESS ALL POSSIBLE SAFETY ISSUES ASSOCIATED WITH USE IN HAZARDOUS CONDITIONS. THE USER OF THIS DOCUMENT MUST EXERCISE SOUND PROFESSIONAL JUDGMENT CONCERNING ITS USE AND APPLICABILITY UNDER THE USER'S PARTICULAR CIRCUMSTANCES. THE USER MUST ALSO CONSIDER THE APPLICABILITY OF ANY GOVERNMENTAL REGULATORY LIMITATIONS AND ESTABLISHED SAFETY AND HEALTH PRACTICES BEFORE IMPLEMENTING THIS DOCUMENT. THE USER OF THIS DOCUMENT SHOULD BE AWARE THAT THIS DOCUMENT MAY BE IMPACTED BY ELECTRONIC SECURITY ISSUES. THE COMMITTEE HAS NOT YET ADDRESSED THE POTENTIAL ISSUES IN THIS VERSION.

### ISA Subcommittee ISA75.01 Members

| Name | Company |
|------|---------|
| T. George, Chair | Richards Industries |
| W. Weidman, Managing Director | WCW Consulting |
| H. Baumann | H B Services Partners LLC |
| H. Boger | Masoneilan Dresser |
| G. Borden | Consultant |
| S. Boyle | Metso Automation USA Inc. |
| E. Bunke | Badger Meter |
| C. Crawford | Consultant |
| J. Faramarzi | Control Components Inc. |
| A. Glenn | Flowserve Corp. |
| H. Hoffmann | Consultant |
| J. Kiesbauer | Samson Aktiengesellschaft |
| J. McCaskill | Expro Group |
| A. McCauley | Chagrin Valley Controls Inc. |
| V. Mezzano | Fluor Corp. |
| J. Reed | Consultant |
| J. Reid | Cashco Inc. |
| M. Riveland | Emerson Process Management |
| E. Skovgaard | Control Valve Solutions |
| F. Volpe | Masoneilan Dresser |
| J. Young | The Dow Chemical Company |

This standard was approved for publication by the ISA Standards and Practices Board on 30 July 2012.

---

## CONTENTS

- **FOREWORD** ..... 9
- **1** Scope ..... 11
- **2** Normative references ..... 12
- **3** Terms and definitions ..... 12
- **4** Symbols ..... 13
- **5** Installation ..... 14
- **6** Sizing equations for incompressible fluids ..... 15
  - 6.1 Turbulent flow ..... 15
  - 6.2 Pressure differentials ..... 16
    - 6.2.1 Sizing pressure differential, ΔP_sizing ..... 16
    - 6.2.2 Choked pressure differential, ΔP_choked ..... 16
    - 6.2.3 Liquid critical pressure ratio factor, F_F ..... 16
  - 6.3 Non-turbulent (laminar and transitional) flow ..... 16
- **7** Sizing equations for compressible fluids ..... 17
  - 7.1 General ..... 17
  - 7.2 Pressure differentials ..... 17
    - 7.2.1 Sizing pressure drop ratio, x_sizing ..... 17
    - 7.2.2 Choked pressure drop ratio, x_choked ..... 17
  - 7.3 Specific heat ratio factor, F_γ ..... 18
  - 7.4 Expansion factor, Y ..... 18
  - 7.5 Compressibility factor, Z ..... 19
  - 7.6 Non-turbulent (laminar and transitional) flow ..... 19
- **8** Correction factors common to both incompressible and compressible flow ..... 19
  - 8.1 Piping geometry correction factors ..... 19
  - 8.2 Estimated piping geometry factor, F_P ..... 20
  - 8.3 Estimated combined liquid pressure recovery factor and piping geometry factor with attached fittings, F_LP ..... 21
  - 8.4 Estimated pressure differential ratio factor with attached fittings, x_TP ..... 21
- **9** Reynolds Number, Re_V ..... 22
- **Annex A** (normative) Sizing equations for non-turbulent flow ..... 25
- **Annex B** (informative) Sizing equations for compressible fluid flow through multistage control valves ..... 29
- **Annex C** (informative) Piping factor computational considerations ..... 37
- **Annex D** (informative) Engineering data ..... 43
- **Annex E** (informative) Reference calculations ..... 53
- **Bibliography** ..... 67

### List of Figures

- Figure 1 — Reference pipe section for sizing ..... 15
- Figure B.1 — Multistage multipath trim ..... 31
- Figure B.2 — Multistage single path trim ..... 32
- Figure B.3 — Disk from a continuous resistance trim ..... 33
- Figure B.4 — Sectional view of continuous resistance trim with multiple flow passages having vertical undulations ..... 33
- Figure C.1 — Determination of the upper limit of the flow coefficient by the iterative method ..... 41
- Figure C.2 — Determination of the final flow coefficient by the iterative method ..... 42
- Figure D.1 — Piping geometry factors ..... 47
- Figure D.2 — Pressure recovery factors ..... 50
- Figure D.3 — Liquid critical pressure ratio factor F_F ..... 51

### List of Tables

- Table 1 — Numerical constants N ..... 23
- Table B.1 — Values of the stage interaction factors, k, and the reheat factors, r for multistage single and multipath control valve trim ..... 35
- Table B.2 — Values of the stage interaction factors, k, and the reheat factors, r for continuous resistance control valve trim ..... 35
- Table C.1 — Incompressible flow ..... 40
- Table C.2 — Compressible flow ..... 40
- Table D.1 — Typical values of valve style modifier F_d, liquid pressure recovery factor F_L and pressure differential ratio factor x_T at full rated travel ..... 44
- Table D.2 — Physical constants of gases and vapor ..... 52

---

## INTERNATIONAL ELECTROTECHNICAL COMMISSION

## INDUSTRIAL-PROCESS CONTROL VALVES — Part 2-1: Flow capacity — Sizing equations for fluid flow under installed conditions

## FOREWORD

1. The International Electrotechnical Commission (IEC) is a worldwide organization for standardization comprising all national electrotechnical committees (IEC National Committees). The object of IEC is to promote international cooperation on all questions concerning standardization in the electrical and electronic fields. To this end and in addition to other activities, IEC publishes International Standards, Technical Specifications, Technical Reports, Publicly Available Specifications (PAS) and Guides (hereafter referred to as 'IEC Publication(s)'). Their preparation is entrusted to technical committees; any IEC National Committee interested in the subject dealt with may participate in this preparatory work. International, governmental and non-governmental organizations liaising with the IEC also participate in this preparation. IEC collaborates closely with the International Organization for Standardization (ISO) in accordance with conditions determined by agreement between the two organizations.

2. The formal decisions or agreements of IEC on technical matters express, as nearly as possible, an international consensus of opinion on the relevant subjects since each technical committee has representation from all interested IEC National Committees.

3. IEC Publications have the form of recommendations for international use and are accepted by IEC National Committees in that sense. While all reasonable efforts are made to ensure that the technical content of IEC Publications is accurate, IEC cannot be held responsible for the way in which they are used or for any misinterpretation by any end user.

4. In order to promote international uniformity, IEC National Committees undertake to apply IEC Publications transparently to the maximum extent possible in their national and regional publications. Any divergence between any IEC Publication and the corresponding national or regional publication shall be clearly indicated in the latter.

5. IEC itself does not provide any attestation of conformity. Independent certification bodies provide conformity assessment services and, in some areas, access to IEC marks of conformity. IEC is not responsible for any services carried out by independent certification bodies.

6. All users should ensure that they have the latest edition of this publication.

7. No liability shall attach to IEC or its directors, employees, servants or agents including individual experts and members of its technical committees and IEC National Committees for any personal injury, property damage or other damage of any nature whatsoever, whether direct or indirect, or for costs (including legal fees) and expenses arising out of the publication, use of, or reliance upon, this IEC Publication or any other IEC Publications.

8. Attention is drawn to the Normative references cited in this publication. Use of the referenced publications is indispensable for the correct application of this publication.

9. Attention is drawn to the possibility that some of the elements of this IEC Publication may be the subject of patent rights. IEC shall not be held responsible for identifying any or all such patent rights.

International Standard IEC 60534-2-1 has been prepared by subcommittee 65B: Measurement and control devices, of IEC technical committee 65: Industrial-process measurement, control and automation.

This second edition cancels and replaces the first edition published in 1998. This edition constitutes a technical revision.

This edition includes the following significant technical changes with respect to the previous edition:

- the same fundamental flow model, but changes the equation framework to simplify the use of the standard by introducing the notion of ΔP_sizing;
- changes to the non-turbulent flow corrections and means of computing results;
- multi-stage sizing as an Annex.

The text of this standard is based on the following documents:

| FDIS | Report on voting |
|------|-----------------|
| 65B/783/FDIS | 65B/786/RVD |

Full information on the voting for the approval of this standard can be found in the report on voting indicated in the above table.

This publication has been drafted in accordance with the ISO/IEC Directives, Part 2.

A list of all the parts of the IEC 60534 series, under the general title *Industrial-process control valves*, can be found on the IEC website.

The committee has decided that the contents of this publication will remain unchanged until the stability date indicated on the IEC web site under "http://webstore.iec.ch" in the data related to the specific publication. At this date, the publication will be

- reconfirmed,
- withdrawn,
- replaced by a revised edition, or
- amended.

---

## 1 Scope

This standard includes equations for predicting the flow of compressible and incompressible fluids through control valves.

The equations for incompressible flow are based on standard hydrodynamic equations for Newtonian incompressible fluids. They are not intended for use when non-Newtonian fluids, fluid mixtures, slurries or liquid-solid conveyance systems are encountered. The equations for incompressible flow may be used with caution for non-vaporizing multi-component liquid mixtures. Refer to Clause 6 for additional information.

At very low ratios of pressure differential to absolute inlet pressure (ΔP / P₁), compressible fluids behave similarly to incompressible fluids. Under such conditions, the sizing equations for compressible flow can be traced to the standard hydrodynamic equations for Newtonian incompressible fluids. However, increasing values of ΔP / P₁ result in compressibility effects which require that the basic equations be modified by appropriate correction factors. The equations for compressible fluids are for use with ideal gas or vapor and are not intended for use with multiphase streams such as gas-liquid, vapor-liquid or gas-solid mixtures. Reasonable accuracy can only be maintained when the specific heat ratio, γ, is restricted to the range 1.08 < γ < 1.65. Refer to Clause 7.2 for more information.

For compressible fluid applications, this standard is valid for valves with x_T ≤ 0.84 (see Table D.2). For valves with x_T > 0.84 (e.g. some multistage valves), greater inaccuracy of flow prediction can be expected.

Reasonable accuracy can only be maintained for control valves if:

$$\frac{C}{N_{18} d^2} < 0.047$$

Note that while the equation structure utilized in this document departs radically from previous versions of the standard, the basic technology is relatively unchanged. The revised equation format was adopted to simplify presentation of the various equations and improve readability of the document.

The accuracy of results computed with the equations in this standard will be governed by the accuracy of the constituent coefficients and the process data supplied. Methods of evaluating the coefficients used in the equations presented herein are given in IEC 60534-2-3. The stated accuracy associated with the coefficients in that document is ±5% when C/d² < 0.047 N₁₈.

---

## 2 Normative references

The following referenced documents are indispensable for the application of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

- IEC 60534-1:2005, *Industrial-process control valves — Part 1: Control valve terminology and general considerations*
- IEC 60534-2-3:1997, *Industrial-process control valves — Part 2-3: Flow capacity — Test procedures*
- ANSI/ISA-75.02.01-2008 (IEC 60534-2-3 Mod), *Control Valve Capacity Test Procedures*
- ANSI/ISA-75.05.01-2000 (R2005), *Control Valve Terminology*

---

## 3 Terms and definitions

For the purposes of this document, the terms and definitions given in IEC 60534-1, and the following apply.

### 3.1 Valve style modifier

The ratio of the hydraulic diameter of a single flow passage to the diameter of a circular orifice, the area of which is equivalent to the sum of areas of all identical flow passages at a given travel. It should be stated by the manufacturer as a function of travel (see Annex A).

### 3.2 Standard volumetric flowrates

Compressible fluid volumetric flow rates in cubic meters per hour, identified by the symbol Q_S, refer to either:

- a) Standard conditions, which is an absolute pressure of 1,013.25 mbar and a temperature of 288.6 K, or
- b) Normal conditions, which is an absolute pressure of 1,013.25 mbar and a temperature of 273 K.

Numerical constants for the flow equations are provided for both conventions (see Table 1).

---

## 4 Symbols

| Symbol | Description | Unit |
|--------|-------------|------|
| C | Flow coefficient (K_v, C_v) | Various (see IEC 60534-1) (see Note 4) |
| d | Nominal valve size | mm (in) |
| D | Internal diameter of the piping | mm (in) |
| D₁ | Internal diameter of upstream piping | mm (in) |
| D₂ | Internal diameter of downstream piping | mm (in) |
| D_o | Orifice diameter | mm (in) |
| F_d | Valve style modifier (see Annex A) | Dimensionless (see Note 4) |
| F_F | Liquid critical pressure ratio factor | Dimensionless |
| F_L | Liquid pressure recovery factor of a control valve without attached fittings | Dimensionless (see Note 4) |
| F_LP | Combined liquid pressure recovery factor and piping geometry factor of a control valve with attached fittings | Dimensionless |
| F_P | Piping geometry factor | Dimensionless |
| F_R | Reynolds number factor | Dimensionless |
| F_γ | Specific heat ratio factor | Dimensionless |
| M | Molecular mass of flowing fluid | kg/kmol (lbm/lbm-mol) |
| N | Numerical constants (see Table 1) | Various (see Note 1) |
| P₁ | Inlet absolute static pressure measured at point A (see Figure 1) | kPa or bar (psia) (see Note 2) |
| P₂ | Outlet absolute static pressure measured at point B (see Figure 1) | kPa or bar (psia) |
| P_c | Absolute thermodynamic critical pressure | kPa or bar (psia) |
| P_r | Reduced pressure (P₁ / P_c) | Dimensionless |
| P_v | Absolute vapor pressure of the liquid at inlet temperature | kPa or bar (psia) |
| ΔP_actual | Differential pressure between upstream and downstream pressure taps (P₁ − P₂) | kPa or bar (psia) |
| ΔP_choked | Computed value of limiting pressure differential for incompressible flow | kPa or bar (psia) |
| ΔP_sizing | Value of pressure differential used in computing flow or required flow coefficient for incompressible flows | kPa or bar (psia) |
| Q | Actual volumetric flow rate | m³/h (ft³/h) |
| Q_S | Standard volumetric flow rate (see definition 3.2) | m³/h (scfh) |
| Re_v | Valve Reynolds number | Dimensionless |
| T₁ | Inlet absolute temperature | K (°R) |
| T_c | Absolute thermodynamic critical temperature | K (°R) |
| T_r | Reduced temperature (T₁ / T_c) | Dimensionless |
| t_s | Absolute reference temperature for standard cubic meter | K (°R) |
| W | Mass flow rate | kg/h (lbm/h) |
| x | Ratio of actual pressure differential to inlet absolute pressure (ΔP / P₁) | Dimensionless |
| x_choked | Choked pressure drop ratio for compressible flow | Dimensionless |
| x_sizing | Value of pressure drop ratio used in computing flow or required flow coefficient for compressible flows | Dimensionless |
| x_T | Pressure differential ratio factor of a control valve without attached fittings at choked flow | Dimensionless (see Note 4) |
| x_TP | Pressure differential ratio factor of a control valve with attached fittings at choked flow | Dimensionless |
| Y | Expansion factor | Dimensionless |
| Z₁ | Compressibility factor at inlet conditions | Dimensionless |
| ν | Kinematic viscosity | m²/s (cS) (see Note 3) |
| ρ₁ | Density of fluid at P₁ and T₁ | kg/m³ (lbm/ft³) |
| ρ₁/ρ_o | Relative density (ρ₁/ρ_o = 1.0 for water at 15 °C) | Dimensionless |
| γ | Specific heat ratio | Dimensionless |
| ζ | Velocity head loss coefficient of a reducer, expander or other fitting attached to a control valve or valve trim | Dimensionless |
| ζ₁ | Upstream velocity head loss coefficient of fitting | Dimensionless |
| ζ₂ | Downstream velocity head loss coefficient of fitting | Dimensionless |
| ζ_B1 | Inlet Bernoulli coefficient | Dimensionless |
| ζ_B2 | Outlet Bernoulli coefficient | Dimensionless |

NOTE 1 To determine the units for the numerical constants, dimensional analysis may be performed on the appropriate equations using the units given in Table 1.

NOTE 2 1 bar = 10² kPa = 10⁵ Pa

NOTE 3 1 centistoke = 10⁻⁶ m²/s

NOTE 4 These values are travel-related and should be stated by the manufacturer.

---

## 5 Installation

In many industrial applications, reducers or other fittings are attached to the control valves. The effect of these types of fittings on the nominal flow coefficient of the control valve can be significant. A correction factor is introduced to account for this effect. Additional factors are introduced to take account of the fluid property characteristics that influence the flow capacity of a control valve.

In sizing control valves, using the relationships presented herein, the flow coefficients calculated are assumed to include all head losses between points A and B, as shown in Figure 1.

<!-- image -->

*IEC 509/11*

l₁ = two nominal pipe diameters

l₂ = six nominal pipe diameters

**Figure 1 — Reference pipe section for sizing**

---

## 6 Sizing equations for incompressible fluids

### 6.1 Turbulent flow

The fundamental flow model for incompressible fluids in the turbulent flow regime is given as:

$$Q = C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}} \tag{1}$$

NOTE 1 The numerical constant N₁ depends on the units used in the general sizing equation and the type of flow coefficient: K_v or C_v.

NOTE 2 The piping geometry factor, F_P, reduces to unity when the valve size and adjoining pipe sizes are identical. Refer to 8.1 for evaluation and additional information.

This model establishes the relationship between flow rate, flow coefficient, fluid properties, related installation factors, and pertinent service conditions for control valves handling incompressible fluids. Equation (1) may be used to compute the required flow coefficient, the flow rate or applied pressure differential given any two of the three quantities.

This model rigorously applies only to single component, single phase fluids (i.e., no multi-phase mixtures, no multi-component mixtures). However, this model may be used with caution under certain conditions for multi-component mixtures in the liquid phase. The underlying assumptions of the flow model would be satisfied for liquid-liquid fluid mixtures subject to the following restrictions:

- the mixture is homogenous;
- the mixture is in chemical and thermodynamic equilibrium;
- the entire throttling process occurs well away from the multiphase region.

When these conditions are satisfied, the mixture density should be substituted for the fluid density ρ₁ in Equation (1).

### 6.2 Pressure differentials

#### 6.2.1 Sizing pressure differential, ΔP_sizing

The value of the pressure differential used in Equation (1) to predict flow rate or compute a required flow coefficient is the lesser of the actual pressure differential or the choked pressure differential:

$$\Delta P_{sizing} = \begin{cases} \Delta P & \text{if } \Delta P < \Delta P_{choked} \\ \Delta P_{choked} & \text{if } \Delta P \geq \Delta P_{choked} \end{cases} \tag{2}$$

#### 6.2.2 Choked pressure differential, ΔP_choked

The condition where further increase in pressure differential at constant upstream pressure no longer produces a corresponding increase in flow through the control valve is designated 'choked flow'. The pressure drop at which this occurs is known as the choked pressure differential and is given by the following equation:

$$\Delta P_{choked} = \left(\frac{F_{LP}}{F_P}\right)^2 (P_1 - F_F P_v) \tag{3}$$

NOTE The expression (F_LP / F_P)² reduces to F_L² when the valve size and adjoining pipe sizes are identical. Refer to 8.1 for more information.

#### 6.2.3 Liquid critical pressure ratio factor, F_F

F_F is the liquid critical pressure ratio factor. This factor is the ratio of the apparent *vena contracta* pressure at choked flow conditions to the vapor pressure of the liquid at inlet temperature. At vapor pressures near zero, this factor is 0.96.

Values of F_F may be supplied by the user if known. For single component fluids it may be determined from the curve in Figure D.3 or approximated from the following equation:

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} \tag{4}$$

Use of Equation (4) to describe the onset of choking of multi-component mixtures is subject to the applicability of appropriate corresponding states parameters in the flashing model.

### 6.3 Non-turbulent (laminar and transitional) flow

The flow model embodied in Equation (1) is for fully developed, turbulent flow only. Non-turbulent conditions may be encountered, especially when flow rates are quite low or fluid viscosity is appreciable. To affirm the applicability of Equation (1), the value of the valve Reynolds Number (see Equation (23)) should be computed. Equation (1) is applicable if Re_V ≥ 10,000.

---

## 7 Sizing equations for compressible fluids

### 7.1 General

The fundamental flow model for compressible fluids in the turbulent flow regime is given as:

$$W = C N_6 F_P Y \sqrt{x_{sizing} P_1 \rho_1} \tag{5}$$

This model establishes the relationship between flow rates, flow coefficients, fluid properties, related installation factors and pertinent service conditions for control valves handling compressible fluids.

Two equivalent forms of Equation (5) are presented to accommodate conventional available data formats:

$$W = C N_8 F_P P_1 Y \sqrt{\frac{x_{sizing} M}{T_1 Z_1}} \tag{6}$$

$$Q_s = C N_9 F_P P_1 Y \sqrt{\frac{x_{sizing}}{M T_1 Z_1}} \tag{7}$$

NOTE See Annex D for values of M.

Equation (6) is derived by substituting the fluid density as computed from the ideal gas equation-of-state into Equation (5). Equation (7) expresses the flow rate in standard volumetric units. Equations (5) through (7) may be used to compute the required flow coefficient, the flow rate or applied pressure differential given any two of the three quantities.

### 7.2 Pressure differentials

#### 7.2.1 Sizing pressure drop ratio, x_sizing

The value of the pressure drop ratio used in Equations (5) through (7) to predict flow rate or compute a required flow coefficient is the lesser of the actual pressure drop ratio or the choked pressure drop ratio:

$$x_{sizing} = \begin{cases} x & \text{if } x < x_{choked} \\ x_{choked} & \text{if } x \geq x_{choked} \end{cases} \tag{8}$$

where

$$x = \frac{\Delta P}{P_1} \tag{9}$$

#### 7.2.2 Choked pressure drop ratio, x_choked

The pressure drop ratio at which flow no longer increases with increased value in pressure drop ratio, is the choked pressure drop ratio, given by the following equation:

$$x_{choked} = F_\gamma \, x_{TP} \tag{10}$$

NOTE The expression x_TP reduces to x_T when the valve size and adjoining pipe sizes are identical. Refer to 8.1 for more information.

### 7.3 Specific heat ratio factor, F_γ

The factor x_T is based on air near atmospheric pressure as the flowing fluid with a specific heat ratio of 1.40. If the specific heat ratio for the flowing fluid is not 1.40, the factor F_γ is used to adjust x_T. Use the following equation to calculate the specific heat ratio factor:

$$F_\gamma = \frac{\gamma}{1.4} \tag{11}$$

NOTE See Annex D for values of γ and F_γ.

Equation (11) evolved from assumption of perfect gas behaviour and extension of an orifice plate model based on air and steam testing to control valves. Analysis of that model over a range of 1.08 < γ < 1.65 leads to adoption of the current linear model embodied in Equation (11). The difference between the original orifice model, other theoretical models and Equation (11) is small within this range. However, the differences become significant outside of the indicated range. For maximum accuracy, flow calculations based on this model should be restricted to a specific heat ratio within this range and to ideal gas behaviour.

### 7.4 Expansion factor, Y

The expansion factor Y accounts for the change in density as the fluid passes from the valve inlet to the *vena contracta* (the location just downstream of the orifice where the jet stream area is a minimum). It also accounts for the change in the *vena contracta* area as the pressure differential is varied.

Theoretically, Y is affected by all of the following:

- a) ratio of port area to body inlet area;
- b) shape of the flow path;
- c) pressure differential ratio x;
- d) Reynolds number;
- e) specific heat ratio γ.

The influence of items a), b), c), and e) is accounted for by the pressure differential ratio factor x_T, which may be established by air test and which is discussed in 8.4.

The Reynolds number is the ratio of inertial to viscous forces at the control valve orifice. In the case of compressible flow, its value is beyond the range of influence since turbulent flow almost always exists.

The pressure differential ratio x_T is influenced by the specific heat ratio of the fluid.

Y shall be calculated using Equation (12).

$$Y = 1 - \frac{x_{sizing}}{3 \, x_{choked}} \tag{12}$$

NOTE The expansion factor, Y, has a limiting value of 2/3 under choked flow conditions.

### 7.5 Compressibility factor, Z

Several of the sizing equations do not contain a term for the actual density of the fluid at upstream conditions. Instead, the density is inferred from the inlet pressure and temperature based on the laws of ideal gases. Under some conditions, real gas behavior can deviate markedly from the ideal. In these cases, the compressibility factor Z shall be introduced to compensate for the discrepancy. Z is a function of both the reduced pressure and reduced temperature. Reduced pressure P_r is defined as the ratio of the actual inlet absolute pressure to the absolute thermodynamic critical pressure for the fluid in question. The reduced temperature T_r is defined similarly. That is:

$$P_r = \frac{P_1}{P_c} \tag{13}$$

$$T_r = \frac{T_1}{T_c} \tag{14}$$

NOTE See Annex D for values of P_c and T_c.

### 7.6 Non-turbulent (laminar and transitional) flow

The flow model embodied in Equations (5) through (7) is for fully developed, turbulent flow only. Non-turbulent conditions may be encountered, especially when flow rates are quite low or fluid viscosity is appreciable. To affirm the applicability of the flow model, the value of the valve Reynolds Number (see Equation (23)) should be computed. The flow model is applicable if Re_V ≥ 10,000.

---

## 8 Correction factors common to both incompressible and compressible flow

### 8.1 Piping geometry correction factors

The various piping geometry factors (F_P, F_LP, x_TP) are necessary to account for fittings attached upstream and/or downstream to a control valve body. The F_P factor is the ratio of the flow rate through a control valve installed with attached fittings to the flow rate that would result if the control valve was installed without attached fittings and tested under identical conditions which will not produce choked flow in either installation (see Figure 1).

To meet the stated flow accuracy of ±5%, all piping geometry factors shall be determined by test in accordance with IEC 60534-2-3.

When estimated values of the piping geometry factors are permissible, the following equations should be used for concentric reducers and expanders directly coupled to the control valve. These equations derive from an analytical accounting of the additional resistance and interchange between the static and dynamic head introduced by the fittings.

The validity of this method is a function of the degree to which the control valve and attached fittings remain hydraulically or aerodynamically independent of each other such that the cumulative effects remain additive. This condition is likely to be satisfied for the majority of practical applications. However, in certain styles of control valves, such as butterfly valves and ball valves, pressure recovery is likely to occur principally in the downstream pipe rather than within the valve body. Replacement of the downstream pipe section with an arbitrary pipe fitting may alter the recovery zone in some cases. Under this condition, it is doubtful that the simple flow resistance method of correction will adequately account for these effects.

### 8.2 Estimated piping geometry factor, F_P

The F_P factor is the ratio of the flow rate through a control valve installed with attached fittings to the flow rate that would result if the control valve was installed without attached fittings and tested under identical conditions which will not produce choked flow in either installation (see Figure 1). When estimated values are permissible, the following equation shall be used:

$$F_P = \frac{1}{\sqrt{1 + \frac{\Sigma\zeta}{N_2} \left(\frac{C}{d^2}\right)^2}} \tag{15}$$

In this equation, the factor Σζ is the algebraic sum of all of the effective velocity head loss coefficients of all fittings attached to the control valve. The velocity head loss coefficient of the control valve itself is not included.

$$\Sigma\zeta = \zeta_1 + \zeta_2 + \zeta_{B1} - \zeta_{B2} \tag{16}$$

In cases where the piping diameters approaching and leaving the control valve are different, the ζ_B coefficients are calculated as follows:

$$\zeta_B = 1 - \left(\frac{d}{D}\right)^4 \tag{17}$$

If the inlet and outlet fittings are short-length, commercially available, concentric reducers, the ζ₁ and ζ₂ coefficients may be approximated as follows:

Inlet reducer:

$$\zeta_1 = 0.5 \left[1 - \left(\frac{d}{D_1}\right)^2\right]^2 \tag{18}$$

Outlet reducer (expander):

$$\zeta_2 = 1.0 \left[1 - \left(\frac{d}{D_2}\right)^2\right]^2 \tag{19}$$

Inlet and outlet reducers of equal size:

$$\zeta_1 + \zeta_2 = 1.5 \left[1 - \left(\frac{d}{D}\right)^2\right]^2 \tag{20}$$

The F_P values calculated with the above ζ factors generally lead to the selection of valve capacities slightly larger than required. See Annex C for methods of solution.

For graphical approximations of F_P, refer to Figures D.2a) and D.2b) in Annex D.

### 8.3 Estimated combined liquid pressure recovery factor and piping geometry factor with attached fittings, F_LP

F_L is the liquid pressure recovery factor of the valve without attached fittings. This factor accounts for the influence of the valve internal geometry on the valve capacity at choked flow. It is defined as the ratio of the actual maximum flow rate under choked flow conditions to a theoretical, non-choked flow rate which would be calculated if the pressure differential used was the difference between the valve inlet pressure and the apparent *vena contracta* pressure at choked flow conditions. The factor F_L may be determined from tests in accordance with IEC 60534-2-3. Typical values of F_L versus percent of rated flow coefficient are shown in Figure D.3.

F_LP is the combined liquid pressure recovery factor and piping geometry factor for a control valve with attached fittings. It is obtained in the same manner as F_L.

To meet a deviation of ±5% for F_LP, F_LP shall be determined by testing. When estimated values are permissible, Equation (21) shall be used:

$$F_{LP} = \frac{F_L}{\sqrt{1 + \frac{F_L^2}{N_2} (\Sigma\zeta_1) \left(\frac{C}{d^2}\right)^2}} \tag{21}$$

Here Σζ₁ is the velocity head loss coefficient, ζ₁ + ζ_B1, of the fitting attached upstream of the valve as measured between the upstream pressure tap and the control valve body inlet.

### 8.4 Estimated pressure differential ratio factor with attached fittings, x_TP

x_T is the pressure differential ratio factor of a control valve installed without reducers or other fittings. If the inlet pressure P₁ is held constant and the outlet pressure P₂ is progressively lowered, the mass flow rate through a valve will increase to a maximum limit, a condition referred to as choked flow. Further reductions in P₂ will produce no further increase in flow rate.

This limit is reached when the pressure differential x reaches a value of F_γ x_T. The limiting value of x is defined as the critical differential pressure ratio. The value of x used in any of the sizing equations and in the relationship for Y (Equation (12)) shall be held to this limit even though the actual pressure differential ratio is greater. Thus, the numerical value of Y may range from 0.667, when x = F_γ x_T, to 1.0 for very low differential pressures.

The values of x_T may be established by air test. The test procedure for this determination is covered in IEC 60534-2-3.

NOTE 1 Representative values of x_T for several types of control valves with full size trim and at full rated openings are given in Table D.1. Caution should be exercised in the use of this information. When precise values are required, they should be obtained by test.

If a control valve is installed with attached fittings, the value of x_T will be affected.

x_TP is the pressure differential ratio factor of a control valve with attached fittings at choked flow. To meet a deviation of ±5% for x_TP, the valve and attached fittings shall be tested as a unit. When estimated values are permissible, Equation (22) shall be used:

$$x_{TP} = \frac{\dfrac{x_T}{F_P^2}}{1 + \dfrac{x_T \, \Sigma\zeta_i}{N_5} \left(\dfrac{C}{d^2}\right)^2} \tag{22}$$

NOTE 2 Values for N₅ are given in Table 1 below.

In the above relationship, x_T is the pressure differential ratio factor for a control valve installed without reducers or other fittings. Σζ_i is the sum of the inlet velocity head loss coefficients (ζ₁ + ζ_B1) of the reducer or other fitting attached to the inlet face of the valve.

If the inlet fitting is a short-length, commercially available reducer, the value of ζ₁ may be estimated using Equation (18).

---

## 9 Reynolds Number, Re_V

The incompressible and compressible flow models presented in the preceding clauses are for fully developed turbulent flow. When non-turbulent flow conditions are established through a control valve because of a low pressure differential, a high viscosity, a very small flow coefficient, or a combination thereof, a different flow model is required.

The valve Reynolds Number, Re_V, is employed to determine whether the flow is fully turbulent. Tests show that flow is fully turbulent when the valve Re_V ≥ 10,000. The valve Reynolds Number is given by Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left(\frac{F_L^2 C^2}{N_2 d^4} + 1\right)^{1/4} \tag{23}$$

NOTE 1 The flow rate in Equation (23) is in actual volumetric flow rate units for both incompressible and compressible flows.

NOTE 2 The kinematic viscosity, ν, should be evaluated at flow conditions.

When Re_v < 10,000, the equations presented in Annex A should be used.

The valve Reynolds Number is a function of the flow rate and the valve flow coefficient. Therefore, when solving the flow equations for either of these two variables it is necessary to employ a solution technique that ensures that all instances of each variable are accounted for.

NOTE 3 The dependency of the Reynolds Number on the flow rate and valve flow coefficient necessitates an iterative solution.

The valve style modifier F_d converts the geometry of the orifice(s) to an equivalent circular single flow passage. See Table D.2 for typical values and Annex A for details. To meet a deviation of ±5% for F_d, the F_d factor shall be determined by test in accordance with IEC 60534-2-3.

NOTE 4 Equations involving F_P are not applicable.

---

### Table 1 — Numerical constants N

| Constant | $K_v$ | $C_v$ | $W$ | $Q$ | $P$, $ΔP$ | $ρ$ | $T$ | $d$, $D$ | $ν$ |
|----------|-----|-----|---|---|-------|---|---|------|---|
| $N_1$ | 1 × 10⁻¹ | 8.65 × 10⁻² | – | m³/h | kPa | kg/m³ | – | – | – |
| | 1 | 8.65 × 10⁻¹ | – | m³/h | bar | kg/m³ | – | – | – |
| | | 1 | – | gpm | psia | lbm/ft³ | – | – | – |
| $N_2$ | 1.60 × 10⁻³ | 2.14 × 10⁻³ | – | – | – | – | – | mm | – |
| | | 8.9 × 10² | | | | | | in | |
| $N_4$ | 7.07 × 10⁻² | 7.60 × 10⁻² | – | m³/h | – | – | – | – | m²/s |
| | | 1.73 × 10⁴ | | gpm | | | | | cS |
| $N_5$ | 1.80 × 10⁻³ | 2.41 × 10⁻³ | – | – | – | – | – | mm | – |
| | | 1.00 × 10³ | | | | | | in | |
| $N_6$ | 3.16 | 2.73 | kg/h | – | kPa | kg/m³ | – | – | – |
| | 3.16 × 10¹ | 2.73 × 10¹ | kg/h | – | bar | kg/m³ | – | – | – |
| | | 6.33 × 10¹ | lbm/h | – | psia | lbm/ft³ | – | – | – |
| $N_8$ | 1.10 | 9.48 × 10⁻¹ | kg/h | – | kPa | – | K | – | – |
| | 1.10 × 10² | 9.48 × 10¹ | kg/h | – | bar | – | K | – | – |
| | | 1.93 × 10¹ | lbm/h | – | psia | – | °R | – | – |
| $N_9$ (t_s = 0 °C) | 2.46 × 10¹ | 2.12 × 10¹ | – | m³/h | kPa | – | K | – | – |
| | 2.46 × 10³ | 2.12 × 10³ | – | m³/h | bar | – | K | – | – |
| | | 6.94 × 10³ | – | scfh | psia | – | °R | – | – |
| $N_9$ (t_s = 15 °C) | 2.60 × 10¹ | 2.25 × 10¹ | – | m³/h | kPa | – | K | – | – |
| | 2.60 × 10³ | 2.25 × 10³ | – | m³/h | bar | – | K | – | – |
| | | 7.32 × 10³ | – | scfh | psia | – | °R | – | – |
| $N_{18}$ | 8.65 × 10⁻¹ | 1.00 | – | – | – | – | – | mm | – |
| | | 6.45 × 10² | | | | | | in | |
| $N_{19}$ | 2.5 | 2.3 | – | – | – | – | – | mm | – |
| | | 9.06 × 10⁻² | | | | | | in | |
| $N_{22}$ (t_s = 0 °C) | 1.73 × 10¹ | 1.50 × 10¹ | – | m³/h | kPa | – | K | – | – |
| | 1.73 × 10³ | 1.50 × 10³ | – | m³/h | bar | – | K | – | – |
| | | 4.92 × 10³ | – | scfh | psia | – | °R | – | – |
| $N_{22}$ (t_s = 15 °C) | 1.84 × 10¹ | 1.59 × 10¹ | – | m³/h | kPa | – | K | – | – |
| | 1.84 × 10³ | 1.59 × 10³ | – | m³/h | bar | – | K | – | – |
| | | 5.2 × 10³ | – | scfh | psia | – | °R | – | – |
| $N_{27}$ | 7.75 × 10⁻¹ | 6.70 × 10⁻¹ | kg/h | – | kPa | – | K | – | – |
| | 7.75 × 10¹ | 6.70 × 10¹ | kg/h | – | bar | – | K | – | – |
| | | 1.37 × 10¹ | lbm/h | – | psia | – | °R | – | – |
| $N_{32}$ | 1.40 × 10² | 1.27 × 10² | – | – | – | – | – | mm | – |
| | | 1.70 × 10¹ | | | | | | in | |

NOTE Use of the numerical constants provided in this table together with the practical metric units specified in the table will yield flow coefficients in the units in which they are defined.

---

## Annex A (normative) — Sizing equations for non-turbulent flow

### A.1 General

This annex presents the sizing equations as currently understood for control valves flowing incompressible and compressible fluids under non-turbulent conditions. Whereas this technology is, in general, less understood than fully developed turbulent flow, and further is strongly dependent on valve geometry, this technology may be augmented by individual valve manufacturers with technology specific to individual valve designs.

### A.2 Symbols

The following variables are unique to this annex. All others have been defined in the main body of this standard.

| Symbol | Description | Unit |
|--------|-------------|------|
| C_rated | Flow coefficient at rated travel | various |
| F_R | Reynolds number factor | Dimensionless |
| n | Intermediate variable | Dimensionless |

### A.3 Discerning a non-turbulent flow condition

As stated in Clause 9 of the main body of this standard, the valve Reynolds Number, Re_v, is employed to determine whether fully developed turbulent flow exists. The valve Reynolds Number is given by Equation (23) and repeated here for convenience:

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left(\frac{F_L^2 C^2}{N_2 d^4} + 1\right)^{1/4} \tag{A.1}$$

NOTE 1 The flow rate in Equation (A.1) is in actual volumetric flow rate units for both incompressible and compressible flows.

NOTE 2 The kinematic viscosity, ν, should be evaluated at (P₁ + P₂)/2 for compressible flows.

NOTE 3 The dependency of the Reynolds Number on the flow rate and valve flow coefficient necessitates an iterative solution.

Flow is considered fully turbulent when Re_v ≥ 10,000. When Re_v < 10,000, the equations presented in this annex should be used.

### A.4 Technology scope

The sizing equations for non-turbulent flow are subject to the following restrictions:

1. The methods given herein are exclusively for a Newtonian rheology. Non-Newtonian fluids can exhibit significant change in viscosity as a function of shear rate, which is proportional to flow rate.

2. The methods given herein are for non-vaporizing fluids.

3. C / (N₁₈ d²) ≤ 0.047

Further, the effect of close-coupled reducers or other flow-disturbing fittings on non-turbulent flow is unknown. While there is no information on the laminar or transitional flow behaviour of control valves installed between pipe reducers, the user of such valves is advised to utilize the appropriate equations for line-sized valves in the calculation of the F_R factor. This should result in conservative flow coefficients, since additional turbulence created by reducers and expanders will further delay the onset of laminar flow. Therefore, it will tend to increase the respective F_R factor for a given valve Reynolds number.

### A.5 Sizing equations for incompressible fluids

The fundamental flow model for incompressible fluids in the non-turbulent flow regime is given as:

$$Q = C N_1 F_R \sqrt{\frac{\Delta P_{actual}}{\rho_1 / \rho_o}} \tag{A.2}$$

This model establishes the relationship between flow rate, flow coefficient, fluid properties, and pertinent service conditions for control valves handling incompressible fluids. Equation (A.2) may be used to compute the required flow coefficient, the flow rate or applied pressure differential given any two of the three quantities.

### A.6 Sizing equations for compressible fluids

The fundamental flow model for compressible fluids in the non-turbulent flow regime is given as:

$$W = C N_{27} F_R Y \sqrt{\frac{\Delta P (P_1 + P_2) M}{T_1}} \tag{A.3}$$

This model establishes the relationship between flow rates, flow coefficients, fluid properties and pertinent service conditions for control valves handling compressible fluids.

An alternate form of Equation (A.3) is presented to accommodate conventional available data formats:

$$Q_s = C N_{22} F_R Y \sqrt{\frac{\Delta P (P_1 + P_2)}{M T_1}} \tag{A.4}$$

NOTE See Annex D for values of M.

where

$$Y = \begin{cases} \dfrac{Re_v - 1{,}000}{9{,}000} \left(1 - \dfrac{x_{sizing}}{3 \cdot x_{choked}} - \sqrt{1 - \dfrac{x}{2}}\right) + \sqrt{1 - \dfrac{x}{2}} & \text{if } 10{,}000 > Re_v \geq 1{,}000 \\[10pt] \sqrt{1 - \dfrac{x}{2}} & \text{if } Re_v < 1{,}000 \end{cases} \tag{A.5}$$

Equation (A.4) expresses the flow rate in standard volumetric units. Equations (A.3) or (A.4) may be used to compute the required flow coefficient, the flow rate or applied pressure differential given any two of the three quantities.

### A.7 Equations for Reynolds Number factor, F_R

The Reynolds Number factor, F_R, is evaluated from the following equations:

If flow is laminar (Re_v < 10),

$$F_R = \operatorname{Min} \begin{bmatrix} \dfrac{0.026}{F_L} \sqrt{n \, Re_v} \\[6pt] 1.00 \end{bmatrix} \tag{A.6}$$

NOTE The 'Min' function returns the smallest value of the expressions contained in the argument.

If flow is transitional (Re_v ≥ 10),

$$F_R = \operatorname{Min} \begin{bmatrix} 1 + \left(\dfrac{0.33 F_L^{1/2}}{n^{1/4}}\right) \log_{10}\left(\dfrac{Re_v}{10{,}000}\right) \\[6pt] \dfrac{0.026}{F_L} \sqrt{n \cdot Re_v} \\[6pt] 1.00 \end{bmatrix} \tag{A.7}$$

The value of the constant, n, is determined on the basis of trim style.

For "full size" trim (C_rated / (d² N₁₈) ≥ 0.016),

$$n = \frac{N_2}{\left(C / d^2\right)^2} \tag{A.8a}$$

For "reduced trim" (C_rated / (d² N₁₈) < 0.016),

$$n = 1 + N_{32} \left(\frac{C}{d^2}\right)^{2/3} \tag{A.8b}$$

---

## Annex B (informative) — Sizing equations for compressible fluid flow through multistage control valves

### B.1 General

This annex presents alternative equations for predicting the flow of a compressible fluid through multistage control valves. The basic flow equations are identical to the equations presented in the main body of this document with the exception of the following differences:

- a) the equation for the calculation of expansion factor Y (Equation B.3);
- b) the inclusion of stage interaction factor k and reheat factor r;
- c) the addition of tables for multistage valves for values of F_L and x_T (Table D.2)

This technology is applicable to designs of multistage multipath control valves, multistage single path control valves and continuous resistance trim control valves. Refer to Clause B.3 for definitions and descriptions of each control valve type.

The test data used to validate the method for multistage single and multipath with one to five stages were obtained from sizing tests carried out in accordance with IEC 60534-2-3 using air as the test medium at pressures varying from 5 × 10⁵ Pa to 13.5 × 10⁵ Pa and at temperatures of approximately 300 K. Some data were obtained under plant conditions using steam at pressures varying from 12 × 10⁵ Pa to 110 × 10⁵ Pa and temperatures from 460 K to 750 K. The method is applicable to any number of stages but has only been validated up to five stages.

The test data used to validate the method for continuous resistance trim with 4 to 30 turns was obtained from sizing tests carried out in accordance with IEC 60534-2-3 using air as the test medium at pressures varying from 5 × 10⁵ Pa and temperatures of approximately 300 K. Some data was obtained under plant conditions using steam at pressures varying from 24 × 10⁵ Pa and temperatures from 500 K to 720 K. This method may be used for any number of turns, but has only been validated up to 30.

If valve specific coefficients (such as K_v or C_v, F_L, and x_T) cannot be determined by appropriate test procedures in IEC 60534-2-3, values supplied by the manufacturer should then be used.

### B.2 Symbols

The following variables are unique to this annex. All others have been defined in the main body of this standard.

| Symbol | Description | Unit |
|--------|-------------|------|
| A_HT | The total hole area of adjacent upstream stage at rated travel | mm² |
| A₀ | The area of the outlet of a single flow path including the total area of related multiple paths | mm² |
| A₁ | The area of the inlet of a single flow path | mm² |
| D_s | The outside diameter of adjacent upstream stage | mm |
| k | Stage interaction factor | Dimensionless |
| l | Travel | mm |
| n | The number of turns (or stages) in a single flow path. In cases of a flow path dividing into multiple paths only one of the paths is included | Dimensionless |
| r | Reheat factor | Dimensionless |

### B.3 Terms and definitions

For the purposes of this annex, the terms and definitions given in IEC 60534-1, those given in this standard as well as the following, apply.

#### B.3.1 Multistage control valves

Globe control valve where the trim has several stages which are separated by a gap (see Figures B.1 and B.2). The geometrical contour of the apertures in all stages should be similar. The ratio of the second stage flow coefficient C to the first stage flow coefficient C should not exceed 1.80. The ratio of the flow coefficient C of the other stages to their previous stage should not exceed 1.55 and should be uniform within a tolerance of ±9%. Normally, for incompressible fluids the flow coefficients of the stages are approximately equal, a slightly smaller flow coefficient C being allocated to a particular stage only if it is required to take a higher pressure drop.

#### B.3.2 Gap

Distance between adjacent stages

#### B.3.3 Multistage multipath control valves

Globe control valve where the trim has multiple flow passages having several stages which are separated by a gap (see Figure B.1). To ensure the validity of the prediction equations of this annex, the gap should conform to the values calculated from the following equation with a tolerance of +15% and −10% (see Figures B.1 and B.2).

$$gap = A_{HT} \left(\frac{1}{l}\right) \left(\frac{1.6}{\sqrt{D_s}}\right) \tag{B.1}$$

where

minimum gap limit = 4 mm; maximum gap limit = 44 mm.

<!-- image -->

NOTE This is one example of a multistage trim.

**Figure B.1 — Multistage multipath trim**

#### B.3.4 Multistage single path control valves

Globe control valve where the trim has one flow passage having several stages which are separated by a gap (see Figure B.2). The gap should be within the following minimum and maximum limits:

minimum gap = 0.60 times the seat diameter of the previous stage;

maximum gap = 1.10 times the seat diameter of the previous stage.

<!-- image -->

*IEC 511/11*

NOTE This is one example of a multistage trim.

**Figure B.2 — Multistage single path trim**

#### B.3.5 Continuous resistance trim control valves

Globe valve where the trim consists of a multistage non-interconnecting multipath throttling restriction of the continuous resistance type, generally referred to as labyrinth valves (see Figures B.3 and B.4). The flow paths should be geometrically similar and should not interconnect but may at some point divide into multiple paths. For incompressible fluids, the cross sectional area of each flow path may be constant but in the case of very high pressure reduction, the area of each flow path may increase to ensure a low exit velocity. For compressible fluids, the area should increase in the direction of flow. The increase should be within these limits:

$$A_1 \times (1.12)^n \leq A_0 \leq A_1 \times (1.23)^n \tag{B.2}$$

The relationship of the number of turns in each flow path to the length of each flow path should be within the maximum and minimum limits calculated from the following equations:

l_max = n × 10.50

l_min = n × 7.00 (minimum flow path can not be less than 25 mm)

where

- l is the length of each flow path — in cases of divided multiple paths, only one is included in l, (units mm).

<!-- image -->

*IEC 512/11*

**Figure B.3 — Disk from a continuous resistance trim. The complete trim consists of a number of these disks stacked together.**

<!-- image -->

*IEC 513/11*

**Figure B.4 — Sectional view of continuous resistance trim with multiple flow passages having vertical undulations**

### B.4 Expansion factor, Y

The expansion factor term and function is described in 7.4. For multistage valves, the following expression should be used to evaluate the expansion factor to account for the effects of reheat between stages.

$$Y = \left[1 - \frac{1 - \left(1 - k \dfrac{x}{x_T}\right)^{\beta_1}}{1.212 \, F_\gamma^{\beta_2}}\right] \left(1 + r \, \frac{x^{\beta_3}}{F_\gamma}\right) \tag{B.3}$$

Where, exponents are defined as follows:

| | Recovered Stage (Multistage) | Continuous Resistance |
|---|---|---|
| β₁ = | 0.5 | (2/n)^0.333 |
| β₂ = | 1.0 | 1.0 if 2 ≤ n ≤ 7; 0.5 if 8 ≤ n |
| β₃ = | √(n−1) | (1/2)√(n/2) − 1 |

The value of x in Equation (B.3) should not exceed F_γ x_T and the maximum value of this term in this Equation (B.3) is 0.963. Further, the value of x_T in Equation (B.3) is not modified by F_γ.

### B.5 Stage interaction factor, k

This factor which is included in the equation for Y, Equation (B.3) introduces the coefficient required to convert the valve pressure drop ratio x into the *vena contracta* pressure drop ratio and it also includes a correction factor for the difference between the pressure recovery between stages and at the exit of the final stage. There is a specific value of k for different numbers of stages. The values are listed in Tables B.1 and B.2.

### B.6 Reheat factor, r

The first part of the equation for Y, Equation (B.3) is based on complete reheat of the fluid between each stage. (Complete restoration of enthalpy following the heat drop during the expansion). This in practice does not happen. There is only partial reheat between stages so the fluid does not expand to the theoretical specific volume. As the number of stages increases above 4 this partial reheat effect is gradually reversed due to increased friction reheat generated by the increased number of stages. The second part of the equation for Y, Equation (B.3) recognizes these effects and changes the theoretical Y calculation by an appropriate amount.

The factor r enables this correction to be calculated from the valve pressure drop ratio. There is a specific value of r for different numbers of stages. The values are listed in Tables B.1 and B.2.

### Table B.1 — Values of the stage interaction factors, k, and the reheat factors, r for multistage single and multipath control valve trim

| Number of stages | k | r |
|-----------------|-------|-------|
| 1 | 0.404 | 0 |
| 2 | 0.673 | 0.215 |
| 3 | 0.825 | 0.316 |
| 4 | 0.885 | 0.335 |
| 5 | 0.915 | 0.310 |

### Table B.2 — Values of the stage interaction factors, k, and the reheat factors, r for continuous resistance control valve trim

| Number of turns | k | r |
|----------------|-------|-------|
| 2 | 0.420 See Note | 0.066 |
| 4 | 0.510 See Note | 0.130 |
| 6 | 0.600 | 0.153 |
| 7 | 0.624 | 0.156 |
| 8 | 0.652 | 0.152 |
| 10 | 0.700 | 0.147 |
| 12 | 0.722 | 0.122 |
| 14 | 0.740 | 0.106 |
| 16 | 0.752 | 0.095 |
| 18 | 0.769 | 0.091 |
| 20 | 0.780 | 0.087 |
| 22 | 0.795 | 0.083 |
| 24 | 0.800 | 0.078 |
| 26 | 0.812 | 0.073 |
| 28 | 0.820 | 0.067 |
| 30 | 0.830 | 0.062 |
| 34 | 0.852 | 0.049 |
| 38 | 0.880 | 0.040 |
| 42 | 0.905 | 0.032 |
| 46 | 0.927 | 0.024 |
| 50 | 0.950 | 0.019 |

NOTE For turns from 2 to 4, if x is equal to or less than 0.35, the tabulated values for k should be multiplied by 1.30.

---

## Annex C (informative) — Piping factor computational considerations

### C.1 Solution

The equations for estimating the piping geometry factors are a function of the flow coefficient, C. The most accurate estimate of the factors will be obtained when the throttling flow coefficient is used in these equations. However, this leads to a system of equations that are difficult or impossible to solve algebraically and an iterative method of solution is preferred. Algebraic solutions can be obtained if the rated flow coefficient (see IEC 60534-1:2005) is used in the equations, however, this will yield an over-estimation of the degree of correction.

Conditions may be encountered that lead to mathematical singularities or failure to converge to a solution. This situation usually indicates that the combined resistance of the control valve and attached fittings is too great to pass the required flow rate. A larger valve diameter should be selected in such circumstances.

A candidate solution schema is presented in the following clauses that may be adapted to each of the flow equations previously presented.

### C.2 Iterative solution schema

#### C.2.1 General

The following numerical solution is based on the notion of finding the root of a function utilizing a simple iterative bisection method. This method has the advantage of being straight forward, robust and providing a predictable degree of accuracy. Other techniques are viable, but provisions should be implemented to ensure real solution, etc.

The bisection concept centers on establishing an initial interval that contains the root to the function. This interval is repetitively bisected until the interval containing the root is sufficiently small to effectively evaluate the root. The overarching logic associated with this schema is shown in Figures C.1 through C.2 and described in the following subclauses.

#### C.2.2 Step 1 — Define flow function

All of the flow equations presented in the main body of this document can be rewritten in the following functional form with the flow coefficient, C, as the independent variable:

$$F(C) = [\text{flow rate}] - [\text{defining flow equation}] \tag{C.1}$$

For example, Equation (1), the incompressible flow equation, may be rewritten in the following functional form:

$$F(C) = Q - C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}} \tag{C.2}$$

It should be noted that certain terms in the functional expression are dependent on the flow coefficient, C. For the example shown, these terms include the piping correction term, F_P, and the sizing pressure differential, ΔP_sizing.

The flow coefficient associated with a given set of service conditions is determined by finding the root of the function, i.e., the value of C such that

$$F(C) = 0 \tag{C.3}$$

#### C.2.3 Step 2 — Set lower flow interval limit

The initial lower limit of the solution interval is set to zero. Appropriate associated values of the subordinate coefficients, F_L and x_T, should be determined for the control valve under consideration (e.g., values associated with low travels). The respective piping correction factor terms, F_P, F_LP, and x_TP, should be evaluated using the values of C, F_L, and x_T. The flow function should be evaluated on the basis of current values of independent variables.

#### C.2.4 Step 3 — Set upper interval limit

Setting the initial upper limit of the solution interval must take certain matters into consideration. First, the upper limit should be set to a sufficiently large value to ensure that the interval contains a root. An arbitrarily large value of

$$C_{Upper} = 0.075 \, d^2 \, N_{18} \tag{C.4}$$

is suggested. This actually corresponds to a value outside the scope of the standard, but should be sufficiently large to capture meaningful real roots.

The second issue concerns large values of the flow coefficient, C. Very large values of the flow coefficient in combination with large downstream expansions can potentially result in mathematical singularities associated with Equation (15). To prevent this from occurring, the expression under the radical in Equation (15) can be used to set an upper bound:

$$C_{Upper} = 0.99 \, d^2 \sqrt{-\frac{N_2}{\Sigma\zeta}} \tag{C.5}$$

The upper limit should be set to the smaller of these two values.

Again, F_L and x_T values associated with C_Upper should be determined and the values of F_P, F_LP, x_TP computed. The flow function is then evaluated using the current values of the independent variables.

#### C.2.5 Step 4 — Check that interval bounds a solution

The solution function, F(C), is monotonic over the defined interval. Therefore, the function value at the interval boundaries will be of opposite sign if a root exists within the interval. If the function is of same sign, then the interval does not contain a real solution. This indicates that the selected flow coefficient range does not have sufficient capacity to pass the flow. A larger valve size should be selected and the process repeated.

If the function is of opposite sign, a solution exists within the interval. Proceed to the next step to progress the convergence of the interval to the solution.

#### C.2.6 Step 5 — Revise interval

The mid-point of the interval should be computed and all parameters that are dependent on the flow coefficient (F_L, x_T, F_P, x_TP, F_LP) evaluated. This divides the initial interval into two sub-intervals, one of which contains the root of the function. To determine which interval contains the root, compare the sign of the flow function at the mid-point to the upper limit. If they are of the same sign, the lower sub-interval contains the root. The upper limit should be redefined to the current mid point. If the functional values are of opposite sign, the upper interval contains the root. The lower limit should be redefined to the current mid-point.

#### C.2.7 Step 6 — Check for convergence

The root is evaluated and iteration may be discontinued when the upper and lower limits of the interval containing the root are suitably close to each other, i.e., when

$$\left| C_{Upper} - C_{Lower} \right| \leq \varepsilon \tag{C.6}$$

A suggested value for the convergence tolerance, ε, is 0.00001.

When the process has suitably converged, the final value should be set to the mid-point of the interval:

$$C = \frac{C_{Upper} + C_{Lower}}{2} \tag{C.7}$$

### C.3 Non-iterative solution schema

If the value C is known and the flow rate W or Q has to be calculated, Equation (15) can be used directly.

If the value C has to be calculated from W or Q, Equation (15) cannot be used directly. To avoid iteration, the following calculation procedure is necessary.

For incompressible flow (see Clause 6) or compressible flow (see Clause 7), the following equations from Table C.1 and C.2 are to be used with C calculated from Equation (1) (incompressible non-choked flow under turbulent conditions without attached fittings) or Equations (6), (7) or (8) (compressible non-choked flow under turbulent conditions without attached fittings). The piping geometry factor F_P and the Reynolds number factor F_R have the value 1. Also the actual pressure drop ratio x and the actual differential pressure ΔP_actual should be used in this case. For compressible flow the expansion factor, Y, has the minimum value of 2/3.

### Table C.1 — Incompressible flow

**Non-choked flow** (x_F,actual < x_F,choked):

x_F,choked is to be calculated from Equation (4) with F_P and F_LP under non-choked flow conditions (see this table)

$$F_P = \sqrt{1 - \frac{\Sigma\zeta}{N_2} \left(\frac{C}{d^2}\right)^2}$$

$$F_{LP} = \frac{F_L}{\sqrt{1 + \frac{\zeta_1 + \zeta_{B1}}{N_2} \left(\frac{C}{d^2}\right)^2 \frac{F_L^2}{F_P^2}}}$$

**Choked flow** (x_F,actual ≥ x_F,choked):

$$F_P = \frac{1 - \dfrac{\Delta P}{P_1 - F_F \cdot P_v} \cdot \dfrac{\zeta_1 + \zeta_{B1}}{N_2} \left(\dfrac{C}{d^2}\right)^2}{\sqrt{1 + \dfrac{\Delta P}{P_1 - F_F \cdot P_v} \cdot \dfrac{1}{N_2} \left(\dfrac{\Sigma\zeta}{F_L^2} - (\zeta_1 + \zeta_{B1})\right) \left(\dfrac{C}{d^2}\right)^2}}$$

$$F_{LP} = F_L \cdot \sqrt{1 - \frac{\Delta P}{P_1 - F_F \cdot P_v} \cdot \frac{\zeta_1 + \zeta_{B1}}{N_2} \left(\frac{C}{d^2}\right)^2}$$

### Table C.2 — Compressible flow

**Non-choked flow** (x_actual < x_choked):

x_choked is to be calculated from Equation (11) with F_P and x_TP under non-choked flow conditions (see this table)

$$F_P = \sqrt{1 - \frac{\Sigma\zeta}{N_2} \left(\frac{C}{d^2}\right)^2}$$

$$x_{TP} = \frac{x_T}{F_P^2 + x_T \cdot \dfrac{\zeta_1 + \zeta_{B1}}{N_5} \left(\dfrac{C}{d^2}\right)^2}$$

**Choked flow** (x_actual ≥ x_choked):

$$F_P = \sqrt{\frac{1 - \dfrac{9}{4} \cdot \dfrac{\Delta P}{F_\gamma \cdot P_1} \cdot Y^2 \cdot \dfrac{\zeta_1 + \zeta_{B1}}{N_5} \left(\dfrac{C}{d^2}\right)^2}{1 + \dfrac{9}{4} \cdot \dfrac{\Delta P}{F_\gamma \cdot P_1} \cdot Y^2 \cdot \dfrac{1}{N_5} \left(\dfrac{\Sigma\zeta}{x_T} - (\zeta_1 + \zeta_{B1})\right) \left(\dfrac{C}{d^2}\right)^2}}$$

$$x_{TP} = x_T \cdot \left(1 + \frac{\Delta P}{F_\gamma \cdot P_1} \cdot Y^2 \cdot \frac{\zeta_1 + \zeta_{B1}}{N_5} \left(\frac{C}{d^2}\right)^2\right)$$

<!-- image -->

*IEC 514/11*

**Figure C.1 — Determination of the upper limit of the flow coefficient by the iterative method**

<!-- image -->

*IEC 515/11*

**Figure C.2 — Determination of the final flow coefficient by the iterative method**

---

## Annex D (informative) — Engineering data

### D.1 Physical constants

Physical constants are given in Table D.1.

### Table D.1 — Physical constants of gases and vapor

| Gas or vapor | Symbol | M | γ | F_γ | P_c (kPa) | T_c (K) |
|---|---|---|---|---|---|---|
| Acetylene | C₂H₂ | 26.04 | 1.30 | 0.929 | 6,140 | 309 |
| Air | — | 28.97 | 1.40 | 1.000 | 3,771 | 133 |
| Ammonia | NH₃ | 17.03 | 1.32 | 0.943 | 11,400 | 406 |
| Argon | A | 39.948 | 1.67 | 1.191 | 4,870 | 151 |
| Benzene | C₆H₆ | 78.11 | 1.12 | 0.800 | 4,924 | 562 |
| Isobutane | C₄H₉ | 58.12 | 1.10 | 0.784 | 3,638 | 408 |
| n-Butane | C₄H₁₀ | 58.12 | 1.11 | 0.793 | 3,800 | 425 |
| Isobutylene | C₄H₈ | 56.11 | 1.11 | 0.790 | 4,000 | 418 |
| Carbon dioxide | CO₂ | 44.01 | 1.30 | 0.929 | 7,387 | 304 |
| Carbon monoxide | CO | 28.01 | 1.40 | 1.000 | 3,496 | 133 |
| Chlorine | Cl₂ | 70.906 | 1.31 | 0.934 | 7,980 | 417 |
| Ethane | C₂H₆ | 30.07 | 1.22 | 0.871 | 4,884 | 305 |
| Ethylene | C₂H₄ | 28.05 | 1.22 | 0.871 | 5,040 | 283 |
| Fluorine | F₂ | 18.998 | 1.36 | 0.970 | 5,215 | 144 |
| Freon 11 (trichloromonofluoromethane) | CCl₃F | 137.37 | 1.14 | 0.811 | 4,409 | 471 |
| Freon 12 (dichlorodifluoromethane) | CCl₂F₂ | 120.91 | 1.13 | 0.807 | 4,114 | 385 |
| Freon 13 (chlorotrifluoromethane) | CClF₃ | 104.46 | 1.14 | 0.814 | 3,869 | 302 |
| Freon 22 (chlorodifluoromethane) | CHClF₂ | 80.47 | 1.18 | 0.846 | 4,977 | 369 |
| Helium | He | 4.003 | 1.66 | 1.186 | 229 | 5.25 |
| n-Heptane | C₇H₁₆ | 100.2 | 1.05 | 0.750 | 2,736 | 540 |
| Hydrogen | H₂ | 2.016 | 1.41 | 1.007 | 1,297 | 33.25 |
| Hydrogen chloride | HCl | 36.46 | 1.41 | 1.007 | 8,319 | 325 |
| Hydrogen fluoride | HF | 20.01 | 0.97 | 0.691 | 6,485 | 461 |
| Methane | CH₄ | 16.04 | 1.32 | 0.943 | 4,600 | 191 |
| Methyl chloride | CH₃Cl | 50.49 | 1.24 | 0.889 | 6,677 | 417 |
| Natural gas ⁴⁾ | — | 17.74 | 1.27 | 0.907 | 4,634 | 203 |
| Neon | Ne | 20.179 | 1.64 | 1.171 | 2,726 | 44.45 |
| Nitric oxide | NO | 63.01 | 1.40 | 1.000 | 6,485 | 180 |
| Nitrogen | N₂ | 28.013 | 1.40 | 1.000 | 3,394 | 126 |
| Octane | C₈H₁₈ | 114.23 | 1.66 | 1.186 | 2,513 | 569 |
| Oxygen | O₂ | 32 | 1.40 | 1.000 | 5,040 | 155 |
| Pentane | C₅H₁₂ | 72.15 | 1.06 | 0.757 | 3,374 | 470 |
| Propane | C₃H₈ | 44.10 | 1.15 | 0.821 | 4,256 | 370 |
| Propylene | C₃H₆ | 42.08 | 1.14 | 0.814 | 4,600 | 365 |
| Saturated steam | — | 18.016 | 1.25–1.32 ⁴⁾ | 0.893–0.943 ⁴⁾ | 22,119 | 647 |
| Sulphur dioxide | SO₂ | 64.06 | 1.26 | 0.900 | 7,822 | 430 |
| Superheated steam | — | 18.016 | 1.315 | 0.939 | 22,119 | 647 |

### D.2 Typical control valve coefficients

### Table D.2 — Typical values of valve style modifier F_d, liquid pressure recovery factor F_L and pressure differential ratio factor x_T at full rated travel

| Valve type | Trim type | Flow direction | F_L | x_T | F_d |
|---|---|---|---|---|---|
| Globe, single port | 3 V-port plug | Open or close | 0.90 | 0.70 | 0.48 |
| | 4 V-port plug | Open or close | 0.90 | 0.70 | 0.41 |
| | 6 V-port plug | Open or close | 0.90 | 0.70 | 0.30 |
| | Contoured plug (linear and equal percentage) | Open | 0.90 | 0.72 | 0.46 |
| | | Close | 0.80 | 0.55 | 1.00 |
| | 60 equal diameter hole drilled cage | Outward or inward | 0.90 | 0.68 | 0.13 |
| | 120 equal diameter hole drilled cage | Outward or inward | 0.90 | 0.68 | 0.09 |
| | Characterized cage, 4-port | Outward | 0.90 | 0.75 | 0.41 |
| | | Inward | 0.85 | 0.70 | 0.41 |
| Globe, double port | Ported plug | Inlet between seats | 0.90 | 0.75 | 0.28 |
| | Contoured plug | Either direction | 0.85 | 0.70 | 0.32 |
| Globe, angle | Contoured plug (linear and equal percentage) | Open | 0.90 | 0.72 | 0.46 |
| | | Close | 0.80 | 0.65 | 1.00 |
| | Characterized cage, 4-port | Outward | 0.90 | 0.65 | 0.41 |
| | | Inward | 0.85 | 0.60 | 0.41 |
| | Venturi | Close | 0.50 | 0.20 | 1.00 |
| Globe, small flow trim | V-notch | Open | 0.98 | 0.84 | 0.70 |
| | Flat seat (short travel) | Close | 0.85 | 0.70 | 0.30 |
| | Tapered needle | Open | 0.95 | 0.84 | N₁₉ C F_d / (F_L D_o) |
| Rotary | Eccentric spherical plug | Open | 0.85 | 0.60 | 0.42 |
| | | Close | 0.68 | 0.40 | 0.42 |
| | Eccentric conical plug | Open | 0.77 | 0.54 | 0.44 |
| | | Close | 0.79 | 0.55 | 0.44 |
| Butterfly (centered shaft) | Swing-through (70°) | Either | 0.62 | 0.35 | 0.57 |
| | Swing-through (60°) | Either | 0.70 | 0.42 | 0.50 |
| | Fluted vane (70°) | Either | 0.67 | 0.38 | 0.30 |
| Butterfly (eccentric shaft) | Offset seat (70°) | Either | 0.67 | 0.35 | 0.57 |
| Ball | Full bore (70°) | Either | 0.74 | 0.42 | 0.99 |
| | Segmented ball | Either | 0.60 | 0.30 | 0.98 |
| Globe and angle | Multistage Multipath, 2 stages | Either | 0.97 | 0.812 | — |
| | Multistage Multipath, 3 stages | Either | 0.99 | 0.888 | — |
| | Multistage Multipath, 4 stages | Either | 0.99 | 0.925 | — |
| | Multistage Multipath, 5 stages | Either | 0.99 | 0.950 | — |
| | Multistage Single path, 2 stages | Either | 0.97 | 0.896 | — |
| | Multistage Single path, 3 stages | Either | 0.99 | 0.935 | — |
| | Multistage Single path, 4 stages | Either | 0.99 | 0.960 | — |

### D.3 Piping geometry factors

<!-- image -->

NOTE 1 Pipe diameter D is the same size at both ends of the valve (see Equation (20)).

NOTE 2 Refer to Annex E for example of the use of these curves.

**Figure D.1 a) — Piping geometry factor F_P for K_v / d²**

<!-- image -->

NOTE 1 Pipe diameter D is the same size at both ends of the valve (see Equation (20)).

NOTE 2 Refer to Annex E for example of the use of these curves.

**Figure D.1 b) — Piping geometry factor F_P for C_v / d²**

**Figure D.1 — Piping geometry factors**

### D.4 Pressure recovery factors

<!-- image -->

**Figure D.2 a) — Double seated globe valves and cage guided globe valves (see Key)**

<!-- image -->

*IEC 519/11*

**Figure D.2 b) — Butterfly valves and contoured small flow valve (see Key)**

**Figure D.2 c) — Contoured globe valves, eccentric spherical plug valves and segmented ball valve (see Key)**

<!-- image -->

**Figure D.2 d) — Eccentric conical plug valves (see Key)**

#### Key

1. Double seated globe valve, V-port plug
2. Ported cage guided globe valve (flow-to-open and flow-to-close)
3. Double seated globe valve, contoured plug
4. Offset seat butterfly valve
5. Swing-through butterfly valve
6. Contoured small flow valve
7. Single port, equal percentage, contoured globe valve, flow-to-open
8. Single port, equal percentage, contoured globe valve, flow-to-close
9. Eccentric spherical plug valve, flow-to-open
10. Eccentric spherical plug valve, flow-to-close
11. Segmented ball valve
12. Eccentric conical plug valve, flow-to-open
13. Eccentric conical plug valve, flow-to-close

NOTE These values are typical only; actual values should be stated by the manufacturer.

**Figure D.2 — Pressure recovery factors**

### D.5 Liquid critical pressure ratio factor

<!-- image -->

**Figure D.3 — Liquid critical pressure ratio factor F_F**

---

## Annex E (informative) — Reference calculations

### Example 1: Incompressible flow — non-choked turbulent flow without attached fittings, solve for K_v

**Process data:**

| Parameter | Value |
|-----------|-------|
| Fluid | water |
| Inlet temperature | T₁ = 363 K |
| Density | ρ₁ = 965.4 kg/m³ |
| Vapor pressure | P_v = 70.1 kPa |
| Thermodynamic critical pressure | P_c = 22,120 kPa |
| Kinematic viscosity | ν = 3.26 × 10⁻⁷ m²/s |
| Inlet absolute pressure | P₁ = 680 kPa |
| Outlet absolute pressure | P₂ = 220 kPa |
| Flow rate | Q = 360 m³/h |
| Pipe size | D₁ = D₂ = 150 mm |

**Valve data:**

| Parameter | Value |
|-----------|-------|
| Valve style | globe |
| Trim | parabolic plug |
| Flow direction | flow-to-open |
| Valve size | d = 150 mm |
| Liquid pressure recovery factor | F_L = 0.90 (from Table D.2) |
| Valve style modifier | F_d = 0.46 (from Table D.2) |

**Calculations:**

The applicable flow model for incompressible fluids in the turbulent flow regime is given in Equation (1):

$$Q = C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}}$$

From Table 1, the numerical constants to use with the given dataset are:

- N₁ = 1 × 10⁻¹
- N₂ = 1.60 × 10⁻³
- N₄ = 7.07 × 10⁻²
- N₁₈ = 8.65 × 10⁻¹

The liquid critical pressure ratio factor, F_F, should be determined using Equation (4):

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} = 0.944$$

Since the valve is line-sized, F_P = 1 and F_LP = F_L.

The choked pressure differential, ΔP_choked, should be determined using Equation (3):

$$\Delta P_{choked} = \left(\frac{F_{LP}}{F_P}\right)^2 (P_1 - F_F P_v) = 497 \text{ kPa}$$

Next, the sizing pressure differential, ΔP_sizing, should be determined using Equation (2):

$$\Delta P = P_1 - P_2 = 460 \text{ kPa}$$

$$\Delta P_{sizing} = \begin{cases} \Delta P & \text{if } \Delta P < \Delta P_{choked} \\ \Delta P_{choked} & \text{if } \Delta P \geq \Delta P_{choked} \end{cases}$$

$$\Delta P_{sizing} = 460 \text{ kPa}$$

It should be solved for K_v after rearranging Equation (1):

$$C = K_v = \frac{Q}{N_1 F_P} \sqrt{\frac{\rho_1 / \rho_o}{\Delta P_{sizing}}}$$

where ρ_o is the density of water at 15 °C

$$K_v = 165 \text{ m}^3/\text{h}$$

Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 2.97 \times 10^6$$

Since Re_v > 10,000, the flow is turbulent.

It should be verified that the result is within the applicable scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.0085 < 0.047$$

---

### Example 2: Incompressible flow — choked flow without attached fittings, solve for K_v

**Process data:**

| Parameter | Value |
|-----------|-------|
| Fluid | water |
| Inlet temperature | T₁ = 363 K |
| Density | ρ₁ = 965.4 kg/m³ |
| Vapor pressure | P_v = 70.1 kPa |
| Thermodynamic critical pressure | P_c = 22,120 kPa |
| Kinematic viscosity | ν = 3.26 × 10⁻⁷ m²/s |
| Inlet absolute pressure | P₁ = 680 kPa |
| Outlet absolute pressure | P₂ = 220 kPa |
| Flow rate | Q = 360 m³/h |
| Pipe size | D₁ = D₂ = 100 mm |

**Valve data:**

| Parameter | Value |
|-----------|-------|
| Valve style | ball valve |
| Trim | segmented ball |
| Flow direction | flow-to-open |
| Valve size | d = 100 mm |
| Liquid pressure recovery factor | F_L = 0.60 (from Table D.2) |
| Valve style modifier | F_d = 0.98 (from Table D.2) |

**Calculations:**

The applicable flow model for incompressible fluids in the turbulent flow regime is given in Equation (1):

$$Q = C N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}}$$

From Table 1, the numerical constants to use with the given dataset are:

- N₁ = 1 × 10⁻¹
- N₂ = 1.60 × 10⁻³
- N₄ = 7.07 × 10⁻²
- N₁₈ = 8.65 × 10⁻¹

The liquid critical pressure ratio factor, F_F, should be determined using Equation (4):

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} = 0.944$$

Since the valve is line-sized, F_P = 1 and F_LP = F_L.

The choked pressure differential, ΔP_choked, should be determined using Equation (3):

$$\Delta P_{choked} = \left(\frac{F_{LP}}{F_P}\right)^2 (P_1 - F_F P_v) = 221 \text{ kPa}$$

Next, the sizing pressure differential, ΔP_sizing, should be determined using Equation (2):

$$\Delta P = P_1 - P_2 = 460 \text{ kPa}$$

$$\Delta P_{sizing} = \begin{cases} \Delta P & \text{if } \Delta P < \Delta P_{choked} \\ \Delta P_{choked} & \text{if } \Delta P \geq \Delta P_{choked} \end{cases}$$

$$\Delta P_{sizing} = 221 \text{ kPa}$$

It should be solved for K_v after rearranging Equation (1):

$$C = K_v = \frac{Q}{N_1 F_P} \sqrt{\frac{\rho_1 / \rho_o}{\Delta P_{sizing}}}$$

where ρ_o is the density of water at 15 °C

$$K_v = 238 \text{ m}^3/\text{h}$$

Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 6.60 \times 10^6$$

Since Re_v > 10,000, the flow is turbulent.

It should be verified that the result is within the scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.028 < 0.047$$

---

### Example 3: Compressible flow — non-choked flow, solve for K_v

**Process data:**

| Parameter | Value |
|-----------|-------|
| Fluid | carbon dioxide gas |
| Inlet temperature | T₁ = 433 K |
| Inlet absolute pressure | P₁ = 680 kPa |
| Outlet absolute pressure | P₂ = 450 kPa |
| Kinematic viscosity | ν = 2.526 × 10⁻⁶ m²/s at 680 kPa and 433 K |
| Flow rate | Q_s = 3,800 standard m³/h at 101.325 kPa and 273 K |
| Density | ρ₁ = 8.389 kg/m³ at 680 kPa and 433 K |
| Compressibility | Z₁ = 0.991 at 680 kPa and 433 K |
| Standard compressibility | Z_s = 0.994 at 101.325 kPa and 273 K |
| Molecular mass | M = 44.01 |
| Specific heat ratio | γ = 1.30 |
| Pipe size | D₁ = D₂ = 100 mm |

**Valve data:**

| Parameter | Value |
|-----------|-------|
| Valve style | rotary |
| Trim | eccentric spherical plug |
| Flow direction | flow-to-open |
| Valve size | d = 100 mm |
| Pressure differential ratio factor | x_T = 0.60 (from Table D.2) |
| Liquid pressure recovery factor | F_L = 0.85 (from Table D.2) |
| Valve style modifier | F_d = 0.42 (from Table D.2) |

**Calculations:**

The applicable flow model for compressible fluids in the turbulent flow regime with the dataset given is found in Equation (7):

$$Q_s = C N_9 F_P P_1 Y \sqrt{\frac{x_{sizing}}{M T_1 Z_1}}$$

From Table 1, the numerical constants to use with the given dataset are:

- N₂ = 1.60 × 10⁻³
- N₄ = 7.07 × 10⁻²
- N₉ = 2.46 × 10¹
- N₁₈ = 8.65 × 10⁻¹

Since the valve is line-sized, F_P = 1 and x_TP = x_T.

The specific heat ratio factor, F_γ, should be calculated using Equation (11):

$$F_\gamma = \frac{\gamma}{1.40} = 0.929$$

The choked pressure drop ratio, x_choked, should be determined using Equation (10):

$$x_{choked} = F_\gamma x_{TP} = 0.557$$

Next, the sizing pressure drop ratio, x_sizing, should be determined using Equations (8) and (9):

$$x = \frac{P_1 - P_2}{P_1} = 0.338$$

$$x_{sizing} = \begin{cases} x & \text{if } x < x_{choked} \\ x_{choked} & \text{if } x \geq x_{choked} \end{cases}$$

$$x_{sizing} = 0.338$$

The expansion factor, Y, should be calculated using Equation (12):

$$Y = 1 - \frac{x_{sizing}}{3 \, x_{choked}} = 0.798$$

It should be solved for K_v after rearranging Equation (7):

$$C = K_v = \frac{Q_s}{N_9 F_P P_1 Y} \sqrt{\frac{M T_1 Z_1}{x_{sizing}}}$$

$$K_v = 67.2 \text{ m}^3/\text{h}$$

The actual volumetric flow rate should be found:

$$Q = Q_s \frac{P_s T_1 Z_1}{P_1 T_s Z_s} = 895.4 \text{ m}^3/\text{h}$$

Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 1.40 \times 10^6$$

Since Re_v > 10,000, the flow is turbulent.

It should be verified that the result is within the scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.0078 < 0.047$$

---

### Example 4: Compressible flow — choked flow, solve for K_v

**Process data:**

| Parameter | Value |
|-----------|-------|
| Fluid | carbon dioxide gas |
| Inlet temperature | T₁ = 433 K |
| Inlet absolute pressure | P₁ = 680 kPa |
| Outlet absolute pressure | P₂ = 250 kPa |
| Kinematic viscosity | ν = 2.526 × 10⁻⁶ m²/s at 680 kPa and 433 K |
| Flow rate | Q_s = 3,800 standard m³/h at 101.325 kPa and 273 K |
| Density | ρ₁ = 8.389 kg/m³ at 680 kPa and 433 K |
| Density at standard conditions | ρ_s = 1.978 kg/m³ at 101.325 kPa and 273 K |
| Compressibility | Z₁ = 0.991 at 680 kPa and 433 K |
| Standard compressibility | Z_s = 0.994 at 101.325 kPa and 273 K |
| Molecular mass | M = 44.01 |
| Specific heat ratio | γ = 1.30 |
| Pipe size | D₁ = D₂ = 100 mm |

**Valve data:**

| Parameter | Value |
|-----------|-------|
| Valve style | rotary |
| Trim | eccentric spherical plug |
| Flow direction | flow-to-open |
| Valve size | d = 100 mm |
| Pressure differential ratio factor | x_T = 0.60 (from Table D.2) |
| Liquid pressure recovery factor | F_L = 0.85 (from Table D.2) |
| Valve style modifier | F_d = 0.42 (from Table D.2) |

**Calculations:**

The applicable flow model for compressible fluids in the turbulent flow regime with the dataset given is found in Equation (7):

$$Q_s = C N_9 F_P P_1 Y \sqrt{\frac{x_{sizing}}{M T_1 Z_1}}$$

From Table 1, the numerical constants to use with the given dataset are:

- N₂ = 1.60 × 10⁻³
- N₄ = 7.07 × 10⁻²
- N₉ = 2.46 × 10¹
- N₁₈ = 8.65 × 10⁻¹

Since the valve is line-sized, F_P = 1 and x_TP = x_T.

The specific heat ratio factor, F_γ, should be calculated using Equation (11):

$$F_\gamma = \frac{\gamma}{1.40} = 0.929$$

The choked pressure drop ratio, x_choked, should be determined using Equation (10):

$$x_{choked} = F_\gamma x_{TP} = 0.557$$

Next, the sizing pressure drop ratio, x_sizing, should be determined using Equations (8) and (9):

$$x = \frac{P_1 - P_2}{P_1} = 0.632$$

$$x_{sizing} = \begin{cases} x & \text{if } x < x_{choked} \\ x_{choked} & \text{if } x \geq x_{choked} \end{cases}$$

$$x_{sizing} = 0.557$$

The expansion factor, Y, should be calculated using Equation (12):

$$Y = 1 - \frac{x_{sizing}}{3 \, x_{choked}} = 0.667$$

It should be solved for K_v after rearranging Equation (7):

$$C = K_v = \frac{Q_s}{N_9 F_P P_1 Y} \sqrt{\frac{M T_1 Z_1}{x_{sizing}}}$$

$$K_v = 62.6 \text{ m}^3/\text{h}$$

The actual volumetric flow rate should be found:

$$Q = Q_s \frac{P_s T_1 Z_1}{P_1 T_s Z_s} = 895.4 \text{ m}^3/\text{h}$$

Next, it should be verified that the flow is turbulent by calculating the Reynolds number, Re_v, using Equation (23):

$$Re_v = \frac{N_4 F_d Q}{\nu \sqrt{C F_L}} \left[\frac{F_L^2 C^2}{N_2 d^4} + 1\right]^{1/4} = 1.45 \times 10^6$$

Since Re_v > 10,000, the flow is turbulent.

It should be verified that the result is within the scope of the standard:

$$\frac{C}{N_{18} d^2} = 0.0073 < 0.047$$

---

### Example 5: Incompressible fluid — choked flow with attached fittings

**Process data:**

| Parameter | Value |
|-----------|-------|
| Fluid | unspecified |
| Density | ρ₁ = 780 kg/m³ |
| Vapor pressure | P_v = 4 kPa |
| Thermodynamic critical pressure | P_c = 22,120 kPa |
| Inlet absolute pressure | P₁ = 3,550 kPa |
| Outlet absolute pressure | P₂ = 2,240 kPa |
| Flow rate | Q = 150 m³/h |
| Upstream pipe size | D₁ = 154.1 mm |
| Downstream pipe size | D₂ = 202.7 mm |

**Valve data:**

| Parameter | Value |
|-----------|-------|
| Valve style | Butterfly |
| Valve size | d = 101.6 mm |

Flow Coefficient Data:

| Rotation | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |
|----------|---|----|----|----|----|----|----|----|----|-----|
| C_v | 0 | 17.2 | 50.2 | 87.8 | 146 | 206 | 285 | 365 | 465 | 521 |
| F_L | 0.85 | 0.85 | 0.84 | 0.79 | 0.75 | 0.71 | 0.63 | 0.58 | 0.56 | 0.54 |

**Calculations:**

The following solution schema is based on the iterative method of Clause C.2. The governing equation is presented followed by the computed result based on the current values of all constitutive variables.

**Constant Values:**

The following variables and terms are either constant or remain constant under the conditions supplied above.

- N₁ = 0.0865
- N₂ = 0.00214
- N₁₈ = 1.00

$$F_F = 0.96 - 0.28 \sqrt{\frac{P_v}{P_c}} = 0.956$$

$$\zeta_1 = 0.5 \left[1 - \left(\frac{d}{D_1}\right)^2\right]^2 = 0.160$$

$$\zeta_2 = \left[1 - \left(\frac{d}{D_2}\right)^2\right]^2 = 0.561$$

$$\zeta_{B1} = 1 - \left(\frac{d}{D_1}\right)^4 = 0.811$$

$$\zeta_{B2} = 1 - \left(\frac{d}{D_2}\right)^4 = 0.937$$

**Step 1:** A flow function per Equation (C.2) should be defined:

$$F(C) = 750 - C \cdot N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}}$$

The root of this function corresponds to the solution for the supplied parameters. Note that F_P and ΔP_sizing values will also change with each iteration.

**Step 2:** A lower flow interval limit per C.2.3 should be set:

Set lower limit: C_Lower = 0

From valve data: F_L_Lower = 0.85

Equation (15): F_P_Lower = 1.0

Equation (21): F_LP_Lower = 0.85

ΔP_choked_Lower = (F_LP_Lower / F_P_Lower)² (P₁ − F_F P_v) = 2,418 kPa

ΔP_sizing_Lower = min(ΔP, ΔP_choked_Lower) = 1,310 kPa (since ΔP = 1,310)

Function Value: F_Lower = Q − C_Lower · N₁ · F_P_Lower · √(ΔP_sizing_Lower / (ρ₁/ρ_o)) = 750

**Step 3:** An upper flow interval limit per C.2.4 should be set:

Set upper limit: C_Upper = 0.075 d² N₁₈ = 774.192

From valve data: F_L_Upper = 0.54

Equation (15): F_P_Upper = 0.625

Equation (21): F_LP_Upper = 0.409

ΔP_choked_Upper = (F_LP_Upper / F_P_Upper)² (P₁ − F_F P_v) = 1,520 kPa

ΔP_sizing_Upper = min(ΔP, ΔP_choked_Upper) = 1,310 kPa

Function Value: F_Upper = Q − C_Upper · N₁ · F_P_Upper · √(ΔP_sizing_Upper / (ρ₁/ρ_o)) = −1,096

**Step 4:** It should be checked that interval bounds a solution per C.2.5:

F_Upper = −1,096 and F_Lower = 750

F_Upper and F_Lower are of opposite sign, therefore the selected interval bounds a solution to the problem.

**Step 5:** The interval mid-point and associated values should be computed:

C_Mid = (C_Upper + C_Lower) / 2 = 387.096

From valve data: F_L_Mid = 0.576

Equation (15): F_P_Mid = 0.848

Equation (21): F_LP_Mid = 0.523

ΔP_choked_Mid = (F_LP_Mid / F_P_Mid)² (P₁ − F_F P_v) = 1,349 kPa

ΔP_sizing_Mid = min(ΔP, ΔP_choked_Mid) = 1,310 kPa

Function Value: F_Mid = Q − C_Mid · N₁ · F_P_Mid · √(ΔP_sizing_Mid / (ρ₁/ρ_o)) = −430.7

**Step 6:** The interval definition should be revised per C.2.6. It should be iterated until satisfactory convergence is achieved.

Since the sign of the upper and midpoint function values are the same, the upper interval limit is set equal to the midpoint value and associated terms adjusted accordingly.

**Iteration summary:**

| Iteration | C_Lower | C_Mid | C_Upper | F_L | F_P | F_LP | ΔP_choked | ΔP_sizing | F_Mid |
|-----------|---------|-------|---------|-----|-----|------|-----------|-----------|-------|
| 1 | 0 | 387 | 774 | 0.576 | 0.848 | 0.523 | 1,349 | 1,349 | −431 |
| 2 | 0 | 194 | 387 | 0.718 | 0.954 | 0.690 | 1,856 | 1,856 | −29.4 |
| 3 | 0 | 96.8 | 194 | 0.784 | 0.988 | 0.774 | 2,179 | 2,179 | 313 |
| 4 | 96.8 | 145 | 194 | 0.751 | 0.974 | 0.732 | 2,006 | 2,006 | 130 |
| 5 | 145 | 169 | 194 | 0.734 | 0.965 | 0.711 | 1,929 | 1,929 | 47.3 |
| 6 | 169 | 181 | 194 | 0.726 | 0.960 | 0.701 | 1,892 | 1,892 | 8.23 |
| 7 | 181 | 188 | 194 | 0.722 | 0.957 | 0.696 | 1,874 | 1,874 | −10.8 |
| 8 | 181 | 184 | 188 | 0.724 | 0.958 | 0.698 | 1,883 | 1,883 | −1.32 |
| 9 | 181 | 183 | 184 | 0.725 | 0.959 | 0.700 | 1,887 | 1,887 | 3.44 |
| 10 | 183 | 183.7 | 184 | 0.725 | 0.959 | 0.699 | 1,885 | 1,885 | 1.06 |

**Final Value: C = 183.7**

**Step 7:** The solution should be confirmed:

Calculate the predicted flow rate using the computed value of the flow coefficient and compare to given value of flow rate:

$$Q_{predicted} = C \cdot N_1 F_P \sqrt{\frac{\Delta P_{sizing}}{\rho_1 / \rho_o}} = 749$$

This compares favourably to the given value of 750 m³/h.

---

## Bibliography

- BAUMANN, H.D., *A Unifying Method for Sizing Throttling Valves Under Laminar or Transitional Flow Conditions*, Journal of Fluids Engineering, Vol. 115, No. 1, March 1993, pp. 166-168.
- BAUMANN, H.D., *Effect of Pipe Reducers on Control Valve Sizing*, Instruments and Control Systems, December 1968, pp 99-102.
- STILES, G.F., *Liquid Viscosity Effects on Control Valve Sizing*, Technical Manual TM 17A, October 1967, Fisher Governor Co., Marshalltown.
- BAUMANN, H.D., *What's New in Valve Sizing*, Chemical Engineering, June 1996.
- BOGER, H.W., *Recent Trends in Sizing Control Valves*, Instruments and Control Systems, 1991, pp 117-121.
- SINGLETON, E.W., *Adapting Single Stage Sizing Standards for Multistage Control Valves*, Intech, August 1997.
- SINGLETON, E.W., *The Calculation of the Expansion Factor 'Y' for Multistage Control Valves*, Valve World, Vol. 6, Issue 2, April 2001.
- BOGER, H.W., *The Control Valve Body — a Variable Flow Restrictor*, ISA Preprint No 11, 11-2-66.
- BAUMANN, H.D., *The Introduction of a Critical Flow Factor for Valve Sizing*, ISA Transactions, Vol. 2, pp 107-111. 1963.

---

*Copyright International Society of Automation. Provided by IHS under license with ISA.*

*ISBN: 978-1-937560-61-4*
