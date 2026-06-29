# Life Cycle Inventory

> Part of [3D Knitting Methodology](README.md)

## 3. Inventory Data -- 3D Knitting (mix)

| Category | Flow | Amount | Unit | Comment |
|---|---|---|---|---|
| **Product** | 3D knitted garment | 1 | kg | Average of mixed yarn types (cotton/synthetic). |
| **Technosphere flows** | Dtex Yarn ("e.g. Cotton") -- yarn losses | 0.02 | kg | Yarn losses 2% (Laursen 2007; van der Velden 2014; Sandin 2019). Typical realisation 94--98% (Advanced Knitting Technology, 2021; Rakib Ahmed, 2024). |
| | Lubricant, average | 0.008 | kg | Lubricant: 8 g/kg fabric (Sandin et al. 2019, p. 45 -- "The lubricant was assumed to correspond to 8% of the weight of the knit.") |
| | Air emissions from lubricant | 0.008 | kg | Equal to lubricant mass for simplicity. |
| **Electricity / heat** | Electricity mix | 4.8 | kWh | Derived from machine data: 1.8 kW x 1.2 garments/h x 0.45 kg/garment, yielding 3--5 kWh/kg (Shima Seiki SWG-XR & MACH2XS; Stoll CMS; NTNU 2024). Confirmed by manufacturer specs. |
| **Indirect energy** | HVAC, compressors, lighting | 4.46 | kWh | Standardised value for knitting indirect systems (compressed air, cooling, robotics). |
| **Capital goods** | Building machine (market for building machine) | 0.0004 | kg/kg fabric | Based on 1,200--1,400 kg machine amortised over 360,000 kg lifetime output (see below). |
| **Waste to treatment** | EoL Machine (Steel) | 0.0003 | kg | 85% of total mass distributed by lifetime output. |
| | Recycling others (Other Materials) | 0.0001 | kg | 15% of mass (electronics, polymer components). |
| | Textile waste incineration (no credits) | 0.02 | kg | Seamless production: >95% utilisation, <5% waste (K&G Garment 2025; GIZ 2023). |

---

## 4. Capital Goods (Machine)

### 4.1 Equipment data

| Machine | Weight (kg) | Source |
|---|---|---|
| Shima Seiki SWG-XR124 / XR154 | 1,300--1,400 | Shima Seiki 2025 datasheet |
| Shima Seiki MACH2XS | 1,000--1,212 | Shima Seiki 2025 |
| Stoll CMS 3D | 1,200 | Stoll / Karl Mayer catalogue |

### 4.2 Allocation parameters

| Scenario | Years | Hours/day | Days/year | Productivity (kg/h) | Lifetime output (kg) | Allocation (kg/kg fabric) |
|---|---|---|---|---|---|---|
| **Average** | 15 | 16 | 300 | 5 | 360,000 | 0.0004 |

> Machine allocation is calculated as:
> `kg machine per kg fabric = M_machine / Q_lifetime`

### 4.3 End-of-Life (EoL) allocation

| Material | Share (%) | Weight (kg) | Allocation (kg/kg fabric) |
|---|---|---|---|
| Steel | 85 | 1,105 | 0.0003 |
| Other materials | 15 | 195 | 0.0001 |

### 4.4 ecoinvent representation

| Field | Entry |
|---|---|
| **Dataset** | market for building machine (GLO) |
| **Amount** | 2.9E-07 unit/kg |
| **Unit** | unit |
| **Product** | building machine |

*(Calculated from 0.0004 / 1,400 kg.)*

### 4.5 Building Infrastructure

The 3D / WHOLEGARMENT knitting process model includes an optional building infrastructure (pavilion) share as a modular and auditable input. The building is represented by an ecoinvent-style construction dataset ("building, hall") whose reference flow is m^2 of industrial hall.

**4.5.1 Allocation principle (area amortisation over lifetime output).**
Building infrastructure is attributed to 1 kg of knitted garment by amortising the allocated hall area over the lifetime production associated with the knitting cell:

