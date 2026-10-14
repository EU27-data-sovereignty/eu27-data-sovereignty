#!/usr/bin/env python3
"""
The edition channel: publish the split edition to Supabase Storage, verify what it serves, check the tree.

    python3 model/edition.py check   --dir mobile/assets/data --bundle web/public/data/eu27.json \
                                     [--site-manifest web/public/data/manifest.json]
    python3 model/edition.py publish --dir mobile/assets/data --bundle web/public/data/eu27.json \
                                     [--commit SHA] [--run-id ID] [--run-url URL] [--summary FILE]
    python3 model/edition.py verify  --url https://<ref>.supabase.co/storage/v1/object/public/editions \
                                     --manifest mobile/assets/data/manifest.json

Why this file exists
--------------------
The mobile reader ships the fact-checked bundle as 28 hash-pinned parts and a manifest (#110), and learns of a
newer edition from one public, read-only bucket (#111). Only the deploy workflow writes to that bucket (#112),
after the site it belongs to passed every check, and what it writes must be provable from outside: the same
manifest the gate tested, under a path named by the edition id, never overwritten. A bash loop of curl lines
cannot be unit-tested and the Supabase CLI would need its own pin and checksum, so the publisher is this
stdlib module, exercised against a fake Storage server in tests/test_edition.py and against a local Supabase
stack by mobile/test.sh --integration. model/smoke.py imports verify() to check the live channel after every
deploy and weekly.

Layout in the bucket `editions`
    <edition>/manifest.json, <edition>/eu27.core.json, <edition>/eu27.<ISO>.json   immutable (x-upsert: false)
    <edition>/published.json   {commit, run_id, run_url, published_at, manifest_sha256}   written once
    latest.json                {edition, manifest_sha256, generated, commit, published_at}   the only mutable object

The service-role key is read from SUPABASE_SERVICE_ROLE_KEY inside the process: it is never an argument, never
part of a URL, and never printed. The anon key is not needed: reading is anonymous, which is also the proof
that anonymous reading works.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUCKET = "editions"
MANIFEST = "manifest.json"
LATEST = "latest.json"
PUBLISHED = "published.json"
AGENT = "eu27-edition/1 (+https://github.com/EU27-data-sovereignty/eu27-data-sovereignty)"
IMMUTABLE = "max-age=31536000"                   # a part under its edition id never changes
POINTER = "max-age=60"                           # latest.json: an installed app sees a new edition within a minute
TIMEOUT = 60

Result = tuple[str, bool, str]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def request(url: str, method: str = "GET", headers: dict[str, str] | None = None,
            data: bytes | None = None) -> tuple[int, dict[str, str], bytes]:
    """One request; a network failure is a status of 0, not an exception, so a check can report it."""
    req = urllib.request.Request(url, method=method, data=data, headers={"User-Agent": AGENT, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, {k.lower(): v for k, v in r.headers.items()}, r.read()
    except urllib.error.HTTPError as e:
        with e:                                  # an error response is a response: read and close it
            return e.code, {k.lower(): v for k, v in e.headers.items()}, e.read()
    except (urllib.error.URLError, OSError):
        return 0, {}, b""


# --------------------------------------------------------------------------- #
# The tree: the parts and the manifest agree (mobile/test.sh `edition`)
# --------------------------------------------------------------------------- #

def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(edition_dir: Path, bundle: Path | None, site_manifest: Path | None) -> list[Result]:
    """The parts on disk are the manifest's, the manifest is the bundle's, and the site's copy is the same."""
    results: list[Result] = []
    manifest_path = edition_dir / MANIFEST
    if not manifest_path.exists():
        return [("manifest present", False, str(manifest_path))]
    manifest = load_manifest(manifest_path)
    for name, entry in sorted(manifest["parts"].items()):
        part = edition_dir / name
        if not part.exists():
            results.append((f"part {name}", False, "missing: run python3 model/export_json.py --split --from <bundle>"))
            continue
        data = part.read_bytes()
        results.append((f"part {name}", sha256(data) == entry["sha256"] and len(data) == entry["bytes"],
                        f"{len(data):,} bytes, sha256 {sha256(data)[:16]}"))
    stray = sorted(p.name for p in edition_dir.glob("eu27.*.json") if p.name not in manifest["parts"])
    results.append(("no stray part", not stray, ", ".join(stray)))
    if bundle:
        got = sha256(bundle.read_bytes())
        results.append(("edition is the bundle's sha256", got == manifest["edition"],
                        f"bundle {got[:16]}, manifest {manifest['edition'][:16]}"))
    if site_manifest:
        same = site_manifest.exists() and site_manifest.read_bytes() == manifest_path.read_bytes()
        results.append(("site manifest equals the app's", same, str(site_manifest)))
    return results


# --------------------------------------------------------------------------- #
# The bucket
# --------------------------------------------------------------------------- #

