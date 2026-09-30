#!/usr/bin/env python3
"""
What this project can honestly say about its own evidence, in one place.

    python3 model/evidence.py      # print the disclaimer and the description of the checks

Why this file exists
--------------------
The report, the country PDFs, the web app, /ask, the posters and the briefs each described the
checks in their own words, and the words drifted past the truth: "every fact ... fetched, hashed and
checked" was printed over five migrated citations that were never quote-checked, and "hashed" over
136 Eurostat figures whose hash no reader could find: it sits in fetch_manifest.csv, not in the
registry the footnotes cite (corrected 2026-09-30; an earlier version of this note said they were
never hashed, which was itself wrong). So the wording lives here, every renderer takes it from the bundle,
and `tests/test_evidence.py` fails when an output describes a check that did not run.

No human has verified the findings. That is said on every surface, first, in the same words.
"""
from __future__ import annotations

import csv
import re
import unicodedata
import urllib.parse
from decimal import Decimal, InvalidOperation
from pathlib import Path

DISCLAIMER = (
    "Machine-checked, not human-verified. Automated agents found these sources and checked them "
    "mechanically; no person has reviewed the findings. English wording of a non-English source is a "
    "machine translation or a machine summary of the quoted text. Treat each fact as a lead to its "
    "cited source, not as established. Corrections are welcome through the repository's issue template."
)

# The checks, as they actually run. Each line must stay true for every fact it describes.
CHECKS = [
    ("Researched claims (holdings, operators, legal bases, indicators)",
     "the cited page or PDF was downloaded and its SHA-256 recorded, and the quoted text was found in "
     "the extracted document by literal matching. Every number and date in the printed value was "
     "found in the original-language quote; the English wording is a machine summary of the quote "
     "unless it appears in it verbatim. An archived copy was looked up on the Internet Archive; where "
     "none exists the footnote says so."),
    ("Eurostat figures",
     "the value was read from a pinned Eurostat dataset through its API and compared with the table "
     "cell, within 0.5%. The raw API response is stored and its SHA-256 recorded in "
     "model/fetch_manifest.csv. The footnote names the dataset, its dimensions and the retrieval date."),
    ("Categorical findings (infrastructure dependency, sovereignty indicators)",
     "admitted only when a second, independent automated reviewer reached the same value from the "
     "same quote."),
]

WITHHELD = ("A value that no checked source supports is withheld and shown as a gap. A gap means "
            "not yet sourced, never that the thing does not exist.")

PROVENANCE = f"{DISCLAIMER} {WITHHELD}"


def checks_text() -> str:
    return " ".join(f"{name}: {what}" for name, what in CHECKS)


# --------------------------------------------------------------------------- #
# Is the rendered value in the quote? (#82)
# --------------------------------------------------------------------------- #
# The quote check proves the quote is in the document. It never proved that the value the report
# prints is in the quote, and 9 of 31 printed counts carried numbers their quote does not contain
# (a 10-year retention period printed as a record count; "48 million victim records" added to a
# quote that says 17 million). So the rendered text is checked against the quote here, at render
# time, where it cannot be bypassed:
#
#   hard      every number and date in the value appears in the original-language quote. Otherwise
#             the value is a gap.
#   disclosed an acronym that is not in the quote, its gloss or the document title (often a
#             transliteration: MVR for МВР) stays, and the fact's checklist names it.
#   labelled  a value that is not a verbatim extract of the original is an English machine summary
#             of the quote, and says so. Its words are not checked; its figures are.

_GLOSS = re.compile(r"\s*\[English: (.*)\]\s*$", re.S)
# A number as written in any EU language: 1,007,920 / 1.007.920 / 1 007 920 / 4,1 / 4.1 / 17
_NUMBER = re.compile(r"(?<![\w.,])\d{1,3}(?:[.,   ]\d{3})+(?:[.,]\d+)?(?![\w])"
                     r"|(?<![\w.,])\d+(?:[.,]\d+)?(?![\w])")
# A name-like abbreviation: some hyphen-separated part has two or more capitals (ZMR, E-ID, RTR-GmbH,
# VIRBI), so "Directorate-General" is not one. Generic English abbreviations are not claims.
_TOKEN = re.compile(r"\b[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\b")
GENERIC = {"EU", "ID", "IT", "ICT", "PDF", "URL", "IP"}


def split_quote(quote: str) -> tuple[str, str]:
    """(original, English gloss) of a citation quote; the gloss is '' for an English source."""
    m = _GLOSS.search(quote)
    return (quote[:m.start()], m.group(1)) if m else (quote, "")


def _readings(token: str) -> set[Decimal]:
    """Every value a written number can mean. '1.007' is 1007 in German and 1.007 in English; a
    value matches a quote when one reading is shared, so locale never decides a pass or a fail."""
    digits = re.sub(r"[   ]", "", token)
    out: set[Decimal] = set()
    for thousands, decimal in ((",", "."), (".", ",")):
        parts = digits.split(decimal)
        if len(parts) > 2:
            continue
        whole = parts[0]
        groups = whole.split(thousands)
        if len(groups) > 1 and not all(len(g) == 3 for g in groups[1:]):
            continue
        text = "".join(groups) + ("." + parts[1] if len(parts) == 2 else "")
        try:
            out.add(Decimal(text).normalize())
        except InvalidOperation:
            continue
    return out


