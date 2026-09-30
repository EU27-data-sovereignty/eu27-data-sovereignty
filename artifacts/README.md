# Representation style guides

**This directory is documentation, not output.** It holds one style guide per *representation* —
the forms this project's single dataset is rendered into. It is unrelated to
`countries/ARTEFACTS.csv` and `./run.sh artefacts`, which mean something else in this repository:
the tracked per-country PNG and PDF binaries. Those are covered here by
[`png/STYLE.md`](png/STYLE.md) and [`pdf/STYLE.md`](pdf/STYLE.md), but the word "artefact" in the
rest of the repo keeps its existing narrower meaning.

**Start with [`STYLE.md`](STYLE.md)**, the one style guide for every representation, generated from
`design/tokens.json` (#74, #76). The per-format guides below add only what is specific to their format.

| Guide | Covers | Built by |
|---|---|---|
| [`STYLE.md`](STYLE.md) | colour, type, facts and gaps, provenance, the ranking: everything shared | `design/build_tokens.py` |
| [`markdown/STYLE.md`](markdown/STYLE.md) | `countries/<ISO>/GOAL.md`, `countries/SUMMARY.md` | `model/generate_countries.py` |
| [`html/STYLE.md`](html/STYLE.md) | the React + Vite app | `web/` |
| [`pdf/STYLE.md`](pdf/STYLE.md) | the EU-27 report, the 27 country reports, the print book | `book/report.py`, `book/build.py` |
| [`png/STYLE.md`](png/STYLE.md) | the 27 poster infographics | `model/export_artifacts.py` |
| [`mobile/STYLE.md`](mobile/STYLE.md) | the Expo reader (stale, see its header) | `mobile/` |

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

The design system used to be upstream ("Warm Neutral + Terracotta", #21). Since #76 it is this
project's own EU palette, defined in `design/tokens.json` and documented in [`STYLE.md`](STYLE.md).

## Invariants that hold across every representation

These are not per-format choices. They are properties of the project, and breaking one in any
representation is a bug in that representation.

1. **One content model, many renderings (#6, #74).** Every sentence and figure comes from
   `model/document.py`, via `web/public/data/eu27.json`. No renderer writes content of its own, or
   recomputes or hardcodes a number.
2. **Every fact is sourced, every gap is visible (#75).** A value without a checked citation is
   never shown as a fact; it is a gap, set in muted italics. `document.py --check` enforces this.
3. **The caveat travels with the artefact (#25).** Anything that can be shared on its own carries
   its own provenance line.
4. **No state emblems, flags, crowns or official-looking wordmarks (#47, #76).** Country flag emoji
   are permitted **only** in the markdown index.
5. **Byte-reproducible output (#15, #34).** Nothing reads the wall clock; the build date comes from
   `.build-epoch` via `SOURCE_DATE_EPOCH`. Re-running with no input change produces a zero diff.
6. **The ranking is groups, never a score (#10, #77).** A placement always appears with its
   confidence and the guardrail sentence.
7. **Generated files say they are generated.** Every rendered document names the script that
   wrote it, so a reader knows what to edit.
