# Denmark: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Medium. With the evidence still open, Denmark could be anywhere from 'Not demonstrated' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1] |
| Classification in law | Partly[^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4][^s5] |
| State-controlled national eID | Partly[^s6] |
| Government data centres | Yes[^s7][^s8][^s9] |
| Government cloud in operation | Yes[^s10][^s8] |

What could move this placement:

- If any of the 30 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Denmark described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 6.026 million[^s11] |
| GDP, current prices | 417.8 EUR bn[^s12] |
| Public administration employment (NACE O) | 169.8 thousand[^s13] |
| Non-household electricity price | 121.6 EUR/MWh[^s14] |
| Renewables share of electricity | 77.7 %[^s15] |
| Land area | 41 987 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Denmark cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 28 of 39 holding classes have a verified source; 4 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Det Centrale Personregister (CPR) - the Central Person Register[^s17] | CPR-administrationen (CPR Office), placed in the department of the Ministry of Research, Education and Digitalisation[^s18][^s17] | *Not yet sourced* | *Not stated in sources* | About 11.4 million persons, of which just under 6.1 million living persons[^s19] |
| Critical | Facial biometric (tier 0) | Immigration authorities' biometric register (facial photos and fingerprints of foreign nationals for residence cards); retained 20 years (10 years for visa cases)[^s20] | Ministry of Immigration and Integration, Udlændingestyrelsen and SIRI[^s20][^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Immigration authorities' biometric register (fingerprints and facial photos of foreign nationals, captured for residence cards and identity control)[^s20] | Ministry of Immigration and Integration, Danish Immigration Service (Udlændingestyrelsen) and SIRI are responsible for the register[^s20][^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Kirkeministeriet's common systems for personregistrering (church registration of births, names and deaths), used by parish registrars[^s22] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | NemLog-in - the joint public digital login infrastructure through which authentications to public self-service solutions pass[^s23][^s24] | Digitaliseringsstyrelsen; NemLog-in described as a society-critical part of public digital infrastructure[^s25][^s26] | *Not yet sourced* | *Not stated in sources* | On average around 35 million logins per month through NemLog-in[^s27] |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | Den Danske Stat Tillidstjenester (CA1) - Danish State trust services, delivered by Digitaliseringsstyrelsen on behalf of the Danish State[^s3] | Digitaliseringsstyrelsen; CA1 is a qualified trust service provider under eIDAS on the EU trusted list[^s3] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | Politiets Efterretningstjeneste (PET) - domestic security intelligence; may collect information relevant to its activities[^s28] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Det Centrale Pasregister (Pasregistret) - Central Passport Register, with Rigspolitiet (Danish National Police) as data controller[^s29][^s30] | Rigspolitiet; retention: deleted two years after passport expiry or holder's death[^s29] | *Not yet sourced* | National infrastructure[^s1] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Information systems in the immigration field incl. Udlændinge Informations Systemet (UIS), used for data exchange between authorities (formerly UIP portal)[^s31] | Udlændingestyrelsen (Danish Immigration Service) receives and processes asylum and other residence permit applications[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | DMS (Declaration Management System) - customs system for import, export and transit declarations[^s33] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | sundhedskort and sikringsgruppe enrolment based on Det Centrale Personregister (CPR) (health insurance card and coverage group registration)[^s34] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | Beneficial ownership data held in CVR: legal persons and trusts obliged to register beneficial owners must be registered in CVR[^s35] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Disputed: the fact check (claude-opus-5-5, run wf_8232a23d-013) was confirmed once, but a second checker in a stability sample did not confirm this: The quote and § 1(2) are on the page; § 1(2) says the register holds data on each vehicle and who it belongs to ('tilhørsforhold'). But the printed text calls the register 'DMR', and that name or abbreviation does not appear anywhere on…. It is withheld until the fact or its source is corrected and checked again* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Det Centrale Kriminalregister (Kriminalregistret) - Central Criminal Register[^s29][^s36] | Rigspolitiet is data controller; regulated by the kriminalregisterbekendtgørelse[^s29] | *Not yet sourced* | National infrastructure[^s1] | *Not yet measured* |
| High | Police information systems (tier 1) | POLSAS - the police case management system[^s29][^s1] | *Not yet sourced* | *Not yet sourced* | National infrastructure[^s1] | *Not yet measured* |
| High | Border and visa systems (tier 1) | Schengeninformationssystemet (SIS, Schengen Information System)[^s37] | Udlændingestyrelsen (Danish Immigration Service), for SIS return alerts[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Politiets Våbenregister (Police Firearms Register), Rigspolitiet data controller[^s29][^s38] | Rigspolitiet (data controller); police may also use the register for investigation and supervision of permits[^s29][^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Statens Bevillings- og Regnskabsløsning (SBRL) - state appropriation and accounts solution supporting Finance Act and state accounts from FY2025[^s39] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Statens Lønløsning (the State Payroll Solution)[^s40] | Økonomistyrelsen (Agency for Public Finance and Management)[^s41] | *Not yet sourced* | *Not stated in sources* | ca. 180.000 statslige ansatte (state employees paid each month)[^s40] |
| High | Election management and results (tier 1) | Election results system: municipalities enter manually counted vote totals into an IT system developed by KMD; Danmarks Statistik compiles results[^s42] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET DKK - Nationalbanken's payment system for krone settlement (via T2 and TIPS on TARGET Services, plus SPI for monetary-policy instruments and collateral)[^s43][^s44] | *Not yet sourced* | At Easter 2025 Nationalbanken moved krone settlement from its own system Kronos2 to the pan-European TARGET Services platform[^s44] | EU provider[^s43][^s44] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | SINE (Sikkerhedsnettet) - Denmark's radio network for emergency communications; use mandatory under beredskabsloven § 29[^s45] | Center for Beredskabskommunikation (CFB), part of the Ministry of Civil Security and Emergency Preparedness; network operation by Dansk Beredskabskommunikation A/S[^s46][^s47] | SINE network operation is supplied by Dansk Beredskabskommunikation A/S (ownership not stated in this source)[^s45] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Sirenevarslingssystemet (the national siren warning system)[^s48] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Energinet carries out system-responsibility (TSO) activities, electricity transmission and gas transmission[^s49] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | STADS (the university student administration system)[^s50] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | Omkring 100.000 studerende (students)[^s50] |
| High | Health records (tier 2) | Fælles Medicinkort (FMK) - Sundhedsdatastyrelsen's electronic register of every citizen's medication data (prescription, purchase, dispensing, dose changes)[^s51][^s52] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Det Danske Vaccinationsregister - national register of citizens' vaccinations, run by Statens Serum Institut[^s51] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Danmarks Adresseregister (DAR) - authoritative register of road names and addresses[^s53] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 28 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 3 |
| EU provider | 1 |
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

> Not yet sized. Capacity for Denmark will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 4 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Denmark without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Electoral roll entry (tier 0)
- Tax (tier 1)
- Benefits & pensions (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Official gazette and legislation (tier 1)
- Defence command and logistics (tier 1)
- Water management control (tier 1)

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

### The verdict on each fact about Denmark

61 of 61 printed facts about Denmark pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:DK:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:DK:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:DK:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:DK:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:DK:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:DK:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:DK:population_m | param:DK:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:DK:gdp_eur_bn | param:DK:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:DK:gov_employment_k | param:DK:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:DK:elec_price_eur_mwh | param:DK:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:DK:renewables_pct | param:DK:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:DK:land_km2 | param:DK:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:civil_registry:count | Civil registry core: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:fingerprint_biometric:operator | Fingerprint biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:authentication_audit_log:operator | Authentication audit log: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:authentication_audit_log:count | Authentication audit log: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:intelligence:register | Intelligence services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:issuance_history:foreign_dependency | Document issuance history: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:judicial_criminal:foreign_dependency | Judicial & criminal justice: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:police_records:foreign_dependency | Police information systems: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:government_payroll:operator | Government payroll and personnel: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:government_payroll:count | Government payroll and personnel: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:central_bank:hosting | Central bank systems: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:DK:central_bank:foreign_dependency | Central bank systems: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:DK:emergency_communications:hosting | Emergency calls and public-safety radio: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:DK:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:education:count | Education: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:DK:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Denmark

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:DK:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | claude-opus-5-5 | not supported | The quote and § 1(2) are on the page; § 1(2) says the register holds data on each vehicle and who it belongs to ('tilhørsforhold'). But the printed text calls the register 'DMR', and that name or abbreviation does not appear anywhere on the page. |

---

[^s1]: Retsinformation / Justitsministeriet — Bekendtgørelse om hel eller delvis opbevaring her i…, 2025-03-20. Bekendtgørelse om hel eller delvis opbevaring her i landet af personoplysninger (Lokationskravsbekendtgørelsen, BEK nr 291 af 20/03/2025). <https://www.retsinformation.dk/eli/lta/2025/291/xml>
[^s2]: Statsministeriet / Retsinformation — Cirkulære om sikkerhedsbeskyttelse af informationer af…, 2014-12-17. Cirkulære om sikkerhedsbeskyttelse af informationer af fælles interesse for landene i NATO eller EU, andre klassificerede informationer samt informationer af sikkerhedsmæssig beskyttelsesinteresse i øvrigt (Sikkerhedscirkulæret), CIR nr. 10338 af 17/12/2014. <https://www.retsinformation.dk/eli/retsinfo/2014/10338/xml>
[^s3]: Digitaliseringsstyrelsen / Den Danske Stat Tillidstjenester — Forside - Den Danske Stat Tillidstjenester. Forside - Den Danske Stat Tillidstjenester. <https://www.ca1.gov.dk/> ([archived](https://web.archive.org/web/20260608195922/https://www.ca1.gov.dk/))
[^s4]: Digitaliseringsstyrelsen — Tilsynsorgan for Danske tillidstjenester. Tilsynsorgan for Danske tillidstjenester. <https://certifikat.gov.dk/> ([archived](https://web.archive.org/web/20251210103253/https://certifikat.gov.dk/))
[^s5]: Digitaliseringsstyrelsen (Den Danske Stat Tillidstjenester) — Den Danske Stat Tillidstjenester - Vilkår for…. Den Danske Stat Tillidstjenester - Vilkår for kvalificerede personsignaturer 1.2. <https://cms.nemlog-in.dk/media/jqebfp5j/vilka-r-kvalificerede-personsignaturer-1-2.pdf> ([archived](https://web.archive.org/web/20240630032003/https://cms.nemlog-in.dk/media/jqebfp5j/vilka-r-kvalificerede-personsignaturer-1-2.pdf))
[^s6]: Digitaliseringsstyrelsen — Om MitID. Om MitID. <https://digst.dk/it-loesninger/mitid/om-mitid/> ([archived](https://web.archive.org/web/20260417215119/https://digst.dk/it-loesninger/mitid/om-mitid/))
[^s7]: Statens It — Om GovCloud. Om GovCloud. <https://govcloud.dk/om-govcloud/> ([archived](https://web.archive.org/web/20260121215411/https://govcloud.dk/om-govcloud/))
[^s8]: Statens It (Agency for Governmental IT Services, Ministry of Finance) — Statens It Årsrapport 2025, 2026. Statens It Årsrapport 2025. <https://statens-it.dk/media/0iwny3lc/statens-it-aaarsrapport-2025.pdf> ([archived](https://web.archive.org/web/20260904155709/https://statens-it.dk/media/0iwny3lc/statens-it-aaarsrapport-2025.pdf))
[^s9]: Statens It — Om Statens It. Om Statens It. <https://statens-it.dk/om-os/om-statens-it/>
[^s10]: Statens It — GovCloud fra Statens It. GovCloud fra Statens It. <https://govcloud.dk/> ([archived](https://web.archive.org/web/20260520192843/https://govcloud.dk/))
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Retsinformation / Forsknings-, Uddannelses- og Digitaliseringsministeriet — Bekendtgørelse af lov om Det Centrale Personregister…, 2023-06-23. Bekendtgørelse af lov om Det Centrale Personregister (LBK nr 1010 af 23/06/2023). <https://www.retsinformation.dk/eli/lta/2023/1010/xml>
[^s18]: CPR-kontoret — Om CPR-kontoret. Om CPR-kontoret. <https://www.cpr.dk/om-cpr-kontoret> ([archived](https://web.archive.org/web/20260517144602/https://www.cpr.dk/om-cpr-kontoret))
[^s19]: CPR-kontoret — CPR-kontoret (forside). CPR-kontoret (forside). <https://www.cpr.dk/> ([archived](https://web.archive.org/web/20260831062401/https://www.cpr.dk/))
[^s20]: Udlændingestyrelsen / SIRI (nyidanmark.dk) — Biometri – Opbevaring af fingeraftryk og ansigtsfoto. Biometri – Opbevaring af fingeraftryk og ansigtsfoto. <https://www.nyidanmark.dk/da/Ord-og-begreber/F%C3%A6lles/Biometri---Opbevaring-af-fingeraftryk-og-ansigtsfoto>
[^s21]: Retsinformation / Udlændinge- og Integrationsministeriet — Bekendtgørelse af udlændingeloven (LBK nr 1183 af…, 2025-09-25. Bekendtgørelse af udlændingeloven (LBK nr 1183 af 25/09/2025). <https://www.retsinformation.dk/eli/lta/2025/1183/xml>
[^s22]: Retsinformation / Kirkeministeriet — Cirkulære om fælles dataansvar ... Kirkeministeriets…, 2021-06-15. Cirkulære om fælles dataansvar ... Kirkeministeriets fælles systemer vedrørende personregistrering (CIR1H nr 9447 af 15/06/2021). <https://www.retsinformation.dk/eli/retsinfo/2021/9447/xml>
[^s23]: Agency for Digital Government (Digitaliseringsstyrelsen) — NemLog-in. NemLog-in. <https://en.digst.dk/systems/nemlog-in/> ([archived](https://web.archive.org/web/20260910172930/https://en.digst.dk/systems/nemlog-in/))
[^s24]: Retsinformation / Digitaliseringsministeriet — Bekendtgørelse af lov om MitID og NemLog-in (LBK nr 333…, 2025-03-19. Bekendtgørelse af lov om MitID og NemLog-in (LBK nr 333 af 19/03/2025). <https://www.retsinformation.dk/eli/lta/2025/333/xml>
[^s25]: Digitaliseringsstyrelsen — Drift af NemLog-in sendes i udbud, 2026-01-26. Drift af NemLog-in sendes i udbud. <https://digst.dk/nyheder/nyhedsarkiv/2026/januar/drift-af-nemlog-in-sendes-i-udbud/> ([archived](https://web.archive.org/web/20260514131623/https://digst.dk/nyheder/nyhedsarkiv/2026/januar/drift-af-nemlog-in-sendes-i-udbud/))
[^s26]: Digitaliseringsstyrelsen — NemLog-in Privatlivspolitik, 2025-12-08. NemLog-in Privatlivspolitik. <https://digst.dk/it-loesninger/nemlog-in/om-loesningen/persondata/> ([archived](https://web.archive.org/web/20260514133820/https://digst.dk/it-loesninger/nemlog-in/om-loesningen/persondata/))
[^s27]: Digitaliseringsstyrelsen — Tal og statistik for Digitaliseringsstyrelsens produkter, 2026-03-06. Tal og statistik for Digitaliseringsstyrelsens produkter. <https://digst.dk/tal-og-statistik/>
[^s28]: Retsinformation / Justitsministeriet — Bekendtgørelse af lov om Politiets Efterretningstjeneste…, 2017-03-07. Bekendtgørelse af lov om Politiets Efterretningstjeneste (PET) (LBK nr 231 af 07/03/2017). <https://www.retsinformation.dk/eli/lta/2017/231/xml>
[^s29]: Politi (Rigspolitiet) — Politiets brug af personoplysninger. Politiets brug af personoplysninger. <https://politi.dk/om-hjemmesiden/politiets-brug-af-personoplysninger> ([archived](https://web.archive.org/web/20260915161055/https://politi.dk/om-hjemmesiden/politiets-brug-af-personoplysninger))
[^s30]: Retsinformation / Justitsministeriet — Bekendtgørelse om pas m.v. (BEK nr 2693 af 28/12/2021), 2021-12-28. Bekendtgørelse om pas m.v. (BEK nr 2693 af 28/12/2021). <https://www.retsinformation.dk/eli/lta/2021/2693/xml>
[^s31]: Udlændingestyrelsen (nyidanmark.dk) — Informationssystemer på udlændingeområdet. Informationssystemer på udlændingeområdet. <https://nyidanmark.dk/da/Collaborators/uip>
[^s32]: Danmarks Statistik — Asylansøgninger og opholdstilladelser: Statistisk behandling. Asylansøgninger og opholdstilladelser: Statistisk behandling. <https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/asylansoegninger-og-opholdstilladelser/statistisk-behandling>
[^s33]: Toldstyrelsen — DMS (Declaration Management System). DMS (Declaration Management System). <https://toldst.dk/erhverv/toldsystemer/dms>
[^s34]: Retsinformation / Indenrigs- og Sundhedsministeriet — Bekendtgørelse om valgfri indplacering i sikringsgrupper…, 2025-05-21. Bekendtgørelse om valgfri indplacering i sikringsgrupper og udstedelse af sundhedskort m.v.. <https://www.retsinformation.dk/eli/lta/2025/529/xml>
[^s35]: Retsinformation / Erhvervsministeriet — Bekendtgørelse af lov om Det Centrale…, 2026-02-05. Bekendtgørelse af lov om Det Centrale Virksomhedsregister (LBK nr 246 af 05/02/2026). <https://www.retsinformation.dk/eli/lta/2026/246/xml>
[^s36]: Retsinformation / Justitsministeriet — Bekendtgørelse om behandling af personoplysninger i Det…, 2026-06-22. Bekendtgørelse om behandling af personoplysninger i Det Centrale Kriminalregister (Kriminalregisteret). <https://www.retsinformation.dk/eli/lta/2026/589/xml>
[^s37]: Retsinformation / Udlændinge- og Integrationsministeriet — Bekendtgørelse om udlændingemyndighedernes kompetence…, 2025-09-30. Bekendtgørelse om udlændingemyndighedernes kompetence til at indberette tilbagesendelsesafgørelser ... i medfør af SIS-tilbagesendelsesforordningen. <https://www.retsinformation.dk/eli/lta/2025/1201/xml>
[^s38]: Retsinformation / Justitsministeriet — Cirkulære om våben og ammunition m.v., 2025-10-29. Cirkulære om våben og ammunition m.v.. <https://www.retsinformation.dk/eli/retsinfo/2025/10066/xml>
[^s39]: Økonomistyrelsen — Statens Bevillings- og Regnskabsløsning. Statens Bevillings- og Regnskabsløsning. <https://oes.dk/digitale-loesninger/statens-bevillings-og-regnskabsloesning/> ([archived](https://web.archive.org/web/20260606021813/https://oes.dk/digitale-loesninger/statens-bevillings-og-regnskabsloesning/))
[^s40]: Økonomistyrelsen — Lønudbetaling med Statens Lønløsning. Lønudbetaling med Statens Lønløsning. <https://oes.dk/digitale-loesninger/statens-loenloesning/> ([archived](https://web.archive.org/web/20260629120521/https://oes.dk/digitale-loesninger/statens-loenloesning/))
[^s41]: Økonomistyrelsen — Statens nye lønsystem under udvikling. Statens nye lønsystem under udvikling. <https://oes.dk/digitale-loesninger/udvikling-og-udbud/statens-nye-loensystem-under-udvikling/>
[^s42]: Danmarks Statistik — Folketingsvalg, folkeafstemninger og…. Folketingsvalg, folkeafstemninger og Europa-parlamentsvalg: Præcision og pålidelighed. <https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/folketingsvalg--folkeafstemninger-og-europa-parlamentsvalg/praecision-og-paalidelighed> ([archived](https://web.archive.org/web/20260611190526/https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/folketingsvalg--folkeafstemninger-og-europa-parlamentsvalg/praecision-og-paalidelighed))
[^s43]: European Central Bank — Danish krone now available in all TARGET Services, 2025-04-23. Danish krone now available in all TARGET Services. <https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr250423~096ce05219.en.html>
[^s44]: Danmarks Nationalbank — Overvågning af den finansielle infrastruktur 2025, 2026. Overvågning af den finansielle infrastruktur 2025. <https://www.nationalbanken.dk/da/viden-og-nyheder/publikationer-og-taler/rapport/2026/overvaagning-af-den-finansielle-infrastruktur-2025> ([archived](https://web.archive.org/web/20260513094446/https://www.nationalbanken.dk/da/viden-og-nyheder/publikationer-og-taler/rapport/2026/overvaagning-af-den-finansielle-infrastruktur-2025))
[^s45]: Center for Beredskabskommunikation — Om SINE. Om SINE. <https://sikkerhedsnet.dk/om-sine> ([archived](https://web.archive.org/web/20260710203543/https://sikkerhedsnet.dk/om-sine))
[^s46]: Center for Beredskabskommunikation — Om CFB. Om CFB. <https://sikkerhedsnet.dk/om-cfb>
[^s47]: Center for Beredskabskommunikation (sikkerhedsnet.dk) — Leverandør. Leverandør. <https://sikkerhedsnet.dk/leverandoer> ([archived](https://web.archive.org/web/20260710202945/https://sikkerhedsnet.dk/leverandoer))
[^s48]: Beredskabsstyrelsen — Sirenevarsling. Sirenevarsling. <https://www.brs.dk/da/borger/var-klar-nar-krisen-rammer/det-skal-du-gore-nar-du-horer-sirenerne/> ([archived](https://web.archive.org/web/20260617225444/https://www.brs.dk/da/borger/var-klar-nar-krisen-rammer/det-skal-du-gore-nar-du-horer-sirenerne/))
[^s49]: Retsinformation / Klima-, Energi- og Forsyningsministeriet — Bekendtgørelse af lov om Energinet (LBK nr 271 af…, 2023-03-09. Bekendtgørelse af lov om Energinet (LBK nr 271 af 09/03/2023). <https://www.retsinformation.dk/eli/lta/2023/271/xml>
[^s50]: Uddannelses- og Forskningsstyrelsen — STADS. STADS. <https://ufsn.dk/institutioner-og-drift/studieadministrative-systemer/stads/> ([archived](https://web.archive.org/web/20260519213542/https://ufsn.dk/institutioner-og-drift/studieadministrative-systemer/stads/))
[^s51]: Retsinformation / Indenrigs- og Sundhedsministeriet — Bekendtgørelse af sundhedsloven (LBK nr 275 af 12/03/2025), 2025-03-12. Bekendtgørelse af sundhedsloven (LBK nr 275 af 12/03/2025). <https://www.retsinformation.dk/eli/lta/2025/275/xml>
[^s52]: Sundhedsdatastyrelsen — Fælles Medicinkort. Fælles Medicinkort. <https://sundhedsdatastyrelsen.dk/digitale-loesninger/faelles-medicinkort> ([archived](https://web.archive.org/web/20260616035826/https://sundhedsdatastyrelsen.dk/digitale-loesninger/faelles-medicinkort))
[^s53]: Retsinformation / Styrelsen for Dataforsyning og Effektivisering — Adresseloven (LOV nr 136 af 01/02/2017), 2017-02-01. Adresseloven (LOV nr 136 af 01/02/2017). <https://www.retsinformation.dk/eli/lta/2017/136/xml>

**Evidence grades:** 6 Strong, 55 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
