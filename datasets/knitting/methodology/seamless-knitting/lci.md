# Life Cycle Inventory

> Part of [Seamless Knitting Methodology](README.md)

## 2. Methodological Overview

### 2.1 Yarn losses and lubricant -- dependency on yarn fineness (dtex)

**Concept**

Yarn losses and lubricant demand depend on yarn fineness and machine efficiency.
Finer yarns require longer running time, higher tension control, and more lubricant per kilogram of output.

**Base definition**

> *"Input quantity refers to the net yarn required to produce 1 kg of knitted fabric. Yarn losses during the knitting process (thread breaks, edge waste, trial runs) should be included."*
>
> (Laursen et al., 2007; van der Velden et al., 2014; Sandin et al., 2019 -- Mistra)

**Empirical references**

- **Material realisation:** 94--98% (Maity et al., 2021; Rakib Ahmed 2024)
- **Lubricant:** 8 g/kg fabric (Sandin et al. 2019, p. 45 -- "The lubricant was assumed to correspond to 8% of the weight of the knit.")

**Values applied**

| Parameter | Average | Comment |
|---|---|---|
| Yarn loss | 2.5% | Derived from 94--98% yarn utilisation |
| Lubricant | 0.008 kg/kg | Upper-bound value adopted for high-load operation |

---

### 2.2 Electricity consumption -- direct and indirect energy

**Direct electricity (machine operation)**

Based on EcoBalyse, Maity et al. (2021) and Shima Seiki datasheets, seamless knitting machines typically consume **1.2--2.1 kWh/kg** of fabric.
A mid-range **average value of 1.5 kWh/kg** is adopted for modelling.

**Indirect energy (compressors, HVAC, lighting, cleaning)**

The same structure used in flat and circular knitting is retained, totalling **4.46 kWh/kg** distributed as:

- 35% knitting machines
- 25% compressors
- 30% HVAC
- 6.5% lighting
- 3.5% auxiliaries

This ensures methodological alignment across knitting technologies.

---

## 3. Capital Goods and End-of-Life

### 3.1 Machine characteristics

| Machine | Weight (kg) | Source |
|---|---|---|
| Santoni SM8-TR1S | 750 | Santoni 2023 -- SM8-TR1S datasheet |

### 3.2 Lifetime parameters

| Scenario | Years | Hours/day | Days/year | Productivity (kg/h) | Allocation (kg/kg garment) |
|---|---|---|---|---|---|
| Best case (BCS) | 20 | 24 | 365 | 26.2 | 0.0002 |
| Average | 15 | 16 | 300 | 26.2 | 0.0004 |
| Worst case (WCS) | 10 | 8 | 300 | 26.2 | 0.0012 |

### 3.3 End-of-life allocation

| Material | Share (%) | Allocation (kg/kg garment) | Notes |
|---|---|---|---|
| Steel | 85% | 0.0003 | Recycled or disposed depending on scenario |
| Other materials | 15% | 0.0001 | Includes electronics and polymers |

**Machine composition:**
Approx. 85% steel (637.5 kg) and 15% other materials (112.5 kg).

### 3.4 Building Infrastructure

The seamless knitting process model includes an optional building infrastructure (pavilion) share as a modular and auditable input. The building is represented by an ecoinvent-style construction dataset ("building, hall") whose reference flow is m^2 of industrial hall.

**Allocation principle (area amortisation over lifetime output).**
Building infrastructure is attributed to 1 kg of knitted garment by amortising the allocated hall area over the lifetime production associated with the knitting cell:

$$
\text{Building intensity (m²/kg)} = \frac{A_{\text{alloc}} \text{ (m²)}}{Q_{\text{lifetime}} \text{ (kg)}}
$$

$$
Q_{\text{lifetime}} = \text{productivity (kg/h)} \times \text{hours/day} \times \text{days/year} \times \text{years}
$$

where $A_{\text{alloc}}$ is the hall area allocated to the knitting cell (machine footprint + access + yarn storage + maintenance space + internal logistics), and $Q_{\text{lifetime}}$ is the total knitted output produced during the reference service life under the chosen operating regime.

**Technology rationale.**
Seamless knitting (body-size knitting on large-diameter circular machines) produces complete garment tubes in a single operation, eliminating cut-and-sew waste. Its throughput per unit of floor space is intermediate between circular fabric knitting and flat or 3D knitting, as the larger machine envelope and more complex programming cycles reduce the production rate per m^2 relative to conventional circular knitting.

**Practical implementation.**
In the seamless knitting foreground unit process, we add an input: *building, hall* (unit = m^2) with amount = 1.61E-05 m^2/kg.

**End-of-life of the building.**
The building dataset includes construction, maintenance and decommissioning within the background system model. No separate building EoL module is created in the foreground; only the amortised m^2/kg input is provided.

**Default value (this study).** In the absence of site-specific $A_{\text{alloc}}$ and $Q_{\text{lifetime}}$, the following reference intensity is applied, shared with the hosiery technology group given comparable machine scale and operating throughput:

> Seamless knitting (garment): **1.61E-05 m^2/kg**

Physical plausibility was cross-checked using machine envelope data from Santoni SM8-TR1S (A = 2700 mm, D = 3150 mm, envelope approximately 8.5 m^2) with a cell factor of 3--4x. This value also aligns directly with the benchmark reported in the openLCA Nexus organic cotton sweater case study.

## 4. Waste and Material Efficiency

Traditional cut-and-sew processes typically lose **10--25%** of fabric as trims (AATCC / GIZ 2023).

Seamless knitting eliminates most cutting operations and achieves **> 95% material utilisation**, corresponding to **< 5% total waste** (K&G Garment 2025).

Accordingly, waste-to-treatment in the LCI is set at **0.025 kg textile waste per kg garment**.

---

## 5. Summary of Inventory Parameters (Average Case)

| Flow | Amount | Unit | Comment |
|---|---|---|---|
| Product | 1 | kg | Average seamless knitted garment |
| Yarn losses | 0.025 | kg | Average 2.5% material loss |
| Lubricant | 0.008 | kg | Upper-bound for high-load production |
| Electricity mix | 1.5 | kWh | Direct machine operation |
| Indirect energy | 4.46 | kWh | Compressors, HVAC, lighting, auxiliaries |
| Capital goods | 0.0004 | kg | Machine allocation (average) |
| EoL steel | 0.0003 | kg | Machine end-of-life |
| EoL others | 0.0001 | kg | Machine end-of-life |
| Textile waste | 0.025 | kg | Process and start-up losses |
