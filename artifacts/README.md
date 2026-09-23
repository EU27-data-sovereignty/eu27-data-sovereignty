# Representation style guides

**This directory is documentation, not output.** It holds one style guide per *representation* —
the forms this project's single dataset is rendered into. It is unrelated to
`countries/ARTEFACTS.csv` and `./run.sh artefacts`, which mean something else in this repository:
the tracked per-country PNG and PDF binaries. Those are covered here by
[`png/STYLE.md`](png/STYLE.md) and [`pdf/STYLE.md`](pdf/STYLE.md), but the word "artefact" in the
rest of the repo keeps its existing narrower meaning.

| Guide | Covers | Built by |
|---|---|---|
| [`markdown/STYLE.md`](markdown/STYLE.md) | `countries/<ISO>/GOAL.md`, `countries/SUMMARY.md` | `model/generate_countries.py` |
| [`html/STYLE.md`](html/STYLE.md) | the React + Vite app | `web/` |
| [`pdf/STYLE.md`](pdf/STYLE.md) | the A5 book, the 27 A4 briefs, the 27 briefing PDFs | `book/build.py`, `model/export_artifacts.py` |
| [`png/STYLE.md`](png/STYLE.md) | the 27 poster infographics | `model/export_artifacts.py` |
| [`mobile/STYLE.md`](mobile/STYLE.md) | the Expo reader | `mobile/` |

## What these guides are, and are not

They are the **working form** of rules that are otherwise scattered across `DECISIONS.md`. They do
not replace it. `DECISIONS.md` stays authoritative for *why* a rule exists and when it was taken;
these guides say *what to do* when you are writing the code, and cite the decision number so the
reasoning is one hop away.

Two consequences, both deliberate:

- **A rule with no decision behind it does not belong here.** If you find yourself writing a new
  constraint into a style guide, it is a decision — add it to `DECISIONS.md` first.
- **The citations are machine-checked.** `tests/test_docs.py` reads every file in its `CITING`
  list, extracts each `#NN` reference, and fails if it does not resolve to a decision. These
  guides are in that list, so a stale citation breaks the suite rather than quietly misleading
  someone.

The page-level design system is also upstream, not here:
`~/dev/design/DESIGN_SYSTEMS.md` owns "Warm Neutral + Terracotta". `html/STYLE.md` records only
this project's **deltas** from it, with the measurement that justified each one.

## Invariants that hold across every representation

These are not per-format choices. They are properties of the project, and breaking one in any
representation is a bug in that representation.

1. **One dict, many renderings (#6, #7).** Every figure comes from `country_data.build()`, via
   `web/public/data/eu27.json`. No renderer recomputes, re-derives or hardcodes a number. A
   representation that can disagree with another one is already wrong, whichever is correct.
2. **The caveat travels with the artefact (#25).** Anything that can be shared on its own carries
   its own provenance line. An image gets forwarded without the page that explained it; a PDF gets
   printed without the site it came from.
3. **No state emblems, flags, crowns or official-looking wordmarks on the artefacts (#47).**
   These describe a programme that exists in no member state. They must not read as though a
   government published them. Country flag emoji are permitted **only** in tables of contents,
   indexes and navigation — never in a poster, a briefing PDF, a title block or a wordmark.
4. **Byte-reproducible output (#15, #53).** Nothing reads the wall clock. The build date comes
   from `.build-epoch` via `SOURCE_DATE_EPOCH`, and Chrome's PDF timestamps are rewritten after
   the fact. Re-running a build with no input change must produce a zero diff.
5. **Ratings are disclosed as judgements, never as measurements.** `gov_cloud_maturity`,
   `certification_strength` and `hyperscaler_dependency` are the author's opinions. Every
   representation that shows one says so in the same breath (#10).
6. **Generated files say they are generated.** Every rendered document names the script that
   wrote it and the inputs it read, so a reader knows what to edit.
