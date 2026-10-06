# Slovakia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Slovakia could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | *Not yet sourced* |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s1][^s2] |
| State-controlled national eID | Yes[^s3] |
| Government data centres | Yes[^s4] |
| Government cloud in operation | Yes[^s4] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Slovakia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.409 million[^s5] |
| GDP, current prices | 136.8 EUR bn[^s6] |
| Public administration employment (NACE O) | 169.4 thousand[^s7] |
| Non-household electricity price | 209.0 EUR/MWh[^s8] |
| Renewables share of electricity | 24.1 %[^s9] |
| Land area | 48 702 km²[^s10] |

## 3. Critical data holdings, by priority

The holdings Slovakia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 29 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Register obyvateľov Slovenskej republiky (Register of Inhabitants of the Slovak Republic), a public-administration information system identifying persons, their residence and relationships[^s11] | The Ministry of Interior (ministerstvo) administers the Register of Natural Persons, a base register; retention is permanent[^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Evidencia občianskych preukazov (ID card records) kept by the Ministry of Interior and district police directorates[^s12] | The Ministry of Interior keeps the central register of travel documents, which includes the facial image[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | Zbierka listín (collection of source documents) kept by registry offices as the basis for civil-status entries[^s14] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Evidencia občianskych preukazov (ID card issuance records), incl. numbers of issued, lost and stolen cards and destruction dates[^s12] | Kept by the Ministry of Interior and district police directorates[^s12] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | eID: electronic identity card with contact chip, issued since 2 December 2013[^s3] | The Ministry of Interior administers the authentication part of the authentication module; MIRRI administers its communication part[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Stály zoznam voličov (permanent electoral roll) compiled and kept by each municipality[^s16] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | Slovenská národná certifikačná autorita (SNCA), providing qualified trust services free of charge to public authorities[^s17][^s2] | *Disputed: sources disagree. Národná agentúra pre sieťové a elektronické služby (SNCA) — Certifikačná autorita gives the value this report printed; Národná agentúra pre sieťové a elektronické služby — Kvalifikované dôveryhodné služby gives “NASES (Národná agentúra pre sieťové a elektronické služby), operator of SNCA”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Kataster nehnuteľností (real-estate cadastre) including ownership, liens and other rights[^s18] | The Office of Geodesy, Cartography and Cadastre (ÚGKK SR, 'úrad') administers the cadastral records and the cadastre information system[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Judicial & criminal justice (tier 1) | Register trestov (Criminal Records Register) kept by the General Prosecutor's Office[^s19] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Police Force information systems processing personal data, fingerprint (dactyloscopic) data and face images[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Police Force information systems holding records on foreigners' entry, stay and departure, visa and residence applicants[^s21] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | Register poistencov a sporiteľov starobného dôchodkového sporenia (register of insured persons and pension savers) and employer register kept by Sociálna poisťovňa[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Centrálny register poistencov (central register of insured persons) kept by the Health Care Surveillance Authority (ÚDZS)[^s23] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Obchodný register (Commercial Register) and collection of deeds, kept electronically by registry courts[^s24] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Register partnerov verejného sektora (Register of Public Sector Partners), run by the Ministry of Justice with Žilina District Court as registering body[^s25] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Evidencia vozidiel (vehicle register), an information system of the Police Force[^s26] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Police Force records on undesirable persons, border-control data on foreigners and illegal stay[^s21] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Police Force information system on firearms licences, holders and registered weapons[^s27] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | Centrálny informačný systém štátnej služby (central civil-service information system) administered by the Government Office[^s28] | Government Office of the Slovak Republic (Úrad vlády SR)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | Register kandidátov a kandidátnych listín (Register of candidates and candidate lists), created and operated by the Ministry of Interior[^s16] | Election results are processed through the information system of the Statistical Office of the Slovak Republic[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | Národná banka Slovenska operates two payment systems: TARGET-SK (RTGS) and SIPS (retail)[^s29] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Coordination centres receive 112 calls, eCall and SMS emergency communications[^s30] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Informačný systém krízového riadenia štátu (state crisis management information system)[^s31] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Dispatch control of the transmission system, incl. defence and restoration plan in a blackout[^s32] | SEPS a.s. is the transmission system operator including the Slovak Electricity Dispatch Centre[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | Centrálny register (central register of children, pupils and students) under the School Act[^s34] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | Národný zdravotnícky informačný systém (National Health Information System), administered by the National Health Information Centre[^s35] | National Health Information Centre (NCZI, 'národné centrum')[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Slov-Lex, the public administration information system administered and operated by the Ministry of Justice[^s36] | The Ministry of Justice publishes the Collection of Laws; it is issued in electronic and paper form[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | Elektronický archív Slovenska (Electronic Archive of Slovakia), the long-term repository of electronic archival records of public authorities[^s37] | The Electronic Archive also archives structured data and data from Ministry of Interior production systems[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Register adries (Address Register), administered by the Ministry of Interior[^s38] | ÚGKK SR creates, administers and operates the geodesy, cartography and cadastre information system (ISGKK)[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 29 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
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

> Not yet sized. Capacity for Slovakia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Slovakia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Fingerprint biometric (tier 0)
- Authentication audit log (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Treasury and state accounts (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1396 facts are printed, 4324 values are withheld as gaps, and 76 are withheld as disputed.

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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 628 |
| T2 competent public body or audit office | 636 |
| T3 other institution or company | 10 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 122 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 108 |
| Standard | 1288 |

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

In this build, 1396 of 1396 printed facts pass the fact check.

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

In this build, 1396 of 1396 printed facts pass, and 56 facts are withheld after the check.

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
| wf_e9645602-884 | 2026-10-06 | 60 | claude-fable-5-1: 60 | supported: 56; not supported: 4 |
| wf_72f99a66-4e9 | 2026-10-03 | 31 | claude-fable-5-1: 31 | supported: 25; not supported: 6 |
| wf_f14edd00-71f | 2026-10-02 | 12 | claude-fable-5-1: 12 | supported: 11; not supported: 1 |
| wf_5fd3e22d-b86 | 2026-10-02 | 27 | claude-fable-5-1: 27 | supported: 27 |
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Slovakia

51 of 51 printed facts about Slovakia pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:SK:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SK:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SK:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SK:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SK:population_m | param:SK:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:SK:gdp_eur_bn | param:SK:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SK:gov_employment_k | param:SK:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SK:elec_price_eur_mwh | param:SK:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SK:renewables_pct | param:SK:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SK:land_km2 | param:SK:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:SK:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:SK:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:SK:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:SK:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:government_payroll:operator | Government payroll and personnel: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:electoral_management:operator | Election management and results: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:SK:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:health_records:operator | Health records: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:national_archives:register | National archives (digital): the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:national_archives:operator | National archives (digital): the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SK:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:SK:geospatial:operator | Geospatial base data: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Slovakia

None.

---

[^s1]: Národná agentúra pre sieťové a elektronické služby (NASES) — Činnosť agentúry. Činnosť agentúry. <https://www.nases.gov.sk/o-nas/cinnost-agentury> ([archived](https://web.archive.org/web/20260928114903/https://www.nases.gov.sk/o-nas/cinnost-agentury))
[^s2]: Národná agentúra pre sieťové a elektronické služby (SNCA) — Certifikačná autorita. Certifikačná autorita. <https://snca.gov.sk/o-nas/certifikacna-autorita> ([archived](https://web.archive.org/web/20260612111428/https://snca.gov.sk/o-nas/certifikacna-autorita))
[^s3]: Národná agentúra pre sieťové a elektronické služby (slovensko.sk) — Nové elektronické občianske preukazy s čipom, 2013-12-01. Nové elektronické občianske preukazy s čipom. <https://www.slovensko.sk/sk/eid> ([archived](https://web.archive.org/web/20260218060914/https://www.slovensko.sk/sk/eid))
[^s4]: Ministerstvo investícií, regionálneho rozvoja a informatizácie SR (MIRRI) — Vládny cloud. Vládny cloud. <https://mirri.gov.sk/sekcie/informatizacia/dokumenty/vladny-cloud/>
[^s5]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s6]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s7]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s8]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s9]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s10]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s11]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o hlásení pobytu občanov Slovenskej republiky a…. Zákon o hlásení pobytu občanov Slovenskej republiky a registri obyvateľov Slovenskej republiky 253/1998. <https://zakony.judikaty.info/predpis/zakon-253/1998> ([archived](https://web.archive.org/web/20240913011250/https://zakony.judikaty.info/predpis/zakon-253/1998))
[^s12]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o občianskych preukazoch 224/2006. Zákon o občianskych preukazoch 224/2006. <https://zakony.judikaty.info/predpis/zakon-224/2006> ([archived](https://web.archive.org/web/20220307183542/https://zakony.judikaty.info/predpis/zakon-224/2006))
[^s13]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o cestovných dokladoch 647/2007. Zákon o cestovných dokladoch 647/2007. <https://zakony.judikaty.info/predpis/zakon-647/2007> ([archived](https://web.archive.org/web/20240913021636/https://zakony.judikaty.info/predpis/zakon-647/2007))
[^s14]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon Národnej rady Slovenskej republiky o matrikách…. Zákon Národnej rady Slovenskej republiky o matrikách 154/1994. <https://zakony.judikaty.info/predpis/zakon-154/1994> ([archived](https://web.archive.org/web/20240913021122/https://zakony.judikaty.info/predpis/zakon-154/1994))
[^s15]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o e-Governmente 305/2013. Zákon o e-Governmente 305/2013. <https://zakony.judikaty.info/predpis/zakon-305/2013>
[^s16]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o podmienkach výkonu volebného práva 180/2014. Zákon o podmienkach výkonu volebného práva 180/2014. <https://zakony.judikaty.info/predpis/zakon-180/2014> ([archived](https://web.archive.org/web/20240913004101/https://zakony.judikaty.info/predpis/zakon-180/2014))
[^s17]: Národná agentúra pre sieťové a elektronické služby — Kvalifikované dôveryhodné služby. Kvalifikované dôveryhodné služby. <https://www.nases.gov.sk/sluzby/sluzby-pre-po-a-ovm/doveryhodne-sluzby-snca> ([archived](https://web.archive.org/web/20260928114903/https://www.nases.gov.sk/sluzby/sluzby-pre-po-a-ovm/doveryhodne-sluzby-snca))
[^s18]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Katastrálny zákon 162/1995. Katastrálny zákon 162/1995. <https://zakony.judikaty.info/predpis/zakon-162/1995> ([archived](https://web.archive.org/web/20251008162932/https://zakony.judikaty.info/predpis/zakon-162/1995))
[^s19]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o registri trestov 330/2007. Zákon o registri trestov 330/2007. <https://zakony.judikaty.info/predpis/zakon-330/2007> ([archived](https://web.archive.org/web/20240913022235/https://zakony.judikaty.info/predpis/zakon-330/2007))
[^s20]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon Národnej rady Slovenskej republiky o Policajnom…. Zákon Národnej rady Slovenskej republiky o Policajnom zbore 171/1993. <https://zakony.judikaty.info/predpis/zakon-171/1993> ([archived](https://web.archive.org/web/20240915235127/https://zakony.judikaty.info/predpis/zakon-171/1993))
[^s21]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o pobyte cudzincov 404/2011. Zákon o pobyte cudzincov 404/2011. <https://zakony.judikaty.info/predpis/zakon-404/2011> ([archived](https://web.archive.org/web/20250624013534/https://zakony.judikaty.info/predpis/zakon-404/2011))
[^s22]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o sociálnom poistení 461/2003. Zákon o sociálnom poistení 461/2003. <https://zakony.judikaty.info/predpis/zakon-461/2003> ([archived](https://web.archive.org/web/20250624100422/https://zakony.judikaty.info/predpis/zakon-461/2003))
[^s23]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o zdravotných poisťovniach, dohľade nad zdravotnou…. Zákon o zdravotných poisťovniach, dohľade nad zdravotnou starostlivosťou 581/2004. <https://zakony.judikaty.info/predpis/zakon-581/2004>
[^s24]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o obchodnom registri 530/2003. Zákon o obchodnom registri 530/2003. <https://zakony.judikaty.info/predpis/zakon-530/2003> ([archived](https://web.archive.org/web/20250624003611/https://zakony.judikaty.info/predpis/zakon-530/2003))
[^s25]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o registri partnerov verejného sektora 315/2016. Zákon o registri partnerov verejného sektora 315/2016. <https://zakony.judikaty.info/predpis/zakon-315/2016> ([archived](https://web.archive.org/web/20240522091210/https://zakony.judikaty.info/predpis/zakon-315/2016))
[^s26]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o cestnej premávke 8/2009. Zákon o cestnej premávke 8/2009. <https://zakony.judikaty.info/predpis/zakon-8/2009> ([archived](https://web.archive.org/web/20240225121954/https://zakony.judikaty.info/predpis/zakon-8/2009))
[^s27]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o strelných zbraniach a strelive 190/2003. Zákon o strelných zbraniach a strelive 190/2003. <https://zakony.judikaty.info/predpis/zakon-190/2003> ([archived](https://web.archive.org/web/20240521050240/https://zakony.judikaty.info/predpis/zakon-190/2003))
[^s28]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o štátnej službe 55/2017. Zákon o štátnej službe 55/2017. <https://zakony.judikaty.info/predpis/zakon-55/2017>
[^s29]: Národná banka Slovenska — Platobné systémy. Platobné systémy. <https://nbs.sk/platby/platobne-systemy/> ([archived](https://web.archive.org/web/20260617103250/https://nbs.sk/platby/platobne-systemy/))
[^s30]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o integrovanom záchrannom systéme 129/2002. Zákon o integrovanom záchrannom systéme 129/2002. <https://zakony.judikaty.info/predpis/zakon-129/2002> ([archived](https://web.archive.org/web/20250624004629/https://zakony.judikaty.info/predpis/zakon-129/2002))
[^s31]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o riadení štátu v krízových situáciách mimo času…. Zákon o riadení štátu v krízových situáciách mimo času vojny a vojnového stavu 387/2002. <https://zakony.judikaty.info/predpis/zakon-387/2002>
[^s32]: Slovenská elektrizačná prenosová sústava, a. s. — Dispečing. Dispečing. <https://www.sepsas.sk/pre-partnerov/dispecing/> ([archived](https://web.archive.org/web/20260614225618/https://www.sepsas.sk/pre-partnerov/dispecing/))
[^s33]: Slovenská elektrizačná prenosová sústava, a. s. — O spoločnosti. O spoločnosti. <https://www.sepsas.sk/o-nas/o-spolocnosti/> ([archived](https://web.archive.org/web/20260516114637/https://www.sepsas.sk/o-nas/o-spolocnosti/))
[^s34]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o výchove a vzdelávaní (školský zákon) 245/2008. Zákon o výchove a vzdelávaní (školský zákon) 245/2008. <https://zakony.judikaty.info/predpis/zakon-245/2008> ([archived](https://web.archive.org/web/20240715115213/https://zakony.judikaty.info/predpis/zakon-245/2008))
[^s35]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o národnom zdravotníckom informačnom systéme 153/2013. Zákon o národnom zdravotníckom informačnom systéme 153/2013. <https://zakony.judikaty.info/predpis/zakon-153/2013> ([archived](https://web.archive.org/web/20250624093444/https://zakony.judikaty.info/predpis/zakon-153/2013))
[^s36]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o tvorbe právnych predpisov a o Zbierke zákonov…. Zákon o tvorbe právnych predpisov a o Zbierke zákonov Slovenskej republiky 400/2015. <https://zakony.judikaty.info/predpis/zakon-400/2015> ([archived](https://web.archive.org/web/20250624015208/https://zakony.judikaty.info/predpis/zakon-400/2015))
[^s37]: Ministerstvo vnútra Slovenskej republiky — Elektronický archív Slovenska MV SR. Elektronický archív Slovenska MV SR. <https://www.minv.sk/?elektronicky-archiv-slovenska-mv-sr>
[^s38]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o registri adries 125/2015. Zákon o registri adries 125/2015. <https://zakony.judikaty.info/predpis/zakon-125/2015> ([archived](https://web.archive.org/web/20210228034237/https://zakony.judikaty.info/predpis/zakon-125/2015))
[^s39]: Úrad geodézie, kartografie a katastra Slovenskej republiky — Výročná správa ÚGKK SR za rok 2025, 2026. Výročná správa ÚGKK SR za rok 2025. <https://www.skgeodesy.sk/files/sk/slovensky/ugkk/kontrakty-vyrocne-spravy/ugkk-sr_vyrocna-sprava_2025.pdf> ([archived](https://web.archive.org/web/20260609112750/https://www.skgeodesy.sk/files/sk/slovensky/ugkk/kontrakty-vyrocne-spravy/ugkk-sr_vyrocna-sprava_2025.pdf))

**Evidence grades:** 1 Strong, 50 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
