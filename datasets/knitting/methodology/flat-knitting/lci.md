# Life Cycle Inventory

> Part of [Flat Knitting Methodology](README.md)

## 3. Process Inventory -- Flat Knitting

### 3.1 Average Case -- Flat Knitting (mix)

**Functional unit: 1 kg knitted fabric**

| Category | Flow | Amount | Unit | Comment |
|---|---|---|---|---|
| **Technosphere flows** | Dtex Yarn, "e.g. Cotton" (yarn losses) | 0.03 | kg | Yarn losses 3%. Typical range 1--5% (Laursen 2007; Sandin 2019). |
| | Lubricant, average | 0.005 | kg | Typical oil consumption per kg (Idemat 2012; Hasanbeigi & Price 2015). |
| | Air emissions from lubricant | 0.005 | kg | Mass-based approximation. |
| **Electricity / heat** | Electricity mix | 1.2 | kWh | EcoBalyse mid-range (1.2--2.4 kWh/kg). |
| | Indirect Energy (Compressors, HVAC, Illumination, etc.) | 4.46 | kWh | |
| **Capital goods** | Capital good (Building Machine) | 0.0013 | kg/kg fabric | Mass of machine allocated per kg of fabric (see section 3.4). |
| **Waste to treatment** | EoL Machine (Steel) | 0.0011 | kg | Steel fraction amortised per kg. |
| | Recycling others (Other Materials) | 0.0002 | kg | Remaining materials amortised per kg. |
| | Textile waste to incineration (no credits) | 0.03 | kg | Consistent with EcoBalyse (3--5.5%). |

---

### 3.2 Worst Case -- Flat Knitting (mix)

| Category | Flow | Amount | Unit | Comment |
|---|---|---|---|---|
| **Product** | Coarse knitted tricot | 1 | kg | |
| **Technosphere flows** | Yarn losses | 0.05 | kg | 5% losses (upper literature range). |
| | Lubricant | 0.008 | kg | Based on Sandin 2019 (p. 46). |
| | Air emissions from lubricant | 0.008 | kg | |
| **Electricity** | Electricity mix | 2.4 | kWh | Upper EcoBalyse estimate; primary data preferred when available. |
| | Indirect Energy (Compressors, HVAC, Illumination, etc.) | 4.46 | kWh | |
| **Capital goods** | Capital good (Building Machine) | 0.0013 | kg/kg fabric | Same machine allocation until better factory data. |
| **Waste** | Steel EoL | 0.0011 | kg | |
| | Other materials EoL | 0.0002 | kg | |
| | Textile waste | 0.05 | kg | 5% waste. |

---

### 3.3 Best Case -- Flat Knitting (mix)

| Category | Flow | Amount | Unit | Comment |
|---|---|---|---|---|
| **Product** | Coarse knitted tricot | 1 | kg | |
| **Technosphere flows** | Yarn losses | 0.015 | kg | 1.5% losses (lower end of literature). |
| | Lubricant | 0.005 | kg | Standard default when primary data unavailable (Idemat 2012). |
| | Air emissions from lubricant | 0.005 | kg | |
| **Electricity** | Electricity mix | 1.16 | kWh | van der Velden et al. 2013 (efficient case). |
| | Indirect Energy (Compressors, HVAC, Illumination, etc.) | 4.46 | kWh | |
| **Capital goods** | Capital good (Building Machine) | 0.0013 | kg/kg fabric | |
| **Waste** | Steel EoL | 0.0011 | kg | |
| | Other materials EoL | 0.0002 | kg | |
| | Textile waste | 0.015 | kg | Consistent with 1.5% yarn losses. |

### 3.4 Capital Goods (Machine) -- Simple Explanation

#### 3.4.1 What we are doing

We allocate a very small fraction of the machine's mass to each kilogram of fabric.
This is consistent with EF rules and ecoinvent practice.

#### 3.4.2 How it works

1. Take the **machine mass** (e.g., 1000 kg).
2. Estimate total lifetime fabric output (years x hours/day x days/year x kg/h).
3. Divide machine mass by lifetime output:

The formula for amortising the machine mass per kg of fabric is:

$$
\text{kg machine per kg fabric} = \frac{M_{\text{machine}}}{Q_{\text{lifetime}}}
$$

Where:

- **M_machine** = Total mass of the machine (kg)
- **Q_lifetime** = Total lifetime production output (kg fabric)

The lifetime output is calculated as:

$$
Q_{\text{lifetime}} = \text{Years} \times \frac{\text{Hours}}{\text{Day}} \times \frac{\text{Days}}{\text{Year}} \times \frac{\text{kg fabric}}{\text{Hour}}
$$

For the average scenario:

- 15 years
- 16 hours/day
- 300 days/year
- **2.5 kg/h productivity** (verified: Sino Finetex industry benchmark for computerised flat knitting: 10--20 kg/day; Changhua Knitting Machine: 30 min--8 h per sweater at 300--500 g each, mid-range ~2.5 kg/h. Sources: sinofinetex.com; changhua-knitting-machine.com)
- **Machine mass: 1000 kg** (verified: Fengfan double-carriage computerised flat knitting machine, 2500x850x1900 mm, net weight ~1000 kg. Source: indiamart.com listing; Fibre2Fashion supplier: 2000x840x1870 mm, 1000 kg)

This yields:

