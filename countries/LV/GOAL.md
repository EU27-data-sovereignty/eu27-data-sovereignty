# Latvia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Latvia could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3][^s4] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s5] |
| State-controlled national eID | Yes[^s6][^s7] |
| Government data centres | Yes[^s8][^s5] |
| Government cloud in operation | Yes[^s9][^s10] |

What could move this placement:

- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Latvia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 1.845 million[^s11] |
| GDP, current prices | 43.0 EUR bn[^s12] |
| Public administration employment (NACE O) | 65.0 thousand[^s13] |
| Non-household electricity price | 136.1 EUR/MWh[^s14] |
| Renewables share of electricity | 57.6 %[^s15] |
| Land area | 62 227 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Latvia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 28 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Fizisko personu reģistrs (Register of Natural Persons), the single system for registering and identifying natural persons[^s17] | The controller and holder of the Register is PMLP (Office of Citizenship and Migration Affairs)[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Biometrijas datu apstrādes sistēma (Biometric Data Processing System)[^s18] | Iekšlietu ministrijas Informācijas centrs (Information Centre of the Ministry of the Interior)[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Biometric Data Processing System, managed and held by the Information Centre of the Ministry of the Interior[^s19] | Iekšlietu ministrijas Informācijas centrs (Information Centre of the Ministry of the Interior)[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Civil status register entries are held on paper in one copy and electronically in the Register of Natural Persons[^s20] | Registry offices keep paper civil status entries for 100 years, then transfer them to the National Archives of Latvia[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Invalid (revoked, lost) identity documents are entered in the state information system 'Register of Invalid Documents'[^s21] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | LVRTC provides four eID means: eID card, eParaksts card, eParaksts card+ and eParaksts mobile[^s22] | The Digital Security Supervisory Committee has qualified and supervises two eID providers: Smart-ID and the state company LVRTC[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Voter Register Law establishes the Voter Register and the Electronic Online Voter Register[^s23] | PMLP processes the data in, and is the controller of, the Voter Register[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | Valsts vienotā datorizētā zemesgrāmata (State Unified Computerised Land Register)[^s24] | Tiesu administrācija (Court Administration)[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | TIS is the state information system for case management and proceedings of all courts, including the Supreme Court and the Constitutional Court[^s25] | The Punishment Register is a state information system controlled and held by the Interior Ministry Information Centre[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Cabinet regulations define the data held in the Integrated Interior Information System for locating persons, property and documents[^s27] | The system's controller and holder is the Interior Ministry Information Centre[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | The Register of Natural Persons records residence permits, EU registration certificates and permanent residence certificates[^s17] | Asylum Law: PMLP maintains the Register of Asylum Seekers[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Law on Taxes and Fees: VID communicates with taxpayers through its Electronic Declaration System (EDS)[^s29] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | Customs documents go through EU central customs systems, the Electronic Customs Data Processing System, or the VID EDS[^s30] | Under Union Customs Code Article 5, the customs administration of Latvia is the State Revenue Service[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | SAIS is the state information system holding social insurance data used to record insured persons and to grant and pay benefits and pensions[^s31] | The controller of SAIS is the Agency (State Social Insurance Agency)[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | veselības aprūpes pakalpojumu saņēmēju datubāze (health care service recipients database), maintained by the Service[^s32] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Komercreģistrs (Commercial Register)[^s33] | Uzņēmumu reģistrs (Register of Enterprises), under the Minister for Justice[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Beneficial owner information held by Latvijas Republikas Uzņēmumu reģistrs (Register of Enterprises)[^s34] | Latvijas Republikas Uzņēmumu reģistrs (Register of Enterprises of the Republic of Latvia)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | transportlīdzekļu un to vadītāju valsts reģistrs (State Register of Vehicles and Drivers)[^s35] | Valsts akciju sabiedrība "Ceļu satiksmes drošības direkcija" (state joint-stock company Road Traffic Safety Directorate, CSDD)[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | nacionālā vīzu informācijas sistēma (national visa information system)[^s36][^s37] | Iekšlietu ministrijas Informācijas centrs (Information Centre of the Ministry of the Interior)[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Ieroču reģistrs (Weapons Register)[^s38] | Iekšlietu ministrijas Informācijas centrs (Information Centre of the Ministry of the Interior)[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | ePakalpojums Maksājumi (Treasury Payments e-service)[^s40] | Valsts kase (State Treasury)[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Centrālā resursu vadības sistēma (Central Resource Management System), used by Valsts kase[^s42] | Valsts kase (State Treasury), provider of the Personāla lietvedības informācijas sistēma (Personnel Records Information System) service[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | ārkārtas situāciju valsts elektronisko sakaru tīkls (state electronic communications network for emergency situations)[^s43] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | valsts agrīnās brīdināšanas sistēma (state early warning system)[^s44] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | VIIS includes the student and graduate registers and the register of recognition statements for foreign qualifications[^s45] | The controller of VIIS is the Ministry of Education and Science[^s45] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | “Latvijas Vēstnesis” (official publication of the Republic of Latvia)[^s46] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Surveillance data are received and processed in the EPID system, including data from the Latvian Digital Health Centre's systems[^s47] | SPKC keeps the records of infectious diseases and laboratory-confirmed pathogens[^s47] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | The base geospatial data include administrative boundaries and the geospatial information of the State Address Register[^s48] | Geospatial Information Law: LĢIA, under the Ministry of Defence, implements state policy in geodesy, cartography and geospatial information[^s49][^s48] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 28 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 28 |

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

> Not yet sized. Capacity for Latvia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Latvia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- State PKI and qualified trust services (tier 0)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1490 facts are printed, 4227 values are withheld as gaps, and 79 are withheld as disputed.

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
| below_T2 | 8 |
| corrected_withheld | 6 |
| corroborated | 278 |
| disputed | 12 |
| filled_gap | 436 |
| holding_not_established | 24 |
| no_better_found | 496 |
| not_reached | 201 |
| not_verified | 197 |
| review_disagreed | 235 |
| same_source | 15 |
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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 673 |
| T2 competent public body or audit office | 687 |
| T3 other institution or company | 8 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 122 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 114 |
| Standard | 1376 |

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

In this build, 1490 of 1490 printed facts pass the fact check.

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

In this build, 1490 of 1490 printed facts pass, and 57 facts are withheld after the check.

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
| wf_b66a7125-0d9 | 2026-10-06 | 68 | claude-fable-5-1: 68 | supported: 66; not supported: 2 |
| wf_c38b3e2e-319 | 2026-10-06 | 32 | claude-fable-5-1: 32 | supported: 32 |
| wf_f7d14e4d-412 | 2026-10-06 | 14 | claude-fable-5-1: 14 | supported: 14 |
| wf_e9645602-884 | 2026-10-06 | 60 | claude-fable-5-1: 60 | supported: 56; not supported: 4 |
| wf_72f99a66-4e9 | 2026-10-03 | 31 | claude-fable-5-1: 31 | supported: 25; not supported: 6 |
| wf_f14edd00-71f | 2026-10-02 | 12 | claude-fable-5-1: 12 | supported: 11; not supported: 1 |
| wf_5fd3e22d-b86 | 2026-10-02 | 27 | claude-fable-5-1: 27 | supported: 27 |
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Latvia

62 of 62 printed facts about Latvia pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:LV:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:LV:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:LV:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:LV:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:LV:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:LV:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:LV:population_m | param:LV:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:LV:gdp_eur_bn | param:LV:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:LV:gov_employment_k | param:LV:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:LV:elec_price_eur_mwh | param:LV:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:LV:renewables_pct | param:LV:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:LV:land_km2 | param:LV:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:facial_biometric:register | Facial biometric: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:facial_biometric:operator | Facial biometric: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:fingerprint_biometric:operator | Fingerprint biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:police_records:operator | Police information systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:customs:operator | Customs declarations: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:health_insurance:register | Statutory health insurance: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:border_control:register | Border and visa systems: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:border_control:operator | Border and visa systems: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:firearms_register:register | Firearms register: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:government_payroll:register | Government payroll and personnel: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:government_payroll:operator | Government payroll and personnel: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:crisis_management:register | Crisis management and civil protection: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:LV:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:education:operator | Education: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:public_health_surveillance:operator | Public health surveillance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:LV:geospatial:operator | Geospatial base data: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Latvia

None.

---

[^s1]: Saeima / Latvijas Vēstnesis (likumi.lv) — Nacionālās kiberdrošības likums (National Cybersecurity…, 2024-07-04. Nacionālās kiberdrošības likums (National Cybersecurity Law), Art. 32. <https://likumi.lv/ta/id/353390> ([archived](https://web.archive.org/web/20260421100217/https://likumi.lv/ta/id/353390))
[^s2]: Ministru kabinets (likumi.lv) — MK noteikumi Nr. 822 (19.12.2023) Valsts noslēpuma,…, 2023-12-19. MK noteikumi Nr. 822 (19.12.2023) Valsts noslēpuma, NATO, ES un ārvalstu institūciju klasificētās informācijas aizsardzības noteikumi, para. 2.1. <https://likumi.lv/ta/id/348742> ([archived](https://web.archive.org/web/20260408194732/https://likumi.lv/ta/id/348742))
[^s3]: Latvijas Vēstnesis (likumi.lv) — Informācijas atklātības likums. Informācijas atklātības likums. <https://likumi.lv/ta/id/50601> ([archived](https://web.archive.org/web/20260802002246/https://likumi.lv/ta/id/50601))
[^s4]: Saeima (likumi.lv) — Likums "Par valsts noslēpumu" (Law on State Secrets),…, 1996-10-17. Likums "Par valsts noslēpumu" (Law on State Secrets), Art. 3(1). <https://likumi.lv/ta/id/41058> ([archived](https://web.archive.org/web/20260925033723/https://likumi.lv/ta/id/41058))
[^s5]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — Par mums (About us). Par mums (About us). <https://www.lvrtc.lv/par-lvrtc/par-mums/> ([archived](https://web.archive.org/web/20260807133227/https://www.lvrtc.lv/par-lvrtc/par-mums/))
[^s6]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — eParaksta un e-Identitātes integrācijas risinājumi. eParaksta un e-Identitātes integrācijas risinājumi. <https://www.lvrtc.lv/projekti/eparaksts_identitate/> ([archived](https://web.archive.org/web/20260207134940/https://www.lvrtc.lv/projekti/eparaksts_identitate/))
[^s7]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — eParaksta vēsture (eParaksts history). eParaksta vēsture (eParaksts history). <https://www.lvrtc.lv/par-lvrtc/vesture-2/eparaksta-vesture/> ([archived](https://web.archive.org/web/20260410091905/https://www.lvrtc.lv/par-lvrtc/vesture-2/eparaksta-vesture/))
[^s8]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — Datu centri (Data centres), public sector services. Datu centri (Data centres), public sector services. <https://www.lvrtc.lv/pakalpojumi/valsts_sektoram/datu_centri/> ([archived](https://web.archive.org/web/20260514171247/https://www.lvrtc.lv/pakalpojumi/valsts_sektoram/datu_centri/))
[^s9]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — Latvijas Nacionālais federētais mākonis (Latvian…. Latvijas Nacionālais federētais mākonis (Latvian National Federated Cloud). <https://www.lvrtc.lv/projekti/latvijas-nacionalais-federetais-makonis/> ([archived](https://web.archive.org/web/20260512124930/https://www.lvrtc.lv/projekti/latvijas-nacionalais-federetais-makonis/))
[^s10]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — LVDC – loģiski vienotais datu centrs 2. kārta (Logically…. LVDC – loģiski vienotais datu centrs 2. kārta (Logically unified data centre, phase 2). <https://www.lvrtc.lv/projekti/lvdc-2/> ([archived](https://web.archive.org/web/20260312033831/https://www.lvrtc.lv/projekti/lvdc-2/))
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Fizisko personu reģistra likums. Fizisko personu reģistra likums. <https://likumi.lv/ta/id/296185> ([archived](https://web.archive.org/web/20260920214621/https://likumi.lv/ta/id/296185))
[^s18]: Latvijas Vēstnesis (likumi.lv) — Biometrijas datu apstrādes sistēmas likums. Biometrijas datu apstrādes sistēmas likums. <https://likumi.lv/ta/id/193111> ([archived](https://web.archive.org/web/20260615194705/https://likumi.lv/ta/id/193111))
[^s19]: Valsts valodas centrs / likumi.lv — Biometric Data Processing System Law (official English…. Biometric Data Processing System Law (official English translation). <https://likumi.lv/ta/en/en/id/193111>
[^s20]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Civilstāvokļa aktu reģistrācijas likums. Civilstāvokļa aktu reģistrācijas likums. <https://likumi.lv/ta/id/253442> ([archived](https://web.archive.org/web/20260907140710/https://likumi.lv/ta/id/253442))
[^s21]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Personu apliecinošu dokumentu likums. Personu apliecinošu dokumentu likums. <https://likumi.lv/ta/id/243484> ([archived](https://web.archive.org/web/20260921064509/https://likumi.lv/ta/id/243484))
[^s22]: Aizsardzības ministrija — Elektroniskā identifikācija. Elektroniskā identifikācija. <https://www.mod.gov.lv/lv/kiberdrosiba/digitalas-drosibas-uzraudzibas-komiteja/elektroniska-identifikacija>
[^s23]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Vēlētāju reģistra likums. Vēlētāju reģistra likums. <https://likumi.lv/ta/id/83681> ([archived](https://web.archive.org/web/20250623071345/https://likumi.lv/ta/id/83681))
[^s24]: Latvijas Vēstnesis (likumi.lv) — Zemesgrāmatu likums. Zemesgrāmatu likums. <https://likumi.lv/ta/id/60460> ([archived](https://web.archive.org/web/20260415062613/https://likumi.lv/ta/id/60460))
[^s25]: Ministru kabinets / Likumi.lv — Tiesu informatīvās sistēmas noteikumi. Tiesu informatīvās sistēmas noteikumi. <https://likumi.lv/ta/id/284905>
[^s26]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Sodu reģistra likums. Sodu reģistra likums. <https://likumi.lv/ta/id/261384> ([archived](https://web.archive.org/web/20260823151729/https://likumi.lv/ta/id/261384))
[^s27]: Ministru kabinets / Likumi.lv — Noteikumi par integrētajā iekšlietu informācijas sistēmā…. Noteikumi par integrētajā iekšlietu informācijas sistēmā iekļaujamām ziņām personas, mantas vai dokumenta atrašanās vietas vai cilvēka personības noskaidrošanai vai neatpazīta cilvēka līķa identificēšanai. <https://likumi.lv/ta/id/312122> ([archived](https://web.archive.org/web/20241104215536/https://likumi.lv/ta/id/312122))
[^s28]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Patvēruma likums. Patvēruma likums. <https://likumi.lv/ta/id/278986> ([archived](https://web.archive.org/web/20250624200825/https://likumi.lv/ta/id/278986))
[^s29]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Par nodokļiem un nodevām. Par nodokļiem un nodevām. <https://likumi.lv/ta/id/33946> ([archived](https://web.archive.org/web/20260312042603/https://likumi.lv/ta/id/33946))
[^s30]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Muitas likums. Muitas likums. <https://likumi.lv/ta/id/283024> ([archived](https://web.archive.org/web/20260210002446/https://likumi.lv/ta/id/283024))
[^s31]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Par valsts sociālo apdrošināšanu. Par valsts sociālo apdrošināšanu. <https://likumi.lv/ta/id/45466> ([archived](https://web.archive.org/web/20260308035439/https://likumi.lv/ta/id/45466))
[^s32]: Saeima / likumi.lv — Veselības aprūpes finansēšanas likums, 2024. Veselības aprūpes finansēšanas likums. <https://likumi.lv/ta/id/296188-veselibas-aprupes-finansesanas-likums>
[^s33]: Latvijas Vēstnesis (likumi.lv) — Par Latvijas Republikas Uzņēmumu reģistru. Par Latvijas Republikas Uzņēmumu reģistru. <https://likumi.lv/ta/id/72847> ([archived](https://web.archive.org/web/20260114002018/https://likumi.lv/ta/id/72847))
[^s34]: Latvijas Vēstnesis (likumi.lv) — Noziedzīgi iegūtu līdzekļu legalizācijas un terorisma un…. Noziedzīgi iegūtu līdzekļu legalizācijas un terorisma un proliferācijas finansēšanas novēršanas likums. <https://likumi.lv/ta/id/178987> ([archived](https://web.archive.org/web/20251114030209/https://likumi.lv/ta/id/178987))
[^s35]: Latvijas Vēstnesis (likumi.lv) — Ceļu satiksmes likums. Ceļu satiksmes likums. <https://likumi.lv/ta/id/45467> ([archived](https://web.archive.org/web/20260608045334/https://likumi.lv/ta/id/45467))
[^s36]: Ministru kabinets / likumi.lv — Vīzu noteikumi (Cabinet Regulation No 676). Vīzu noteikumi (Cabinet Regulation No 676). <https://likumi.lv/ta/id/235770-vizu-noteikumi> ([archived](https://web.archive.org/web/20260519013019/https://likumi.lv/ta/id/235770-vizu-noteikumi))
[^s37]: Saeima / likumi.lv — Šengenas informācijas sistēmas darbības likums. Šengenas informācijas sistēmas darbības likums. <https://likumi.lv/ta/id/159481-sengenas-informacijas-sistemas-darbibas-likums>
[^s38]: Saeima / likumi.lv — Ieroču aprites likums, 2026. Ieroču aprites likums. <https://likumi.lv/ta/id/305818-ierocu-aprites-likums> ([archived](https://web.archive.org/web/20260907182139/https://likumi.lv/ta/id/305818-ierocu-aprites-likums))
[^s39]: Latvijas Vēstnesis (likumi.lv) — Ieroču aprites likums. Ieroču aprites likums. <https://likumi.lv/ta/id/305818> ([archived](https://web.archive.org/web/20260907182052/https://likumi.lv/ta/id/305818))
[^s40]: Valsts kase — Norēķini, 2026-05-14. Norēķini. <https://www.kase.gov.lv/pakalpojumi/norekini>
[^s41]: Valsts kase — Par mums, 2024-03-11. Par mums. <https://www.kase.gov.lv/valsts-kase/par-mums> ([archived](https://web.archive.org/web/20260612014819/https://www.kase.gov.lv/valsts-kase/par-mums))
[^s42]: Ministru kabinets / likumi.lv — Kārtība, kādā Valsts kase sniedz pakalpojumus valsts…, 2024-10. Kārtība, kādā Valsts kase sniedz pakalpojumus valsts pārvaldes vienotā pakalpojumu centra ietvaros (MK noteikumi Nr. 653). <https://likumi.lv/ta/id/355802-kartiba-kada-valsts-kase-sniedz-pakalpojumus-valsts-parvaldes-vienota-pakalpojumu-centra-ietvaros-unkartiba-un-apjoms>
[^s43]: Saeima / likumi.lv — Elektronisko sakaru likums, 2026. Elektronisko sakaru likums. <https://likumi.lv/ta/id/334345> ([archived](https://web.archive.org/web/20260806175404/https://likumi.lv/ta/id/334345))
[^s44]: Saeima / likumi.lv — Civilās aizsardzības un katastrofas pārvaldīšanas likums. Civilās aizsardzības un katastrofas pārvaldīšanas likums. <https://likumi.lv/ta/id/282333>
[^s45]: Ministru kabinets / Likumi.lv — Valsts izglītības informācijas sistēmas noteikumi. Valsts izglītības informācijas sistēmas noteikumi. <https://likumi.lv/ta/id/307796> ([archived](https://web.archive.org/web/20250614053013/https://likumi.lv/ta/id/307796))
[^s46]: Latvijas Vēstnesis — Oficiālais izdevums. Oficiālais izdevums. <https://www.vestnesis.lv/oficialais-izdevums> ([archived](https://web.archive.org/web/20260818235707/https://www.vestnesis.lv/oficialais-izdevums))
[^s47]: Ministru kabinets / Likumi.lv — Infekcijas slimību reģistrācijas kārtība. Infekcijas slimību reģistrācijas kārtība. <https://likumi.lv/ta/id/20667> ([archived](https://web.archive.org/web/20260315234430/https://likumi.lv/ta/id/20667))
[^s48]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Ģeotelpiskās informācijas likums. Ģeotelpiskās informācijas likums. <https://likumi.lv/ta/id/202999>
[^s49]: Latvijas Ģeotelpiskās informācijas aģentūra — Par mums. Par mums. <https://www.lgia.gov.lv/lv/par-mums> ([archived](https://web.archive.org/web/20260422142445/https://www.lgia.gov.lv/lv/par-mums))

**Evidence grades:** 2 Strong, 60 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
