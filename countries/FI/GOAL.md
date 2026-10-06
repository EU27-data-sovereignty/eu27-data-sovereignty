# Finland: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Finland could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1] |
| Classification in law | Yes[^s2][^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s6][^s7] |
| Government data centres | Yes[^s8][^s9][^s10][^s1] |
| Government cloud in operation | Yes[^s11][^s12] |

What could move this placement:

- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Finland described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.653 million[^s13] |
| GDP, current prices | 281.8 EUR bn[^s14] |
| Public administration employment (NACE O) | 149.1 thousand[^s15] |
| Non-household electricity price | 74.8 EUR/MWh[^s16] |
| Renewables share of electricity | 56.6 %[^s17] |
| Land area | 303 109 km²[^s18] |

## 3. Critical data holdings, by priority

The holdings Finland cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 16 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Väestötietojärjestelmä (Population Information System) is the general national base register of persons, real estate, buildings and dwellings[^s19][^s20] | Digital and Population Data Services Agency (DVV) carries the controller duties for the Population Information System[^s21][^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | passirekisteri (passport register)[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | passirekisteri (passport register)[^s23][^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | The Population Information System includes regionally organised documentary records not taken into digital form[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | DVV must keep a log register of processing of data stored from use of the support services (incl. identification)[^s24] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | About 17 million authentications per month through Suomi.fi e-Identification[^s25] |
| High | Document issuance history (tier 0) | Henkilökortti- ja passijärjestelmä, Heko-Passi (ID card and passport system)[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | äänioikeusrekisteri (voting register)[^s26] | ORK (Oikeusrekisterikeskus, Legal Register Centre) maintains the election information system technically; the system is owned by oikeusministeriö (Ministry of Justice)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | DVV keeps a certificate register of the personal certificates it issues, under the eIDAS Regulation[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | Poliisiasiaintietojärjestelmä PATJA (Police Information System)[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | The aliens-affairs case management system holds data on non-visa immigration matters[^s28] | Each authority is controller for data it stores; the Finnish Immigration Service is controller for international-protection registration data[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Business registry (tier 1) | The registration authority keeps a public diary and document files in its information system[^s29] | The Trade Register Act names the Finnish Patent and Registration Office as registrar[^s29][^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Finnish Customs receives beneficial-owner data from the PRH Trade Register[^s31] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | The national visa information system stores short- and long-term visa processing data[^s28] | *Disputed: sources disagree. Oikeusministeriö / Finlex (Ministry of Justice) — Laki henkilötietojen käsittelystä Rajavartiolaitoksessa…, 2019 gives the value this report printed; Poliisihallitus — Tietosuojaseloste; Schengenin tietojärjestelmän…, 2023-05-11 gives “Poliisihallitus (National Police Board)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Asetietojärjestelmä (firearms information system)[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | The Government Shared Services Centre for Finance and HR holds data on central-government agencies' financial and HR administration[^s32] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Building data are recorded in the Population Information System[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 16 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 16 |

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

> Not yet sized. Capacity for Finland will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Finland without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Land & property registry (tier 1)
- Vehicle & licensing (tier 1)
- Judicial & criminal justice (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Crisis management and civil protection (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

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

### The verdict on each fact about Finland

33 of 33 printed facts about Finland pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:FI:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:FI:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:FI:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:FI:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:FI:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:FI:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:FI:population_m | param:FI:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:FI:gdp_eur_bn | param:FI:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:FI:gov_employment_k | param:FI:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:FI:elec_price_eur_mwh | param:FI:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:FI:renewables_pct | param:FI:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:FI:land_km2 | param:FI:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:authentication_audit_log:count | Authentication audit log: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:electoral_roll:operator | Electoral roll entry: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:FI:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:FI:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Finland

None.

---

[^s1]: Finlex / Oikeusministeriö — Laki turvallisuusverkkotoiminnasta (10/2015), 5 §. Laki turvallisuusverkkotoiminnasta (10/2015), 5 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2015/10/fin@>
[^s2]: Finlex / Oikeusministeriö — Valtioneuvoston asetus asiakirjojen…. Valtioneuvoston asetus asiakirjojen turvallisuusluokittelusta valtionhallinnossa (1101/2019), 3 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2019/1101/fin@>
[^s3]: Finlex / oikeusministeriö — Laki julkisen hallinnon tiedonhallinnasta 906/2019…. Laki julkisen hallinnon tiedonhallinnasta 906/2019 (ajantasainen). <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2019/906/fin@>
[^s4]: Digital and Population Data Services Agency (DVV) — CA Certificates. CA Certificates. <https://dvv.fi/en/ca-certificates> ([archived](https://web.archive.org/web/20260202204257/https://dvv.fi/en/ca-certificates))
[^s5]: Finlex / Oikeusministeriö — Laki väestötietojärjestelmästä ja…. Laki väestötietojärjestelmästä ja Väestörekisterikeskuksen varmennepalveluista (661/2009), 61 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute/2009/661/fin@>
[^s6]: Digi- ja väestötietovirasto (DVV) — Tunnistus (Suomi.fi-tunnistus). Tunnistus (Suomi.fi-tunnistus). <https://dvv.fi/suomi.fi-tunnistus>
[^s7]: Finlex / Oikeusministeriö — Laki hallinnon yhteisistä sähköisen asioinnin…. Laki hallinnon yhteisistä sähköisen asioinnin tukipalveluista (571/2016), 4 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2016/571/fin@>
[^s8]: Suomen Erillisverkot Oy — Suomalainen data turvaan Suomeen, 2019-04-23. Suomalainen data turvaan Suomeen. <https://www.erillisverkot.fi/suomalainen-data-turvaan-suomeen/> ([archived](https://web.archive.org/web/20260510201952/https://www.erillisverkot.fi/suomalainen-data-turvaan-suomeen/))
[^s9]: Suomen Erillisverkot Oy — Erillisverkkojen vuosikertomus 2025, 2026. Erillisverkkojen vuosikertomus 2025. <https://www.erillisverkot.fi/vuosikertomus-2025/> ([archived](https://web.archive.org/web/20260727163800/https://www.erillisverkot.fi/vuosikertomus-2025/))
[^s10]: Suomen Erillisverkot Oy — Konesalipalvelu. Konesalipalvelu. <https://www.erillisverkot.fi/palvelut/konesali-ja-suojatilat/> ([archived](https://web.archive.org/web/20260727163800/https://www.erillisverkot.fi/palvelut/konesali-ja-suojatilat/))
[^s11]: Suomen Erillisverkot Oy — Turvapilvipalvelu (Virtuaalinen konesalipalvelu). Turvapilvipalvelu (Virtuaalinen konesalipalvelu). <https://www.erillisverkot.fi/palvelut/virtuaalinen-konesali/> ([archived](https://web.archive.org/web/20260727163800/https://www.erillisverkot.fi/palvelut/virtuaalinen-konesali/))
[^s12]: Suomen Erillisverkot Oy — Turvapilvipalvelu – täysin kotimainen pilvipalvelu ja…, 2021-12-03. Turvapilvipalvelu – täysin kotimainen pilvipalvelu ja tiedon turvasatama. <https://www.erillisverkot.fi/turvapilvipalvelu-taysin-kotimainen-pilvipalvelu-ja-tiedon-turvasatama/> ([archived](https://web.archive.org/web/20260419203958/https://www.erillisverkot.fi/turvapilvipalvelu-taysin-kotimainen-pilvipalvelu-ja-tiedon-turvasatama/))
[^s13]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s14]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s15]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s16]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s17]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s18]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s19]: Digital and Population Data Services Agency (DVV) — Population Information System. Population Information System. <https://dvv.fi/en/population-information-system> ([archived](https://web.archive.org/web/20260512125439/https://dvv.fi/en/population-information-system))
[^s20]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki väestötietojärjestelmästä ja Digi- ja…, 2009. Laki väestötietojärjestelmästä ja Digi- ja väestötietoviraston varmennepalveluista (661/2009). <https://www.finlex.fi/fi/lainsaadanto/2009/661> ([archived](https://web.archive.org/web/20260522204328/https://www.finlex.fi/fi/lainsaadanto/2009/661))
[^s21]: Digi- ja väestötietovirasto — Väestötietojärjestelmän tietosuojaseloste. Väestötietojärjestelmän tietosuojaseloste. <https://dvv.fi/vtj-tietosuoja> ([archived](https://web.archive.org/web/20260831170900/https://dvv.fi/vtj-tietosuoja))
[^s22]: Poliisihallitus — Poliisin asiakirjajulkisuuskuvaus, 2021-06-30. Poliisin asiakirjajulkisuuskuvaus. <https://poliisi.fi/documents/25235045/26823782/Poliisin+asiakirjajulkisuuskuvaus.pdf/0bc008c3-7106-fa8b-89a1-fb01b8088e8d?t=1630301434861>
[^s23]: Poliisi — Sormenjäljet matkustusoikeudelliselle henkilökortille. Sormenjäljet matkustusoikeudelliselle henkilökortille. <https://poliisi.fi/neuvontapalvelu/-/asset_publisher/ZtAEeHB39Lxr/content/sormenjaljet-matkustusoikeudelliselle-henkilokortille>
[^s24]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki hallinnon yhteisistä sähköisen asioinnin…, 2016. Laki hallinnon yhteisistä sähköisen asioinnin tukipalveluista (571/2016). <https://www.finlex.fi/fi/lainsaadanto/2016/571> ([archived](https://web.archive.org/web/20260919081102/https://www.finlex.fi/fi/lainsaadanto/2016/571))
[^s25]: Digi- ja väestötietovirasto (DVV), via STT Info — Digi- ja väestötietovirasto valitsi vahvan tunnistamisen…, 2024-01-31. Digi- ja väestötietovirasto valitsi vahvan tunnistamisen välityspalveluntarjoajaksi Telia Finland Oyj:n. <https://www.sttinfo.fi/tiedote/70085553/digi-ja-vaestotietovirasto-valitsi-vahvan-tunnistamisen-valityspalveluntarjoajaksi-telia-finland-oyjn?publisherId=3777&lang=fi> ([archived](https://web.archive.org/web/20240202092418/https://www.sttinfo.fi/tiedote/70085553/digi-ja-vaestotietovirasto-valitsi-vahvan-tunnistamisen-valityspalveluntarjoajaksi-telia-finland-oyjn?publisherId=3777&lang=fi))
[^s26]: Digi- ja väestötietovirasto — Äänioikeusrekisterin tietosuojaseloste. Äänioikeusrekisterin tietosuojaseloste. <https://dvv.fi/aanioikeusrekisterin-tietosuoja> ([archived](https://web.archive.org/web/20260529172204/https://dvv.fi/aanioikeusrekisterin-tietosuoja))
[^s27]: Oikeusrekisterikeskus — Uusi vaalitietojärjestelmä testissä: käyttäjien…, 2026-01-19. Uusi vaalitietojärjestelmä testissä: käyttäjien näkemykset tärkeitä vaalitietojärjestelmän kehityksessä. <https://www.oikeusrekisterikeskus.fi/ajankohtaista/tiedote-ja-uutisarkisto/uusi-vaalitietojarjestelma-testissa-kayttajien-nakemykset-tarkeita-vaalitietojarjestelman-kehityksessa/> ([archived](https://web.archive.org/web/20260617125057/https://www.oikeusrekisterikeskus.fi/ajankohtaista/tiedote-ja-uutisarkisto/uusi-vaalitietojarjestelma-testissa-kayttajien-nakemykset-tarkeita-vaalitietojarjestelman-kehityksessa/))
[^s28]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki henkilötietojen käsittelystä…, 2020. Laki henkilötietojen käsittelystä maahanmuuttohallinnossa (615/2020). <https://www.finlex.fi/fi/lainsaadanto/2020/615> ([archived](https://web.archive.org/web/20260421162858/https://www.finlex.fi/fi/lainsaadanto/2020/615))
[^s29]: Oikeusministeriö / Finlex (Ministry of Justice) — Kaupparekisterilaki (564/2023), 2023. Kaupparekisterilaki (564/2023). <https://www.finlex.fi/fi/lainsaadanto/2023/564> ([archived](https://web.archive.org/web/20251010152906/https://www.finlex.fi/fi/lainsaadanto/2023/564))
[^s30]: Finlex / oikeusministeriö — Kaupparekisterilaki 564/2023 (ajantasainen). Kaupparekisterilaki 564/2023 (ajantasainen). <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2023/564/fin@>
[^s31]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki henkilötietojen käsittelystä Tullissa (650/2019), 2019. Laki henkilötietojen käsittelystä Tullissa (650/2019). <https://www.finlex.fi/fi/lainsaadanto/2019/650> ([archived](https://web.archive.org/web/20260205004618/https://www.finlex.fi/fi/lainsaadanto/2019/650))
[^s32]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki Valtiokonttorista (305/1991), 1991. Laki Valtiokonttorista (305/1991). <https://www.finlex.fi/fi/lainsaadanto/1991/305> ([archived](https://web.archive.org/web/20260411111736/https://www.finlex.fi/fi/lainsaadanto/1991/305))

**Evidence grades:** 2 Strong, 31 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
