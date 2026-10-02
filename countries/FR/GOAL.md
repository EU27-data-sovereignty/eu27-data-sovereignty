# France: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, France could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | Yes[^s3][^s4] |
| State-controlled trust anchor | Yes[^s5][^s6] |
| State-controlled national eID | Yes[^s7][^s8][^s9] |
| Government data centres | Yes[^s10] |
| Government cloud in operation | Yes[^s10] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

France described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 69.11 million[^s11] |
| GDP, current prices | 2 991.1 EUR bn[^s12] |
| Public administration employment (NACE O) | 2 535.1 thousand[^s13] |
| Non-household electricity price | 153.4 EUR/MWh[^s14] |
| Renewables share of electricity | 33.1 %[^s15] |
| Land area | 633 886 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings France cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 35 of 39 holding classes have a verified source; 6 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | RNIPP, the register used to verify the civil status of people born in France[^s17][^s18] | Insee has managed the RNIPP since its creation[^s19][^s18] | *Not stated in sources* | Civil status of 113 million people born in or having lived in France[^s19] |
| Critical | Facial biometric (tier 0) | TES centralises the digitised facial image and fingerprints of every ID-card and passport applicant[^s20] | Ministry of the Interior is the controller of TES[^s20] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | TES holds fingerprints for issuing national ID cards and passports[^s20] | Ministry of the Interior[^s20] | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | SCEC draws up the civil-status acts of persons who acquire French nationality[^s21] | SCEC is a national-competence service of the Ministry of Foreign Affairs[^s21] | *Not stated in sources* | About 16 million civil-status acts[^s21] |
| Critical | Authentication audit log (tier 0) | FranceConnect keeps traceability records of access to the teleservice[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | TES records document number, type, and date and place of issue for each ID card and passport[^s20] | Ministry of the Interior[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | FranceConnect (the State's electronic identification and authentication service)[^s8] | DINUM (Direction interministérielle du numérique)[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | répertoire électoral unique (REU) (single electoral register)[^s24] | Insee[^s24] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | The Justice ministry root CA is to be signed by IGC/A, the administration's trust infrastructure[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | plan cadastral (cadastral plan)[^s26] | *Not yet sourced* | *Not stated in sources* | 598747 plan sheets[^s26] |
| High | Judicial & criminal justice (tier 1) | ASTREA is the information system of the national criminal record[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | TAJ is a Ministry of the Interior file shared by police and gendarmerie[^s28] | FAED is run by the Direction centrale de la police judiciaire[^s29] | *Not stated in sources* | *Not yet sourced* |
| High | Intelligence services (tier 1) | DRSD SIRCID information system contracted to Airbus Defence & Space[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Residence and migration status (tier 1) | AGDREF manages the right of residence of foreign nationals[^s31] | DGEF of the Ministry of the Interior is responsible[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | Customs declarations are lodged in the DELTA online service[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | RGCU is the single career register of the whole population, built by CNAV[^s33] | CNAV also runs the SNGI identifier system for the whole social-security sphere[^s33] | *Not stated in sources* | 15.3 million pensioners paid by the general scheme[^s33] |
| High | Statutory health insurance (tier 1) | CNAV runs the healthcare entitlement calculation tool (ODSS) on behalf of Cnam[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Single register covering all businesses in France[^s34] | RNE is operated by INPI[^s34] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Register of beneficial owners; discrepancies are reported to the court registry (greffe)[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | SIV, in place since April 2009, replaced the FNI[^s36] | Managed by France Titres (ANTS)[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | VISABIO (national visa-applicant processing, the French access point to VIS)[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | SIA, the national firearms information system[^s38] | Ministry of the Interior[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Chorus (the State's budgetary and accounting application)[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | PAYSAGE consolidates the payroll application for State employees[^s40] | Listed among IT projects carried by budget programmes 156 and 218[^s40] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | French component of the Eurosystem's TARGET services[^s41] | Banque de France[^s41] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | Artemis: AI applications for massive processing of military data[^s30] | *Not yet sourced* | National infrastructure[^s30] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | NexSIS pools the information systems of fire and rescue services[^s42] | ANSC designs, deploys and maintains NexSIS[^s42] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | FR-Alert, the public warning system over mobile telephony[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Téléconduite: the tools that control the power system, from dispatching rooms to substations[^s43] | RTE is the French transmission system operator[^s44] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | Vigicrues (national flood-risk information service)[^s45] | Service central Vigicrues (Central Vigicrues Service), under the DGPR[^s46] | *Not stated in sources* | *Not yet measured* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | DMP and the digital health space are State digital infrastructures[^s47] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The JO is made available electronically, permanently and free of charge[^s48] | DILA publishes the JORF[^s48] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | The notifiable-diseases system covers 38 diseases[^s49] | Data go to the ARS and to Santé publique France epidemiologists[^s49] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Secure access services for confidential data[^s50] | CASD is a GIP whose members include the State represented by Insee[^s50] | National infrastructure[^s51] | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | BAN is a State database listing all addresses in France[^s52] | IGN runs operation and distribution of the BAN[^s52] | *Not stated in sources* | *Disputed: the cited source no longer contains the quoted text (rechecked 2026-09-30)* |

## 4. Foreign-dependency exposure

Of the 35 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 33 |

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

> Not yet sized. Capacity for France will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 6 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for France without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Tax (tier 1)
- Election management and results (tier 1)
- Education (tier 1)

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

### The verdict on each fact about France

0 of 75 printed facts about France pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:FR:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | none | never checked |  |
| indicator:FR:L3 | indicator L3: Is a cloud certification that requires immunity from non-EU law in force or adopted for government use? | unrecorded | none | never checked |  |
| indicator:FR:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:FR:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:FR:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | none | never checked |  |
| indicator:FR:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | none | never checked |  |
| param:FR:population_m | param:FR:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:FR:gdp_eur_bn | param:FR:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:FR:gov_employment_k | param:FR:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:FR:elec_price_eur_mwh | param:FR:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:FR:renewables_pct | param:FR:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:FR:land_km2 | param:FR:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:FR:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | none | never checked |  |
| record:FR:civil_registry:count | Civil registry core: how many records it holds | unrecorded | none | never checked |  |
| record:FR:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | none | never checked |  |
| record:FR:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:fingerprint_biometric:operator | Fingerprint biometric: the body that operates it | unrecorded | none | never checked |  |
| record:FR:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | none | never checked |  |
| record:FR:breeder_documents:count | Breeder document scans: how many records it holds | unrecorded | none | never checked |  |
| record:FR:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | none | never checked |  |
| record:FR:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | none | never checked |  |
| record:FR:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | none | never checked |  |
| record:FR:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:land_property:register | Land & property registry: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:land_property:count | Land & property registry: how many records it holds | unrecorded | none | never checked |  |
| record:FR:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:police_records:register | Police information systems: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:police_records:operator | Police information systems: the body that operates it | unrecorded | none | never checked |  |
| record:FR:intelligence:register | Intelligence services: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | none | never checked |  |
| record:FR:customs:register | Customs declarations: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | none | never checked |  |
| record:FR:benefits_pensions:count | Benefits & pensions: how many records it holds | unrecorded | none | never checked |  |
| record:FR:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:business_registry:register | Business registry: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:business_registry:operator | Business registry: the body that operates it | unrecorded | none | never checked |  |
| record:FR:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | none | never checked |  |
| record:FR:border_control:register | Border and visa systems: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:firearms_register:register | Firearms register: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:firearms_register:operator | Firearms register: the body that operates it | unrecorded | none | never checked |  |
| record:FR:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:government_payroll:operator | Government payroll and personnel: the body that operates it | unrecorded | none | never checked |  |
| record:FR:central_bank:register | Central bank systems: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:central_bank:operator | Central bank systems: the body that operates it | unrecorded | none | never checked |  |
| record:FR:defence_command:register | Defence command and logistics: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:defence_command:foreign_dependency | Defence command and logistics: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:FR:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | none | never checked |  |
| record:FR:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | none | never checked |  |
| record:FR:water_control:register | Water management control: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:water_control:operator | Water management control: the body that operates it | unrecorded | none | never checked |  |
| record:FR:health_records:register | Health records: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | none | never checked |  |
| record:FR:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:public_health_surveillance:operator | Public health surveillance: the body that operates it | unrecorded | none | never checked |  |
| record:FR:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:statistics_microdata:operator | Statistical microdata: the body that operates it | unrecorded | none | never checked |  |
| record:FR:statistics_microdata:foreign_dependency | Statistical microdata: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:FR:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | none | never checked |  |
| record:FR:geospatial:operator | Geospatial base data: the body that operates it | unrecorded | none | never checked |  |

### Withheld after the fact check: France

None.

---

[^s1]: Secrétariat général de la défense et de la sécurité nationale (SGDSN) — Protéger le secret de la défense nationale, 2022-11-23. Protéger le secret de la défense nationale. <https://www.sgdsn.gouv.fr/nos-missions/proteger/proteger-le-secret-de-la-defense-nationale> ([archived](https://web.archive.org/web/20260702145838/https://www.sgdsn.gouv.fr/nos-missions/proteger/proteger-le-secret-de-la-defense-nationale))
[^s2]: Secrétariat général de la défense et de la sécurité nationale (SGDSN) — Réforme de la protection du secret de la défense nationale. Réforme de la protection du secret de la défense nationale. <https://www.sgdsn.gouv.fr/nos-missions/proteger/proteger-le-secret-de-la-defense-nationale/reforme-de-la-protection-du-secret>
[^s3]: Direction interministérielle du numérique (DINUM) — Cloud au centre : la doctrine de l'État. Cloud au centre : la doctrine de l'État. <https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/la-doctrine-cloud-etat/> ([archived](https://web.archive.org/web/20260825221329/https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/la-doctrine-cloud-etat/))
[^s4]: Direction interministérielle du numérique (DINUM) — Vade-mecum sur la sensibilité des données au sens de…, 2026-02-04. Vade-mecum sur la sensibilité des données au sens de l'article 31 de la loi SREN. <https://www.numerique.gouv.fr/documents/244/20260204_Vademecum_donnees_sensibles_.pdf>
[^s5]: Agence nationale de la sécurité des systèmes d'information (ANSSI) — La liste nationale de confiance. La liste nationale de confiance. <https://cyber.gouv.fr/reglementation/reglementation-identite-confiance-numerique/securite-echanges-voie-electronique/reglement-eidas/la-liste-nationale-de-confiance/> ([archived](https://web.archive.org/web/20260509192253/https://cyber.gouv.fr/reglementation/reglementation-identite-confiance-numerique/securite-echanges-voie-electronique/reglement-eidas/la-liste-nationale-de-confiance/))
[^s6]: Agence nationale de la sécurité des systèmes d'information (ANSSI) — Trusted List of France (TL-FR v6, XML). Trusted List of France (TL-FR v6, XML). <https://messervices.cyber.gouv.fr/visas/tl-fr_v6.xml>
[^s7]: France Titres (Agence nationale des titres sécurisés) — France Identité : Le service public officiel de…. France Identité : Le service public officiel de l'identité numérique. <https://france-identite.gouv.fr/presenter-france-identite/>
[^s8]: DINUM / FranceConnect — Conditions générales d'utilisation - FranceConnect…, 2026-02-20. Conditions générales d'utilisation - FranceConnect (version 1.8). <https://www.franceconnect.gouv.fr/cgu/> ([archived](https://web.archive.org/web/20260907155638/https://www.franceconnect.gouv.fr/cgu/))
[^s9]: Direction interministérielle du numérique (DINUM) — Accueil - FranceConnect. Accueil - FranceConnect. <https://www.franceconnect.gouv.fr/> ([archived](https://web.archive.org/web/20260927173544/https://www.franceconnect.gouv.fr/))
[^s10]: Direction interministérielle du numérique (DINUM) — Le Cloud interministériel. Le Cloud interministériel. <https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/le-cloud-interne/> ([archived](https://web.archive.org/web/20260614102447/https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/le-cloud-interne/))
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: CNIL — RNIPP : Répertoire national d’identification des…, 2023-02-09. RNIPP : Répertoire national d’identification des personnes physiques. <https://www.cnil.fr/fr/rnipp-repertoire-national-didentification-des-personnes-physiques> ([archived](https://web.archive.org/web/20260828044632/https://www.cnil.fr/fr/rnipp-repertoire-national-didentification-des-personnes-physiques))
[^s18]: Insee — Répertoire national d'identification des personnes…, 2026-08-11. Répertoire national d'identification des personnes physiques - Définition. <https://www.insee.fr/fr/metadonnees/definition/c1602> ([archived](https://web.archive.org/web/20260703065105/https://www.insee.fr/fr/metadonnees/definition/c1602))
[^s19]: Insee — Le Répertoire national d’identification des personnes…, 2022. Le Répertoire national d’identification des personnes physiques (RNIPP) au cœur de la vie administrative française (Courrier des statistiques N8). <https://www.insee.fr/fr/information/6665188> ([archived](https://web.archive.org/web/20260607172632/https://www.insee.fr/fr/information/6665188))
[^s20]: CNIL — Le fichier des titres électroniques sécurisés (TES), 2020-11-17. Le fichier des titres électroniques sécurisés (TES). <https://www.cnil.fr/fr/le-fichier-des-titres-electroniques-securises-tes> ([archived](https://web.archive.org/web/20260515193658/https://www.cnil.fr/fr/le-fichier-des-titres-electroniques-securises-tes))
[^s21]: Ministère de l’Europe et des Affaires étrangères — Missions du Service central d’état civil. Missions du Service central d’état civil. <https://www.diplomatie.gouv.fr/fr/services-aux-francaises-et-aux-francais/vie-administrative-et-elections/etat-civil/missions-du-service-central-d-etat-civil>
[^s22]: DINUM / FranceConnect — Politique de protection des données personnelles -…, 2023-02-15. Politique de protection des données personnelles - FranceConnect / FranceConnect+. <https://www.franceconnect.gouv.fr/cgu/politique-protection-donnees-personnelles/> ([archived](https://web.archive.org/web/20260907155638/https://www.franceconnect.gouv.fr/cgu/politique-protection-donnees-personnelles/))
[^s23]: DINUM / FranceConnect — Présentation générale - FranceConnect (partner…. Présentation générale - FranceConnect (partner documentation). <https://docs.partenaires.franceconnect.gouv.fr/fi/general/fi-general-presentation/> ([archived](https://web.archive.org/web/20260609080237/https://docs.partenaires.franceconnect.gouv.fr/fi/general/fi-general-presentation/))
[^s24]: Insee — Le Répertoire électoral unique, 2023-05-15. Le Répertoire électoral unique. <https://www.insee.fr/fr/information/3539086> ([archived](https://web.archive.org/web/20260910152019/https://www.insee.fr/fr/information/3539086))
[^s25]: Ministère de la Justice — Politique de certification – AC Racine Justice, 2011-09-15. Politique de certification – AC Racine Justice. <https://crl.justice.gouv.fr/igc/ants/MJ-PC-AC-Racine.pdf> ([archived](https://web.archive.org/web/20240920193913/https://crl.justice.gouv.fr/igc/ants/MJ-PC-AC-Racine.pdf))
[^s26]: Direction Générale des Finances Publiques — cadastre.gouv.fr - service de consultation du plan cadastral. cadastre.gouv.fr - service de consultation du plan cadastral. <https://www.cadastre.gouv.fr/scpc/accueil.do>
[^s27]: Sénat — Projet de loi de finances pour 2026 : Justice, 2025. Projet de loi de finances pour 2026 : Justice. <https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html> ([archived](https://web.archive.org/web/20260914153452/https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html))
[^s28]: CNIL — Traitement d’Antécédents Judiciaires - TAJ : comment…, 2025-11-20. Traitement d’Antécédents Judiciaires - TAJ : comment exercer vos droits ?. <https://www.cnil.fr/fr/taj-traitement-dantecedents-judiciaires> ([archived](https://web.archive.org/web/20251011141131/https://www.cnil.fr/fr/taj-traitement-dantecedents-judiciaires))
[^s29]: CNIL — FAED : Fichier automatisé des empreintes digitales. FAED : Fichier automatisé des empreintes digitales. <https://www.cnil.fr/fr/faed-fichier-automatise-des-empreintes-digitales> ([archived](https://web.archive.org/web/20260310135247/https://www.cnil.fr/fr/faed-fichier-automatise-des-empreintes-digitales))
[^s30]: Sénat / Assemblée nationale (Délégation parlementaire au renseignement) — Délégation parlementaire au renseignement - rapport…, 2020. Délégation parlementaire au renseignement - rapport d'activité 2019-2020. <https://www.senat.fr/rap/r19-506/r19-506_mono.html> ([archived](https://web.archive.org/web/20260312003200/https://www.senat.fr/rap/r19-506/r19-506_mono.html))
[^s31]: CNIL — Application de gestion des dossiers des ressortissants…, 2021-06-09. Application de gestion des dossiers des ressortissants étrangers en France (AGDREF). <https://www.cnil.fr/fr/application-de-gestion-des-dossiers-des-ressortissants-etrangers-en-france-agdref> ([archived](https://web.archive.org/web/20260919225732/https://www.cnil.fr/fr/application-de-gestion-des-dossiers-des-ressortissants-etrangers-en-france-agdref))
[^s32]: Direction générale des douanes et droits indirects — Demande d'accès aux données des déclarations en douane. Demande d'accès aux données des déclarations en douane. <https://www.douane.gouv.fr/professionnels/autres-demarches/demande-dacces-aux-donnees-des-declarations-en-douane> ([archived](https://web.archive.org/web/20260922143713/https://www.douane.gouv.fr/professionnels/autres-demarches/demande-dacces-aux-donnees-des-declarations-en-douane))
[^s33]: L’Assurance retraite (CNAV) — Dossier institutionnel 2025, 2025. Dossier institutionnel 2025. <https://www.lassuranceretraite.fr/portail-info/files/live/sites/pub/files/PDF/dossier-institutionnel-2025.pdf>
[^s34]: INPI — Le Guichet unique des entreprises et le Registre…. Le Guichet unique des entreprises et le Registre national des entreprises. <https://www.inpi.fr/decouvrir-inpi/formalites-dentreprises/guichet-unique-formalites-dentreprises-et-registre-national-entreprises> ([archived](https://web.archive.org/web/20260418192503/https://www.inpi.fr/decouvrir-inpi/formalites-dentreprises/guichet-unique-formalites-dentreprises-et-registre-national-entreprises))
[^s35]: INPI — Bénéficiaires effectifs. Bénéficiaires effectifs. <https://www.inpi.fr/ressources/formalites-dentreprises/beneficiaires-effectifs> ([archived](https://web.archive.org/web/20260902100357/https://www.inpi.fr/ressources/formalites-dentreprises/beneficiaires-effectifs))
[^s36]: CNIL — SIV : Système d’immatriculation des véhicules. SIV : Système d’immatriculation des véhicules. <https://www.cnil.fr/fr/siv-systeme-dimmatriculation-des-vehicules> ([archived](https://web.archive.org/web/20260913062431/https://www.cnil.fr/fr/siv-systeme-dimmatriculation-des-vehicules))
[^s37]: CNIL — Système d'information sur les visas - Visa information…. Système d'information sur les visas - Visa information system (VIS). <https://www.cnil.fr/fr/systeme-dinformation-sur-les-visas-visa-information-system-vis>
[^s38]: Ministère de l’Intérieur — Accueil, Système d'Information des Armes. Accueil, Système d'Information des Armes. <https://sia.detenteurs.interieur.gouv.fr/>
[^s39]: Agence pour l'informatique financière de l'État (AIFE) — Chorus Cœur et Chorus Formulaires. Chorus Cœur et Chorus Formulaires. <https://aife.economie.gouv.fr/nos-applications/chorus-et-chorus-formulaire/> ([archived](https://web.archive.org/web/20260607062032/https://aife.economie.gouv.fr/nos-applications/chorus-et-chorus-formulaire/))
[^s40]: Sénat — Projet de loi de finances pour 2025 : Gestion des…, 2024. Projet de loi de finances pour 2025 : Gestion des finances publiques - Crédits non répartis - Transformation et fonction publiques. <https://www.senat.fr/rap/l24-144-315-1/l24-144-315-1_mono.html>
[^s41]: Banque de France — Systems operated by the Banque de France. Systems operated by the Banque de France. <https://www.banque-france.fr/en/financial-stability/institutional-framework/systems-operated-banque-de-france> ([archived](https://web.archive.org/web/20260905155101/https://www.banque-france.fr/en/financial-stability/institutional-framework/systems-operated-banque-de-france))
[^s42]: Sénat — Projet de loi de finances pour 2025 : Sécurités…, 2024. Projet de loi de finances pour 2025 : Sécurités (Sécurité civile). <https://www.senat.fr/rap/l24-144-329-2/l24-144-329-2_mono.html> ([archived](https://web.archive.org/web/20251207021927/https://www.senat.fr/rap/l24-144-329-2/l24-144-329-2_mono.html))
[^s43]: RTE — Un centre d’expertise « téléconduite », 2021-09-16. Un centre d’expertise « téléconduite ». <https://www.rte-france.com/decouvrir-rte/campus-expertise-formation/centre-expertise-teleconduite> ([archived](https://web.archive.org/web/20260913085708/https://www.rte-france.com/decouvrir-rte/campus-expertise-formation/centre-expertise-teleconduite))
[^s44]: RTE — RTE en bref. RTE en bref. <https://www.rte-france.com/rte-en-bref> ([archived](https://web.archive.org/web/20250915070403/https://www.rte-france.com/rte-en-bref))
[^s45]: Service central Vigicrues (ministère de la Transition écologique) — Carte de vigilance crues nationale : Vigicrues.gouv.fr. Carte de vigilance crues nationale : Vigicrues.gouv.fr. <https://www.vigicrues.gouv.fr/> ([archived](https://web.archive.org/web/20260930055744/https://www.vigicrues.gouv.fr/))
[^s46]: Service-Public.gouv.fr (DILA) — Service central Vigicrues - Annuaire de l'administration. Service central Vigicrues - Annuaire de l'administration. <https://lannuaire.service-public.gouv.fr/gouvernement/7e9f75fc-5862-4a33-8015-da82e7edfafd> ([archived](https://web.archive.org/web/20251202100405/https://lannuaire.service-public.gouv.fr/gouvernement/7e9f75fc-5862-4a33-8015-da82e7edfafd))
[^s47]: Sénat — Projet de loi de finances pour 2025 : Santé, 2024. Projet de loi de finances pour 2025 : Santé. <https://www.senat.fr/rap/l24-144-328/l24-144-328_mono.html> ([archived](https://web.archive.org/web/20250902143337/https://www.senat.fr/rap/l24-144-328/l24-144-328_mono.html))
[^s48]: DILA — Diffusion légale, 2026-06-26. Diffusion légale. <https://www.dila.premier-ministre.gouv.fr/institution/missions/article/diffusion-legale> ([archived](https://web.archive.org/web/20251102205650/https://www.dila.premier-ministre.gouv.fr/institution/missions/article/diffusion-legale))
[^s49]: Santé publique France — Maladies à signalement obligatoire, 2026-04-22. Maladies à signalement obligatoire. <https://www.santepubliquefrance.fr/maladies-a-declaration-obligatoire> ([archived](https://web.archive.org/web/20260305175756/https://www.santepubliquefrance.fr/maladies-a-declaration-obligatoire))
[^s50]: CASD — Gouvernance et Missions. Gouvernance et Missions. <https://www.casd.eu/le-casd/gouvernance-et-missions/>
[^s51]: CASD — Infrastructure. Infrastructure. <https://www.casd.eu/technologie/infrastructure/> ([archived](https://web.archive.org/web/20260310125751/https://www.casd.eu/technologie/infrastructure/))
[^s52]: adresse.data.gouv.fr (DINUM / IGN) — Découvrir la Base Adresse Nationale. Découvrir la Base Adresse Nationale. <https://adresse.data.gouv.fr/decouvrir-la-BAN> ([archived](https://web.archive.org/web/20260921135714/https://adresse.data.gouv.fr/decouvrir-la-BAN))

**Evidence grades:** 6 Strong, 69 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
