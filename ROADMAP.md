# Roadmap

This document tracks planned improvements to the Carbonfact Open Source LCA Database for Footwear & Apparel beyond new datasets. The list of upcoming process datasets lives in the [README](README.md#whats-included). Items below are grouped by theme, not prioritized. See [CHANGELOG.md](CHANGELOG.md) for what has already shipped.

If you'd like to help with any of these, or think something is missing, open an [issue](https://github.com/carbonfact/lca-database-footwear-apparel/issues) or [discussion](https://github.com/carbonfact/lca-database-footwear-apparel/discussions).

## Data formats & exports

- [ ] **EcoSpold 1 export**: provide the full inventories in EcoSpold 1 format, for compatibility with SimaPro and other tools.
- [ ] **Consolidated workbook**: a single Excel file bundling every dataset's impact scores, DQR breakdown, and key energy inputs (electricity, heat) across all processes, so users can compare processes without stitching CSVs together.

## Impact scores file

- [ ] **Energy input columns**: add electricity (kWh) and heat (MJ) per functional unit directly in each process's `impact-scores.csv`, so these key inventory values are visible directly in the results file.
- [ ] **GHG sub-category breakdown**: split the climate change (GHG) result into fossil, biogenic, and land use change sub-totals, so users can see the composition of each dataset's carbon footprint rather than only the aggregated kgCO2eq value.

## Methodology

- [ ] **DQR refresh**: re-compute Data Quality Ratings across datasets using the current framework, and document any scoring changes in the changelog.

## External verification

- [ ] **Independent critical review**: submit selected process datasets and the cross-cutting methodology to an independent ISO 14040/14044-aligned critical review, and publish the reviewer's statement alongside the affected datasets.
- [x] **Community feedback channel**: [GitHub Discussions](https://github.com/carbonfact/lca-database-footwear-apparel/discussions) is open continuously for LCA practitioners to comment on assumptions, proxies, impact-category coverage, or anything else. No fixed review windows at this stage; feedback is welcome at any time.

## Aii benchmark refresh

- [ ] Refresh dyeing and wet-processing datasets that rely on the [Apparel Impact Institute Facility Benchmark](https://apparelimpact.org/) as new Aii releases become available.
