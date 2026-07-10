# The Carbonfact Open Source LCA Database for Footwear & Apparel

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Version](https://img.shields.io/badge/version-v1.1.0-blue.svg)](CHANGELOG.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21102755.svg)](https://doi.org/10.5281/zenodo.21102755)

**Carbonfact's open-source reference database for textile lifecycle assessment.**

> **Early version.** This is an early release that will continue to evolve, so please check the [changelog](CHANGELOG.md) before re-using results across releases. Several datasets (notably dyeing and wet processing) rely on the [Apparel Impact Institute (Aii) Facility Benchmark](https://apparelimpact.org/) as a key industry data source. In early June, Aii published version 1.1 of its Energy and Carbon Benchmark, which updates the dry-process values; we will integrate it over the coming weeks, and it will affect a number of impact scores.
>
> If you spot something worth improving or have data to contribute, see the [Contributing](#contributing) section below. We'd love to hear from you.

## What is this?

The Carbonfact Open Source LCA Database for Footwear & Apparel is a free, open-source collection of lifecycle assessment (LCA) datasets for core textile manufacturing processes, with impact scores calculated using EF 3.1 characterization factors across 16 PEF (Product Environmental Footprint) impact indicators.

**Looking for emission factors and impact scores?** Jump to the [process table](#whats-included) and click any process to open its `impact-scores.csv`, readable right in your browser. The columns use indicator codes (ACD, GHG, etc.) — see the [Impact indicators](#impact-indicators) table for what each one means. See [Getting the emission factors and impact scores](#getting-the-emission-factors-and-impact-scores) for the steps.

## Methodological alignment

These datasets are designed to align with established textile LCA practice rather than stand apart from it. In building them we have reviewed, harmonized and ingested a large share of the current textile LCA literature, and benchmarked each dataset against existing references to keep results consistent with the field.

Our ambition is for these datasets to become a **shared industry reference**: openly available, adopted across the sector, and improved over time through community contribution. We welcome contributions from across the industry, so see the [Contributing](#contributing) section to get involved. All results are calculated with EF 3.1 characterization factors across the 16 PEF impact indicators.

## What's included

The database is organised by **process**. Click any process below to open its folder, where you'll find the `impact-scores.csv` results file (emission factors + data quality scores) and the methodology documentation for that family.

| Process | Datasets | Technologies | Functional Unit |
|---------|----------|-------------|-----------------|
| [Spinning](datasets/spinning/) | 159 | Ring spun, Melt spinning, Open end rotor | 1 kg yarn |
| [Knitting](datasets/knitting/) | 13 | Flat, Circular, Seamless, Hosiery, 3D | 1 kg fabric |
| [Weaving](datasets/weaving/) | 19 | Air jet, Rapier, Water jet, Projectile | 1 kg fabric |
| [Dyeing](datasets/dyeing/) | 38 | Exhaust, Continuous, Pad steam, Thermosol | 1 kg dyed textile |
| [Shoe Assembly](datasets/shoe-assembly/) | 5 | Sneaker (VN, GLO), Women's Boots (CN, GLO, IT) | 1 pair / 1 kg |
| [Synthetic PU Leather](datasets/synthetic-pu-leather/) | 2 | DMF-free (water-borne), DMF-based (solvent-based) | 1 m² PU leather |
| [Natural Rubber](datasets/natural-rubber/) | 4 | STR production (TH, ID, CI, VN) | 1 kg STR |
| [Use Phase](datasets/use-phase/) | 15 | Dry cleaning, Hand washing, Machine washing (30/40/60°), Tumble drying, Ironing, Detergents | 1 kg textile / 1 min / 1 kg detergent |
| [Printing](datasets/printing/) | 16 | Rotary screen, Digital inkjet, Flat screen, Transfer, Batch garment | 1 kg printed fabric/garment |
| [Finishing](datasets/finishing/) | 18 | Pre-treatment, Mechanical, Thermal, Chemical | 1 kg finished fabric |
| [Textile Assembly](datasets/textile-assembly/) | 15 | Generic assembly per product archetype (apparel, accessories, home textiles) | 1 kg assembled product |
| **Total** | **304** | | |

### Getting the emission factors and impact scores

No special tools needed. You can read the numbers straight from your browser:

1. **Pick a process** from the table above and click it to open its folder.
2. **Open `impact-scores.csv`**: GitHub previews it right in your browser: emission factors and data quality scores, no download required.
3. **Download** with the *Download raw file* button to open it in Excel or Google Sheets and work with the numbers.

Prefer everything at once? Use the green **Code → Download ZIP** button at the top of the repository to grab all processes in one go.

**Upcoming**

- [x] ~~Printing~~
- [x] ~~Fabric Finishing~~
- [ ] Nonwoven Fabric Formation
- [ ] Viscose
- [x] ~~Apparel Assembly~~
- [ ] Dyeing and Printing Chemicals
- [x] ~~Synthetic PU Leather (DMF-free & DMF-based)~~
- [ ] Bovine Leather
- [x] ~~Natural Rubber (STR Production)~~
- [x] ~~Footwear Assembly~~
- [x] ~~Use Phase (Laundry)~~

> Beyond new datasets, see [ROADMAP.md](ROADMAP.md) for planned improvements to data formats, methodology, and external verification.

## Data files

Each process directory contains its results file:

| File | Description |
|------|-------------|
| `impact-scores.csv` | Emission factors (LCIA results) across all 16 EF 3.1 impact indicators, plus Data Quality Rating (DQR) scores for each dataset. Where available, includes an **Input required (kg)** column, the kg of input material needed to produce 1 kg of output (e.g. 1.18 means 1.18 kg of input per 1 kg of output). See [Handling material losses](#handling-material-losses) for how to apply it. This is the primary results file. |

> **Full inventories.** The detailed Brightway/Activity Browser inventory files are not currently published in this repository. The impact scores above remain openly available, and the key foreground parameters are described in each process's methodology documentation.

### Handling material losses

Yarn and other material losses are **not modelled inside the process datasets**. The process inventories contain no waste-yarn or waste-material exchanges. They are meant to be applied externally by the caller using the **Input required (kg)** value (this is the column name in the CSV files; it is sometimes referred to as the *Input-Output Ratio*, or IOR, in methodology docs).

To correctly account for material losses, the caller must:

1. **Scale the upstream material input** by the process-specific Input required (kg), so the material-production burden reflects the actual loss rate. For example, 1 kg of knitted fabric at `Input required (kg) = 1.05` means modelling 1.05 kg of upstream yarn production.
2. **Add a material waste flow** for the lost material (e.g. textile waste to recycling, landfill, or incineration) to account for the end-of-life treatment of the fraction that did not end up in the product.

Auxiliary and chemical waste flows (oils, cleaning agents, wastewater treatment, etc.) are already embedded in the process emission factors and do **not** need to be added separately.

## Impact indicators

All datasets report results for the 16 EF 3.1 impact indicators:

| Code | Indicator | Unit |
|------|-----------|------|
| ACD | Acidification | molH+e/kg |
| ETF | Ecotoxicity, freshwater | CTUe/kg |
| FRU | Fossil resource use | MJ/kg |
| FWE | Eutrophication, freshwater | kgPe/kg |
| GHG | Climate change | kgCO2eq/kg |
| HTC | Human toxicity, cancer | CTUhtc/kg |
| HTN | Human toxicity, non-cancer | CTUhtn/kg |
| IOR | Ionising radiation | kBqU235e/kg |
| LDU | Land use | Pt/kg |
| MRU | Mineral resource use | kgSbe/kg |
| OZD | Ozone depletion | kgCFC11e/kg |
| PCO | Photochemical ozone formation | kgNMVOCe/kg |
| PMA | Particulate matter | dis.inc./kg |
| SWE | Eutrophication, marine | kgNe/kg |
| TRE | Eutrophication, terrestrial | molNe/kg |
| WTU | Water use | m3Weq/kg |

## Methodology

For a general introduction to the LCA approach, see the [methodology overview](methodology/overview.md). Each process directory contains detailed methodology documentation covering system boundaries, data sources, allocation rules, and modeling choices:

- [Spinning methodology](datasets/spinning/methodology/)
- [Knitting methodology](datasets/knitting/methodology/)
- [Weaving methodology](datasets/weaving/methodology/)
- [Dyeing methodology](datasets/dyeing/methodology/)
- [Printing methodology](datasets/printing/methodology/)
- [Finishing methodology](datasets/finishing/methodology/)
- [Textile Assembly methodology](datasets/textile-assembly/methodology/)
- [Shoe Assembly methodology](datasets/shoe-assembly/) (Sneaker + Women's Boots)
- [Synthetic PU Leather methodology](datasets/synthetic-pu-leather/methodology/)
- [Natural Rubber methodology](datasets/natural-rubber/methodology/)
- [Use Phase methodology](datasets/use-phase/methodology/)

Cross-cutting methodology docs (applicable to all processes):

- [Impact indicators](methodology/impact-indicators.md): Full table of 16 EF 3.1 indicators
- [Data Quality Rating framework](methodology/dqr-framework.md): PEF DQR scoring methodology
- [Capital goods (PDF)](methodology/capital-goods.pdf): Machine amortization approach
- [Building infrastructure (PDF)](methodology/building-infrastructure.pdf): Building allocation approach
- [Indirect energy (PDF)](methodology/indirect-energy.pdf): HVAC, compressors, lighting and auxiliaries allocation

## Background database & pre-calculated scores

If you want to **use the emission factors or pre-calculated impact scores**, these are shared openly in this repository. The `impact-scores.csv` file in each process directory gives you ready-to-use results.

The lifecycle inventories behind these results are built on top of **ecoinvent 3.12** as the background database. The full inventory files are not currently distributed in this repository. Running the full inventories in LCA software (e.g. Brightway, Activity Browser, SimaPro, openLCA) requires a valid [ecoinvent license](https://ecoinvent.org/offerings/).

## Versioning & changelog

This project follows [Semantic Versioning](https://semver.org/). Major versions indicate breaking schema changes, minor versions add new datasets or processes, and patch versions fix data errors.

See [CHANGELOG.md](CHANGELOG.md) for a full history of changes.

## Contributing

We welcome contributions from the LCA and textile communities. See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines; in short, here's what we're actively looking for:

- **Report data errors or methodology issues**: open an [issue](https://github.com/carbonfact/lca-database-footwear-apparel/issues) or start a [discussion](https://github.com/carbonfact/lca-database-footwear-apparel/discussions).
- **Submit a new dataset**: if you've modelled a process that fits the scope (textile manufacturing or use phase), open a PR following the structure of an existing process folder.
- **Point us at a good non-LCA source**: if you don't have an LCI but know of a solid technical reference (industry benchmark, academic paper, supplier disclosure) for a process we don't yet cover, get in touch and we can talk about modelling it together.
- **Suppliers: share primary data.** Most of the current datasets are built on secondary data. Our vision is to progressively collect primary data from manufacturers to improve quality. If you're a supplier willing to share process data for one of the existing processes, we'll run an LCA of your process in return. Your data can remain anonymous and be averaged with other suppliers' data so the published dataset stays fully anonymised.

For supplier data-sharing or any other partnership questions, contact us at science@carbonfact.com.

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](LICENSE).

### What you can do

- **Use** the data for any purpose, including commercial use. No permission needed.
- **Share**: copy and redistribute the data in any medium or format.
- **Adapt**: remix, transform, modify, or build upon the datasets (e.g. improve an inventory, add new exchanges, recalculate with updated characterization factors).

### What you must do

- **Give credit**: You must include the following attribution when sharing or using the data:

  > Data source: [The Carbonfact Open Source LCA Database for Footwear & Apparel](https://github.com/carbonfact/lca-database-footwear-apparel), CC BY-SA 4.0

  We strongly encourage displaying this attribution on the same page or screen where emission factors or impact scores derived from this database are shown, rather than burying it in a bibliography or appendix.

- **ShareAlike**: if you modify or improve the datasets and distribute your version, you must release it under the same CC BY-SA 4.0 license (or a compatible one). This ensures improvements stay open for the community.

### What you cannot do

- **Add restrictions**: you may not apply legal terms or technological measures that restrict others from doing anything the license permits.

### If you integrate this database into a product or platform

If you build the database into a software product, platform, or service that displays emission factors or impact scores to your users, you must:

- **Display the attribution on the same page or screen** where values derived from this database are shown — not only in documentation or settings.
- **Retain the license and attribution notice** in any data you deliver to your customers, so they know the terms that apply.
- **Inform your customers** that if they republish these values (for example in a sustainability report or public disclosure), the same attribution requirement applies to them. Citing the database DOI (see [Citation](#citation)) is the expected form.
- **Indicate modifications** if you have adapted or recalculated the values, so your version is not mistaken for ours.

We'd also love to know how the database is being used — telling us is entirely optional and not a condition of the license. Reach us at science@carbonfact.com.

### Commercial licensing

For companies that need different attribution terms or cannot comply with the ShareAlike requirement, a separate commercial license is available. Contact us at science@carbonfact.com.

## Citation

If you use this database in your work, please cite it via its DOI:

**DOI: [10.5281/zenodo.21102755](https://doi.org/10.5281/zenodo.21102755)** — this concept DOI always resolves to the latest release; each release also has its own version DOI on Zenodo.

Suggested citation:

> *The Carbonfact Open Source LCA Database for Footwear & Apparel* (Version 1.1.0) [Data set]. Carrières, V., Vieira, G., & Vandepaer, L. (2026). Zenodo. https://doi.org/10.5281/zenodo.21102755

Or in BibTeX:

```bibtex
@dataset{carbonfact_lca_footwear_apparel_2026,
  title     = {The Carbonfact Open Source LCA Database for Footwear \& Apparel},
  author    = {Carrières, Vincent and Vieira, Gustavo and Vandepaer, Laurent},
  year      = {2026},
  version   = {1.1.0},
  doi       = {10.5281/zenodo.21102755},
  url       = {https://github.com/carbonfact/lca-database-footwear-apparel},
  license   = {CC-BY-SA-4.0}
}
```

GitHub's **"Cite this repository"** button (top right of the repo page) also generates ready-to-use APA and BibTeX automatically from [`CITATION.cff`](CITATION.cff).

## Quick start (Python)

```python
import pandas as pd

knitting = pd.read_csv("datasets/knitting/impact-scores.csv")
print(knitting[["Activity", "GHG"]].to_string(index=False))
```

