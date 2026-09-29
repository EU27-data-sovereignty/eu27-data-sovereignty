#!/usr/bin/env python3
"""
Admit researched claims about critical holdings only after checking them against the document.

    python3 model/research.py verify [--iso DE ...]   # fetch, hash, find the quote, look up an archive
    python3 model/research.py admit                    # write verified claims into the registers
    python3 model/research.py report                   # coverage per country, from verification.csv

Why this file exists
--------------------
The inventory of critical holdings (DECISIONS.md #73) is researched by agents across all 27 member
states at once. An agent can misquote, paraphrase, cite a homepage or invent a page. So nothing an
agent returns is trusted: its output lands in `model/research/<ISO>.json` (staging, never rendered),
and a claim reaches the source register only when this script has

1. fetched the cited URL through `fetch.py` (polite, robots-aware, one request at a time),
2. stored the document in `cache/` and recorded its sha256 in `fetch_manifest.csv`,
3. extracted the text (HTML, or PDF via `pdftotext`) and found the quote in it, and
4. looked up an archived copy on the Internet Archive, recorded when one exists.

That is what makes a footnote "unimpeachable" (#75): the reader can fetch the same URL, compare the
hash, and find the same words, or open the archived copy if the page has moved.

Matching is deliberately literal. Whitespace, quote marks, dashes and soft hyphens are normalised,
because PDF extraction and HTML rendering change them; words are not. A second pass ignores
punctuation entirely and is recorded as `match: loose`, so a reader can tell the two apart. A quote
that is not in the document is `not_found`, and the claim stays in staging with that reason.

Every outcome is a row in `model/research/verification.csv`, including failures: a page that refused
us (403, robots) is a measured fact, not a gap.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import html
import html.parser
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import fetch  # noqa: E402

STAGING = ROOT / "model" / "research"
INDICATOR_STAGING = STAGING / "indicators"
INDICATOR_VALUES = ROOT / "model" / "sovereignty_indicators.csv"
VERIFICATION = STAGING / "verification.csv"
VFIELDS = ["iso", "class_id", "field", "url", "http_status", "content_type", "sha256", "match",
           "archived_url", "checked"]
KIND = "holdings"

# The agent's document types, mapped onto the registry's closed vocabulary (provenance.DOC_TYPES).
DOC_TYPE = {
    "legislation": "statute", "official_page": "webpage", "annual_report": "annual_report",
    "audit_report": "report", "statistics": "report", "procurement": "webpage",
    "eu_document": "report", "press_release": "webpage", "secondary": "webpage",
}
SECONDARY = {"secondary", "press_release"}


# --------------------------------------------------------------------------- #
# Text extraction and matching
# --------------------------------------------------------------------------- #

class _Text(html.parser.HTMLParser):
    SKIP = {"script", "style", "noscript", "template"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def extract(body: bytes, content_type: str) -> str:
    if content_type == "application/pdf" or body[:5] == b"%PDF-":
        with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
            fh.write(body)
            fh.flush()
            r = subprocess.run(["pdftotext", "-enc", "UTF-8", fh.name, "-"], capture_output=True)
        return r.stdout.decode("utf-8", errors="replace")
    text = body.decode("utf-8", errors="replace")
    if "html" in content_type or "<html" in text[:2000].lower():
        p = _Text()
        p.feed(text)
        return " ".join(p.parts)
    return text


_QUOTES = str.maketrans({"‘": "'", "’": "'", "‚": "'", "‛": "'", "´": "'",
                         "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
                         "–": "-", "—": "-", "‑": "-", " ": " ", " ": " "})


def normalise(s: str) -> str:
    s = unicodedata.normalize("NFKC", html.unescape(s)).translate(_QUOTES).replace("­", "")
    s = re.sub(r"-\s*\n\s*", "", s)          # PDF line-break hyphenation
    return re.sub(r"\s+", " ", s).strip().lower()


def loose(s: str) -> str:
    return re.sub(r"[\W_]+", "", normalise(s))


def match(quote: str, text: str) -> str:
    q, t = normalise(quote), normalise(text)
    if len(q) < 20:
        return "too_short"
    if q in t:
        return "exact"
    if loose(quote) in loose(text):
        return "loose"
    return "not_found"


def archived(url: str) -> str:
    """The Internet Archive's closest snapshot, or '' if it has none. Never raises."""
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    req = urllib.request.Request(api, headers={"User-Agent": fetch.UA})
    try:
        fetch._throttle()
        with urllib.request.urlopen(req, timeout=fetch.TIMEOUT) as resp:
            snap = json.load(resp).get("archived_snapshots", {}).get("closest", {})
        return snap.get("url", "").replace("http://", "https://", 1) if snap.get("available") else ""
    except Exception:
        return ""