class Storage:
    """Supabase Storage REST, for one bucket. Public reads need no key; writes carry the service role."""

    def __init__(self, url: str, key: str | None = None):
        self.url = url.rstrip("/")
        self._key = key

    def public(self, path: str) -> str:
        return f"{self.url}/storage/v1/object/public/{BUCKET}/{path}"

    def object(self, path: str) -> str:
        return f"{self.url}/storage/v1/object/{BUCKET}/{path}"

    def get(self, path: str) -> tuple[int, dict[str, str], bytes]:
        return request(self.public(path))

    def put(self, path: str, data: bytes, cache: str, upsert: bool) -> tuple[int, bytes]:
        if not self._key:
            raise RuntimeError("SUPABASE_SERVICE_ROLE_KEY is not set")
        headers = {"Authorization": f"Bearer {self._key}", "apikey": self._key,
                   "Content-Type": "application/json", "cache-control": cache,
                   "x-upsert": "true" if upsert else "false"}
        code, _, body = request(self.object(path), "POST", headers, data)
        return code, body


def exists_already(code: int, body: bytes) -> bool:
    """Storage answers a POST for an existing object with 400 and a Duplicate error."""
    text = body.decode("utf-8", "replace").lower()
    return code in (400, 409) and ("duplicate" in text or "already exists" in text)


def put_immutable(store: Storage, path: str, data: bytes) -> Result:
    """Write an object once. Already there and identical: fine (a re-run of the same commit). Already there
    and different: the edition id names other bytes somewhere, which is exactly what must never happen."""
    want = sha256(data)
    code, _, body = store.get(path)
    if code == 200:
        return (path, sha256(body) == want, "already published, identical" if sha256(body) == want
                else f"already published with different bytes (served {sha256(body)[:16]}, ours {want[:16]})")
    code, body = store.put(path, data, IMMUTABLE, upsert=False)
    if code != 200 and not exists_already(code, body):
        return (path, False, f"upload failed: HTTP {code} {body[:120].decode('utf-8', 'replace')}")
    code, _, served = store.get(path)                      # read after write: what is served is what was sent
    if code != 200:
        return (path, False, f"uploaded but not served: HTTP {code}")
    return (path, sha256(served) == want, f"uploaded, {len(data):,} bytes" if sha256(served) == want
            else f"served bytes differ after upload ({sha256(served)[:16]} vs {want[:16]})")


def put_pointer(store: Storage, data: bytes) -> Result:
    code, body = store.put(LATEST, data, POINTER, upsert=True)
    if code != 200:
        return (LATEST, False, f"upload failed: HTTP {code} {body[:120].decode('utf-8', 'replace')}")
    code, _, served = store.get(LATEST)
    return (LATEST, code == 200 and served == data, "points at this edition" if served == data else f"HTTP {code}")


def publish(edition_dir: Path, bundle: Path, commit: str, run_id: str, run_url: str,
            now: dt.datetime | None = None) -> tuple[list[Result], dict]:
    """Upload the edition in edition_dir, then move latest.json. Local proof first, so nothing half-checked is
    ever uploaded. Returns the results and what the summary prints."""
    local = check(edition_dir, bundle, None)
    if not all(ok for _, ok, _ in local):
        return local, {}
    manifest_bytes = (edition_dir / MANIFEST).read_bytes()
    manifest = json.loads(manifest_bytes)
    edition = manifest["edition"]
    store = Storage(os.environ["SUPABASE_URL"], os.environ.get("SUPABASE_SERVICE_ROLE_KEY"))
    results: list[Result] = []
    for name in sorted(manifest["parts"]):
        results.append(put_immutable(store, f"{edition}/{name}", (edition_dir / name).read_bytes()))
    results.append(put_immutable(store, f"{edition}/{MANIFEST}", manifest_bytes))
    stamp = (now or dt.datetime.now(dt.timezone.utc)).replace(microsecond=0).isoformat()
    published = {"commit": commit, "run_id": run_id, "run_url": run_url, "published_at": stamp,
                 "manifest_sha256": sha256(manifest_bytes)}
    code, _, _ = store.get(f"{edition}/{PUBLISHED}")
    if code == 200:
        results.append((f"{edition}/{PUBLISHED}", True, "already published; the first record stands"))
    else:
        results.append(put_immutable(store, f"{edition}/{PUBLISHED}",
                                     json.dumps(published, indent=1, sort_keys=True).encode("utf-8")))
    if not all(ok for _, ok, _ in results):
        return local + results, {}                        # the pointer moves only when every part is served
    latest = {"edition": edition, "manifest_sha256": sha256(manifest_bytes), "generated": manifest["generated"],
              "commit": commit, "published_at": stamp}
    results.append(put_pointer(store, json.dumps(latest, indent=1, sort_keys=True).encode("utf-8")))
    summary = {"edition": edition, "manifest_sha256": sha256(manifest_bytes), "commit": commit,
               "uploaded": sum(1 for _, ok, d in results if ok and d.startswith("uploaded")),
               "identical": sum(1 for _, ok, d in results if ok and d.startswith("already")),
               "bytes": sum(p["bytes"] for p in manifest["parts"].values()), "latest": latest}
    return local + results, summary


