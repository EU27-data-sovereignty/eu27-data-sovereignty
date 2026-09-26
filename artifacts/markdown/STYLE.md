# Markdown style

Covers `countries/<ISO>/GOAL.md` (26 generated briefs), `countries/SUMMARY.md` (the cross-country
table), and by exception `countries/NL/GOAL.md`.

Everything here is emitted by `model/generate_countries.py` — `write_goal()` for a brief,
`write_summary()` for the summary. There is no template engine: `write_goal()` is a pure
dict → markdown function built from one long f-string. That is deliberate (#7), and it means the
markdown *is* the template. Read it before changing it.

## The generated/authored split

| File | Status | Who may edit |
|---|---|---|
| `countries/<ISO>/GOAL.md`, 26 of them | generated | nobody — edit the generator or the CSVs |
| `countries/SUMMARY.md` | generated | nobody — edit `write_summary()` |
| `countries/NL/GOAL.md` | **hand-written** | a human, freely |

NL is the reference case the other 26 are scaled from, so it is excluded from generation (#5) and
`tests/test_model.py` asserts the generator never touches its bytes. **Any change to the brief
structure has to be applied to NL by hand, in the same commit.** Forgetting this is the most
likely way for the 27 to drift apart.

To keep hand edits to a generated country, rename the file (`GOAL.md` → `ANALYSIS.md`). The
generator only ever writes `GOAL.md`, `params.csv`, `workloads_inputs.csv` and
`region_allocation_inputs.csv`.

## Document shape

Every generated brief opens with an H1 naming the country, then a blockquote provenance banner
that names the generating script, its inputs, and what to re-run after an edit. Then numbered
H2 sections, in a fixed order.

A generated brief has **thirteen** sections; the hand-written Dutch one has twenty-one. Both are
driven from a single list — `SECTIONS` in `model/generate_countries.py` for the generated briefs —
so the contents list and the headings are built from the same source and cannot disagree.
`tests/test_model.py` asserts that for all 27, NL included.

The section list is stable and the numbers are part of the contract — the README, the web app,
the book and `countries/NL/GOAL.md` all cross-reference sections by number ("see §10", "Dutch
`GOAL.md` section 16"). **Renumbering is a breaking change.** Adding a section at the end is not;
adding one in the middle is.

Extending the brief rather than adding a second document per country is itself a decision (#3).
A new document per country would have to be generated, tracked, linked and kept in sync; a
section would not.

## Tables

The brief is mostly tables, and there are exactly two idioms. Use them; do not invent a third.

**Key–value facts** — a headerless two-column table. The empty header row is intentional: these
are labelled facts, not a dataset with column semantics.

```markdown
| | |
|---|---|
| Population | 83.58 m (1 January; Eurostat tps00001, 2025) |
| Land area | 353,296 km2 (Eurostat reg_area3, 2019) |
```

**Datasets** — a headed table, numeric columns right-aligned with `---:`.

```markdown
| Workload | Class | CPU cores | Storage (PB) |
|---|---|---:|---:|
| Core government applications | Government | 244,100 | 79.9 |
```

Rules for both:

- Every number carries its unit in the label or the cell, never neither.
- **Citations are looked up, never typed.** A figure that came from a source gets its citation
  from the source register (`model/sources/`), which `write_goal()` resolves by `source_id` (#67).
  `tests/test_provenance.py` fails if a literal `(Eurostat …)` string reappears in the generator,
  so hand-writing one is not a style preference — it breaks the suite. This replaced an inline
  form that had drifted: one brief named a series and year the pinned source does not use.
- A citation that cannot support its cell says so in the cell. Where a value does not reproduce
  its source within 0.5%, the brief prints that beside the figure rather than hiding it — as
  `gov_employment_k` currently does in all 27.
- Thousands separators on counts, not on years or identifiers.
- ASCII only in generated prose: `km2`, not `km²`; `-`, not `—`. The generator's output is
  compared byte-for-byte across platforms, and the briefs are re-rendered into Typst and HTML
  downstream. Country names keep their own diacritics, because those come from the dataset.

## Prose

- **Say what the number is, then what it means.** Each section leads with the table and follows
  with one or two sentences of reading. The brief is for a civil servant skimming for the number
  and a policymaker reading for the argument; both are served by that order.
- **Hedge the claim, not the sentence.** "187 of the 189 have not been checked against primary
  sources" beats "these may possibly be somewhat unverified".
- **Conditional prose comes from the data, not from a human deciding per country.** The generator
  builds its variant sentences from dict lookups keyed on ordinal ratings. A sentence that is true
  of only one country belongs in that country's parameters, not in an `if iso == "DE"`.
- **Never assert a legal requirement without its disclaimer.** §10 carries a standing blockquote
  saying the entries are unverified research and not legal advice. It is not optional and not
  shortenable (#25).

## Links

- Cross-references inside the repo are relative paths, so they resolve on GitHub and on disk.
- External links point at an **official description page** for the thing named, and are rendered
  as `[name](url)`. A bare URL in a table cell wraps badly in every downstream renderer.
- Sourced claims cite the ledger, not a URL alone: a URL shows a page exists, not that it still
  says what the row claims (`VERIFICATION.md`).

## Reproducibility

`write_goal()` must stay a pure function of its input dict. No wall-clock reads, no dict iteration
whose order is not fixed, no floating-point formatting that varies by platform. The generation date
comes from `SOURCE_DATE_EPOCH` (#15), and `./test.sh` regenerates all 27 and fails on any diff —
so a non-deterministic renderer fails the gate rather than producing drift.

## Verify

```
./run.sh data                                    # regenerate briefs, CSVs and the bundle
git diff --stat -- countries/                    # expected: only what you meant to change
python3 -m unittest tests.test_model -v          # includes the regeneration no-op test
```