# --------------------------------------------------------------------------- #
# Staging
# --------------------------------------------------------------------------- #

def staged(isos: list[str] | None = None, where: Path = STAGING) -> dict[str, dict]:
    out = {}
    for path in sorted(where.glob("*.json")):
        if isos and path.stem not in isos:
            continue
        out[path.stem] = json.loads(path.read_text(encoding="utf-8"))
    return out


def claims(doc: dict):
    """(class_id, claim) for every claim in one country's staging file, extras included."""
    for h in doc.get("holdings", []):
        for c in h.get("claims", []):
            yield h["class_id"], c
    for x in doc.get("extra_holdings", []):
        for c in x.get("claims", []):
            yield f"extra:{x['suggested_class']}", c
    for ind in doc.get("indicators", []):
        for c in ind.get("claims", []):
            yield f"indicator:{ind['id']}", {**c, "field": "indicator"}


def load_verification() -> list[dict[str, str]]:
    if not VERIFICATION.exists():
        return []
    with VERIFICATION.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_verification(rows: list[dict[str, str]]) -> None:
    rows = sorted(rows, key=lambda r: (r["iso"], r["class_id"], r["field"], r["url"]))
    with VERIFICATION.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=VFIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


# --------------------------------------------------------------------------- #
# verify
# --------------------------------------------------------------------------- #

def verify(isos: list[str] | None) -> int:
    today = dt.date.today().isoformat()
    docs = staged(isos)
    for iso, doc in staged(isos, INDICATOR_STAGING).items():
        docs.setdefault(iso, {}).setdefault("indicators", doc.get("indicators", []))
    existing = {(r["iso"], r["class_id"], r["field"], r["url"]): r for r in load_verification()}
    manifest = fetch.load_manifest()
    fresh_manifest = []
    texts: dict[str, tuple[fetch.Result, str]] = {}
    archives: dict[str, str] = {}

    for iso, doc in docs.items():
        for class_id, c in claims(doc):
            url = c["url"].strip()
            key = (iso, class_id, c["field"], url)
            if key in existing and existing[key]["match"] in ("exact", "loose"):
                continue
            if not url.startswith("https://"):
                existing[key] = dict(zip(VFIELDS, [iso, class_id, c["field"], url, "not-https",
                                                   "", "", "rejected", "", today]))
                continue
            if url not in texts:
                result = fetch.fetch(url)
                text = extract(result.body, result.content_type) if result.ok else ""
                texts[url] = (result, text)
                fresh_manifest.append(fetch.store(iso, KIND, class_id, url, result, today))
            result, text = texts[url]
            m = match(c["quote"], text) if result.ok else "fetch_failed"
            if m in ("exact", "loose") and url not in archives:
                archives[url] = archived(url)
            existing[key] = {
                "iso": iso, "class_id": class_id, "field": c["field"], "url": url,
                "http_status": result.status, "content_type": result.content_type,
                "sha256": fetch.sha256(result.body) if result.body else "",
                "match": m, "archived_url": archives.get(url, ""), "checked": today,
            }
        print(f"{iso}: checked", file=sys.stderr)

    fetch.write_manifest(fetch.merge(manifest, fresh_manifest))
    write_verification(list(existing.values()))
    return report()


