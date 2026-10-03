# Ireland: critical data holdings and sovereign hosting

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

> Dependent on non-EU providers. Confidence: High. With the evidence still open, Ireland could be anywhere from 'Dependent on non-EU providers' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The 2019 Cloud Computing Advice Note says some organisations have their own classification systems and 'there are no central classification rules in place except for information defined as top secret, see Department of Finance Circular…. It is withheld until the fact or its source is corrected and checked again* |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The quote (found verbatim) establishes that the Revenue Commissioners, a state body, act as Certification Authority for ROS digital certificates, and the same manual says those certificates are used by the CRO, Department of Transport and…. It is withheld until the fact or its source is corrected and checked again* |
| State-controlled national eID | Yes[^s1] |
| Government data centres | Yes[^s2][^s3][^s4] |
| Government cloud in operation | Yes[^s4][^s5] |

What could move this placement:

Nothing: every input the rule reads is settled by a source.

## 2. Fundamentals

Ireland described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.511 million[^s6] |
| GDP, current prices | 602.4 EUR bn[^s7] |
| Public administration employment (NACE O) | 150.8 thousand[^s8] |
| Non-household electricity price | 255.2 EUR/MWh[^s9] |
| Renewables share of electricity | 41.7 %[^s10] |
| Land area | 68 655 km²[^s11] |

## 3. Critical data holdings, by priority

