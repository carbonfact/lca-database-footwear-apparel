# Documentation

> Part of [Sneaker Shoe Assembly Methodology](README.md)

This document describes the methodology used to construct the Assembly Footwear Datasets, focused exclusively on the assembly phase of footwear, using a modular approach by process and by chemical families. It covers assembly process inputs and outputs only and does **not** include physical footwear materials or components, which are modelled separately.

The database was developed based on primary data from a supplier in Vietnam, collected through an onsite visit followed by additional data collection via email.

## 1. Scope and functional unit

### 1.1 System analysed

The database covers the following assembly processes:

1. Lamination
2. Cutting
3. HF Welding Process
4. Screen Printing
5. Insole
6. Nosew
7. Stitching
8. Stock fit
9. Assembly

Each of these processes was modelled as an autonomous module, with their respective inputs and outputs. Physical footwear materials and components are outside the scope of this database and are modelled separately.

### 1.2 Functional unit

The functional unit adopted is:

- **1 pair of footwear** ("per pair")

The processes were implemented in Activity Browser with reference product and amount = 1 unit, assuming that "unit" represents the operation equivalent per pair, consistent with the structure of the model.

## 2. Modelling strategy

### 2.1 Modular logic

The LCI construction followed a layered logic:

1. **Primary chemicals per process** (e.g., base adhesives, resins, hardeners, main solvents)
2. **Derived/specific chemicals** (hardener, glue, treatment agents, etc.)
3. **Cross-cutting inputs and outputs:**
   - energy
   - water
   - packaging
   - NMVOC
   - waste outputs
4. **Modular integration into the final process activities** (1–9)

This separation enables:
- a clear interpretation of what enters, where, and why,
- traceability of proxy decisions by chemical family,
- reduced duplication and easier future substitutions.

## 3. Cross-process inventory

### 3.1 Electricity

Electricity supply is modelled in two scenarios:

- **VN**: market for electricity, medium voltage, Vietnam
- **GLO**: market group for electricity, medium voltage, GLO (global average)

Vietnam was selected as the primary scenario because it is the origin of the available primary data. The GLO scenario provides a location-independent reference. Both are applied consistently across all processes involving electricity consumption.

### 3.2 Water

Across all processes, water was modelled as:

- **water, decarbonised** (primary proxy)
- **water, deionised** (where process requirements dictate higher purity)

This choice was made to maintain internal consistency and reduce methodological noise until factory- or site-specific industrial water data are available.

### 3.3 NMVOC emissions

Solvent-related emissions were modelled using:

- **non-methane volatile organic compounds (NMVOC)**
- compartment: air
- Biosphere3

This approach was kept uniform, assuming emissions associated with solvent-based systems in relevant processes.

### 3.4 Physical footwear materials and components

No physical materials/components of the footwear were included in this database (upper, outsole, foam, knit upper, etc.). The **Assembly Footwear DB** is a **process-only** database covering chemicals, energy, water, packaging, emissions and waste. Material flows are modelled separately.

## 4. Construction of chemical inputs by phase

### 4.1 Data source

Chemical quantities per process were calculated based on internal data organised in the Excel file:

- **"01-Material used for Cloud 6"**

This file contains the list and/or percentage shares of chemicals used by formulation type and by process.

### 4.2 Calculation method applied

The calculation logic was:

- Identify in Excel the **percentage composition per chemical**, according to:
  - formulation type (hardener, glue, treatment agents, etc.)
  - and associated process (lamination, stock fit, screen printing, etc.)
- Define the **total formulation mass per pair** (or the internally defined reference mass for each process).
- Convert percentages into absolute quantities by applying: m_i = m_total × %_i

This procedure ensures that:
- quantities reflect the real internal composition structure,
- and the model does not depend solely on generic defaults.

## 5. Proxies and process-specific decisions

### 5.1 Lamination

Within lamination chemicals, the internal decision was maintained to consider **Vinyl Acetate – Ethylene copolymers** and **Vinyl Acetate** as represented under the same vinyl acetate proxy family for operational consistency within the current dataset version.

### 5.2 Screen Printing

Proxies were used for resin families, pigments, fillers and solvents, including:

- **polyurethane (flexible foam)** as a resin proxy
- **titanium dioxide + carbon black (50/50)** for pigments
- **brass** for metallic powders
- **silica sand** for texture powders
- **flat glass** for reflective compounds
- **LDPE fine** for matting agent
- **propylene glycol** as humectant
- solvents such as **ethyl acetate** and **n-butyl acetate**

Selection was guided by functional equivalence and compatibility with available ecoinvent entries.

### 5.3 Stitching

The following proxies were used:

- **SBR rubber** → proxy for synthetic rubber
- **Terpene resin** → proxied by **rosin size**

representing auxiliary materials typically associated with stitching/assembly chemistry.

### 5.4 Stock fit

Stock fit includes the most complex chemical set and was modelled using carefully selected proxies, including:

- **1-Ethylpyrrolidin-2-one (NEP)** → proxy NMP
- **UV-curable resin (urethane acrylate system)** modelled as a representative mixture:
  - urethane acrylate oligomer → proxy PU
  - reactive acrylate diluents → proxy butyl acrylate
  - photoinitiator → chemical, organic
  - plus additional electricity for UV curing

Additionally:
- Methoxypropyl acetate 2 → **DPGME**
- Tetramethylene dimethacrylate → **methyl methacrylate**
- 2-Hydroxyethyl methacrylate → **butyl acrylate**
- Phenol, 4-isocyanato-, phosphorothioate (3:1) → **MDI**

### 5.5 Assembly (final process)

In the final assembly module, solvent and aromatic acid proxies were applied using functional equivalence logic, including:

- 1,3-dimethylimidazolidin-2-one → **DMF**
- m-toluic acid → **benzoic acid**
- N,N-diethylformamide → **DMF**
- Dimethyl glutarate → **dimethyl malonate**

### Internal cut-off

The chemical **SW-08AT** was not included in the assembly process because it is < 1% (0.10%), therefore below the internally defined relevance threshold.
