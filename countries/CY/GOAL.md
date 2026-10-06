# Cyprus: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Cyprus could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | *Disputed: the cited source is gone (HTTP 404, rechecked 2026-09-30)* |
| State-controlled national eID | *Disputed: the cited source is gone (HTTP 404, rechecked 2026-09-30)* |
| Government data centres | *Disputed: the cited source is gone (HTTP 404, rechecked 2026-09-30)* |
| Government cloud in operation | *Disputed: the cited source is gone (HTTP 404, rechecked 2026-09-30)* |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 30 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Cyprus described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 0.997 million[^s2] |
| GDP, current prices | 36.5 EUR bn[^s3] |
| Public administration employment (NACE O) | 36.8 thousand[^s4] |
| Non-household electricity price | 242.9 EUR/MWh[^s5] |
| Renewables share of electricity | 27.5 %[^s6] |
| Land area | 9 213 km²[^s7] |

## 3. Critical data holdings, by priority

The holdings Cyprus cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 30 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Civil Registry System[^s8] | Civil Registry and Migration Department, with District Administration offices as registration authorities[^s9] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Critical | Fingerprint biometric (tier 0) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: Art. 63(5) (and 67(4) for passports) says fingerprints taken for an ID card may be used only to issue the card and are deleted within 48 hours, verbatim. That shows ID-document fingerprints are not retained under this law, but the source…. It is withheld until the fact or its source is corrected and checked again* | — | — | — | — |
| Critical | Breeder document scans (tier 0) | Civil register of births and deaths kept by the Registrar of each District[^s9] | Civil Registry and Migration Department and District Administrations (registration authorities for births and deaths)[^s9] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Civil Registry System (handles applications for the issuance of identity cards and passports)[^s8] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | CY Login[^s8] | The Director of the Civil Registry and Migration Department instructs the eID service provider to issue or renew the eID[^s9] | JCC Payment Systems outsources operation of the eID certification authority to ADACOM, a qualified trust service provider registered in Greece[^s10] | EU provider[^s10] | CY Login: 542,716 verified citizen profiles (September 2026)[^s11] |
| High | Electoral roll entry (tier 0) | computerised population register system (used for the preparation and conduct of elections)[^s8] | The competent District Officer enters voters on the electoral roll[^s9] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | iJustice (electronic registration system)[^s8] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Cyprus Police computerised information system, with per-officer access codes[^s12] | The National N.SIS Service is part of the Cyprus Police and reports to the Police IT Department[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | electronic system of the Asylum Service (CASS)[^s8] | Civil Registry and Migration Department (the 'Department' under the Aliens and Immigration Law)[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | TAXISnet System[^s8] | Tax Commissioner and officers of the Tax Department[^s15][^s8] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | THESEAS customs electronic system for import declarations and manifests[^s16] | Customs and Excise Department, acting through its Director[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | ERGANI system of Social Insurance Services[^s8] | Director of the Social Insurance Services, Ministry of Labour and Social Insurance[^s18][^s8] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | GeSY information system, which providers must use for referrals, prescriptions, claims and beneficiary lists[^s19][^s20] | The Health Insurance Organisation develops and operates the information system[^s19][^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Computerised Integrated Lands Information System (CILIS)[^s8] | Director of the Department of Lands and Surveys[^s21][^s8] | Central and backup systems of the Land Information System are maintained by officers of the government Department of Information Technology Services together with DLS officers[^s22] | National infrastructure[^s22] | *Not yet sourced* |
| High | Business registry (tier 1) | Register of companies kept by the Registrar[^s23][^s24] | Registrar of Companies is the Official Receiver and Registrar[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Central Register of Beneficial Owners of Companies and Other Legal Entities[^s25][^s26] | Registrar of Companies and Official Receiver, as the authority keeping the register[^s25][^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Registrar's Register of motor vehicles[^s27][^s8] | Road Transport Department[^s8] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | National N.SIS: the Cyprus Police is the competent authority for its installation, operation and maintenance[^s13] | Ministry of Foreign Affairs[^s8] | National N.SIS installed, operated and maintained by the Cyprus Police (national)[^s13] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Firearms file kept by the Police recording firearms and essential components[^s28] | Cyprus Police, keeping the data in a data filing system[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | FIMAS[^s29] | Treasury (of the Republic of Cyprus)[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | Civil Registry System (functionalities for preparing and conducting all elections)[^s8] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | T2-CY, the Cypriot component of the European T2 payment system[^s30] | The Central Bank may open accounts for credit institutions, public bodies and other market participants[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | General Civil Defence Plan drawn up by the Minister of Interior and approved by the Council of Ministers[^s32] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | Integrated School Management System (SMS)[^s8] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | Single Bank of Electronic Health Records, which keeps and manages citizens' electronic health records[^s33] | National eHealth Authority, a public-law legal person[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The electronic edition of the Official Gazette is the only authentic edition with legal effect[^s34][^s8] | Published permanently and free of charge on the Government Printing Office website[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Emergency calls and public-safety radio (tier 1) | Next Generation 112 system; development agreement between Civil Defence and CYTA, 20-month implementation[^s35] | *Not yet sourced* | *Disputed: the fact check (claude-fable-5-1, run wf_e9645602-884) did not confirm this: The article supports that the NG112 development agreement was signed between Civil Defence and CYTA, but it mentions CYTA only by name and nowhere describes it as 'the Cypriot telecommunications organisation'; that descriptor is added from…. It is withheld until the fact or its source is corrected and checked again* | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The article only reports that Civil Defence signed a development agreement with CYTA for a system to be built over 20 months; it says nothing about where the infrastructure runs, what kind of entity CYTA is, or any hosting arrangement, so…. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | State Archives, in which public records are deposited and kept[^s36] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | Confidential statistical data: data that permit direct or indirect identification of statistical units[^s37] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | Address data theme: location of properties by street name, house number and postcode[^s38] | Steering Group chaired by the Director of the Department of Lands and Surveys[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 29 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 1 |
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

> Not yet sized. Capacity for Cyprus will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Cyprus without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Facial biometric (tier 0)
- Authentication audit log (tier 0)
- State PKI and qualified trust services (tier 0)
- Government payroll and personnel (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
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

### The verdict on each fact about Cyprus

63 of 63 printed facts about Cyprus pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:CY:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:CY:population_m | param:CY:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:CY:gdp_eur_bn | param:CY:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:CY:gov_employment_k | param:CY:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:CY:elec_price_eur_mwh | param:CY:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:CY:renewables_pct | param:CY:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:CY:land_km2 | param:CY:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:digital_identity_credentials:hosting | Digital identity credentials: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:CY:digital_identity_credentials:foreign_dependency | Digital identity credentials: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:digital_identity_credentials:count | Digital identity credentials: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:police_records:operator | Police information systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:tax:operator | Tax: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:customs:operator | Customs declarations: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:land_property:hosting | Land & property registry: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:CY:land_property:foreign_dependency | Land & property registry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:border_control:hosting | Border and visa systems: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:CY:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:central_bank:operator | Central bank systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:health_records:operator | Health records: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:national_archives:register | National archives (digital): the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:CY:geospatial:operator | Geospatial base data: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Cyprus

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:CY:emergency_communications:foreign_dependency | Emergency calls and public-safety radio: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | not supported | The article only reports that Civil Defence signed a development agreement with CYTA for a system to be built over 20 months; it says nothing about where the infrastructure runs, what kind of entity CYTA is, or any hosting arrangement, so 'National infrastructure' needs outside knowledge the source does not supply. |
| record:CY:emergency_communications:hosting | Emergency calls and public-safety radio: hosting | claude-fable-5-1 | not supported | The article supports that the NG112 development agreement was signed between Civil Defence and CYTA, but it mentions CYTA only by name and nowhere describes it as 'the Cypriot telecommunications organisation'; that descriptor is added from outside the source. The core clause would pass if the gloss were dropped. |
| record:CY:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | claude-fable-5-1 | unclear | Art. 63(5) (and 67(4) for passports) says fingerprints taken for an ID card may be used only to issue the card and are deleted within 48 hours, verbatim. That shows ID-document fingerprints are not retained under this law, but the source does not state that no central fingerprint register exists at all, so the general negative 'No central register' goes beyond what the page says. |

---

[^s1]: Republic of Cyprus (consolidated text via CyLaw, Cyprus Bar Association) — Ο περί Κανόνων Ασφαλείας Διαβαθμισμένων Πληροφοριών,…, 2021. Ο περί Κανόνων Ασφαλείας Διαβαθμισμένων Πληροφοριών, Εγγράφων και Υλικού και για Συναφή Θέματα Νόμος του 2021 (Ν. 84(I)/2021). <https://www.cylaw.org/nomoi/enop/non-ind/2021_1_84/full.html> ([archived](https://web.archive.org/web/20260710074341/http://www.cylaw.org/nomoi/enop/non-ind/2021_1_84/full.html))
[^s2]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s3]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s4]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s5]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s6]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s7]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s8]: European Commission, Interoperable Europe (NIFO) — CYPRUS 2025 Digital Public Administration Factsheet -…, 2025-11. CYPRUS 2025 Digital Public Administration Factsheet - Supporting document. <https://interoperable-europe.ec.europa.eu/sites/default/files/custom-page/attachment/2026-06/iopeu-monitoring_2025-supporting-document_cyprus_final.pdf>
[^s9]: CyLaw (Cyprus Bar Association) — Ο Περί Αρχείου Πληθυσμού Νόμος του 2002 (141(I)/2002), 2002. Ο Περί Αρχείου Πληθυσμού Νόμος του 2002 (141(I)/2002). <https://www.cylaw.org/nomoi/enop/non-ind/2002_1_141/full.html> ([archived](https://web.archive.org/web/20260922145702/https://www.cylaw.org/nomoi/enop/non-ind/2002_1_141/full.html))
[^s10]: JCC Payment Systems Ltd — Δήλωση Πρακτικών Πιστοποίησης για την Κυπριακή…, 2025-11-03. Δήλωση Πρακτικών Πιστοποίησης για την Κυπριακή Ηλεκτρονική Ταυτότητα (eID), έκδοση 1.4. <https://pki.jcc.com.cy/repository/el/CPS/files/JCC-PL-QTSP-Certification_Practice_Statement_for_eID_GR-1.4_FINAL.pdf>
[^s11]: Politis — From The Counter To The Screen: CY Login Becomes…, 2026-09-13. From The Counter To The Screen: CY Login Becomes Cyprus's Key To Digital Government. <https://en.politis.com.cy/in-depth/1032645/from-the-counter-to-the-screen-cy-login-becomes-cypruss-key-to-digital-government>
[^s12]: Politis — Στο στόχαστρο αστυνομικοί για διαρροές - Ποινικές και…. Στο στόχαστρο αστυνομικοί για διαρροές - Ποινικές και πειθαρχικές ευθύνες σε εξέλιξη. <https://www.politis.com.cy/politis-news/cyprus/1031511/sto-stokhastro-astinomiki-ghia-diarroes-poinikes-kai-peitharkhikes-efthynes-se-ekseliksi> ([archived](https://web.archive.org/web/20260909045932/https://www.politis.com.cy/politis-news/cyprus/1031511/sto-stokhastro-astinomiki-ghia-diarroes-poinikes-kai-peitharkhikes-efthynes-se-ekseliksi))
[^s13]: CyLaw (Cyprus Bar Association) — Ο περί της Λειτουργίας και Χρήσης στη Δημοκρατία του…, 2023. Ο περί της Λειτουργίας και Χρήσης στη Δημοκρατία του Συστήματος Πληροφοριών Σένγκεν (SIS) Νόμος του 2023 (171(I)/2023). <https://www.cylaw.org/nomoi/enop/non-ind/2023_1_171/full.html> ([archived](https://web.archive.org/web/20260510162357/http://www.cylaw.org/nomoi/enop/non-ind/2023_1_171/full.html))
[^s14]: CyLaw (Cyprus Bar Association) — Ο περί Αλλοδαπών και Μεταναστεύσεως Νόμος (ΚΕΦ.105). Ο περί Αλλοδαπών και Μεταναστεύσεως Νόμος (ΚΕΦ.105). <https://www.cylaw.org/nomoi/enop/non-ind/0_105/full.html> ([archived](https://web.archive.org/web/20260723072018/http://www.cylaw.org/nomoi/enop/non-ind/0_105/full.html))
[^s15]: CyLaw (Cyprus Bar Association) — Ο περί Βεβαιώσεως και Εισπράξεως Φόρων Νόμος του 1978…, 1978. Ο περί Βεβαιώσεως και Εισπράξεως Φόρων Νόμος του 1978 (4/1978). <https://www.cylaw.org/nomoi/enop/non-ind/1978_1_4/full.html> ([archived](https://web.archive.org/web/20260407105946/https://www.cylaw.org/nomoi/enop/non-ind/1978_1_4/full.html))
[^s16]: Customs and Excise Department, Ministry of Finance — CUSTOMS & EXCISE - eCustoms Project. CUSTOMS & EXCISE - eCustoms Project. <https://www.mof.gov.cy/mof/customs/customs.nsf/ced12_en/ced12_en?OpenDocument=> ([archived](https://web.archive.org/web/20250609163803/https://www.mof.gov.cy/mof/customs/customs.nsf/ced12_en/ced12_en?OpenDocument=))
[^s17]: CyLaw (Cyprus Bar Association) — Ο Περί Τελωνειακού Κώδικα Νόμος του 2004 (94(I)/2004), 2004. Ο Περί Τελωνειακού Κώδικα Νόμος του 2004 (94(I)/2004). <https://www.cylaw.org/nomoi/enop/non-ind/2004_1_94/full.html> ([archived](https://web.archive.org/web/20260617232701/http://www.cylaw.org/nomoi/enop/non-ind/2004_1_94/full.html))
[^s18]: CyLaw (Cyprus Bar Association) — Ο περί Κοινωνικών Ασφαλίσεων Νόμος του 2010 (59(I)/2010), 2010. Ο περί Κοινωνικών Ασφαλίσεων Νόμος του 2010 (59(I)/2010). <https://www.cylaw.org/nomoi/enop/non-ind/2010_1_59/full.html> ([archived](https://web.archive.org/web/20250912191023/https://www.cylaw.org/nomoi/enop/non-ind/2010_1_59/full.html))
[^s19]: CyLaw (Cyprus Bar Association) — Ο Περί Γενικού Συστήματος Υγείας Νόμος του 2001 (89(I)/2001), 2001. Ο Περί Γενικού Συστήματος Υγείας Νόμος του 2001 (89(I)/2001). <https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html> ([archived](https://web.archive.org/web/20240917113142/https://www.cylaw.org/nomoi/enop/non-ind/2001_1_89/full.html))
[^s20]: Health Insurance Organisation (HIO) — GHS Information Technology System. GHS Information Technology System. <https://www.gesy.org.cy/en-us/hioinformationtechnologysys>
[^s21]: CyLaw (Cyprus Bar Association) — Ο περί Ακίνητης Ιδιοκτησίας (Διακατοχή, Εγγραφή και…. Ο περί Ακίνητης Ιδιοκτησίας (Διακατοχή, Εγγραφή και Εκτίμηση) Νόμος (ΚΕΦ.224). <https://www.cylaw.org/nomoi/enop/non-ind/0_224/full.html> ([archived](https://web.archive.org/web/20260122044453/https://www.cylaw.org/nomoi/enop/non-ind/0_224/full.html))
[^s22]: Department of Lands and Surveys — Ετήσια Έκθεση Τμήματος Κτηματολογίου και Χωρομετρίας 2022, 2023. Ετήσια Έκθεση Τμήματος Κτηματολογίου και Χωρομετρίας 2022. <https://portal.dls.moi.gov.cy/wp-content/uploads/2023/05/Annual-report-DLS-2022.pdf> ([archived](https://web.archive.org/web/20230630141403/https://portal.dls.moi.gov.cy/wp-content/uploads/2023/05/Annual-report-DLS-2022.pdf))
[^s23]: Department of Registrar of Companies and Intellectual Property — Modernisation of the Department. Modernisation of the Department. <https://www.companies.gov.cy/en/about/modernisation-of-the-department> ([archived](https://web.archive.org/web/20260609215558/https://www.companies.gov.cy/en/about/modernisation-of-the-department))
[^s24]: CyLaw (Cyprus Bar Association) — Ο περί Εταιρειών Νόμος (ΚΕΦ.113). Ο περί Εταιρειών Νόμος (ΚΕΦ.113). <https://www.cylaw.org/nomoi/enop/non-ind/0_113/full.html> ([archived](https://web.archive.org/web/20260908033223/https://www.cylaw.org/nomoi/enop/non-ind/0_113/full.html))
[^s25]: Department of Registrar of Companies and Intellectual Property — Registration of beneficial owner particulars. Registration of beneficial owner particulars. <https://www.companies.gov.cy/en/21-eservices/1-registration-of-beneficial-owner-particulars/2-registration-of-beneficial-owner-particulars> ([archived](https://web.archive.org/web/20260829094445/https://www.companies.gov.cy/en/21-eservices/1-registration-of-beneficial-owner-particulars/2-registration-of-beneficial-owner-particulars))
[^s26]: CyLaw (Cyprus Bar Association) — Ο περί της Παρεμπόδισης και Καταπολέμησης της…, 2007. Ο περί της Παρεμπόδισης και Καταπολέμησης της Νομιμοποίησης Εσόδων από Παράνομες Δραστηριότητες Νόμος του 2007 (188(I)/2007). <https://www.cylaw.org/nomoi/enop/non-ind/2007_1_188/full.html> ([archived](https://web.archive.org/web/20260721164149/https://www.cylaw.org/nomoi/enop/non-ind/2007_1_188/full.html))
[^s27]: CyLaw (Cyprus Bar Association) — Ο περί Μηχανοκινήτων Οχημάτων και Τροχαίας Κινήσεως…, 1972. Ο περί Μηχανοκινήτων Οχημάτων και Τροχαίας Κινήσεως Νόμος του 1972 (86/1972). <https://www.cylaw.org/nomoi/enop/non-ind/1972_1_86/full.html> ([archived](https://web.archive.org/web/20240419181847/https://www.cylaw.org/nomoi/enop/non-ind/1972_1_86/full.html))
[^s28]: CyLaw (Cyprus Bar Association) — Ο Περί Πυροβόλων και Μη Πυροβόλων Όπλων Νόμος του 2004…, 2004. Ο Περί Πυροβόλων και Μη Πυροβόλων Όπλων Νόμος του 2004 (113(I)/2004). <https://www.cylaw.org/nomoi/enop/non-ind/2004_1_113/full.html> ([archived](https://web.archive.org/web/20260418111012/http://www.cylaw.org/nomoi/enop/non-ind/2004_1_113/full.html))
[^s29]: Statistical Service of Cyprus (CYSTAT) — Inventory of the methods, procedures and sources used…, 2026-06. Inventory of the methods, procedures and sources used for the compilation of deficit and debt data (ESA 2010), Cyprus 2024. <https://library.cystat.gov.cy/NEW/EDP_Inventory(Sources&Methods)_ESA2010-EN-290626.pdf>
[^s30]: Central Bank of Cyprus — Central Bank of Cyprus Annual Report 2025, 2026. Central Bank of Cyprus Annual Report 2025. <https://www.centralbank.cy/images/media/redirectfile/CBC_Annual_Report_English_2025_Final%20(006).pdf>
[^s31]: CyLaw (Cyprus Bar Association) — Ο περί της Κεντρικής Τράπεζας της Κύπρου Νόμος του 2002…, 2002. Ο περί της Κεντρικής Τράπεζας της Κύπρου Νόμος του 2002 (138(I)/2002). <https://www.cylaw.org/nomoi/enop/non-ind/2002_1_138/full.html> ([archived](https://web.archive.org/web/20251116053446/http://www.cylaw.org/nomoi/enop/non-ind/2002_1_138/full.html))
[^s32]: CyLaw (Cyprus Bar Association) — Ο περί Πολιτικής Άμυνας Νόμος του 1996 (117(I)/1996), 1996. Ο περί Πολιτικής Άμυνας Νόμος του 1996 (117(I)/1996). <https://www.cylaw.org/nomoi/enop/non-ind/1996_1_117/full.html>
[^s33]: CyLaw (Cyprus Bar Association) — Ο περί Ηλεκτρονικής Υγείας Νόμος του 2019 (59(I)/2019), 2019. Ο περί Ηλεκτρονικής Υγείας Νόμος του 2019 (59(I)/2019). <https://www.cylaw.org/nomoi/enop/non-ind/2019_1_59/full.html>
[^s34]: CyLaw (Cyprus Bar Association) — Ο περί της Ηλεκτρονικής Έκδοσης της Επίσημης Εφημερίδας…, 2019. Ο περί της Ηλεκτρονικής Έκδοσης της Επίσημης Εφημερίδας της Δημοκρατίας Νόμος του 2019 (82(I)/2019). <https://www.cylaw.org/nomoi/enop/non-ind/2019_1_82/full.html>
[^s35]: RIK (Cyprus Broadcasting Corporation) — Πληρέστερη και ταχύτερη πληροφόρηση σε κρίσιμα…, 2026-07-14. Πληρέστερη και ταχύτερη πληροφόρηση σε κρίσιμα περιστατικά με το Σύστημα Νέας Γενιάς 112. <https://news.rik.cy/el/article/2026/7/14/plerestere-kai-takhutere-plerophorese-se-krisima-peristatika-me-to-sustema-neas-genias-112/> ([archived](https://web.archive.org/web/20260721094537/https://news.rik.cy/el/article/2026/7/14/plerestere-kai-takhutere-plerophorese-se-krisima-peristatika-me-to-sustema-neas-genias-112/))
[^s36]: CyLaw (Cyprus Bar Association) — Ο περί Κρατικού Αρχείου Νόμος του 1991 (208/1991), 1991. Ο περί Κρατικού Αρχείου Νόμος του 1991 (208/1991). <https://www.cylaw.org/nomoi/enop/non-ind/1991_1_208/full.html> ([archived](https://web.archive.org/web/20260315110743/http://www.cylaw.org/nomoi/enop/non-ind/1991_1_208/full.html))
[^s37]: CyLaw (Cyprus Bar Association) — Ο περί Επίσημων Στατιστικών Νόμος του 2021 (Ν. 25(Ι)/2021), 2021. Ο περί Επίσημων Στατιστικών Νόμος του 2021 (Ν. 25(Ι)/2021). <https://www.cylaw.org/nomoi/arith/2021_1_025.pdf> ([archived](https://web.archive.org/web/20250507125237/http://www.cylaw.org/nomoi/arith/2021_1_025.pdf))
[^s38]: CyLaw (Cyprus Bar Association) — Ο περί της Δημιουργίας Υποδομής Χωρικών Δεδομένων…, 2010. Ο περί της Δημιουργίας Υποδομής Χωρικών Δεδομένων (INSPIRE) Νόμος του 2010 (43(I)/2010). <https://www.cylaw.org/nomoi/enop/non-ind/2010_1_43/full.html> ([archived](https://web.archive.org/web/20240527211128/https://www.cylaw.org/nomoi/enop/non-ind/2010_1_43/full.html))

**Evidence grades:** 4 Strong, 59 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
