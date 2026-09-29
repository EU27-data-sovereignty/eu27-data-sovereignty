# Sovereign Data Centers for European States

An analysis, per EU member state, of the critical government data holdings a state cannot let depend on
infrastructure a foreign power can compel or switch off, and of what sovereign hosting for them requires.
Each state is analysed on its own fundamentals; none is scaled from or measured against another (#72).
Every fact is footnoted to a source whose text was fetched, hashed and checked (#75).

## Live site

**https://sovereign-data-centers.vercel.app**

Deliberately **not indexed** by search engines while the research is incomplete. The site, the EU-27
report (`/eu27-report.pdf`) and the 27 country reports (`/report/<ISO>.pdf`) show a value only when a
checked source supports it; everything else is shown as a gap. Capacity is not yet sized (#73).
Indexing is gated on the verification work in [`VERIFICATION.md`](VERIFICATION.md), as is the
`eu27.cloud` domain.

Corrections are welcome — there is a data-correction issue template.

## Deployment

Live at **https://sovereign-data-centers.vercel.app**, on the Vercel project
`pieteradejongs-projects/sovereign-data-centers`.

```
./run.sh deploy     # refuses a dirty tree or a non-main branch, runs ./test.sh, then deploys
```

**Deploys are manual: a push ships nothing.** Everything else is in
[`DEPLOYMENT.md`](DEPLOYMENT.md): topology and headers, the deploy flow, what `.vercelignore` must keep off
Vercel, the three stages, the freshness check for a stale site, known gaps, and a log of every production deploy.

The domain is deliberately unofficial-sounding so the site is not mistaken for an EU
institution's (#50); it is being registered through Vercel ($7.99 first year, $24/yr renewal; checked 2026-09-26) and held unattached until stage 3 (#70).

## Verification

The legal and regulatory columns assert what 27 real jurisdictions **require**. That is a
different kind of claim from a scaled capacity placeholder, and it is the gate on everything
public-facing (#25).

```
./run.sh sources            # legal cells: currently 2 of 189
python3 model/provenance.py # every claim, per namespace: 138 of 621 parameter cells
./run.sh fetch              # retrieve the source documents into cache/
```

`model/sources/` is the **source register** (#67): `registry.csv` holds each original document once,
and `citations.csv` links every claim to it with a locator and **the sentence on the page that
supports the cell** (for a dataset, the value found there, which must reproduce the cell). A URL only shows a page exists — it cannot show the page still says what
it said, which is why the documents themselves are fetched and hashed (`SOURCES.md`).

Tier 1 — `legal_instrument`, `data_classification`, `certification_scheme` — asserts a legal
obligation and admits nothing but the instrument itself, or, where the cell says no such
instrument exists, an authoritative enumeration showing so (`confidence: absence`, #58). 39 of the
189 cells assert an absence; without that value tier 1 was capped at 72.8% and `--strict` could
never have passed. Tier 2 describes what a state runs, buys
or depends on, and takes an official government page. The three ordinal columns are the author's
judgements, **disclosed and never cited**; a source row for one is a validation error.

`COVERAGE_FLOOR` in `tests/test_sources.py` is a ratchet: it moves in the same commit as the rows
it counts, so progress cannot be silently undone. Method is in [`VERIFICATION.md`](VERIFICATION.md),
endpoints in [`SOURCES.md`](SOURCES.md).

## How decisions are recorded

Every choice that closes off an alternative gets an entry in [`DECISIONS.md`](DECISIONS.md). An entry
states the decision precisely enough that someone who was not there can see what was chosen, why, and why
not the other ways. From #72 on, every entry has these parts, in this order:

| Part | What it must say |
|---|---|
| **Decision.** | What was chosen, in one or two sentences, with the date. Concrete: file names, numbers, rules. |
| **Problem.** | What was wrong or missing that forced a choice. |
| **Alternatives considered.** | Every serious option, including the one chosen. Each rejected option carries a *Why not:* line giving the specific reason. "Worse" is not a reason; "needs pinned binaries on every build" is. |
| **Closes off.** | What this makes harder or impossible from now on. |
| **Verified:** | The command and output that show it is true in the tree, or `NOT YET` with what would verify it. |
| *Would change if:* | The observable condition under which the decision should be reopened. |

`tests/test_docs.py` fails the build when an entry from #72 on is missing one of these parts. Entries
before #72 keep their original shape; #71 is the closest earlier example.

A decision that is overturned is marked **Superseded by #N** and left in place.

## Layout

```
init.sh / run.sh / test.sh   set up, run, and fully test the project
model/
  assumptions.csv            engineering and cost constants for the capacity engine (sizing is paused, #73)
  holding_classes.csv        the 39 critical holding classes, by tier, with why each cannot depend on
                             foreign control (#73)
  eu27_parameters.csv        one row per country: population, GDP, public-admin employment, power price,
                             renewables, land, flags, existing gov cloud, digital ID, IXPs, and the
                             legal/regulatory posture columns (certification, classification, procurement)
  sources/registry.csv       the source register: one row per original document or dataset (#67)
  sources/citations.csv      one row per (claim, source), with locator and quote or dataset value
  provenance.py              validates the register; coverage per claim namespace
  sources.py                 the tiered rule for the legal cells, read from the register (./run.sh sources)
  institutions.csv           the public institutional contact map: web routes only, no names (#68)
  national_data.csv          the critical holdings register: per state and class, the register, operator,
                             legal basis, hosting, foreign dependency, size -- each cell cited (#73)
  research.py                admits researched claims only after fetching, hashing and finding the quote
  research/                  agent research staging (<ISO>.json) and verification.csv; never rendered
  document.py                the one content model every output renders (#74); --check is the #75 gate
  national_data.py           validates the register and reports coverage (./run.sh registers)
  emoji.py                   country flag emoji, derived from the ISO code (#61, #62)
  migration_phases.csv       workload class -> migration phase
  capacity_model.py          the capacity engine: workloads -> servers -> MW -> sites -> CAPEX/OPEX; kept for
                             sizing from measured holdings, checked against the one spreadsheet it reproduces
  country_data.py            one country's parameter row and register view, nothing about any other (#72)
  generate_countries.py      writes countries/<ISO>/GOAL.md (markdown rendering of the document) + SUMMARY.md
  export_json.py             writes web/public/data/eu27.json: countries, documents, claims, sources
  export_artifacts.py        renders the tracked per-country poster (./run.sh artefacts)
design/                      tokens.json, the one colour and type source, and build_tokens.py (#74, #76)
book/                        report.py (EU-27 report + 27 country PDFs) and the print book; see book/README.md
artifacts/                   one style guide per output representation - markdown, html, pdf, png,
                             mobile. Documentation, not output; see artifacts/README.md (#63)
OUTREACH.md                  institutional distribution map, one entry per member state
countries/
  SUMMARY.md                 cross-country table (generated)
  ARTEFACTS.csv              sha256 of every tracked poster, and of the bundle it came from
  <ISO>/ (x27)               GOAL.md (generated from the content model) and <ISO>-infographic.png (tracked)
  NL/                        also: REFERENCE-CASE.md (the original hand-written Dutch plan, now a note, not
                             an input), the xlsx the engine reproduces, FRONTIER-MODEL.md, TODO, plan
web/                         React + Vite visualization app; reads the JSON bundle, no server
mobile/                      Expo reader for the same bundle; local only, never built or deployed
tests/                       stdlib unittest suite for the model and the data
PROGRESS.md                  where every workstream stands today, on one page
DECISIONS.md                 why every choice was made
CHANGELOG.md                 what changed and when
VERIFICATION.md              the source-verification workstream: schema, tiered rule, where it stands
FEASIBILITY-RANKING.md       authored note: EU-27 ranked on feasibility of sovereign data centers plus
                             sovereign AI models, in four groups; model half unsourced (#59)
DISTRIBUTION-AND-TRUST.md    authored note: what sovereign infrastructure can borrow from CDN
                             architecture, and the encryption, accountability and auditability
                             that wide distribution depends on (#64)
```

Python is the source of truth. The markdown briefs, the PDFs, the web app and the posters all render one
content model (`model/document.py`), so they cannot disagree with each other (#74).

## Running

```
./init.sh                                   # set up from scratch (checks tools, installs, builds data)
./run.sh                                    # dev server on http://localhost:5173
./run.sh data                               # regenerate country files, briefs and the JSON bundle
./run.sh help                               # every command
./test.sh                                   # the full gate: model, types, lint, unit, build, e2e, a11y
./run.sh artefacts                          # re-render the tracked posters
./run.sh sources                            # verification-ledger coverage
./run.sh registers                          # critical national data register coverage
./run.sh fetch                              # fetch source documents into cache/ (see SOURCES.md)
./run.sh deploy                             # full gate, then deploy to Vercel production
./run.sh export                             # EU-27 report + 27 country reports (PDF, footnoted)
./run.sh book                               # typeset the print book's authored parts
python3 model/research.py verify            # check staged research: fetch, hash, find each quote
python3 model/research.py admit             # write verified claims into the registers
```

`export` and `book` need typst (`brew install typst`), and write into `book/build/`, which is
gitignored — that build output is never committed (`DECISIONS.md` #41).

`artefacts` is the other, separate pipeline: headless Chrome renders `<ISO>-infographic.png` into
each country directory, a **tracked deliverable** (#24, #51). `countries/ARTEFACTS.csv` records the
data bundle each was rendered from so the test suite can tell when one has gone stale (#52). Needs
Chrome and `npm`. The Chrome briefing PDF is retired (#76).

The model on its own, without the app:

```
python3 model/document.py DE                # one country's document as JSON
python3 model/document.py --check           # the #75 gate: every fact shown is sourced
python3 model/generate_countries.py         # regenerate the 27 markdown briefs and SUMMARY.md
```

Standard library only. The capacity engine still reproduces the xlsx it was built from (5,691 servers,
14.2 MW, EUR 339 m) as an arithmetic check; those inputs size nothing (#72).

## Method

1. **Fundamentals.** Each state's measured characteristics come from pinned Eurostat series, each value
   footnoted with the series, dimensions and retrieval date.
2. **Critical holdings.** `model/holding_classes.csv` lists 39 classes of government data holding, from
   the identity spine (tier 0) through the legal, fiscal and security state (tier 1) to health,
   statistics and archives (tiers 2 and 3). For each state and class the register records the holding,
   its operator, legal basis, hosting, foreign dependency and size, each only where a source states it.
3. **Research, then verification.** Agents research all 27 states in parallel and stage claims with
   verbatim quotes. `model/research.py` admits a claim only after fetching the document, recording its
   SHA-256, finding the quote in the extracted text and looking up an archived copy.
4. **Priority.** Holdings are ranked by a declared rule: consequence of loss, difficulty of rebuilding and
   known exposure to non-EU providers. It is a formula, not a judgement about any state.
5. **Capacity.** Withdrawn until each state can be sized from its own measured holdings (#73).

## What the evidence shows so far

`countries/SUMMARY.md` and the Overview page give the live figures: how many holdings are verified per
state, how many facts are sourced, and what is still open. The earlier headline figures (EU-27 design
load, servers, CAPEX) were Dutch-scaled and are withdrawn; `CHANGELOG.md` records them and why.

## Who this is for

The audience is European policymakers and civil servants. The bodies below are the
institutional owners of the decisions this model touches — cloud policy, certification,
classification and procurement for government workloads.

**This repository lists institutions and roles only, never named individuals.** A public
official's work contact is still personal data, and a public repository is a scrape target
(see `DECISIONS.md` #26).

### EU level

| Body | Why it is relevant |
|---|---|
| European Parliament — ITRE | Industry, Research and Energy: the cloud, data and infrastructure file |
| European Parliament — LIBE | Civil Liberties: data protection and the jurisdiction question |
| European Parliament — IMCO | Internal Market: the Data Act and procurement rules |
| European Commission — DG CONNECT | Cloud policy, the EU Cloud Services Scheme, Digital Decade targets |
| European Commission — DG DIGIT | The Commission's own cloud and interoperability posture |
| Council — Telecom Working Party | Where member-state positions on cloud sovereignty are reconciled |
| ENISA | Certification schemes, including the unresolved sovereignty requirements in EUCS |
| European Court of Auditors | Has previously audited Commission cloud procurement |

### National level

Each country's own institutions are already in the dataset rather than duplicated here.
`model/eu27_parameters.csv` carries, per member state:

- `procurement_vehicle` — the central purchasing body a sovereign core would be bought through
  (BBG, UGAP, Consip, Hansel, SKI, CPO LT, ESPAP, Kammarkollegiet, and so on)
- `sovereign_cloud_initiative` — the operator of the existing government cloud
  (BRZ, ITZBund, DINUM, PSN, GRNET, MITA, RIT, APIS IT, NISZ, VRAA, CTIE, ADR, MIRRI, …)
- `digital_id` — the national identity scheme and its operator
- `certification_scheme` — the national cloud assurance regime and its authority
  (ANSSI for SecNumCloud, BSI for C5, CCN for ENS, ACN in Italy, NÚKIB in Czechia, Traficom in Finland)

Read them per country in that country's `GOAL.md` §10 and §11, or across all 27 in
`countries/SUMMARY.md`.

### A note on timing

The legal and regulatory entries are not yet verified against primary sources. The first
thing any of these bodies would check is the entry about their own country, so outreach
before that verification is done invites an easy dismissal. See `ROADMAP.md`.

## Caveats

The electricity prices are 2025-S2 band-IC averages rather than negotiated tariffs, and public-administration
employment is *nominally* Eurostat NACE section O (excludes public health and education) — but for 9 of
the 27 states that column matches no year of the official series, and is a known open defect rather than
a sourced figure (`VERIFICATION.md`). The other five Eurostat columns are pinned to a stated dataset and
period and machine-checked to reproduce from it. The per-country sovereign-cloud
and digital-ID entries were researched in September 2026 and will date.

**The legal and regulatory entries are withheld until sourced.** The certification
schemes, classification ladders and procurement routes are assertions about what real jurisdictions
actually require, and **187 of the 189 have not been checked against primary sources**. Two have:
`./run.sh sources` prints the live figure, and `model/sources/citations.csv` names exactly which,
with the quote that supports each. Assume any given entry is unverified unless the ledger says otherwise.

Checking the first of them found two defects — France's classification ladder listed a protective
marking as a classification level, and Cyprus's population was Estonia's — so the unverified
entries should be read as what they are: one researcher's reading, useful and quite possibly
wrong in specifics. Nothing here should be relied on for a procurement or policy decision until
that verification is done — see `DECISIONS.md` #25 for the gate, and open an issue if you can
correct an entry.

## Licence

Two licences, because this repository holds two different things.

| | Covers | Terms |
|---|---|---|
| `LICENSE` | The code — `model/*.py`, `tests/`, `web/src/`, `web/e2e/`, `*.sh` | MIT |
| `LICENSE-DATA` | The dataset and documents — `model/*.csv`, `countries/**`, the JSON bundle, the markdown | CC BY 4.0 |

Images are a separate case again: provenance for every one, including which are AI-generated, is in
[`ASSETS.md`](ASSETS.md).

CC BY rather than MIT for the data because MIT grants rights over "the Software" and says nothing about a
database, and because an EU-focused dataset attracts a sui generis right under Directive 96/9/EC that MIT
does not address. Attribution also keeps the contestable ratings in this dataset traceable back to their
caveats.

## The original Dutch plan

`countries/NL/REFERENCE-CASE.md` is the hand-written plan this project began from: design philosophy,
architecture, sovereignty stack and threat model for the Netherlands. It is kept as a note. It is no longer
an input to any country's analysis, the Netherlands' included (#72).
