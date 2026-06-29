# Life Cycle Inventory

> Part of [Circular Knitting Methodology](README.md)

## 2. Methodological Overview

### 2.1 Yarn losses and lubricant -- dependency on yarn fineness (dtex)

#### Concept

Circular knitting waste and lubricant use vary with yarn fineness.
Finer yarns require longer machine time, experience higher friction, and tend to break more often -- leading to higher waste, lubricant use and, indirectly, energy demand.

The base definition follows the same logic as in flat knitting:

> *"Input quantity refers to the net yarn required to produce 1 kg of knitted fabric. Yarn losses during the knitting process (thread breaks, edge waste, trial runs) should be included. Typical material losses for knitting range between 1--5%, depending on yarn type and machine efficiency. If no primary data exist, use 2% as default."*
>
> (Laursen et al., 2007; van der Velden et al., 2014; Sandin et al., 2019 -- Mistra)

#### Classification by yarn fineness (dtex)

| Yarn category | Tex range | Approx. dtex | Description |
|---|---|---|---|
| **Super fine** | 2 -- 7.5 tex | < 75 dtex | Very fine yarns used for lightweight jerseys |
| **Fine** | 7.5 -- 16 tex | 75 -- 160 dtex | Common in high-quality apparel fabrics |
| **Medium** | 16 -- 40 tex | 160 -- 400 dtex | Typical for sportswear and medium-weight knits |
| **Coarse** | > 40 tex | > 400 dtex | Thicker yarns for heavy or technical fabrics |

*(Burkinshaw 2016; Banerjee 2014; Ray 2012; Australian Cotton 2022)*

#### Adjustment logic

| Parameter | Observation | Representative quote | Source |
|---|---|---|---|
| **Yarn loss / waste** | Finer yarns are more fragile and break more often during operation. | "Reducing the yarn linear density from 300 to 45 dtex significantly increased yarn breakage during machine operation." | Haque & Naebe (2024) |
| **Lubricant** | More yarn contact and friction increase lubricant demand. | "Yarns with lower dtex required increased lubricant pre-treatment due to higher friction and mechanical interaction." | Liu, Cano & Ardanuy (2025) |
| **Indirect energy (HVAC, air, etc.)** | Lower throughput leads to more energy per kg. | "Knitting finer yarns resulted in longer machine running time, thereby increasing energy use per kilogram of fabric." | Palamutcu (2016); Haque & Naebe (2024) |
| **Capital allocation (machine)** | Longer knitting time increases depreciation per kg. | "Lower tex yarns required longer processing time, raising capital cost per kg of output." | INTI (2021) |

#### Parameter values applied

| Yarn fineness | Yarn losses (%) | Lubricant (kg/kg fabric) |
|---|---|---|
| **Super fine (<75 dtex)** | 5% | 0.008 |
| **Fine (75--160 dtex)** | 4% | 0.007 |
| **Medium (160--400 dtex)** | 3% | 0.006 |
| **Coarse (>400 dtex)** | 2% | 0.005 |

These values are used as a reference to adjust inventory parameters when the yarn fineness is known.
If not, the **medium range** (3% losses, 0.006 kg/kg lubricant) is applied by default.

## 3. Building Infrastructure, Capital Goods and End-of-Life (EoL)

### 3.1 Modelling approach

**Goal and scope:**
The circular knitting process model includes **capital goods (machinery)** and their **end-of-life** as separate mass-based allocations, consistent with EF and ecoinvent guidelines.

We apply the same calculation logic used in the flat knitting process:

$$
M_{\text{machine per kg fabric}} = \frac{M_{\text{machine}}}{Q_{\text{lifetime}}}
$$

where

$$
Q_{\text{lifetime}} = \text{productivity (kg/h)} \times \text{hours/day} \times \text{days/year} \times \text{years}
$$

- **Machine mass** is taken from OEM brochures.
- **Productivity** is taken from manufacturer specifications (e.g., Mayer & Cie., Leadsfon).
- **Service life** parameters vary by scenario (see below); **we are using average**.

### 3.2 Lifetime parameters (for transparency)

| Scenario | Years | Hours/day | Days/year | Productivity (kg/h) | Resulting allocation (kg/kg fabric) |
|---|---|---|---|---|---|
| **Best case (BCS)** | 20 | 24 | 365 | 30 | 0.0005 |
| **Average case** | 15 | 16 | 300 | 30 | 0.0013 |
| **Worst case (WCS)** | 10 | 8 | 300 | 30 | 0.0039 |