def numbers(text: str) -> list[tuple[str, set[Decimal]]]:
    return [(m.group(0), _readings(m.group(0))) for m in _NUMBER.finditer(text)]


def acronyms(text: str) -> set[str]:
    out = set()
    for tok in _TOKEN.findall(text):
        parts = tok.split("-")
        named = [p for p in parts if sum(ch.isupper() for ch in p) >= 2]
        if named and not all(p in GENERIC or p.isdigit() for p in named):
            out.add(tok)
    return out - GENERIC


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    return re.sub(r"\s+", " ", s).strip().casefold()


def value_in_quote(value: str, quote: str, title: str = "") -> dict:
    """How a printed value relates to its quote.

    ok               every number and date in the value is in the original quote (the hard rule)
    how              verbatim | verbatim_gloss | summary
    missing_numbers  numbers or dates not in the original; any makes ok False
    missing_names    acronyms not in the original, gloss or title; disclosed, never fatal"""
    original, gloss = split_quote(quote)
    in_original = set().union(*(r for _, r in numbers(original))) if original else set()
    missing_numbers = [tok for tok, readings in numbers(value) if readings and not readings & in_original]
    context = f"{original} {gloss} {title}"
    missing_names = sorted(a for a in acronyms(value) if a not in context)
    if _norm(value) and _norm(value) in _norm(original):
        how = "verbatim"
    elif gloss and _norm(value) in _norm(gloss):
        how = "verbatim_gloss"
    else:
        how = "summary"
    return {"ok": not missing_numbers, "how": how, "missing_numbers": missing_numbers,
            "missing_names": missing_names}


if __name__ == "__main__":
    print(DISCLAIMER, "", checks_text(), "", WITHHELD, sep="\n")


# --------------------------------------------------------------------------- #
# The per-fact checklist and grade (#82)
# --------------------------------------------------------------------------- #
# No numeric confidence: nothing has calibrated one (#10, #77). Instead each fact lists the checks it
# passed, and a fixed rule turns the list into one of two grades. A fact below Standard is not
# printed at all; it is a gap. The grade is always computed here, never read from data.

# --------------------------------------------------------------------------- #
# Source tiers (#83)
# --------------------------------------------------------------------------- #
# What "a top-quality source" means, mechanically. model/sources/authorities.csv classifies every
# cited host once; two cases are decided here, because the host alone cannot decide them:
#   - ec.europa.eu is Eurostat (T1) for a dataset, and otherwise a Commission page (T3);
#   - an archive URL is as good as the page it archived.
# Not (yet) a rule: "the operator's own domain is T1 for its register". national_data.csv's holder_url
# is the URL the research agent cited, not an independently known operator domain, so the rule would
# be true by construction. It needs operator domains recorded on their own evidence first.
# The classification was made by an agent on 2026-09-30 and has not been reviewed by a person.

TIERS = {
    1: "T1 authoritative original (official law portal, statistics office, Eurostat)",
    2: "T2 competent public body or audit office",
    3: "T3 other institution or company",
    4: "T4 secondary (unofficial law mirror, press, encyclopedia)",
}
AUTHORITIES = Path(__file__).resolve().parent / "sources" / "authorities.csv"
_authorities: dict[str, dict[str, str]] | None = None


def authorities() -> dict[str, dict[str, str]]:
    global _authorities
    if _authorities is None:
        with AUTHORITIES.open(newline="", encoding="utf-8") as fh:
            _authorities = {r["host"]: r for r in csv.DictReader(fh)}
    return _authorities


