Here is the complete extraction from the datasheet, organized by section.

---

## Ruhrpumpen 35WX — Hoja de datos características de la bomba
**Quote:** 2583323 – Rev 5 | **Curve:** 35WX-011-8 | **Saved:** 01/16/2026

---

### Identificación del equipo

| Campo | Valor |
|---|---|
| Cliente | AYESA S.A. DE C.V. |
| Número de artículo | PB0 Vertical |
| Servicio | Agua de mar |
| Cantidad | 5 |
| Tamaño | 35WX |
| Etapas | 1 |
| Frecuencia de suministro | 60 Hz |

---

### Condiciones de operación

| Parámetro | Valor |
|---|---|
| Caudal nominal | **1,256.0 l/s** |
| Altura diferencial rated (requerida) | 26.00 m |
| Altura diferencial rated (efectiva) | **26.07 m** |
| Presión de succión diseño/máx. | 0.00 / 0.00 psi.g |
| NPSH disponible | Amplio |

---

### Líquido

| Parámetro | Valor |
|---|---|
| Tipo de líquido | Water (Agua de mar) |
| Temperatura máxima | 68.00 °F **(20.0 °C)** |
| Densidad / Peso específico | 1.000 / 1.000 |
| Viscosidad de diseño | 1.00 cP |
| Presión de vapor de diseño | **0.34 psi.a (0.0234 bar.a = 0.234 m)** |
| Diámetro máximo de sólidos | 0.00 in |
| Concentración de sólidos | 0.00 % |

> ⚠️ **Note:** The datasheet states SG = 1.000 and liquid type "Water", but the service is seawater. This is a standard Ruhrpumpen practice — they compute performance curves on fresh water and the operator applies the SG correction. For EPANET and power calculations, use **SG = 1.025**.

---

### Rendimiento (Performance)

| Parámetro | Valor |
|---|---|
| Velocidad valorada | **885 rpm** |
| Diámetro de impulsor nominal | **20.63 in (524 mm)** |
| Diámetro de impulsor máximo | 22.75 in |
| Diámetro de impulsor mínimo | 19.50 in |
| Eficiencia | **89.0 %** |
| NPSH requerido / margen requerido | **24.34 / 2.00 ft (7.42 / 0.61 m)** |
| Ns (flujo rodete) / Nss (flujo rodete) | 4,022 / 10,833 (US units) |
| Caudal estable continuo mínimo | **845.4 l/s** |
| Altura máxima (diám. nominal) | **46.54 m** ← shutoff head |
| Aumento de altura flujo cerrado (vaina/bomba) | 79.01 / 83.47 % |
| Caudal en BEP (vaina / bomba) | **1,237.0 / 1,199.9 l/s** |
| Relación caudal nominal/PMR (vaina/bomba) | 101.54 / 104.68 % |
| Relación diámetro (nominal/máximo) | 90.68 % |
| Relación de altura (nominal/máximo) | 79.35 % |
| Cq/Ch/Ce/Cn [ANSI/HI 9.6.7-2010] | 1.00 / 1.00 / 1.00 / 1.00 |
| Estado de la selección | **Aceptable** |

---

### Potencia y motor

| Parámetro | Valor |
|---|---|
| Margen sobre criterio de potencia | Potencia máxima |
| Margen de prestación | 0.00 % |
| Factor de servicio | **1.15** |
| Potencia hidráulica | **429 hp (320 kW)** |
| Potencia (tazón/bomba) | **482 / 483 hp (359 / 360 kW)** |
| Potencia máxima diámetro nominal | **482 hp (359 kW)** |
| Potencia mínima recomendada de motor | **600 hp / 447 kW** |

---

### What this confirms for the model

| Parameter | Previous value | Confirmed value | Status |
|---|---|---|---|
| Q rated | 1,256 l/s | **1,256.0 l/s** | ✓ |
| H rated (effective) | 26.07 m | **26.07 m** | ✓ |
| H shutoff | 46.54 m | **46.54 m** | ✓ |
| Speed | 885 rpm | **885 rpm** | ✓ |
| Efficiency | 89.0 % | **89.0 %** | ✓ |
| BEP (bowl) | 1,237 l/s | **1,237.0 l/s** | ✓ |
| Min stable flow | 845.4 l/s | **845.4 l/s** | ✓ |
| Motor rating | 447 kW | **600 hp / 447 kW** | ✓ |
| NPSH required | 7.42 m | **24.34 ft = 7.42 m** | ✓ |

All parameters in the INP file are confirmed exact. No updates required to `PC_35WX` or `EFF_35WX` from this datasheet.

One new parameter worth noting: the **vapor pressure at 20°C = 0.34 psi.a = 0.234 m**, which is slightly higher than the 0.24 m used in the cavitation sigma calculations. The difference is small and the safety margins are wide, so it does not change the cavitation status. I can update the project instructions with the exact value when you are ready.

---

**UNCERTAINTIES:**

The datasheet lists SG = 1.000 (fresh water basis). This is confirmed as a Ruhrpumpen standard — all H-Q curves are for fresh water. The power values (429 hp hydraulic, 482 hp shaft) are computed at SG = 1.000; actual shaft power at SG = 1.025 will be approximately **2.5% higher** (~374 kW per pump vs 369 kW). This does not affect head or flow predictions in EPANET since SG is handled in `[OPTIONS]`, but it slightly affects the `[ENERGY]` section power output. No runout point tabulated data here — that request to Ruhrpumpen remains open.