These values correspond to the **mass of machine attributed per kilogram of fabric**.
They represent the "infrastructure weight" of the process and ensure consistency across product systems.

### 3.3 End-of-life allocation

Machine composition is assumed **2800 kg**:

- **85% steel** --> 2380 kg
- **15% other materials** --> 450 kg

EoL per kg of fabric (average scenario):

| Material | Allocation (kg/kg fabric) | Note |
|---|---|---|
| Steel | 0.0011 | Recycled or disposed depending on scenario |
| Other materials (Electric and Electronics) | 0.0002 | Non-ferrous components (motors, electronics) |

### 3.4 Alignment with standards

- Complies with EF guidelines for capital goods inclusion.
- Mirrors ecoinvent's approach to infrastructure amortisation and decommissioning.
- Neutral and impact-method independent.

### 3.5 In ecoinvent format

For the **"market for building machine"** dataset:

| Field | Entry |
|---|---|
| **Amount** | 4.6E-07 unit/kg (average scenario) |
| **Unit** | unit |
| **Product** | building machine |
| **Dataset** | market for building machine / GLO |

*(Derived from 0.0013 kg/kg fabric / 2800 kg machine weight.)*

### 3.6 Building Infrastructure

The circular knitting process model includes an optional building infrastructure (pavilion) share as a modular and auditable input. The building is represented by an ecoinvent-style construction dataset ("building, hall") whose reference flow is m^2 of industrial hall.

**3.6.1 Allocation principle (area amortisation over lifetime output).**
Building infrastructure is attributed to 1 kg of knitted fabric by amortising the allocated hall area over the lifetime production associated with the knitting cell:

$$
\text{Building intensity (m²/kg)} = \frac{A_{\text{alloc}} \text{ (m²)}}{Q_{\text{lifetime}} \text{ (kg)}}
$$

$$
Q_{\text{lifetime}} = \text{productivity (kg/h)} \times \text{hours/day} \times \text{days/year} \times \text{years}
$$

where $A_{\text{alloc}}$ is the hall area allocated to the knitting cell (machine footprint + access + creel/yarn storage + maintenance space + internal logistics), and $Q_{\text{lifetime}}$ is the total knitted output produced during the reference service life under the chosen operating regime.

**3.6.2 Technology rationale.**
Circular knitting is the highest-throughput knitting technology, operating continuously with minimal interruptions. Its compact cylindrical machine footprint combined with high production rates yields the lowest building intensity per kg of output among all knitting technologies considered.

**3.6.3 Practical implementation.**
In the circular knitting foreground unit process, we add an input: *building, hall* (unit = m^2) with amount = 1.00E-05 m^2/kg.

**3.6.4 End-of-life of the building.**
The building dataset includes construction, maintenance and decommissioning within the background system model. No separate building EoL module is created in the foreground; only the amortised m^2/kg input is provided.

**Default value (this study).** In the absence of site-specific $A_{\text{alloc}}$ and $Q_{\text{lifetime}}$, the following reference intensity is applied:

> Circular knitting: **1.00E-05 m^2/kg**

This value is consistent with the benchmark reported in the openLCA Nexus organic cotton sweater case study (1.61E-05 m^2/kg for circular knitting). Physical plausibility was cross-checked using machine envelope data from Terrot GmbH single-jersey machines (e = 2550 mm, k = 2200 mm, envelope approximately 5.6 m^2) with a conservative cell factor of ~6x, yielding A_alloc approximately 35 m^2 and a calculated intensity of ~1.62E-05 m^2/kg -- same order of magnitude as the adopted default.

## 4. Indirect Energy Allocation

### 4.1 Context

For both **flat and circular knitting**, total electricity consumption per kg of fabric is often known, but sub-metered values for subsystems (machines, compressors, HVAC, lighting, cleaning) are rarely available.

To keep models transparent and editable, we allocate total energy into subsystems using percentage factors derived from literature.

### 4.2 Evidence base

- Factory case showing **80%** of total electricity from HVAC and chillers (Sakti et al., 2021).
- Energy breakdown in spinning: **machines 78%, humidification 16%, lighting 3%, compressors 3%** (Hasanbeigi, 2010).
- Compressed air typically **10--40%** of total plant energy (Confederation of Indian Industry, n.d.).
- Cleaning accounts for **~40% of stoppage time** in knitting (Celik et al., 2025).
- Weaving process benchmark: **machines 36.3%, compressors 29.4%, HVAC 27.1%**, total **5.06 kWh/kg** (Koc & Cincik, 2010).

