# Rosarito Desalination Plant — Pump Operation Scenarios Report

| Field | Value |
|-------|-------|
| **Project** | Rosarito Desalination Plant — Seawater Intake System |
| **Client** | CONAGUA / AYESA S.A. de C.V. |
| **Engineer** | Dr. Raul Trujillo (VAG GmbH) |
| **Model** | ROSARITO_EPANET_Rev2.inp |
| **Date** | 2026-02-28 |
| **Software** | EPANET 2.2 via EPyT |

## System Overview

### Topology

```
SEA (H=0m) -> P_INTAKE -> J_SUCTION -> PUMP_1..5 (parallel) -> J_MANIFOLD
-> P_US -> J_RIKO_IN -> RIKO valve (GPV) -> J_RIKO_OUT
-> P_DS -> PLANT (H=18.17m)
```

### Equipment

| Equipment | Specification |
|-----------|---------------|
| Pumps | 5x Ruhrpumpen 35WX vertical centrifugal (4 duty + 1 standby) |
| Control valve | VAG RIKO DN1800 plunger valve |
| Configuration | N+1 redundancy, rule-based staging |
| Pipe material | DN2500 (intake), DN1800 (upstream/downstream) |
| Friction model | Darcy-Weisbach |

## Steady-State Staging Scenarios

| Pumps | RIKO phi (%) | Kv (m3/h) | Q_total (l/s) | Q_total (m3/h) | Q/pump (l/s) | H_pump (m) | dH_RIKO (m) | v_DS (m/s) | hf_INTAKE (m) | hf_US (m) | hf_DS (m) |
|------:|-------------:|----------:|--------------:|---------------:|-------------:|-----------:|------------:|-----------:|--------------:|----------:|----------:|
| 4 | 44 | 21,038.45 | 5012.2 | 18044 | 1253.1 | 26.14 | 7.50 | 1.970 | 0.029 | 0.094 | 0.345 |
| 3 | 38 | 14,444.21 | 3660.9 | 13179 | 1220.3 | 26.93 | 8.50 | 1.439 | 0.016 | 0.052 | 0.190 |
| 2 | 30 | 7,621.47 | 2218.6 | 7987 | 1109.3 | 29.51 | 11.24 | 0.872 | 0.006 | 0.020 | 0.074 |
| 1 | 22 | 3,179.78 | 1012.3 | 3644 | 1012.3 | 31.66 | 13.47 | 0.398 | 0.001 | 0.005 | 0.017 |

## Energy Summary

| Pumps | Q/pump (l/s) | H_pump (m) | eta (%) | P_hyd (kW) | P_shaft (kW) | Motor load (%) | P_total (kW) | E_24h (kWh) |
|------:|-------------:|-----------:|--------:|-----------:|-------------:|---------------:|-------------:|------------:|
| 4 | 1253.1 | 26.14 | 88.0 | 329.4 | 374.3 | 83.7 | 1497.1 | 35931 |
| 3 | 1220.3 | 26.93 | 88.0 | 330.4 | 375.4 | 84.0 | 1126.3 | 27031 |
| 2 | 1109.3 | 29.51 | 88.0 | 329.1 | 374.0 | 83.7 | 748.0 | 17953 |
| 1 | 1012.3 | 31.66 | 88.0 | 322.3 | 366.3 | 81.9 | 366.3 | 8790 |

## Validation — Computed vs Hand-Calculated Reference

Tolerance: 5%. Reference values from Project Instructions Section 5.

### 4-pump scenario (phi=44%) — PASS

| Parameter | Computed | Reference | Deviation (%) | Result |
|-----------|--------:|---------:|--------------:|:------:|
| Q_total | 5012.21 | 5016.00 | 0.08 | OK |
| Q/pump | 1253.05 | 1254.00 | 0.08 | OK |
| H_pump | 26.14 | 26.12 | 0.08 | OK |
| dH_RIKO | 7.50 | 7.51 | 0.09 | OK |

### 3-pump scenario (phi=38%) — PASS

| Parameter | Computed | Reference | Deviation (%) | Result |
|-----------|--------:|---------:|--------------:|:------:|
| Q_total | 3660.85 | 3664.00 | 0.09 | OK |
| Q/pump | 1220.28 | 1221.00 | 0.06 | OK |
| H_pump | 26.93 | 26.90 | 0.10 | OK |
| dH_RIKO | 8.50 | 8.50 | 0.02 | OK |