# --------------------------------------------------------------------------- #
# report
# --------------------------------------------------------------------------- #

def report() -> int:
    rows = load_verification()
    by: dict[str, dict[str, int]] = {}
    for r in rows:
        by.setdefault(r["iso"], {}).setdefault(r["match"], 0)
        by[r["iso"]][r["match"]] += 1
    kinds = ["exact", "loose", "not_found", "fetch_failed", "too_short", "rejected"]
    print(f"{'iso':<4}" + "".join(f"{k:>13}" for k in kinds))
    for iso in sorted(by):
        print(f"{iso:<4}" + "".join(f"{by[iso].get(k, 0):>13}" for k in kinds))
    total = {k: sum(v.get(k, 0) for v in by.values()) for k in kinds}
    print(f"{'all':<4}" + "".join(f"{total[k]:>13}" for k in kinds))
    return 0


# --------------------------------------------------------------------------- #
# admit
# --------------------------------------------------------------------------- #

def slug(s: str, n: int = 40) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n] or "source"


def source_id(url: str) -> str:
    host = urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")
    return f"{slug(host)}:{hashlib.sha256(url.encode()).hexdigest()[:10]}"


def admit() -> int:
    """Verified claims -> sources/registry.csv, sources/citations.csv and national_data.csv."""
    import national_data as nd  # noqa: PLC0415
    import provenance  # noqa: PLC0415

    ok = {(r["iso"], r["class_id"], r["field"], r["url"]): r for r in load_verification()
          if r["match"] in ("exact", "loose")}
    reg = provenance.registry()
    cites = {(c["claim"], c["source_id"], c["locator"]): c for c in provenance.citations()}
    rows = {(r["iso"], r["record_class"]): r for r in nd.read_rows()}
    admitted = 0

    for iso, doc in staged().items():
        for h in doc.get("holdings", []):
            cls = h["class_id"]
            if cls not in nd.RECORD_CLASSES:
                continue
            good = {}
            for c in h.get("claims", []):
                v = ok.get((iso, cls, c["field"], c["url"].strip()))
                if v and c["field"] not in good:
                    good[c["field"]] = (c, v)
            status = h.get("status")
            if status == "held" and "holding_name" not in good:
                continue       # a holding is admitted only when its existence is verified
            if status == "not_held" and "not_held" not in good:
                continue
            if status not in ("held", "not_held"):
                continue

            for field, (c, v) in good.items():
                sid = source_id(v["url"])
                reg.setdefault(sid, {
                    "source_id": sid, "title": c.get("title", "").strip() or v["url"],
                    "publisher": c.get("publisher", "").strip() or urllib.parse.urlsplit(v["url"]).netloc,
                    "url": v["url"], "doc_type": DOC_TYPE.get(c.get("doc_type", ""), "webpage"),
                    "published": c.get("published", ""), "language": c.get("language", ""),
                    "license": "", "archived_url": v["archived_url"],
                    "notes": f"sha256 {v['sha256']} ({v['content_type']}), fetched {v['checked']}",
                })
                kind = nd.KIND_OF_FIELD[field]
                confidence = ("absence" if field == "not_held" else
                              "secondary" if c.get("doc_type") in SECONDARY else "official")
                claim = f"record:{iso}:{cls}:{kind}"
                locator = "PDF text" if "pdf" in v["content_type"] else "page text"
                quote = c["quote"].strip()
                if c.get("quote_english", "").strip():
                    quote += f" [English: {c['quote_english'].strip()}]"
                cites[(claim, sid, locator)] = {
                    "claim": claim, "source_id": sid, "locator": locator, "quote": quote,
                    "value_as_found": c["value"].strip(), "unit": "", "confidence": confidence,
                    "retrieved": v["checked"],
                    "checked_by": f"research.py: quote {v['match']} in fetched document",
                }

            name = good.get("holding_name", (None, None))[0]
            oper = good.get("operator", (None, None))[0]
            first = next(iter(good.values()))[1]
            row = rows.get((iso, cls), {})
            row.update({
                "iso": iso, "tier": str(nd.TIER_OF[cls]), "record_class": cls, "status": status,
                "register": name["value"].strip() if name else row.get("register", ""),
                "holder": (oper["value"].strip() if oper else h.get("operator", "").strip()
                           or row.get("holder", "")),
                "holder_url": good["operator"][1]["url"] if "operator" in good else first["url"],
            })
            for field in nd.EXTRA_FIELDS:
                row[field] = good[field][0]["value"].strip() if field in good else row.get(field, "")
            rows[(iso, cls)] = row
            admitted += 1

    indicator_rows = admit_indicators(ok, reg, cites)
    provenance.write_registry(reg)
    provenance.write_citations(list(cites.values()))
    nd.write_rows(list(rows.values()))
    print(f"admitted {admitted} holdings and {indicator_rows} indicator values")
    return 0