def verify(base_url: str, manifest_path: Path) -> list[Result]:
    """What the bucket serves, read anonymously: latest.json names this manifest's edition, the served manifest
    is this manifest byte for byte, and every part hashes to its entry."""
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    edition = manifest["edition"]
    base = base_url.rstrip("/")
    results: list[Result] = []
    code, headers, body = request(f"{base}/{LATEST}")
    try:
        latest = json.loads(body) if code == 200 else {}
    except ValueError:
        latest = {}
    results.append((f"{LATEST} names the committed edition", latest.get("edition") == edition,
                    f"HTTP {code}, serves {str(latest.get('edition', ''))[:16] or '(none)'}, committed {edition[:16]}"))
    results.append((f"{LATEST} is served with cache-control", "cache-control" in headers, headers.get("cache-control", "(missing)")))
    code, _, body = request(f"{base}/{edition}/{MANIFEST}")
    results.append((f"served {MANIFEST} is the committed one", code == 200 and body == manifest_bytes,
                    f"HTTP {code}, served {sha256(body)[:16]}, committed {sha256(manifest_bytes)[:16]}"))
    for name, entry in sorted(manifest["parts"].items()):
        code, _, body = request(f"{base}/{edition}/{name}")
        results.append((f"served {name}", code == 200 and sha256(body) == entry["sha256"],
                        f"HTTP {code}, served {sha256(body)[:16]}, committed {entry['sha256'][:16]}"))
    return results


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def report(results: list[Result], summary_path: Path | None, title: str, extra: str = "") -> int:
    failed = [r for r in results if not r[1]]
    for name, ok, detail in results:
        print(f"{'ok  ' if ok else 'FAIL'} {name}{f'  ({detail})' if detail else ''}")
    print(f"{len(results) - len(failed)} of {len(results)} checks passed")
    if summary_path:
        with summary_path.open("a", encoding="utf-8") as fh:
            fh.write(f"### {title}: {len(results) - len(failed)} of {len(results)} passed\n\n")
            if extra:
                fh.write(extra + "\n")
            fh.write("| Check | Result |\n|---|---|\n")
            for name, ok, detail in results:
                fh.write(f"| {name} | {'ok' if ok else 'FAIL'} {detail} |\n")
            fh.write("\n")
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="the parts on disk match the manifest, the manifest the bundle")
    c.add_argument("--dir", type=Path, required=True)
    c.add_argument("--bundle", type=Path)
    c.add_argument("--site-manifest", type=Path)
    p = sub.add_parser("publish", help="upload the edition and move latest.json (SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)")
    p.add_argument("--dir", type=Path, required=True)
    p.add_argument("--bundle", type=Path, required=True)
    p.add_argument("--commit", default=os.environ.get("GITHUB_SHA", ""))
    p.add_argument("--run-id", default=os.environ.get("GITHUB_RUN_ID", ""))
    p.add_argument("--run-url", default="")
    p.add_argument("--summary", type=Path, help="append a markdown table (e.g. $GITHUB_STEP_SUMMARY)")
    v = sub.add_parser("verify", help="what the bucket serves equals this manifest, read anonymously")
    v.add_argument("--url", required=True, help=".../storage/v1/object/public/editions")
    v.add_argument("--manifest", type=Path, required=True)
    v.add_argument("--summary", type=Path)
    a = ap.parse_args(argv)

    if a.cmd == "check":
        return report(check(a.dir, a.bundle, a.site_manifest), None, "Edition check")
    if a.cmd == "verify":
        return report(verify(a.url, a.manifest), a.summary, "Edition channel")
    if "SUPABASE_URL" not in os.environ:
        print("SUPABASE_URL is not set", file=sys.stderr)
        return 2
    results, summary = publish(a.dir, a.bundle, a.commit, a.run_id, a.run_url)
    extra = ""
    if summary:
        extra = ("| Edition (bundle sha256) | manifest.json sha256 | Commit | Parts uploaded / already present | Bytes | latest.json |\n"
                 "|---|---|---|---|---|---|\n"
                 f"| `{summary['edition']}` | `{summary['manifest_sha256']}` | `{summary['commit'][:7]}` | "
                 f"{summary['uploaded']} / {summary['identical']} | {summary['bytes']:,} | "
                 f"`{summary['latest']['edition'][:16]}` at {summary['latest']['published_at']} |\n")
    return report(results, a.summary, "Edition published", extra)


if __name__ == "__main__":
    sys.exit(main())
