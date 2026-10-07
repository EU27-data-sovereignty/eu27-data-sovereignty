# Italy: critical data holdings and sovereign hosting

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

> Secured in law, not yet in practice. Confidence: Low. With the evidence still open, Italy could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Yes[^s1][^s2] |
| Classification in law | Yes[^s3][^s1] |
| Sovereign cloud certification | Partly[^s1] |
| State-controlled trust anchor | Yes[^s4] |
| State-controlled national eID | Yes[^s5][^s6][^s4] |
| Government data centres | Yes[^s2] |
| Government cloud in operation | *Not yet sourced* |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Italy described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 58.943 million[^s7] |
| GDP, current prices | 2 265.0 EUR bn[^s8] |
| Public administration employment (NACE O) | 1 213.1 thousand[^s9] |
| Non-household electricity price | 220.3 EUR/MWh[^s10] |
| Renewables share of electricity | 43.5 %[^s11] |
| Land area | 297 823 km²[^s12] |

## 3. Critical data holdings, by priority

The holdings Italy cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 28 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | ANPR (National Register of the Resident Population) is the Ministry of the Interior's single database for population data[^s13][^s14] | Ministry of the Interior; Sogei S.p.A. provides the technical operation[^s13][^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| Critical | Fingerprint biometric (tier 0) | No permanent central register: fingerprint images are held in the banca dati del CP-CIE e di SSCE (database of the CIE production centre and of the CNSD services system) only for the time strictly necessary to produce the CIE[^s16] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: Both quotes are verbatim and support 'ANSC - national computerised archive of civil-status registers', but neither the ANSC guide page nor art. 62 CAD says the registers are those of births, marriages and deaths; the printed parenthetical…. It is withheld until the fact or its source is corrected and checked again* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Facial biometric (tier 0) | The CIE electronic record card (cartellino elettronico), kept by SSCE, holds the holder's photograph, signature scan and registry data[^s17] | Centro Nazionale dei Servizi Demografici (CNSD), Ministry of the Interior[^s17] | *Not yet sourced* | National infrastructure[^s17] | *Not yet measured* |
| High | Digital identity credentials (tier 0) | SPID (sistema pubblico per la gestione dell'identità digitale di cittadini e imprese – public digital identity system)[^s18] | Open set of public and private entities accredited by AgID[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Anagrafe Immobiliare Integrata (Integrated Property Register)[^s19] | Agenzia del Territorio (Land Agency)[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | casellario giudiziale (criminal records register)[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Centro elaborazione dati (Data Processing Centre, the inter-force police database)[^s21] | Ministero dell'interno (Ministry of the Interior)[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The CIE database is part of the CNSD infrastructure[^s17] | Only the Ministry of the Interior may issue the CIE[^s6][^s22] | The CIE issuance circuit (SSCE) runs on IT infrastructure located in the Ministry of the Interior's CNSD[^s17] | National infrastructure[^s17] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | The CNSD 'CA Autenticazione' is the Ministry of the Interior's certification authority that issues online-authentication certificates for the CIE[^s17] | AgID is Italy's supervisory authority for qualified trust service providers[^s23] | The CIE certification authority (CA Autenticazione and PKI-CIE) is part of the IT infrastructure located in the CNSD[^s17] | National infrastructure[^s17] | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Tax (tier 1) | Anagrafe tributaria (national tax register)[^s24] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | AIDA (Integrated Customs and Excise Automation) data warehouse of the Customs and Monopolies Agency[^s25] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | casellario centrale dei pensionati (central register of pensioners)[^s26] | Istituto nazionale della previdenza sociale (INPS)[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | The National Register of Patients (ANA) is the reference register for public health, run within Sistema Tessera Sanitaria[^s27][^s28] | ANA is built by the Ministry of Economy and Finance in agreement with the Ministry of Health[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Registro delle imprese (Register of Companies)[^s29] | Camera di commercio (chambers of commerce)[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Apposita sezione del Registro delle imprese (dedicated beneficial-ownership section of the Register of Companies)[^s30] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | archivio nazionale dei veicoli (national vehicle archive)[^s31] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | SIOPE monitors the receipts and payments made by the treasurers of all public administrations[^s32][^s33] | The SIOPE+ infrastructure is operated by the Banca d'Italia[^s32][^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | NoiPA[^s34] | Dipartimento dell'Amministrazione Generale del personale e dei servizi (DAG), Ministero dell'Economia e delle Finanze (MEF)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | The historical election archive is an online database of election results down to municipality level[^s35] | The Central Directorate for Electoral Services publishes turnout and results data[^s35][^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | BI‑Comp (national multilateral clearing system)[^s37] | Banca d'Italia[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | IT-alert is the public warning service that sends messages to devices in an area hit by a serious emergency[^s38][^s39] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | Anagrafe nazionale dell'istruzione (ANIST) (National Education Register)[^s40] | Ministero dell'istruzione (Ministry of Education)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | The electronic health record (FSE) holds the patient's clinical data and documents[^s41][^s42] | The FSE is set up by the regions and autonomous provinces[^s41][^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The printed Gazzetta Ufficiale is the only definitive text and prevails over the digital version[^s43] | IPZS publishes the Gazzetta Ufficiale in digital form[^s43] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | The Central State Archive is building the repository for digital archives produced by central state bodies[^s44] | *Not yet sourced* | The Digital Preservation Hub is described as a 'natively cloud' infrastructure; no provider is named[^s44] | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet sourced* | ISTAT is the main producer of official statistics[^s45][^s46] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 28 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 3 |
| EU provider | 0 |
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

> Not yet sized. Capacity for Italy will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Italy without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- Residence and migration status (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
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

### The verdict on each fact about Italy

61 of 61 printed facts about Italy pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:IT:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:IT:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:IT:L3 | indicator L3: Is a cloud certification that requires immunity from non-EU law in force or adopted for government use? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:IT:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:IT:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_c38b3e2e-319 |
| indicator:IT:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IT:population_m | param:IT:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:IT:gdp_eur_bn | param:IT:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IT:gov_employment_k | param:IT:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IT:elec_price_eur_mwh | param:IT:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IT:renewables_pct | param:IT:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IT:land_km2 | param:IT:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_b66a7125-0d9 |
| record:IT:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:facial_biometric:foreign_dependency | Facial biometric: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:police_records:operator | Police information systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_c38b3e2e-319 |
| record:IT:issuance_history:hosting | Document issuance history: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:IT:issuance_history:foreign_dependency | Document issuance history: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:trust_services_pki:hosting | State PKI and qualified trust services: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:IT:trust_services_pki:foreign_dependency | State PKI and qualified trust services: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:government_payroll:operator | Government payroll and personnel: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:electoral_management:operator | Election management and results: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:central_bank:operator | Central bank systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:education:operator | Education: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:health_records:operator | Health records: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:national_archives:register | National archives (digital): the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IT:national_archives:hosting | National archives (digital): hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:IT:statistics_microdata:operator | Statistical microdata: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Italy

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:IT:breeder_documents:register | Breeder document scans: the name of the register or system | claude-fable-5-1 | not supported | Both quotes are verbatim and support 'ANSC - national computerised archive of civil-status registers', but neither the ANSC guide page nor art. 62 CAD says the registers are those of births, marriages and deaths; the printed parenthetical '(births, marriages, deaths)' is an addition the cited sources do not state (art. 62 mentions birth and death declarations only as ANPR services, not as ANSC con |

---

[^s1]: Agenzia per la cybersicurezza nazionale (ACN) — Regolamento per le infrastrutture digitali e per i…, 2024. Regolamento per le infrastrutture digitali e per i servizi cloud per la pubblica amministrazione (Regolamento ACN n. 21007/2024), Allegato 2, sezione 2. <https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud> ([archived](https://web.archive.org/web/20260807151428/https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud))
[^s2]: Normattiva (Istituto Poligrafico e Zecca dello Stato / Presidenza del Consiglio dei ministri) — Decreto-legge 18 ottobre 2012, n. 179, art. 33-septies…, 2012-10-18. Decreto-legge 18 ottobre 2012, n. 179, art. 33-septies (Consolidamento e razionalizzazione dei siti e delle infrastrutture digitali del Paese). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art33septies>
[^s3]: Agenzia per la cybersicurezza nazionale (ACN) — Strategia Cloud Italia. Strategia Cloud Italia. <https://www.acn.gov.it/portale/strategia-cloud-italia> ([archived](https://web.archive.org/web/20240918060056/https://www.acn.gov.it/portale/strategia-cloud-italia))
[^s4]: Agenzia per l'Italia Digitale (AgID), trusted list scheme operator — Italian Trusted List (TSL-IT), trust service provider…. Italian Trusted List (TSL-IT), trust service provider entry: Ministero dell'Interno. <https://eidas.agid.gov.it/TL/TSL-IT.xml> ([archived](https://web.archive.org/web/20260925060906/https://eidas.agid.gov.it/TL/TSL-IT.xml))
[^s5]: Ministero dell'Interno — Entra con CIE. Entra con CIE. <https://www.cartaidentita.interno.gov.it/info-utili/entra-con-cie/> ([archived](https://web.archive.org/web/20260822165458/https://www.cartaidentita.interno.gov.it/info-utili/entra-con-cie/))
[^s6]: Ministero dell'Interno — Cos'è la carta - Carta di Identità Elettronica (CIE). Cos'è la carta - Carta di Identità Elettronica (CIE). <https://www.cartaidentita.interno.gov.it/la-carta/> ([archived](https://web.archive.org/web/20260515172529/https://www.cartaidentita.interno.gov.it/la-carta/))
[^s7]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s8]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s9]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s10]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s11]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s12]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s13]: Ministero dell'Interno - Anagrafe Nazionale — Conosci l'ANPR. Conosci l'ANPR. <https://www.anagrafenazionale.interno.it/anpr/> ([archived](https://web.archive.org/web/20260927003857/https://www.anagrafenazionale.interno.it/anpr/))
[^s14]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto legislativo 7 marzo 2005, n. 82 (Codice…, 2005. Decreto legislativo 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale), art. 62. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62> ([archived](https://web.archive.org/web/20260125120137/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62))
[^s15]: Ministero dell'Interno — Missione – ANPR. Missione – ANPR. <https://www.anagrafenazionale.interno.it/anpr/missione/> ([archived](https://web.archive.org/web/20260906012128/https://www.anagrafenazionale.interno.it/anpr/missione/))
[^s16]: Gazzetta Ufficiale della Repubblica Italiana, Serie generale n. 302 (Ministero dell'interno) — Decreto 23 dicembre 2015 - Modalita' tecniche di…, 2015-12-30. Decreto 23 dicembre 2015 - Modalita' tecniche di emissione della Carta d'identita' elettronica (Allegato, 4.4.1.2 Dati biometrici secondari: le impronte digitali). <https://www.gazzettaufficiale.it/do/atto/serie_generale/caricaPdf?cdimg=15A0980900100010110001&dgu=2015-12-30&art.dataPubblicazioneGazzetta=2015-12-30&art.codiceRedazionale=15A09809&art.num=1&art.tiposerie=SG> ([archived](https://web.archive.org/web/20260917070715/https://www.gazzettaufficiale.it/do/atto/serie_generale/caricaPdf?cdimg=15A0980900100010110001&dgu=2015-12-30&art.dataPubblicazioneGazzetta=2015-12-30&art.codiceRedazionale=15A09809&art.num=1&art.tiposerie=SG))
[^s17]: Gazzetta Ufficiale della Repubblica Italiana - Istituto Poligrafico e Zecca dello Stato — Decreto del Ministero dell'Interno 23 dicembre 2015 -…, 2015-12-30. Decreto del Ministero dell'Interno 23 dicembre 2015 - Modalità tecniche di emissione della Carta d'identità elettronica (GU Serie Generale n. 302 del 30-12-2015). <https://www.gazzettaufficiale.it/eli/gu/2015/12/30/302/sg/pdf>
[^s18]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 82/2005 (CAD), art. 64, 2022-06-30. D.Lgs. 82/2005 (CAD), art. 64. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art64> ([archived](https://web.archive.org/web/20251111011946/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art64))
[^s19]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DL 78/2010, art. 19 (Aggiornamento del catasto), 2011-02-27. DL 78/2010, art. 19 (Aggiornamento del catasto). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art19> ([archived](https://web.archive.org/web/20251116145932/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art19))
[^s20]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DPR 313/2002 (Testo unico casellario giudiziale), art. 2, 2024-05-01. DPR 313/2002 (Testo unico casellario giudiziale), art. 2. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2002-11-14;313~art2>
[^s21]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — Legge 121/1981, art. 8 (Istituzione del Centro…, 2005-06-01. Legge 121/1981, art. 8 (Istituzione del Centro elaborazione dati). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1981-04-01;121~art8> ([archived](https://web.archive.org/web/20250709093424/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1981-04-01;121~art8))
[^s22]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto-legge 31 gennaio 2005, n. 7, art. 7-vicies ter, 2005. Decreto-legge 31 gennaio 2005, n. 7, art. 7-vicies ter. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2005-01-31;7~art7viciester>
[^s23]: Agenzia per l'Italia Digitale (AgID) — Servizi fiduciari qualificati / Firma elettronica…, 2024-04-23. Servizi fiduciari qualificati / Firma elettronica qualificata. <https://www.agid.gov.it/it/piattaforme/firma-elettronica-qualificata> ([archived](https://web.archive.org/web/20260924003149/https://www.agid.gov.it/it/piattaforme/firma-elettronica-qualificata))
[^s24]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DPR 605/1973, art. 1, 1976-12-04. DPR 605/1973, art. 1. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;605~art1!vig=2026-09-30>
[^s25]: Agenzia delle Dogane e dei Monopoli — Libro Blu 2024 - Relazione, 2025. Libro Blu 2024 - Relazione. <https://www.adm.gov.it/portale/documents/20182/261920520/Libro+blu+2024+-+Relazione.pdf/e46989ce-b39f-a404-3b4b-2af3196cba43?t=1784560697678>
[^s26]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DPR 1388/1971 – Istituzione del casellario centrale dei…, 1998-01-01. DPR 1388/1971 – Istituzione del casellario centrale dei pensionati. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1971-12-31;1388~art1>
[^s27]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto legislativo 7 marzo 2005, n. 82 (Codice…, 2005. Decreto legislativo 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale), art. 62-ter. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62ter> ([archived](https://web.archive.org/web/20251012072920/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62ter))
[^s28]: MEF - Ragioneria Generale dello Stato — Sistema Tessera Sanitaria - Home. Sistema Tessera Sanitaria - Home. <https://www.sistemats.it/> ([archived](https://web.archive.org/web/20160502181750/http://www.sistemats.it:80/))
[^s29]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — Legge 580/1993, art. 8 (Registro delle imprese), 2016-12-10. Legge 580/1993, art. 8 (Registro delle imprese). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1993-12-29;580~art8>
[^s30]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 231/2007, art. 21, 2026-07-23. D.Lgs. 231/2007, art. 21. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art21> ([archived](https://web.archive.org/web/20260106152255/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art21))
[^s31]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 285/1992 (Codice della strada), art. 226, 2018-07-01. D.Lgs. 285/1992 (Codice della strada), art. 226. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1992-04-30;285~art226> ([archived](https://web.archive.org/web/20251011185708/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1992-04-30;285~art226))
[^s32]: Agenzia per l'Italia Digitale (AgID) — SIOPE. SIOPE. <https://www.agid.gov.it/it/piattaforme/siope> ([archived](https://web.archive.org/web/20260923012741/https://www.agid.gov.it/it/piattaforme/siope))
[^s33]: MEF – Ragioneria Generale dello Stato — SIOPE+. SIOPE+. <https://www.rgs.mef.gov.it/VERSIONE-I/e_government/amministrazioni_pubbliche/siope/siope_/> ([archived](https://web.archive.org/web/20260921013404/https://www.rgs.mef.gov.it/VERSIONE-I/e_government/amministrazioni_pubbliche/siope/siope_/))
[^s34]: Ministero dell'Economia e delle Finanze — Chi siamo – NoiPA. Chi siamo – NoiPA. <https://noipa.mef.gov.it/cl/chi-siamo> ([archived](https://web.archive.org/web/20250413225956/https://noipa.mef.gov.it/cl/chi-siamo))
[^s35]: Ministero dell'Interno - Dipartimento per gli Affari Interni e Territoriali — Le elezioni. Le elezioni. <https://dait.interno.gov.it/elezioni> ([archived](https://web.archive.org/web/20260929012749/https://dait.interno.gov.it/elezioni))
[^s36]: Ministero dell'Interno – DAIT — Archivio Storico delle Elezioni. Archivio Storico delle Elezioni. <https://elezionistorico.interno.gov.it/> ([archived](https://web.archive.org/web/20260924110557/https://elezionistorico.interno.gov.it/))
[^s37]: Banca d'Italia — Gestione dei sistemi di pagamento. Gestione dei sistemi di pagamento. <https://www.bancaditalia.it/compiti/sistema-pagamenti/index.html>
[^s38]: Presidenza del Consiglio dei Ministri – Dipartimento della Protezione Civile — IT-alert – Cos'è. IT-alert – Cos'è. <https://www.it-alert.it/it/cose/> ([archived](https://web.archive.org/web/20260629070727/https://www.it-alert.it/it/cose/))
[^s39]: Presidenza del Consiglio dei Ministri - Dipartimento della Protezione Civile — Come funziona | IT-alert. Come funziona | IT-alert. <https://www.it-alert.it/it/come-funziona/>
[^s40]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 82/2005 (CAD), art. 62-quater, 2021-07-31. D.Lgs. 82/2005 (CAD), art. 62-quater. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62quater> ([archived](https://web.archive.org/web/20250713135628/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62quater))
[^s41]: Ministero della Salute / Dipartimento per la trasformazione digitale — Fascicolo Sanitario Elettronico, 2026. Fascicolo Sanitario Elettronico. <https://www.fascicolosanitario.gov.it/>
[^s42]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto-legge 18 ottobre 2012, n. 179, art. 12, 2012. Decreto-legge 18 ottobre 2012, n. 179, art. 12. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art12> ([archived](https://web.archive.org/web/20250819092310/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art12))
[^s43]: Istituto Poligrafico e Zecca dello Stato — Gazzetta Ufficiale - Home. Gazzetta Ufficiale - Home. <https://www.gazzettaufficiale.it/> ([archived](https://web.archive.org/web/20260913204754/https://www.gazzettaufficiale.it/))
[^s44]: Archivio Centrale dello Stato — Polo di conservazione digitale. Polo di conservazione digitale. <https://acs.cultura.gov.it/piano-nazionale-di-ripresa-e-resilienza-del-ministero-della-cultura/polo-di-conservazione-digitale/>
[^s45]: Istituto nazionale di statistica (ISTAT) — L'Istituto: organizzazione e attività. L'Istituto: organizzazione e attività. <https://www.istat.it/listituto/> ([archived](https://web.archive.org/web/20260927005502/https://www.istat.it/listituto/))
[^s46]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 322/1989, art. 15 (Compiti dell'ISTAT), 1989-10-07. D.Lgs. 322/1989, art. 15 (Compiti dell'ISTAT). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1989-09-06;322~art15> ([archived](https://web.archive.org/web/20250906141609/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1989-09-06;322~art15))

**Evidence grades:** 1 Strong, 60 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
