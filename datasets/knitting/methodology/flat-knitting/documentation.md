# Documentation

> Part of [Flat Knitting Methodology](README.md)

## 1. Background

### 1.1 Context

This document describes the modelling approach for the **flat knitting process** for a functional unit of **1 kg of knitted fabric ("coarse knitted tricot")**.

It is designed so that every team member can understand:

- which data sources were used,
- how the three scenarios (best / average / worst) were constructed,
- how yarn losses, lubricants, electricity, waste and capital goods were modelled,
- how indirect energy (HVAC, compressors, lighting, cleaning systems) was handled.

### 1.2 Scope

- **Functional unit**: 1 kg of knitted fabric.
- **Technology**: flat knitting (mix of typical machine types; mid-level scenario).
- **Included**:
  - yarn losses,
  - lubricants and associated emissions,
  - electricity consumption (direct and indirect from the process),
  - textile waste to treatment,
  - capital goods (machine) and end-of-life (EoL) of machine materials.
- **Excluded**:
  - fibre and yarn production (handled upstream),
  - building construction,
  - packaging and distribution.

## 2. Analysis

### 2.1 Key findings from literature

1. **Flat-knitting-specific data are extremely scarce.**
   Most studies either combine flat and circular knitting or report factory-level electricity averages without distinction between technologies.

2. **Electricity values with the strongest evidence**:
   - **EcoBalyse**: 1.2--2.4 kWh/kg for knitting.
   - **van der Velden et al. (2013)**: ~1.16 kWh/kg for flat knitted fabrics.

3. **Yarn losses (waste yarn during knitting)**:
   - Typically **1--5%**, depending on yarn, machine efficiency and operator adjustments.
   - EcoBalyse: **3--5.5%** (flat and circular knitting).
   - Sources: Laursen 2007; Sandin 2019; Roos 2015.

4. **Lubricant consumption**:
   - Typical: **~0.005 kg/kg fabric**.
   - Worst case: **0.008 kg/kg**.
   - Sources: Idemat 2012; Hasanbeigi & Price 2015; Sandin 2019.

5. **Textile waste (trimmings, machine adjustments, errors)**:
   - Around **1.5--5%**.
   - EcoBalyse: **3--5.5%**.
   - Sources: Laursen 2007; Sandin 2019; Roos 2015.

6. **Capital goods (machine) and EoL**:
   - EF and ecoinvent require infrastructure/capital goods to be included unless excluded with justification.
   - Mass-based amortisation over lifetime output is the recommended approach.

7. **Indirect energy (HVAC, compressors, lighting, cleaning)**:
   - Sub-metered data rarely exist.
   - Evidence from spinning and weaving shows that compressors, HVAC and auxiliaries may represent a substantial share of electricity consumption.