The holdings Ireland cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 9 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | register of births (with registers of stillbirths, deaths, marriages etc.)[^s12] | an tArd-Chláraitheoir (Registrar General)[^s12] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | SAFE 2 registration biometric facial templates (Public Services Card)[^s13] | Department of Social Protection (DSP)[^s13] | *Not stated in sources* | Facial templates for 70% of the State's population (2021)[^s13] |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | foreign births register[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Electoral roll entry (tier 0) | *Not yet sourced* | *Not yet sourced* | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The quote is one bullet in a list of LGERS project requirements ('Migration of project to DCC's Azure Public Cloud Tenancy') for a new central database that local authorities are still preparing to migrate to in 2025-2026; the page does…. It is withheld until the fact or its source is corrected and checked again* | 3.87 million registered electors (December 2024)[^s15] |
| Critical | Defence command and logistics (tier 1) | Defence Forces Enterprise network (NGWE project) and national Communications Information Services Network (CISN)[^s16] | Defence Forces CIS Corps[^s16] | Mixed[^s17] | *Not yet measured* |
| High | Document issuance history (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | MyGovID[^s1] | *Not yet sourced* | *Not stated in sources* | over 3.2 million people actively using their MyGovID account[^s1] |
| High | State PKI and qualified trust services (tier 0) | ROS digital certificate PKI (Revenue CA), also used by CRO, Department of Transport and Department of Social Protection[^s18] | Revenue Commissioners act as Certification Authority for ROS digital certificates[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | National Land Register (folios of the Land Registry) and Registry of Deeds[^s19][^s20] | Tailte Éireann (civil service body under the Tailte Éireann Act 2022)[^s19] | *Not stated in sources* | 2.4 million folios with associated spatial data accessible via landdirect.ie[^s19][^s20] |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | *Disputed: the fact check (claude-fable-5-1, run wf_72f99a66-4e9) did not confirm this: garda.ie refused the connection, so I read the project's hashed copy (sha256 c415d6a9…, as in fetch_manifest.csv); the quote is there and the CSO page quote is live. Both call PULSE 'An Garda Síochána's database' with incident data, but…. It is withheld until the fact or its source is corrected and checked again* | An Garda Síochána[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Intelligence services (tier 1) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The quote names Military Intelligence as a Defence Forces function delivering security outputs; nowhere does the report name a register or system, and 'holdings' is the report's own wording. The source confirms the unit exists but not a…. It is withheld until the fact or its source is corrected and checked again* | Military Intelligence (Defence Forces)[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | National Digital Radio Service (NDRS), TETRA network for first responders[^s22] | *Not yet sourced* | Non-EU provider[^s22] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Irish Residence Permission (IRP) register: the register of non-nationals with permission to be in the State[^s23] | Immigration Service Delivery (ISD), Department of Justice (took over first-time registration from the Garda National Immigration Bureau, 13 January 2025)[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | ROS database[^s2] | Revenue[^s2] | *Not stated in sources* | over 900,000 self-assessed taxpayers, 287,000 companies and 293,000 VAT traders registered[^s2] |
| High | Customs declarations (tier 1) | Automated Import System (AIS), Automated Export System (AES) and New Computerised Transit System (NCTS)[^s2] | Revenue Commissioners[^s2] | *Not stated in sources* | *Not yet sourced* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | PCRS eligibility records (medical card / GMS scheme eligibility, keyed on PPSN)[^s25] | HSE Primary Care Reimbursement Service (PCRS)[^s25] | *Not stated in sources* | 1,552,553 GMS (medical card) eligible persons and 785,152 GP visit card holders in 2025[^s26] |
| High | Business registry (tier 1) | Register of companies, business names and limited partnerships held by the Companies Registration Office[^s27] | Companies Registration Office (CRO), an office of the Department of Enterprise, Tourism and Employment[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Central Register of Beneficial Ownership of Companies and Industrial and Provident Societies[^s28] | Registrar of Beneficial Ownership of Companies and Industrial and Provident Societies[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | National Vehicle and Driver File (NVDF)[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | National connection to the Schengen Information System (SIS), live in Ireland since 15 March 2021[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Firearm certificates (three-year certificates, renewal phases administered by An Garda Síochána)[^s31] | An Garda Síochána (applications decided by the local Superintendent)[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The FMSS system name is supported, but the page contradicts '(incl. the Exchequer)': it says the Exchequer ran FMSS in parallel from April 2022 and that in September 2022 the Department of Finance 'made the decision to pause the…. It is withheld until the fact or its source is corrected and checked again* | National Shared Services Office (FMSS); Department of Finance manages the Exchequer[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | Election Count Database System (Ecount), used alongside the manual paper-ballot count[^s33] | Returning Officers per constituency[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET2-Ireland (Irish component of the Eurosystem T2 RTGS system)[^s34] | Central Bank of Ireland[^s34][^s35] | EU provider[^s34] | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | National Control Centres (NCCs) of the transmission system operator[^s36][^s37] | EirGrid (transmission system operator)[^s38][^s37] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Disputed: the cited source no longer contains the quoted text (rechecked 2026-09-30)* | *Disputed: the cited source no longer contains the quoted text (rechecked 2026-09-30)* | *Not stated in sources* | *Disputed: the cited source no longer contains the quoted text (rechecked 2026-09-30)* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | National Shared Care Record (NSCR), HSE MyHealth@IE programme (read-only aggregated record)[^s39] | Health Service Executive (Health Identifiers Service)[^s40] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Computerised Infectious Disease Reporting (CIDR)[^s41] | Health Protection Surveillance Centre (HPSC); CIDR established 2004[^s42] | *Not stated in sources* | On average 33,394 notified cases per year, 2013-2019 (range 25,814-46,065)[^s42] |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 27 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 1 |
| Mixed | 1 |
| Non-EU provider | 2 |
| Not stated in sources | 23 |

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

> Not yet sized. Capacity for Ireland will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 9 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Ireland without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Fingerprint biometric (tier 0)
- Document issuance history (tier 0)
- Authentication audit log (tier 0)
- Benefits & pensions (tier 1)
- Judicial & criminal justice (tier 1)
- Official gazette and legislation (tier 1)
- Government payroll and personnel (tier 1)
- Crisis management and civil protection (tier 1)
- Education (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1346 facts are printed, 3340 values are withheld as gaps, and 66 are withheld as disputed.

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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 620 |
| T2 competent public body or audit office | 612 |
| T3 other institution or company | 7 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 107 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 105 |
| Standard | 1241 |

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

In this build, 1346 of 1346 printed facts pass the fact check.

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

In this build, 1346 of 1346 printed facts pass, and 46 facts are withheld after the check.

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
| wf_72f99a66-4e9 | 2026-10-03 | 31 | claude-fable-5-1: 31 | supported: 25; not supported: 6 |
| wf_f14edd00-71f | 2026-10-02 | 12 | claude-fable-5-1: 12 | supported: 11; not supported: 1 |
| wf_5fd3e22d-b86 | 2026-10-02 | 27 | claude-fable-5-1: 27 | supported: 27 |
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Ireland

61 of 61 printed facts about Ireland pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:IE:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:IE:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:IE:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IE:population_m | param:IE:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:IE:gdp_eur_bn | param:IE:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IE:gov_employment_k | param:IE:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IE:elec_price_eur_mwh | param:IE:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IE:renewables_pct | param:IE:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:IE:land_km2 | param:IE:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:facial_biometric:count | Facial biometric: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:electoral_roll:count | Electoral roll entry: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:defence_command:register | Defence command and logistics: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:defence_command:operator | Defence command and logistics: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:defence_command:foreign_dependency | Defence command and logistics: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:IE:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:digital_identity_credentials:count | Digital identity credentials: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:land_property:count | Land & property registry: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:police_records:operator | Police information systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:intelligence:operator | Intelligence services: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:IE:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:emergency_communications:foreign_dependency | Emergency calls and public-safety radio: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:tax:operator | Tax: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:tax:count | Tax: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:customs:operator | Customs declarations: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:health_insurance:count | Statutory health insurance: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:electoral_management:operator | Election management and results: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:central_bank:operator | Central bank systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:central_bank:foreign_dependency | Central bank systems: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:grid_control:register | Electricity grid control: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:IE:grid_control:operator | Electricity grid control: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:IE:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:health_records:operator | Health records: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:public_health_surveillance:operator | Public health surveillance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:IE:public_health_surveillance:count | Public health surveillance: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Ireland

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| indicator:IE:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | claude-fable-5-1 | unclear | The quote (found verbatim) establishes that the Revenue Commissioners, a state body, act as Certification Authority for ROS digital certificates, and the same manual says those certificates are used by the CRO, Department of Transport and Department of Social Protection. However the document never describes this CA as the root of the government's PKI or as a qualified trust service (no occurrence  |
| indicator:IE:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | claude-fable-5-1 | unclear | The 2019 Cloud Computing Advice Note says some organisations have their own classification systems and 'there are no central classification rules in place except for information defined as top secret, see Department of Finance Circular 39/07'. Whether a Finance circular counts as a 'statute or binding regulation' is a judgment the source does not make, so 'Partly' is neither clearly supported nor  |
| record:IE:electoral_roll:foreign_dependency | Electoral roll entry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | not supported | The quote is one bullet in a list of LGERS project requirements ('Migration of project to DCC's Azure Public Cloud Tenancy') for a new central database that local authorities are still preparing to migrate to in 2025-2026; the page does not say the current 31 registers run there, nor does it identify Azure as a non-EU provider. Reaching 'Non-EU provider' needs outside knowledge and a future state  |
| record:IE:intelligence:register | Intelligence services: the name of the register or system | claude-fable-5-1 | not supported | The quote names Military Intelligence as a Defence Forces function delivering security outputs; nowhere does the report name a register or system, and 'holdings' is the report's own wording. The source confirms the unit exists but not a register of that name. |
| record:IE:police_records:register | Police information systems: the name of the register or system | claude-fable-5-1 | not supported | garda.ie refused the connection, so I read the project's hashed copy (sha256 c415d6a9…, as in fetch_manifest.csv); the quote is there and the CSO page quote is live. Both call PULSE 'An Garda Síochána's database' with incident data, but neither describes it as a 'national incident and intelligence database'; 'intelligence' is added beyond the sources. |
| record:IE:public_finance:register | Treasury and state accounts: the name of the register or system | claude-fable-5-1 | not supported | The FMSS system name is supported, but the page contradicts '(incl. the Exchequer)': it says the Exchequer ran FMSS in parallel from April 2022 and that in September 2022 the Department of Finance 'made the decision to pause the Exchequer's transfer to FMSS'. The source does not say the Exchequer is on FMSS. |

---

[^s1]: Department of Social Protection — Department of Social Protection Annual Report 2025, 2026-09-15. Department of Social Protection Annual Report 2025. <https://assets.gov.ie/static/documents/d05bae0e/20260915_-_DepartmentSocialProtection_AnnualReport_2025_EN_web.pdf>
[^s2]: Revenue Commissioners — Annual Report 2025, 2026. Annual Report 2025. <https://www.revenue.ie/en/corporate/press-office/annual-report/2025/ar-2025.pdf> ([archived](https://web.archive.org/web/20260507225147/https://www.revenue.ie/en/corporate/press-office/annual-report/2025/ar-2025.pdf))
[^s3]: Office of the Government Chief Information Officer (OGCIO) — Cloud Computing Advice Note (October 2019), 2019-10. Cloud Computing Advice Note (October 2019). <https://assets.per.gov.ie/documents/4468be59812f40dda7003116cf05f196_1.pdf>
[^s4]: Office of the Government Chief Information Officer (OGCIO) — Build To Share, 2025-07-30. Build To Share. <https://www.ogcio.gov.ie/en/corporate-pages/policy/build-to-share/> ([archived](https://web.archive.org/web/20260128012721/https://www.ogcio.gov.ie/en/corporate-pages/policy/build-to-share/))
[^s5]: Office of the Government Chief Information Officer (OGCIO) — Infrastructure, 2025-07-30. Infrastructure. <https://www.ogcio.gov.ie/en/corporate-pages/services/infrastructure/> ([archived](https://web.archive.org/web/20260618083911/https://www.ogcio.gov.ie/en/corporate-pages/services/infrastructure/))
[^s6]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s7]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s8]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s9]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s10]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s11]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s12]: Office of the Attorney General (Irish Statute Book) — Civil Registration Act 2004, Section 13, 2004. Civil Registration Act 2004, Section 13. <https://www.irishstatutebook.ie/eli/2004/act/3/section/13/enacted/en/html> ([archived](https://web.archive.org/web/20260615114456/https://www.irishstatutebook.ie/eli/2004/act/3/section/13/enacted/en/html))
[^s13]: Data Protection Commission — DPC announces conclusion of investigation into use of…, 2025-06-12. DPC announces conclusion of investigation into use of facial matching technology in connection with Public Services Card. <https://www.dataprotection.ie/en/news-media/press-releases/dpc-announces-conclusion-investigation-use-facial-matching-technology-connection-public-services> ([archived](https://web.archive.org/web/20260926120514/https://www.dataprotection.ie/en/news-media/press-releases/dpc-announces-conclusion-investigation-use-facial-matching-technology-connection-public-services))
[^s14]: Office of the Attorney General (Irish Statute Book) — Passports Act 2008, 2008. Passports Act 2008. <https://www.irishstatutebook.ie/eli/2008/act/4/enacted/en/print> ([archived](https://web.archive.org/web/20260607170551/https://www.irishstatutebook.ie/eli/2008/act/4/enacted/en/print))
[^s15]: An Coimisiún Toghcháin (Electoral Commission) — Oversight Report on the Electoral Registers, 2025. Oversight Report on the Electoral Registers. <https://cdn.electoralcommission.ie/app/uploads/2025/04/30104313/Oversight-Report-on-the-Electoral-Registers_online_english_tagged.pdf> ([archived](https://web.archive.org/web/20251026075202/https://cdn.electoralcommission.ie/app/uploads/2025/04/30104313/Oversight-Report-on-the-Electoral-Registers_online_english_tagged.pdf))
[^s16]: Department of Defence — Department of Defence and Defence Forces Annual Report 2024, 2025. Department of Defence and Defence Forces Annual Report 2024. <https://assets.gov.ie/static/documents/54a1dec6/Department_of_Defence_and_Defence_Forces_Annual_Report_2024_English_DNet.pdf> ([archived](https://web.archive.org/web/20260311093310/https://assets.gov.ie/static/documents/54a1dec6/Department_of_Defence_and_Defence_Forces_Annual_Report_2024_English_DNet.pdf))
[^s17]: Department of Defence (Ireland) — Department of Defence and Defence Forces Annual Report 2023, 2024. Department of Defence and Defence Forces Annual Report 2023. <https://assets.gov.ie/309800/2b584813-bbbb-4c12-be67-7489bc5c5a8b.pdf> ([archived](https://web.archive.org/web/20250126183302/https://assets.gov.ie/309800/2b584813-bbbb-4c12-be67-7489bc5c5a8b.pdf))
[^s18]: Revenue Commissioners — Tax and Duty Manual Part 38-06-01 Revenue Online Service…, 2025-10. Tax and Duty Manual Part 38-06-01 Revenue Online Service (ROS). <https://www.revenue.ie/en/tax-professionals/tdm-wm/income-tax-capital-gains-tax-corporation-tax/part-38/38-06-01.pdf> ([archived](https://web.archive.org/web/20260520131022/https://www.revenue.ie/en/tax-professionals/tdm-wm/income-tax-capital-gains-tax-corporation-tax/part-38/38-06-01.pdf))
[^s19]: Tailte Éireann — Tailte Éireann Annual Report 2024, 2025. Tailte Éireann Annual Report 2024. <https://tailte.ie/wp-content/uploads/2025/11/TE_AnnualReport2024_GA_EN.pdf> ([archived](https://web.archive.org/web/20260513220930/https://tailte.ie/wp-content/uploads/2025/11/TE_AnnualReport2024_GA_EN.pdf))
[^s20]: Tailte Éireann — Tailte Éireann Annual Report 2025, 2026-09. Tailte Éireann Annual Report 2025. <https://tailte.ie/wp-content/uploads/2026/09/Annual-Report-2025-Final-EN-GA-1.pdf>
[^s21]: An Garda Síochána — Garda Information Services Centre (GISC). Garda Information Services Centre (GISC). <https://www.garda.ie/en/about-us/our-departments/garda-information-services-centre-gisc-/> ([archived](https://web.archive.org/web/20260610071140/https://www.garda.ie/en/about-us/our-departments/garda-information-services-centre-gisc-/))
[^s22]: Motorola Solutions, Inc. — Motorola Solutions Acquires TETRA Ireland…, 2022-03-23. Motorola Solutions Acquires TETRA Ireland Communications, The Provider of Ireland's National Digital Radio Service. <https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-acquires-tetra-ireland-communications.html> ([archived](https://web.archive.org/web/20260711055831/https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-acquires-tetra-ireland-communications.html))
[^s23]: Immigration Service Delivery, Department of Justice — Information on revocation of registered Irish Residence…. Information on revocation of registered Irish Residence Permissions. <https://www.irishimmigration.ie/information-on-revocation-of-registered-irish-residence-permissions/> ([archived](https://web.archive.org/web/20260518125209/https://www.irishimmigration.ie/information-on-revocation-of-registered-irish-residence-permissions/))
[^s24]: An Garda Síochána — Immigration (GNIB) - Registration & Renewal of…. Immigration (GNIB) - Registration & Renewal of Immigration Permission. <https://www.garda.ie/en/about-us/organised-serious-crime/immigration-gnib-/> ([archived](https://web.archive.org/web/20260917111236/https://www.garda.ie/en/about-us/organised-serious-crime/immigration-gnib-/))
[^s25]: Health Information and Quality Authority — Primary Care Reimbursement Service (PCRS). Primary Care Reimbursement Service (PCRS). <https://www.hiqa.ie/areas-we-work/health-information/data-collections/primary-care-reimbursement-service-pcrs>
[^s26]: Health Service Executive (copy hosted by HRB National Drugs Library) — Primary Care Reimbursement Service Statistical Analysis…, 2026. Primary Care Reimbursement Service Statistical Analysis of Claims and Payments 2025. <https://www.drugsandalcohol.ie/46590/1/PCRS_Statistical_Analysis_of_Claims_and_Payments_2025.pdf>
[^s27]: Department of Enterprise, Tourism and Employment — Companies Registration Office (CRO). Companies Registration Office (CRO). <https://enterprise.gov.ie/en/who-we-are/offices-agencies/companies-registration-office-cro-.html> ([archived](https://web.archive.org/web/20260526152748/https://enterprise.gov.ie/en/who-we-are/offices-agencies/companies-registration-office-cro-.html))
[^s28]: Office of the Attorney General (Irish Statute Book) — S.I. No. 110 of 2019 European Union (Anti-Money…, 2019. S.I. No. 110 of 2019 European Union (Anti-Money Laundering: Beneficial Ownership of Corporate Entities) Regulations 2019. <https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print> ([archived](https://web.archive.org/web/20260613064358/https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print))
[^s29]: Government of Ireland PSB Data Catalogue — National Vehicle and Driver Database. National Vehicle and Driver Database. <https://datacatalogue.gov.ie/dataset/national-vehicle-and-driver-database> ([archived](https://web.archive.org/web/20260217001228/https://datacatalogue.gov.ie/dataset/national-vehicle-and-driver-database))
[^s30]: An Garda Síochána — Schengen Information System (SIS): When was it introduced?. Schengen Information System (SIS): When was it introduced?. <https://www.garda.ie/en/about-us/our-departments/garda-national-crime-security-intelligence-service1/schengen-information-system-sis-/when-was-it-introduced-.html>
[^s31]: An Garda Síochána — Firearms Licensing. Firearms Licensing. <https://www.garda.ie/en/about-us/online-services/firearms-licensing/> ([archived](https://web.archive.org/web/20260917111136/https://www.garda.ie/en/about-us/online-services/firearms-licensing/))
[^s32]: Office of the Comptroller and Auditor General — Report on the Accounts of the Public Services 2022,…, 2023. Report on the Accounts of the Public Services 2022, Chapter 6: Financial management shared services: implementation progress. <https://www.audit.gov.ie/media/jqinw3i5/6-financial-management-shared-services-implementation-progress.pdf>
[^s33]: Department of Housing, Local Government and Heritage — Memorandum for the Guidance of Returning Officers,…, 2024. Memorandum for the Guidance of Returning Officers, General Election 2024. <https://assets.gov.ie/312963/3e85cb42-027b-4ede-8249-20112f9f652c.pdf>
[^s34]: Central Bank of Ireland — T2. T2. <https://www.centralbank.ie/financial-system/payments-and-securities-settlements/target-services/t2> ([archived](https://web.archive.org/web/20260315043823/https://www.centralbank.ie/financial-system/payments-and-securities-settlements/target-services/t2))
[^s35]: Central Bank of Ireland — Annual Report 2025 and Annual Performance Statement…, 2026. Annual Report 2025 and Annual Performance Statement 2025-2026. <https://www.centralbank.ie/docs/default-source/publications/corporate-reports/annual-reports/annual-report-2025-and-annual-performance-statement-2025-2026.pdf> ([archived](https://web.archive.org/web/20260801021138/https://www.centralbank.ie/docs/default-source/publications/corporate-reports/annual-reports/annual-report-2025-and-annual-performance-statement-2025-2026.pdf))
[^s36]: EirGrid plc — EirGrid Grid Code Version 14.3, 2025-03-25. EirGrid Grid Code Version 14.3. <https://cms.eirgrid.ie/sites/default/files/publications/GridCodeVersion14.3.pdf> ([archived](https://web.archive.org/web/20260828073337/https://cms.eirgrid.ie/sites/default/files/publications/GridCodeVersion14.3.pdf))
[^s37]: EirGrid — National Control Centres. National Control Centres. <https://www.eirgrid.ie/grid/how-grid-works/national-control-centres>
[^s38]: EirGrid — Did You Know? 10 fast facts about EirGrid. Did You Know? 10 fast facts about EirGrid. <https://www.eirgrid.ie/did-you-know> ([archived](https://web.archive.org/web/20260305052734/https://www.eirgrid.ie/did-you-know))
[^s39]: HSE MyHealth@IE programme (hosted by Irish Institute of Pharmacy) — National Shared Care Record: Enabling Data, Enhancing…, 2026-06-10. National Shared Care Record: Enabling Data, Enhancing Care (MyHealth@IE programme webinar). <https://iiop.ie/sites/default/files/2026-06/NSCR%20Presentation_10%20June%202026_IIOPWebinar.pdf>
[^s40]: Health Information and Quality Authority — National Register of Individual Health Identifiers. National Register of Individual Health Identifiers. <https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-register-individual-health-identifiers>
[^s41]: Health Protection Surveillance Centre (HSE) — Computerised Infectious Disease Reporting (CIDR). Computerised Infectious Disease Reporting (CIDR). <https://www.hpsc.ie/cidr/> ([archived](https://web.archive.org/web/20260911101522/https://www.hpsc.ie/cidr/))
[^s42]: Health Information and Quality Authority — Computerised Infectious Disease Reporting (CIDR) system. Computerised Infectious Disease Reporting (CIDR) system. <https://www.hiqa.ie/areas-we-work/health-information/data-collections/computerised-infectious-disease-reporting-cidr> ([archived](https://web.archive.org/web/20240704233334/https://www.hiqa.ie/areas-we-work/health-information/data-collections/computerised-infectious-disease-reporting-cidr))

**Evidence grades:** 28 Strong, 33 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
