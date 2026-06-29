# Changelog

All notable changes to the Open Source LCA Database for Footwear & Apparel will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Sneaker Shoe Assembly, GLO electricity scenario: updated impact scores to use a more carbon-intensive global market mix (`market group for electricity, medium voltage, GLO` in ecoinvent 3.12). GHG total moves from 1.014 → 1.905 kg CO₂-eq/pair (+88%); switching VN→GLO now **increases** GWP by +14% (previously −39%). VN values unchanged.

### Removed

- Brightway/Activity Browser inventory files (`inventory-brightway.xlsx`) across all processes, withdrawn while the terms for sharing the full inventories openly are finalised with our partners. Impact scores remain openly available, and the key foreground parameters remain described in each process's methodology.
- Per-dataset `ghg-contributions.csv` files (per-exchange contribution breakdowns) across all processes, withdrawn alongside the full inventories while sharing terms are finalised with our partners. Aggregated impact scores remain openly available.
- Markdown versions of the shared `capital-goods` and `building-infrastructure` methodology documents (duplicated the canonical PDFs).

## [1.1.0] - 2026-04-15

### Added

- Natural Rubber (STR Production): 4 datasets (TH, ID, CI, VN)
  - Cradle-to-gate with country-specific LUC and peatland drainage emissions
  - Economic allocation for plantation co-products (17.8% to field coagulum)
- Women's Boots Assembly: 3 datasets (CN, GLO, IT electricity scenarios)
  - PU/Microfiber Upper + TPR/EVA/Rubber Outsole
  - 3 sub-processes: cutting, stitching, lasting (aggregated loss rate: 1.049)
- Sneaker Shoe Assembly: 2 datasets (VN and GLO electricity scenarios)
- Synthetic PU Leather: 2 datasets (DMF-free water-borne, DMF-based solvent-based)
  - Impact scores for 16 EF 3.1 indicators
  - Per-exchange GHG contribution analysis
  - Methodology documentation

### Changed

- Restructured footwear assembly into `datasets/shoe-assembly/` with `sneaker/` and `womens-boots/` subfolders (previously `datasets/sneaker-shoe-assembly/`)

## [1.0.0] - 2026-04-08

### Added

- Initial release of the Open Source LCA Database for Footwear & Apparel
- 230 datasets across 4 textile processes:
  - Spinning: 159 datasets (Ring spun, Melt spinning, Open end rotor)
  - Knitting: 13 datasets (Flat, Circular, Seamless, Hosiery, 3D)
  - Weaving: 16 datasets (Air jet, Rapier, Water jet, Projectile)
  - Dyeing: 38 datasets (Exhaust, Continuous, Semi-continuous)
- Emission factors (LCIA results) for 16 EF 3.1 impact indicators per dataset
- GHG contribution analysis with per-exchange breakdown
- Data Quality Rating (DQR) scores following PEF methodology
- Methodology documentation for all processes
