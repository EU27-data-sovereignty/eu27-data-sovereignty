# Hungary: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Hungary could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2][^s3] |
| Classification in law | Yes[^s4][^s3] |
| Sovereign cloud certification | No[^s3] |
| State-controlled trust anchor | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The quote is on the page and says NISZ Zrt. is the designated government certification service provider (GovCA) providing trust and PKI services, but the page nowhere states that NISZ is state-owned or state-controlled (no mention of 'állam It is withheld until the fact or its source is corrected and checked again* |
| State-controlled national eID | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The DMÜ page says the agency owns six companies and that IdomSoft contributes 'as developer' to the Digital Citizenship Programme, and the Act says the Government designates the framework-service body and the digital citizenship provider; n It is withheld until the fact or its source is corrected and checked again* |
| Government data centres | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The DMÜ page says the agency decides on mandatory use of, or exemption from, 'Kormányzati Adatközpont' services, which implies such services exist, but the quote does not say the state operates the data centre or that it is in operation tod It is withheld until the fact or its source is corrected and checked again* |
| Government cloud in operation | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: Annex 1 point 4.2.2.4 of Decree 418/2024 names 'kormányzati felhő' as a permitted venue for F4 data, which presupposes a government cloud, but the decree does not state that such a platform is in operation rather than merely provided for, s It is withheld until the fact or its source is corrected and checked again* |

What could move this placement:

- If any of the 24 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Hungary described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 9.49 million[^s5] |
| GDP, current prices | 218.8 EUR bn[^s6] |
| Public administration employment (NACE O) | 346.3 thousand[^s7] |
| Non-household electricity price | 213.2 EUR/MWh[^s8] |
| Renewables share of electricity | 28.3 %[^s9] |
| Land area | 91 248 km²[^s10] |

## 3. Critical data holdings, by priority

The holdings Hungary cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 31 of 39 holding classes have a verified source; 2 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| High | Civil registry core (tier 0) | Személyiadat- és lakcímnyilvántartás (Personal Data and Address Register): the authentic official register of citizens' personal, address and notification-address data[^s11][^s12] | *Not yet sourced* | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The quote states IdomSoft is state-owned; the page nowhere mentions the civil register (anyakönyv) or who hosts it, so it does not support that the civil registry's infrastructure is national. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | Facial biometric (tier 0) | The SZL stores the facial image (arcképmás) and signature of citizens who applied for an ID card[^s12] | The Minister for Science and Technology is designated central organ under the 2015 facial image analysis act[^s13] | National infrastructure[^s12] | *Not yet measured* |
| High | Fingerprint biometric (tier 0) | With written consent, the SZL stores the citizen's fingerprint for replacing the permanent ID card[^s12] | Minister of Interior designated as criminal records body, including the register of criminal and law-enforcement biometric data[^s13] | National infrastructure[^s12] | *Not yet measured* |
| High | Breeder document scans (tier 0) | The electronic civil register includes the register of civil-status and name-change certificates (okiratnyilvántartás)[^s14] | Minister for Science and Technology is the civil-register keeping body[^s13] | National infrastructure[^s14] | *Not yet measured* |
| High | Authentication audit log (tier 0) | The register keeper records every data-processing operation in an automated log system (naplórendszer)[^s15] | *Not yet sourced* | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The quote only says IdomSoft came into direct state ownership in July 2024; the page elsewhere names IdomSoft as the DÁP provider and operator, but never mentions the log system (naplórendszer) or where its infrastructure runs, so 'National It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | CSCA-HUNGARY country signing CA for e-passports, operated by the passport-issuing ministry[^s16][^s17] | NISZ Zrt. is the designated provider of government e-signature, e-seal and signature validation[^s18][^s19] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | The land register contains every property located in Hungary, settlement by settlement[^s20][^s21][^s22] | Lechner Tudásközpont is designated land authority (with county government offices)[^s21][^s23] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | Police place SIS alerts via the wanted-persons register system[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The SZL records ID card document identifiers and electronic unique identifiers[^s11][^s12] | Energiaügyi Minisztérium (Ministry of Energy) as registering body for passports[^s17] | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The quote establishes IdomSoft's state ownership only; the history page never mentions document issuance records or document registers, so it does not support where that holding's infrastructure runs. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Digital citizenship register: the client-registration register created by the Digital State Act[^s15] | IdomSoft Zrt. designated as digital citizenship service provider[^s25][^s26][^s19] | National infrastructure[^s26] | *Not yet measured* |
| High | Electoral roll entry (tier 0) | The central electoral register is an electronic register kept by the National Election Office[^s27] | IdomSoft builds the National Election System used by election offices[^s11] | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The quote only states that IdomSoft became directly state-owned; neither the quote nor anything else on the history page mentions the electoral roll or any election system, so the page does not connect this holding to IdomSoft or say what i It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | Tax (tier 1) | adószámla (taxpayer current accounts) kept by NAV[^s28] | *Not yet sourced* | *Not stated in sources* | more than 8 million tax accounts[^s28] |
| High | Customs declarations (tier 1) | Automatizált Export Rendszer (AES) (Automated Export System)[^s28] | *Not yet sourced* | *Not stated in sources* | 2 404 687 customs goods declarations[^s28] |
| High | Benefits & pensions (tier 1) | társadalombiztosítási jogszerzési nyilvántartás (social-security entitlement register) and register of benefits paid[^s29] | Government designates the Hungarian State Treasury Pension Disbursement Directorate as a pension insurance administration body[^s30][^s31] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | NEAK keeps the register of insured persons' relationship data, entitlement and TAJ data[^s32][^s33] | NEAK is a health insurance body[^s34][^s33] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | The beneficial ownership register contains the data of reporting entities[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | N.SIS comprises the full national copy of SIS and the national backbone, among other parts[^s36] | N.SIS Office is responsible for data in the national copy[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Holders must report firearm data to police for the central firearms register[^s37] | Firearms licences are issued by the police[^s37] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Központi Költségvetés Végrehajtását Támogató Rendszer (KKVTR / IFMIS) (Central Budget Execution Support System)[^s38] | Magyar Államkincstár (Hungarian State Treasury)[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Payroll-based tax obligations are met exclusively through the centralised payroll system operated by the Treasury[^s29][^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | Nemzeti Választási Rendszer (National Election System)[^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | Instant payment service launched 2 March 2020[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | EDR: the Schengen-compliant digital government radio network[^s41][^s42] | The police handle calls to emergency numbers[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Public alarm system managed by the professional disaster management body[^s43][^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Central register of issued school-leaving (matura) certificates[^s45] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Residence and migration status (tier 1) | Third-country nationals' data are kept in the sub-registers of the central aliens-policing register[^s46] | The Minister of Interior is responsible for aliens policing and asylum[^s13] | National infrastructure[^s46] | *Not yet measured* |
| Standard | Vehicle & licensing (tier 1) | National Vehicle Register system built/run by IdomSoft[^s11][^s47] | Minister for Science and Technology is the road transport registering body[^s13] | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: The quote is about IdomSoft's ownership; the history page does not mention the vehicle register or driving licences, so it does not tie that holding to IdomSoft or say on what infrastructure it runs. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Magyar Közlöny (Hungarian Official Gazette)[^s48] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Vaccination data are entered into the electronic epidemiological surveillance system[^s49][^s50] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | KSH conducts censuses and micro-censuses[^s51] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | Central address register provides an authentic address source for registers[^s52][^s15] | Lechner manages national geodata databases and runs the national spatial data infrastructure[^s53][^s23] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 31 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 10 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 21 |

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

> Not yet sized. Capacity for Hungary will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 2 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Hungary without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Business registry (tier 1)
- Judicial & criminal justice (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1309 facts are printed, 3342 values are withheld as gaps, and 101 are withheld as disputed.

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
| below_T2 | 5 |
| corroborated | 238 |
| disputed | 10 |
| filled_gap | 363 |
| holding_not_established | 38 |
| no_better_found | 447 |
| not_reached | 201 |
| not_verified | 176 |
| review_disagreed | 153 |
| same_source | 8 |
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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 612 |
| T2 competent public body or audit office | 589 |
| T3 other institution or company | 7 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 101 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 100 |
| Standard | 1209 |

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

In this build, 1309 of 1309 printed facts pass the fact check.

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

In this build, 1309 of 1309 printed facts pass, and 81 facts are withheld after the check.

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
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Hungary

64 of 64 printed facts about Hungary pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:HU:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:HU:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:HU:L3 | indicator L3: Is a cloud certification that requires immunity from non-EU law in force or adopted for government use? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:HU:population_m | param:HU:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:HU:gdp_eur_bn | param:HU:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:HU:gov_employment_k | param:HU:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:HU:elec_price_eur_mwh | param:HU:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:HU:renewables_pct | param:HU:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:HU:land_km2 | param:HU:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:facial_biometric:foreign_dependency | Facial biometric: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:fingerprint_biometric:operator | Fingerprint biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:fingerprint_biometric:foreign_dependency | Fingerprint biometric: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:breeder_documents:foreign_dependency | Breeder document scans: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:digital_identity_credentials:foreign_dependency | Digital identity credentials: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:tax:count | Tax: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:customs:count | Customs declarations: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:residence_permits:foreign_dependency | Residence and migration status: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:HU:geospatial:operator | Geospatial base data: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Hungary

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| indicator:HU:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | claude-fable-5-1 | unclear | The DMÜ page says the agency decides on mandatory use of, or exemption from, 'Kormányzati Adatközpont' services, which implies such services exist, but the quote does not say the state operates the data centre or that it is in operation today. |
| indicator:HU:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | claude-fable-5-1 | unclear | Annex 1 point 4.2.2.4 of Decree 418/2024 names 'kormányzati felhő' as a permitted venue for F4 data, which presupposes a government cloud, but the decree does not state that such a platform is in operation rather than merely provided for, so it does not by itself establish 'in operation (not announced)'. |
| indicator:HU:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | claude-fable-5-1 | unclear | The quote is on the page and says NISZ Zrt. is the designated government certification service provider (GovCA) providing trust and PKI services, but the page nowhere states that NISZ is state-owned or state-controlled (no mention of 'állami tulajdon'), so the 'state or state-controlled body' element of the indicator rests on knowledge outside the cited source. |
| indicator:HU:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | claude-fable-5-1 | unclear | The DMÜ page says the agency owns six companies and that IdomSoft contributes 'as developer' to the Digital Citizenship Programme, and the Act says the Government designates the framework-service body and the digital citizenship provider; neither cited passage states who operates the eID scheme or that the operator is state-controlled, so 'Yes' is not established by these quotes. |
| record:HU:authentication_audit_log:foreign_dependency | Authentication audit log: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | unclear | The quote only says IdomSoft came into direct state ownership in July 2024; the page elsewhere names IdomSoft as the DÁP provider and operator, but never mentions the log system (naplórendszer) or where its infrastructure runs, so 'National infrastructure' rests on inference rather than the source. |
| record:HU:civil_registry:foreign_dependency | Civil registry core: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | not supported | The quote states IdomSoft is state-owned; the page nowhere mentions the civil register (anyakönyv) or who hosts it, so it does not support that the civil registry's infrastructure is national. |
| record:HU:electoral_roll:foreign_dependency | Electoral roll entry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | not supported | The quote only states that IdomSoft became directly state-owned; neither the quote nor anything else on the history page mentions the electoral roll or any election system, so the page does not connect this holding to IdomSoft or say what infrastructure it runs on. |
| record:HU:issuance_history:foreign_dependency | Document issuance history: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | not supported | The quote establishes IdomSoft's state ownership only; the history page never mentions document issuance records or document registers, so it does not support where that holding's infrastructure runs. |
| record:HU:vehicle_licensing:foreign_dependency | Vehicle & licensing: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | not supported | The quote is about IdomSoft's ownership; the history page does not mention the vehicle register or driving licences, so it does not tie that holding to IdomSoft or say on what infrastructure it runs. |

---

[^s1]: Wolters Kluwer Jogtár (consolidated text of Act LXIX of 2024) — 2024. évi LXIX. törvény Magyarország kiberbiztonságáról…, 2024. 2024. évi LXIX. törvény Magyarország kiberbiztonságáról (Kiberbiztonsági tv.), 9. §. <https://net.jogtar.hu/jogszabaly?docid=a2400069.tv>
[^s2]: Wolters Kluwer Jogtár (consolidated text of Government Decree 418/2024) — 418/2024. (XII. 23.) Korm. rendelet a Magyarország…, 2024-12-23. 418/2024. (XII. 23.) Korm. rendelet a Magyarország kiberbiztonságáról szóló törvény végrehajtásáról, 1. melléklet. <https://net.jogtar.hu/jogszabaly?docid=a2400418.kor> ([archived](https://web.archive.org/web/20251123140140/https://net.jogtar.hu/jogszabaly?docid=A2400418.KOR))
[^s3]: Nemzeti Kibervédelmi Intézet / national cybersecurity authority — Felhő – harmadik fél által tanúsított…. Felhő – harmadik fél által tanúsított felhőszolgáltatások (Cloud – third-party certified cloud services). <https://nki.gov.hu/hatosag/tartalom/felho/> ([archived](https://web.archive.org/web/20250628235716/https://nki.gov.hu/hatosag/tartalom/felho/))
[^s4]: Wolters Kluwer Jogtár (consolidated text of Act CLV of 2009) — 2009. évi CLV. törvény a minősített adat védelméről, 5.…, 2009. 2009. évi CLV. törvény a minősített adat védelméről, 5. § (4). <https://net.jogtar.hu/jogszabaly?docid=a0900155.tv> ([archived](https://web.archive.org/web/20260107073215/https://net.jogtar.hu/jogszabaly?docid=A0900155.TV))
[^s5]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s6]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s7]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s8]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s9]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s10]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s11]: IdomSoft Informatikai Zrt. — Termékek | IdomSoft Zrt.. Termékek | IdomSoft Zrt.. <https://www.idomsoft.hu/termekek> ([archived](https://web.archive.org/web/20260512054003/https://www.idomsoft.hu/termekek/))
[^s12]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 1992. évi LXVI. törvény a polgárok személyi adatainak és…, 1992. 1992. évi LXVI. törvény a polgárok személyi adatainak és lakcímének nyilvántartásáról. <https://net.jogtar.hu/jogszabaly?docid=99200066.tv> ([archived](https://web.archive.org/web/20251224033602/https://net.jogtar.hu/jogszabaly?docid=99200066.TV))
[^s13]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 90/2026. (V. 13.) Korm. rendelet a Kormány tagjainak…, 2026. 90/2026. (V. 13.) Korm. rendelet a Kormány tagjainak feladat- és hatásköréről. <https://net.jogtar.hu/jogszabaly?docid=A2600090.KOR>
[^s14]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2010. évi I. törvény az anyakönyvi eljárásról, 2010. 2010. évi I. törvény az anyakönyvi eljárásról. <https://net.jogtar.hu/jogszabaly?docid=A1000001.TV> ([archived](https://web.archive.org/web/20260913003001/https://net.jogtar.hu/jogszabaly?docid=a1000001.tv))
[^s15]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2023. évi CIII. törvény a digitális államról és a…, 2023. 2023. évi CIII. törvény a digitális államról és a digitális szolgáltatások nyújtásának egyes szabályairól. <https://net.jogtar.hu/jogszabaly?docid=A2300103.TV> ([archived](https://web.archive.org/web/20251203022211/https://net.jogtar.hu/jogszabaly?docid=A2300103.TV))
[^s16]: Magyarország Kormánya (kormany.hu) — Tájékoztató a CSCA tanúsítványról. Tájékoztató a CSCA tanúsítványról. <https://kormany.hu/nyilvantartasok/biometrikus-utlevel/tajekoztato-a-csca-tanusitvanyrol> ([archived](https://web.archive.org/web/20260920201822/https://kormany.hu/nyilvantartasok/biometrikus-utlevel/tajekoztato-a-csca-tanusitvanyrol))
[^s17]: Magyarország Kormánya (kormany.hu) — Biometrikus útlevél. Biometrikus útlevél. <https://kormany.hu/nyilvantartasok/biometrikus-utlevel/biometrikus-utlevel> ([archived](https://web.archive.org/web/20260928081611/https://kormany.hu/nyilvantartasok/biometrikus-utlevel/biometrikus-utlevel))
[^s18]: Kormányzati Hitelesítés Szolgáltató (GovCA), NISZ Zrt. — Kormányzati Hitelesítés Szolgáltató – Kik vagyunk. Kormányzati Hitelesítés Szolgáltató – Kik vagyunk. <https://hiteles.gov.hu/cikk/185/kormanyzati_hitelesites_szolgaltato> ([archived](https://web.archive.org/web/20260708154825/https://hiteles.gov.hu/cikk/185/kormanyzati_hitelesites_szolgaltato))
[^s19]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 320/2024. (XI. 6.) Korm. rendelet a digitális állam…, 2024. 320/2024. (XI. 6.) Korm. rendelet a digitális állam megvalósításához kapcsolódó egyes szervezetek kijelöléséről. <https://net.jogtar.hu/jogszabaly?docid=A2400320.KOR>
[^s20]: Magyarország Kormánya / Tudományos és Technológiai Minisztérium — Büntetőfeljelentést tesz a kormány a félkész…, 2026-09-28. Büntetőfeljelentést tesz a kormány a félkész ingatlan-nyilvántartási rendszer miatt. <https://kormany.hu/hirek/buntetofeljelentest-tesz-a-kormany-a-felkesz-ingatlan-nyilvantartasi-rendszer-miatt>
[^s21]: Lechner Tudásközpont — Ingatlan-nyilvántartás áttekintés. Ingatlan-nyilvántartás áttekintés. <https://lechnerkozpont.hu/oldal/ingatlan-nyilvantartas-attekintes> ([archived](https://web.archive.org/web/20260615084146/https://lechnerkozpont.hu/oldal/ingatlan-nyilvantartas-attekintes))
[^s22]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2021. évi C. törvény az ingatlan-nyilvántartásról, 2021. 2021. évi C. törvény az ingatlan-nyilvántartásról. <https://net.jogtar.hu/jogszabaly?docid=A2100100.TV>
[^s23]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 383/2016. (XII. 2.) Korm. rendelet a földművelésügyi…, 2016. 383/2016. (XII. 2.) Korm. rendelet a földművelésügyi hatósági és igazgatási feladatokat ellátó szervek kijelöléséről. <https://net.jogtar.hu/jogszabaly?docid=A1600383.KOR> ([archived](https://web.archive.org/web/20240711234223/https://net.jogtar.hu/jogszabaly?docid=a1600383.kor))
[^s24]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 1994. évi XXXIV. törvény a Rendőrségről, 1994. 1994. évi XXXIV. törvény a Rendőrségről. <https://net.jogtar.hu/jogszabaly?docid=99400034.TV> ([archived](https://web.archive.org/web/20260626121651/https://net.jogtar.hu/jogszabaly?docid=99400034.tv))
[^s25]: Digitális Állampolgárság Program (dap.gov.hu) — Impresszum - Digitális Állampolgár weboldal. Impresszum - Digitális Állampolgár weboldal. <https://dap.gov.hu/impresszum> ([archived](https://web.archive.org/web/20260519223451/https://dap.gov.hu/impresszum))
[^s26]: IdomSoft Informatikai Zrt. — Történetünk | IdomSoft Zrt.. Történetünk | IdomSoft Zrt.. <https://www.idomsoft.hu/rolunk/tortenetunk> ([archived](https://web.archive.org/web/20260422201158/https://www.idomsoft.hu/rolunk/tortenetunk/))
[^s27]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2013. évi XXXVI. törvény a választási eljárásról, 2013. 2013. évi XXXVI. törvény a választási eljárásról. <https://net.jogtar.hu/jogszabaly?docid=A1300036.TV> ([archived](https://web.archive.org/web/20260727221758/https://net.jogtar.hu/jogszabaly?docid=a1300036.tv))
[^s28]: Nemzeti Adó- és Vámhivatal (NAV) — NAV Évkönyv 2025, 2026-06-03. NAV Évkönyv 2025. <https://nav.gov.hu/pfile/file?path=/kiadvanyok/evkonyvek/nav-evkonyv-2025>
[^s29]: Magyar Államkincstár (Hungarian State Treasury) — A Kincstár tevékenysége, 2023-02-01. A Kincstár tevékenysége. <https://www.allamkincstar.gov.hu/header-tartalmak/rolunk/a-kincstar-tevekenysege/a-kincstar-tevekenysege1> ([archived](https://web.archive.org/web/20260616063952/https://www.allamkincstar.gov.hu/header-tartalmak/rolunk/a-kincstar-tevekenysege/a-kincstar-tevekenysege1))
[^s30]: Magyar Államkincstár (Hungarian State Treasury) — Nyugdíjfolyósító Igazgatóság. Nyugdíjfolyósító Igazgatóság. <https://www.allamkincstar.gov.hu/header-tartalmak/rolunk/a-kincstar-szervezete/magyar-allamkincstar-szervezeti-egysegei/nyugdijfolyosito-igazgatosag> ([archived](https://web.archive.org/web/20260917090433/https://www.allamkincstar.gov.hu/header-tartalmak/rolunk/a-kincstar-szervezete/magyar-allamkincstar-szervezeti-egysegei/nyugdijfolyosito-igazgatosag))
[^s31]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 168/1997. (X. 6.) Korm. rendelet a társadalombiztosítási…, 1997. 168/1997. (X. 6.) Korm. rendelet a társadalombiztosítási nyugellátásról szóló 1997. évi LXXXI. törvény végrehajtásáról. <https://net.jogtar.hu/jogszabaly?docid=99700168.KOR> ([archived](https://web.archive.org/web/20260523233650/https://net.jogtar.hu/jogszabaly?docid=99700168.kor))
[^s32]: Nemzeti Egészségbiztosítási Alapkezelő (NEAK) — Bejelentett személyek jogviszonyadatainak nyilvántartása. Bejelentett személyek jogviszonyadatainak nyilvántartása. <https://www.neak.gov.hu/felso_menu/rolunk/kozerdeku_adatok/tevekenysegre_mukodesre_vonatkozo_adatok/a_szerv_nyilvantartasai/bejelentett_szemelyek_jogviszonyadatainak_nyilvant/bejelentett_szemeleyek_jogviszonyadatainak_nyilvan> ([archived](https://web.archive.org/web/20260520013907/https://www.neak.gov.hu/felso_menu/rolunk/kozerdeku_adatok/tevekenysegre_mukodesre_vonatkozo_adatok/a_szerv_nyilvantartasai/bejelentett_szemelyek_jogviszonyadatainak_nyilvant/bejelentett_szemeleyek_jogviszonyadatainak_nyilvan))
[^s33]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 386/2016. (XII. 2.) Korm. rendelet az…, 2016. 386/2016. (XII. 2.) Korm. rendelet az egészségbiztosítási szervekről. <https://net.jogtar.hu/jogszabaly?docid=A1600386.KOR>
[^s34]: Nemzeti Egészségbiztosítási Alapkezelő (NEAK) — Tasks of the National Health Insurance Fund of Hungary…. Tasks of the National Health Insurance Fund of Hungary (Hungarian acronym: NEAK). <https://www.neak.gov.hu/felso_menu/rolunk/kozerdeku_adatok/tevekenysegre_mukodesre_vonatkozo_adatok/a_szerv_feladata_alaptevekenysege_es_hatarkore/en_a_szerv_alaptevekenyege_feladata_es_hatarkore/a_neak_feladata_alaptevekenysege_hataskore_angol> ([archived](https://web.archive.org/web/20260609092111/https://www.neak.gov.hu/felso_menu/rolunk/kozerdeku_adatok/tevekenysegre_mukodesre_vonatkozo_adatok/a_szerv_feladata_alaptevekenysege_es_hatarkore/en_a_szerv_alaptevekenyege_feladata_es_hatarkore/a_neak_feladata_alaptevekenysege_hataskore_angol))
[^s35]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2021. évi XLIII. törvény a pénzügyi és egyéb…, 2021. 2021. évi XLIII. törvény a pénzügyi és egyéb szolgáltatók azonosítási feladatához kapcsolódó adatszolgáltatási háttér megteremtéséről és működtetéséről. <https://net.jogtar.hu/jogszabaly?docid=A2100043.TV> ([archived](https://web.archive.org/web/20250823190745/https://net.jogtar.hu/jogszabaly?docid=a2100043.tv))
[^s36]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2012. évi CLXXXI. törvény a Schengeni Információs…, 2012. 2012. évi CLXXXI. törvény a Schengeni Információs Rendszer második generációja keretében történő információcseréről. <https://net.jogtar.hu/jogszabaly?docid=A1200181.TV>
[^s37]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2004. évi XXIV. törvény a lőfegyverekről és lőszerekről, 2004. 2004. évi XXIV. törvény a lőfegyverekről és lőszerekről. <https://net.jogtar.hu/jogszabaly?docid=A0400024.TV>
[^s38]: Magyar Államkincstár (Hungarian State Treasury) — Központi Költségvetés Végrehajtását Támogató Rendszer…, 2022-11-30. Központi Költségvetés Végrehajtását Támogató Rendszer (KKVTR / IFMIS). <https://www.allamkincstar.gov.hu/nem-lakossagi-ugyek/kozponti-koltsegvetes-vegrehajtasat-tamogato-rendszer-kkvtr--ifmis1> ([archived](https://web.archive.org/web/20260422044324/https://www.allamkincstar.gov.hu/nem-lakossagi-ugyek/kozponti-koltsegvetes-vegrehajtasat-tamogato-rendszer-kkvtr--ifmis1))
[^s39]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2011. évi CXCV. törvény az államháztartásról, 2011. 2011. évi CXCV. törvény az államháztartásról. <https://net.jogtar.hu/jogszabaly?docid=A1100195.TV>
[^s40]: Magyar Nemzeti Bank — Azonnali fizetés. Azonnali fizetés. <https://www.mnb.hu/penzforgalom/azonnalifizetes> ([archived](https://web.archive.org/web/20260718155137/https://www.mnb.hu/penzforgalom/azonnalifizetes))
[^s41]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 346/2010. (XII. 28.) Korm. rendelet a kormányzati célú…, 2010. 346/2010. (XII. 28.) Korm. rendelet a kormányzati célú hálózatokról. <https://net.jogtar.hu/jogszabaly?docid=A1000346.KOR>
[^s42]: Pro-M Professzionális Mobilrádió Zrt. — Vezeték nélküli hálózat – EDR – Pro-M. Vezeték nélküli hálózat – EDR – Pro-M. <https://pro-m.hu/vezetek-nelkuli-halozat-edr/> ([archived](https://web.archive.org/web/20260916150440/https://pro-m.hu/vezetek-nelkuli-halozat-edr/))
[^s43]: BM Országos Katasztrófavédelmi Főigazgatóság — MoLaRi-rendszer. MoLaRi-rendszer. <https://www.katasztrofavedelem.hu/49/molari-rendszer>
[^s44]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2011. évi CXXVIII. törvény a katasztrófavédelemről, 2011. 2011. évi CXXVIII. törvény a katasztrófavédelemről. <https://net.jogtar.hu/jogszabaly?docid=A1100128.TV> ([archived](https://web.archive.org/web/20251202170941/https://net.jogtar.hu/jogszabaly?docid=a1100128.tv))
[^s45]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2011. évi CXC. törvény a nemzeti köznevelésről, 2011. 2011. évi CXC. törvény a nemzeti köznevelésről. <https://net.jogtar.hu/jogszabaly?docid=A1100190.TV> ([archived](https://web.archive.org/web/20260907112557/https://net.jogtar.hu/jogszabaly?docid=a1100190.tv))
[^s46]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2023. évi XC. törvény a harmadik országbeli…, 2023. 2023. évi XC. törvény a harmadik országbeli állampolgárok beutazására és tartózkodására vonatkozó általános szabályokról. <https://net.jogtar.hu/jogszabaly?docid=A2300090.TV> ([archived](https://web.archive.org/web/20260805072340/https://net.jogtar.hu/jogszabaly?docid=a2300090.tv))
[^s47]: Magyarország Kormánya (kormany.hu) — Adatszolgáltatás a közúti közlekedési nyilvántartásból. Adatszolgáltatás a közúti közlekedési nyilvántartásból. <https://kormany.hu/nyilvantartasok/ugyleirasok/adatszolgaltatas-a-kozuti-kozlekedesi-nyilvantartasbol>
[^s48]: Miniszterelnökség / MKIFK Magyar Közlönykiadó és Igazságügyi Fordítóközpont Zrt. — Magyar Közlöny. Magyar Közlöny. <https://magyarkozlony.hu/>
[^s49]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 18/1998. (VI. 3.) NM rendelet a fertőző betegségek és a…, 1998. 18/1998. (VI. 3.) NM rendelet a fertőző betegségek és a járványok megelőzése érdekében szükséges járványügyi intézkedésekről. <https://net.jogtar.hu/jogszabaly?docid=99800018.NM>
[^s50]: Nemzeti Népegészségügyi és Gyógyszerészeti Központ (NNGYK) — Üzemszünetek, 2026. Üzemszünetek. <https://nngyk.gov.hu/hu/szakrendszerek/uzemszunetek.html> ([archived](https://web.archive.org/web/20260906104753/https://nngyk.gov.hu/hu/szakrendszerek/uzemszunetek.html))
[^s51]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2016. évi CLV. törvény a hivatalos statisztikáról, 2016. 2016. évi CLV. törvény a hivatalos statisztikáról. <https://net.jogtar.hu/jogszabaly?docid=A1600155.TV> ([archived](https://web.archive.org/web/20251005015911/https://net.jogtar.hu/jogszabaly?docid=a1600155.tv))
[^s52]: Lechner Tudásközpont — Címregiszter. Címregiszter. <https://lechnerkozpont.hu/oldal/cimregiszter> ([archived](https://web.archive.org/web/20260512221840/https://lechnerkozpont.hu/oldal/cimregiszter))
[^s53]: Lechner Tudásközpont — Bemutatkozás. Bemutatkozás. <https://lechnerkozpont.hu/oldal/bemutatkozas> ([archived](https://web.archive.org/web/20260615083845/https://lechnerkozpont.hu/oldal/bemutatkozas))

**Evidence grades:** 2 Strong, 62 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
