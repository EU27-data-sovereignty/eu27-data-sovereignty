# Verification

The one thing gating everything public-facing: whether the legal and regulatory claims in
`model/eu27_parameters.csv` have been checked against primary sources. `ROADMAP.md` states the
gate; this file is how the work is done and where it currently stands.

**Status: 2 of 189 cells sourced.** Run `./run.sh sources` for the live figure.

Where to look for each state's instruments is a separate document, [`SOURCES.md`](SOURCES.md),
together with the fetch pipeline that keeps a local copy of every document consulted. This file
stays about method.

## A second register, same bargain, different claim

`model/national_data.csv` is a parallel workstream with the same discipline and a different
subject (#60). This file's ledger asks *what does this state's law require*; that one asks *what
records does this state hold, and where is the official page that says so*. Both carry the
publisher, the retrieval date and a quote from the page, for the same reason — a URL shows that a
page exists, not that it says what the row claims.

**Status: 3 of 405 (country, record class) pairs recorded.** Run `./run.sh registers`.

Two differences worth knowing before working on it:

- It has **three** states, not two. `held`, `not_held`, and no row at all. A blank renders as
  "not yet recorded" in words, never as a dash and never as absence.
- Its `confidence: absence` guard is **weaker** than the one described below. Here an absence
  claim is checked against the parameter cell in a different file; there the cell *is* the row, so
  nothing independent corroborates it. That is stated in the module docstring rather than papered
  over.

It is not currently a gate on publication. It becomes one if the register section starts being
read as a statement of what a state does and does not hold, rather than as a scope note.

---

## What is and is not at issue

The capacity figures are openly scaled placeholders. The model says so, the briefs say so, the
posters print it on their face, and nobody is misled by a number that announces its own basis.

The legal and regulatory columns are a different kind of claim. They assert what 27 real
jurisdictions **require** — the governing instrument, the certification regime, the
classification ladder, the procurement route. They were researched from public policy documents
by one person and have not been checked against the instruments themselves. That is fine for a
research repository that says so and offers a corrections channel, which is what exists today.
It is not fine for an indexed site, a custom domain, a printed book, or anything handed to an
official (`DECISIONS.md` #25).

The three ordinal columns — `gov_cloud_maturity`, `certification_strength`,
`hyperscaler_dependency` — are author judgements derived from the columns above (#10). They are
**disclosed as judgements, never cited**. Attaching a source row to one is a validation error,
because a sourced-looking judgement is precisely the dishonesty this workstream exists to
prevent.

## The ledger

Since 2026-09-24 (#67) every sourced claim in the repository — not only the legal cells — is recorded
in one **source register**, `model/sources/`, validated by `model/provenance.py`:

| File | One row per | Key fields |
|---|---|---|
| `registry.csv` | original document or dataset | `source_id` (`<publisher>:<doc>[@vintage]`), `title`, `publisher`, `url`, `doc_type`, `published` |
| `citations.csv` | (claim, source) | `claim`, `source_id`, `locator` (page / article / dataset filter), `quote` or `value_as_found`, `confidence`, `retrieved` |

A legal cell is the claim `param:<ISO>:<column>`:

```csv
claim,source_id,locator,quote,value_as_found,unit,confidence,retrieved,checked_by
param:NL:data_classification,wetten-nl:bwbr0033507@2013-06-01,Artikel 4,"a. Staatsgeheim ZEER GEHEIM ...",,,primary,2026-09-11,...
```

`model/sources.py` reads these rows back in the shape this document describes below (`country`,
`column`, `url`, `publisher`, `retrieved`, `confidence`, `quote`) and applies the tiered rule to
them unchanged; `model/sources.csv` is retired.

**The quote is the requirement.** A URL shows that a page exists, not that it says what the cell
claims. It also survives the page being rewritten: a quote that no longer appears at its URL is a
finding, whereas a bare link that now says something else looks exactly like a verified cell.
Citations with a quote under 20 characters fail validation. The one exception is a dataset, which
has no words to quote: there the evidence is the `locator` (dataset, dimension filters, geo, period)
and the `value_as_found`, and a value that does not reproduce the cell within 0.5% does not count as
a citation of it. That is why the 26 `gov_employment_k` cells below are cited but not sourced.

Citations are sorted by `(claim, source_id)` so a diff shows what was added rather than where it
landed. The locator is checked against the cached document, not typed from memory: the first
migration's French locator was corrected from a section number of the instrument the quote *refers
to* to the page the quote is actually on.

## The tiered rule

| Tier | Columns | What counts |
|---|---|---|
| **1** — asserts a legal obligation | `legal_instrument`, `data_classification`, `certification_scheme` | the instrument itself: the statute, decree or scheme document (`confidence: primary`) — or, where the cell says no such instrument exists, an authoritative enumeration showing so (`confidence: absence`, see below). |
| **2** — describes what the state does | `sovereign_cloud_initiative`, `procurement_vehicle`, `digital_id`, `hyperscaler_gov_exposure` | an official government page. `primary` or `official`. |
| — **not sourceable** | `gov_cloud_maturity`, `certification_strength`, `hyperscaler_dependency` | author judgements; disclosed in the briefs and the CSVs, never cited |

`secondary` (press, vendor material, an aggregator) never satisfies tier 1. It is allowed to be
recorded for tier 2 while a better source is found, and it is visible as such in the ledger.

7 sourceable columns x 27 member states = **189 cells**.

## Working through it

```bash
./run.sh sources            # coverage report; fails on an unusable row
python3 model/sources.py --strict   # the end state: fails while any cell is unsourced
```

One country at a time, tier 1 first:

1. Read the cell in `model/eu27_parameters.csv`.
2. Find the instrument. National legal gazette first (Riigi Teataja, Legifrance,
   Gesetze-im-Internet, and so on), the ministry's own page second.
3. Add the row, with the sentence that carries the claim as the `quote`.
4. If the source contradicts the cell, **fix the cell**, and note it in `CHANGELOG.md`. The point
   of the exercise is to find these, so finding one is the process working.
5. Raise `COVERAGE_FLOOR` in `tests/test_sources.py` in the same commit.

`COVERAGE_FLOOR` is a ratchet and may only be raised. `--strict` is the end state `ROADMAP.md`
step 3 asks for and already works; it is not wired into CI yet, because a gate that fails on the
day it lands is a gate that gets disabled on the day after (`DECISIONS.md` #54).

## What the first nine cells found

The pilot took NL, EE and FR -- an easy case, the reference case and the hardest case -- across
the three tier-1 columns. Two cells were sourced to primary instruments, and the exercise
immediately earned its keep by finding two defects in the data it was checking.

**FR `data_classification` was wrong.** It read *"IGI 1300: Diffusion Restreinte / Secret / Tres
Secret"*, presenting Diffusion Restreinte as one of three classification levels. The instrument
says the opposite, in terms:

> Traitee par le § 1.4.3 de l'IGI 1300, la mention « Diffusion Restreinte » (DR) n'est pas un
> niveau de classification mais une mention de protection.

Corrected to the two levels that exist, with DR named as the protective marking it is.

**CY `population_m` was Estonia's.** The cell held `1.370`, which is exactly Estonia's Eurostat
figure for 1 January 2025 (1,369,995). Cyprus's own is 0.983 m. A copy-paste, found by the
Eurostat re-pull rather than by reading, and invisible to every test in the suite because a
plausible number in the right format is not a detectable error. Corrected. The capacity outputs
did not move, because the small-state floors already bind for Cyprus (#12) -- which is a
confirmation of the small-state cliff, not a reason the fix did not matter.

Neither would have been caught by more careful reading. That is the argument for the process.

## Two problems the schema had, found by using it — one solved

**Compound cells.** `covered_cells()` marks a cell sourced once one row exists, but the cells are
free prose and several assert more than one thing -- NL `legal_instrument` names two instruments,
DE `sovereign_cloud_initiative` names six programmes. Half a cell can therefore read as verified.
The convention is one row per instrument named, and where a clause cannot be sourced, **narrow
the cell** rather than leave it standing.

**Negative claims have no primary source — solved by `confidence: absence` (#58).** 22 of the 81
tier-1 cells assert that something does *not* exist, 21 of them in `certification_scheme` ("No
national scheme; ISO 27001"). No instrument enacts the absence of a scheme, so under a tier-1
rule admitting only `primary` those cells could never be sourced:

| | Under `primary` only | With `absence` |
|---|---|---|
| Tier-1 ceiling | 59/81 = **72.8%** | 81/81 |
| Whole ledger ceiling | 167/189 = **88.4%** | 189/189 |
| Can `--strict` ever pass? | **No** | Yes |

That was an unsatisfiable specification rather than a research backlog, and it would have let
`COVERAGE_FLOOR` ratchet quietly into a ceiling nobody had written down.

`absence` cites an **authoritative enumeration** — the competent authority's own register of
schemes, showing the category empty — because a claim about a complete list is evidenced by the
complete list. Demanding an instrument for a negative is a category error.

It is also the one value that could make this ledger *less* honest, by excusing a source nobody
could find, so `sources.py` refuses an `absence` row whose cell does not actually assert an
absence. `./run.sh sources` prints, per column, how many cells are negative and how many were
sourced that way. **39 of the 189 cells are negative** (22 tier-1, 17 tier-2).

No `absence` rows are recorded yet. ENISA's NCCA directory enumerates authorities rather than
schemes, and citing something weaker is exactly what this value exists to prevent. The mechanism
is unblocked; the register per state is the next batch of work.

## Then: the sampling audit

Coverage is not accuracy. Once a column is fully sourced, a random sample of its cells is
re-checked independently, and the disagreement rate is published per column. That measured error
rate — confidence as a number rather than a feeling — is what opens deployment stage 3 and the
book. Sourcing every cell only makes it possible to measure.

## Separately: the Eurostat figures

`population_m`, `gdp_eur_bn`, `gov_employment_k`, `elec_price_eur_mwh`, `renewables_pct` and
`land_km2` are Eurostat values. `ROADMAP.md` step 4 asked for a retrieval date and a re-pull
against the public API; `./run.sh fetch eurostat` does it, and `model/eurostat_pull.csv` now
carries a dataset code, a pinned period and the API's own `updated` vintage beside every value.

**Five of the six columns were already exactly right.** Pinned to the vintage each was actually
taken from, they reproduce at 0/27 cells differing:

| Column | Dataset | Pinned period | Differing |
|---|---|---|---|
| `population_m` | `tps00001` | 2025 | 0/27 |
| `gdp_eur_bn` | `nama_10_gdp` B1GQ CP_MEUR | 2025 | 0/27 |
| `elec_price_eur_mwh` | `nrg_pc_205` band IC, X_VAT | 2025-S2 | 0/27 |
| `renewables_pct` | `nrg_ind_ren` REN_ELC | 2024 | 0/27 |
| `land_km2` | `reg_area3` L0008 | 2019 | 0/27 |
| `gov_employment_k` | `nama_10_a64_e` NACE O | 2023 | **26/27** |

So the figures did not need updating; they needed a provenance, and now have one that
`tests/test_fetch.py` re-checks on every run. The pins do not move on their own (#57).

### The open defect: `gov_employment_k`

It reproduces from **no period at all** — best match 2023 at 5.3% median error — and **9 of 27
values match no year of the official series within 10%**:

| | SE | FI | SK | ES | AT | EE | LU | EL | MT |
|---|---|---|---|---|---|---|---|---|---|
| off by | 40% | 25% | 19% | 16% | 16% | 15% | 15% | 14% | 11% |

`README.md` describes this column as "Eurostat NACE section O". For a third of the member states
that is not where the number came from, and no re-pull fixes it — it is a provenance defect, not
a stale vintage. The 27 values are **held unchanged** rather than overwritten, because replacing
them would substitute one unexplained column for another without establishing what the first one
measured. `tests/test_fetch.py` names it as a known defect so it stays documented rather than
silently tolerated.

It matters: public-administration employment is one of the three scaling weights, so it moves
server counts. Adopting the official series wholesale would move EU-27 servers +1.4% and swing
individual states as far as SE −5.9% and ES +4.7%.

### A note on the tooling

The first version of this pipeline requested `nrg_cons=MWH2000-19999` for a column documented as
band IC. Band IC is 500–1,999 MWh/yr; that code is band ID. The mis-specified fetcher reported,
with a full table across all 27, that the column was 10% adrift and the published OPEX overstated
by 12%. Every part of that was false. A measurement tool that is itself wrong does not fail
quietly — it manufactures findings and attaches evidence to them. That is the argument for
pinning filters and periods in code with their reasoning beside them (#57), and for a test that
re-derives the claim rather than trusting the last run.
