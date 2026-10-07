# Slovenia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Slovenia could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4] |
| State-controlled national eID | Yes[^s3][^s5][^s6][^s4] |
| Government data centres | Yes[^s7] |
| Government cloud in operation | Yes[^s8][^s9][^s10] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 27 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Slovenia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 2.135 million[^s11] |
| GDP, current prices | 71.2 EUR bn[^s12] |
| Public administration employment (NACE O) | 51.1 thousand[^s13] |
| Non-household electricity price | 150.3 EUR/MWh[^s14] |
| Renewables share of electricity | 45.6 %[^s15] |
| Land area | 20 145 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Slovenia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 34 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | The Central Population Register (CRP) is the central database of basic population data for Slovenia[^s17][^s18] | CRP is managed by the Ministry of the Interior[^s17][^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | The ID card issuance register stores the digital photograph, but in a form that biometric readers cannot read[^s19] | The interior ministry manages the ID card issuance register centrally[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The source shows fingerprints ARE held in the centrally managed register of issued identity cards for 15 days (90 if undelivered) before deletion; it does not state that no central register exists and covers only ID cards, so 'No central…. It is withheld until the fact or its source is corrected and checked again* | — | — | — | — |
| Critical | Breeder document scans (tier 0) | The collection of documents underlying civil status entries is part of the civil status register[^s20] | *Not yet sourced* | Parts or all of the document collection may be kept in the register's central computerised database[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | The register records production and delivery dates and the validity status of each ID card[^s19] | The interior ministry manages the ID card issuance register centrally[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Authentication audit log (tier 0) | SI-PASS keeps registered-user records including account usage data[^s21] | Controller: Ministry of the Interior and Public Administration, SI-TRUST[^s21] | Processed on Slovenian territory; no transfers to third countries[^s21] | National infrastructure[^s21] | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Voting rights are recorded in the register of voting rights, kept within the permanent-residence register and CRP[^s22][^s18] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | 1.695.249 voters entered in the electoral rolls[^s23] |
| High | Land & property registry (tier 1) | The Land Register is a public book of rights in real property, kept by the district courts[^s24] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | kazenska evidenca (criminal record)[^s25] | Ministrstvo za pravosodje (Ministry of Justice)[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Police records include criminal offences, misdemeanours and wanted persons[^s27] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | SI-PASS is the single identity-verification and e-signature service for citizens, businesses and civil servants[^s3][^s5] | SI-TRUST operates within the Ministry of the Interior and Public Administration[^s4] | SI-PASS personal data are not transferred to third countries and are processed on Slovenian territory[^s21] | National infrastructure[^s21] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | SI-TRUST manages the SI-TRUST Root and the qualified issuers SIGEN-CA and SIGOV-CA[^s3][^s4] | SI-TRUST operates within the Ministry of the Interior and Public Administration[^s3][^s4] | Qualified SI-PASS-CA signing certificates are stored at SI-TRUST[^s5] | National infrastructure[^s28][^s5] | *Not yet measured* |
| High | Residence and migration status (tier 1) | The interior ministry manages the central register of residence permits and their revocations (Register tujcev)[^s18][^s29] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | The tax register is a single computerised, linked database of taxpayers[^s30] | Under the Financial Administration Act (ZFU), FURS keeps and manages the tax register[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | FURS runs the SIAIS2 import declaration system; a centralised-clearance upgrade was ordered in 2024[^s31] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | 1.146.962 customs declarations accepted in 2025[^s32] |
| High | Benefits & pensions (tier 1) | matična evidenca o zavarovancih in uživalcih pravic (master record of insured persons and beneficiaries)[^s33] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | ZZZS keeps the register of persons covered by compulsory health insurance[^s34] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | About 2.1 million insured persons (2025)[^s35] |
| High | Business registry (tier 1) | Poslovni register Slovenije (PRS) (Slovenian Business Register)[^s36] | AJPES[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | The RDL is a database of beneficial owners, kept for ownership transparency and AML purposes[^s37][^s38] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | evidenca registriranih vozil (register of registered vehicles)[^s39] | Ministrstvo za infrastrukturo (Ministry of Infrastructure)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | SIS consists of a central system and national SIS systems in the member states, linked by a network[^s41] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | UJP provides payment services to budget users and keeps the register of budget users and their sub-accounts[^s42][^s43] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | TARGET services settle large-value payments, securities transactions and instant payments[^s44][^s45] | *Not yet sourced* | *Not yet sourced* | EU provider[^s44][^s45] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Regional notification centres receive and process 112 emergency calls[^s46] | *Not yet sourced* | The contractor was a bidder group represented by Telekom Slovenije[^s47] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | NCKU provides premises, IT and telecom conditions for the government in crises threatening national security[^s48] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | ELES ensures safe, reliable and efficient operation of the transmission and distribution system[^s49] | Under ZOEE, ELES performs the mandatory public service of combined transmission and distribution system operator[^s50][^s49] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | Vodni kataster (water cadastre)[^s51] | *Disputed: the fact check (claude-fable-5-1, run wf_b66a7125-0d9) did not confirm this: The page says only that ARSO carries out the tasks of the state hydrological service (monitoring, forecasting and warning of hydrological conditions); it says nothing about operating water management control or the water cadastre, which…. It is withheld until the fact or its source is corrected and checked again* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Education (tier 1) | The register is kept in the application 'Centralna evidenca udeležencev vzgoje in izobraževanja'[^s52] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Firearms register (tier 1) | The central register of issued firearms documents combines the registers kept by the competent bodies[^s53] | *Not yet sourced* | Registers are kept on the interior ministry's central computer[^s53] | National infrastructure[^s53] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Pravni informacijski sistem Republike Slovenije (PISRS) (Legal Information System of the Republic of Slovenia), sole publication platform of the Uradni list RS[^s54] | Služba Vlade Republike Slovenije za zakonodajo (Government Legislation Office)[^s54] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Government payroll and personnel (tier 1) | MFERAC supports budget users in finance, accounting and payroll/HR[^s55][^s56] | *Not yet sourced* | *Not yet sourced* | National infrastructure[^s56] | *Not yet measured* |
| Standard | Health records (tier 2) | CRPP is the single system for collecting and exchanging health data on patients in Slovenia[^s57] | NIJZ is responsible for the CeZZ information system, its maintenance and security[^s58] | Central health ICT is a public service run by a public company wholly owned by the Republic of Slovenia[^s58] | National infrastructure[^s58] | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | e-ARH.si is the Slovenian electronic archive for long-term preservation of electronic archival records[^s59] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | The electronic register of vaccinated persons and adverse events (eRCO) has operated since 2017[^s60] | *Not yet sourced* | The state-owned public company is the contractual processor for the public-health collections (Art. 22(2))[^s58] | National infrastructure[^s58] | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 33 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 7 |
| EU provider | 1 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 25 |

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

> Not yet sized. Capacity for Slovenia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Slovenia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)

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

### The verdict on each fact about Slovenia

76 of 76 printed facts about Slovenia pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:SI:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SI:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SI:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SI:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SI:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SI:population_m | param:SI:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:SI:gdp_eur_bn | param:SI:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SI:gov_employment_k | param:SI:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SI:elec_price_eur_mwh | param:SI:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SI:renewables_pct | param:SI:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SI:land_km2 | param:SI:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:breeder_documents:hosting | Breeder document scans: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:SI:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:authentication_audit_log:operator | Authentication audit log: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:authentication_audit_log:hosting | Authentication audit log: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:SI:authentication_audit_log:foreign_dependency | Authentication audit log: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:electoral_roll:count | Electoral roll entry: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:SI:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:SI:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:digital_identity_credentials:hosting | Digital identity credentials: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:SI:digital_identity_credentials:foreign_dependency | Digital identity credentials: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:trust_services_pki:hosting | State PKI and qualified trust services: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:SI:trust_services_pki:foreign_dependency | State PKI and qualified trust services: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:SI:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:tax:operator | Tax: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:customs:count | Customs declarations: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:health_insurance:count | Statutory health insurance: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:SI:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:SI:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:central_bank:foreign_dependency | Central bank systems: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:emergency_communications:hosting | Emergency calls and public-safety radio: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:SI:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:water_control:register | Water management control: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:SI:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:firearms_register:hosting | Firearms register: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:SI:firearms_register:foreign_dependency | Firearms register: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:government_payroll:foreign_dependency | Government payroll and personnel: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:health_records:operator | Health records: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:health_records:hosting | Health records: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:SI:health_records:foreign_dependency | Health records: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:national_archives:register | National archives (digital): the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SI:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_c38b3e2e-319 |
| record:SI:public_health_surveillance:hosting | Public health surveillance: hosting | unrecorded | claude-fable-5-1 | supported | wf_c38b3e2e-319 |
| record:SI:public_health_surveillance:foreign_dependency | Public health surveillance: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_c38b3e2e-319 |

### Withheld after the fact check: Slovenia

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:SI:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | claude-fable-5-1 | not supported | The source shows fingerprints ARE held in the centrally managed register of issued identity cards for 15 days (90 if undelivered) before deletion; it does not state that no central register exists and covers only ID cards, so 'No central register' is not what the page says. |
| record:SI:water_control:operator | Water management control: the body that operates it | claude-fable-5-1 | not supported | The page says only that ARSO carries out the tasks of the state hydrological service (monitoring, forecasting and warning of hydrological conditions); it says nothing about operating water management control or the water cadastre, which the paired register fact places on the Direkcija za vode page. Hydrological service is a different scope from the printed 'water management control' operator. |

---

[^s1]: Urad Vlade Republike Slovenije za varovanje tajnih podatkov — Tajni podatki, 2026-03-26. Tajni podatki. <https://www.gov.si/teme/tajni-podatki/> ([archived](https://web.archive.org/web/20260518182748/https://www.gov.si/teme/tajni-podatki/))
[^s2]: Uradni list Republike Slovenije — Zakon o tajnih podatkih (uradno prečiščeno besedilo)…, 2006-05-16. Zakon o tajnih podatkih (uradno prečiščeno besedilo) (ZTP-UPB2), 13. člen. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2006-01-2128/zakon-o-tajnih-podatkih-uradno-precisceno-besedilo-ztp-upb2>
[^s3]: Ministrstvo za notranje zadeve und javno upravo — Sektor za storitve zaupanja, 2026-08-10. Sektor za storitve zaupanja. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-notranje-zadeve-in-javno-upravo/o-ministrstvu/direktorat-za-informatiko/urad-za-razvoj-digitalnih-resitev/sektor-za-storitve-zaupanja/>
[^s4]: SI-TRUST / Državni center za storitve zaupanja — O nas - SI-TRUST. O nas - SI-TRUST. <https://www.si-trust.gov.si/sl/o-nas> ([archived](https://web.archive.org/web/20260727081457/https://www.si-trust.gov.si/sl/o-nas))
[^s5]: SI-TRUST / Državni center za storitve zaupanja — Spletna prijava in e-podpis (SI-PASS). Spletna prijava in e-podpis (SI-PASS). <https://www.si-trust.gov.si/sl/si-pass> ([archived](https://web.archive.org/web/20260727081439/https://www.si-trust.gov.si/sl/si-pass))
[^s6]: SI-TRUST / Državni center za storitve zaupanja — Elektronska osebna izkaznica. Elektronska osebna izkaznica. <https://www.si-trust.gov.si/sl/eoi> ([archived](https://web.archive.org/web/20260615134158/https://www.si-trust.gov.si/sl/eoi))
[^s7]: Ministrstvo za notranje zadeve in javno upravo (GOV.SI) — Sektor za podatkovno in strežniško infrastrukturo. Sektor za podatkovno in strežniško infrastrukturo. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-notranje-zadeve-in-javno-upravo/o-ministrstvu/direktorat-za-informatiko/urad-za-digitalno-infrastrukturo/sektor-za-podatkovno-in-streznisko-infrastrukturo/>
[^s8]: Ministrstvo za javno upravo — Vzdrževanje državnega računalniškega oblaka (DRO - VMware), 2026-03-25. Vzdrževanje državnega računalniškega oblaka (DRO - VMware). <https://www.gov.si/zbirke/javne-objave/vzdrzevanje-drzavnega-racunalniskega-oblaka-dro-vmware-260317002023/>
[^s9]: Ministrstvo za notranje zadeve in javno upravo (GOV.SI) — Sektor za virtualizacijo in orkestracijo. Sektor za virtualizacijo in orkestracijo. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-notranje-zadeve-in-javno-upravo/o-ministrstvu/direktorat-za-informatiko/urad-za-digitalno-infrastrukturo/sektor-za-virt/>
[^s10]: Ministrstvo za notranje zadeve in javno upravo (GOV.SI) — Informatika v državni upravi. Informatika v državni upravi. <https://www.gov.si/teme/informatika-v-drzavni-upravi/>
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Ministrstvo za notranje zadeve (CRP portal) — Predstavitev CRP - CRP portal. Predstavitev CRP - CRP portal. <https://ecrp.gov.si/predstavitevCRP.html> ([archived](https://web.archive.org/web/20250527084027/https://ecrp.gov.si/predstavitevCRP.html))
[^s18]: Ministrstvo za notranje zadeve in javno upravo — Registri in evidence prebivalstva, 2026-08-17. Registri in evidence prebivalstva. <https://www.gov.si/teme/registri-in-evidence-prebivalstva/> ([archived](https://web.archive.org/web/20260314092109/https://www.gov.si/teme/registri-in-evidence-prebivalstva/))
[^s19]: Uradni list Republike Slovenije — Zakon o spremembah in dopolnitvah Zakona o osebni…, 2025-03-18. Zakon o spremembah in dopolnitvah Zakona o osebni izkaznici (ZOIzk-1C), Uradni list RS, št. 17/2025. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-0584> ([archived](https://web.archive.org/web/20260510231526/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-0584))
[^s20]: Uradni list Republike Slovenije — Zakon o matičnem registru (uradno prečiščeno besedilo)…, 2011-02-21. Zakon o matičnem registru (uradno prečiščeno besedilo) (ZMatR-UPB2), Uradni list RS, št. 11/2011. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-0451> ([archived](https://web.archive.org/web/20231115081008/http://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-0451))
[^s21]: SI-TRUST / Ministrstvo za notranje zadeve in javno upravo — Obvestilo posameznikom glede obdelave osebnih podatkov…. Obvestilo posameznikom glede obdelave osebnih podatkov storitve SI-PASS. <https://www.si-trust.gov.si/sl/si-pass-obvestilo-posameznikom>
[^s22]: GOV.SI (Ministrstvo za notranje zadeve) — Volivci in evidenca volilne pravice. Volivci in evidenca volilne pravice. <https://www.gov.si/teme/volivci-in-evidenca-volilne-pravice/> ([archived](https://web.archive.org/web/20260518161634/https://www.gov.si/teme/volivci-in-evidenca-volilne-pravice/))
[^s23]: Državna volilna komisija — Volitve v Državni zbor 2026, 2026. Volitve v Državni zbor 2026. <https://www.dvk-rs.si/volitve-in-referendumi/drzavni-zbor-rs/volitve-drzavnega-zbora-rs/volitve-v-drzavni-zbor/> ([archived](https://web.archive.org/web/20260728104354/https://www.dvk-rs.si/volitve-in-referendumi/drzavni-zbor-rs/volitve-drzavnega-zbora-rs/volitve-v-drzavni-zbor/))
[^s24]: Sodstvo Republike Slovenije — Zemljiška knjiga - javne knjige. Zemljiška knjiga - javne knjige. <https://www.sodisce.si/javne_knjige/zemljiska_knjiga/> ([archived](https://web.archive.org/web/20260720094305/https://www.sodisce.si/javne_knjige/zemljiska_knjiga/))
[^s25]: Ministrstvo za pravosodje (GOV.SI) — Izpis iz kazenske evidence, evidence vzgojnih ukrepov in…. Izpis iz kazenske evidence, evidence vzgojnih ukrepov in evidence izbrisanih obsodb za kazniva dejanja zoper spolno nedotakljivost (Potrdilo o (ne)kaznovanosti). <https://www.gov.si/zbirke/storitve/izpis-iz-kazenske-evidence-evidence-vzgojnih-ukrepov-in-evidence-izbrisanih-obsodb-za-kazniva-dejanja-zoper-spolno-nedotakljivost-potrdilo-o-nekaznovanosti/> ([archived](https://web.archive.org/web/20260412003548/https://www.gov.si/zbirke/storitve/izpis-iz-kazenske-evidence-evidence-vzgojnih-ukrepov-in-evidence-izbrisanih-obsodb-za-kazniva-dejanja-zoper-spolno-nedotakljivost-potrdilo-o-nekaznovanosti/))
[^s26]: Ministrstvo za pravosodje — Kazenskopravne evidence, 2024-03-22. Kazenskopravne evidence. <https://www.gov.si/teme/kazenskopravne-evidence/> ([archived](https://web.archive.org/web/20260519042322/https://www.gov.si/teme/kazenskopravne-evidence/))
[^s27]: Uradni list Republike Slovenije — Zakon o nalogah in pooblastilih policije (ZNPPol),…, 2013-02-18. Zakon o nalogah in pooblastilih policije (ZNPPol), Uradni list RS, št. 15/2013. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2013-01-0435/> ([archived](https://web.archive.org/web/20260119082921/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2013-01-0435/))
[^s28]: Državni center za storitve zaupanja SI-TRUST (Ministrstvo za digitalno preobrazbo) — Krovna politika SI-TRUST za izdajatelje, ki delujejo v…, 2025-12. Krovna politika SI-TRUST za izdajatelje, ki delujejo v okviru ponudnika storitev zaupanja SI-TRUST, verzija 1.7. <https://www.si-trust.gov.si/assets/Politike/si-trust-krovna/verzija-1-7/SI-TRUST-krovna-v1.7-2025p.pdf> ([archived](https://web.archive.org/web/20260609141651/https://www.si-trust.gov.si/assets/Politike/si-trust-krovna/verzija-1-7/SI-TRUST-krovna-v1.7-2025p.pdf))
[^s29]: Uradni list Republike Slovenije — Zakon o tujcih (uradno prečiščeno besedilo)…, 2021-06-07. Zakon o tujcih (uradno prečiščeno besedilo) (ZTuj-2-UPB9), Uradni list RS, št. 91/2021. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2021-01-1957> ([archived](https://web.archive.org/web/20260216110731/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2021-01-1957/))
[^s30]: Finančna uprava Republike Slovenije — Vpis v davčni register in davčna številka. Vpis v davčni register in davčna številka. <https://www.fu.gov.si/davki_in_druge_dajatve/poslovanje_z_nami/vpis_v_davcni_register_in_davcna_stevilka/> ([archived](https://web.archive.org/web/20260520064339/https://www.fu.gov.si/davki_in_druge_dajatve/poslovanje_z_nami/vpis_v_davcni_register_in_davcna_stevilka/))
[^s31]: Finančna uprava Republike Slovenije — Letno poročilo Finančne uprave za leto 2024, 2025. Letno poročilo Finančne uprave za leto 2024. <https://www.gov.si/assets/organi-v-sestavi/FURS/Strateski-dokumenti/2025/Letno-porocilo-Financne-uprave-za-leto-2024.pdf> ([archived](https://web.archive.org/web/20260916213111/https://www.gov.si/assets/organi-v-sestavi/FURS/Strateski-dokumenti/2025/Letno-porocilo-Financne-uprave-za-leto-2024.pdf))
[^s32]: Finančna uprava Republike Slovenije — Letno poročilo Finančne uprave za leto 2025, 2026-02. Letno poročilo Finančne uprave za leto 2025. <https://www.gov.si/assets/organi-v-sestavi/FURS/Strateski-dokumenti/2026/Letno-porocilo-Financne-uprave-za-leto-2025.pdf>
[^s33]: Zavod za pokojninsko in invalidsko zavarovanje Slovenije (ZPIZ) — O zavodu. O zavodu. <https://www.zpiz.si/cms/?ids=content2019&inf=1191> ([archived](https://web.archive.org/web/20260710194720/https://www.zpiz.si/cms/?ids=content2019&inf=1191))
[^s34]: Zavod za zdravstveno zavarovanje Slovenije — Evidenca o zavarovanih osebah (katalog zbirke). Evidenca o zavarovanih osebah (katalog zbirke). <https://www.zzzs.si/fileadmin/user_upload/dokumenti/informacije_in_publikacije/evidenca_o_zavarovanih_osebah.pdf> ([archived](https://web.archive.org/web/20240802165003/https://www.zzzs.si/fileadmin/user_upload/dokumenti/informacije_in_publikacije/evidenca_o_zavarovanih_osebah.pdf))
[^s35]: Zavod za zdravstveno zavarovanje Slovenije — Poslovanje ZZZS v letu 2025, 2026. Poslovanje ZZZS v letu 2025. <https://zavezanec.zzzs.si/fileadmin/user_upload/dokumenti/novice/2026/zzzsporocilo2025-infografika-web.pdf>
[^s36]: AJPES — Poslovni register Slovenije – Splošno. Poslovni register Slovenije – Splošno. <https://www.ajpes.si/registri/poslovni_register/splosno> ([archived](https://web.archive.org/web/20260912024435/https://www.ajpes.si/registri/poslovni_register/splosno))
[^s37]: AJPES — Register dejanskih lastnikov - Splošno. Register dejanskih lastnikov - Splošno. <https://www.ajpes.si/registri/drugi_registri/register_dejanskih_lastnikov/splosno>
[^s38]: Finančna uprava Republike Slovenije — Preverite vpis v register dejanskih lastnikov, 2026-09-24. Preverite vpis v register dejanskih lastnikov. <https://www.gov.si/novice/2026-09-24-preverite-vpis-v-register-dejanskih-lastnikov/>
[^s39]: eUprava (Republika Slovenija) — Registracija vozila. Registracija vozila. <https://e-uprava.gov.si/podrocja/promet/vozniki-in-vozila/registracija-vozila.html> ([archived](https://web.archive.org/web/20240615065317/https://e-uprava.gov.si/podrocja/promet/vozniki-in-vozila/registracija-vozila.html))
[^s40]: Ministrstvo za infrastrukturo in energetiko — Tehnični pregled in registracija vozil, 2026-06-04. Tehnični pregled in registracija vozil. <https://www.gov.si/teme/tehnicni-pregled-in-registracija-vozil/> ([archived](https://web.archive.org/web/20260518213157/https://www.gov.si/teme/tehnicni-pregled-in-registracija-vozil/))
[^s41]: GOV.SI (Ministrstvo za notranje zadeve) — Prenovljeni Schengenski informacijski sistem, 2023-03-08. Prenovljeni Schengenski informacijski sistem. <https://www.gov.si/novice/2023-03-08-prenovljeni-schengenski-informacijski-sistem/> ([archived](https://web.archive.org/web/20230604005507/https://www.gov.si/novice/2023-03-08-prenovljeni-schengenski-informacijski-sistem/))
[^s42]: Uprava Republike Slovenije za javna plačila — Register proračunskih uporabnikov, 2026-04-13. Register proračunskih uporabnikov. <https://www.gov.si/teme/register-proracunskih-uporabnikov/> ([archived](https://web.archive.org/web/20251208071415/https://www.gov.si/teme/register-proracunskih-uporabnikov/))
[^s43]: GOV.SI (Uprava RS za javna plačila) — O Upravi Republike Slovenije za javna plačila. O Upravi Republike Slovenije za javna plačila. <https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-javna-placila/o-upravi/> ([archived](https://web.archive.org/web/20260517120748/https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-javna-placila/o-upravi/))
[^s44]: European Central Bank — TARGET Services. TARGET Services. <https://www.ecb.europa.eu/paym/target/html/index.en.html> ([archived](https://web.archive.org/web/20260917182025/https://www.ecb.europa.eu/paym/target/html/index.en.html))
[^s45]: Banka Slovenije — Plačilna infrastruktura. Plačilna infrastruktura. <https://www.bsi.si/sl/placilni-sistemi/placilna-infrastruktura>
[^s46]: GOV.SI (Uprava RS za zaščito in reševanje) — Urad za obveščanje in alarmiranje. Urad za obveščanje in alarmiranje. <https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/o-upravi/urad-za-obvescanje-in-alarmiranje/> ([archived](https://web.archive.org/web/20260323061511/https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/o-upravi/urad-za-obvescanje-in-alarmiranje/))
[^s47]: GOV.SI (Ministrstvo za notranje zadeve) — Po več letih bo zgrajena nova infrastruktura sistema TETRA, 2020-12-10. Po več letih bo zgrajena nova infrastruktura sistema TETRA. <https://www.gov.si/novice/2020-12-10-po-vec-letih-bo-zgrajena-nova-infrastruktura-sistema-tetra/>
[^s48]: GOV.SI (Ministrstvo za obrambo) — Nacionalni center za krizno upravljanje. Nacionalni center za krizno upravljanje. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-obrambo/o-ministrstvu/direktorat-za-obrambne-zadeve/nacionalni-center-za-krizno-upravljanje/> ([archived](https://web.archive.org/web/20250727032849/https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-obrambo/o-ministrstvu/direktorat-za-obrambne-zadeve/nacionalni-center-za-krizno-upravljanje/))
[^s49]: Portal Energetika (ministry responsible for energy) — ELES, d.o.o. sistemski operater prenosnega…. ELES, d.o.o. sistemski operater prenosnega elektroenergetskega omrežja. <https://www.energetika-portal.si/podrocja/energetika/upravljanje-kapitalskih-nalozb/eles/> ([archived](https://web.archive.org/web/20250516111733/https://www.energetika-portal.si/podrocja/energetika/upravljanje-kapitalskih-nalozb/eles/))
[^s50]: ELES, d. o. o. — ELES, d. o. o.. ELES, d. o. o.. <https://www.eles.si/>
[^s51]: Direkcija RS za vode (GOV.SI) — Direkcija Republike Slovenije za vode. Direkcija Republike Slovenije za vode. <https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-vode/> ([archived](https://web.archive.org/web/20260901222222/https://www.gov.si/drzavni-organi/organi-v-sestavi/direkcija-za-vode/))
[^s52]: Uradni list Republike Slovenije — Pravilnik o načinu in pogojih dostopa do podatkov iz…, 2011-06-03. Pravilnik o načinu in pogojih dostopa do podatkov iz centralne evidence udeležencev vzgoje in izobraževanja, Uradni list RS, št. 43/2011. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-2099> ([archived](https://web.archive.org/web/20240504214009/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-2099))
[^s53]: Uradni list Republike Slovenije — Zakon o orožju (ZOro-1), Uradni list RS, št. 61/2000, 2000-07-06. Zakon o orožju (ZOro-1), Uradni list RS, št. 61/2000. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2000-01-2747/zakon-o-orozju-zoro-1> ([archived](https://web.archive.org/web/20210924055842/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2000-01-2747/zakon-o-orozju-zoro-1))
[^s54]: Uradni list Republike Slovenije — O glasilu, 2026. O glasilu. <https://www.uradni-list.si/glasilo-uradni-list-rs/glasilo-uradni-list-rs/o-glasilu> ([archived](https://web.archive.org/web/20260608175302/https://www.uradni-list.si/glasilo-uradni-list-rs/glasilo-uradni-list-rs/o-glasilu))
[^s55]: GOV.SI (Ministrstvo za finance) — Sistem MFERAC. Sistem MFERAC. <https://www.gov.si/zbirke/storitve/mferac/>
[^s56]: Ministrstvo za finance — Prenova MFERAC, 2024-01-24. Prenova MFERAC. <https://www.gov.si/zbirke/projekti-in-programi/prenova-mferac/> ([archived](https://web.archive.org/web/20260216201728/https://www.gov.si/zbirke/projekti-in-programi/prenova-mferac/))
[^s57]: eZdravje (NIJZ) — CRPP - eZdravje. CRPP - eZdravje. <https://ezdrav.si/resitve/crpp/> ([archived](https://web.archive.org/web/20251015032134/https://ezdrav.si/resitve/crpp/))
[^s58]: Uradni list Republike Slovenije — Zakon o digitalizaciji zdravstva (ZDigZ), Uradni list…, 2025-12-04. Zakon o digitalizaciji zdravstva (ZDigZ), Uradni list RS, št. 100/2025. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-3387>
[^s59]: GOV.SI — Slovenski elektronski arhiv. Slovenski elektronski arhiv. <https://www.gov.si/teme/slovenski-elektronski-arhiv/> ([archived](https://web.archive.org/web/20260612043003/https://www.gov.si/teme/slovenski-elektronski-arhiv/))
[^s60]: Nacionalni inštitut za javno zdravje (NIJZ) — Elektronski register cepljenih oseb in neželenih učinkov…, 2025-11-06. Elektronski register cepljenih oseb in neželenih učinkov po cepljenju - eRCO. <https://nijz.si/nalezljive-bolezni/cepljenje/elektronski-register-cepljenih-oseb-in-nezelenih-ucinkov-po-cepljenju-erco/> ([archived](https://web.archive.org/web/20260210081857/https://nijz.si/nalezljive-bolezni/cepljenje/elektronski-register-cepljenih-oseb-in-nezelenih-ucinkov-po-cepljenju-erco/))

**Evidence grades:** 6 Strong, 70 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
