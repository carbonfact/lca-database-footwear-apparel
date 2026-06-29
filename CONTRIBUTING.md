# Contributing to the Open Source LCA Database for Footwear & Apparel

Thank you for your interest in improving textile LCA data. This database is in **soft release**: we're actively collecting feedback from the community, and every form of contribution — from typo fixes to full dataset submissions to sharing primary supplier data — is valuable.

Here's how you can contribute.

## Reporting data errors

If you find an error in the data (wrong values, incorrect units, missing datasets), please [open an issue](https://github.com/carbonfact/lca-database-footwear-apparel/issues/new?template=data-error.md) with:

- The affected file and dataset name
- What you believe is incorrect
- A reference or source supporting the correction

## Requesting new datasets

Want to see a process or material added? [Open a dataset request](https://github.com/carbonfact/lca-database-footwear-apparel/issues/new?template=dataset-request.md) describing:

- The process or material
- Why it matters (e.g., industry relevance, gap in current coverage)
- Any references or data sources you can point to

### You know a good non-LCA source but haven't modelled it?

If you don't have an LCI but know of a solid technical reference — an industry benchmark, an academic paper, a supplier disclosure, a regulatory filing — for a process we don't yet cover, get in touch at **science@carbonfact.com**. If the source looks strong enough to build a transparent inventory on, we can talk about modelling it together and contributing the result back to this database.

## Proposing methodology improvements

For discussions about methodology choices, modeling approaches, or data quality, please use [GitHub Discussions](https://github.com/carbonfact/lca-database-footwear-apparel/discussions). This is the right place for open-ended questions and community dialogue.

## Contributing data

If you'd like to contribute datasets:

1. Fork the repository
2. Add your data following the existing structure (see any process folder for the template)
3. Include methodology documentation
4. Open a pull request with a description of the data and its sources

All contributions must be compatible with the [CC BY-SA 4.0](LICENSE) license.

## Suppliers: sharing primary process data

Most of the current datasets are built on **secondary data** (literature, industry benchmarks, public disclosures). Our long-term vision is to progressively replace and complement these with **primary data from manufacturers** so that the published emission factors better reflect real production.

If you're a supplier or manufacturer willing to share data for one of the processes already in the database (or a new one), here's what we offer:

- **LCA of your process in return**: we'll run a full LCA of your specific setup using your primary data and share the results with you.
- **Anonymity preserved**: your raw data is never published. What gets released back into this open database is an averaged dataset combining your data with at least a few other suppliers, so individual contributors cannot be re-identified.
- **Typical data we need**: electricity and thermal energy consumption per kg/unit of output, chemical/dye/auxiliary inputs (with MSDS where possible), water intake and wastewater volumes, waste rates, and any measured emissions.

To discuss data sharing, contact us at **science@carbonfact.com**. We'll walk you through the data template and what anonymisation looks like in practice.

## Data quality standards

Contributed datasets should:

- Cover at least 16 EF 3.1 impact indicators
- Include Data Quality Rating (DQR) scores
- Be accompanied by methodology documentation
- Reference primary literature or data sources
