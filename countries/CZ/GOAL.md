# Czechia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Czechia could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2][^s3] |
| Classification in law | Yes[^s4][^s5] |
| Sovereign cloud certification | Yes[^s1] |
| State-controlled trust anchor | Yes[^s6][^s7][^s8] |
| State-controlled national eID | Yes[^s9][^s10][^s11] |
| Government data centres | Yes[^s12] |
| Government cloud in operation | Yes[^s12][^s3] |

What could move this placement:

- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Czechia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.92 million[^s13] |
| GDP, current prices | 347.3 EUR bn[^s14] |
| Public administration employment (NACE O) | 325.8 thousand[^s15] |
| Non-household electricity price | 182.5 EUR/MWh[^s16] |
| Renewables share of electricity | 19.2 %[^s17] |
| Land area | 77 212 km²[^s18] |

## 3. Critical data holdings, by priority

The holdings Czechia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 32 of 39 holding classes have a verified source; 4 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | informační systém evidence obyvatel (population register information system)[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | ID card register (Evidence občanských průkazů), a public administration information system[^s20][^s21] | Ministry of the Interior is the controller of the ID card register[^s21] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s21] | — | — | — |
| Critical | Breeder document scans (tier 0) | Collection of documents (sbírka listin) underlying each civil status register book[^s22][^s23] | Ministerstvo vnitra (Ministry of the Interior) as controller of the Matriční informační systém (civil status information system)[^s24] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | NIA keeps operational data including a record of each use of NIA data[^s9][^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | The ID card register records invalid cards, the date and the reason they became invalid[^s20][^s21] | Ministry of the Interior is the controller of the ID card register[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | National point for identification and authentication (Národní bod, NIA), administered by DIA[^s9][^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Electoral roll entry (tier 0) | Election administration information system (ISSV) whose components include the voter list[^s25][^s26] | Ministry of the Interior administers the ISSV, which keeps voter records[^s25][^s26] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet sourced* | DIA acts as founder of the State Trust Services Administration[^s6][^s8] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Cadastre is kept in the Cadastre of Real Estate Information System (ISKN)[^s27] | ČÚZK is the central state authority for surveying and the cadastre[^s28][^s29] | *Not stated in sources* | More than 33 million documents in the digital part of the cadastral deed collection[^s27] |
| High | Judicial & criminal justice (tier 1) | Criminal Records Register: public administration IS of persons finally convicted[^s30][^s31] | Ministry of Justice is the controller[^s30][^s31] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Police operate and control the foreigners' information system, incl. photos and fingerprints[^s32][^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Automated Tax Information System (ADIS) of the Financial Administration[^s34][^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | Automated import system e-Dovoz completing electronic customs systems for transit, export and import[^s36] | Customs Administration: General Directorate of Customs and customs offices[^s37] | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | ČSSZ keeps the register of pension insurance contributors[^s38][^s39] | MPSV is controller of the integrated MPSV information system, which includes the ČSSZ system[^s38][^s39] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | VZP keeps the register of all persons insured under public health insurance[^s40][^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | The Public Register is a public administration IS kept electronically by the registry courts[^s42][^s43] | DIA administers the Basic Register of Persons (ROS) and assigns company identification numbers[^s44] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Register of beneficial owners is a public administration IS controlled by the Ministry of Justice[^s45] | Kept by the court competent for registration; entries made by courts or notaries[^s45] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Road Vehicle Register, controlled by the Ministry of Transport, records vehicles, owners and operators[^s46] | Ministry of Transport keeps the central driver register and digital tachograph system[^s47][^s48] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Ministry of Foreign Affairs visa information system incl. photographs and fingerprints[^s33] | Police Presidium operates the national component of SIS and the SIRENE function[^s49][^s50] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Central Firearms Register: non-public public administration IS[^s51] | Police Presidium is the controller[^s51] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Integrovaný informační systém Státní pokladny (IISSP) (Integrated Information System of the State Treasury)[^s52] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Civil service information system for service relationships[^s53][^s54] | Office of the Government is the controller[^s53][^s54] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | informační systém správy voleb (election administration information system)[^s25] | Czech Statistical Office runs results collection and builds the results system including software[^s26] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | systém CERTIS (CERTIS interbank payment system)[^s55] | Česká národní banka (Czech National Bank)[^s56] | *Not stated in sources* | over 983 million items in 2024[^s56] |
| High | Emergency calls and public-safety radio (tier 1) | 14 interconnected 112 call centres[^s57] | hasičské záchranné sbory jednotlivých krajů (regional Fire Rescue Services), in Centra tísňové komunikace (CTK)[^s58] | *Not stated in sources* | 1,995,395 calls and 33,035 SMS to 112 in 2025[^s59][^s60] |
| High | Crisis management and civil protection (tier 1) | Crisis management information system supporting crisis authorities[^s61] | Administered by the Ministry of the Interior through the Fire Rescue Service directorate[^s62][^s61] | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | matrika studentů (student register), kept by each higher education institution[^s63] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | SÚKL ('Ústav') establishes eRecept as a public administration information system[^s64][^s65] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Elektronický systém Sbírky zákonů a mezinárodních smluv (electronic system of the Collection of Laws and International Treaties, e-Sbírka)[^s66] | Ministerstvo vnitra (Ministry of the Interior)[^s66] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Includes the register of infectious disease cases and vaccination[^s67][^s68] | Infectious disease IS: Ministry of Health controller, ÚZIS operator[^s67][^s68] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | ČÚZK publishes parcels from ISKN and buildings/addresses from RÚIAN[^s27] | Český úřad zeměměřický a katastrální (Czech Office for Surveying, Mapping and Cadastre)[^s69] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 31 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 31 |

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

> Not yet sized. Capacity for Czechia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 4 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Czechia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Police information systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1388 facts are printed, 3342 values are withheld as gaps, and 22 are withheld as disputed.

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
| below_T2 | 5 |
| corroborated | 238 |
| disputed | 10 |
| filled_gap | 363 |
| holding_not_established | 38 |
| no_better_found | 447 |
| not_reached | 201 |
| not_verified | 176 |
| review_disagreed | 153 |
| same_source | 8 |
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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 633 |
| T2 competent public body or audit office | 633 |
| T3 other institution or company | 9 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 113 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 106 |
| Standard | 1282 |

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

In this build, 28 of 1388 printed facts pass the fact check.

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

In this build, 28 of 1388 printed facts pass, and 2 facts are withheld after the check.

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
- Before every production deploy, factcheck.py gate requires a current supported verdict from an eligible checker for every printed fact, and this file to be current.

A verdict holds for one fact exactly as printed: a SHA-256 of the claim, the question it answers, the printed text and every citation behind it. If any of these changes, the verdict lapses and the fact must be checked again before the next deploy.

### Fact-check runs

| Run | Date | Facts checked | Checker models | Verdicts |
|---|---|---:|---|---|
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Czechia

0 of 69 printed facts about Czechia pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:CZ:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | none | never checked |  |
| indicator:CZ:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | none | never checked |  |
| indicator:CZ:L3 | indicator L3: Is a cloud certification that requires immunity from non-EU law in force or adopted for government use? | unrecorded | none | never checked |  |
| indicator:CZ:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:CZ:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:CZ:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | none | never checked |  |
| indicator:CZ:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | none | never checked |  |
| param:CZ:population_m | param:CZ:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:CZ:gdp_eur_bn | param:CZ:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:CZ:gov_employment_k | param:CZ:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:CZ:elec_price_eur_mwh | param:CZ:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:CZ:renewables_pct | param:CZ:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:CZ:land_km2 | param:CZ:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:CZ:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:land_property:register | Land & property registry: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:land_property:operator | Land & property registry: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:land_property:count | Land & property registry: how many records it holds | unrecorded | none | never checked |  |
| record:CZ:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:tax:register | Tax: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:customs:register | Customs declarations: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:customs:operator | Customs declarations: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:business_registry:register | Business registry: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:business_registry:operator | Business registry: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:border_control:register | Border and visa systems: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:border_control:operator | Border and visa systems: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:firearms_register:register | Firearms register: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:firearms_register:operator | Firearms register: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:government_payroll:operator | Government payroll and personnel: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:electoral_management:register | Election management and results: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:electoral_management:operator | Election management and results: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:central_bank:register | Central bank systems: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:central_bank:operator | Central bank systems: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:central_bank:count | Central bank systems: how many records it holds | unrecorded | none | never checked |  |
| record:CZ:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:emergency_communications:count | Emergency calls and public-safety radio: how many records it holds | unrecorded | none | never checked |  |
| record:CZ:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:crisis_management:operator | Crisis management and civil protection: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:education:register | Education: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:health_records:register | Health records: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:public_health_surveillance:operator | Public health surveillance: the body that operates it | unrecorded | none | never checked |  |
| record:CZ:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | none | never checked |  |
| record:CZ:geospatial:operator | Geospatial base data: the body that operates it | unrecorded | none | never checked |  |

### Withheld after the fact check: Czechia

None.

---

[^s1]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Vyhláška č. 505/2025 Sb., o některých požadavcích pro…, 2026-01-01. Vyhláška č. 505/2025 Sb., o některých požadavcích pro zápis do katalogu cloud computingu (znění od 2026-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2025%2F505%2F2026-01-01/fragmenty?cisloStranky=0>
[^s2]: Národní úřad pro kybernetickou a informační bezpečnost (NÚKIB), Sbírka zákonů ČR — Vyhláška č. 505/2025 Sb., o některých požadavcích pro…, 2025-12-05. Vyhláška č. 505/2025 Sb., o některých požadavcích pro zápis do katalogu cloud computingu, příloha č. 4. <https://www.zakonyprolidi.cz/cs/2025-505> ([archived](https://web.archive.org/web/20260421002355/https://www.zakonyprolidi.cz/cs/2025-505))
[^s3]: Sbírka zákonů ČR (consolidated text via zakonyprolidi.cz) — Zákon č. 365/2000 Sb., o informačních systémech veřejné…, 2026-01-01. Zákon č. 365/2000 Sb., o informačních systémech veřejné správy, § 6m odst. 2 (consolidated text, version effective 1.1.2026). <https://www.zakonyprolidi.cz/cs/2000-365> ([archived](https://web.archive.org/web/20260130002605/https://www.zakonyprolidi.cz/cs/2000-365))
[^s4]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 412/2005 Sb., o ochraně utajovaných informací a…, 2026-07-01. Zákon č. 412/2005 Sb., o ochraně utajovaných informací a o bezpečnostní způsobilosti (znění od 2026-07-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2005%2F412%2F2026-07-01/fragmenty?cisloStranky=0>
[^s5]: Sbírka zákonů ČR (consolidated text via zakonyprolidi.cz) — Zákon č. 412/2005 Sb., o ochraně utajovaných informací a…, 2005-10-18. Zákon č. 412/2005 Sb., o ochraně utajovaných informací a o bezpečnostní způsobilosti, § 4 Stupně utajení. <https://www.zakonyprolidi.cz/cs/2005-412> ([archived](https://web.archive.org/web/20260416083654/https://www.zakonyprolidi.cz/cs/2005-412))
[^s6]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 297/2016 Sb., o službách vytvářejících důvěru…, 2023-04-01. Zákon č. 297/2016 Sb., o službách vytvářejících důvěru pro elektronické transakce (znění od 2023-04-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2016%2F297%2F2023-04-01/fragmenty?cisloStranky=0>
[^s7]: Správa státních služeb vytvářejících důvěru, s. p. o. — Úvodní strana – Správa státních služeb vytvářejících důvěru. Úvodní strana – Správa státních služeb vytvářejících důvěru. <https://sssvd.gov.cz/>
[^s8]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 297/2016 Sb., o službách vytvářejících důvěru…, 2016. Zákon č. 297/2016 Sb., o službách vytvářejících důvěru pro elektronické transakce. <https://www.zakonyprolidi.cz/cs/2016-297> ([archived](https://web.archive.org/web/20260503120919/https://www.zakonyprolidi.cz/cs/2016-297))
[^s9]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 250/2017 Sb., o elektronické identifikaci…, 2023-04-01. Zákon č. 250/2017 Sb., o elektronické identifikaci (znění od 2023-04-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2017%2F250%2F2023-04-01/fragmenty?cisloStranky=0>
[^s10]: Digitální a informační agentura — Elektronická identita – Informační web elektronické…. Elektronická identita – Informační web elektronické identity (Národní identitní autorita). <https://info.identitaobcana.cz/> ([archived](https://web.archive.org/web/20241116155854/https://info.identitaobcana.cz/))
[^s11]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 250/2017 Sb., o elektronické identifikaci, 2017. Zákon č. 250/2017 Sb., o elektronické identifikaci. <https://www.zakonyprolidi.cz/cs/2017-250>
[^s12]: Státní pokladna Centrum sdílených služeb, s. p. — SPCSS – Státní pokladna Centrum sdílených služeb, s. p.…, 2026-05-14. SPCSS – Státní pokladna Centrum sdílených služeb, s. p. (homepage, archived 14 May 2026). <https://web.archive.org/web/20260514094405/https://www.spcss.cz/>
[^s13]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s14]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s15]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s16]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s17]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s18]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s19]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 133/2000 Sb., o evidenci obyvatel a rodných…, 2025-01-01. Zákon č. 133/2000 Sb., o evidenci obyvatel a rodných číslech (znění od 2025-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2000%2F133%2F2025-01-01/fragmenty?cisloStranky=0>
[^s20]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 269/2021 Sb., o občanských průkazech (znění od…, 2026-01-01. Zákon č. 269/2021 Sb., o občanských průkazech (znění od 2026-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2021%2F269%2F2026-01-01/fragmenty?cisloStranky=0>
[^s21]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 269/2021 Sb., o občanských průkazech, 2021. Zákon č. 269/2021 Sb., o občanských průkazech. <https://www.zakonyprolidi.cz/cs/2021-269>
[^s22]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení…, 2025-01-01. Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení (znění od 2025-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2000%2F301%2F2025-01-01/fragmenty?cisloStranky=0>
[^s23]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení, 2000. Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení. <https://www.zakonyprolidi.cz/cs/2000-301> ([archived](https://web.archive.org/web/20260224043912/https://www.zakonyprolidi.cz/cs/2000-301))
[^s24]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení…, 2027-01-01. Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení (budoucí znění od 2027-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2000%2F301%2F2027-01-01/fragmenty?cisloStranky=0>
[^s25]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 88/2024 Sb., o správě voleb (znění od 2026-06-26), 2026-06-26. Zákon č. 88/2024 Sb., o správě voleb (znění od 2026-06-26). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2024%2F88%2F2026-06-26/fragmenty?cisloStranky=0>
[^s26]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 88/2024 Sb., o správě voleb, 2024. Zákon č. 88/2024 Sb., o správě voleb. <https://www.zakonyprolidi.cz/cs/2024-88> ([archived](https://web.archive.org/web/20260113232740/https://www.zakonyprolidi.cz/cs/2024-88))
[^s27]: Český úřad zeměměřický a katastrální — Výroční zpráva ČÚZK za rok 2025, 2026-03-10. Výroční zpráva ČÚZK za rok 2025. <https://cuzk.gov.cz/getattachment/f9eb09fe-b4e4-4fae-9a5a-57af8e46edeb/Vyrocni-zprava-2025_final.pdf.aspx> ([archived](https://web.archive.org/web/20260310200755/https://cuzk.gov.cz/getattachment/f9eb09fe-b4e4-4fae-9a5a-57af8e46edeb/Vyrocni-zprava-2025_final.pdf.aspx))
[^s28]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 359/1992 Sb., o zeměměřických a katastrálních…, 2024-01-01. Zákon č. 359/1992 Sb., o zeměměřických a katastrálních orgánech (znění od 2024-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F1992%2F359%2F2024-01-01/fragmenty?cisloStranky=0>
[^s29]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 359/1992 Sb., o zeměměřických a katastrálních…, 1992. Zákon č. 359/1992 Sb., o zeměměřických a katastrálních orgánech. <https://www.zakonyprolidi.cz/cs/1992-359> ([archived](https://web.archive.org/web/20260210112357/https://www.zakonyprolidi.cz/cs/1992-359))
[^s30]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 269/1994 Sb., o rejstříku trestů a evidenci…, 2026-07-01. Zákon č. 269/1994 Sb., o rejstříku trestů a evidenci přestupků (znění od 2026-07-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F1994%2F269%2F2026-07-01/fragmenty?cisloStranky=0>
[^s31]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 269/1994 Sb., o rejstříku trestů, 1994. Zákon č. 269/1994 Sb., o rejstříku trestů. <https://www.zakonyprolidi.cz/cs/1994-269> ([archived](https://web.archive.org/web/20260312160053/https://www.zakonyprolidi.cz/cs/1994-269))
[^s32]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 326/1999 Sb., o pobytu cizinců na území České…, 2026-06-12. Zákon č. 326/1999 Sb., o pobytu cizinců na území České republiky (znění od 2026-06-12). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F1999%2F326%2F2026-06-12/fragmenty?cisloStranky=2>
[^s33]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 326/1999 Sb., o pobytu cizinců na území České…, 1999. Zákon č. 326/1999 Sb., o pobytu cizinců na území České republiky. <https://www.zakonyprolidi.cz/cs/1999-326>
[^s34]: Generální finanční ředitelství — Organizační řád Finanční správy České republiky (úplné…, 2022. Organizační řád Finanční správy České republiky (úplné znění ve znění Dodatku č. 15). <https://financnisprava.gov.cz/assets/cs/prilohy/fs-financni-sprava-cr/OR_FS_UZ_D15.pdf>
[^s35]: Generální finanční ředitelství — Organizační řád Generálního finančního ředitelství. Organizační řád Generálního finančního ředitelství. <https://financnisprava.gov.cz/assets/cs/prilohy/fs-financni-sprava-cr/OR_FS_UZ_D4.pdf>
[^s36]: Celní správa ČR — e-Dovoz (tisková zpráva), 2010-10-29. e-Dovoz (tisková zpráva). <https://celnisprava.gov.cz/cz/crhradeckralove/tiskove-zpravy/2010/Stranky/e-dovoz.aspx>
[^s37]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 17/2012 Sb., o Celní správě České republiky, 2012. Zákon č. 17/2012 Sb., o Celní správě České republiky. <https://www.zakonyprolidi.cz/cs/2012-17> ([archived](https://web.archive.org/web/20260214074216/https://www.zakonyprolidi.cz/cs/2012-17))
[^s38]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 582/1991 Sb., o organizaci a provádění…, 2026-07-01. Zákon č. 582/1991 Sb., o organizaci a provádění sociálního zabezpečení (znění od 2026-07-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F1991%2F582%2F2026-07-01/fragmenty?cisloStranky=0>
[^s39]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 582/1991 Sb., o organizaci a provádění…, 1991. Zákon č. 582/1991 Sb., o organizaci a provádění sociálního zabezpečení. <https://www.zakonyprolidi.cz/cs/1991-582>
[^s40]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 592/1992 Sb., o pojistném na veřejné zdravotní…, 2026-05-27. Zákon č. 592/1992 Sb., o pojistném na veřejné zdravotní pojištění (znění od 2026-05-27). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F1992%2F592%2F2026-05-27/fragmenty?cisloStranky=0>
[^s41]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 592/1992 Sb., o pojistném na veřejné zdravotní…, 1992. Zákon č. 592/1992 Sb., o pojistném na veřejné zdravotní pojištění. <https://www.zakonyprolidi.cz/cs/1992-592> ([archived](https://web.archive.org/web/20260501174125/https://www.zakonyprolidi.cz/cs/1992-592))
[^s42]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 304/2013 Sb., o veřejných rejstřících…, 2024-07-19. Zákon č. 304/2013 Sb., o veřejných rejstřících právnických a fyzických osob (znění od 2024-07-19). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2013%2F304%2F2024-07-19/fragmenty?cisloStranky=0>
[^s43]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 304/2013 Sb., o veřejných rejstřících…, 2013. Zákon č. 304/2013 Sb., o veřejných rejstřících právnických a fyzických osob. <https://www.zakonyprolidi.cz/cs/2013-304> ([archived](https://web.archive.org/web/20260201065444/https://www.zakonyprolidi.cz/cs/2013-304))
[^s44]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 111/2009 Sb., o základních registrech, 2009. Zákon č. 111/2009 Sb., o základních registrech. <https://www.zakonyprolidi.cz/cs/2009-111> ([archived](https://web.archive.org/web/20251114195208/https://www.zakonyprolidi.cz/cs/2009-111))
[^s45]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 37/2021 Sb., o evidenci skutečných majitelů, 2021. Zákon č. 37/2021 Sb., o evidenci skutečných majitelů. <https://www.zakonyprolidi.cz/cs/2021-37> ([archived](https://web.archive.org/web/20251007111453/https://www.zakonyprolidi.cz/cs/2021-37))
[^s46]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 56/2001 Sb., o podmínkách provozu vozidel na…, 2001. Zákon č. 56/2001 Sb., o podmínkách provozu vozidel na pozemních komunikacích. <https://www.zakonyprolidi.cz/cs/2001-56> ([archived](https://web.archive.org/web/20260323232108/https://www.zakonyprolidi.cz/cs/2001-56))
[^s47]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 361/2000 Sb., o provozu na pozemních…, 2026-01-01. Zákon č. 361/2000 Sb., o provozu na pozemních komunikacích (znění od 2026-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2000%2F361%2F2026-01-01/fragmenty?cisloStranky=1>
[^s48]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 361/2000 Sb., o provozu na pozemních komunikacích, 2000. Zákon č. 361/2000 Sb., o provozu na pozemních komunikacích. <https://www.zakonyprolidi.cz/cs/2000-361> ([archived](https://web.archive.org/web/20260711182736/https://www.zakonyprolidi.cz/cs/2000-361))
[^s49]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 273/2008 Sb., o Policii České republiky (znění…, 2026-06-12. Zákon č. 273/2008 Sb., o Policii České republiky (znění od 2026-06-12). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2008%2F273%2F2026-06-12/fragmenty?cisloStranky=0>
[^s50]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 273/2008 Sb., o Policii České republiky, 2008. Zákon č. 273/2008 Sb., o Policii České republiky. <https://www.zakonyprolidi.cz/cs/2008-273> ([archived](https://web.archive.org/web/20260404065219/https://www.zakonyprolidi.cz/cs/2008-273))
[^s51]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 90/2024 Sb., o zbraních a střelivu, 2024. Zákon č. 90/2024 Sb., o zbraních a střelivu. <https://www.zakonyprolidi.cz/cs/2024-90> ([archived](https://web.archive.org/web/20260623173655/https://www.zakonyprolidi.cz/cs/2024-90))
[^s52]: Ministerstvo financí ČR — IISSP - MONITOR. IISSP - MONITOR. <https://mf.gov.cz/cs/ministerstvo/informacni-systemy/iissp--monitor> ([archived](https://web.archive.org/web/20260926100113/https://mf.gov.cz/cs/ministerstvo/informacni-systemy/iissp--monitor))
[^s53]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 234/2014 Sb., o státní službě (znění od 2026-01-01), 2026-01-01. Zákon č. 234/2014 Sb., o státní službě (znění od 2026-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2014%2F234%2F2026-01-01/fragmenty?cisloStranky=1>
[^s54]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 234/2014 Sb., o státní službě, 2014. Zákon č. 234/2014 Sb., o státní službě. <https://www.zakonyprolidi.cz/cs/2014-234> ([archived](https://web.archive.org/web/20260427134705/https://www.zakonyprolidi.cz/cs/2014-234))
[^s55]: Česká národní banka — Popis systému CERTIS. Popis systému CERTIS. <https://www.cnb.cz/cs/platebni-styk/certis/popis-systemu-certis/>
[^s56]: Česká národní banka — Systém CERTIS ročně zpracuje téměř miliardu…, 2025-01. Systém CERTIS ročně zpracuje téměř miliardu mezibankovních platebních transakcí. ČNB jej nově zpřístupní i nebankovním subjektům. <https://www.cnb.cz/cs/cnb-news/tiskove-zpravy/System-CERTIS-rocne-zpracuje-temer-miliardu-mezibankovnich-platebnich-transakci.-CNB-jej-nove-zpristupni-inbspnebankovnim-subjektum/>
[^s57]: Hasičský záchranný sbor České republiky — Tísňová linka 112 má svůj den. Tísňová linka 112 má svůj den. <https://hzscr.gov.cz/clanek/tisnova-linka-112-ma-svuj-den> ([archived](https://web.archive.org/web/20250429081533/https://hzscr.gov.cz/clanek/tisnova-linka-112-ma-svuj-den))
[^s58]: Hasičský záchranný sbor České republiky — HZS Jihomoravského kraje - Dnes je Evropský den linky 112, 2026-02-11. HZS Jihomoravského kraje - Dnes je Evropský den linky 112. <https://hzscr.gov.cz/clanek/hzs-jihomoravskeho-kraje-menu-informacni-servis-zpravodajstvi-2026-dnes-je-evropsky-den-linky-112.aspx> ([archived](https://web.archive.org/web/20260308233354/https://hzscr.gov.cz/clanek/hzs-jihomoravskeho-kraje-menu-informacni-servis-zpravodajstvi-2026-dnes-je-evropsky-den-linky-112.aspx))
[^s59]: Hasičský záchranný sbor České republiky — Záchranný útvar HZS ČR - Tísňová linka 112 funguje už 22 let, 2026-02-10. Záchranný útvar HZS ČR - Tísňová linka 112 funguje už 22 let. <https://hzscr.gov.cz/clanek/organizacni-slozky-zachranny-utvar-hzs-cr-menu-informacni-servis-zpravodajstvi-tisnova-linka-112-funguje-uz-22-let.aspx> ([archived](https://web.archive.org/web/20260616095518/https://hzscr.gov.cz/clanek/organizacni-slozky-zachranny-utvar-hzs-cr-menu-informacni-servis-zpravodajstvi-tisnova-linka-112-funguje-uz-22-let.aspx))
[^s60]: Hasičský záchranný sbor České republiky — Tísňová linka 112 funguje už 22 let, 2026-02-10. Tísňová linka 112 funguje už 22 let. <https://hzscr.gov.cz/clanek/hzs-jihoceskeho-kraje-menu-informacni-servis-zpravodajstvi-2026-unor-tisnova-linka-112-funguje-uz-22-let.aspx>
[^s61]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 240/2000 Sb., o krizovém řízení (krizový zákon), 2000. Zákon č. 240/2000 Sb., o krizovém řízení (krizový zákon). <https://www.zakonyprolidi.cz/cs/2000-240>
[^s62]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 240/2000 Sb., o krizovém řízení (krizový zákon)…, 2025-08-19. Zákon č. 240/2000 Sb., o krizovém řízení (krizový zákon) (znění od 2025-08-19). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2000%2F240%2F2025-08-19/fragmenty?cisloStranky=0>
[^s63]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 111/1998 Sb., o vysokých školách (znění od…, 2026-01-01. Zákon č. 111/1998 Sb., o vysokých školách (znění od 2026-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F1998%2F111%2F2026-01-01/fragmenty?cisloStranky=1>
[^s64]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 378/2007 Sb., o léčivech (znění od 2026-01-01), 2026-01-01. Zákon č. 378/2007 Sb., o léčivech (znění od 2026-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2007%2F378%2F2026-01-01/fragmenty?cisloStranky=0>
[^s65]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 378/2007 Sb., o léčivech, 2007. Zákon č. 378/2007 Sb., o léčivech. <https://www.zakonyprolidi.cz/cs/2007-378>
[^s66]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 222/2016 Sb., o Sbírce zákonů a mezinárodních…, 2026-08-29. Zákon č. 222/2016 Sb., o Sbírce zákonů a mezinárodních smluv (znění od 2026-08-29). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2016%2F222%2F2026-08-29/fragmenty?cisloStranky=0>
[^s67]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 258/2000 Sb., o ochraně veřejného zdraví (znění…, 2026-06-12. Zákon č. 258/2000 Sb., o ochraně veřejného zdraví (znění od 2026-06-12). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2000%2F258%2F2026-06-12/fragmenty?cisloStranky=0>
[^s68]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 258/2000 Sb., o ochraně veřejného zdraví, 2000. Zákon č. 258/2000 Sb., o ochraně veřejného zdraví. <https://www.zakonyprolidi.cz/cs/2000-258> ([archived](https://web.archive.org/web/20260319172250/https://www.zakonyprolidi.cz/cs/2000-258))
[^s69]: Ministerstvo vnitra ČR – e-Sbírka (official Collection of Laws portal) — Zákon č. 111/2009 Sb., o základních registrech (znění od…, 2026-01-01. Zákon č. 111/2009 Sb., o základních registrech (znění od 2026-01-01). <https://www.e-sbirka.cz/sbr-cache/dokumenty-sbirky/%2Fsb%2F2009%2F111%2F2026-01-01/fragmenty?cisloStranky=0>

**Evidence grades:** 4 Strong, 65 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
