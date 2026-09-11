# Sovereign Data Centers for European States

Planning models and write-ups for national sovereign government data center networks, one per EU member state.
The Netherlands (`RijksCloud`) is the worked reference case; the other 26 are generated from it by a
parameterized model and are meant to be refined country by country.

## Live site

**https://sovereign-data-centers.vercel.app**

Deliberately **not indexed** by search engines. The capacity figures are openly scaled placeholders, and
the legal and regulatory entries are assertions about what 27 real jurisdictions require, researched from
public policy documents by one person and **not yet checked against primary sources**. That is fine for a
research repository that says so; it is not fine for something search engines present as authoritative.
Indexing is gated on the verification work in [`VERIFICATION.md`](VERIFICATION.md), as is the
`eu27.cloud` domain.

Corrections are welcome — there is a data-correction issue template.

## Deployment

Live at **https://sovereign-data-centers.vercel.app**, on the Vercel project
`pieteradejongs-projects/sovereign-data-centers`.

```
./run.sh deploy     # refuses a dirty tree or a non-main branch, runs ./test.sh, then deploys
```

Three things about this deployment are easy to get wrong, so they are written down:

- **Deploys are manual.** The Vercel GitHub App is not installed on the account, so the project
  is not linked to the repository and **a push does not ship anything**. A stale site is the
  failure mode to watch for, and `./run.sh deploy` exists so shipping is one command rather than
  a remembered incantation.
- **`vercel.json` sets `github.silent`**, so there is no deploy status on the commit. Check the
  Vercel dashboard, not GitHub.
