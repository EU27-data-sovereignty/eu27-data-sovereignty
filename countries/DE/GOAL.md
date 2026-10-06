# Germany: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Germany could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s6][^s7][^s8] |
| Government data centres | Yes[^s9][^s10][^s11] |
| Government cloud in operation | Yes[^s12][^s13][^s11] |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Germany described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 83.467 million[^s14] |
| GDP, current prices | 4 529.7 EUR bn[^s15] |
| Public administration employment (NACE O) | 2 915.0 thousand[^s16] |
| Non-household electricity price | 226.4 EUR/MWh[^s17] |
| Renewables share of electricity | 57.9 %[^s18] |
| Land area | 353 260 km²[^s19] |

## 3. Critical data holdings, by priority

The holdings Germany cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Melderegister (population/residence registers) kept by the Meldebehörden[^s20] | The Federal Central Tax Office (BZSt) stores the national personal identification number (Identifikationsnummer) with core identity data for every natural person (Abgabenordnung § 139b(3))[^s21][^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | Biometric features may be stored only at the issuing ID-card authorities[^s23] | No nationwide central database of biometric features is to be established; storage is decentral[^s23] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s23] | — | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet sourced* | Each Standesamt keeps the birth register (Geburtenregister) and other civil status registers[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The ID-card register records serial number, revocation password/sum and expiry date[^s25] | A central store of all ID-card serial numbers is permitted only at the card manufacturer, solely to trace the cards[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Wählerverzeichnis (electoral roll)[^s26] | Gemeindebehörden (municipal authorities)[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | Bundeszentralregister (Federal Central Criminal Register)[^s27] | Bundesamt für Justiz (Federal Office of Justice)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | polizeilicher Informationsverbund zwischen Bund und Ländern (federal-state police information network)[^s28] | Bundeskriminalamt (Federal Criminal Police Office)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | BundID is to become the single central citizen account 'DeutschlandID' under the OZG[^s29][^s30] | *Not yet sourced* | *Disputed: the fact check (claude-fable-5-1, run wf_e9645602-884) did not confirm this: The page says 'Der Betrieb der BundID erfolgt im Rechenzentrum des ITZBund', which supports the core clause, but the expansion 'Informationstechnikzentrum Bund' and the description 'the federal IT service provider' appear nowhere on the…. It is withheld until the fact or its source is corrected and checked again* | National infrastructure[^s30] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | V-PKI provides certificate-based security services to federal and state authorities, municipalities and public institutions[^s4] | *Not yet sourced* | The root CA (trust anchor) of the public-administration PKI has been operated at the BSI since 20 February 2001[^s4] | National infrastructure[^s4] | *Not yet measured* |
| High | Residence and migration status (tier 1) | The AZR consists of a general data stock and a separately kept visa file[^s31] | The AZR is kept by BAMF; the Federal Office of Administration (BVA) processes the data on BAMF's behalf[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | ELSTER (ELektronische STeuerERklärung; electronic tax return)[^s32] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | ATLAS is the customs IT procedure for automated clearance and monitoring of cross-border goods traffic[^s33] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Versichertenverzeichnis (register of insured persons)[^s34] | die Krankenkasse (each statutory health insurance fund)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Handelsregister (commercial register)[^s35] | die Gerichte (the courts)[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Transparenzregister (transparency register)[^s36] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Zentrales Fahrzeugregister des Kraftfahrt-Bundesamtes (Central Vehicle Register)[^s37][^s38] | Kraftfahrt-Bundesamt (Federal Motor Transport Authority)[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet sourced* | The BKA is the central national authority operating the national part of the Schengen Information System[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Nationales Waffenregister (National Firearms Register)[^s40] | Bundesverwaltungsamt (Federal Office of Administration)[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | automatisierte Verfahren für das Haushalts-, Kassen- und Rechnungswesen des Bundes (automated federal budget, cash and accounting procedure, HKR)[^s42] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | TARGET (Eurosystem real-time gross settlement payment system)[^s43] | Deutsche Bundesbank[^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Digitalfunk BOS (nationwide digital radio for public-safety authorities)[^s45] | Bundesanstalt für den Digitalfunk der BOS (BDBOS)[^s45] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | MoWaS is a highly available, hardened system for warning the population in Germany[^s46] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Bundesgesetzblatt (Federal Law Gazette)[^s47] | Bundesamt für Justiz (Federal Office of Justice)[^s48] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | The Bundesarchiv provides the Digital Intermediate Archive of the Federation (DZAB) as a central service to all federal public bodies[^s49] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 26 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 24 |

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

> Not yet sized. Capacity for Germany will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Germany without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- Land & property registry (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

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

### The verdict on each fact about Germany

54 of 54 printed facts about Germany pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:DE:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| indicator:DE:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:DE:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| indicator:DE:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| indicator:DE:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:DE:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:DE:population_m | param:DE:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:DE:gdp_eur_bn | param:DE:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_074137f6-b8e |
| param:DE:gov_employment_k | param:DE:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_074137f6-b8e |
| param:DE:elec_price_eur_mwh | param:DE:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_074137f6-b8e |
| param:DE:renewables_pct | param:DE:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_074137f6-b8e |
| param:DE:land_km2 | param:DE:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:civil_registry:operator | Civil registry core: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:DE:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:facial_biometric:hosting | Facial biometric: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:DE:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:police_records:operator | Police information systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:digital_identity_credentials:foreign_dependency | Digital identity credentials: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:trust_services_pki:hosting | State PKI and qualified trust services: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:DE:trust_services_pki:foreign_dependency | State PKI and qualified trust services: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:central_bank:operator | Central bank systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |
| record:DE:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DE:national_archives:register | National archives (digital): the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_074137f6-b8e |

### Withheld after the fact check: Germany

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:DE:digital_identity_credentials:hosting | Digital identity credentials: hosting | claude-fable-5-1 | not supported | The page says 'Der Betrieb der BundID erfolgt im Rechenzentrum des ITZBund', which supports the core clause, but the expansion 'Informationstechnikzentrum Bund' and the description 'the federal IT service provider' appear nowhere on the page; the page itself expands ITZBund as 'IT-Dienstleistungszentrum Berlin'. Only the added gloss fails. |

---

[^s1]: Bundesamt für Sicherheit in der Informationstechnik (BSI) — Mindeststandard des BSI zur Nutzung externer…, 2022-12. Mindeststandard des BSI zur Nutzung externer Cloud-Dienste, Version 2.1 (NCD.2.2.03 Gerichtsbarkeit). <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_Nutzung_externer_Cloud-Dienste_Version_2_1.pdf?__blob=publicationFile&v=4> ([archived](https://web.archive.org/web/20260701150216/https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_Nutzung_externer_Cloud-Dienste_Version_2_1.pdf?__blob=publicationFile&v=4))
[^s2]: Bundesministerium des Innern und für Heimat — Allgemeine Verwaltungsvorschrift zum materiellen…, 2023-03-13. Allgemeine Verwaltungsvorschrift zum materiellen Geheimschutz (Verschlusssachenanweisung - VSA), § 34. <https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_13032023_SII554001405.htm> ([archived](https://web.archive.org/web/20260928140800/https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_13032023_SII554001405.htm))
[^s3]: Bundesministerium der Justiz (gesetze-im-internet.de) — Sicherheitsüberprüfungsgesetz (SÜG) § 4 Allgemeine…. Sicherheitsüberprüfungsgesetz (SÜG) § 4 Allgemeine Grundsätze zum Schutz von Verschlusssachen. <https://www.gesetze-im-internet.de/s_g/__4.html> ([archived](https://web.archive.org/web/20250821134415/https://www.gesetze-im-internet.de/s_g/__4.html))
[^s4]: Bundesamt für Sicherheit in der Informationstechnik — Verwaltungs-PKI. Verwaltungs-PKI. <https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Moderner-Staat/Verwaltungs-PKI/verwaltungs-pki_node.html> ([archived](https://web.archive.org/web/20260213021318/https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Moderner-Staat/Verwaltungs-PKI/verwaltungs-pki_node.html))
[^s5]: D-Trust GmbH — Über uns - D-Trust. Über uns - D-Trust. <https://www.d-trust.net/de/ueber-uns> ([archived](https://web.archive.org/web/20260902212705/https://www.d-trust.net/de/ueber-uns))
[^s6]: Bundesdruckerei Gruppe GmbH — Konzern - Bundesdruckerei-Gruppe. Konzern - Bundesdruckerei-Gruppe. <https://www.bundesdruckerei.de/de/konzern> ([archived](https://web.archive.org/web/20260727120331/https://www.bundesdruckerei.de/de/konzern))
[^s7]: Bundesverwaltungsamt — Personalausweis mit Online-Ausweisfunktion. Personalausweis mit Online-Ausweisfunktion. <https://www.bva.bund.de/DE/Das-BVA/Aufgaben/P/Personalausweis/PA_Allgemein/PA_Allgemein_node.html> ([archived](https://web.archive.org/web/20240530193953/https://www.bva.bund.de/DE/Das-BVA/Aufgaben/P/Personalausweis/PA_Allgemein/PA_Allgemein_node.html))
[^s8]: Bundesministerium der Justiz (gesetze-im-internet.de) — Personalausweisgesetz (PAuswG) § 4 Eigentum am Ausweis;…. Personalausweisgesetz (PAuswG) § 4 Eigentum am Ausweis; Ausweishersteller; Vergabestelle für Berechtigungszertifikate. <https://www.gesetze-im-internet.de/pauswg/__4.html> ([archived](https://web.archive.org/web/20260309012726/https://www.gesetze-im-internet.de/pauswg/__4.html))
[^s9]: Informationstechnikzentrum Bund (ITZBund) — Informationstechnikzentrum Bund (ITZBund) - Über uns. Informationstechnikzentrum Bund (ITZBund) - Über uns. <https://www.itzbund.de/DE/dasitzbund/ueber-uns/ueber-uns.html> ([archived](https://web.archive.org/web/20260302061921/https://www.itzbund.de/DE/dasitzbund/ueber-uns/ueber-uns.html))
[^s10]: Informationstechnikzentrum Bund (ITZBund) — Hosting und Betrieb - Die Rechenzentren des ITZBund. Hosting und Betrieb - Die Rechenzentren des ITZBund. <https://www.itzbund.de/DE/leistungsportfolio/hostingundbetrieb/hostingundbetrieb.html> ([archived](https://web.archive.org/web/20260223163818/https://www.itzbund.de/DE/leistungsportfolio/hostingundbetrieb/hostingundbetrieb.html))
[^s11]: Informationstechnikzentrum Bund (ITZBund) — ITZBund - Facts & Figures 2024, 2025. ITZBund - Facts & Figures 2024. <https://www.itzbund.de/Webs/GB2024/DE/home/home_node.html?__site=GB2024> ([archived](https://web.archive.org/web/20251029102820/https://www.itzbund.de/Webs/GB2024/DE/home/home_node.html?__site=GB2024))
[^s12]: IT-Planungsrat — Digitalisierung der Verwaltung: Deutsche…, 2025-03-27. Digitalisierung der Verwaltung: Deutsche Verwaltungscloud startet in den Produktivbetrieb. <https://www.it-planungsrat.de/aktuelles/details/digitalisierung-der-verwaltung-deutsche-verwaltungscloud-startet-in-den-produktivbetrieb>
[^s13]: Informationstechnikzentrum Bund (ITZBund) — Die Bundescloud – eine exklusive, private Cloud für die…. Die Bundescloud – eine exklusive, private Cloud für die Bundesverwaltung. <https://www.itzbund.de/DE/itloesungen/egovernment/bundescloud/bundescloud.html> ([archived](https://web.archive.org/web/20260708195922/https://www.itzbund.de/DE/itloesungen/egovernment/bundescloud/bundescloud.html))
[^s14]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s15]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s16]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s17]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s18]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s19]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s20]: Bundesministerium der Justiz / gesetze-im-internet.de — § 2 BMG - Aufgaben und Befugnisse der Meldebehörden. § 2 BMG - Aufgaben und Befugnisse der Meldebehörden. <https://www.gesetze-im-internet.de/bmg/__2.html> ([archived](https://web.archive.org/web/20260102165107/https://www.gesetze-im-internet.de/bmg/__2.html))
[^s21]: Bundeszentralamt für Steuern — Die Identifikationsnummer. Die Identifikationsnummer. <https://www.bzst.de/DE/Privatpersonen/SteuerlicheIdentifikationsnummer/steuerlicheidentifikationsnummer_node.html> ([archived](https://web.archive.org/web/20260909163733/https://www.bzst.de/DE/Privatpersonen/SteuerlicheIdentifikationsnummer/steuerlicheidentifikationsnummer_node.html))
[^s22]: Bundesministerium der Justiz / gesetze-im-internet.de — § 139b AO - Identifikationsnummer. § 139b AO - Identifikationsnummer. <https://www.gesetze-im-internet.de/ao_1977/__139b.html> ([archived](https://web.archive.org/web/20260227090600/https://www.gesetze-im-internet.de/ao_1977/__139b.html))
[^s23]: Bundesministerium der Justiz / gesetze-im-internet.de — § 26 PAuswG - Sonstige Speicherung personenbezogener Daten. § 26 PAuswG - Sonstige Speicherung personenbezogener Daten. <https://www.gesetze-im-internet.de/pauswg/__26.html> ([archived](https://web.archive.org/web/20251117090709/https://www.gesetze-im-internet.de/pauswg/__26.html))
[^s24]: Bundesministerium der Justiz / gesetze-im-internet.de — § 3 PStG - Personenstandsregister. § 3 PStG - Personenstandsregister. <https://www.gesetze-im-internet.de/pstg/__3.html>
[^s25]: Bundesministerium der Justiz / gesetze-im-internet.de — § 23 PAuswG - Personalausweisregister. § 23 PAuswG - Personalausweisregister. <https://www.gesetze-im-internet.de/pauswg/__23.html> ([archived](https://web.archive.org/web/20251009222823/https://www.gesetze-im-internet.de/pauswg/__23.html))
[^s26]: Bundesamt für Justiz (gesetze-im-internet.de) — Bundeswahlgesetz § 17. Bundeswahlgesetz § 17. <https://www.gesetze-im-internet.de/bwahlg/__17.html> ([archived](https://web.archive.org/web/20260113161029/https://www.gesetze-im-internet.de/bwahlg/__17.html))
[^s27]: Bundesamt für Justiz (gesetze-im-internet.de) — Bundeszentralregistergesetz § 1. Bundeszentralregistergesetz § 1. <https://www.gesetze-im-internet.de/bzrg/__1.html> ([archived](https://web.archive.org/web/20251225083011/https://www.gesetze-im-internet.de/bzrg/__1.html))
[^s28]: Bundesamt für Justiz (gesetze-im-internet.de) — Bundeskriminalamtgesetz § 29. Bundeskriminalamtgesetz § 29. <https://www.gesetze-im-internet.de/bkag_2018/__29.html> ([archived](https://web.archive.org/web/20260908002421/https://www.gesetze-im-internet.de/bkag_2018/__29.html))
[^s29]: Bundesministerium der Justiz / Bundesamt für Justiz (gesetze-im-internet.de) — Onlinezugangsgesetz (OZG) § 3. Onlinezugangsgesetz (OZG) § 3. <https://www.gesetze-im-internet.de/ozg/__3.html> ([archived](https://web.archive.org/web/20260213222849/https://www.gesetze-im-internet.de/ozg/__3.html))
[^s30]: Land Brandenburg, OZG-Portal — BundID (Nutzerkonto) - DeutschlandID. BundID (Nutzerkonto) - DeutschlandID. <https://ozg.brandenburg.de/ozg/de/it-infrastrukturen/it-basiskomponenten/bundid-nutzerkonto-deutschlandid/>
[^s31]: Bundesministerium der Justiz / gesetze-im-internet.de — § 1 AZR-Gesetz. § 1 AZR-Gesetz. <https://www.gesetze-im-internet.de/azrg/__1.html> ([archived](https://web.archive.org/web/20250215034909/https://www.gesetze-im-internet.de/azrg/__1.html))
[^s32]: Bayerisches Landesamt für Steuern — ELSTER - Bayerisches Landesamt für Steuern. ELSTER - Bayerisches Landesamt für Steuern. <https://www.lfst.bayern.de/elster> ([archived](https://web.archive.org/web/20260725175431/https://www.lfst.bayern.de/elster))
[^s33]: Generalzolldirektion (Zoll online) — ATLAS. ATLAS. <https://www.zoll.de/DE/Fachthemen/Zoelle/ATLAS/atlas_node.html> ([archived](https://web.archive.org/web/20260618015312/https://www.zoll.de/DE/Fachthemen/Zoelle/ATLAS/atlas_node.html))
[^s34]: Bundesamt für Justiz (gesetze-im-internet.de) — SGB V § 288 Versichertenverzeichnis. SGB V § 288 Versichertenverzeichnis. <https://www.gesetze-im-internet.de/sgb_5/__288.html> ([archived](https://web.archive.org/web/20260329171945/https://www.gesetze-im-internet.de/sgb_5/__288.html))
[^s35]: Bundesamt für Justiz (gesetze-im-internet.de) — Handelsgesetzbuch § 8. Handelsgesetzbuch § 8. <https://www.gesetze-im-internet.de/hgb/__8.html> ([archived](https://web.archive.org/web/20260128064431/https://www.gesetze-im-internet.de/hgb/__8.html))
[^s36]: Bundesamt für Justiz (gesetze-im-internet.de) — Geldwäschegesetz § 18. Geldwäschegesetz § 18. <https://www.gesetze-im-internet.de/gwg_2017/__18.html> ([archived](https://web.archive.org/web/20241226225736/https://www.gesetze-im-internet.de/gwg_2017/__18.html))
[^s37]: Bundesamt für Justiz (gesetze-im-internet.de) — Straßenverkehrsgesetz § 48. Straßenverkehrsgesetz § 48. <https://www.gesetze-im-internet.de/stvg/__48.html> ([archived](https://web.archive.org/web/20250219144555/https://www.gesetze-im-internet.de/stvg/__48.html))
[^s38]: Bundesamt für Justiz (gesetze-im-internet.de) — Straßenverkehrsgesetz § 31. Straßenverkehrsgesetz § 31. <https://www.gesetze-im-internet.de/stvg/__31.html> ([archived](https://web.archive.org/web/20251117061329/https://www.gesetze-im-internet.de/stvg/__31.html))
[^s39]: Bundesministerium der Justiz / gesetze-im-internet.de — § 3 BKAG. § 3 BKAG. <https://www.gesetze-im-internet.de/bkag_2018/__3.html> ([archived](https://web.archive.org/web/20260227115654/https://www.gesetze-im-internet.de/bkag_2018/__3.html))
[^s40]: Bundesamt für Justiz (gesetze-im-internet.de) — Waffenregistergesetz § 1. Waffenregistergesetz § 1. <https://www.gesetze-im-internet.de/waffrg/__1.html> ([archived](https://web.archive.org/web/20240806132426/https://www.gesetze-im-internet.de/waffrg/__1.html))
[^s41]: Bundesamt für Justiz (gesetze-im-internet.de) — Waffenregistergesetz § 3 Registerbehörde. Waffenregistergesetz § 3 Registerbehörde. <https://www.gesetze-im-internet.de/waffrg/__3.html> ([archived](https://web.archive.org/web/20240806134530/https://www.gesetze-im-internet.de/waffrg/__3.html))
[^s42]: Zentrum für Finanzen des Bundes (ZFB) / Bundeskasse (zrb.bund.de) — HKR-Verfahren. HKR-Verfahren. <https://zrb.bund.de/vorschriften/hkr-verfahren>
[^s43]: Deutsche Bundesbank — TARGET - Der Entwicklungsprozess. TARGET - Der Entwicklungsprozess. <https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/target/target-603342> ([archived](https://web.archive.org/web/20260724075900/https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/target/target-603342))
[^s44]: Bundesamt für Justiz (gesetze-im-internet.de) — Gesetz über die Deutsche Bundesbank § 3. Gesetz über die Deutsche Bundesbank § 3. <https://www.gesetze-im-internet.de/bbankg/__3.html> ([archived](https://web.archive.org/web/20241206140449/https://www.gesetze-im-internet.de/bbankg/__3.html))
[^s45]: Bundesamt für Justiz (gesetze-im-internet.de) — BDBOS-Gesetz § 1. BDBOS-Gesetz § 1. <https://www.gesetze-im-internet.de/bdbosg/__1.html> ([archived](https://web.archive.org/web/20211207215735/https://www.gesetze-im-internet.de/bdbosg/__1.html))
[^s46]: Bundesamt für Bevölkerungsschutz und Katastrophenhilfe — MoWaS. MoWaS. <https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/MoWaS/mowas_node.html> ([archived](https://web.archive.org/web/20260924105236/https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/MoWaS/mowas_node.html))
[^s47]: Bundesamt für Justiz (gesetze-im-internet.de) — Verkündungs- und Bekanntmachungsgesetz § 1. Verkündungs- und Bekanntmachungsgesetz § 1. <https://www.gesetze-im-internet.de/vkbkmg/__1.html>
[^s48]: Bundesamt für Justiz (gesetze-im-internet.de) — Verkündungs- und Bekanntmachungsgesetz § 2. Verkündungs- und Bekanntmachungsgesetz § 2. <https://www.gesetze-im-internet.de/vkbkmg/__2.html> ([archived](https://web.archive.org/web/20260113175356/https://www.gesetze-im-internet.de/vkbkmg/__2.html))
[^s49]: Bundesarchiv — Nutzung des Digitalen Zwischenarchivs (DZAB). Nutzung des Digitalen Zwischenarchivs (DZAB). <https://www.bundesarchiv.de/unterlagen-abgeben/behoerdenberatung-zu-schriftgut-und-informationsverwaltung/nutzung-des-digitalen-zwischenarchivs-dzab/> ([archived](https://web.archive.org/web/20260618022322/https://www.bundesarchiv.de/unterlagen-abgeben/behoerdenberatung-zu-schriftgut-und-informationsverwaltung/nutzung-des-digitalen-zwischenarchivs-dzab/))

**Evidence grades:** 1 Strong, 53 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