### 4.3 Default distribution ("mid-range knitting" set)

| Subsystem | Share (%) | Comment |
|---|---|---|
| Knitting machines | 35 | Main mechanical load |
| Compressors | 25 | Pneumatic system for needle actuation |
| HVAC | 30 | Air conditioning and humidification |
| Lighting | 6.5 | Facility lighting |
| Cleaning / auxiliaries | 3.5 | Maintenance and automation units |

This distribution is **identical for flat and circular knitting** until factory-level data allow refinement.

### 4.4 Total indirect energy

Extrapolating to include HVAC, air compression and auxiliaries, a consistent high-load total of **4.46 kWh/kg** is adopted.

> Indirect energy = 4.46 kWh/kg fabric

This figure is used for both **flat and circular knitting** as a temporary reference, pending real measurements.
It can later be split by the above percentages to isolate subsystem consumption.

## 5. Electricity Consumption

### 5.1 Concept

Electricity demand in knitting is mainly driven by **yarn fineness (dtex)**, machine speed, and fabric structure.
Finer yarns require longer knitting time and higher frictional work per kilogram of fabric, which increases energy use.

This dependency has been empirically demonstrated by van der Velden et al. (2013) and Sandin et al. (2019), who modelled electricity consumption as inversely proportional to yarn thickness.

### 5.2 Empirical foundation

For knitting, consumption values from Idemat (2012) and ITMF (2010) were interpolated by Sandin et al. (2019), producing the reference equation:

$$
E_{\text{circular knitting}} = 0.00303 + \frac{dtex}{38.805}
$$

To improve representativeness, an expanded dataset of **13 anchor points** (80--300 dtex) from literature and factory records was used to recalibrate the model.

The updated regression (ordinary least squares) yielded:

$$
E_{\text{circular knitting}} = 0.01457 + \frac{37.119}{dtex} \text{ (kWh/kg fabric)}
$$

with **RMSE = 0.0219 kWh/kg** and **R^2 = 0.967**.

This function remains valid between **80 dtex and 400 dtex**.
Outside this range, values should be cautiously extrapolated. We use it down to 40 dtex and up to 450 dtex, but this is considered "low risk".

### 5.3 Representative values

The model was then applied to generate reference values across typical yarn fineness ranges used in **circular knitting**.
For consistency, the corresponding NE, Nm and denier equivalents were also listed.

| Representative Value (kWh/kg) | Circular Knitting dtex | Approx. denier | Nm | NE |
|---|---|---|---|---|
| 0.76 | 40 | 45 | 250 | 148 |
| 0.54 | 60 | 63 | 167 | 98 |
| 0.48 | 80 | 72 | 125 | 74 |
| 0.39 | 100 | 90 | 100 | 59 |
| 0.32 | 120 | 108 | 83 | 49 |
| 0.26 | 150 | 135 | 67 | 40 |
| 0.23 | 170 | 153 | 59 | 35 |
| 0.22 | 180 | 162 | 55 | 33 |
| 0.20 | 200 | 180 | 50 | 30 |
| 0.18 | 230 | 207 | 43 | 27 |
| 0.16 | 250 | 225 | 40 | 24 |
| 0.15 | 270 | 245 | 37 | 22 |
| 0.14 | 300 | 270 | 33 | 20 |
| 0.13 | 330 | 297 | 30 | 18 |
| 0.12 | 370 | 333 | 27 | 16 |
| 0.11 | 400 | 470 | 25 | 15 |
| 0.10 | 450 | 420 | 20 | 13 |

*(Values rounded; derived from E = 0.01457 + 37.119/dtex)*

### 5.4 Interpretation

- Below 80 dtex, consumption rises sharply as machine efficiency drops.
- For coarser yarns (> 400 dtex), marginal energy reduction is minimal.

### 5.5 Application in LCI models

When primary data are unavailable, these reference values are used to populate the **electricity input** of knitting unit processes.

The selected value must correspond to the **yarn fineness (dtex)** of the fabric modelled.
For multi-yarn blends, a **mass-weighted dtex** is calculated prior to lookup.