- **`.vercelignore` is read *instead of* `.gitignore`**, not in addition to it. Every rule that
  matters has to be repeated there — `**/contacts/` first among them (#46), and `cache/`, which
  would otherwise upload the entire fetched corpus with the source. `./run.sh deploy` checks that
  last one before shipping.

### The three stages

| Stage | What it is | Gated on |
|---|---|---|
| 1 — `*.vercel.app`, `noindex` | where it is today | nothing; done 2026-09-07 |
| 2 — indexing | delete the two `Disallow` lines from `web/public/robots.txt` | tier-1 cells sourced for all 27, Eurostat re-pulled |
| 3 — `eu27.cloud` | custom domain | the sampling audit's measured error rate |

The domain is deliberately unofficial-sounding so the site is not mistaken for an EU
institution's (#50); it was still available at $9.99/yr when last checked, 2026-09-11.

## Verification

The legal and regulatory columns assert what 27 real jurisdictions **require**. That is a
different kind of claim from a scaled capacity placeholder, and it is the gate on everything
public-facing (#25).

```
./run.sh sources    # coverage; currently 2 of 189 cells
./run.sh fetch      # retrieve the source documents into cache/
```

`model/sources.csv` is the ledger: one row per sourced claim, carrying **the sentence on the page
that supports the cell**. A URL only shows a page exists — it cannot show the page still says what
it said, which is why the documents themselves are fetched and hashed (`SOURCES.md`).

Tier 1 — `legal_instrument`, `data_classification`, `certification_scheme` — asserts a legal
obligation and admits nothing but the instrument itself. Tier 2 describes what a state runs, buys
or depends on, and takes an official government page. The three ordinal columns are the author's
judgements, **disclosed and never cited**; a source row for one is a validation error.

`COVERAGE_FLOOR` in `tests/test_sources.py` is a ratchet: it moves in the same commit as the rows
it counts, so progress cannot be silently undone. Method is in [`VERIFICATION.md`](VERIFICATION.md),
endpoints in [`SOURCES.md`](SOURCES.md).

## Layout

```
init.sh / run.sh / test.sh   set up, run, and fully test the project
model/
  assumptions.csv            shared engineering/economic defaults (the Dutch "working assumptions")
  eu27_parameters.csv        one row per country: population, GDP, public-admin employment, power price,
                             renewables, land, flags, existing gov cloud, digital ID, IXPs, and the
                             legal/regulatory posture columns (certification, classification, procurement)
  sources.csv                the verification ledger: one row per sourced claim, with the quote
  sources.py                 validates the ledger and reports coverage (./run.sh sources)
  scaling_rules.csv          how each workload class scales from the NL baseline (weights, floors, frontline multiplier)
  migration_phases.csv       workload class -> migration phase
  capacity_model.py          workloads -> servers -> racks -> MW -> sites -> CAPEX/OPEX, for any country dir
  country_data.py            assembles every fact about a country into one dict (the single source)
  generate_countries.py      builds countries/<ISO>/ inputs + GOAL.md for all 27, runs the model, writes SUMMARY.md
  export_json.py             writes web/public/data/eu27.json from the same dict
  export_artifacts.py        renders the tracked per-country poster and briefing PDF (./run.sh artefacts)
  eu27_results.csv           one result row per country (generated)
book/                        print edition and per-country PDF briefs (typst); see book/README.md
OUTREACH.md                  institutional distribution map, one entry per member state
countries/
  SUMMARY.md                 cross-country table (generated)
  ARTEFACTS.csv              sha256 of every tracked poster and PDF, and of the bundle it came from
  NL/                        the reference case: hand-written GOAL.md, xlsx model, inputs, TODO, plan,
                             FRONTIER-MODEL.md (authored companion note, not generated), and the
                             AI-generated concept infographic (see ASSETS.md)
  DE/ FR/ ... (x26)          params.csv, workloads_inputs.csv, region_allocation_inputs.csv (generated inputs, edit freely)
                             GOAL.md (generated 12-section brief), facility_summary.csv,
                             region_allocation_output.csv, migration_phases.csv (outputs),
                             <ISO>-infographic.png and <ISO>-briefing.pdf (tracked deliverables)
web/                         React + Vite visualization app; reads the JSON bundle, no server
tests/                       stdlib unittest suite for the model and the data
DECISIONS.md                 why every choice was made
CHANGELOG.md                 what changed and when
VERIFICATION.md              the source-verification workstream: schema, tiered rule, where it stands
```

Python is the source of truth. The markdown briefs, the JSON bundle, the app and the exports are all
renderings of one `country_data.build()` dict, so they cannot disagree with each other.

## Running

```
./init.sh                                   # set up from scratch (checks tools, installs, builds data)
./run.sh                                    # dev server on http://localhost:5173
./run.sh data                               # regenerate country files, briefs and the JSON bundle
./run.sh help                               # every command
./test.sh                                   # the full gate: model, types, lint, unit, build, e2e, a11y
./run.sh artefacts                          # re-render the tracked posters and briefing PDFs
./run.sh sources                            # verification-ledger coverage
./run.sh fetch                              # fetch source documents into cache/ (see SOURCES.md)
./run.sh deploy                             # full gate, then deploy to Vercel production
./run.sh export                             # 27 standalone A4 country briefs (PDF)
./run.sh book                               # typeset the A5 print edition
```

`export` and `book` need typst (`brew install typst`), and write into `book/build/`, which is
gitignored — that build output is never committed (`DECISIONS.md` #41).

`artefacts` is the other, separate pipeline: headless Chrome renders `<ISO>-infographic.png` and
`<ISO>-briefing.pdf` into each country directory, and **those two are tracked deliverables**
(#24, #51). They are byte-reproducible (#53), and `countries/ARTEFACTS.csv` records the data
bundle each was rendered from so the test suite can tell when they have gone stale (#52). Needs
Chrome and `npm`.

The model on its own, without the app:

```
python3 model/capacity_model.py NL          # one country
python3 model/capacity_model.py --all       # all, refreshes model/eu27_results.csv
python3 model/generate_countries.py         # regenerate the 26 derived countries from NL + parameters
```

Standard library only. `capacity_model.py` reproduces the Dutch xlsx exactly (5,691 servers, 14.2 MW design,
EUR 339 m CAPEX) when run on `countries/NL/`.

## Method

Every country inherits the Dutch assumption set (`model/assumptions.csv`) and overrides only what is
observably different: the Eurostat non-household electricity price and the minimum number of in-country sites
(2 for LU/MT/CY, 4 for DE/FR/IT/ES/PL/RO, 3 otherwise). Workload demand is the Dutch workload table scaled
per class by a blend of population, public-administration employment and GDP (`model/scaling_rules.csv`),
with a floor for small states (an identity platform or a SOC does not shrink linearly with population) and a
multiplier on defense/security for frontline states. Regions are first-pass geographic hypotheses that
encode only the obvious constraints; they are placeholders for the scored site selection described in
`countries/NL/TODO.md` workstream A.

The write-ups are generated, and say so at the top. To keep hand edits to a country's `GOAL.md`, rename it
(e.g. `GOAL.md` -> `ANALYSIS.md`) or stop running the generator for that country; the generator only ever
rewrites `GOAL.md`, `params.csv`, `workloads_inputs.csv` and `region_allocation_inputs.csv`, never `NL/`.

## What the first pass shows

- The EU-27 "sovereign core" tier is small: ~306 MW design load, ~125k servers, ~EUR 7.2 bn CAPEX,
  ~EUR 0.7 bn/yr OPEX across 86 sites. Germany alone is ~60 MW; eight states are under 3 MW.
- For states under ~3 MW, three in-country sites means sub-1 MW rooms, which is a closet, not a data center.
  The Dutch 3-region rule does not survive contact with Estonia, Slovenia or Luxembourg; those cases push
  toward fewer, hardened in-country sites plus an out-of-country reserve, i.e. the EU federation layer that
  is deliberately out of scope for now (Dutch `GOAL.md` section 16).
- Power price, not hardware, separates the OPEX outcomes: Ireland and Cyprus pay 3x Finland per MWh.
- Seven states have frontline exposure (EE, LV, LT, PL, FI, RO, BG); five have no live hyperscaler region and
  therefore no in-jurisdiction commercial tier for the hybrid model.

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

Same as the Dutch case, only more so: every input is a working assumption or a scaled placeholder, the
electricity prices are 2025-S2 band-IC averages rather than negotiated tariffs, and public-administration
employment is Eurostat NACE section O (excludes public health and education). The per-country sovereign-cloud
and digital-ID entries were researched in September 2026 and will date.

**The legal and regulatory entries are a different kind of claim from the rest.** Capacity figures are
openly scaled placeholders, and the "working assumption" framing covers them honestly. The certification
schemes, classification ladders and procurement routes are assertions about what real jurisdictions
actually require, and **187 of the 189 have not been checked against primary sources**. Two have:
`./run.sh sources` prints the live figure, and `model/sources.csv` names exactly which, with the
quote that supports each. Assume any given entry is unverified unless the ledger says otherwise.

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

## Reference case

`countries/NL/GOAL.md` is the full write-up of the design philosophy, physical/logical architecture,
sovereignty stack, threat model and open questions. Read it first; the generated country files assume it.
