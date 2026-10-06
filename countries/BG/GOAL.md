# Bulgaria: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Bulgaria could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | *Not yet sourced* |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s1][^s2] |
| State-controlled national eID | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: Both quotes are on their pages, but neither states who operates the national eID scheme: the CRC quote lists trust-service providers (not eID), and the Sega article only says the eID certificates are to be written to the ID-card chip and…. It is withheld until the fact or its source is corrected and checked again* |
| Government data centres | Yes[^s3][^s4] |
| Government cloud in operation | Yes[^s3] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 32 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Bulgaria described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 6.423 million[^s5] |
| GDP, current prices | 116.0 EUR bn[^s6] |
| Public administration employment (NACE O) | 217.8 thousand[^s7] |
| Non-household electricity price | 141.3 EUR/MWh[^s8] |
| Renewables share of electricity | 34.4 %[^s9] |
| Land area | 110 001 km²[^s10] |

## 3. Critical data holdings, by priority

The holdings Bulgaria cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 31 of 39 holding classes have a verified source; 2 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | Identity documents are issued by the Ministry of Interior, Ministry of Foreign Affairs, Ministry of Transport and Communications and Ministry of Defence[^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | National Register of Bulgarian Identity Documents (automated information fund)[^s11] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Document issuance history (tier 0) | *Not yet sourced* | From 27 April 2026 the Ministry of Interior moved to centralised personalisation and a new generation of identity documents[^s12] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet sourced* | *Disputed: the fact check (claude-opus-5-5, run wf_90fb82e7-35e) was confirmed once, but a second checker in a stability sample did not confirm this: Art. 4(3) only says that persons designated by order of the Minister of Interior also have access to the Art. 3(1) register. Neither that article nor Art. 3 says that the MVR runs or maintains the register, so the parenthetical operator…. It is withheld until the fact or its source is corrected and checked again* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | избирателните списъци, отпечатвани от ГД ГРАО (voter lists printed by DG Civil Registration and Administrative Services)[^s13] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | The Communications Regulation Commission creates, maintains and publishes the national Trusted List[^s1] | Qualified trust service providers on the Bulgarian Trusted List: Borica AD, Evrotrust Technologies AD, InfoNotary EAD, Information Services AD and Idocs Bulgaria EOOD[^s1] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet sourced* | Criminal-record bureaus at every district court and a Central Criminal Records Bureau at the Ministry of Justice[^s14] | EISS is a centralised web-based application accessed over the Internet (host not stated)[^s15] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Автоматизираната информационна система "Издирвателна дейност" - Национална Шенгенска информационна система (АИС ИД - НШИС) (Automated Information System 'Search Activity' – National Schengen Information System)[^s16] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | *Not yet sourced* | Migration Directorate of MVR and Migration units of the regional MVR directorates (Foreigners in the Republic of Bulgaria Act)[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Tax and Social Security Procedure Code: NRA creates and maintains the register and databases of obliged persons[^s18] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | Митническата информационна система за внасяне (МИСВ) (Customs Import Information System), Агенция "Митници"[^s19] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | AGCC creates and maintains the cadastral map and cadastral registers for the whole country under the Cadastre and Property Register Act[^s20] | The Registry Agency (executive agency under the Minister of Justice) keeps the property register, commercial register, BULSTAT and other registers[^s21] | *Not yet sourced* | National infrastructure[^s21] | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | The software change enabling beneficial-owner entries went live on 28.01.2019[^s21] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | автоматизираната информационна система КАТ (АИС – КАТ) (Automated Information System KAT, the vehicle registration system)[^s16] | "Пътна полиция" при СДВР/ОДМВР (Traffic Police units of the Ministry of Interior's regional directorates)[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: Both quotes are verbatim, but the MFA citation names a different system (НВИС, not printed), and the RTA ordinance names 'АИС Издирвателна дейност – НШИС' only in the context of wanted-vehicle registration termination, never as a border or…. It is withheld until the fact or its source is corrected and checked again* | Министерството на външните работи (Ministry of Foreign Affairs), for the national visa system[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | SEBRA (System for Electronic Budget Payments) is used to initiate payments of budget organisations[^s23] | BORICA AD transforms approved SEBRA payments into ISO 20022 XML[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | TARGET-BNB (national system component of the Eurosystem's TARGET)[^s24] | Българската народна банка (Bulgarian National Bank)[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Националната система 112 (National System 112)[^s25] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | шест центъра (six emergency call centres)[^s25] |
| High | Crisis management and civil protection (tier 1) | BG-ALERT public warning system over mobile networks (Cell Broadcast)[^s26][^s27] | Developed jointly by MVR and the Ministry of e-Government[^s26][^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Project to modernise and extend the SCADA/EMS and information environment in ESO's Central Dispatch (CDU)[^s28] | *Not yet sourced* | The project includes a backup data storage and processing centre for the Central Dispatch[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | Register of all current, interrupted and graduated students and doctoral candidates, kept as an electronic database through NACID[^s29] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | The NHIS holds an electronic health record for every citizen[^s30][^s31] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Business registry (tier 1) | The Commercial Register and Register of Non-Profit Legal Entities is a common electronic database[^s21] | *Not yet sourced* | Registry Agency contract to expand storage arrays, upgrade servers and supply tape libraries serving the registers' information systems[^s21] | National infrastructure[^s21] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The State Gazette website provides the full content of all issues for the last 7 years in PDF (EU N-Lex description)[^s32] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | 2021 Population and Housing Census, the 18th in Bulgaria (census site of the National Statistical Institute)[^s33] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | AGCC creates and maintains the topographic databases and the geo-information system[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 31 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 29 |

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

> Not yet sized. Capacity for Bulgaria will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 2 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Bulgaria without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Civil registry core (tier 0)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1424 facts are printed, 4296 values are withheld as gaps, and 76 are withheld as disputed.

### How sources were found

Research agents, one per member state, looked for each critical holding and each indicator. Each claim needed a verbatim quote of 8 to 60 words from an exact URL. Nothing an agent returned was used until it passed the mechanical checks below. Agent output is staged separately and is never rendered.

| Quote check of the first research runs | Claims |
|---|---:|
| exact | 2192 |
| loose | 21 |
| not_found | 75 |
| fetch_failed | 228 |

A vetting run then re-examined every printed fact, and after it the gaps. It looked for a better source, for newer information and for any source that disagrees. Each of its findings was judged by a blind reviewer, shown the quote and URL but never the proposed value. Runs: wf_1c6b8bb6-450. Reviewer model: claude-opus-5-5, the same model as the researcher.

| Vetting outcome | Findings or items |
|---|---:|
| below_T2 | 6 |
| corrected_withheld | 6 |
| corroborated | 275 |
| disputed | 11 |
| filled_gap | 367 |
| holding_not_established | 38 |
| no_better_found | 486 |
| not_reached | 201 |
| not_verified | 173 |
| review_disagreed | 177 |
| same_source | 14 |
| superseded_higher_tier | 24 |
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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 651 |
| T2 competent public body or audit office | 643 |
| T3 other institution or company | 8 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 122 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 109 |
| Standard | 1315 |

There is no numeric confidence score: nothing has calibrated one.

### Calculations

Priority of a holding. Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

Infrastructure exposure counts, for each state, the verified holdings whose cited source says where the infrastructure runs. Silence counts as not stated, never as national.

Key infrastructure and hosting, the EU-27 overview, lists every holding whose hosting a checked source states. Each cell is a copy of the one the state's own report prints, so it has the same source and the same fact check, and a withheld value stays withheld. Its counts per state are of printed facts only.

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

In this build, 1424 of 1424 printed facts pass the fact check.

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

In this build, 1424 of 1424 printed facts pass, and 55 facts are withheld after the check.

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
| wf_c38b3e2e-319 | 2026-10-06 | 32 | claude-fable-5-1: 32 | supported: 32 |
| wf_f7d14e4d-412 | 2026-10-06 | 14 | claude-fable-5-1: 14 | supported: 14 |
| wf_e9645602-884 | 2026-10-06 | 60 | claude-fable-5-1: 60 | supported: 56; not supported: 4 |
| wf_72f99a66-4e9 | 2026-10-03 | 31 | claude-fable-5-1: 31 | supported: 25; not supported: 6 |
| wf_f14edd00-71f | 2026-10-02 | 12 | claude-fable-5-1: 12 | supported: 11; not supported: 1 |
| wf_5fd3e22d-b86 | 2026-10-02 | 27 | claude-fable-5-1: 27 | supported: 27 |
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Bulgaria

46 of 46 printed facts about Bulgaria pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:BG:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:BG:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | claude-opus-5-5 | claude-fable-5-1 | supported | wf_c38b3e2e-319 |
| indicator:BG:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_c38b3e2e-319 |
| param:BG:population_m | param:BG:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:BG:gdp_eur_bn | param:BG:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BG:gov_employment_k | param:BG:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BG:elec_price_eur_mwh | param:BG:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BG:renewables_pct | param:BG:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:BG:land_km2 | param:BG:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:judicial_criminal:hosting | Judicial & criminal justice: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:BG:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:customs:register | Customs declarations: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:BG:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:land_property:foreign_dependency | Land & property registry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:central_bank:operator | Central bank systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:emergency_communications:count | Emergency calls and public-safety radio: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:crisis_management:operator | Crisis management and civil protection: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:grid_control:hosting | Electricity grid control: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:BG:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:business_registry:hosting | Business registry: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:BG:business_registry:foreign_dependency | Business registry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:BG:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Bulgaria

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| indicator:BG:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | claude-fable-5-1 | unclear | Both quotes are on their pages, but neither states who operates the national eID scheme: the CRC quote lists trust-service providers (not eID), and the Sega article only says the eID certificates are to be written to the ID-card chip and that МВР has not yet activated them. 'Partly' is an inference the sources do not state, so the support is genuinely ambiguous. |
| record:BG:border_control:register | Border and visa systems: the name of the register or system | claude-fable-5-1 | not supported | Both quotes are verbatim, but the MFA citation names a different system (НВИС, not printed), and the RTA ordinance names 'АИС Издирвателна дейност – НШИС' only in the context of wanted-vehicle registration termination, never as a border or visa system; the printed form also truncates the system's name. The source does not establish the printed system as the border/visa register. |
| record:BG:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | claude-opus-5-5 | not supported | Art. 4(3) only says that persons designated by order of the Minister of Interior also have access to the Art. 3(1) register. Neither that article nor Art. 3 says that the MVR runs or maintains the register, so the parenthetical operator claim '(MVR runs the register)' is added by the report. |

---

[^s1]: Комисия за регулиране на съобщенията — Електронни удостоверителни услуги. Електронни удостоверителни услуги. <https://crc.bg/bg/rubriki/560/elektronni-udostoveritelni-uslugi>
[^s2]: Информационно обслужване АД — Информационно обслужване АД – Доклад за дейността 2024…, 2025. Информационно обслужване АД – Доклад за дейността 2024 (Annual activity report 2024). <https://www.is-bg.net/upload/4944/IS_2024_%D0%94%D0%BE%D0%BA%D0%BB%D0%B0%D0%B4%20%D0%B7%D0%B0%20%D0%B4%D0%B5%D0%B9%D0%BD%D0%BE%D1%81%D1%82%D1%82%D0%B0.pdf>
[^s3]: eufunds.bg (Министерство на финансите) — Надграждане и развитие на Държавния хибриден частен…, 2022-01-01. Надграждане и развитие на Държавния хибриден частен облак, финансиран по ОП „Добро управление“. <https://www.eufunds.bg/bg/opgg/node/9490> ([archived](https://web.archive.org/web/20260314130013/https://www.eufunds.bg/bg/opgg/node/9490))
[^s4]: Информационно обслужване АД — Инфраструктура. Инфраструктура. <https://www.is-bg.net/bg/solutions/infrastructure>
[^s5]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s6]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s7]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s8]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s9]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s10]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s11]: Държавна агенция за бежанците (копие на закона) — Закон за българските лични документи (консолидиран текст), 2024. Закон за българските лични документи (консолидиран текст). <https://aref.government.bg/sites/default/files/2024-04/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D1%82%D0%B5%20%D0%BB%D0%B8%D1%87%D0%BD%D0%B8%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B8.pdf> ([archived](https://web.archive.org/web/20260315085009/https://aref.government.bg/sites/default/files/2024-04/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D1%82%D0%B5%20%D0%BB%D0%B8%D1%87%D0%BD%D0%B8%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B8.pdf))
[^s12]: Министерство на вътрешните работи – ОДМВР София — Въвеждане на ново поколение български лични документи, 2026-04-27. Въвеждане на ново поколение български лични документи. <https://mvr.bg/sofia/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D0%BD-%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BF%D1%80%D0%B5%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/90242> ([archived](https://web.archive.org/web/20260427064743/https://mvr.bg/sofia/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D0%BD-%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BF%D1%80%D0%B5%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/90242))
[^s13]: Централна избирателна комисия — Централна избирателна комисия, Протокол № 821 от 14.05.2026, 2026-05-14. Централна избирателна комисия, Протокол № 821 от 14.05.2026. <https://www.cik.bg/upload/280009/%E2%84%96+821-14052026-bld.pdf> ([archived](https://web.archive.org/web/20260519104206/https://www.cik.bg/upload/280009/%E2%84%96+821-14052026-bld.pdf))
[^s14]: Комисия за финансов надзор (копие на наредбата, актуално към 01.01.2022) — Наредба № 8 от 26.02.2008 г. за функциите и…, 2022. Наредба № 8 от 26.02.2008 г. за функциите и организацията на дейността на бюрата за съдимост. <https://www.fsc.bg/wp-content/uploads/2021/files/31563_file.pdf> ([archived](https://web.archive.org/web/20240909150602/https://www.fsc.bg/wp-content/uploads/2021/files/31563_file.pdf))
[^s15]: Висш адвокатски съвет — ВСС прие график за въвеждане на Единната информационна…. ВСС прие график за въвеждане на Единната информационна система на съдилищата (ЕИСС). <https://www.vas.bg/bg/a/vss-prie-grafik-za-vvezhdane-na-edinnata-informatsionna-sistema-na-sdilishchata-eiss>
[^s16]: Изпълнителна агенция „Автомобилна администрация“ — Наредба № I-45 от 24.03.2000 г. за регистриране, отчет…, 2023-11. Наредба № I-45 от 24.03.2000 г. за регистриране, отчет ... на моторните превозни средства. <https://www.rta.government.bg/upload/11661/n-I45.pdf>
[^s17]: Министерство на външните работи (копие на закона) — Закон за чужденците в Република България. Закон за чужденците в Република България. <https://www.mfa.bg/upload/138160/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D1%87%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D1%82%D0%B5%20%D0%B2%20%D0%A0%D0%B5%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%20%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D0%B8%D1%8F.pdf>
[^s18]: Министерство на вътрешните работи (копие на кодекса) — Данъчно-осигурителен процесуален кодекс. Данъчно-осигурителен процесуален кодекс. <https://www.mvr.bg/upload/296043/%D0%94%D0%9E%D0%9F%D0%9A.pdf>
[^s19]: Агенция "Митници" (Bulgarian Customs Agency) — Е-Портал на Агенция "Митници" — архив на новините, 2026-01-22. Е-Портал на Агенция "Митници" — архив на новините. <https://ep.customs.bg/eportal/public/newsArchive> ([archived](https://web.archive.org/web/20241105154640/https://ep.customs.bg/eportal/public/newsArchive))
[^s20]: Агенция по геодезия, картография и кадастър — Функции на АГКК. Функции на АГКК. <https://www.cadastre.bg/funkcii-na-agkk>
[^s21]: Сметна палата на Република България — Одитен доклад № 0300101019 – Ефективност на…, 2021-08-05. Одитен доклад № 0300101019 – Ефективност на организацията и контрола на дейностите по водене и съхраняване на поддържаните от Агенцията по вписванията регистри. <https://www.bulnao.government.bg/media/documents/OD_AV_230821.pdf> ([archived](https://web.archive.org/web/20250714123738/https://www.bulnao.government.bg/media/documents/OD_AV_230821.pdf))
[^s22]: Министерство на външните работи — Въвеждане в експлоатация на нова версия на Национална…, 2024-08-02. Въвеждане в експлоатация на нова версия на Национална визова информационна система. <https://www.mfa.bg/bg/news/41822> ([archived](https://web.archive.org/web/20260412085753/https://www.mfa.bg/bg/news/41822))
[^s23]: Министерство на финансите – дирекция „Държавно съкровище“ (публикувано от БНБ) — ДДС № 03/03.05.2023 г. – Изисквания за структурата,…, 2023-05-03. ДДС № 03/03.05.2023 г. – Изисквания за структурата, формата и съдържанието на платежни документи ... чрез СЕБРА. <https://www.bnb.bg/bnbweb/groups/public/documents/bnb_law/instructions_bnb_51681_bg.pdf> ([archived](https://web.archive.org/web/20250527084951/https://www.bnb.bg/bnbweb/groups/public/documents/bnb_law/instructions_bnb_51681_bg.pdf))
[^s24]: Българска народна банка — Платежни и сетълмент системи. Платежни и сетълмент системи. <https://www.bnb.bg/PaymentSystem/index.htm>
[^s25]: Министерство на вътрешните работи, дирекция „Национална система 112“ — 112 в България. 112 в България. <https://www.mvr.bg/112/%D0%B4%D0%B5%D0%B9%D0%BD%D0%BE%D1%81%D1%82%D0%B8/%D0%B4%D0%B5%D0%B9%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B8-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8/112_v_bg>
[^s26]: Министерство на вътрешните работи — Мотиви към проект на наредба за реда за изграждане,…. Мотиви към проект на наредба за реда за изграждане, поддържане, развитие и използване на системата BG-ALERT. <https://www.mvr.bg/upload/8121/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B8_%D0%BD%D0%B0%D1%80%D0%B5%D0%B4%D0%B1%D0%B0_bg-alert.pdf> ([archived](https://web.archive.org/web/20251211103031/https://www.mvr.bg/upload/8121/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B8_%D0%BD%D0%B0%D1%80%D0%B5%D0%B4%D0%B1%D0%B0_bg-alert.pdf))
[^s27]: Вестник „Сега“ — МВР ще издирва бандити чрез BG-ALERT, 2026-01-07. МВР ще издирва бандити чрез BG-ALERT. <https://www.segabg.com/hot/category-bulgaria/mvr-shte-izdirva-banditi-chrez-bg-alert> ([archived](https://web.archive.org/web/20260122112807/https://www.segabg.com/hot/category-bulgaria/mvr-shte-izdirva-banditi-chrez-bg-alert))
[^s28]: Електроенергиен системен оператор ЕАД — Модернизация и Разширение на Системата SCADA/EMS и…, 2016-01-20. Модернизация и Разширение на Системата SCADA/EMS и Информационната среда в ЦДУ на ЕСО – предварително обявление. <https://www.eso.bg/fileObj.php?oid=131>
[^s29]: НАЦИД — Регистър на студенти и докторанти. Регистър на студенти и докторанти. <https://nacid.bg/bg/register_rdpzsd/>
[^s30]: Министерство на здравеопазването — Национална здравноинформационна система :: НЗИС, 2026-08-31. Национална здравноинформационна система :: НЗИС. <https://www.his.bg/>
[^s31]: Национална здравноосигурителна каса (копие на закона) — Закон за здравето. Закон за здравето. <https://www.nhif.bg/upload/30458/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%B5%D1%82%D0%BE.pdf>
[^s32]: Европейска комисия / Службата за публикации на ЕС (N-Lex) — За националната база данни – България. За националната база данни – България. <https://n-lex.europa.eu/n-lex/info/info-bg/index?lang=bg> ([archived](https://web.archive.org/web/20250629165146/https://n-lex.europa.eu/n-lex/info/info-bg/index?lang=bg))
[^s33]: Национален статистически институт — Преброяване 2021. Преброяване 2021. <https://census2021.bg/> ([archived](https://web.archive.org/web/20260717163802/https://census2021.bg/))

**Evidence grades:** 4 Strong, 42 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
