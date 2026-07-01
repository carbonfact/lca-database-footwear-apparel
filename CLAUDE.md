# Repository guide for Claude

This is a public, open-data LCA database for footwear & apparel (impact scores +
methodology; full inventories are intentionally not published).

## Releasing
When cutting a new release or bumping the version, **follow [`RELEASING.md`](RELEASING.md)**.
Key point: the Zenodo DOI is a stable concept DOI and auto-refreshes on each
GitHub Release; only the static version/date strings (in `CITATION.cff`,
`README.md`, `CHANGELOG.md`) need bumping.

## Citation
`CITATION.cff` is the source of truth. If you change authors, title, version, or
DOI, keep these in sync: the README BibTeX block, the README plain-text
citation, and `.zenodo.json`. Author order is deliberate (senior author last) —
do not re-alphabetize.

## Contributing changes
- `main` is protected: land changes via a **pull request**, never push to `main`.
- Admin-merge is acceptable for additive/tooling/docs/citation changes. For PRs
  that change **published data values** (the `impact-scores.csv` files), get a
  human review first — do not admin-merge those.
- Do **not** add "Co-Authored-By" or "Generated with Claude Code" to commits or
  PRs (also enforced via `.claude/settings.json`).

## Sensitive-data hygiene
Do not commit ecoinvent-derived inventories (Brightway/Activity Browser `.xlsx`,
UPR exports) or contribution-analysis CSVs/PDFs. Only impact scores, foreground
parameters, and methodology docs are publishable.
