# Markdown style

Shared look: [`../STYLE.md`](../STYLE.md). This file covers `countries/<ISO>/GOAL.md` (27 generated
briefs) and `countries/SUMMARY.md` (the cross-country index).

Both are written by `model/generate_countries.py` as a **markdown rendering of the content model**
(`model/document.py`, #74). The class `Markdown` walks the same sections, blocks and spans as the PDF and
the web page, so a brief cannot say anything the report does not.

## Generated, all of them

| File | Status | Who may edit |
|---|---|---|
| `countries/<ISO>/GOAL.md`, all 27 | generated | nobody: edit the content model or the data |
| `countries/SUMMARY.md` | generated | nobody: edit `summary()` |
| `countries/NL/REFERENCE-CASE.md` | **hand-written note**, the original Dutch plan | a human; it feeds nothing (#72) |

The Netherlands is generated like the other 26. No country is a baseline (#72).

## Document shape

- **Header.** An H1 naming the country, then a blockquote saying the file is generated, by what, and
  that italic values are withheld until sourced.
- **Contents.** Anchor links to the numbered sections.
- **Sections.** Numbered H2 sections, in the content model's order: placement, fundamentals, critical
  holdings by priority, foreign-dependency exposure, legal posture, capacity status, open research.
  Contents and headings come from the same list; `tests/test_model.py` asserts they match.
- **Footer.** A rule, then the footnote definitions: one per source, in first-citation order.

## Facts, gaps and sources

- **A fact is followed by its footnote marker(s).** Markdown footnotes (`[^s3]`), one per source, render
  on GitHub. `[^s3]` is `[S3]` in the country's PDF.
- **A gap is in italics**: `*Not yet sourced*`, `*Not yet verified*`. Never an empty cell, never a guess.
- **Footnote definitions** give the short label, the title, the URL, and the archived copy when one
  matches the URL.
- **No hand-typed citation.** Every source comes from the register through the content model (#67, #75).

## Tables

The content model decides the columns. The renderer escapes `|` and aligns numeric columns right
(`---:`). Every number carries its unit.

## Reproducibility

The renderer is a pure function of the bundle. The date comes from `SOURCE_DATE_EPOCH` (#34), and
`./test.sh` regenerates all 27 and fails on any diff.

## Verify

```
./run.sh data                                    # regenerate briefs, bundle and /ask corpus
git diff --stat -- countries/                    # expected: only what you meant to change
python3 -m unittest tests.test_model -v          # contents match headings; regeneration is a no-op
```
