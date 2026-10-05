# Structured hosting: operators as entities

The design for decision #96. Status: **planned, not built.** What is built is #95: hosting printed per
holding, and a generated EU-27 overview.

## Why

Hosting is one free-text field per holding today, for example "In 2015 IBM Svenska AB took over
Transportstyrelsen's IT operations…". A reader can see it, but nothing can be computed from it:

- "Which private or non-EU firms run state registers, and in how many states?" needs every row read by
  hand.
- `foreign_dependency` is a label an agent applies and a second model reviews (#79). Seven of eight
  unreviewed "Dependent" labels did not survive review. A label that follows from sourced links is easier
  for a third party to check than a judgement.

The idea is borrowed from Palantir's Ontology: typed objects, typed properties and typed links, with every
view reading the one layer. This project's provenance already exceeds it, with a quote and a hash per
property. What it lacks is the organisation as an object, and links between organisations. The platform
weight is not copied: three stdlib-read CSV files are enough.

## Schema

Separate tables, not new columns on `national_data.csv`:

- One holding can involve several organisations. DK's CPR is state-owned but operated by DXC.
- One organisation spans several states. DXC, IBM and Microsoft each run registers in more than one.
- `national_data.read_rows` rejects any header change.

| File | Columns |
|---|---|
| `model/organisations.csv` | `org_id` (slug), `name`, `seat` (ISO-2, or a non-EU country code), `sector` ∈ {state, state_owned, private, eu_body, intergovernmental}, `url` |
| `model/hosting.csv` | `iso`, `record_class`, `role` ∈ {operator, processor, host, cloud}, `org_id`, `model` ∈ {own_dc, state_shared_service, outsourced_operation, public_cloud, private_cloud}, `location` ∈ {in_country, eu, non_eu} |
| `model/org_links.csv` | `child`, `relation` ∈ {owned_by, subsidiary_of, controlled_by}, `parent` |

## Claims

- **New record kinds:** `record:<ISO>:<class>:host_org`, `:host_model` and `:host_location`, in
  `provenance.RECORD_KINDS`. The role goes in the citation's locator.
- **A new namespace, `org`:** `org:<id>:seat`, `org:<id>:sector` and `org:<id>:parent`, in
  `provenance.NAMESPACES`, with `FLOORS["org"] = 0` in `tests/test_provenance.py`.

## Staging, review, admission

The same path as every other claim: staging is never data.

1. **Staging.** Agents write `model/research/hosting/<ISO>.json` and
   `model/research/organisations/<org_id>.json` in the existing claim shape (url, quote, quote_english,
   value). `research.claims()` is extended so `verify` fetches and hashes them.
2. **Review (#79).** Every categorical value (sector, seat, model, location, relation) needs an agreeing
   verdict from an independent reviewer, in `model/research/hosting_review/` or `org_review/`.
   `research.dependency_verdict` is generalised to `agreed(kind, key)`. With no verdict, or a disputed
   one, the field stays empty.
3. **Admission.** `research.admit_hosting()`, called from `admit()`, writes only rows whose quote verified.
   The three CSVs join `model/reproduce.py` `REGISTERS`, so `./run.sh admit --check` covers them (#84).
4. **Validation.** A `model/hosting.py` validator checks the enums, that every `org_id` is known, that the
   links are acyclic, and that every cited host is in `model/sources/authorities.csv` (#83).

## Backfill

- `python3 model/hosting.py candidates` turns the 71 existing hosting quotes, plus `holder`, into
  **candidate staging only**. Nothing is admitted from a candidate directly.
- Agents re-cite each candidate. Ownership links need their own sources: annual reports, company
  registers, procurement notices.
- Then a review round, `verify`, `admit` and `admit --check`.

## Computed views

These are new sections in the EU-27 overview. They carry `host_org` and `org:*:parent` claims, so they are
new printed facts. `factcheck.facts()` must learn to walk `bundle["infrastructure"]` before they print.

- **Operators across states:** each organisation, its ultimate parent, and the states and holding classes
  it touches.
- **Operator-type mix per state.**

## Derived dependency

- `derive(iso, cls)` walks each host organisation to its ultimate controller:
  - a state body of the same state: national;
  - private with an EU seat: eu_provider;
  - a seat outside the EU: non_eu_provider;
  - roles that disagree: mixed;
  - any unsourced link: **unknown, never national.**
- `hosting.py reconcile` reports, for each holding, the reviewed label against the derived value. **No
  printed fact changes silently.**
  - If they agree, the derivation is recorded as corroboration.
  - If the label is empty and the derivation is fully sourced, the derived value becomes a new fact,
    through `/factcheck`.
  - If they differ, the label is kept and a dispute is staged for a review round.

## Risks

- **Placements.** A derived non_eu_provider can move a state's group (`sovereignty.py` reads
  `foreign_dependency`). Diff `python3 model/sovereignty.py` before and after; any placement change needs
  the owner's OK.
- **Ownership chains** are poorly sourced and go stale, especially private-equity owners. The chain stops
  at unknown.
- **Public repo.** Staging and review files are public once committed.
- **Decision numbering.** `tests/test_docs.py` matches only 1–2 digit references. Widen it before #100.