def host(url: str) -> str:
    """The host a URL speaks for; an archived copy speaks for the page it archived."""
    if url.startswith("https://web.archive.org/web/"):
        parts = url.split("/", 5)
        if len(parts) == 6:
            url = parts[5]
    return (urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")


def tier(source: dict) -> tuple[int, str]:
    """(tier, kind) of a source. Raises KeyError for a host nobody classified."""
    row = authorities()[host(source["url"])]
    if row["kind"] == "eurostat_or_commission":
        return (1, "eurostat") if source["doc_type"] == "dataset" else (3, "commission_page")
    if row["kind"] == "archive_of_another_source":
        return 4, "archive_without_original"
    return int(row["tier"]), row["kind"]


MANIFEST = Path(__file__).resolve().parent / "fetch_manifest.csv"
_dataset_hashes: set[str] | None = None


def dataset_hashes() -> set[str]:
    """Eurostat columns whose raw API response is stored with a recorded sha256 (fetch_eurostat.py)."""
    global _dataset_hashes
    if _dataset_hashes is None:
        with MANIFEST.open(newline="", encoding="utf-8") as fh:
            _dataset_hashes = {r["key"] for r in csv.DictReader(fh)
                               if r["kind"] == "eurostat" and r["http_status"] == "200" and r["sha256"]}
    return _dataset_hashes


STRONG, STANDARD = "Strong", "Standard"
GRADE_RULE = (
    f"{STRONG}: a T1 or T2 source (an authoritative original or a competent public body); an official "
    "or primary source; the quote found exactly in the hashed document; an "
    "archived copy of exactly that URL; no name in the value missing from the quote; and the value "
    "either quoted from an English source, found verbatim in the original, or resting on figures "
    "matched in the original. A categorical finding is Strong only after a blind review (a reviewer "
    "shown the quote and URL but not the proposed value). "
    f"{STANDARD}: every required check passed, but one of those did not. Anything less is not printed."
)


def _url_key(url: str) -> str:
    """Scheme, a trailing slash and the order of query parameters do not change the page."""
    u = urllib.parse.urlsplit(url.strip())
    query = urllib.parse.urlencode(sorted(urllib.parse.parse_qsl(u.query, keep_blank_values=True)))
    return f"{(u.hostname or '').removeprefix('www.')}{u.path.rstrip('/')}?{query}".lower()


def snapshot_is_exact(snapshot: str, url: str) -> bool:
    """Is this Wayback snapshot of exactly `url` (scheme and a trailing slash aside)?"""
    parts = snapshot.split("/", 5)          # https: '' web.archive.org web <timestamp> <original>
    if len(parts) < 6 or not snapshot.startswith("https://web.archive.org/web/"):
        return False
    return "@" not in urllib.parse.urlsplit(parts[5]).netloc and _url_key(parts[5]) == _url_key(url)


def checklist(checks: dict) -> list[str]:
    """The checks as short phrases a reader can scan, in the order the grade rule reads them."""
    out = [TIERS[checks["tier"]].split(" (")[0] + f" ({checks['tier_kind'].replace('_', ' ')})"]
    out += [{"primary": "primary source", "official": "official source", "secondary": "secondary source",
            "absence": "authoritative statement of absence"}.get(checks["source"], checks["source"])]
    if checks.get("dataset_value_reproduced"):
        out.append("dataset value reproduced from the hashed API response" if checks["document_hashed"]
                   else "dataset value reproduced; response not hashed")
    else:
        out.append(f"quote found ({checks['quote_match']} match) in the hashed document")
    out.append("archived copy of this URL" if checks["archived"] else "no archived copy of this URL")
    if "value" in checks:
        out.append({"verbatim": "value quoted verbatim",
                    "verbatim_gloss": "value quoted from the machine translation",
                    "summary": "value is a machine summary of the quote"}[checks["value"]])
        if checks["figures_matched"]:
            out.append("every figure found in the original")
        if checks["names_not_in_quote"]:
            out.append(f"not in the quote: {', '.join(checks['names_not_in_quote'])}")
    if "review" in checks:
        out.append({"agreed, not blind": "independent review agreed (not blind)",
                    "blind, same model": "blind review agreed (reviewer: same model as the researcher)",
                    "none": "not independently reviewed"}[checks["review"]])
    out.append("English source" if checks["language"] == "english" else "non-English source, machine-translated")
    return out


def assess(value: str, citation: dict, source: dict, *, categorical: bool) -> dict:
    """The checklist and grade for one citation backing one printed value."""
    dataset = source["doc_type"] == "dataset"
    original, gloss = split_quote(citation["quote"])
    t, t_kind = tier(source)
    checks: dict = {
        "tier": t,
        "tier_kind": t_kind,
        "source": citation["confidence"],
        "archived": snapshot_is_exact(source.get("archived_url", ""), source["url"]),
        "language": "english" if not gloss else "machine-translated",
    }
    if dataset:
        checks["dataset_value_reproduced"] = True
        checks["document_hashed"] = citation["claim"].split(":")[-1] in dataset_hashes()
    else:
        checks["quote_match"] = "loose" if "quote loose" in citation["checked_by"] else "exact"
        checks["document_hashed"] = True
    if categorical:
        reviewed = (citation["claim"].split(":")[-1] == "foreign_dependency"
                    or citation["claim"].startswith("indicator:"))
        checks["review"] = ("blind, same model" if "blind review agreed" in citation["checked_by"] else
                            "agreed, not blind" if reviewed else "none")
    elif not dataset:
        v = value_in_quote(value, citation["quote"], source["title"])
        checks["value"] = v["how"]
        checks["figures_matched"] = bool(numbers(value))
        checks["names_not_in_quote"] = v["missing_names"]

    strong = (
        checks["tier"] in (1, 2)
        and checks["source"] in ("primary", "official")
        and checks["archived"]
        and checks["document_hashed"]
        and checks.get("quote_match") == "exact"
        and (not categorical or checks.get("review") == "blind, same model")
        and not checks.get("names_not_in_quote")
        and (checks["language"] == "english" or checks.get("value") == "verbatim"
             or checks.get("figures_matched", False))
    )
    return {"grade": STRONG if strong else STANDARD, "checks": checks}
