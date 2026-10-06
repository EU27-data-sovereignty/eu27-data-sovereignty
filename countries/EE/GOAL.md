# Estonia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Estonia could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2][^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Partly[^s4] |
| State-controlled national eID | Yes[^s5] |
| Government data centres | Yes[^s6][^s7][^s8][^s9] |
| Government cloud in operation | Yes[^s6][^s10][^s11][^s12][^s13] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Estonia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 1.361 million[^s14] |
| GDP, current prices | 41.9 EUR bn[^s15] |
| Public administration employment (NACE O) | 43.1 thousand[^s16] |
| Non-household electricity price | 141.0 EUR/MWh[^s17] |
| Renewables share of electricity | 41.1 %[^s18] |
| Land area | 43 110 km²[^s19] |

## 3. Critical data holdings, by priority

The holdings Estonia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 26 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Rahvastikuregister (Population Register)[^s20] | Siseministeerium (Ministry of the Interior)[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: Both quotes are verbatim (ITDS archive live; ABIS page via its cited archived copy), and the ITDS sentence does define biometric data as facial image, fingerprints, signature and iris images. But the printed text is that statutory…. It is withheld until the fact or its source is corrected and checked again* | ABIS controllers are the Police and Border Guard Board and the Ministry of Foreign Affairs[^s21][^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | ABIS (automaatse biomeetrilise isikutuvastuse süsteemi andmekogu; Automated Biometric Identification System database)[^s23] | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The quote says the controller is Politsei- ja Piirivalveamet 'välja arvatud lõigetes 2 ja 3 sätestatud andmete puhul', with the Ministry of Foreign Affairs as controller for data entered under §§ 10, 15 and 16; the printed statement names…. It is withheld until the fact or its source is corrected and checked again* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | Riigi autentimisteenus (State Authentication Service, TARA)[^s24] | RIA (Riigi Infosüsteemi Amet; Information System Authority)[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Isikut tõendavate dokumentide andmekogu (Identity Documents Database)[^s25] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s25] | *Not yet sourced* | *Not stated in sources* | over 3,2 miljoni isikutunnistuse ja elamisloakaardi (over 3.2 million ID cards and residence permit cards issued)[^s26] |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | Valijate nimekiri (list of voters), compiled from the Rahvastikuregister (Population Register)[^s27] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | E-kinnistusraamat (e-Land Register)[^s28] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Karistusregister (Criminal Records Database)[^s29] | Justiits- ja Digiministeerium (Ministry of Justice and Digital Affairs); processor Registrite ja Infosüsteemide Keskus (RIK)[^s30][^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Infosüsteem POLIS (Information System POLIS)[^s32] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | elamislubade ja töölubade register (Register of Residence Permits and Work Permits)[^s33] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Maksukohustuslaste register (Register of Taxable Persons)[^s34] | Maksu- ja Tolliamet (Tax and Customs Board)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | Impulss (import customs clearance information system)[^s35] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The page supports the name 'sotsiaalkaitse infosüsteem' and its English name 'Social Security Information System', but the acronym 'SKAIS' printed alongside them appears nowhere on the cited page, so the statement as printed adds something…. It is withheld until the fact or its source is corrected and checked again* | Sotsiaalkindlustusamet (Social Insurance Board)[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Tervisekassa andmekogu (Health Insurance Fund Database)[^s37] | Tervisekassa (Health Insurance Fund)[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | E-äriregister (e-Business Register)[^s38] | Tartu Maakohtu registriosakond (registrar); RIK (develops and manages the portal)[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Tegelike kasusaajate andmekogu (Beneficial Owners Database)[^s39] | Rahandusministeerium (Ministry of Finance)[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | Schengeni infosüsteemi riiklik register (national register of the Schengen Information System)[^s40] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | teenistus- ja tsiviilrelvade register (Register of Service and Civilian Weapons)[^s41] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | riigi finants-, personali- ja palgaarvestuse süsteem SAP (state financial, personnel and payroll accounting system SAP)[^s42] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | riigi finants-, personali- ja palgaarvestuse süsteem SAP (state financial, personnel and payroll accounting system SAP)[^s42] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | valimiste infosüsteem (election information system) and elektroonilise hääletamise süsteem (electronic voting system)[^s27] | Riigi valimisteenistus (State Electoral Office)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | hädaabiteadete ning abi- ja infoteadete andmekogu (database of emergency notifications and assistance and information notifications)[^s43] | Häirekeskus (Emergency Response Centre)[^s44][^s43] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | ohuteavituse süsteem (public warning system, EE-ALARM), operated by Häirekeskus[^s43] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | SCADA/EMS at Eleringi juhtimiskeskus (Elering control centre)[^s45] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | Eesti Hariduse Infosüsteem (EHIS; Estonian Education Information System)[^s46] | Haridus- ja Teadusministeerium (Ministry of Education and Research)[^s47] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Riigi Teataja (State Gazette)[^s48] | Justiits- ja Digiministeerium (publisher); Registrite ja Infosüsteemide Keskus (RIK) (hosting and technical operation)[^s48] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 26 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 26 |

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

> Not yet sized. Capacity for Estonia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Estonia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Breeder document scans (tier 0)
- Digital identity credentials (tier 0)
- State PKI and qualified trust services (tier 0)
- Vehicle & licensing (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1408 facts are printed, 4312 values are withheld as gaps, and 76 are withheld as disputed.

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
| corroborated | 264 |
| disputed | 10 |
| filled_gap | 377 |
| holding_not_established | 41 |
| no_better_found | 486 |
| not_reached | 201 |
| not_verified | 177 |
| review_disagreed | 177 |
| same_source | 9 |
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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 634 |
| T2 competent public body or audit office | 644 |
| T3 other institution or company | 8 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 122 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 109 |
| Standard | 1299 |

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

In this build, 1408 of 1408 printed facts pass the fact check.

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

In this build, 1408 of 1408 printed facts pass, and 56 facts are withheld after the check.

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
| wf_f7d14e4d-412 | 2026-10-06 | 14 | claude-fable-5-1: 14 | supported: 14 |
| wf_e9645602-884 | 2026-10-06 | 60 | claude-fable-5-1: 60 | supported: 56; not supported: 4 |
| wf_72f99a66-4e9 | 2026-10-03 | 31 | claude-fable-5-1: 31 | supported: 25; not supported: 6 |
| wf_f14edd00-71f | 2026-10-02 | 12 | claude-fable-5-1: 12 | supported: 11; not supported: 1 |
| wf_5fd3e22d-b86 | 2026-10-02 | 27 | claude-fable-5-1: 27 | supported: 27 |
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Estonia

53 of 53 printed facts about Estonia pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:EE:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EE:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EE:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EE:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EE:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EE:population_m | param:EE:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:EE:gdp_eur_bn | param:EE:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EE:gov_employment_k | param:EE:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EE:elec_price_eur_mwh | param:EE:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EE:renewables_pct | param:EE:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EE:land_km2 | param:EE:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:authentication_audit_log:operator | Authentication audit log: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:issuance_history:count | Document issuance history: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:EE:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:police_records:operator | Police information systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:tax:operator | Tax: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:EE:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:EE:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:electoral_management:operator | Election management and results: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:EE:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:EE:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:EE:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:education:operator | Education: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_f14edd00-71f |
| record:EE:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EE:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Estonia

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:EE:benefits_pensions:register | Benefits & pensions: the name of the register or system | claude-fable-5-1 | not supported | The page supports the name 'sotsiaalkaitse infosüsteem' and its English name 'Social Security Information System', but the acronym 'SKAIS' printed alongside them appears nowhere on the cited page, so the statement as printed adds something the source does not say. |
| record:EE:facial_biometric:register | Facial biometric: the name of the register or system | claude-fable-5-1 | not supported | Both quotes are verbatim (ITDS archive live; ABIS page via its cited archived copy), and the ITDS sentence does define biometric data as facial image, fingerprints, signature and iris images. But the printed text is that statutory definition, not the name of a register or system, so it does not answer 'what'; the source that names a register holding facial images (ABIS, siseministeerium.ee) is not |
| record:EE:fingerprint_biometric:operator | Fingerprint biometric: the body that operates it | claude-fable-5-1 | unclear | The quote says the controller is Politsei- ja Piirivalveamet 'välja arvatud lõigetes 2 ja 3 sätestatud andmete puhul', with the Ministry of Foreign Affairs as controller for data entered under §§ 10, 15 and 16; the printed statement names PPA alone, and the quote does not establish whether fingerprint data fall wholly outside the MFA exception, so the source is ambiguous for the scope as printed. |

---

[^s1]: Välisluureamet – Estonian National Security Authority — Korduma kippuvad küsimused (Riigi julgeoleku volitatud…. Korduma kippuvad küsimused (Riigi julgeoleku volitatud esindaja). <https://www.teabeamet.ee/nsa/kkk.html>
[^s2]: Välisluureamet – Estonian National Security Authority — Võrdlustabelid. Võrdlustabelid. <https://www.teabeamet.ee/nsa/tabelid.html>
[^s3]: Riigi Teataja — Riigisaladuse ja salastatud välisteabe seadus…, 2026-01-17. Riigisaladuse ja salastatud välisteabe seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260117004320/https://www.riigiteataja.ee/akt/RSVS>
[^s4]: Riigi Infosüsteemi Amet (Information System Authority) — Electronic identity (eID). Electronic identity (eID). <https://www.ria.ee/en/state-information-system/electronic-identity-eid-and-trust-services/electronic-identity-eid> ([archived](https://web.archive.org/web/20260915103115/https://www.ria.ee/en/state-information-system/electronic-identity-eid-and-trust-services/electronic-identity-eid))
[^s5]: Riigi Infosüsteemi Amet (Information System Authority) — Estonian electronic identity ecosystem – Overview,…, 2025-10. Estonian electronic identity ecosystem – Overview, Version 1.0. <https://www.ria.ee/sites/default/files/documents/2025-10/Estonian-eID-ecosystem.pdf> ([archived](https://web.archive.org/web/20251023190958/https://www.ria.ee/sites/default/files/documents/2025-10/Estonian-eID-ecosystem.pdf))
[^s6]: Riigikontroll (National Audit Office of Estonia) — Eesti riigi kriitiliste andmekogude turvalisuse ja…, 2018-05-14. Eesti riigi kriitiliste andmekogude turvalisuse ja säilitamise tagamine. <https://www.riigikontroll.ee/sites/default/files/arhivaalid/2462/RKTR_2462_2-1.4_2213_001-2.pdf>
[^s7]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Riigipilve tehniline lahendus. Riigipilve tehniline lahendus. <https://www.riigipilv.ee/riigipilvest/riigipilve-tehniline-lahendus>
[^s8]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Mis saab Riigipilvest eriolukorras?. Mis saab Riigipilvest eriolukorras?. <https://www.riigipilv.ee/riigipilvest/riigipilvest-kkk/mis-saab-riigipilvest-eriolukorras>
[^s9]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) — Serverteenused ja Riigipilv. Serverteenused ja Riigipilv. <https://www.rit.ee/serverteenused> ([archived](https://web.archive.org/web/20260612050140/https://www.rit.ee/serverteenused))
[^s10]: Eesti Riigipilv / RIT — Riigipilv — mis see on?. Riigipilv — mis see on?. <https://www.riigipilv.ee/riigipilvest/riigipilvest-kkk/riigipilv-mis-see-on> ([archived](https://web.archive.org/web/20260414213340/https://www.riigipilv.ee/riigipilvest/riigipilvest-kkk/riigipilv-mis-see-on))
[^s11]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Eesti Riigipilv. Eesti Riigipilv. <https://www.riigipilv.ee/et>
[^s12]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Tellijad. Tellijad. <https://www.riigipilv.ee/riigipilvest/kliendid> ([archived](https://web.archive.org/web/20260510204636/https://www.riigipilv.ee/riigipilvest/kliendid))
[^s13]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) — Uuendatud riigipilv – Eesti avaliku sektori pilvteenus…, 2025-01-09. Uuendatud riigipilv – Eesti avaliku sektori pilvteenus on senisest võimsam ja turvalisem. <https://www.rit.ee/uudised/uuendatud-riigipilv-eesti-avaliku-sektori-pilvteenus-senisest-voimsam-ja-turvalisem>
[^s14]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s15]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s16]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s17]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s18]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s19]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s20]: Siseministeerium (Ministry of the Interior) — Rahvastikuregister. Rahvastikuregister. <https://www.siseministeerium.ee/tegevusvaldkonnad/rahvastikutoimingud/rahvastikuregister>
[^s21]: Riigi Teataja — Isikut tõendavate dokumentide seadus (Internet Archive…, 2026-03-13. Isikut tõendavate dokumentide seadus (Internet Archive copy of Riigi Teataja). <https://web.archive.org/web/20260313205329/https://www.riigiteataja.ee/akt/itds>
[^s22]: Riigi Teataja (Vabariigi Valitsus) — Automaatse biomeetrilise isikutuvastuse süsteemi…, 2026-04-18. Automaatse biomeetrilise isikutuvastuse süsteemi andmekogu põhimäärus. <https://web.archive.org/web/20260418112026/https://www.riigiteataja.ee/akt/131122021018>
[^s23]: Siseministeerium (Ministry of the Interior) — Automaatse biomeetrilise isikutuvastuse süsteemi…. Automaatse biomeetrilise isikutuvastuse süsteemi andmekogu ABIS. <https://www.siseministeerium.ee/abis> ([archived](https://web.archive.org/web/20260811150453/https://www.siseministeerium.ee/abis))
[^s24]: Riigi Infosüsteemi Amet (Information System Authority) — Riigi Infosüsteemi Ameti teenustaseme leppe vorm – Riigi…, 2025-02. Riigi Infosüsteemi Ameti teenustaseme leppe vorm – Riigi autentimisteenus (TARA). <https://www.ria.ee/sites/default/files/documents/2025-02/TARA-SLA-Riigi-autentimisteenus-1-3-2025.pdf>
[^s25]: Riigi Teataja — Isikut tõendavate dokumentide seadus (consolidated text,…, 2026-03-09. Isikut tõendavate dokumentide seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260309063502/https://www.riigiteataja.ee/akt/ITDS>
[^s26]: Siseministeerium (Ministry of the Interior) — Isikut tõendavad dokumendid ja identiteedihaldus. Isikut tõendavad dokumendid ja identiteedihaldus. <https://www.siseministeerium.ee/tegevusvaldkonnad/tohus-rahvastikuhaldus/isikut-toendavad-dokumendid-ja-identiteedihaldus> ([archived](https://web.archive.org/web/20260703201829/https://www.siseministeerium.ee/tegevusvaldkonnad/tohus-rahvastikuhaldus/isikut-toendavad-dokumendid-ja-identiteedihaldus))
[^s27]: Riigi Teataja — Riigikogu valimise seadus (consolidated text, Riigi…, 2026-02-18. Riigikogu valimise seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260218005759/https://www.riigiteataja.ee/akt/RKVS>
[^s28]: Registrite ja Infosüsteemide Keskus (RIK) — E-kinnistusraamat. E-kinnistusraamat. <https://www.rik.ee/et/e-kinnistusraamat/e-kinnistusraamat> ([archived](https://web.archive.org/web/20260829055311/https://www.rik.ee/et/e-kinnistusraamat/e-kinnistusraamat))
[^s29]: Registrite ja Infosüsteemide Keskus (RIK) — Päring karistusregistrist. Päring karistusregistrist. <https://www.rik.ee/et/karistusregister/paring-karistusregistrist> ([archived](https://web.archive.org/web/20260902232345/https://www.rik.ee/et/karistusregister/paring-karistusregistrist))
[^s30]: Justiits- ja Digiministeerium — Isikuandmete töötlemine, 2026-08. Isikuandmete töötlemine. <https://web.archive.org/web/20260824074134/https://www.justdigi.ee/isikuandmete-tootlemine>
[^s31]: Riigi Teataja — Karistusregistri seadus (consolidated text, Riigi…, 2025-08-03. Karistusregistri seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20250803214052/https://www.riigiteataja.ee/akt/KarRS>
[^s32]: Riigi Teataja — Politsei andmekogu pidamise põhimäärus, 2025-12-12. Politsei andmekogu pidamise põhimäärus. <https://web.archive.org/web/20251212223739/https://www.riigiteataja.ee/akt/113012017004>
[^s33]: Riigi Teataja — Elamislubade ja töölubade registri põhimäärus, 2025-05-14. Elamislubade ja töölubade registri põhimäärus. <https://web.archive.org/web/20250514142132/https://www.riigiteataja.ee/akt/114012017018>
[^s34]: Riigi Teataja — Maksukorralduse seadus (consolidated text, Riigi Teataja…, 2026-02-07. Maksukorralduse seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260207063839/https://www.riigiteataja.ee/akt/MKS>
[^s35]: Maksu- ja Tolliamet (Tax and Customs Board) — MTA võtab kasutusele uue impordi tollivormistuse…, 2021. MTA võtab kasutusele uue impordi tollivormistuse infosüsteemi. <https://www.emta.ee/uudised/mta-votab-kasutusele-uue-impordi-tollivormistuse-infosusteemi>
[^s36]: Riigi Teataja — Sotsiaalkaitse infosüsteemi põhimäärus, 2022-10-24. Sotsiaalkaitse infosüsteemi põhimäärus. <https://web.archive.org/web/20221024144600/https://www.riigiteataja.ee/akt/108052020012>
[^s37]: Riigi Teataja — Tervisekassa andmekogu pidamise põhimäärus, 2024-11-24. Tervisekassa andmekogu pidamise põhimäärus. <https://web.archive.org/web/20241124195714/https://www.riigiteataja.ee/akt/107052024007>
[^s38]: Registrite ja Infosüsteemide Keskus (RIK) — E-äriregistri portaal. E-äriregistri portaal. <https://www.rik.ee/et/e-ariregister/e-ariregistri-portaal> ([archived](https://web.archive.org/web/20260829032113/https://www.rik.ee/et/e-ariregister/e-ariregistri-portaal))
[^s39]: Riigi Teataja — Rahapesu ja terrorismi rahastamise tõkestamise seadus…, 2026-03-06. Rahapesu ja terrorismi rahastamise tõkestamise seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260306092107/https://www.riigiteataja.ee/akt/RahaPTS>
[^s40]: Riigi Teataja — Schengeni infosüsteemi riikliku registri pidamise põhimäärus, 2025-10-22. Schengeni infosüsteemi riikliku registri pidamise põhimäärus. <https://web.archive.org/web/20251022021813/https://www.riigiteataja.ee/akt/118042013027>
[^s41]: Politsei- ja Piirivalveamet (Police and Border Guard Board) — Avaandmete seletuskiri – Teenistus- ja tsiviilrelvade…, 2020-06-05. Avaandmete seletuskiri – Teenistus- ja tsiviilrelvade register. <https://www.politsei.ee/files/Anal%C3%BC%C3%BCs%20ja%20statistika/ppa-avaandmete-seletuskiri-relvaregister-05.06.20.pdf>
[^s42]: Riigi Tugiteenuste Keskus (State Shared Service Centre) — Riigitöötaja iseteenindusportaal. Riigitöötaja iseteenindusportaal. <https://www.rtk.ee/riigitootaja-iseteenindusportaal> ([archived](https://web.archive.org/web/20260829052208/https://www.rtk.ee/riigitootaja-iseteenindusportaal))
[^s43]: Siseministeerium (Ministry of the Interior) — Riiklik avalikkuse hoiatamise süsteem ja ohuteavitus…, 2024-02-07. Riiklik avalikkuse hoiatamise süsteem ja ohuteavitus Eestis (EE-ALARM ülevaade). <https://www.siseministeerium.ee/sites/default/files/documents/2024-02/EE-ALARM_ylevaade_avalik_07022024.pdf>
[^s44]: Häirekeskus — Häirekeskus liigub üle uuele domeeninimele ja e-posti…, 2026-01-30. Häirekeskus liigub üle uuele domeeninimele ja e-posti aadressidele. <https://www.112.ee/et/uudised/haeirekeskus-liigub-uele-uuele-domeeninimele-ja-e-posti-aadressidele-170> ([archived](https://web.archive.org/web/20260514065117/https://www.112.ee/et/uudised/haeirekeskus-liigub-uele-uuele-domeeninimele-ja-e-posti-aadressidele-170))
[^s45]: Elering AS — Juhtimiskeskus, 2025-05-09. Juhtimiskeskus. <https://www.elering.ee/juhtimiskeskus>
[^s46]: Haridus- ja Teadusministeerium — EHIS - Eesti Hariduse Infosüsteem. EHIS - Eesti Hariduse Infosüsteem. <https://www.ehis.ee/> ([archived](https://web.archive.org/web/20260824092833/https://www.ehis.ee/))
[^s47]: Haridus- ja Teadusministeerium — Eesti keele tasemeeksamiks ettevalmistava…, 2024-07. Eesti keele tasemeeksamiks ettevalmistava täienduskoolituse tegevusloa taotlemise kirjeldus. <https://www.hm.ee/sites/default/files/documents/2024-07/Eesti%20keele%20tasemeeksamiks%20ettevalmistava%20t%C3%A4ienduskoolituse%20tegevusloa%20taotlemise%20kirjeldus.pdf>
[^s48]: Registrite ja Infosüsteemide Keskus (RIK) — Riigi Teataja. Riigi Teataja. <https://www.rik.ee/et/muud-teenused/riigi-teataja> ([archived](https://web.archive.org/web/20260312042839/https://www.rik.ee/et/muud-teenused/riigi-teataja))

**Evidence grades:** 3 Strong, 50 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
