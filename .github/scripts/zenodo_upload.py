#!/usr/bin/env python3
"""Deposit a release archive on Zenodo via the REST API.

No GitHub access is granted to Zenodo: authentication is a personal Zenodo API
token, passed as the ZENODO_TOKEN environment variable (a GitHub Actions secret).

Behaviour:
  - First run (no ZENODO_CONCEPT_RECID): creates a brand-new deposition,
    uploads the archive, sets metadata from .zenodo.json, and publishes.
    Prints the concept record id to store as the ZENODO_CONCEPT_RECID variable.
  - Later runs (ZENODO_CONCEPT_RECID set): creates a NEW VERSION of that
    concept (keeping the stable concept DOI), replaces the files, bumps the
    version, and publishes.

Required env: ZENODO_TOKEN, ARCHIVE (path), VERSION (e.g. 1.1.0)
Optional env: ZENODO_CONCEPT_RECID, ZENODO_METADATA (path, default .zenodo.json),
              ZENODO_BASE (default https://zenodo.org/api; use the sandbox to test)
"""
import json
import os
import sys
import urllib.error
import urllib.request

TOKEN = os.environ.get("ZENODO_TOKEN", "").strip()
CONCEPT = os.environ.get("ZENODO_CONCEPT_RECID", "").strip()
ARCHIVE = os.environ["ARCHIVE"]
VERSION = os.environ["VERSION"]
METADATA_FILE = os.environ.get("ZENODO_METADATA", ".zenodo.json")
BASE = os.environ.get("ZENODO_BASE", "https://zenodo.org/api").rstrip("/")

if not TOKEN:
    print("ZENODO_TOKEN not set — skipping Zenodo deposit (nothing to do).")
    sys.exit(0)


def api(method, url, payload=None, raw_body=None, expect_json=True):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    data = None
    if raw_body is not None:
        data = raw_body
        headers["Content-Type"] = "application/octet-stream"
    elif payload is not None:
        data = json.dumps(payload).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read()
            return json.loads(body) if (expect_json and body) else body
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        print(f"HTTP {e.code} on {method} {url}\n{detail}", file=sys.stderr)
        raise


def load_metadata():
    with open(METADATA_FILE, encoding="utf-8") as fh:
        md = json.load(fh)
    md["version"] = VERSION  # always reflect the release tag
    return md


def upload_file(bucket_url):
    fname = os.path.basename(ARCHIVE)
    with open(ARCHIVE, "rb") as fh:
        data = fh.read()
    print(f"Uploading {fname} ({len(data)} bytes) -> {bucket_url}")
    api("PUT", f"{bucket_url}/{fname}", raw_body=data)


def find_latest_deposition(concept):
    url = (f"{BASE}/deposit/depositions?q=conceptrecid:{concept}"
           f"&all_versions=true&size=25&sort=mostrecent")
    deps = api("GET", url)
    published = [d for d in deps if d.get("submitted")]
    if not published:
        raise SystemExit(
            f"No published deposition found for concept {concept}. "
            "Check ZENODO_CONCEPT_RECID.")
    return max(published, key=lambda d: d["id"])


def publish_and_report(dep_id):
    rec = api("POST", f"{BASE}/deposit/depositions/{dep_id}/actions/publish")
    doi = rec.get("doi") or rec.get("metadata", {}).get("doi")
    concept_recid = rec.get("conceptrecid")
    concept_doi = rec.get("conceptdoi")
    print("\n=== Published on Zenodo ===")
    print(f"Version DOI : {doi}")
    print(f"Concept DOI : {concept_doi}   (use this for the README badge)")
    print(f"Concept recid: {concept_recid}")
    if not CONCEPT:
        print("\n>>> First deposit. Store this as a repo VARIABLE named "
              f"ZENODO_CONCEPT_RECID = {concept_recid}")
    # Expose to later workflow steps if running in GitHub Actions.
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"version_doi={doi}\n")
            fh.write(f"concept_doi={concept_doi}\n")
            fh.write(f"concept_recid={concept_recid}\n")


def bootstrap():
    print("No concept id set — creating a new Zenodo record.")
    dep = api("POST", f"{BASE}/deposit/depositions", payload={})
    upload_file(dep["links"]["bucket"])
    api("PUT", f"{BASE}/deposit/depositions/{dep['id']}",
        payload={"metadata": load_metadata()})
    publish_and_report(dep["id"])


def new_version():
    print(f"Creating a new version under concept {CONCEPT}.")
    latest = find_latest_deposition(CONCEPT)
    resp = api("POST",
               f"{BASE}/deposit/depositions/{latest['id']}/actions/newversion")
    draft_url = resp["links"].get("latest_draft") or resp["links"]["newversion"]
    draft = api("GET", draft_url)
    # A new version inherits the previous files; remove them before uploading.
    for f in draft.get("files", []):
        api("DELETE",
            f"{BASE}/deposit/depositions/{draft['id']}/files/{f['id']}",
            expect_json=False)
    upload_file(draft["links"]["bucket"])
    api("PUT", f"{BASE}/deposit/depositions/{draft['id']}",
        payload={"metadata": load_metadata()})
    publish_and_report(draft["id"])


if __name__ == "__main__":
    if CONCEPT:
        new_version()
    else:
        bootstrap()
