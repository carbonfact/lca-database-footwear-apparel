# Methodology Overview

## General approach

The Open Source LCA Database for Footwear & Apparel follows a **gate-to-gate** modelling approach for each textile manufacturing process. Datasets represent the environmental impact of transforming an input material (yarn, greige fabric, etc.) into an output product (yarn, fabric, dyed textile) at the factory gate.

Each process is modelled as a standalone foreground unit process, linked to the ecoinvent 3.12 background database for upstream inputs (electricity, heat, chemicals, water, waste treatment) and characterised using the **Environmental Footprint (EF) 3.1** method across 16 impact indicators.

## Functional unit

The functional unit is defined per process and specified in each process methodology documentation.

## System boundaries

**Included in each process:**
- Direct electricity consumption (machine operation)
- Indirect energy (HVAC, compressors, lighting, auxiliaries)
- Process-specific inputs (lubricants, sizing agents, dyes, chemicals, water)
- Capital goods (machinery) and their end-of-life
- Building infrastructure (where applicable)
- Yarn/material losses and waste treatment

**Excluded (modelled separately):**
- Upstream fibre and yarn production
- Downstream finishing, assembly, packaging, and distribution
- Use phase and end-of-life of the final product

## Background database

All datasets use **ecoinvent 3.12** (cut-off system model) as the background database. Electricity is modelled using the global market group for medium voltage (`market group for electricity, medium voltage, GLO`) unless a region-specific market is justified.

## Impact assessment method

Life Cycle Impact Assessment (LCIA) is performed using the **EF 3.1** characterisation method, reporting results for all 16 PEF impact indicators. See [impact-indicators.md](impact-indicators.md) for the full indicator list with codes, names, and units.

## Parameterisation

Many process parameters (electricity consumption, lubricant use, yarn waste) are parameterised by **yarn fineness (dtex)** and **fibre type**. This enables the database to cover a wide range of textile products from a consistent modelling framework. The parameterisation approach is documented in each process methodology:

- [Spinning methodology](../datasets/spinning/methodology/)
- [Knitting methodology](../datasets/knitting/methodology/)
- [Weaving methodology](../datasets/weaving/methodology/)
- [Dyeing methodology](../datasets/dyeing/methodology/)

## Methodology documentation

### Cross-cutting methodology

| Document | Description |
|----------|-------------|
| [Impact indicators](impact-indicators.md) | Full table of 16 EF 3.1 indicators with codes, names, and units |
| [Data Quality Rating framework](dqr-framework.md) | PEF DQR scoring methodology and calculation steps |
| [Capital goods (PDF)](capital-goods.pdf) | Machine amortisation approach |
| [Building infrastructure (PDF)](building-infrastructure.pdf) | Building allocation approach |
| [Indirect energy (PDF)](indirect-energy.pdf) | HVAC, compressors, lighting and auxiliaries allocation |

### Process-specific methodology

| Process | Documentation |
|---------|---------------|
| Spinning | [Ring Spun](../datasets/spinning/methodology/ring-spun/) · [Filament](../datasets/spinning/methodology/filament/) · [Open End Rotor](../datasets/spinning/methodology/open-end-rotor/) |
| Knitting | [Flat](../datasets/knitting/methodology/flat-knitting/) · [Circular](../datasets/knitting/methodology/circular-knitting/) · [Seamless](../datasets/knitting/methodology/seamless-knitting/) · [Hosiery](../datasets/knitting/methodology/hosiery-knitting/) · [3D](../datasets/knitting/methodology/3d-knitting/) |
| Weaving | [Weaving](../datasets/weaving/methodology/) |
| Dyeing | [Dyeing](../datasets/dyeing/methodology/) |

## References

- Fazio, S., Castellani, V., & Sala, S. (2020). *Guide for EF-compliant data sets (Version 2.0).* European Commission, JRC.
- Weidema, B. P. et al. (2013). *Overview and methodology: Data quality guideline for the ecoinvent database version 3.* ecoinvent Centre.
- ADEME & Ministere de la Transition Ecologique (2024). *Ecobalyse methodological guide: Textiles and footwear.*
