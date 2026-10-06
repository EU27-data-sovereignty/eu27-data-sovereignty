# Greece: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Greece could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2][^s3][^s4] |
| State-controlled national eID | Yes[^s4][^s5] |
| Government data centres | Yes[^s6][^s7][^s8] |
| Government cloud in operation | Yes[^s4][^s9][^s10][^s11] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 29 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Greece described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.367 million[^s12] |
| GDP, current prices | 248.4 EUR bn[^s13] |
| Public administration employment (NACE O) | 400.6 thousand[^s14] |
| Non-household electricity price | 173.8 EUR/MWh[^s15] |
| Renewables share of electricity | 60.9 %[^s16] |
| Land area | 130 048 km²[^s17] |

## 3. Critical data holdings, by priority

The holdings Greece cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 32 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | «Μητρώο Πολιτών» (Citizens' Register): national information system combining the National Municipal Register (Δημοτολόγιο) and civil-status (registry) records[^s18][^s19] | *Not yet sourced* | The law allows hosting of the Citizens' Register to be assigned by joint ministerial decision to the technological infrastructure of another public-sector body (no source found naming the actual host)[^s19] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Facial image and two flat fingerprints collected by the Passports and Security Documents Directorate (Δ.Δ.Ε.Α./Α.Ε.Α.) of Hellenic Police HQ and stored on the passport chip[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Encrypted fingerprint images kept in the Central Database of the Passports Directorate, accessible only to authorised police staff[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: Art. 115 of Law 4483/2017 (both the PDF and lawspot) says the Citizens' Register comprises the civil-status acts (ληξιαρχικές πράξεις) of Greek citizens and foreigners with events in Greece, held in the Ministry of the Interior's Registry…. It is withheld until the fact or its source is corrected and checked again* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | GRNET keeps for 12 months a history of actions taken in the Gov.gr Wallet document-presentation process[^s21] | GRNET (Ε.Δ.Υ.Τ.Ε. Α.Ε.), company of the Greek State, is the designated processor[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Web services supplying public bodies with data on issued Greek passports, via the Interoperability Centre[^s20] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Electoral rolls kept at the Ministry of the Interior, compiled from municipal registers (δημοτολόγια)[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | ΑΠΕΔ issues and manages certificates for trust services to all public-sector bodies[^s4][^s23] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Criminal record consists of record slips, subject to use of the computerised system[^s24][^s25] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | Gov.gr Wallet requires the personal TaxisNet credentials (or web-banking credentials) plus a verified mobile number[^s26] | Ministry of Digital Governance is the controller for the authentication services of gov.gr[^s4][^s23] | GRNET (Ε.Δ.Υ.Τ.Ε. Α.Ε.), a Greek state-owned company, is the processor that designs, implements and maintains the Gov.gr Wallet application[^s21] | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The quote is on the page and says GRNET, a Greek State company, designs, implements and maintains the application on behalf of the Ministry; but the page says nothing about where the infrastructure runs (no hosting, server or data-centre…. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | Residence and migration status (tier 1) | Migration Information Systems and the Register of Aliens (Μητρώο Αλλοδαπών), centrally operated by the Ministry of Migration and Asylum[^s27] | *Not yet sourced* | Migration and asylum data centres (holding biometric data) are in ministry/agency premises; consolidation into a Tier-4 data centre at the Ministry of Migration's Kerani building was planned[^s6] | *Not stated in sources* | *Not yet sourced* |
| High | Benefits & pensions (tier 1) | ATLAS: digital pension award system of e-EFKA, whose database holds insurance-period data digitised from former IKA archives[^s28] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Statutory health insurance (tier 1) | Electronic prescription system installed and operated at ΗΔΥΚΑ (IDIKA) for the social-insurance funds[^s29] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Cadastre Information System (ΣΠΕΚ), into which legacy mortgage-registry archives are being digitised[^s30] | Hellenic Cadastre (Ελληνικό Κτηματολόγιο), public-law entity supervised by the Minister of Environment and Energy[^s31][^s32] | Hellenic Cadastre operates its own Data Center and Disaster Recovery Center (upgrade planned)[^s33] | National infrastructure[^s33] | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | Central Register of Beneficial Owners, created at the General Secretariat for Information Systems and linked to each legal entity's tax number (ΑΦΜ)[^s34][^s35][^s36] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Driving licences and police ID cards are drawn into the Gov.gr Wallet from the respective registers in which they are held[^s21] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Central information system of the Hellenic Police with its files and databases, protected by the Police IT Directorate[^s37][^s38] | *Not yet sourced* | The Hellenic Police IT Directorate designs the computerised information systems and creates and supports their technical infrastructure[^s38] | National infrastructure[^s38] | *Not yet measured* |
| High | Border and visa systems (tier 1) | πληροφοριακό σύστημα της εθνικής αρχής στο πλαίσιο της σύμβασης SCHENGEN (information system of the national authority under the Schengen Convention)[^s37] | Hellenic Police handles requests submitted through the national SIRENE bureau[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | ηλεκτρονικό αρχείο πυροβόλων όπλων (electronic firearms file)[^s39] | Διεύθυνση Κρατικής Ασφάλειας του Αρχηγείου Ελληνικής Αστυνομίας (State Security Directorate, Hellenic Police Headquarters)[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Integrated Information System for Fiscal Policy (ΟΠΣΔΠ), to evolve into a central Government ERP[^s40] | *Not yet sourced* | G-Cloud project plans infrastructure for systems hosted in the data centre and disaster site of the Ministry of Finance and AADE[^s9] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Central Human Resources Management System for the Greek public administration, from appointment to retirement[^s41] | Payroll rules to be applied centrally by the Single Payment Authority (Ενιαία Αρχή Πληρωμής, ΕΑΠ)[^s42] | *Not yet sourced* | *Not stated in sources* | At least 680,000 paid staff in 3,500 wider-public-sector bodies[^s42] |
| High | Election management and results (tier 1) | Courts of first instance compile detailed preference-vote results and send them in print or electronically to the Ministry of the Interior[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | EMS (Energy Management System)[^s43][^s44] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | MySchool[^s45] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Tax (tier 1) | Integrated Tax Information System of AADE: TAXIS - TAXISnet - Elenxis[^s46] | *Not yet sourced* | *Not yet sourced* | National infrastructure[^s47] | *Not yet measured* |
| Standard | Customs declarations (tier 1) | ICISnet — integrated customs information system of AADE[^s48] | *Not yet sourced* | ICISnet is hosted on ΓΓΠΣΔΔ infrastructure[^s49] | National infrastructure[^s49] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Government Gazette (Εφημερίδα της Κυβερνήσεως, ΦΕΚ): printed and electronic edition and citizens' access to published texts[^s50] | National Printing Office (Εθνικό Τυπογραφείο), a public service under the Presidency of the Government, publishes the Government Gazette (ΦΕΚ) in print and electronically[^s50] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Health records (tier 2) | National Electronic Health Record (ΕΗΦΥ): a central point for storing and managing medical data[^s51] | *Not yet sourced* | *Not yet sourced* | National infrastructure[^s52] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | EODY core functions include epidemiological surveillance and provision of epidemiological data[^s53] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | Digitisation of all physical holdings of the General State Archives (ΓΑΚ) and migration of data from related information systems[^s54] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 32 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 6 |
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

> Not yet sized. Capacity for Greece will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Greece without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Business registry (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
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

### The verdict on each fact about Greece

60 of 60 printed facts about Greece pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:EL:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EL:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EL:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EL:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:EL:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EL:population_m | param:EL:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:EL:gdp_eur_bn | param:EL:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EL:gov_employment_k | param:EL:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EL:elec_price_eur_mwh | param:EL:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EL:renewables_pct | param:EL:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:EL:land_km2 | param:EL:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:civil_registry:hosting | Civil registry core: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:EL:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:authentication_audit_log:operator | Authentication audit log: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:digital_identity_credentials:hosting | Digital identity credentials: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:EL:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:residence_permits:hosting | Residence and migration status: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:EL:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:land_property:hosting | Land & property registry: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:EL:land_property:foreign_dependency | Land & property registry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:police_records:hosting | Police information systems: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:EL:police_records:foreign_dependency | Police information systems: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:public_finance:hosting | Treasury and state accounts: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:EL:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:government_payroll:operator | Government payroll and personnel: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:government_payroll:count | Government payroll and personnel: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:tax:foreign_dependency | Tax: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:customs:hosting | Customs declarations: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:EL:customs:foreign_dependency | Customs declarations: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:health_records:foreign_dependency | Health records: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:EL:national_archives:register | National archives (digital): the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Greece

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:EL:breeder_documents:register | Breeder document scans: the name of the register or system | claude-fable-5-1 | not supported | Art. 115 of Law 4483/2017 (both the PDF and lawspot) says the Citizens' Register comprises the civil-status acts (ληξιαρχικές πράξεις) of Greek citizens and foreigners with events in Greece, held in the Ministry of the Interior's Registry Acts Management system, which matches the rest of the sentence; but the parenthetical '(births, marriages, deaths)' appears in neither cited source (searched bot |
| record:EL:digital_identity_credentials:foreign_dependency | Digital identity credentials: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | unclear | The quote is on the page and says GRNET, a Greek State company, designs, implements and maintains the application on behalf of the Ministry; but the page says nothing about where the infrastructure runs (no hosting, server or data-centre statement anywhere on it). A national operator is not the same as a national hosting location, so the source is ambiguous for this categorical label. |

---

[^s1]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 1 – Purpose and scope, 2020-09-23. Law 4727/2020, Article 1 – Purpose and scope. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-1-nomos-4727-2020-skopos-kai-pedio-efarmogis-toy/>
[^s2]: Υπουργείο Ψηφιακής Διακυβέρνησης — Αρχή Πιστοποίησης του Ελληνικού Δημοσίου – Αρχική. Αρχή Πιστοποίησης του Ελληνικού Δημοσίου – Αρχική. <https://aped.gov.gr/> ([archived](https://web.archive.org/web/20260922185215/https://aped.gov.gr/))
[^s3]: Αρχή Πιστοποίησης του Ελληνικού Δημοσίου (ΑΠΕΔ) – Υπουργείο Ψηφιακής Διακυβέρνησης — Σχετικά με την ΑΠΕΔ. Σχετικά με την ΑΠΕΔ. <https://aped.gov.gr/about-aped/> ([archived](https://web.archive.org/web/20260413053433/https://aped.gov.gr/about-aped/))
[^s4]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4727/2020 Ψηφιακή Διακυβέρνηση (ΦΕΚ Α'…, 2020-09-23. Νόμος 4727/2020 Ψηφιακή Διακυβέρνηση (ΦΕΚ Α' 184/23.09.2020), άρθρο 87. <https://api.et.gr/apiLAW/1/2020/4727/pdf>
[^s5]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 25 – Identification for the…, 2020-09-23. Law 4727/2020, Article 25 – Identification for the issuance of credentials. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-25-nomos-4727-2020-taytopoiisi-gia-tin-ekdosi/>
[^s6]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κέντρο Δεδομένων υψηλής διαθεσιμότητας (Tier-4 Datacenter), 2023-12-01. Κέντρο Δεδομένων υψηλής διαθεσιμότητας (Tier-4 Datacenter). <https://digitalstrategy.gov.gr/project/tier-4_datacenter> ([archived](https://web.archive.org/web/20260125084953/https://digitalstrategy.gov.gr/project/tier-4_datacenter))
[^s7]: GRNET (Εθνικό Δίκτυο Υποδομών Τεχνολογίας και Έρευνας, ΕΔΥΤΕ Α.Ε.) — GRNET Datacenters. GRNET Datacenters. <https://grnet.gr/en/infrastructures/grnet-datacenters/> ([archived](https://web.archive.org/web/20260920044608/https://grnet.gr/en/infrastructures/grnet-datacenters/))
[^s8]: Κοινωνία της Πληροφορίας Μ.Α.Ε. — Παροχή Νεφο-Υπολογιστικών Υποδομών και υπηρεσιών (Cloud…, 2022-09-06. Παροχή Νεφο-Υπολογιστικών Υποδομών και υπηρεσιών (Cloud Services). <https://www.ktpae.gr/erga/parochi-nefo-ypologistikon-ypodomon-kai-ypiresion-cloud-services/>
[^s9]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ενίσχυση των κεντρικών υποδομών Κυβερνητικού Νέφους (G-…, 2023-12-01. Ενίσχυση των κεντρικών υποδομών Κυβερνητικού Νέφους (G- Cloud) της Γ.Γ.Π.Σ.Δ.Δ.. <https://digitalstrategy.gov.gr/project/g-cloud> ([archived](https://web.archive.org/web/20260413104922/https://digitalstrategy.gov.gr/project/g-cloud))
[^s10]: Κοινωνία της Πληροφορίας Μ.Α.Ε. — Government Cloud / G-Cloud, 2020-01-12. Government Cloud / G-Cloud. <https://www.ktpae.gr/erga/government-cloud-g-cloud/> ([archived](https://web.archive.org/web/20260829044912/https://www.ktpae.gr/erga/government-cloud-g-cloud/))
[^s11]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 87 – Government clouds, 2020-09-23. Law 4727/2020, Article 87 – Government clouds. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-87-nomos-4727-2020-kyvernitika-nefi/>
[^s12]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s13]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s14]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s15]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s16]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s17]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s18]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4483/2017, άρθρο 115 (Δημιουργία Μητρώου Πολιτών), 2017-07-31. Νόμος 4483/2017, άρθρο 115 (Δημιουργία Μητρώου Πολιτών). <https://api.et.gr/apiLAW/1/2017/4483/pdf>
[^s19]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4483/2017 (ΦΕΚ Α΄ 107/2017), 2017-07-31. Νόμος 4483/2017 (ΦΕΚ Α΄ 107/2017). <https://www.lawspot.gr/nomothesia/nomos-4483-2017/>
[^s20]: Ελληνική Αστυνομία - Διεύθυνση Διαβατηρίων και Εγγράφων Ασφαλείας — Προστασία Προσωπικών Δεδομένων - Διεύθυνση Διαβατηρίων &…, 2025-12-31. Προστασία Προσωπικών Δεδομένων - Διεύθυνση Διαβατηρίων & Εγγράφων Ασφαλείας. <https://www.passport.gov.gr/npc/data.html> ([archived](https://web.archive.org/web/20260902152156/https://www.passport.gov.gr/npc/data.html))
[^s21]: Υπουργείο Ψηφιακής Διακυβέρνησης — Gov.gr Wallet - Πολιτική Απορρήτου. Gov.gr Wallet - Πολιτική Απορρήτου. <https://wallet.gov.gr/privacy/> ([archived](https://web.archive.org/web/20260513043821/https://wallet.gov.gr/privacy/))
[^s22]: Lawspot (reproduction of the Government Gazette text) — Προεδρικό Διάταγμα 26/2012 (κωδικοποίηση εκλογικής…, 2012-03-14. Προεδρικό Διάταγμα 26/2012 (κωδικοποίηση εκλογικής νομοθεσίας). <https://www.lawspot.gr/nomothesia/proedriko-diatagma-26-2012/>
[^s23]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4727/2020 (ΦΕΚ Α΄ 184/2020), 2020-09-23. Νόμος 4727/2020 (ΦΕΚ Α΄ 184/2020). <https://www.lawspot.gr/nomothesia/nomos-4727-2020/> ([archived](https://web.archive.org/web/20260309090533/https://www.lawspot.gr/nomothesia/nomos-4727-2020/))
[^s24]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4620/2019 Κώδικας Ποινικής Δικονομίας, άρθρο 569, 2019-06-11. Νόμος 4620/2019 Κώδικας Ποινικής Δικονομίας, άρθρο 569. <https://api.et.gr/apiLAW/1/2019/4620/pdf>
[^s25]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4620/2019 - Κώδικας Ποινικής Δικονομίας, 2019-06-11. Νόμος 4620/2019 - Κώδικας Ποινικής Δικονομίας. <https://www.lawspot.gr/nomothesia/nomos-4620-2019/> ([archived](https://web.archive.org/web/20260308031021/https://www.lawspot.gr/nomothesia/nomos-4620-2019/))
[^s26]: Υπουργείο Ψηφιακής Διακυβέρνησης — Gov.gr Wallet. Gov.gr Wallet. <https://wallet.gov.gr/> ([archived](https://web.archive.org/web/20260905163745/https://wallet.gov.gr/))
[^s27]: Υπουργείο Μετανάστευσης και Ασύλου — Διοίκηση - Υπουργείο Μετανάστευσης και Ασύλου. Διοίκηση - Υπουργείο Μετανάστευσης και Ασύλου. <https://migration.gov.gr/migration-policy/dioikisi/> ([archived](https://web.archive.org/web/20260923144946/https://migration.gov.gr/migration-policy/dioikisi/))
[^s28]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση Ασφαλιστικής Ιστορίας e-ΕΦΚΑ, 2023-12-01. Ψηφιοποίηση Ασφαλιστικής Ιστορίας e-ΕΦΚΑ. <https://digitalstrategy.gov.gr/project/psifiopoiisi_asfalistikis_istorias_e-efka> ([archived](https://web.archive.org/web/20250918090757/https://digitalstrategy.gov.gr/project/psifiopoiisi_asfalistikis_istorias_e-efka))
[^s29]: Η.Δ.Υ.Κ.Α. Μ.Α.Ε. (IDIKA) — Ηλεκτρονική Συνταγογράφηση. Ηλεκτρονική Συνταγογράφηση. <https://www.idika.gr/erga/ilektroniki-syntagografisi/> ([archived](https://web.archive.org/web/20260903145627/https://www.idika.gr/erga/ilektroniki-syntagografisi/))
[^s30]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση Αρχείου Υποθηκοφυλακείων για το Εθνικό…, 2023-12-01. Ψηφιοποίηση Αρχείου Υποθηκοφυλακείων για το Εθνικό Κτηματολόγιο. <https://digitalstrategy.gov.gr/project/psifiopoiisi_archeioy_ypothikofylakeion_gia_to_ethniko_ktimatologio> ([archived](https://web.archive.org/web/20250613012620/https://digitalstrategy.gov.gr/project/psifiopoiisi_archeioy_ypothikofylakeion_gia_to_ethniko_ktimatologio))
[^s31]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4512/2018, άρθρο 1, 2018-01-17. Νόμος 4512/2018, άρθρο 1. <https://api.et.gr/apiLAW/1/2018/4512/pdf>
[^s32]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4512/2018, 2018-01-16. Νόμος 4512/2018. <https://www.lawspot.gr/nomothesia/nomos-4512-2018/>
[^s33]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Αναβάθμιση εξοπλισμού Κέντρου Δεδομένων (Data Center)…, 2023-12-01. Αναβάθμιση εξοπλισμού Κέντρου Δεδομένων (Data Center) και Εφεδρικού Κέντρου Δεδομένων Κτηματολογίου. <https://digitalstrategy.gov.gr/project/anavathmisi_exoplismoy_ktimatologioy_gia_leitoyrgia_se_eikoniko_perivallon_virtualization> ([archived](https://web.archive.org/web/20251119054015/https://digitalstrategy.gov.gr/project/anavathmisi_exoplismoy_ktimatologioy_gia_leitoyrgia_se_eikoniko_perivallon_virtualization))
[^s34]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4557/2018, άρθρο 20 παρ. 4, 2018-07-30. Νόμος 4557/2018, άρθρο 20 παρ. 4. <https://api.et.gr/apiLAW/1/2018/4557/pdf>
[^s35]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4557/2018, 2018-07-30. Νόμος 4557/2018. <https://www.lawspot.gr/nomothesia/nomos-4557-2018/>
[^s36]: Εθνικό Μητρώο Διοικητικών Διαδικασιών (ΜΙΤΟΣ), Υπουργείο Εσωτερικών — Κεντρικό Μητρώο Πραγματικών Δικαιούχων - Εθνικό Μητρώο…, 2026-09-29. Κεντρικό Μητρώο Πραγματικών Δικαιούχων - Εθνικό Μητρώο Διοικητικών Διαδικασιών. <https://mitos.gov.gr/index.php/%CE%94%CE%94:%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CF%8C_%CE%9C%CE%B7%CF%84%CF%81%CF%8E%CE%BF_%CE%A0%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8E%CE%BD_%CE%94%CE%B9%CE%BA%CE%B1%CE%B9%CE%BF%CF%8D%CF%87%CF%89%CE%BD> ([archived](https://web.archive.org/web/20260418223455/https://mitos.gov.gr/index.php/%CE%94%CE%94:%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CF%8C_%CE%9C%CE%B7%CF%84%CF%81%CF%8E%CE%BF_%CE%A0%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8E%CE%BD_%CE%94%CE%B9%CE%BA%CE%B1%CE%B9%CE%BF%CF%8D%CF%87%CF%89%CE%BD))
[^s37]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4249/2014 (Αναδιοργάνωση της Ελληνικής…, 2014-03. Νόμος 4249/2014 (Αναδιοργάνωση της Ελληνικής Αστυνομίας), Διεύθυνση Πληροφορικής. <https://api.et.gr/apiLAW/1/2014/4249/pdf>
[^s38]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4249/2014, 2014-03-23. Νόμος 4249/2014. <https://www.lawspot.gr/nomothesia/nomos-4249-2014/>
[^s39]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4678/2020 (τροποποίηση ν. 2168/1993, ενσωμάτωση…, 2020-03-20. Νόμος 4678/2020 (τροποποίηση ν. 2168/1993, ενσωμάτωση Οδηγίας (ΕΕ) 2017/853), άρθρο 28 παρ. 4 ν. 2168/1993. <https://api.et.gr/apiLAW/1/2020/4678/pdf>
[^s40]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κεντρικό και Ενιαίο Σύστημα Δημοσιονομικής Πολιτικής…, 2023-12-01. Κεντρικό και Ενιαίο Σύστημα Δημοσιονομικής Πολιτικής (Government ERP). <https://digitalstrategy.gov.gr/project/government_erp> ([archived](https://web.archive.org/web/20260413112148/https://digitalstrategy.gov.gr/project/government_erp))
[^s41]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κεντρικό Σύστημα Διαχείρισης Ανθρώπινου Δυναμικού, 2023-12-01. Κεντρικό Σύστημα Διαχείρισης Ανθρώπινου Δυναμικού. <https://digitalstrategy.gov.gr/project/kentriko_systima_diacheirisis_anthropinoy_dynamikoy> ([archived](https://web.archive.org/web/20260413104530/https://digitalstrategy.gov.gr/project/kentriko_systima_diacheirisis_anthropinoy_dynamikoy))
[^s42]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Μισθοδοσία, 2023-12-01. Μισθοδοσία. <https://digitalstrategy.gov.gr/project/misthodosia> ([archived](https://web.archive.org/web/20260413121425/https://digitalstrategy.gov.gr/project/misthodosia))
[^s43]: IPTO (ΑΔΜΗΕ) — Event at the National Control Center in Kryoneri, 2019-12. Event at the National Control Center in Kryoneri. <https://www.admie.gr/en/nea/ekdiloseis/egkainia-psifiakoy-kentroy-eleghoy-sto-kryoneri>
[^s44]: ΑΔΜΗΕ (IPTO, Independent Power Transmission Operator) — ΜΕΤΑΓΩΓΗ ΣΥΣΤΗΜΑΤΟΣ EMS, 2017-05-30. ΜΕΤΑΓΩΓΗ ΣΥΣΤΗΜΑΤΟΣ EMS. <https://www.admie.gr/anakoinoseis/enimerosi/metagogi-systimatos-ems>
[^s45]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού) — Ψηφιακές Υπηρεσίες MySchool, 2023-12-01. Ψηφιακές Υπηρεσίες MySchool. <https://digitalstrategy.gov.gr/project/myschool> ([archived](https://web.archive.org/web/20240416211029/https://digitalstrategy.gov.gr/project/myschool))
[^s46]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού…, 2023-12-01. Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού Συστήματος Φορολογίας της ΑΑΔΕ. <https://digitalstrategy.gov.gr/project/anaptyxi_neoy_enopoiimenoy_olokliromenoy_pliroforiakoy_systimatos_forologias_tis_aade>
[^s47]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4389/2016, 2016-05-27. Νόμος 4389/2016. <https://www.lawspot.gr/nomothesia/nomos-4389-2016/>
[^s48]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού…, 2023-12-01. Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού Συστήματος Τελωνείων της ΑΑΔΕ (ICISnet). <https://digitalstrategy.gov.gr/project/icisnet>
[^s49]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Αναβάθμιση διαθεσιμότητας, εφεδρείας, ασφάλειας…, 2023-12-01. Αναβάθμιση διαθεσιμότητας, εφεδρείας, ασφάλειας δεδομένων, που φιλοξενούνται στις υποδομές της ΓΓΠΣΔΔ. <https://digitalstrategy.gov.gr/project/anavathmisi_diathesimotitas_efedreias_asfaleias_dedomenon_poy_filoxenoyntai_stis_ypodomes_tis_ggpsdd> ([archived](https://web.archive.org/web/20260514161810/https://digitalstrategy.gov.gr/project/anavathmisi_diathesimotitas_efedreias_asfaleias_dedomenon_poy_filoxenoyntai_stis_ypodomes_tis_ggpsdd))
[^s50]: Εθνικό Τυπογραφείο — Αποστολή - Εθνικό Τυπογραφείο. Αποστολή - Εθνικό Τυπογραφείο. <https://et.gr/yphresia/mission/> ([archived](https://web.archive.org/web/20260514100450/https://et.gr/yphresia/mission/))
[^s51]: Υπουργείο Υγείας — Εθνικός Ηλεκτρονικός Φάκελος Υγείας. Εθνικός Ηλεκτρονικός Φάκελος Υγείας. <https://www.ehealthrecord.gov.gr/ehfy-overview-details>
[^s52]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Σύστημα Διακυβέρνησης Δεδομένων για τον Τομέα της Υγείας, 2023-12-01. Σύστημα Διακυβέρνησης Δεδομένων για τον Τομέα της Υγείας. <https://digitalstrategy.gov.gr/project/systima_diakyvernisis_dedomenon_gia_ton_tomea_tis_ygeias> ([archived](https://web.archive.org/web/20260413103817/https://digitalstrategy.gov.gr/project/systima_diakyvernisis_dedomenon_gia_ton_tomea_tis_ygeias))
[^s53]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4633/2019, 2019-10-16. Νόμος 4633/2019. <https://www.lawspot.gr/nomothesia/nomos-4633-2019/> ([archived](https://web.archive.org/web/20260121092729/https://www.lawspot.gr/nomothesia/nomos-4633-2019/))
[^s54]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση των Γενικών Αρχείων του Κράτους, 2023-12-01. Ψηφιοποίηση των Γενικών Αρχείων του Κράτους. <https://digitalstrategy.gov.gr/project/psifiopoiisi_ton_genikon_archeion_toy_kratoys> ([archived](https://web.archive.org/web/20260413121410/https://digitalstrategy.gov.gr/project/psifiopoiisi_ton_genikon_archeion_toy_kratoys))

**Evidence grades:** 4 Strong, 56 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