> **0.0056 kg machine / kg fabric**
>
> Calculation: 1000 kg / (15 yr x 16 h/d x 300 d/yr x 2.5 kg/h) = 1000 / 180,000 = **0.0056 kg/kg**
>
> **Source:** Machine dimensions (2700 mm x 909 mm) confirmed from KARL MAYER STOLL CMS 503 ki L official brochure (stoll.com [PDF](https://www.stoll.com/ecomaXL/files/20-04-29-503kiL_EN.pdf)). Machine mass (1000 kg) based on verified OEM datasheets for comparable computerised flat knitting machines (Fengfan double-carriage, Fibre2Fashion listings) -- STOLL does not publish machine weight in public brochures. Productivity (2.5 kg/h) consistent with industry benchmarks for computerised flat knitting (Sino Finetex 2025; Changhua Knitting Machine). Operational parameters (15 years, 16 h/day, 300 days/year) are mid-range engineering defaults bracketed by WCS/BCS scenarios; consistent with Hasanbeigi (2010) and IPPC BREF (2003). Replace with primary factory data when available.

#### 3.4.3 End-of-life of the machine

Machine material split:

- **85% steel** --> 850 kg
- **15% other materials** --> 150 kg

Amortised as (/ 180,000 kg lifetime output):

- **Steel EoL = 0.0047 kg/kg fabric**
- **Other materials EoL = 0.00083 kg/kg fabric**

#### 3.4.4 How this goes into Activity Browser

The dataset **"market for building machine"** uses **unit**, not kg.

- 1 unit = one entire machine
- We convert our kg/kg figure into a *fraction of a unit*:

$$
X = \frac{0.0056}{2800} = 2 \times 10^{-6} \text{ unit per kg fabric}
$$

**In ecoinvent:**

- **Amount = 2E-06**
- **Unit = unit**
- **Product = building machine**

### 3.5 Building Infrastructure

**3.5.1 Goal and scope.**
The flat knitting process model includes an optional building infrastructure (pavilion) share as a modular and auditable input. The building is represented by an ecoinvent-style construction dataset ("building, hall") whose reference flow is m^2 of industrial hall.

**3.5.2 Allocation principle (area amortisation over lifetime output).**
Building infrastructure is attributed to 1 kg of knitted panels by amortising the allocated hall area over the lifetime production associated with the knitting cell:

$$
\text{Building intensity (m²/kg)} = \frac{Q_{\text{lifetime}} \text{ (kg)}}{A_{\text{alloc}} \text{ (m²)}}
$$

$$
Q_{\text{lifetime}} = \text{productivity (kg/h)} \times \frac{\text{hours}}{\text{day}} \times \frac{\text{days}}{\text{year}} \times \text{years}
$$

where $A_{\text{alloc}}$ is the hall area allocated to the knitting cell (machine footprint + access + yarn storage + maintenance space + internal logistics), and $Q_{\text{lifetime}}$ is the total knitted output produced during the reference service life under the chosen operating regime.

**Technology rationale.**
Flat knitting operates panel-by-panel with frequent stop-and-start cycles, garment shaping, and yarn carrier changes, resulting in markedly lower throughput per m^2 of allocated space compared to circular or seamless technologies. This lower throughput drives a higher building intensity per kg of output.

**Practical implementation.**
In the flat knitting foreground unit process, we add an input: *building, hall* (unit = m^2) with amount = 1.39E-04 m^2/kg.

**End-of-life of the building.**
The building dataset includes construction, maintenance and decommissioning within the background system model. No separate building EoL module is created in the foreground; only the amortised m^2/kg input is provided.

**Default value (this study).** In the absence of site-specific $A_{\text{alloc}}$ and $Q_{\text{lifetime}}$, the following reference intensity is applied:

> Flat knitting: **1.39E-04 m^2/kg**

This is consistent with the expectation that flat knitting has markedly lower throughput per allocated space than circular or seamless technologies. Physical plausibility was cross-checked using machine envelope data from KARL MAYER STOLL CMS 503 ki L (length 2700 mm x depth 909 mm) combined with a cell factor accounting for aisles, yarn storage and maintenance access.

---

### 3.6 Indirect Energy (HVAC, Compressors, Lighting, Cleaning)

Knitting plants (both flat and circular) rarely have sub-metered values for each subsystem (machines, compressors, HVAC, lighting, cleaning, etc.).

Because of that, and until primary factory data are collected, we use:

1. a **total indirect energy value per kg of fabric**, and
2. **literature-based percentage shares** to split this total across subsystems.

Starting from the **upper EcoBalyse value of 2.4 kWh/kg** for knitting, we extrapolated a consistent indirect energy demand for a "high-load" knitting scenario and obtained:

- **Indirect energy = 4.46 kWh/kg**

This 4.46 kWh/kg value is used as a **generic indirect energy term for both flat and circular knitting**, and can be updated as soon as better data (e.g. sub-metered values) become available.

---

#### 3.6.1 Subsystems considered

- Knitting machines
- Compressors
- HVAC (air conditioning / humidification / chillers)
- Lighting
- Cleaning & auxiliary systems

---

#### 3.6.2 Recommended mid-range distribution

Until real measurements exist, we split the **total electricity (direct + indirect)** across subsystems using mid-range shares inspired by Koc (2010), Hasanbeigi (2010), Sakti (2021), CII guidance and Celik (2025):

- **Knitting machines** --> 35%
- **Compressors** --> 25%
- **HVAC** --> 30%
- **Lighting** --> 6.5%
- **Cleaning / auxiliaries** --> 3.5%

These parameters are deliberately **editable**:

- they provide a transparent starting point for LCA modelling,
- and can be overridden easily when factory-specific sub-meter data become available.
