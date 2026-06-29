# Documentation

> Part of [Synthetic PU Leather Methodology](README.md)

This document describes the methodology used to construct the Synthetic PU Leather datasets, covering the combined wet and dry manufacturing process for PU (polyurethane) leather with a thickness of 1.5-2 mm, intended for footwear applications. Two variants are modeled: DMF-free (water-borne) and DMF-based (solvent-based).

## 1. Scope and functional unit

### 1.1 System analysed

The database covers PU synthetic leather production through a combined wet and dry process with four manufacturing steps:

1. **Fabric preparation**: base fabric cleaning and surface treatment to improve adhesion and ensure uniform polymer application
2. **Impregnation** (wet method): polyurethane slurry application, drying and curing to stabilize the initial PU structure
3. **Foam layer** (wet method): foamed polymer mixture synthesis with thickening and foaming agents, uniformly applied and cured
4. **Top layer** (dry method): final polyurethane mixture cast onto release paper, dried, then glued or laminated onto the foam layer

Each foreground database contains 5 activity datasets corresponding to these process steps plus a "Finished PU leather" assembly activity.

### 1.2 Functional unit

The functional unit is:

- **1 m² of PU leather** (1.5-2 mm thickness)

An areal density of 1 kg/m² is assumed for the finished PU leather. This means impact scores per m² can be read directly as scores per kg. This is a simplifying assumption consistent with typical PU synthetic leather in the 1.5-2 mm thickness range for footwear applications.

### 1.3 System boundaries

- **Cradle-to-gate**: raw material extraction through manufacturing
- **Excluded**: transport to manufacturing site, use phase, end-of-life
- **Geographical boundaries**: CN (electricity), GLO/RoW (materials)

## 2. Key differences: DMF-based vs DMF-free

The DMF-based (solvent-based) process results in:

- Use of N,N-Dimethylformamide (DMF) as solvent, leading to higher toxicity impacts
- Longer drying periods (to remove DMF, which boils at 153°C vs water at 100°C)
- More water consumption
- More wastewater (contaminated with DMF)

The top layer is the only process step with a significant electricity difference. The DMF-based top layer requires ~4x more energy (24 vs 6.11 kWh/m²) because:
- DMF has a higher boiling point requiring higher temperatures
- Solvent recovery is needed to capture and recycle evaporated DMF
- Extended curing time is necessary for complete DMF removal

## 3. Electricity consumption

Electricity consumption per process step (per m²):

| Process step | DMF-free (kWh/m²) | DMF-based (kWh/m²) |
|---|---|---|
| Fabric preparation | 2 | 2 |
| Impregnation | 2.055 | 2.04 |
| Foam layer | 6 | 6.07 |
| Top layer | 6.11 | 24 |
| **Total** | **16.17** | **34.11** |

All electricity is modeled as CN medium voltage (Chinese grid mix).

The electricity values were derived through the Piccinno et al. (2016) scale-up framework, converting laboratory-scale process parameters from patents into industrial-scale energy estimates, calibrated against real industrial machinery specifications.

## 4. Background database

- **ecoinvent 3.12 cutoff**: background database for all material and energy inputs
- **EF v3.1**: impact assessment method with 16 impact categories

## 5. Data sources

- **Patent 1 (Water-borne / DMF-free)**: Luo, X., Feng, J., Qu, J., & Li, P. (2012). Chinese Patent CN102080332B. Assignee: Hefei Scisky Technology Co Ltd.
- **Patent 2 (DMF-based / Solvent-based)**: Huang, Z. (2016). Chinese Patent CN106192450A. Assignee: Fujian Boyi Mstar Technology Ltd.