### 2-pump scenario (phi=30%) — PASS

| Parameter | Computed | Reference | Deviation (%) | Result |
|-----------|--------:|---------:|--------------:|:------:|
| Q_total | 2218.60 | 2221.00 | 0.11 | OK |
| Q/pump | 1109.30 | 1111.00 | 0.15 | OK |
| H_pump | 29.51 | 29.48 | 0.09 | OK |
| dH_RIKO | 11.24 | 11.22 | 0.15 | OK |

### 1-pump scenario (phi=22%) — PASS

| Parameter | Computed | Reference | Deviation (%) | Result |
|-----------|--------:|---------:|--------------:|:------:|
| Q_total | 1012.32 | 1014.00 | 0.17 | OK |
| Q/pump | 1012.32 | 1014.00 | 0.17 | OK |
| H_pump | 31.66 | 31.63 | 0.11 | OK |
| dH_RIKO | 13.47 | 13.44 | 0.23 | OK |

> **Warning:** Q_total = 3644 m3/h < VAG Qmin (4500 m3/h) — known system characteristic for 1-pump


## 24h Extended Period Simulation — Event Log

Pump trips scheduled at:
- **PUMP_4**: trip at hour 6, restore at hour 8
- **PUMP_3**: trip at hour 12, restore at hour 14
- **PUMP_2**: trip at hour 18, restore at hour 20

| Time | P1 | P2 | P3 | P4 | P5 | Active | RIKO | Q_DS (l/s) | Q_DS (m3/h) | H_pump (m) |
|-----:|:--:|:--:|:--:|:--:|:--:|-------:|-----:|-----------:|------------:|-----------:|
| 0:00 | ON | ON | ON | ON | OFF | 4 | 44% | 5012.2 | 18044 | 26.14 |
| 6:00 | ON | ON | ON | OFF | OFF | 3 | 44% | 4083.4 | 14700 | 23.48 |
| 6:00 | ON | ON | ON | OFF | ON | 4 | 38% | 4300.1 | 15481 | 30.28 |
| 6:00 | ON | ON | ON | OFF | ON | 4 | 44% | 5012.2 | 18044 | 26.14 |
| 8:00 | ON | ON | ON | ON | ON | 5 | 44% | 5733.4 | 20640 | 28.65 |
| 8:00 | ON | ON | ON | ON | OFF | 4 | 44% | 5012.2 | 18044 | 26.14 |
| 12:00 | ON | ON | OFF | ON | OFF | 3 | 44% | 4083.4 | 14700 | 23.48 |
| 12:00 | ON | ON | OFF | ON | ON | 4 | 44% | 5012.2 | 18044 | 26.14 |
| 14:00 | ON | ON | ON | ON | ON | 5 | 44% | 5733.4 | 20640 | 28.65 |
| 14:00 | ON | ON | ON | ON | OFF | 4 | 44% | 5012.2 | 18044 | 26.14 |
| 18:00 | ON | OFF | ON | ON | OFF | 3 | 44% | 4083.4 | 14700 | 23.48 |
| 18:00 | ON | OFF | ON | ON | ON | 4 | 44% | 5012.2 | 18044 | 26.14 |
| 20:00 | ON | ON | ON | ON | ON | 5 | 44% | 5733.4 | 20640 | 28.65 |
| 20:00 | ON | ON | ON | ON | OFF | 4 | 44% | 5012.2 | 18044 | 26.14 |
| 24:00 | ON | ON | ON | ON | OFF | 4 | 44% | 5012.2 | 18044 | 26.14 |

## Notes and Warnings

1. **H_PLANT = 18.17 m** is back-calculated from system data, not field-measured. All operating points shift if this value changes.
2. **1-pump scenario** produces Q_total < VAG Qmin (4500 m3/h). This is a known system characteristic, not a modeling error.
3. Valve headloss uses ISO 5167 Kv method: dH = Q^2 x 132.15 / Kv^2. VAG's internal zeta values are **not** used.
4. Pump efficiency is fixed at the duty-point value for energy calculations. Actual efficiency varies with operating point.
5. EPS rule-based controls handle standby pump activation (PUMP_5) and RIKO valve position changes automatically per Georgescu et al. (CCWI 2015).
