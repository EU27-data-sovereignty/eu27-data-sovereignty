# Belgium: critical data holdings and sovereign hosting

> Generated 2026-09-29 by `model/generate_countries.py` from the content model (`model/document.py`). The same document is typeset as the country PDF and rendered on the web.
>
> **Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.** A value that no checked source supports is withheld and shown as a gap. A gap means not yet sourced, never that the thing does not exist. A value in *italics* is withheld.

## Contents

1. [Data-sovereignty placement](#1-data-sovereignty-placement)
2. [Fundamentals](#2-fundamentals)
3. [Critical data holdings, by priority](#3-critical-data-holdings-by-priority)
4. [Foreign-dependency exposure](#4-foreign-dependency-exposure)
5. [Legal and institutional posture](#5-legal-and-institutional-posture)
6. [Capacity](#6-capacity)
7. [Research still open](#7-research-still-open)

## 1. Data-sovereignty placement

> Not demonstrated. Confidence: Low. With the evidence still open, Belgium could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4] |
| State-controlled national eID | Yes[^s5][^s6] |
| Government data centres | Yes[^s7] |
| Government cloud in operation | Yes[^s8] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Belgium described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 11.955 million[^s9] |
| GDP, current prices | 642.0 EUR bn[^s10] |
| Public administration employment (NACE O) | 459.5 thousand[^s11] |
| Non-household electricity price | 186.6 EUR/MWh[^s12] |
| Renewables share of electricity | 34.3 %[^s13] |
| Land area | 30 452 km²[^s14] |

## 3. Critical data holdings, by priority

The holdings Belgium cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 20 of 39 holding classes have a verified source; 2 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Rijksregister van de natuurlijke personen (National Register of Natural Persons), the central database of identification data of all registered persons[^s15][^s6] | The National Register is managed by the Directorate-General Identity and Civil Affairs of the FPS Interior[^s6][^s16] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | ID-card photos are stored and visible in the National Register[^s17][^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s17][^s5] | — | — | — |
| Critical | Breeder document scans (tier 0) | DABS: a central database holding all civil status deeds, replacing the municipal and consular registers[^s19][^s20] | DABS is governed by a DABS Management Committee responsible for its set-up and management[^s19][^s20] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | FAS audit trail of authentication logs, kept for 10 years[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Register van de Identiteitskaarten: a permanent inventory of the identity cards produced and issued in Belgium[^s22][^s6] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Federal Authentication Service (FAS)[^s21] | DG Simplification and Digitization (FPS Policy and Support, BOSA)[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | Belgium Root CA (BRCA), the top of the government CA hierarchy[^s3][^s4] | The Belgian authorities are the certification service provider responsible for the Belgium Root CAs[^s3][^s4] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | kadastrale documentatie of the AAPD (cadastral documentation of the General Administration of Patrimonial Documentation)[^s23] | Algemene Administratie van de Patrimoniumdocumentatie (AAPD) (General Administration of Patrimonial Documentation)[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Centraal Strafregister (Central Criminal Register)[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Evibel is the internal database of the immigration service, to be replaced by eMigration[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | Pensioenkadaster (Pension Register)[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Kruispuntbank van Ondernemingen (Crossroads Bank for Enterprises)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | UBO-register (register of ultimate beneficial owners)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Kruispuntbank van de Voertuigen (Crossroads Bank for Vehicles)[^s29] | Directie voor de Inschrijving van Voertuigen van de Federale Overheidsdienst Mobiliteit en Vervoer (DIV, Vehicle Registration Directorate of FPS Mobility and Transport)[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | Centraal Wapenregister (Central Weapons Register)[^s30] | een dienst van de Federale Politie (a service of the Federal Police)[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | NBB Securities Settlement System (NBB-SSS)[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | ASTRID-radionetwerk (ASTRID TETRA radio network)[^s32] | ASTRID (naamloze vennootschap van publiek recht, public-law company)[^s33] | *Not stated in sources* | more than 2 million radio contacts per day[^s32] |
| High | Crisis management and civil protection (tier 1) | BE-Alert (the government's alerting system)[^s34] | *Not yet sourced* | *Not stated in sources* | more than 1 million registered addresses[^s34] |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | LED, de Leer- en ErvaringsbewijzenDatabank (Learning and Experience Certificates Database)[^s35] | Agentschap voor Kwaliteitszorg in Onderwijs en Vorming (Agency for Quality Assurance in Education and Training)[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 19 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 19 |

## 5. Legal and institutional posture

0 of 8 posture entries have a verified source. The others were researched from public policy documents but are withheld here until each is checked against the governing instrument.

| Dimension | Position |
|---|---|
| Governing instrument | *Not yet sourced* |
| Sovereign or government cloud | *Not yet sourced* |
| Cloud certification | *Not yet sourced* |
| Data classification | *Not yet sourced* |
| Procurement route | *Not yet sourced* |
| National digital identity | *Not yet sourced* |
| Internet exchange | *Not yet sourced* |
| Hyperscaler regions in country | *Not yet sourced* |

## 6. Capacity

> Not yet sized. Capacity for Belgium will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 2 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Belgium without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Electoral roll entry (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Statutory health insurance (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1340 facts are printed, 3340 values are withheld as gaps, and 72 are withheld as disputed.

### How sources were found

Research agents, one per member state, looked for each critical holding and each indicator. Each claim needed a verbatim quote of 8 to 60 words from an exact URL. Nothing an agent returned was used until it passed the mechanical checks below. Agent output is staged separately and is never rendered.

| Quote check of the first research runs | Claims |
|---|---:|
| exact | 2138 |
| loose | 20 |
| not_found | 107 |
| fetch_failed | 251 |

A vetting run then re-examined every printed fact, and after it the gaps. It looked for a better source, for newer information and for any source that disagrees. Each of its findings was judged by a blind reviewer, shown the quote and URL but never the proposed value. Runs: wf_1c6b8bb6-450. Reviewer model: claude-opus-5-5, the same model as the researcher.

| Vetting outcome | Findings or items |
|---|---:|
| below_T2 | 6 |
| corrected_withheld | 6 |
| corroborated | 261 |
| disputed | 10 |
| filled_gap | 365 |
| holding_not_established | 41 |
| no_better_found | 461 |
| not_reached | 201 |
| not_verified | 178 |
| review_disagreed | 172 |
| same_source | 9 |
| superseded_higher_tier | 23 |
| superseded_later_same_authority | 3 |

Every cited source is re-fetched periodically and each quote looked for again. A fact whose quote has vanished, or whose source is gone, is withheld as disputed. A refusal to serve the page changes nothing.

| Latest recheck | Sources |
|---|---:|
| changed_quotes_present | 373 |
| gone | 3 |
| quote_vanished | 3 |
| unchanged | 306 |
| unreachable | 6 |

### What must hold for a fact to be printed

- Researched claims (holdings, operators, legal bases, indicators): the cited page or PDF was downloaded and its SHA-256 recorded, and the quoted text was found in the extracted document by literal matching. Every number and date in the printed value was found in the original-language quote; the English wording is a machine summary of the quote unless it appears in it verbatim. An archived copy was looked up on the Internet Archive; where none exists the footnote says so.
- Eurostat figures: the value was read from a pinned Eurostat dataset through its API and compared with the table cell, within 0.5%. The raw API response is stored and its SHA-256 recorded in model/fetch_manifest.csv. The footnote names the dataset, its dimensions and the retrieval date.
- Categorical findings (infrastructure dependency, sovereignty indicators): admitted only when a second, independent automated reviewer reached the same value from the same quote.

The printed value is checked against its quote at build time. Every number and date in it must appear in the original-language quote, read in any EU number format. A number found only in the English translation does not count. An abbreviation not found in the quote is shown in the fact's checklist. A value that is not a verbatim extract is a machine summary of the quote, and is labelled as one.

A value that no checked source supports is withheld and shown as a gap. A gap means not yet sourced, never that the thing does not exist.

### Source tiers

How good is the best source behind each fact? Each cited host is classified once. An archived copy counts as the page it archived. The classification was drawn up by an agent and has not been reviewed by a person.

| Tier | Printed facts |
|---|---:|
| T1 authoritative original (official law portal, statistics office, Eurostat) | 619 |
| T2 competent public body or audit office | 607 |
| T3 other institution or company | 7 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 107 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 105 |
| Standard | 1235 |

There is no numeric confidence score: nothing has calibrated one.

### Calculations

Priority of a holding. Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

Infrastructure exposure counts, for each state, the verified holdings whose cited source says where the infrastructure runs. Silence counts as not stated, never as national.

Data-sovereignty placement. An input without a checked source is unknown and counts as not demonstrated: never as sovereign, never as dependent. Each state is placed by the first rule it meets, in this order:

- Dependent on non-EU providers: a source shows a tier 0 or 1 holding on non-EU infrastructure, or a national eID or trust anchor outside state or EU control.
- Sovereign in law and in practice: a statute keeps government data under national or EU jurisdiction, and at least 75% of verified tier 0/1 holdings run on national or EU infrastructure, the trust anchor and eID are state-controlled, and the state runs its own data centres or government cloud.
- Sovereign in practice, not secured in law: the practice test, without the statute.
- Secured in law, not yet in practice: the statute, without the practice test.
- Not demonstrated: neither.

Confidence is how many groups a state could still reach if every unknown resolved for or against it: one group is High, two Medium, three or more Low. Within a group, states are alphabetical; the order carries no meaning.

Fundamentals are Eurostat values at a pinned period, read through the dissemination API. Each is multiplied into the unit shown and rounded, and must reproduce the published value within 0.5%:

| Figure | Dataset | Filters | Period | Scale | Decimals |
|---|---|---|---|---|---|
| population_m | tps00001 | indic_de=JAN | 2026 | × 1e-06 | 3 |
| gdp_eur_bn | nama_10_gdp | na_item=B1GQ; unit=CP_MEUR | 2025 | × 0.001 | 1 |
| gov_employment_k | nama_10_a64_e | na_item=EMP_DC; nace_r2=O; unit=THS_PER | 2024 | × 1 | 1 |
| elec_price_eur_mwh | nrg_pc_205 | currency=EUR; nrg_cons=MWH500-1999; tax=X_VAT; unit=KWH | 2025-S2 | × 1000 | 1 |
| renewables_pct | nrg_ind_ren | nrg_bal=REN_ELC; unit=PC | 2025 | × 1 | 1 |
| land_km2 | reg_area3 | landuse=L0008; unit=KM2 | 2026 | × 1 | 0 |

### The cross-model fact check before every deploy

Before anything is published, every printed fact is checked once more, exactly as printed, by a second model: the one that did not write it. The checker fetches the cited source and decides whether it supports the statement as printed. A production deploy is refused unless every printed fact has a current verdict of supported. The rule, the steps and each fact's verdict are in the fact-check appendix.

| Fact written by | Checked by |
|---|---|
| claude-opus-5-5 | claude-fable-5-1 |
| claude-fable-5-1 | claude-opus-5-5 |
| anything else: unrecorded, a person, or a program | claude-fable-5-1 |

In this build, 1340 of 1340 printed facts pass the fact check.

### Citizens and human review

Anyone in any member state may submit a source or check a printed fact, through public issue forms. A submitted source passes the same mechanical checks as agent research. A fact counts as verified by a person only under the two-person rule: confirmed by someone on the reviewer roster, who did not submit it, who reads the source's language, and who declared no conflict of interest. One such rejection makes a fact disputed; two withdraw it, unless two reviewers confirmed it.

| Human review | Count |
|---|---:|
| Facts verified by a person | 0 |
| Facts disputed by a reviewer | 0 |
| Facts withdrawn after review | 0 |
| Reviewers on the roster | 0 |
| Citizen submissions staged | 0 |

### Questions answered on the web

The web page's Ask feature answers questions using only these sourced findings, with a citation for every fact. Each question is sent to Anthropic's API to generate the answer and is not stored by this site. The model is told the findings are machine-checked and to say so in every answer.

### Reproducing this document

Everything is built from the project's repository. `./run.sh reproduce` rebuilds every output in a fresh clone and compares it with the published one. `./run.sh reproduce --evidence` also re-fetches every cited source and checks every quote again. The git commit and the data bundle's SHA-256 this document was built from are printed on its title page.

Not reproducible byte for byte: agent research gives different findings if run again, so what is reproducible is their admission, from the recorded outputs. Also not: the posters (browser screenshots), and the hash of a page rendered in a browser.

### What this does not establish

- No person has verified any finding. Agents found and checked everything.
- The blind reviewer during research was the same model as the researcher, so the two readings can share its blind spots. The fact check before each deploy uses a different model, which narrows that risk but does not remove blind spots that models share.
- English wording of a non-English source is a machine translation or machine summary. Its figures are checked against the original; its words are not.
- A gap means not yet sourced. It never means the thing does not exist.
- Most states do not publish where their critical registers are hosted, so placements are mostly of low confidence. That is a finding about transparency, not about sovereignty.

## Appendix: fact check

*Method · how this was made*

### What was checked, and by whom

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. The check below is made by a second model, not by a person.

Every printed fact is put, exactly as printed, to a checker that is a different model from the one that wrote it. The checker fetches the cited source and decides whether it supports the statement as printed: the same value, name, unit, date, country and scope. A fact it does not confirm is withheld, shown as disputed with the checker's reason, until it is corrected and checked again. A production deploy is refused unless every printed fact has a current verdict of supported from an eligible checker.

In this build, 1340 of 1340 printed facts pass, and 52 facts are withheld after the check.

| Fact written by | Checked by |
|---|---|
| claude-opus-5-5 | claude-fable-5-1 |
| claude-fable-5-1 | claude-opus-5-5 |
| anything else: unrecorded, a person, or a program | claude-fable-5-1 |

### How a check runs

- factcheck.py prepare lists every printed fact whose verdict is missing, stale or not passing, hashes each as printed, names its author from the recorded files, and assigns the checker by the rule.
- The checked-in workflow (model/research/factcheck/workflow.js) asks for that checker model by name, one agent per batch of one state's facts. The checker fetches each cited page (or the Eurostat API response), looks for the quote, and decides whether it supports the statement exactly as printed: value, unit, date, country and scope. It answers supported, not supported or unclear, with a reason.
- factcheck.py stage refuses any batch whose checker reports a different model than the one asked for, or is an author of a fact in it.
- factcheck.py record writes the verdicts to the ledger, the run's manifest (input, workflow and bundle hashes, commit, counts) and this audit file.
- A fact the checker does not confirm is withheld: it is shown as disputed, with the checker's reason, instead of printed, until the fact or its source is corrected and checked again. The verdict stays on the record.
- Samples of confirmed facts are put to the other checker model to measure how often a second checker disagrees; a fact the second checker does not confirm is withheld in the same way.
- Before every production deploy, factcheck.py gate requires a current supported verdict from an eligible checker for every printed fact, and this file to be current.

A verdict holds for one fact exactly as printed: a SHA-256 of the claim, the question it answers, the printed text and every citation behind it. If any of these changes, the verdict lapses and the fact must be checked again before the next deploy.

### Fact-check runs

| Run | Date | Facts checked | Checker models | Verdicts |
|---|---|---:|---|---|
| wf_72f99a66-4e9 | 2026-10-03 | 31 | claude-fable-5-1: 31 | supported: 25; not supported: 6 |
| wf_f14edd00-71f | 2026-10-02 | 12 | claude-fable-5-1: 12 | supported: 11; not supported: 1 |
| wf_5fd3e22d-b86 | 2026-10-02 | 27 | claude-fable-5-1: 27 | supported: 27 |
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Belgium

42 of 42 printed facts about Belgium pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:BE:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:BE:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:BE:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:BE:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:BE:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BE:population_m | param:BE:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:BE:gdp_eur_bn | param:BE:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BE:gov_employment_k | param:BE:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BE:elec_price_eur_mwh | param:BE:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BE:renewables_pct | param:BE:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BE:land_km2 | param:BE:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:emergency_communications:count | Emergency calls and public-safety radio: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:crisis_management:count | Crisis management and civil protection: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BE:education:operator | Education: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Belgium

None.

---

[^s1]: Moniteur belge (copy on etaamb.openjustice.be); numac 1999007004 — Loi du 11 décembre 1998 relative à la classification et…, 1999-05-07. Loi du 11 décembre 1998 relative à la classification et aux habilitations de sécurité. <https://etaamb.openjustice.be/fr/loi-du-11-decembre-1998_n1999007004.html>
[^s2]: Agence fédérale de contrôle nucléaire (FANC), Jurion regulatory database — Loi du 11 décembre 1998 relative à la classification,…. Loi du 11 décembre 1998 relative à la classification, aux habilitations de sécurité, aux avis de sécurité et au service public réglementé; Chapitre II. <https://www.jurion.fanc.fgov.be/jurdb-consult/plainWettekstServlet?wettekstId=1384&lang=fr>
[^s3]: eID Repository (Belgian State / certipost) — Belgian Certificate Policy & Practice Statement for eID…, 2024-09-03. Belgian Certificate Policy & Practice Statement for eID PKI infrastructure, Citizen CA, v5.0. <https://repository.eid.belgium.be/downloads/citizen/en/CPS_CitizenCA_BRCA34.pdf> ([archived](https://web.archive.org/web/20240228070218/http://repository.eid.belgium.be/downloads/citizen/en/CPS_CitizenCA_BRCA34.pdf))
[^s4]: Belgian eID PKI repository — Citizen CA Certification Practice Statement (v1.4). Citizen CA Certification Practice Statement (v1.4). <https://repository.eid.belgium.be/downloads/citizen/en/CPS_CitizenCA.pdf>
[^s5]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID | IBZ - FOD Binnenlandse Zaken. eID | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid> ([archived](https://web.archive.org/web/20260617223429/https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid))
[^s6]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Wie beheert het Rijksregister van de natuurlijke personen?. Wie beheert het Rijksregister van de natuurlijke personen?. <https://www.ibz.rrn.fgov.be/nl/faq/wat-is-het-rijksregister-van-de-natuurlijke-personen/wie-beheert-het-rijksregister-van-de>
[^s7]: G-Cloud (Belgian federal government community cloud) — Housing – Datacenter-as-a-Service (G-Cloud). Housing – Datacenter-as-a-Service (G-Cloud). <https://www.gcloud.belgium.be/nl/service/detail/housing>
[^s8]: G-Cloud (Belgian federal government community cloud) — G-Cloud, de community cloud van de overheid. G-Cloud, de community cloud van de overheid. <https://www.gcloud.belgium.be/nl> ([archived](https://web.archive.org/web/20260720192938/https://www.gcloud.belgium.be/nl))
[^s9]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s10]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s11]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s12]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s13]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s14]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s15]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Rijksregister | IBZ - FOD Binnenlandse Zaken. Rijksregister | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/rijksregister-en-bevolking/rijksregister> ([archived](https://web.archive.org/web/20260911221802/https://www.ibz.rrn.fgov.be/nl/burger/rijksregister-en-bevolking/rijksregister))
[^s16]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Home | IBZ - FOD Binnenlandse Zaken. Home | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl>
[^s17]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID en GDPR, 2020-11-25. eID en GDPR. <https://www.ibz.rrn.fgov.be/sites/default/files/documents/nl/identiteitsdocumenten/eid/eID_en_GDPR.pdf>
[^s18]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID en GDPR | IBZ - FOD Binnenlandse Zaken. eID en GDPR | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid/eid-en-gdpr>
[^s19]: Rijksarchief in België — Het Rijksarchief is vertegenwoordigd in het…, 2023-06-14. Het Rijksarchief is vertegenwoordigd in het beheerscomité van de Databank voor Akten van de Burgerlijke Stand. <https://www.arch.be/index.php?l=nl&m=nieuws&r=alle-nieuwsberichten&a=2023-06-14-het-rijksarchief-is-vertegenwoordigd-in-het-beheerscomite-van-de-databank-voor-akten-van-de-burgerlijke-stand> ([archived](https://web.archive.org/web/20260416001407/https://www.arch.be/index.php?l=nl&m=nieuws&r=alle-nieuwsberichten&a=2023-06-14-het-rijksarchief-is-vertegenwoordigd-in-het-beheerscomite-van-de-databank-voor-akten-van-de-burgerlijke-stand))
[^s20]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — FAQ DABS (NL) Versie 01/07/2020, 2020-07-01. FAQ DABS (NL) Versie 01/07/2020. <https://www.ibz.rrn.fgov.be/sites/default/files/documents/nl/dabs/FAQ_DABS_NL_20200701.pdf>
[^s21]: FPS Policy and Support (BOSA), DG Simplification and Digitization — FAS Privacy Notice – FAS – My Digital Keys – version 1.3, 2025-08-05. FAS Privacy Notice – FAS – My Digital Keys – version 1.3. <https://sma-help.bosa.belgium.be/en/fas-privacy> ([archived](https://web.archive.org/web/20260928063339/https://sma-help.bosa.belgium.be/en/fas-privacy))
[^s22]: Belgisch Staatsblad (copy published by etaamb.openjustice.be) — Koninklijk Besluit van 25/05/2005 tot bepaling van de…, 2005-05-25. Koninklijk Besluit van 25/05/2005 tot bepaling van de personen en instellingen die toegang hebben tot het register van de identiteitskaarten. <https://etaamb.openjustice.be/nl/koninklijk-besluit-van-25-mei-2005_n2005000390.html>
[^s23]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies 29/2018 van 21 maart 2018 (kadastrale documentatie), 2018-03-21. Advies 29/2018 van 21 maart 2018 (kadastrale documentatie). <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-29-2018.pdf> ([archived](https://web.archive.org/web/20240921144846/https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-29-2018.pdf))
[^s24]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr. 73/2026 van 15 april 2026, 2026-04-15. Advies nr. 73/2026 van 15 april 2026. <https://gegevensbeschermingsautoriteit.be/publications/advies-nr.-73-2026.pdf>
[^s25]: Gegevensbeschermingsautoriteit — Advies nr. 121/2022 van 1 juli 2022, 2022-07-01. Advies nr. 121/2022 van 1 juli 2022. <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-121-2022.pdf> ([archived](https://web.archive.org/web/20220706131107/https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-121-2022.pdf))
[^s26]: Kruispuntbank van de Sociale Zekerheid (KSZ) — Datawarehouse | DWH_ONP_SFP_CADASTRE. Datawarehouse | DWH_ONP_SFP_CADASTRE. <https://dwh.ksz-bcss.fgov.be/nl/sourcedetail/dwh-onp-sfp-cadastre.html>
[^s27]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr. 03/2023 van 20 januari 2023, 2023-01-20. Advies nr. 03/2023 van 20 januari 2023. <https://gegevensbeschermingsautoriteit.be/publications/advies-nr.-03-2023.pdf>
[^s28]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr. 81/2022 van 25 april 2022…, 2022-04-25. Advies nr. 81/2022 van 25 april 2022 (werkingsmodaliteiten UBO-register). <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-81-2022.pdf>
[^s29]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Geschillenkamer Beslissing ten gronde 56/2026 van 12…, 2026-03-12. Geschillenkamer Beslissing ten gronde 56/2026 van 12 maart 2026. <https://www.gegevensbeschermingsautoriteit.be/publications/beslissing-ten-gronde-nr.-56-2026.pdf> ([archived](https://web.archive.org/web/20260603114950/https://www.gegevensbeschermingsautoriteit.be/publications/beslissing-ten-gronde-nr.-56-2026.pdf))
[^s30]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr 169/2019 van 8 november 2019, 2019-11-08. Advies nr 169/2019 van 8 november 2019. <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-169-2019.pdf> ([archived](https://web.archive.org/web/20251008074530/https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-169-2019.pdf))
[^s31]: Nationale Bank van België — Het Securities Settlement System (NBB-SSS). Het Securities Settlement System (NBB-SSS). <https://www.nbb.be/nl/betalingen-en-effecten/het-securities-settlement-system-nbb-sss>
[^s32]: ASTRID nv van publiek recht — Radiocommunicatie | ASTRID. Radiocommunicatie | ASTRID. <https://www.astrid.be/nl/diensten/radiocommunicatie> ([archived](https://web.archive.org/web/20250403085231/https://www.astrid.be/nl/diensten/radiocommunicatie))
[^s33]: ASTRID nv van publiek recht — Organisatie | ASTRID. Organisatie | ASTRID. <https://www.astrid.be/nl/over-astrid/organisatie> ([archived](https://web.archive.org/web/20230131192154/https://www.astrid.be/nl/over-astrid/organisatie))
[^s34]: Nationaal Crisiscentrum (NCCN) — Meer dan 1 miljoen geregistreerde adressen in BE-Alert, 2022. Meer dan 1 miljoen geregistreerde adressen in BE-Alert. <https://crisiscentrum.be/nl/newsroom/meer-dan-1-miljoen-geregistreerde-adressen-be-alert>
[^s35]: Kruispuntbank van de Sociale Zekerheid (KSZ) — Datawarehouse | DWH_AHOVOKS_LED. Datawarehouse | DWH_AHOVOKS_LED. <https://dwh.ksz-bcss.fgov.be/nl/sourcedetail/dwh-ahovoks-led> ([archived](https://web.archive.org/web/20260211053943/https://dwh.ksz-bcss.fgov.be/nl/sourcedetail/dwh-ahovoks-led))

**Evidence grades:** 6 Strong, 36 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
