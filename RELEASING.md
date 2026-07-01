# Releasing

How to publish a new version. Most of the work is automated — you bump a few
version strings, then cut a GitHub Release, and the rest happens on its own.

## What is automatic
- Cutting a **GitHub Release** triggers `.github/workflows/zenodo-release.yml`,
  which archives the tagged snapshot on **Zenodo** as a **new version under the
  same concept DOI** (`10.5281/zenodo.21102755`).
- The concept DOI always resolves to the latest release, so the DOI badge, the
  `doi:` in `CITATION.cff`, and the BibTeX `doi` never need changing.
- Title, authors (and their order), license, and keywords come from
  `.zenodo.json` — only touch it if those actually change.
- The Zenodo record's version number is taken from the git tag.

## What you must bump for each release (static text)
These do **not** update themselves. For version `X.Y.Z`:
1. `CITATION.cff` → `version:` and `date-released:`
2. `README.md` → the version **badge**, the BibTeX `version` / `year`, and the
   plain-text citation `(Version X.Y.Z)` / `(YEAR)`
3. `CHANGELOG.md` → add the new version section

## Steps
1. Make the bumps above on a branch and open a PR (main is protected).
2. Merge to `main`.
3. Create a **GitHub Release**: tag **`vX.Y.Z`** (no stray dot — `v1.2.0`, not
   `v.1.2.0`), target `main`, publish.
4. Check the **Actions** run ("Archive release on Zenodo") is green, and that
   the Zenodo record shows the new version.

## One-time setup (already done, for reference)
- Repo **secret** `ZENODO_TOKEN` — a Zenodo personal token (`deposit:write`,
  `deposit:actions`). No GitHub access is granted to Zenodo.
- Repo **variable** `ZENODO_CONCEPT_RECID` = `21102755` — makes each release a
  new version of the same concept DOI.
