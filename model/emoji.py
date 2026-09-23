#!/usr/bin/env python3
"""
Country flag emoji, derived from an ISO code.

    python3 model/emoji.py        # print the 27 pairs, for eyeballing

Why this is its own module
--------------------------
A flag glyph is *presentation*, not a fact about a country, so it does not belong in
`country_data.build()` and it is deliberately not in the JSON bundle. Two reasons, and the
second is the expensive one:

  * `build()` returns the canonical figures every renderer shares (DECISIONS.md #6). A glyph
    derived from `iso2`, which is already there, has nothing to reconcile against.
  * Adding any key to the bundle changes its sha256, which marks all 54 tracked artefacts
    stale (`tests/test_artifacts.py`) and forces a Chrome re-render -- in exchange for a glyph
    that must not appear on either artefact. Maximum cost, zero benefit.

Who may import this
-------------------
`generate_countries.py` only. Flags belong in tables of contents, indexes and navigation, and
nowhere else:

  * **not** `export_artifacts.py` / `Poster.tsx` -- no state emblems on an artefact (#47).
  * **not** `book/build.py` -- the book interior is mono (#28), and typst can only reach flag
    glyphs by falling back to a colour, macOS-only font, which would make `./run.sh book`
    render tofu anywhere else and stop being reproducible.

The web and mobile readers use `flagEmoji()` in `web/src/utils/format.ts` instead; mobile
inherits that file byte-for-byte via `mobile/__tests__/parity.test.ts`, so the two TypeScript
renderers share one implementation and this module is the only other one. Both are asserted
against the same 27-pair table, in `tests/test_emoji.py`.

The source stays ASCII: the glyphs are computed, never pasted, so this file survives any
encoding mishap and the expected values live in the test where they can be read.
"""
from __future__ import annotations

# Eurostat writes Greece as EL; the regional-indicator sequence needs the ISO 3166-1
# alpha-2 code, which is GR. This is the only member state where the two disagree.
OVERRIDES = {"EL": "GR"}

# 'A' -> U+1F1E6 REGIONAL INDICATOR SYMBOL LETTER A, and so on through 'Z'.
_REGIONAL_INDICATOR_A = 0x1F1E6
_OFFSET = _REGIONAL_INDICATOR_A - ord("A")


def flag(iso: str) -> str:
    """The flag emoji for a two-letter country code, e.g. 'NL' -> the Dutch flag.

    Raises on anything that is not a two-letter ASCII code, rather than returning a
    plausible-looking pair of boxes that would survive review.
    """
    code = OVERRIDES.get(iso.upper(), iso.upper())
    if len(code) != 2 or not code.isascii() or not code.isalpha():
        raise ValueError(f"not a two-letter ISO country code: {iso!r}")
    return "".join(chr(_OFFSET + ord(ch)) for ch in code)


def main() -> int:
    import csv
    from pathlib import Path

    params = Path(__file__).resolve().parent / "eu27_parameters.csv"
    with params.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            print(f"{row['iso2']}  {flag(row['iso2'])}  {row['country']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
