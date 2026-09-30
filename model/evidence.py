#!/usr/bin/env python3
"""
What this project can honestly say about its own evidence, in one place.

    python3 model/evidence.py      # print the disclaimer and the description of the checks

Why this file exists
--------------------
The report, the country PDFs, the web app, /ask, the posters and the briefs each described the
checks in their own words, and the words drifted past the truth: "every fact ... fetched, hashed and
checked" was printed over 136 Eurostat figures that were never hashed and five migrated citations
that were never quote-checked. So the wording lives here, every renderer takes it from the bundle,
and `tests/test_evidence.py` fails when an output describes a check that did not run.

No human has verified the findings. That is said on every surface, first, in the same words.
"""
from __future__ import annotations

import re
import unicodedata
from decimal import Decimal, InvalidOperation

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
     "cell, within 0.5%. The footnote names the dataset, its dimensions and the retrieval date."),
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