def register_source(reg: dict, c: dict, v: dict) -> str:
    sid = source_id(v["url"])
    reg.setdefault(sid, {
        "source_id": sid, "title": c.get("title", "").strip() or v["url"],
        "publisher": c.get("publisher", "").strip() or urllib.parse.urlsplit(v["url"]).netloc,
        "url": v["url"], "doc_type": DOC_TYPE.get(c.get("doc_type", ""), "webpage"),
        "published": c.get("published", ""), "language": c.get("language", ""),
        "license": "", "archived_url": v["archived_url"],
        "notes": f"sha256 {v['sha256']} ({v['content_type']}), fetched {v['checked']}",
    })
    return sid


def admit_indicators(ok: dict, reg: dict, cites: dict) -> int:
    """Verified indicator claims -> sovereignty_indicators.csv and indicator:<ISO>:<id> citations.

    A value is admitted when at least one of its claims verified. A 'no' is an absence claim and is
    recorded with confidence 'absence', like a not-held register (#58)."""
    values: dict[tuple[str, str], str] = {}
    if INDICATOR_VALUES.exists():
        with INDICATOR_VALUES.open(newline="", encoding="utf-8") as fh:
            values = {(r["iso"], r["indicator"]): r["value"] for r in csv.DictReader(fh)}
    for iso, doc in staged(None, INDICATOR_STAGING).items():
        for ind in doc.get("indicators", []):
            if ind.get("value") not in ("yes", "partial", "no"):
                continue
            good = [(c, ok[(iso, f"indicator:{ind['id']}", "indicator", c["url"].strip())])
                    for c in ind.get("claims", [])
                    if (iso, f"indicator:{ind['id']}", "indicator", c["url"].strip()) in ok]
            if not good:
                continue
            claim = f"indicator:{iso}:{ind['id']}"
            for c, v in good:
                sid = register_source(reg, c, v)
                locator = "PDF text" if "pdf" in v["content_type"] else "page text"
                quote = c["quote"].strip()
                if c.get("quote_english", "").strip():
                    quote += f" [English: {c['quote_english'].strip()}]"
                cites[(claim, sid, locator)] = {
                    "claim": claim, "source_id": sid, "locator": locator, "quote": quote,
                    "value_as_found": ind["value"], "unit": "",
                    "confidence": ("absence" if ind["value"] == "no" else
                                   "secondary" if c.get("doc_type") in SECONDARY else "official"),
                    "retrieved": v["checked"],
                    "checked_by": f"research.py: quote {v['match']} in fetched document",
                }
            values[(iso, ind["id"])] = ind["value"]
    with INDICATOR_VALUES.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["iso", "indicator", "value"], lineterminator="\n")
        w.writeheader()
        w.writerows({"iso": i, "indicator": k, "value": val} for (i, k), val in sorted(values.items()))
    return len(values)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["verify", "admit", "report"])
    ap.add_argument("--iso", action="append")
    args = ap.parse_args(argv)
    if args.command == "verify":
        return verify([i.upper() for i in args.iso] if args.iso else None)
    if args.command == "admit":
        return admit()
    return report()


if __name__ == "__main__":
    sys.exit(main())