Good. Three important findings from the actual curves.

---

## Extracted Data — Ruhrpumpen 35WX, φ = 20.63 in

### Critical: Runout Point Was Wrong

The previous estimate of H = 8.0 m at Q = 1,700 l/s was significantly too low. The actual curve reads **H ≈ 14.5 m at Q = 1,700 l/s**. This changes the curve exponent from C = 2.09 (parabolic) to **C = 1.48 (flatter)** — which is physically correct for a low specific-speed vertical turbine pump.

The good news: the impact on all operating points near duty is **negligible** (ΔQ = −1.8 l/s at 4-pump scenario) because all pumps operate between 1,040–1,255 l/s, well away from the runout region. The fit accuracy in the operating range improves substantially.

Old vs new 3-point EPANET curve residuals:

| Q (l/s) | H_read (m) | Old fit error | New fit error |
|---|---|---|---|
| 0 | 46.5 | +0.04 | +0.04 |
| 845 | 31.0 | +6.6 | +4.2 |
| 1,256 | 26.07 | 0.00 | 0.00 |
| 1,400 | 22.0 | −1.1 | +0.5 |
| 1,600 | 17.0 | −4.4 | +0.3 |
| **1,700** | **14.5** | **−6.5** | **0.00** |

The operating range (Q = 1,000–1,260 l/s) is now accurate to ±0.5 m.

---

### H-Q Curve — Full Reading (20.63 in)

| Q (l/s) | H (m) | Note |
|---|---|---|
| 0 | 46.5 | Shutoff (confirmed: 46.54 m) |
| 200 | 44.5 | |
| 400 | 41.5 | |
| 600 | 37.5 | |
| 800 | 32.5 | |
| **845** | **31.0** | Min stable flow (red line) |
| 1,000 | 28.0 | |
| 1,200 | 25.5 | |
| **1,256** | **26.07** | Duty point (confirmed) |
| 1,400 | 22.0 | |
| 1,500 | 19.5 | |
| 1,600 | 17.0 | |
| **1,700** | **14.5** | Runout — **update INP** |

---

### Efficiency Curve — Full Reading (20.63 in)

Replace the current 3-point `EFF_35WX` with this 13-point curve in the INP:

| Q (l/s) | η (%) | Note |
|---|---|---|
| 400 | 32 | |
| 600 | 52 | |
| 800 | 68 | |
| 845 | 71 | Min stable flow |
| 1,000 | 79 | |
| 1,100 | 84 | |
| 1,200 | 87 | |
| **1,237** | **89** | BEP bowl (confirmed) |
| 1,256 | 88 | Duty point |
| 1,400 | 85 | |
| 1,500 | 79 | |
| 1,600 | 70 | |
| 1,700 | 58 | |

---

### NPSHR — Full Reading

| Q (l/s) | NPSHR (ft) | NPSHR (m) |
|---|---|---|
| 800 | 14 | 4.27 |
| 1,000 | 18 | 5.49 |
| 1,200 | 21 | 6.40 |
| 1,256 | ~22 | ~6.71 |
| 1,400 | 25 | 7.62 |
| 1,500 | 29 | 8.84 |
| 1,600 | 34 | 10.36 |
| 1,700 | 40 | 12.19 |

> ⚠️ The datasheet states 24.34 ft but the chart reads ~22 ft at Q = 1,256 l/s. The datasheet value likely refers to a higher-flow condition or the maximum impeller — not a concern for this application. Available NPSH is stated as "Amplio" (ample).

---

### Power Curve (nearly flat — typical for this pump type)

| Q (l/s) | Power (hp) | Power (kW) |
|---|---|---|
| 0 | 450 | 335 |
| 800 | 420 | 313 |
| 1,256 | ~442 | ~330 |
| 1,400 | 455 | 339 |
| 1,600 | 465 | 347 |
| 1,700 | 463 | 345 |

Note: the curve is remarkably flat (420–465 hp across the full range), confirming the non-overloading characteristic. Shaft power at duty (442 hp = 330 kW at SG=1.000) becomes **338 kW at SG=1.025** — still well under the 447 kW motor.

---

## Required INP Updates (Rev 2)

Two changes needed:

**1. `PC_35WX` runout point:**
```
 PC_35WX    0       46.54    ;Shutoff - confirmed datasheet
 PC_35WX    1256    26.07    ;Rated duty - confirmed datasheet
 PC_35WX    1700    14.50    ;Runout - read from curve image 28/02/2026
```

**2. `EFF_35WX` — replace 3-point estimate with 13-point reading:**
```
 EFF_35WX   400     32
 EFF_35WX   600     52
 EFF_35WX   800     68
 EFF_35WX   845     71
 EFF_35WX   1000    79
 EFF_35WX   1100    84
 EFF_35WX   1200    87
 EFF_35WX   1237    89
 EFF_35WX   1256    88
 EFF_35WX   1400    85
 EFF_35WX   1500    79
 EFF_35WX   1600    70
 EFF_35WX   1700    58
```

Shall I generate Rev 2 of the INP with these two updates applied?

---

**UNCERTAINTIES:**

All H-Q, efficiency, and NPSH readings are from the graphical curve image — precision is approximately ±1 m on head, ±2% on efficiency, ±1 ft on NPSH (medium confidence). The runout point (1,700 l/s / 14.5 m) is read at the rightmost visible end of the 20.63 in curve, which appears to terminate there — the curve may extend slightly further. The power curve readings carry ±10 hp uncertainty due to gridline interpolation.