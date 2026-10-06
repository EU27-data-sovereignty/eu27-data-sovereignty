# Netherlands: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Netherlands could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | No[^s2][^s3] |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s4][^s6][^s7] |
| Government data centres | Yes[^s8][^s9][^s10][^s3] |
| Government cloud in operation | No[^s3] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 30 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Netherlands described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 18.130 million[^s11] |
| GDP, current prices | 1 170.6 EUR bn[^s12] |
| Public administration employment (NACE O) | 661.0 thousand[^s13] |
| Non-household electricity price | 199.1 EUR/MWh[^s14] |
| Renewables share of electricity | 54.7 %[^s15] |
| Land area | 33 984 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Netherlands cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 25 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s17][^s18] | — | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | DigiD gebruiksgeschiedenis (DigiD usage history)[^s19] | Logius[^s19] | Solvinity currently manages the PICARD platform for Logius on which the DigiD service depends[^s20][^s21] | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Basisregister Reisdocumenten (BR) (Basic Register of Travel Documents)[^s22] | Rijksdienst voor Identiteitsgegevens (National Office for Identity Data, RvIG)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | registratie van de kiesgerechtigdheid (municipal registration of voting eligibility)[^s23] | Burgemeester en wethouders (municipal executives)[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | TSPs issue certificates under the State of the Netherlands trust anchor[^s5] | PKIoverheid is a trust framework managed by Logius on behalf of Ministry of BZK[^s5] | KPN B.V. supplies the technical services for the PKIoverheid Root and Intermediate Certificates for Logius, including the CRLs[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet sourced* | *Not yet sourced* | Kadaster moved to a platform of KPN that is not tied to one specific cloud solution[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Justitiële Documentatie (Judicial Documentation, the criminal records system)[^s26] | Justitiële Informatiedienst (Justid, Judicial Information Service)[^s26] | Justid's own Functioneel Beheer and Technisch Applicatiebeheer teams run day-to-day management of the Justitieel Documentatie Systeem (JDS)[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | DigiD: the national means for citizens to identify digitally[^s4][^s6] | Minister of BZK is controller; DigiD is managed by Logius[^s19][^s28] | Stored on ICT facilities on Dutch territory managed by Logius; not transferred outside the EU[^s19] | National infrastructure[^s19] | *Not yet measured* |
| High | Residence and migration status (tier 1) | vreemdelingenadministratie (aliens administration)[^s29] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | Current declaration system AGS is being replaced by the new DMS[^s30][^s31] | *Not yet sourced* | IBM modifies and manages (beheert) the Douaneaangiften Management Systeem (DMS)[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | polisadministratie (policy administration of employment, wages and benefits)[^s33] | Uitvoeringsinstituut werknemersverzekeringen (UWV, Employee Insurance Agency)[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Business registry (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | UBO-register (Ultimate Beneficial Owner register)[^s34] | handelsregister (trade register, kept by the Kamer van Koophandel)[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | uitslagprogrammatuur OSV2020-U or Abacus (results-tabulation software)[^s36] | Kiesraad (Electoral Council)[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | meldkamers (emergency dispatch control rooms)[^s37] | politie (national police)[^s37] | The Landelijke Meldkamer Samenwerking (LMS), an autonomous unit within the police organisation, manages the control rooms and their interconnected network of control-room locations[^s38] | *Not stated in sources* | tien meldkamers (ten control rooms)[^s37] |
| High | Crisis management and civil protection (tier 1) | NL-Alert (national public warning system)[^s39] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | register onderwijsdeelnemers (register of education participants)[^s40] | Onze Minister (Minister of Education, Culture and Science)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | LSP is a national infrastructure through which care providers exchange patients' medical data[^s41][^s42] | VZVZ Servicecentrum (executive organisation of the association VZVZ)[^s42][^s43] | Medical data remain stored decentrally at the source (GP or pharmacist)[^s44] | *Not stated in sources* | *Not yet measured* |
| Standard | Vehicle & licensing (tier 1) | *Not yet sourced* | RDW manages and is controller of the vehicle registration register[^s45] | RDW register data is stored in RDW's own data centre (eigen datacenter)[^s46] | National infrastructure[^s46] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Staatsblad en Staatscourant (Bulletin of Acts and Decrees; Government Gazette)[^s47] | Minister van Justitie en Veiligheid (Minister of Justice and Security, for the Staatsblad)[^s47] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Government payroll and personnel (tier 1) | registratiesysteem P-Direkt (P-Direkt HR/payroll registration system)[^s10] | *Not yet sourced* | P-Direkt's servers moved to the Overheids Data Centrum (Government Data Centre) of SSC-ICT[^s48] | National infrastructure[^s48] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Praeventis centrally registers vaccinations of every participant in the national immunisation programme[^s49][^s50] | *Not yet sourced* | Sopra Steria carries out technical application management and application development of Praeventis[^s51] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Microdata: linkable person, business and address-level data for authorised researchers[^s52] | *Not yet sourced* | Research is done inside the CBS microdata environment[^s52] | National infrastructure[^s53] | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 24 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 4 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 20 |

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

> Not yet sized. Capacity for Netherlands will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Netherlands without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Breeder document scans (tier 0)
- Tax (tier 1)
- Statutory health insurance (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Treasury and state accounts (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
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

### The verdict on each fact about Netherlands

63 of 63 printed facts about Netherlands pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:NL:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:NL:L3 | indicator L3: Is a cloud certification that requires immunity from non-EU law in force or adopted for government use? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:NL:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:NL:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:NL:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:NL:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:NL:population_m | param:NL:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:NL:gdp_eur_bn | param:NL:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:NL:gov_employment_k | param:NL:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:NL:elec_price_eur_mwh | param:NL:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:NL:renewables_pct | param:NL:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:NL:land_km2 | param:NL:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:NL:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:authentication_audit_log:operator | Authentication audit log: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:authentication_audit_log:hosting | Authentication audit log: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:trust_services_pki:hosting | State PKI and qualified trust services: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:land_property:hosting | Land & property registry: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:judicial_criminal:hosting | Judicial & criminal justice: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:digital_identity_credentials:hosting | Digital identity credentials: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:NL:digital_identity_credentials:foreign_dependency | Digital identity credentials: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:customs:hosting | Customs declarations: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:electoral_management:operator | Election management and results: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:emergency_communications:hosting | Emergency calls and public-safety radio: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:emergency_communications:count | Emergency calls and public-safety radio: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:education:operator | Education: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:health_records:register | Health records: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:health_records:operator | Health records: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:health_records:hosting | Health records: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:NL:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:vehicle_licensing:hosting | Vehicle & licensing: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:vehicle_licensing:foreign_dependency | Vehicle & licensing: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:government_payroll:hosting | Government payroll and personnel: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:government_payroll:foreign_dependency | Government payroll and personnel: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:public_health_surveillance:hosting | Public health surveillance: hosting | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |
| record:NL:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:NL:statistics_microdata:hosting | Statistical microdata: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:NL:statistics_microdata:foreign_dependency | Statistical microdata: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-opus-5-5 | claude-fable-5-1 | supported | wf_f7d14e4d-412 |

### Withheld after the fact check: Netherlands

None.

---

[^s1]: Ministerie van Algemene Zaken / Staatscourant — Besluit voorschrift informatiebeveiliging Rijksdienst…, 2025-09-08. Besluit voorschrift informatiebeveiliging Rijksdienst bijzondere informatie 2025 (VIRBI 2025), Staatscourant 2025, 30222. <https://zoek.officielebekendmakingen.nl/stcrt-2025-30222.html>
[^s2]: Tweede Kamer der Staten-Generaal (letter from the State Secretary of Economic Affairs and Climate) — Kamerstuk 26643 nr. 1542 - Nationaal beleid voor de…, 2026-07. Kamerstuk 26643 nr. 1542 - Nationaal beleid voor de Nederlandse cloudmarkt. <https://zoek.officielebekendmakingen.nl/kst-1263281.pdf>
[^s3]: Ministerie van BZK (bijlage bij Kamerstuk 26643-1537) — Notitie Verkenning Overheidsbrede Soevereine Clouddiensten, 2026-07-20. Notitie Verkenning Overheidsbrede Soevereine Clouddiensten. <https://zoek.officielebekendmakingen.nl/blg-1263102.pdf>
[^s4]: Logius — Onze organisatie. Onze organisatie. <https://www.logius.nl/over-ons/onze-organisatie> ([archived](https://web.archive.org/web/20260519142506/https://www.logius.nl/over-ons/onze-organisatie))
[^s5]: Logius — Wat is PKIoverheid. Wat is PKIoverheid. <https://www.logius.nl/onze-dienstverlening/toegang/pkioverheid/wat-pkioverheid> ([archived](https://web.archive.org/web/20260618011710/https://www.logius.nl/onze-dienstverlening/toegang/pkioverheid/wat-pkioverheid))
[^s6]: Logius — DigiD. DigiD. <https://www.logius.nl/onze-dienstverlening/toegang/digid> ([archived](https://web.archive.org/web/20260826221154/https://www.logius.nl/onze-dienstverlening/toegang/digid))
[^s7]: wetten.overheid.nl (KOOP) — Wet digitale overheid, 2025-11-11. Wet digitale overheid. <https://wetten.overheid.nl/BWBR0048156>
[^s8]: ODC-Noord (Rijksoverheid, SSO-Noord) — Organisatie - ODC-Noord. Organisatie - ODC-Noord. <https://www.odc-noord.nl/Organisatie> ([archived](https://web.archive.org/web/20260226165411/https://www.odc-noord.nl/Organisatie))
[^s9]: Tweede Kamer der Staten-Generaal (letter from the State Secretary of the Interior and Kingdom Relations) — Kamerstuk 26643 nr. 1537 - Stand van zaken verkenning…, 2026-07-01. Kamerstuk 26643 nr. 1537 - Stand van zaken verkenning soevereine overheidscloud. <https://zoek.officielebekendmakingen.nl/kst-1263099.pdf>
[^s10]: Ministerie van BZK — Jaarrapportage Bedrijfsvoering Rijk 2025, 2026-05-26. Jaarrapportage Bedrijfsvoering Rijk 2025. <https://zoek.officielebekendmakingen.nl/blg-1249197.pdf>
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Rijksdienst voor Identiteitsgegevens (RvIG) — Afname kwalitatief goede vingerafdruk luistert nauw, 2023. Afname kwalitatief goede vingerafdruk luistert nauw. <https://www.rvig.nl/afname-kwalitatief-goede-vingerafdruk-luistert-nauw> ([archived](https://web.archive.org/web/20260608174816/https://www.rvig.nl/afname-kwalitatief-goede-vingerafdruk-luistert-nauw))
[^s18]: Overheid.nl Wettenbank — Paspoortwet, 2024-01-01. Paspoortwet. <https://wetten.overheid.nl/BWBR0005212/2024-01-01> ([archived](https://web.archive.org/web/20260928030739/https://wetten.overheid.nl/BWBR0005212/2024-01-01/))
[^s19]: DigiD / Logius — Privacy DigiD. Privacy DigiD. <https://www.digid.nl/over-digid/privacy> ([archived](https://web.archive.org/web/20260927120423/https://www.digid.nl/over-digid/privacy))
[^s20]: Logius — Gegevensverwerkingen DigiD. Gegevensverwerkingen DigiD. <https://www.logius.nl/onze-dienstverlening/toegang/digid/documentatie/gegevensverwerkingen-digid> ([archived](https://web.archive.org/web/20261002113720/https://www.logius.nl/onze-dienstverlening/toegang/digid/documentatie/gegevensverwerkingen-digid))
[^s21]: Tweede Kamer / Staatssecretaris van Binnenlandse Zaken en Koninkrijksrelaties — Aanhangsel Handelingen TK 2025-2026, nr. 2359…, 2026-06-25. Aanhangsel Handelingen TK 2025-2026, nr. 2359 (Kamervragen over DigiD, Solvinity en Kyndryl). <https://zoek.officielebekendmakingen.nl/ah-tk-20252026-2359.html>
[^s22]: Rijksdienst voor Identiteitsgegevens (RvIG) — Basisregister Reisdocumenten. Basisregister Reisdocumenten. <https://www.rvig.nl/basisregister-reisdocumenten> ([archived](https://web.archive.org/web/20260901014608/https://www.rvig.nl/basisregister-reisdocumenten))
[^s23]: wetten.overheid.nl (KOOP) — Kieswet, 2026-01-01. Kieswet. <https://wetten.overheid.nl/BWBR0004627>
[^s24]: Logius – Policy Authority PKIoverheid — CPS PA PKIoverheid Unified version 5.6, 2026-07-15. CPS PA PKIoverheid Unified version 5.6. <https://cps.pkioverheid.nl/pkioverheid-cps-unified-v5.6.html> ([archived](https://web.archive.org/web/20260712001717/https://cps.pkioverheid.nl/pkioverheid-cps-unified-v5.6.html))
[^s25]: Kadaster (sent to the Eerste Kamer) — Jaarverslag Kadaster 2025, 2026. Jaarverslag Kadaster 2025. <https://www.eerstekamer.nl/behandeling/20260414/jaarverslag_kadaster_2025_bijlage/document3/f=/vmxgpusqksww.pdf>
[^s26]: Justitiële Informatiedienst (Justid) — Strafblad en het Justitieel Documentatie Systeem. Strafblad en het Justitieel Documentatie Systeem. <https://www.justid.nl/onderwerpen/s/strafblad-en-het-justitieel-documentatie-systeem> ([archived](https://web.archive.org/web/20260910021135/https://www.justid.nl/onderwerpen/s/strafblad-en-het-justitieel-documentatie-systeem))
[^s27]: Justitiële Informatiedienst (Justid) — Functioneel en technisch applicatiebeheer - Justitieel…. Functioneel en technisch applicatiebeheer - Justitieel Documentatie Systeem (JDS). <https://www.justid.nl/producten-en-dienstencatalogus/nieuwbouw-en-onderhoud-systemen/informatiesystemen/justitieel-documentatie-systeem-jds>
[^s28]: Logius (Ministerie van BZK) — DigiD – Wie doet wat?. DigiD – Wie doet wat?. <https://www.logius.nl/onze-dienstverlening/toegang/digid/wie-doet-wat> ([archived](https://web.archive.org/web/20260413115624/https://www.logius.nl/onze-dienstverlening/toegang/digid/wie-doet-wat))
[^s29]: wetten.overheid.nl (KOOP) — Vreemdelingenwet 2000, 2026-09-01. Vreemdelingenwet 2000. <https://wetten.overheid.nl/BWBR0011823>
[^s30]: Tweede Kamer der Staten-Generaal — Douane; Brief regering; Uitstel invoering nieuw…, 2022-11-07. Douane; Brief regering; Uitstel invoering nieuw aangiftesysteem van de Douane. <https://zoek.officielebekendmakingen.nl/kst-31934-61.html>
[^s31]: Douane / Ministerie van Financiën — Douane Monitor 2024, 2025-07-08. Douane Monitor 2024. <https://zoek.officielebekendmakingen.nl/blg-1205324.pdf>
[^s32]: Adviescollege ICT-toetsing — Advies project CCI/CCE, 2025-10-31. Advies project CCI/CCE. <https://www.tweedekamer.nl/downloads/document?id=2025D49022>
[^s33]: wetten.overheid.nl (KOOP) — Wet structuur uitvoeringsorganisatie werk en inkomen…, 2026-07-01. Wet structuur uitvoeringsorganisatie werk en inkomen (Wet SUWI). <https://wetten.overheid.nl/BWBR0013060>
[^s34]: Kamer van Koophandel (KVK) — Ultimate Beneficial Owner (UBO). Ultimate Beneficial Owner (UBO). <https://www.kvk.nl/ubo/> ([archived](https://web.archive.org/web/20260925130737/https://www.kvk.nl/ubo/))
[^s35]: wetten.overheid.nl (KOOP) — Handelsregisterwet 2007, 2025-07-16. Handelsregisterwet 2007. <https://wetten.overheid.nl/BWBR0021777>
[^s36]: Kiesraad — Evaluatieadvies Kiesraad – gemeenteraadsverkiezingen 2026, 2026-07-06. Evaluatieadvies Kiesraad – gemeenteraadsverkiezingen 2026. <https://zoek.officielebekendmakingen.nl/blg-1261396.pdf>
[^s37]: wetten.overheid.nl (KOOP) — Politiewet 2012, 2026-06-12. Politiewet 2012. <https://wetten.overheid.nl/BWBR0031788>
[^s38]: Landelijke Meldkamer Samenwerking — Over LMS. Over LMS. <https://www.meldkamersamenwerking.nl/over-lms/> ([archived](https://web.archive.org/web/20260513041639/https://www.meldkamersamenwerking.nl/over-lms/))
[^s39]: Rijksoverheid (NL-Alert / NCTV) — NL-Alert. NL-Alert. <https://www.nl-alert.nl/> ([archived](https://web.archive.org/web/20260919232645/https://www.nl-alert.nl/))
[^s40]: wetten.overheid.nl (KOOP) — Wet register onderwijsdeelnemers, 2026-08-01. Wet register onderwijsdeelnemers. <https://wetten.overheid.nl/BWBR0042012>
[^s41]: VZVZ — AORTA-LSP. AORTA-LSP. <https://www.aorta-lsp.nl/> ([archived](https://web.archive.org/web/20260710165804/https://www.aorta-lsp.nl/))
[^s42]: Minister van VWS / Tweede Kamer — Kamerstuk 27529-170: Informatie over de beveiliging van…, 2019-02-11. Kamerstuk 27529-170: Informatie over de beveiliging van gegevens die gedeeld worden via het Landelijk Schakelpunt (LSP). <https://zoek.officielebekendmakingen.nl/kst-27529-170.html> ([archived](https://web.archive.org/web/20240220054303/https://zoek.officielebekendmakingen.nl/kst-27529-170.html))
[^s43]: Tweede Kamer / Minister van VWS (officielebekendmakingen.nl) — Antwoord op vragen van het lid Van Esch over de…, 2020-05-01. Antwoord op vragen van het lid Van Esch over de 'veronderstelde toegang' tot elektronische patiëntendossiers. <https://zoek.officielebekendmakingen.nl/ah-tk-20192020-2652.html>
[^s44]: VZVZ — Hoe werkt het Landelijk Schakelpunt. Hoe werkt het Landelijk Schakelpunt. <https://www.aorta-lsp.nl/over-aorta-lsp/hoe-werkt-het-landelijk-schakelpunt> ([archived](https://web.archive.org/web/20260608090659/https://www.aorta-lsp.nl/over-aorta-lsp/hoe-werkt-het-landelijk-schakelpunt))
[^s45]: Overheid.nl Wettenbank — Wegenverkeerswet 1994, 2026-09-01. Wegenverkeerswet 1994. <https://wetten.overheid.nl/BWBR0006622/2026-09-01> ([archived](https://web.archive.org/web/20260922170754/https://wetten.overheid.nl/BWBR0006622/2026-09-01))
[^s46]: RDW — Jaarverslag RDW 2025, 2026. Jaarverslag RDW 2025. <https://www.rdw.nl/-/media/rdwnl/overrdw/documenten/publicaties/jaarverslagen/rdw-wettelijk-jaarverslag-2025-sdt-def.pdf>
[^s47]: wetten.overheid.nl (KOOP) — Bekendmakingswet, 2024-01-01. Bekendmakingswet. <https://wetten.overheid.nl/BWBR0004287>
[^s48]: Ministerie van Binnenlandse Zaken en Koninkrijksrelaties — Jaarverslag en slotwet Wonen en Rijksdienst (XVIII) 2017, 2018. Jaarverslag en slotwet Wonen en Rijksdienst (XVIII) 2017. <https://zoek.officielebekendmakingen.nl/kst-34950-XVIII-1.html> ([archived](https://web.archive.org/web/20240617083409/https://zoek.officielebekendmakingen.nl/kst-34950-XVIII-1.html))
[^s49]: RIVM — Vaccinatiegraad Rijksvaccinatieprogramma Nederland, 2026-07-02. Vaccinatiegraad Rijksvaccinatieprogramma Nederland. <https://zoek.officielebekendmakingen.nl/blg-1258843.pdf>
[^s50]: Tweede Kamer der Staten-Generaal — Wijziging van een aantal wetten op het terrein van VWS…, 2024-10-02. Wijziging van een aantal wetten op het terrein van VWS (grondslagen gegevensverwerking); Memorie van toelichting. <https://zoek.officielebekendmakingen.nl/kst-36621-3.html> ([archived](https://web.archive.org/web/20251013160730/https://zoek.officielebekendmakingen.nl/kst-36621-3.html))
[^s51]: Adviescollege ICT-toetsing — Advies programma Doorontwikkeling Praeventis, 2025-06-23. Advies programma Doorontwikkeling Praeventis. <https://www.adviescollegeicttoetsing.nl/site/binaries/site-content/collections/documents/2025/06/23/advies-doorontwikkeling-praeventis/advies-programma-doorontwikkeling-praeventis.pdf> ([archived](https://web.archive.org/web/20250909012810/https://www.adviescollegeicttoetsing.nl/site/binaries/site-content/collections/documents/2025/06/23/advies-doorontwikkeling-praeventis/advies-programma-doorontwikkeling-praeventis.pdf))
[^s52]: CBS — Microdata: Zelf onderzoek doen. Microdata: Zelf onderzoek doen. <https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen> ([archived](https://web.archive.org/web/20260923230852/https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen))
[^s53]: Centraal Bureau voor de Statistiek — Toegang tot microdata CBS flexibeler voor onderzoekers, 2017-01. Toegang tot microdata CBS flexibeler voor onderzoekers. <https://www.cbs.nl/nl-nl/corporate/2017/04/toegang-tot-microdata-cbs-flexibeler-voor-onderzoekers> ([archived](https://web.archive.org/web/20260413144015/https://www.cbs.nl/nl-nl/corporate/2017/04/toegang-tot-microdata-cbs-flexibeler-voor-onderzoekers))

**Evidence grades:** 2 Strong, 61 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