$$
\text{Building intensity (m²/kg)} = \frac{A_{\text{alloc}} \text{ (m²)}}{Q_{\text{lifetime}} \text{ (kg)}}
$$

$$
Q_{\text{lifetime}} = \text{productivity (kg/h)} \times \text{hours/day} \times \text{days/year} \times \text{years}
$$

where $A_{\text{alloc}}$ is the hall area allocated to the knitting cell (machine footprint + access + yarn storage + programming workstation + maintenance space + internal logistics), and $Q_{\text{lifetime}}$ is the total knitted output produced during the reference service life under the chosen operating regime.

**Technology rationale.**
3D / WHOLEGARMENT knitting produces complete, fully fashioned garments in a single operation with near-zero cut waste. However, the complexity of the knitting programme, frequent needle-bed changes, and the significantly lower knitting speed relative to circular or seamless technologies result in the lowest throughput per m^2 of all knitting technologies considered. This low throughput drives the highest building intensity per kg of output in the technology group.

**Practical implementation.**
In the 3D / WHOLEGARMENT knitting foreground unit process, we add an input: *building, hall* (unit = m^2) with amount = 4.86E-04 m^2/kg.

**End-of-life of the building.**
The building dataset includes construction, maintenance and decommissioning within the background system model. No separate building EoL module is created in the foreground; only the amortised m^2/kg input is provided.

**Default value (this study).** In the absence of site-specific $A_{\text{alloc}}$ and $Q_{\text{lifetime}}$, the following reference intensity is applied:

> 3D / WHOLEGARMENT knitting: **4.86E-04 m^2/kg**

This is the highest value in the technology group, consistent with the expectation that 3D knitting has substantially lower throughput per allocated space than all other knitting technologies. Physical plausibility was cross-checked using machine envelope data from SHIMA SEIKI MACH2VS WholeGarment (A = 3430 mm, B = 3266 mm, envelope approximately 11.2 m^2) with a cell factor of ~3x, yielding an allocated area and calculated intensity in the same order of magnitude as the adopted default.

---

## 5. Indirect Energy

Indirect energy (HVAC, compressors, lighting, robotics) is modelled as **4.46 kWh/kg**, consistent with all knitting processes.

In 3D knitting, this category is particularly relevant due to:

- increased use of vacuum and suction for yarn handling,
- robotic arms for automated take-down and quality inspection,
- air-conditioning to stabilise yarn humidity.

The indirect-to-direct electricity ratio (~1:1) is realistic for 3D knitting environments with moderate automation.

| Subsystem | Share (%) | Equivalent (kWh/kg) |
|---|---|---|
| Machines | 35 | 1.56 |
| Compressors | 25 | 1.12 |
| HVAC | 30 | 1.34 |
| Lighting | 6.5 | 0.29 |
| Cleaning / auxiliaries | 3.5 | 0.16 |

---

## 6. Waste and Material Efficiency

3D knitting eliminates cutting and assembly waste.

Compared to traditional garment production (10--25% cutting waste), seamless knitting reaches >95% material utilisation (GIZ, 2023; K&G Garment, 2025).

The model therefore applies **0.02 kg/kg** textile waste, equivalent to ~2% of yarn input.

---

## 7. Key Assumptions Summary

| Parameter | Average value | Comment |
|---|---|---|
| **Electricity (machine)** | 4.8 kWh/kg | Based on Shima Seiki and Stoll specs |
| **Indirect energy** | 4.46 kWh/kg | Harmonised with other knitting processes |
| **Lubricant** | 0.008 kg/kg | 3--8 g/kg per literature |
| **Yarn loss** | 0.02 kg/kg | 2% default, consistent with yarn realisation 94--98% |
| **Machine mass allocation** | 0.0004 kg/kg | Derived from 1,200--1,400 kg machine |
| **EoL (steel)** | 0.0003 kg/kg | 85% share |
| **Textile waste** | 0.02 kg/kg | <5% material losses |
