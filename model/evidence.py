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
     "the extracted document by literal matching. An archived copy was looked up on the Internet "
     "Archive; where none exists the footnote says so."),
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


if __name__ == "__main__":
    print(DISCLAIMER, "", checks_text(), "", WITHHELD, sep="\n")
