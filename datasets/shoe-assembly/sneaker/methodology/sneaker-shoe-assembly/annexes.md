# Annexes

> Part of [Sneaker Shoe Assembly Methodology](README.md)

## 8. Record of methodological decisions

- Modular model by process and chemical families
- FU defined **per pair**
- Two electricity scenarios: VN (market for electricity, medium voltage, Vietnam) and GLO (market group for electricity, medium voltage, GLO)
- Water standardised as **water, decarbonised**
- NMVOC emissions to air via **Biosphere3**
- Proxies applied using functional equivalence logic
- Cut-off applied to **SW-08AT (<1%)**
- Background database: **ecoinvent 3.12** (cut-off)

## 9. Treatment of material losses, Input–Output Ratios (IOR) and defect rate

### 9.1 Rationale

In parallel to the process-level assembly database, material efficiency losses occurring along the footwear manufacturing chain were quantified using **Input–Output Ratios (IORs)** derived from primary gross and net material consumption data.

This approach allows us to:
- explicitly capture cutting losses, trimming losses, yield losses and inefficiencies,
- separate process chemistry and energy modelling from material flow efficiency,
- and apply losses in a transparent, auditable and harmonised manner across the full product system.

### 9.2 Definition of Input–Output Ratio (IOR)

For each material flow, the Input-Output Ratio was calculated as:

IOR = Gross material input / Net material incorporated into product

An IOR equal to 1 indicates no loss, while values above 1 reflect material losses upstream of the final product.

### 9.3 Data source and calculation

IORs were computed using the **Materials / Raw Materials table**, based on primary client data, including:
- material specifications,
- gross input quantities per process,
- net quantities effectively incorporated into footwear components.

For each process (lamination, cutting, HF welding, stitching, stock fit, assembly, etc.), individual IORs were calculated at material level.

### 9.4 Modelling approach and application point

To preserve model clarity and avoid double counting, the following modelling strategy was adopted:

- **All process modules** (chemicals, energy, water, NMVOC, waste) are modelled **per functional unit (1 pair)** assuming ideal yield.
- **Material losses (IORs)** are **not applied within individual process modules**.
- Instead, an **average material IOR**, aggregated across the full process chain, is applied **once at the end of the assembly chain**, on top of the net material demand.

This ensures that:
- chemical and energy intensities remain comparable across scenarios,
- material inefficiencies are accounted for consistently,
- and future updates to loss rates do not require re-building process inventories.

### 9.5 Defect rate treatment

In addition to process-related material losses, a **defect rate** (rejected or non-conforming pairs) is applied **on top of the average IOR**, reflecting manufacturing quality losses.

Total factor = Average IOR × (1 + Defect rate)

This defect rate is applied at the **final product level**, consistent with industrial practice and avoiding distortion of upstream process intensities.

Defect Rate: 0.2%

### 9.6 Assumptions and limitations

- IORs are derived from available primary data and may evolve as additional materials or production lines are integrated.
- Averages are used to balance representativeness and model stability.
- Losses are applied to **physical material flows only**, not to chemicals, energy or water used in assembly processes.
- The approach is conservative and aligned with LCA best practice for complex manufactured products.

## 10. Reference flow and scope

**Reference flow:** Assembly Footwear - Process | Functional unit: **1 pair**

This value represents **assembly operations only**, including chemicals, electricity, water, packaging, NMVOC emissions, and process-related waste, **excluding** physical footwear materials and components, which are modelled in a separate system block.

The user is responsible for including material inputs and accounting for material losses (IOR) and defect rates as documented in Section 9.

## References

- ecoinvent v3.12, cut-off system model
- EF v3.1 impact assessment method
- Internal primary data collection from Vietnam-based supplier
