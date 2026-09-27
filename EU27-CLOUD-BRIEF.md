# EU27.cloud

Plans for data-centre sovereignty in every EU member state.

**eu27.cloud** is an independent playbook: country-by-country notes on where compute can be built, powered, permitted, owned, and operated under EU law — not another “EU region of a US cloud” page.

This repo is a seed. Replace placeholders as the project takes shape. This is **not** an official European Commission, EURid, or Gaia-X property.

## Why this exists

The EU is trying to triple data-centre capacity, stand up acceleration zones in member states, and score cloud/AI services on sovereignty levels (residency, ownership, operations, supply chain). Capacity without jurisdiction is only half the problem. An EU rack owned or compelled from outside the Union is not the same as a sovereign one.

EU27.cloud tracks the boring layer that actually decides outcomes:

- sites and grid connection
- water, heat reuse, and permitting
- who owns the building, the operator, and the keys
- what “sovereign” means at CADA / Gaia-X / national assurance levels
- what each of the 27 can realistically host in the next 5–7 years

## Scope

| In | Out (for now) |
| --- | --- |
| EU-27 member states | UK, EFTA, candidates (sidebar only) |
| Data centres, power, water, heat | Consumer SaaS reviews |
| Ownership, jurisdiction, ops | Vendor marketing copy |
| Public-sector and critical-infra use cases | Building a hyperscaler |
| Country playbooks + a cross-EU map | Pretending to be the Commission |

**EU-27** (27 countries, post-Brexit):

Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden.

If the Union enlarges, the brand stays; the dataset gains a row.

## Working definition of sovereignty

Residency ≠ sovereignty. Bytes in Frankfurt on a US-parent platform can still sit under extraterritorial process.

Treat sovereignty as stacked, not binary:

1. **Location** — infrastructure and data in the Union (baseline).
2. **Operations** — EU-based staff, support, and break-glass; no silent third-country admin path.
3. **Legal entity** — EU-established operator; control and financing not dominated by a third-country parent.
4. **Supply chain** — known silicon, firmware, orchestration, and key custody; auditable.
5. **Energy and place** — the site can actually be built and powered under local law without becoming a grid parasite.

Map these to whatever label the Commission, a member state, or Gaia-X is using that year. Do not invent a competing certification scheme unless the project later decides to.

## Repo layout (suggested)

```text
eu27.cloud/
├── README.md                 ← this file
├── LICENSE                   ← pick one (see below)
├── CONTRIBUTING.md
├── data/
│   ├── countries/            ← one markdown or YAML file per member state
│   ├── glossary.yml
│   └── sources.yml
├── playbooks/
│   ├── how-to-read-a-country.md
│   └── sovereignty-checklist.md
├── notes/
│   └── decisions.md          ← architecture / scope decisions
└── site/                     ← later: static site for eu27.cloud
```

Start with `data/countries/` and a shared checklist. The website can wait.

## Country file template

Copy into `data/countries/de.md` (use ISO 3166-1 alpha-2 filenames).

```markdown
# Germany (DE)

Status: draft
Last reviewed: YYYY-MM-DD
Sources: []

## Snapshot
- Installed / announced DC capacity:
- Grid constraint (high / medium / low):
- Typical permit timeline:
- Acceleration zone designated? (CADA):
- Dominant operators (EU-hq vs extra-EU):
- Heat-reuse / water notes:

## Sovereignty picture
- What a Level-1 workload can use today:
- What a high-assurance (approx. Level 3–4) workload can use today:
- Known gaps (ownership, ops, silicon, energy):

## Plan sketch (5–7 years)
- Where new MW can land without wrecking the grid:
- Policy or market moves that would change the map:
- Open questions:

## Sources
- Primary (laws, TSO, ministry, Commission):
- Secondary:
```

Keep tone dry. Link sources. Separate fact from judgment.

## Cross-cutting questions (every country)

- Where is spare **transmission** and **generation**, not just cheap land?
- Who issues the permit stack (planning, environment, water, energy)?
- Is there a **data-centre acceleration zone** or equivalent fast track?
- Can waste heat actually connect to a district network?
- Which operators are EU-headquartered *and* operationally isolated?
- What does the public sector already procure, and at which assurance level?
- What would “balanced capacity” mean here vs Frankfurt / Dublin / Amsterdam concentration?

## Principles

- **Independent.** No official-looking crest, no “europa” impersonation.
- **Cite.** Prefer primary documents over LinkedIn threads.
- **Country-first.** EU policy is the frame; the unit of work is a member state.
- **Honest about US and other extra-EU capacity.** It exists, it will stay, and it is not the same as sovereign capacity.
- **Energy is in scope.** A sovereign DC that cannot connect is a PDF.
- **No sovereign-washing.** If a product is an EU region of a third-country parent, say so.

## Name and domain

- Product: **eu27.cloud**
- Spoken: “E-U twenty-seven dot cloud”
- Register via an EU registrar; host DNS in the EU; turn on DNSSEC.
- Parking line: *Plans for sovereign compute in every member state.*

Optional shields if cheap: `eu-27.cloud`, `eu27.eu` (EEA eligibility), `eu27dc.cloud`.

## Near-term build order

1. Register the domain and put a one-pager live.
2. Fill the glossary (`CADA`, acceleration zone, assurance levels, data embassy, CLOUD Act, SecNumCloud, C5, etc.).
3. Draft 3 country files that stress-test the template: **IE** (capacity magnet), **DE** (industry + grid), **EE** or **LU** (digital state / data embassy).
4. Then the rest of the 27, shallow first, deep second.
5. Only then a map UI.

## License

Pick before the first external contribution:

- Content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) is a reasonable default for playbooks.
- Code (if any): MIT or EUPL-1.2.

Add a `LICENSE` file. Do not leave this blank if others will commit.

## Disclaimer

Not legal advice, not an official EU position, not a certification. Capacity numbers go stale; always check the source date. Jurisdiction analysis is a sketch, not an opinion of counsel.
