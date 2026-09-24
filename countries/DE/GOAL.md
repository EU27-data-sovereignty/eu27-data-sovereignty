# Germany - Sovereign Government Data Center Network

> Generated 2026-09-05 by `model/generate_countries.py` from the Dutch reference case
> (`countries/NL/GOAL.md`) and `model/eu27_parameters.csv`. Every number below is a **scaled working
> assumption**, not a sourced figure. Edit the CSVs in this directory and re-run
> `python3 model/capacity_model.py DE` to update the capacity numbers; edit
> `model/eu27_parameters.csv` or `model/scaling_rules.csv` and re-run the generator to update this file.

## Contents

1. [Working thesis](#1-working-thesis)
2. [Starting point](#2-starting-point)
3. [What is structurally different from the Dutch case](#3-what-is-structurally-different-from-the-dutch-case)
4. [Workload demand (scaled from the Dutch baseline)](#4-workload-demand-scaled-from-the-dutch-baseline)
5. [Capacity model output](#5-capacity-model-output)
6. [Proposed geography (first-pass hypothesis)](#6-proposed-geography-first-pass-hypothesis)
7. [Geography and threat notes](#7-geography-and-threat-notes)
8. [Recommendations specific to Germany](#8-recommendations-specific-to-germany)
9. [Open questions](#9-open-questions)
10. [Legal and regulatory posture](#10-legal-and-regulatory-posture)
11. [Current state and provider landscape](#11-current-state-and-provider-landscape)
12. [Migration path and cost](#12-migration-path-and-cost)
13. [Critical national data in scope (Tier 0 / Tier 1)](#13-critical-national-data-in-scope-tier-0--tier-1)

## 1. Working thesis

Germany does not need to become technologically autarkic. It needs enough independently controlled compute,
storage, networking, identity, cryptography and operational capability that the state can continue functioning
when foreign commercial infrastructure is unavailable, politically constrained, compromised, or no longer
trustworthy. The Dutch design rules (sovereignty is a stack, not a building; 3-5 separated regions; dual fibre
paths; no single hardware supplier; a first-class developer platform) are taken as the starting point and
adjusted below for what is structurally different about Germany.

## 2. Starting point

| | |
|---|---|
| Population | 83.58 m (1 January; Eurostat tps00001, 2025) |
| GDP | EUR 4,530 bn (current prices; Eurostat nama_10_gdp, 2025) |
| Public administration employment (NACE O) | 3,041 k (Eurostat nama_10_a64_e, 2023; value does not reproduce the source, under review) |
| Non-household electricity price | 226.4 EUR/MWh (band IC, excl. VAT; Eurostat nrg_pc_205, 2025-S2) |
| Renewables in electricity | 54.1% (Eurostat nrg_ind_ren, 2024) |
| Land area | 353,296 km2 (Eurostat reg_area3, 2019) |
| Live hyperscaler regions in-country | 6 |
| Existing government / sovereign cloud | Deutsche Verwaltungscloud (DVC) federated launched Mar 2025 (IT-Planungsrat/govdigital/FITKO); Bundescloud (ITZBund); Delos Cloud (SAP/Arvato on Azure, BSI-aligned); openDesk (ZenDiS); STACKIT/IONOS/T-Cloud; BSI C5 |
| National digital identity (anchor workload) | Online-Ausweis eID + BundID/DeutschlandID |
| Internet exchange / cable landings | DE-CIX Frankfurt (world's largest) Hamburg Munich; Norden/Sylt/Rostock landings |

Relative to the Dutch baseline: population x4.63, public administration x4.25,
GDP x3.87. Resulting design load: x4.28 the Dutch figure.

## 3. What is structurally different from the Dutch case

- **Expensive power (226 EUR/MWh vs. EU average ~184).** Power is the dominant OPEX line; free cooling, heat reuse, and siting near renewables or nuclear baseload move the economics more than server choice does. The model's power OPEX line is the number to attack first.
- **Dense hyperscaler presence (6 live regions).** Commercial capacity, fibre and skills exist in-country; the sovereign core can stay lean and the hybrid model works as designed. The risk is the opposite one: political pressure to declare a hyperscaler region 'sovereign enough' (Dutch GOAL.md section 17: location is not sovereignty).

## 4. Workload demand (scaled from the Dutch baseline)

Scaling weights per workload class are in `model/scaling_rules.csv`; the Dutch rows they scale are in
`countries/NL/workloads_inputs.csv`. Frontline multiplier applied: no.

| Workload | Class | CPU cores | GPU eq. | Storage (PB) | Avail. factor |
|---|---|---:|---:|---:|---:|
| Digital identity / Online-Ausweis eID + BundID | Critical government | 83,400 | 0 | 18.5 | 1.5 |
| Core government applications | Government | 244,100 | 0 | 79.9 | 1.35 |
| Data platforms & analytics | Government data | 148,800 | 344 | 255.0 | 1.25 |
| AI / sovereign model serving | AI | 69,700 | 1984 | 46.4 | 1.3 |
| Defense classified compute | Defense | 139,000 | 1184 | 69.5 | 1.5 |
| Cybersecurity / SOC / telemetry | Security | 99,300 | 144 | 112.9 | 1.4 |
| Scientific / public research | Research | 100,600 | 496 | 77.4 | 1.15 |

## 5. Capacity model output

| Metric | Value |
|---|---:|
| Physical servers | 24,627 (CPU 16,970 / GPU 1,159 / storage 6,498) |
| Rack equivalents | ~770 |
| IT critical load | 40.5 MW |
| Facility load (PUE 1.25) | 50.6 MW |
| Facility design load (+20% headroom) | **60.7 MW** |
| Sites by capacity / recommended | 6 / **6** (minimum 4) |
| Average design MW per site | 10.1 MW |
| Total CAPEX | **EUR 1,444 m** (facility EUR 607 m, IT EUR 709 m, network EUR 128 m) |
| Annual energy | 443,147 MWh |
| Annual OPEX | **EUR 165 m / yr** (power EUR 100 m, non-power EUR 65 m) |

Full table: `facility_summary.csv`.

## 6. Proposed geography (first-pass hypothesis)

Site posture: standard. Separation target: 50-100 km failure domains, dual fibre paths, distinct grid feeds.

| Region | Role | Share | Design MW | Racks | Facility CAPEX | Notes |
|---|---|---:|---:|---:|---:|---|
| Frankfurt - Rhine-Main | Primary civil cloud | 36% | 21.9 | 277 | EUR 218 m | DE-CIX, ITZBund estate; grid saturated - expect multi-year connection lead time. |
| Berlin - Brandenburg | Sovereign secondary | 18% | 10.9 | 138 | EUR 109 m | Federal ministries, AWS ESC and STACKIT prove grid headroom in the east. |
| Munich / Bavaria | Defense / industrial | 18% | 10.9 | 138 | EUR 109 m | Defense-industrial cluster, Bundeswehr IT; southern separation. |
| Hamburg / North | Government / continuity | 18% | 10.9 | 138 | EUR 109 m | Wind surplus, North Sea cable landings (Norden/Sylt). |
| Leipzig - Saxony | Strategic reserve | 10% | 6.1 | 77 | EUR 61 m | Post-coal land and grid; reserve/expansion. |

These regions encode only the obvious constraints (capital estate, second metro, distance from the frontier,
fault or flood zone). They are to be replaced by the scored site selection in workstream A of the Dutch
`TODO.md` (grid capacity, flood risk, fibre, failure independence, physical security, land, cooling).

## 7. Geography and threat notes

Low seismic; Ahr/Rhine/Elbe floods (2021); Frankfurt grid saturated (multi-year waits) with headroom in Brandenburg/east; 3rd-highest EU power price; north-south grid bottlenecks; LNG gas import; NATO; sabotage/drone incidents at DCs 2024-25

## 8. Recommendations specific to Germany

1. **Anchor on Online-Ausweis eID + BundID.** Digital identity is the workload that, if it fails, stops every other
   government service; it belongs in the sovereign core first, active-active across at least two regions.
2. **Build on the existing estate, do not replace it.** Deutsche Verwaltungscloud (DVC) federated launched Mar 2025 (IT-Planungsrat/govdigital/FITKO) is the
   institutional starting point; the sovereign core should be its next generation, with one governance owner.
3. **Site posture: standard.** Standard Tier III+ with 50-100 km separation is sufficient; spend the hardening budget on supply-chain assurance instead.
4. **Power strategy.** Power is the binding constraint; treat grid connection lead time and on-site generation as first-order site criteria.
5. **Hybrid tier.** Use in-country commercial regions for the non-critical tier, but keep identity, defense, security telemetry and registries in the sovereign core.

## 9. Open questions

- Replace scaled workload rows with real ministry/agency demand (see `countries/NL/CAPACITY_PLAN.md` for the method).
- Which body owns the sovereign core, and how are agencies compelled or incentivised to migrate?
- Which regions federate with EU partners for mutual disaster recovery, and which stay national-only?
- Site-size assumption: is the 12 MW planning unit right for Germany, or should sites be larger?

## 10. Legal and regulatory posture

> **These entries are unverified research, not legal advice.** They were compiled in September 2026 from
> public policy documents and have **not** been checked against the primary instruments. The maturity,
> certification-strength and dependency ratings below are the author's judgements, not official or
> measured ratings. Do not rely on this section for a procurement or policy decision. Corrections are
> welcome via the repository's issue template.

Every member state shares one baseline: GDPR for personal data, NIS2 for the security of essential
entities, the Data Act for switching and access, and the EU Cloud Services Scheme (EUCS) still unresolved
on the sovereignty requirements that would matter most here. That baseline governs *processing*. It does
not, on its own, place infrastructure under national control - which is the gap a sovereign core exists
to close.

| | |
|---|---|
| Governing instrument | Onlinezugangsgesetz; IT-Planungsrat Deutsche Verwaltungscloud-Strategie (DVC) |
| Cloud certification | BSI C5 (Cloud Computing Compliance Criteria Catalogue) |
| Data classification | Verschlusssachenanweisung (VSA): VS-NfD / VS-Vertraulich / Geheim / Streng Geheim |
| Procurement route | Beschaffungsamt des BMI and Kaufhaus des Bundes; ITZBund as federal operator |

BSI C5 (Cloud Computing Compliance Criteria Catalogue) is among the most demanding cloud assurance regimes in the Union. The sovereign core inherits a mature control baseline and, more usefully, an existing qualification path that suppliers already know how to pass.

The classification ladder is the practical control: it decides which tier of data may leave the
jurisdiction at all, and it should be mapped onto the four migration phases in section 12 before any
procurement starts. Buying capacity before deciding what may sit on it is how sovereign programmes end up
with expensive infrastructure hosting the wrong workloads.

**Foreign jurisdiction exposure.** Delos Cloud (SAP/Arvato on Azure, BSI-aligned) for federal workloads; M365 use contested by the Datenschutzkonferenz

Dependency on US hyperscalers is **moderate**: national arrangements carry part of the estate, and the sovereign core extends an existing position rather than reversing one. Under the US CLOUD Act and FISA 702, a provider subject to US jurisdiction can face a lawful
order for data it holds, regardless of where the data physically sits. Data residency in-country is
therefore necessary but not sufficient; what matters is who holds the keys and who can be compelled.

## 11. Current state and provider landscape

| | |
|---|---|
| Government cloud | Deutsche Verwaltungscloud (DVC) federated launched Mar 2025 (IT-Planungsrat/govdigital/FITKO); Bundescloud (ITZBund); Delos Cloud (SAP/Arvato on Azure, BSI-aligned); openDesk (ZenDiS); STACKIT/IONOS/T-Cloud; BSI C5 |
| Maturity | federated (author's rating, not an official one) |
| Digital identity | Online-Ausweis eID + BundID/DeutschlandID |
| In-country commercial regions | 6 |
| Interconnection | DE-CIX Frankfurt (world's largest) Hamburg Munich; Norden/Sylt/Rostock landings |

A federated government cloud is already in production. The open question is consolidation and governance, not construction.

Against that starting point, the modelled sovereign core is **60.7 MW of design load across
6 site(s)**, or roughly 24,627 servers. The gap between what runs today and that
figure is the actual programme; the capacity model in sections 4-6 sizes the destination, not the journey.

## 12. Migration path and cost

Workloads are sequenced by how badly loss of control would hurt, not by how easy they are to move. The
phases below are derived from the workload classes in `model/migration_phases.csv`; per-country figures
are in `migration_phases.csv` in this directory.

| Phase | Scope | Servers | Design MW | CAPEX | Cumulative | Hybrid-eligible |
|---|---|---:|---:|---:|---:|---|
| 1 | Sovereign core | 7,476 | 14.7 | EUR 281 m | 19% | no |
| 2 | Security and defense | 7,317 | 18.8 | EUR 456 m | 51% | no |
| 3 | State record | 5,124 | 10.6 | EUR 267 m | 70% | no |
| 4 | Elective | 4,710 | 16.6 | EUR 440 m | 100% | yes |

**Phase 1 is the number that matters: EUR 281 m for 14.7 MW,
19% of total CAPEX.** That is the floor - identity and core government
services - below which no hybrid arrangement helps, because these workloads cannot be foreign-hosted under
any sovereignty posture worth the name. It is also, notably, a small fraction of the full build: sovereignty
for the workloads that define the state is cheaper than the headline figure suggests.

Phases 2 and 3 follow on clearance and legal constraints rather than cost. Phase 4 can use in-country commercial capacity (6 live region(s)) under sovereign-held keys, which is what keeps the sovereign core small.

Sequencing caveat: the CAPEX split above apportions facility cost by each phase's share of IT load, which
assumes phases are built into a shared facility programme rather than as separate buildings. Building
phase 1 alone, on its own site, costs disproportionately more - the facility is largely a fixed cost.

## 13. Critical national data in scope (Tier 0 / Tier 1)

The workloads above are sized in servers and megawatts. This section says what they would *hold*:
the records whose loss or foreign control is the reason a sovereign core is argued for at all. The
tiering is by consequence of loss rather than by department, and is set out in
`TIER0-TIER1-SIZING.md` - tier 0 is the identity spine, without which the state cannot say who
exists; tier 1 is the enforceable relationship between citizen and state.

**0 of 15 record classes recorded for Germany.** The register is
`model/national_data.csv`; run `./run.sh registers` for coverage across all 27.

| Tier | Record class | Register | Held by | Official description |
|---|---|---|---|---|
| 0 | Civil registry core | *not yet recorded* |  |  |
| 0 | Facial biometric | *not yet recorded* |  |  |
| 0 | Fingerprint biometric | *not yet recorded* |  |  |
| 0 | Breeder document scans | *not yet recorded* |  |  |
| 0 | Document issuance history | *not yet recorded* |  |  |
| 0 | Digital identity credentials | *not yet recorded* |  |  |
| 0 | Authentication audit log | *not yet recorded* |  |  |
| 0 | Electoral roll entry | *not yet recorded* |  |  |
| 1 | Tax | *not yet recorded* |  |  |
| 1 | Benefits & pensions | *not yet recorded* |  |  |
| 1 | Land & property registry | *not yet recorded* |  |  |
| 1 | Judicial & criminal justice | *not yet recorded* |  |  |
| 1 | Education | *not yet recorded* |  |  |
| 1 | Business registry | *not yet recorded* |  |  |
| 1 | Vehicle & licensing | *not yet recorded* |  |  |

A blank row means this repository has not yet researched that register. It is not a statement that the country holds no such data. Tiers 2 (health records, imaging) and 3 (genomics, archives, video retention, geospatial) are out of scope: they hold most of the bytes, but Tiers 0 and 1 hold the sovereignty.
