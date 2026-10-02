# Sweden: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Sweden could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: SOU 2023:61 says Efos (Försäkringskassan's E-identitet för offentlig sektor) is notified at eIDAS level high but is an employee e-service credential (e-tjänstelegitimation). Nothing on the page addresses the root of a government PKI or a…. It is withheld until the fact or its source is corrected and checked again* |
| State-controlled national eID | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The quote is the Government's proposal in Prop. 2025/26:250 that the Act on state e-ID enter into force on 1 December 2026, i.e. a state-operated scheme is legislated but not in operation as of today. The source neither states current…. It is withheld until the fact or its source is corrected and checked again* |
| Government data centres | Yes[^s3][^s4] |
| Government cloud in operation | Yes[^s5][^s4] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Sweden described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.606 million[^s6] |
| GDP, current prices | 600.4 EUR bn[^s7] |
| Public administration employment (NACE O) | 245.0 thousand[^s8] |
| Non-household electricity price | 97.0 EUR/MWh[^s9] |
| Renewables share of electricity | 89.2 %[^s10] |
| Land area | 407 300 km²[^s11] |

## 3. Critical data holdings, by priority

The holdings Sweden cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 24 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Folkbokföringsverksamheten / Skatteverket's population registration data (the national population register)[^s12] | Skatteverket (Swedish Tax Agency) is responsible for population registration[^s13][^s14] | *Not stated in sources* | 10 610 500 persons folkbokförda (registered) at mid-year 2026[^s15] |
| Critical | Facial biometric (tier 0) | Passregistret (passport register), which holds holders' photographs[^s16][^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Disputed: sources disagree. Sveriges riksdag (Svensk författningssamling) — Passlag (1978:302), 1978 gives the value this report printed; Regeringskansliet (SFS) — Lag (2018:1693) om polisens behandling av…, 2026 gives “Biometriregister (biometric registers) of suspects, convicted persons and traces, kept by Polismyndigheten”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | — | — | — |
| Critical | Breeder document scans (tier 0) | Folkbokföring (population registration of births, marriages and deaths), Skatteverket[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Passregistret: central passport register kept by the Police Authority[^s16][^s17] | *Not yet sourced* | *Not stated in sources* | Skatteverket issues about 170,000 identity cards per year[^s19] |
| High | Digital identity credentials (tier 0) | Registret över ärenden om statlig e-legitimation (register of state e-ID cases)[^s20] | Polismyndigheten (Swedish Police Authority)[^s20] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | Fastighetsregistret (real property register)[^s21][^s22] | The state cadastral authority (Lantmäteriet) is controller[^s21][^s22] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Belastningsregistret (criminal records register), Police Authority[^s23][^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Misstankeregistret (register of suspects), Polismyndigheten[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | Röstlängd (electoral roll), drawn up by the central election authority per voting district from folkbokföring data[^s26] | *Not yet sourced* | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The quote is on the page, but it concerns Valmyndighetens valadministrativa it-stöd (ballot ordering, voting cards, result reporting); the page never says the röstlängd is kept or produced in that system, mentioning the roll only as a…. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Aktiebolagsregistret (companies register); Bolagsverket controller[^s27][^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Registret över verkliga huvudmän, kept by Bolagsverket[^s29][^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Vägtrafikregistret (road traffic register) kept by Transportstyrelsen[^s31][^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Swedish national part of the Schengen Information System, kept by the Police Authority[^s33] | Police Authority and Migrationsverket are each controllers for their processing in N.SIS[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Hermes, the state information system for budgeting and follow-up, developed and managed by ESV[^s34] | ESV is responsible for state accounts[^s34] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Primula (Statens servicecenter)[^s5] | Statens servicecenter (SSC), payroll services to 143 agencies in 2023[^s5] | *Not stated in sources* | about 1,5 million payslips (lönespecifikationer) per year[^s5] |
| High | Central bank systems (tier 1) | RIX-RTGS (Riksbank's large-value payment settlement system)[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Rakel (national public-safety radio communication system)[^s36] | Myndigheten för civilt försvar (Swedish Civil Defence Agency)[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Systemet för varning och information till allmänheten (public warning and information system)[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Each higher-education institution keeps a student register (studieregister)[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Svensk författningssamling (SFS, Swedish Code of Statutes), published electronically on a dedicated website[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Election management and results (tier 1) | Valmyndighetens it-stöd used to compile and publish results[^s40] | *Not yet sourced* | National infrastructure[^s40] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Vaccinationsregistret, Folkhälsomyndigheten[^s41][^s42] | Folkhälsomyndigheten coordinates communicable disease control nationally[^s43][^s44] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 23 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
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

> Not yet sized. Capacity for Sweden will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Sweden without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- State PKI and qualified trust services (tier 0)
- Residence and migration status (tier 1)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1321 facts are printed, 3342 values are withheld as gaps, and 89 are withheld as disputed.

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
| T1 authoritative original (official law portal, statistics office, Eurostat) | 613 |
| T2 competent public body or audit office | 594 |
| T3 other institution or company | 7 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 107 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 100 |
| Standard | 1221 |

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

In this build, 1321 of 1321 printed facts pass the fact check.

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

In this build, 1321 of 1321 printed facts pass, and 69 facts are withheld after the check.

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
| wf_f14edd00-71f | 2026-10-02 | 12 | claude-fable-5-1: 12 | supported: 11; not supported: 1 |
| wf_5fd3e22d-b86 | 2026-10-02 | 27 | claude-fable-5-1: 27 | supported: 27 |
| wf_da123db1-a4e | 2026-10-02 | 1360 | claude-fable-5-1: 1360 | supported: 1281; not supported: 46; unclear: 33 |
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Sweden

43 of 43 printed facts about Sweden pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:SE:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SE:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:SE:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SE:population_m | param:SE:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:SE:gdp_eur_bn | param:SE:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SE:gov_employment_k | param:SE:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SE:elec_price_eur_mwh | param:SE:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SE:renewables_pct | param:SE:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:SE:land_km2 | param:SE:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:civil_registry:count | Civil registry core: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:issuance_history:count | Document issuance history: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:government_payroll:operator | Government payroll and personnel: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:government_payroll:count | Government payroll and personnel: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:electoral_management:foreign_dependency | Election management and results: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:SE:public_health_surveillance:operator | Public health surveillance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Sweden

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| indicator:SE:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | claude-fable-5-1 | not supported | SOU 2023:61 says Efos (Försäkringskassan's E-identitet för offentlig sektor) is notified at eIDAS level high but is an employee e-service credential (e-tjänstelegitimation). Nothing on the page addresses the root of a government PKI or a qualified trust service, so it does not answer K1 with 'Yes'. |
| indicator:SE:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | claude-fable-5-1 | unclear | The quote is the Government's proposal in Prop. 2025/26:250 that the Act on state e-ID enter into force on 1 December 2026, i.e. a state-operated scheme is legislated but not in operation as of today. The source neither states current state operation nor a partial one, so whether this maps to 'Partly' is ambiguous without a rubric the page does not supply. |
| record:SE:electoral_roll:foreign_dependency | Electoral roll entry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | unclear | The quote is on the page, but it concerns Valmyndighetens valadministrativa it-stöd (ballot ordering, voting cards, result reporting); the page never says the röstlängd is kept or produced in that system, mentioning the roll only as a limited 2026 feature for digitally marking received votes. Whether the electoral roll's infrastructure is the one Skatteverket operates is not stated by this source. |

---

[^s1]: Regeringskansliet (SFS) — Säkerhetsskyddsförordning (2021:955), 2026. Säkerhetsskyddsförordning (2021:955). <https://data.riksdagen.se/dokument/sfs-2021-955.html> ([archived](https://web.archive.org/web/20260519033902/https://data.riksdagen.se/dokument/sfs-2021-955.html))
[^s2]: Sveriges riksdag / Regeringskansliet (SFS) — Säkerhetsskyddslag (2018:585), 2 kap. 5 §. Säkerhetsskyddslag (2018:585), 2 kap. 5 §. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/> ([archived](https://web.archive.org/web/20260906142442/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/))
[^s3]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2021:1 Säker och kostnadseffektiv it-drift, 2021-01-18. SOU 2021:1 Säker och kostnadseffektiv it-drift. <https://data.riksdagen.se/dokument/ZZB31.html>
[^s4]: Regeringskansliet (SFS, via Sveriges riksdag) — Förordning (2024:1005) om samordnad och säker statlig…, 2024-11-07. Förordning (2024:1005) om samordnad och säker statlig it-drift. <https://data.riksdagen.se/dokument/sfs-2024-1005.html>
[^s5]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2025:13 En effektivare organisering av mindre…, 2025-02-10. SOU 2025:13 En effektivare organisering av mindre myndigheter. <https://data.riksdagen.se/dokument/HDB313.html>
[^s6]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s7]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s8]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s9]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s10]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s11]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s12]: Sveriges riksdag (Svensk författningssamling) — Folkbokföringsdatalag (2026:126), 2026. Folkbokföringsdatalag (2026:126). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingsdatalag-2026126_sfs-2026-126/> ([archived](https://web.archive.org/web/20260611073903/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingsdatalag-2026126_sfs-2026-126/))
[^s13]: Regeringskansliet (SFS) — Folkbokföringsdatalag (2026:126), 2026-02-26. Folkbokföringsdatalag (2026:126). <https://data.riksdagen.se/dokument/sfs-2026-126.html>
[^s14]: Sveriges riksdag (Svensk författningssamling) — Folkbokföringslag (1991:481), 1991. Folkbokföringslag (1991:481). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingslag-1991481_sfs-1991-481/> ([archived](https://web.archive.org/web/20260913214218/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingslag-1991481_sfs-1991-481/))
[^s15]: Statistiska centralbyrån (SCB) — Befolkningsstatistik, 2026-08-21. Befolkningsstatistik. <https://www.scb.se/hitta-statistik/statistik-efter-amne/befolkning-och-levnadsforhallanden/befolkningens-sammansattning-och-utveckling/befolkningsstatistik/> ([archived](https://web.archive.org/web/20260914063708/https://www.scb.se/hitta-statistik/statistik-efter-amne/befolkning-och-levnadsforhallanden/befolkningens-sammansattning-och-utveckling/befolkningsstatistik/))
[^s16]: Regeringskansliet (SFS) — Passförordning (1979:664), 2026. Passförordning (1979:664). <https://data.riksdagen.se/dokument/sfs-1979-664.html>
[^s17]: Sveriges riksdag (Svensk författningssamling) — Passförordning (1979:664), 1979. Passförordning (1979:664). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passforordning-1979664_sfs-1979-664/> ([archived](https://web.archive.org/web/20260813145910/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passforordning-1979664_sfs-1979-664/))
[^s18]: Regeringskansliet (SFS) — Folkbokföringslag (1991:481), 2026. Folkbokföringslag (1991:481). <https://data.riksdagen.se/dokument/sfs-1991-481.html> ([archived](https://web.archive.org/web/20251208011308/https://data.riksdagen.se/dokument/sfs-1991-481.html))
[^s19]: Regeringen (via Sveriges riksdag) — Prop. 2025/26:250 En statlig e-legitimation, 2026-05-07. Prop. 2025/26:250 En statlig e-legitimation. <https://data.riksdagen.se/dokument/hd03250.html>
[^s20]: Regeringskansliet (SFS) — Lag (2026:1358) om statlig e-legitimation och…, 2026-06-18. Lag (2026:1358) om statlig e-legitimation och elektronisk identifiering. <https://data.riksdagen.se/dokument/sfs-2026-1358.html>
[^s21]: Regeringskansliet (SFS) — Förordning (2000:308) om fastighetsregister. Förordning (2000:308) om fastighetsregister. <https://data.riksdagen.se/dokument/sfs-2000-308.html>
[^s22]: Sveriges riksdag (Svensk författningssamling) — Lag (2000:224) om fastighetsregister, 2000. Lag (2000:224) om fastighetsregister. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2000224-om-fastighetsregister_sfs-2000-224/> ([archived](https://web.archive.org/web/20250210201207/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2000224-om-fastighetsregister_sfs-2000-224/))
[^s23]: Polismyndigheten — Belastningsregistret - begära utdrag. Belastningsregistret - begära utdrag. <https://polisen.se/tjanster-tillstand/belastningsregistret/> ([archived](https://web.archive.org/web/20260912120459/https://polisen.se/tjanster-tillstand/belastningsregistret/))
[^s24]: Sveriges riksdag (Svensk författningssamling) — Lag (1998:620) om belastningsregister, 1998. Lag (1998:620) om belastningsregister. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1998620-om-belastningsregister_sfs-1998-620/> ([archived](https://web.archive.org/web/20260813145908/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1998620-om-belastningsregister_sfs-1998-620/))
[^s25]: Regeringskansliet (SFS) — Lag (1998:621) om misstankeregister, 2026. Lag (1998:621) om misstankeregister. <https://data.riksdagen.se/dokument/sfs-1998-621.html>
[^s26]: Sveriges riksdag (Svensk författningssamling) — Vallag (2005:837), 2005. Vallag (2005:837). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vallag-2005837_sfs-2005-837/> ([archived](https://web.archive.org/web/20260924072102/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vallag-2005837_sfs-2005-837/))
[^s27]: Regeringskansliet (SFS) — Aktiebolagslag (2005:551), 2026. Aktiebolagslag (2005:551). <https://data.riksdagen.se/dokument/sfs-2005-551.html> ([archived](https://web.archive.org/web/20230328035707/https://data.riksdagen.se/dokument/sfs-2005-551.html))
[^s28]: Sveriges riksdag (Svensk författningssamling) — Aktiebolagsförordning (2005:559), 2005. Aktiebolagsförordning (2005:559). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/aktiebolagsforordning-2005559_sfs-2005-559/> ([archived](https://web.archive.org/web/20260417064235/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/aktiebolagsforordning-2005559_sfs-2005-559/))
[^s29]: Regeringskansliet (SFS) — Lag (2017:631) om registrering av verkliga huvudmän, 2026. Lag (2017:631) om registrering av verkliga huvudmän. <https://data.riksdagen.se/dokument/sfs-2017-631.html>
[^s30]: Sveriges riksdag (Svensk författningssamling) — Lag (2017:631) om registrering av verkliga huvudmän, 2017. Lag (2017:631) om registrering av verkliga huvudmän. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2017631-om-registrering-av-verkliga_sfs-2017-631/> ([archived](https://web.archive.org/web/20260813171133/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2017631-om-registrering-av-verkliga_sfs-2017-631/))
[^s31]: Sveriges riksdag (Svensk författningssamling) — Vägtrafikdatalag (2019:369), 2019. Vägtrafikdatalag (2019:369). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vagtrafikdatalag-2019369_sfs-2019-369/> ([archived](https://web.archive.org/web/20260609063421/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vagtrafikdatalag-2019369_sfs-2019-369/))
[^s32]: Transportstyrelsen — Fordonsdata från vägtrafikregistret. Fordonsdata från vägtrafikregistret. <https://www.transportstyrelsen.se/sv/vagtrafik/fordon/fordons-agaruppgift/uttag-av-fordonsdata-pa-fil/fordonsdata-fran-vagtrafikregistret/> ([archived](https://web.archive.org/web/20260930160034/https://www.transportstyrelsen.se/sv/vagtrafik/fordon/fordons-agaruppgift/uttag-av-fordonsdata-pa-fil/fordonsdata-fran-vagtrafikregistret/))
[^s33]: Sveriges riksdag (Svensk författningssamling) — Lag (2021:1187) med kompletterande bestämmelser till…, 2021. Lag (2021:1187) med kompletterande bestämmelser till EU:s förordningar om Schengens informationssystem. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20211187-med-kompletterande-bestammelser_sfs-2021-1187/> ([archived](https://web.archive.org/web/20260813144455/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20211187-med-kompletterande-bestammelser_sfs-2021-1187/))
[^s34]: Sveriges riksdag (Svensk författningssamling) — Förordning (2016:1023) med instruktion för…, 2016. Förordning (2016:1023) med instruktion för Ekonomistyrningsverket. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-20161023-med-instruktion-for_sfs-2016-1023/> ([archived](https://web.archive.org/web/20250502031355/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-20161023-med-instruktion-for_sfs-2016-1023/))
[^s35]: Sveriges riksbank — Betalningssystemet RIX. Betalningssystemet RIX. <https://www.riksbank.se/sv/betalningar--kontanter/betalningssystemet-rix/>
[^s36]: Myndigheten för civilt försvar — Rakel. Rakel. <https://www.mcf.se/sv/amnesomraden/samhallsviktiga-kommunikationstjanster/rakel/> ([archived](https://web.archive.org/web/20260915155037/https://www.mcf.se/sv/amnesomraden/samhallsviktiga-kommunikationstjanster/rakel/))
[^s37]: Regeringskansliet (SFS) — Förordning (2008:1002) med instruktion för Myndigheten…, 2026. Förordning (2008:1002) med instruktion för Myndigheten för civilt försvar. <https://data.riksdagen.se/dokument/sfs-2008-1002.html> ([archived](https://web.archive.org/web/20230228040108/https://data.riksdagen.se/dokument/sfs-2008-1002.html))
[^s38]: Sveriges riksdag (Svensk författningssamling) — Förordning (1993:1153) om redovisning av studier m.m.…, 1993. Förordning (1993:1153) om redovisning av studier m.m. vid universitet och högskolor. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-19931153-om-redovisning-av-studier-m_sfs-1993-1153/> ([archived](https://web.archive.org/web/20260516085842/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-19931153-om-redovisning-av-studier-m_sfs-1993-1153/))
[^s39]: Regeringskansliet (SFS) — Lag (1976:633) om kungörande av lagar och andra…. Lag (1976:633) om kungörande av lagar och andra författningar. <https://data.riksdagen.se/dokument/sfs-1976-633.html>
[^s40]: Valmyndigheten — Vårt it-stöd. Vårt it-stöd. <https://www.val.se/om-valmyndigheten/vart-it-stod> ([archived](https://web.archive.org/web/20260913174143/https://www.val.se/om-valmyndigheten/vart-it-stod))
[^s41]: Folkhälsomyndigheten — Nationella vaccinationsregistret. Nationella vaccinationsregistret. <https://www.folkhalsomyndigheten.se/vara-amnesomraden/vaccinationer/nationella-vaccinationsregistret/> ([archived](https://web.archive.org/web/20260907024120/https://www.folkhalsomyndigheten.se/vara-amnesomraden/vaccinationer/nationella-vaccinationsregistret/))
[^s42]: Sveriges riksdag (Svensk författningssamling) — Lag (2012:453) om register över nationella…, 2012. Lag (2012:453) om register över nationella vaccinationsprogram m.m.. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2012453-om-register-over-nationella_sfs-2012-453/> ([archived](https://web.archive.org/web/20260606164900/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2012453-om-register-over-nationella_sfs-2012-453/))
[^s43]: Regeringskansliet (SFS) — Förordning (2021:248) med instruktion för…, 2026. Förordning (2021:248) med instruktion för Folkhälsomyndigheten. <https://data.riksdagen.se/dokument/sfs-2021-248.html>
[^s44]: Sveriges riksdag (Svensk författningssamling) — Smittskyddslag (2004:168), 2004. Smittskyddslag (2004:168). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/smittskyddslag-2004168_sfs-2004-168/>

**Evidence grades:** 1 Strong, 42 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
