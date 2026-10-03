# Portugal: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Portugal could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2][^s3] |
| Classification in law | Yes[^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | *Not yet sourced* |
| State-controlled national eID | Yes[^s4][^s5] |
| Government data centres | Yes[^s6][^s7][^s8][^s9] |
| Government cloud in operation | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: All three quotes are present (ARTE news 29 May 2026; PNNS May 2026 with 'Desenvolvimento, pelo Estado, de infraestrutura nacional soberana de nuvem' scheduled from S1 2026; RCM 102/2026 funding implementation and initial migration via ARTE…. It is withheld until the fact or its source is corrected and checked again* |

What could move this placement:

- If state-controlled trust anchor is found to be no: Dependent on non-EU providers.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Portugal described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 11.424 million[^s10] |
| GDP, current prices | 308.5 EUR bn[^s11] |
| Public administration employment (NACE O) | 314.8 thousand[^s12] |
| Non-household electricity price | 132.9 EUR/MWh[^s13] |
| Renewables share of electricity | 65.6 %[^s14] |
| Land area | 90 977 km²[^s15] |

## 3. Critical data holdings, by priority

The holdings Portugal cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 4 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Civil registry database (base de dados do registo civil) holding nationality, civil status and legal capacity of citizens[^s16] | The President of IRN, I.P. is the data controller of the civil registry database[^s16] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Facial image files collected for the Citizen Card are communicated only to the civil identification database[^s17] | IRN, I.P. is the controller for Citizen Card data processing operations[^s17] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Citizen Card applications must include facial image and fingerprints[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: Article 32(1) of Lei 33/99 says ID-card applications and 'certidões não emitidas pelo registo civil português' are microfilmed or kept on secure computer media and then destroyed; the printed 'foreign-issued certificates' narrows a scope…. It is withheld until the fact or its source is corrected and checked again* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | Authentication records (type, date/time) and signatures are processed to manage electronic identification[^s4] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Document issuance history (tier 0) | Citizen Card data processing covers issuance, update, renewal and cancellation requests[^s17] | IRN, I.P. is the body responsible for SIPEP[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 7/2007, de 5 de Fevereiro – Cartão de Cidadão…, 2007 gives the value this report printed; ARTE - Agência para a Reforma Tecnológica do Estado (Autenticação.gov) — Chave Móvel Digital gives “Chave Móvel Digital (CMD) (Digital Mobile Key)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | *Disputed: the fact check (claude-fable-5-1, run wf_72f99a66-4e9) did not confirm this: Lei 37/2014 art. 2(8) does assign management and security of the CMD infrastructure to AMA, I.P., and autenticacao.gov.pt says the site is managed by ARTE; but neither page says AMA was the predecessor of ARTE, so the printed parenthetical…. It is withheld until the fact or its source is corrected and checked again* | *Not stated in sources* | *Not yet sourced* |
| High | Electoral roll entry (tier 0) | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 13/99, de 22 de Março – Regime Jurídico do…, 1999 gives the value this report printed; Secretaria-Geral do Ministério da Administração Interna (SGMAI) — Administração Eleitoral gives “Base de Dados do Recenseamento Eleitoral (Voter Registration Database)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | SGMAI electoral administration organises, maintains and manages BDRE and SIGRE[^s19] | *Not stated in sources* | 11 130 316 inscritos para votar (registered voters)[^s20] |
| High | State PKI and qualified trust services (tier 0) | The State Electronic Certification Entity is the state's root certification authority at the top of the SCEE chain[^s21] | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 12/2021, de 9 de fevereiro (art. 27.º), 2021 gives the value this report printed; Agência para a Reforma Tecnológica do Estado, I.P. (ARTE) — Certificação eletrónica gives “ARTE (Agência para a Reforma Tecnológica do Estado; Agency for the Technological Reform of the State)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Land registry databases hold the legal status of real property[^s22] | The President of IRN, I.P. is the controller of the land registry databases[^s22] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Electronic court case processing takes place in the courts' support information system[^s23] | DGAJ is the entity responsible for the criminal identification databases[^s24][^s25] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | centros de dados do Serviço de Informações de Segurança e do Serviço de Informações Estratégicas de Defesa (data centres of the SIS and the SIED)[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Residence and migration status (tier 1) | SII AIMA: personal-data information system holding non-police information on foreign nationals[^s27] | Administrative migration and asylum functions were transferred to the new AIMA, I.P.[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | STADA-IMP (customs import declaration processing system)[^s29] | AT (Autoridade Tributária e Aduaneira; Tax and Customs Authority)[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | All natural and legal persons dealing with social security are identified in the information system[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | The National Patient Register (RNU) is used as the patient identification reference by other national health systems[^s31][^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | The commercial registry database holds the legal status of registered entities[^s33] | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) did not confirm this: Código do Registo Comercial art. 78-C(1) says verbatim that the director-geral dos Registos e do Notariado is the database controller, but the page never mentions IRN; the printed gloss '(now IRN)' is added from outside the source. It is withheld until the fact or its source is corrected and checked again* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Registo Central de Beneficiário Efetivo (RCBE) (Central Register of Beneficial Ownership)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | The vehicle registry database holds the legal status of motor vehicles[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | SII UCFE: shared police information system on borders and foreign nationals, used by security forces[^s27] | Management of former SEF systems, including the national part of SIS, passes to a security information technology unit[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | Budget data are registered in SIGO (DGO) and entered in information systems managed by ESPAP, I.P.[^s37] | *Disputed: the fact check (claude-fable-5-1, run wf_72f99a66-4e9) did not confirm this: Both IGCP quotes are present and say the IGCP, E.P.E. manages the State's treasury, financing and direct public debt. Neither page mentions the Direção-Geral do Orçamento or ESPAP, so the printed operator is not what the cited sources say. It is withheld until the fact or its source is corrected and checked again* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 53/2008, de 29 de Agosto – Lei de Segurança Interna, 2008 gives the value this report printed; SIRESP, S.A. — Home - SIRESP gives “Rede Nacional de Emergência e Segurança – SIRESP (National Emergency and Security Network)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | SIRESP, S.A.[^s38] | *Not stated in sources* | mais de 40.000 utilizadores (more than 40,000 users)[^s38] |
| High | Crisis management and civil protection (tier 1) | ANEPC organises a national alert and warning system[^s39] | ANEPC plans, coordinates and executes emergency and civil protection policy, including civil emergency planning for crisis or war[^s39] | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | centro de Despacho (National Dispatch centre) of REN - Rede Elétrica Nacional[^s40] | REN - Rede Elétrica Nacional[^s40] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | The national water authority establishes and maintains the national water resources information system[^s41][^s42] | APA, I.P. is the national water authority exercising the powers of the Water Law[^s42] | *Not stated in sources* | *Not yet measured* |
| High | Education (tier 1) | Qualification diplomas and certificates under the National Qualifications System are made available in SIGO[^s43][^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | National reference geographic database products include topographic mapping and orthophoto mapping[^s45] | DGT gathers territorial geographic information in the National Territorial Information System (SNIT)[^s45] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 27 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 27 |

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

> Not yet sized. Capacity for Portugal will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 4 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Portugal without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Tax (tier 1)
- Police information systems (tier 1)
- Firearms register (tier 1)
- Official gazette and legislation (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)

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

### The verdict on each fact about Portugal

49 of 49 printed facts about Portugal pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:PT:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:PT:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:PT:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:PT:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:PT:population_m | param:PT:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:PT:gdp_eur_bn | param:PT:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:PT:gov_employment_k | param:PT:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:PT:elec_price_eur_mwh | param:PT:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:PT:renewables_pct | param:PT:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:PT:land_km2 | param:PT:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:electoral_roll:count | Electoral roll entry: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:land_property:operator | Land & property registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:intelligence:register | Intelligence services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:customs:operator | Customs declarations: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:health_insurance:register | Statutory health insurance: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:PT:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:border_control:operator | Border and visa systems: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:emergency_communications:count | Emergency calls and public-safety radio: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:crisis_management:operator | Crisis management and civil protection: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:water_control:register | Water management control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:water_control:operator | Water management control: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:education:register | Education: the name of the register or system | claude-opus-5-5 | claude-fable-5-1 | supported | wf_72f99a66-4e9 |
| record:PT:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:PT:geospatial:operator | Geospatial base data: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Portugal

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| indicator:PT:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | claude-fable-5-1 | unclear | All three quotes are present (ARTE news 29 May 2026; PNNS May 2026 with 'Desenvolvimento, pelo Estado, de infraestrutura nacional soberana de nuvem' scheduled from S1 2026; RCM 102/2026 funding implementation and initial migration via ARTE and IP Telecom). They show an approved, funded plan in execution, but none states that a sovereign cloud platform is in operation, so whether 'Partly' rather th |
| record:PT:breeder_documents:register | Breeder document scans: the name of the register or system | claude-fable-5-1 | not supported | Article 32(1) of Lei 33/99 says ID-card applications and 'certidões não emitidas pelo registo civil português' are microfilmed or kept on secure computer media and then destroyed; the printed 'foreign-issued certificates' narrows a scope the source states as 'not issued by the Portuguese civil registry', which is not the same thing, and 'paper originals' is likewise not in the text. |
| record:PT:business_registry:operator | Business registry: the body that operates it | claude-fable-5-1 | not supported | Código do Registo Comercial art. 78-C(1) says verbatim that the director-geral dos Registos e do Notariado is the database controller, but the page never mentions IRN; the printed gloss '(now IRN)' is added from outside the source. |
| record:PT:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | claude-fable-5-1 | not supported | Lei 37/2014 art. 2(8) does assign management and security of the CMD infrastructure to AMA, I.P., and autenticacao.gov.pt says the site is managed by ARTE; but neither page says AMA was the predecessor of ARTE, so the printed parenthetical adds a succession claim the sources do not state. |
| record:PT:public_finance:operator | Treasury and state accounts: the body that operates it | claude-fable-5-1 | not supported | Both IGCP quotes are present and say the IGCP, E.P.E. manages the State's treasury, financing and direct public debt. Neither page mentions the Direção-Geral do Orçamento or ESPAP, so the printed operator is not what the cited sources say. |

---

[^s1]: Agência para a Reforma Tecnológica do Estado, I.P. (ARTE) — Estratégia Digital Nacional – Plano de Ação 2026-2027…, 2025-12-29. Estratégia Digital Nacional – Plano de Ação 2026-2027 (projeto 8.2). <https://www.arte.gov.pt/wp-content/uploads/2026/05/Plano-de-Acao-2026-2027_EDN.pdf>
[^s2]: Presidência do Conselho de Ministros (Diário da República, 1.ª série, N.º 102) — Resolução do Conselho de Ministros n.º 102/2026 – Aprova…, 2026-05-27. Resolução do Conselho de Ministros n.º 102/2026 – Aprova o Plano Nacional de Nuvem Soberana. <https://bo.digital.gov.pt/api/assets/etic/2fecc6f4-b424-41c6-b2a8-722b17b1914f/> ([archived](https://web.archive.org/web/20260702232015/https://bo.digital.gov.pt/api/assets/etic/2fecc6f4-b424-41c6-b2a8-722b17b1914f/))
[^s3]: Assembleia da República (copy hosted by SIRP) — Lei Orgânica n.º 2/2014, de 6 de agosto – Regime do…, 2014-08-06. Lei Orgânica n.º 2/2014, de 6 de agosto – Regime do Segredo de Estado (Diário da República, 1.ª série, N.º 150). <https://sirp.pt/wp-content/uploads/2025/09/LEI_DO_SEGREDO_DE_ESTADO.pdf> ([archived](https://web.archive.org/web/20251108103511/https://sirp.pt/wp-content/uploads/2025/09/LEI_DO_SEGREDO_DE_ESTADO.pdf))
[^s4]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — Termos e Condições – Autenticação.gov. Termos e Condições – Autenticação.gov. <https://www.autenticacao.gov.pt/web/guest/termos-e-condicoes> ([archived](https://web.archive.org/web/20260830101400/https://www.autenticacao.gov.pt/web/guest/termos-e-condicoes))
[^s5]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — A Chave Móvel Digital. A Chave Móvel Digital. <https://www.autenticacao.gov.pt/web/guest/a-chave-movel-digital> ([archived](https://web.archive.org/web/20260914162323/https://www.autenticacao.gov.pt/web/guest/a-chave-movel-digital))
[^s6]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — Plano Nacional de Nuvem Soberana (Maio 2026), 2026-05. Plano Nacional de Nuvem Soberana (Maio 2026). <https://www.arte.gov.pt/wp-content/uploads/2026/05/Plano-Nacional-de-Nuvem-Soberana.pdf>
[^s7]: IP Telecom – Serviços de Telecomunicações, S.A. — Sobre Nós. Sobre Nós. <https://www.iptelecom.pt/pt-pt/empresa/sobre-nos> ([archived](https://web.archive.org/web/20260626202759/https://www.iptelecom.pt/pt-pt/empresa/sobre-nos))
[^s8]: IP Telecom – Serviços de Telecomunicações, S.A. — IPT Cloud & Datacenter. IPT Cloud & Datacenter. <https://www.iptelecom.pt/pt-pt/servicos/ipt-cloud-datacenter> ([archived](https://web.archive.org/web/20260626202758/https://www.iptelecom.pt/pt-pt/servicos/ipt-cloud-datacenter))
[^s9]: Sistema de Informações da República Portuguesa (SIRP) — Organização do SIRP, 2026. Organização do SIRP. <https://sirp.pt/organizacao-do-sirp/> ([archived](https://web.archive.org/web/20260608091525/https://sirp.pt/organizacao-do-sirp/))
[^s10]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s11]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s12]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s13]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s14]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s15]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s16]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Código do Registo Civil (DL n.º 131/95), art. 220.º-A, 1995. Código do Registo Civil (DL n.º 131/95), art. 220.º-A. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=682A0220A&nid=682&tabela=leis&pagina=1&ficha=1&nversao=>
[^s17]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 7/2007, de 5 de Fevereiro – Cartão de Cidadão…, 2007. Lei n.º 7/2007, de 5 de Fevereiro – Cartão de Cidadão (art. 37.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2807&tabela=leis>
[^s18]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 86/2000, de 12 de Maio – SIPEP (art. 2.º), 2000. Decreto-Lei n.º 86/2000, de 12 de Maio – SIPEP (art. 2.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2056&tabela=leis>
[^s19]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 13/99, de 22 de Março – Regime Jurídico do…, 1999. Lei n.º 13/99, de 22 de Março – Regime Jurídico do Recenseamento Eleitoral (art. 10.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2545&tabela=leis>
[^s20]: Secretaria-Geral do Ministério da Administração Interna (SGMAI) — Portal da SGMAI – Números Administração Eleitoral, 2026-08. Portal da SGMAI – Números Administração Eleitoral. <https://www.sg.mai.gov.pt/> ([archived](https://web.archive.org/web/20141227112353/http://www.sg.mai.gov.pt:80/?))
[^s21]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 12/2021, de 9 de fevereiro (art. 27.º), 2021. Decreto-Lei n.º 12/2021, de 9 de fevereiro (art. 27.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3404&tabela=leis>
[^s22]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Código do Registo Predial (DL n.º 224/84), art. 106.º, 1984. Código do Registo Predial (DL n.º 224/84), art. 106.º. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=488A0106&nid=488&tabela=leis&pagina=1&ficha=1&nversao=>
[^s23]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Portaria n.º 350-A/2025/1, de 9 de outubro – tramitação…, 2025. Portaria n.º 350-A/2025/1, de 9 de outubro – tramitação eletrónica dos processos (art. 2.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3949&tabela=leis>
[^s24]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 37/2015, de 5 de Maio – Lei da Identificação…, 2015. Lei n.º 37/2015, de 5 de Maio – Lei da Identificação Criminal (art. 38.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2321&tabela=leis>
[^s25]: Direção-Geral da Administração da Justiça (DGAJ) — Certificado do Registo Criminal Online, 2026-09-10. Certificado do Registo Criminal Online. <https://registocriminal.justica.gov.pt/> ([archived](https://web.archive.org/web/20260731123603/https://registocriminal.justica.gov.pt/))
[^s26]: Sistema de Informações da República Portuguesa (SIRP) — Fiscalização, 2026. Fiscalização. <https://sirp.pt/fiscalizacao/> ([archived](https://web.archive.org/web/20260608080258/https://sirp.pt/fiscalizacao/))
[^s27]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 23/2007, de 4 de Julho – Entrada, permanência,…, 2007. Lei n.º 23/2007, de 4 de Julho – Entrada, permanência, saída e afastamento de estrangeiros (art. 3.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=920&tabela=leis> ([archived](https://web.archive.org/web/20260723065246/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=920&tabela=leis))
[^s28]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 41/2023, de 2 de junho – cria a AIMA, I.…, 2023. Decreto-Lei n.º 41/2023, de 2 de junho – cria a AIMA, I. P. (preâmbulo). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3676&tabela=leis>
[^s29]: Autoridade Tributária e Aduaneira (AT) — Relatório de Atividades 2024, 2025. Relatório de Atividades 2024. <https://info.portaldasfinancas.gov.pt/pt/at/Instrumentos_Gestao/Relatorio_atividades/Documents/Relatorio_de_Atividades_AT_2024.pdf> ([archived](https://web.archive.org/web/20260509164626/https://info.portaldasfinancas.gov.pt/pt/at/Instrumentos_Gestao/Relatorio_atividades/Documents/Relatorio_de_Atividades_AT_2024.pdf))
[^s30]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 4/2007, de 16 de Janeiro – Bases gerais do…, 2007. Lei n.º 4/2007, de 16 de Janeiro – Bases gerais do sistema de segurança social (art. 98.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2243&tabela=leis> ([archived](https://web.archive.org/web/20250430135035/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2243&tabela=leis))
[^s31]: Entidade Reguladora da Saúde (ERS) — O Registo Nacional de Utentes (RNU) e a inscrição nos…, 2026-08-12. O Registo Nacional de Utentes (RNU) e a inscrição nos cuidados de saúde primários. <https://www.ers.pt/pt/utentes/perguntas-frequentes/faq/o-registo-nacional-de-utentes-rnu-e-a-inscricao-nos-cuidados-de-saude-primarios/>
[^s32]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Portaria n.º 22/2016, de 10 de fevereiro – Regulamento…, 2016. Portaria n.º 22/2016, de 10 de fevereiro – Regulamento de Notificação Obrigatória de Doenças Transmissíveis (art. 12.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2506&tabela=leis>
[^s33]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Código do Registo Comercial (DL n.º 403/86), art. 78.º-B, 1986. Código do Registo Comercial (DL n.º 403/86), art. 78.º-B. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=506A0078B&nid=506&tabela=leis&pagina=1&ficha=1&nversao=>
[^s34]: Instituto dos Registos e do Notariado, I.P. (IRN) / Justiça.gov.pt — Registo Central do Beneficiário Efetivo, 2026-09-30. Registo Central do Beneficiário Efetivo. <https://rcbe.justica.gov.pt/> ([archived](https://web.archive.org/web/20260724173200/https://rcbe.justica.gov.pt/))
[^s35]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 54/75, de 12 de Fevereiro – Registo…, 1975. Decreto-Lei n.º 54/75, de 12 de Fevereiro – Registo automóvel (art. 27.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=598&tabela=leis> ([archived](https://web.archive.org/web/20251010024521/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=598&tabela=leis))
[^s36]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 73/2021, de 12 de novembro – reestruturação do…, 2021. Lei n.º 73/2021, de 12 de novembro – reestruturação do sistema português de controlo de fronteiras. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3468&tabela=leis> ([archived](https://web.archive.org/web/20240601081051/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3468&tabela=leis))
[^s37]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 13-A/2025, de 10 de março – normas de…, 2025. Decreto-Lei n.º 13-A/2025, de 10 de março – normas de execução do Orçamento do Estado para 2025. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3890&tabela=leis>
[^s38]: SIRESP, S.A. — Home - SIRESP. Home - SIRESP. <https://www.siresp.pt/> ([archived](https://web.archive.org/web/20260608175758/https://www.siresp.pt/))
[^s39]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 45/2019, de 1 de abril – orgânica da…, 2019. Decreto-Lei n.º 45/2019, de 1 de abril – orgânica da ANEPC (art. 3.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3049&tabela=leis>
[^s40]: REN - Redes Energéticas Nacionais — Eletricidade. Eletricidade. <https://www.ren.pt/pt-pt/atividade/eletricidade>
[^s41]: Agência Portuguesa do Ambiente (APA) — Sistema Nacional de Informação de Recursos Hídricos - SNIRH, 2026-06-05. Sistema Nacional de Informação de Recursos Hídricos - SNIRH. <https://apambiente.pt/agua/sistema-nacional-de-informacao-de-recursos-hidricos-snirh> ([archived](https://web.archive.org/web/20260617184912/https://apambiente.pt/agua/sistema-nacional-de-informacao-de-recursos-hidricos-snirh))
[^s42]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 58/2005, de 29 de Dezembro – Lei da Água (art. 7.º), 2005. Lei n.º 58/2005, de 29 de Dezembro – Lei da Água (art. 7.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1191&tabela=leis> ([archived](https://web.archive.org/web/20250712012849/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1191&tabela=leis))
[^s43]: Direção-Geral da Educação (Ministério da Educação) — Modelos de diplomas e de certificados em formato eletrónico. Modelos de diplomas e de certificados em formato eletrónico. <https://www.dge.mec.pt/noticias/modelos-de-diplomas-e-de-certificados-em-formato-eletronico> ([archived](https://web.archive.org/web/20260214042656/https://www.dge.mec.pt/noticias/modelos-de-diplomas-e-de-certificados-em-formato-eletronico))
[^s44]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 396/2007, de 31 de Dezembro – Sistema…, 2007. Decreto-Lei n.º 396/2007, de 31 de Dezembro – Sistema Nacional de Qualificações (art. 7.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1081&tabela=leis> ([archived](https://web.archive.org/web/20221206135358/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1081&tabela=leis))
[^s45]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 99/2019, de 5 de setembro – revisão do PNPOT, 2019. Lei n.º 99/2019, de 5 de setembro – revisão do PNPOT. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3139&tabela=leis>

**Evidence grades:** 3 Strong, 46 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
