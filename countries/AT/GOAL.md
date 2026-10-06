# Austria: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Austria could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Partly[^s3][^s4] |
| State-controlled national eID | Yes[^s5][^s6] |
| Government data centres | Yes[^s7][^s8][^s9] |
| Government cloud in operation | Yes[^s10][^s11][^s12] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Austria described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 9.216 million[^s13] |
| GDP, current prices | 514.3 EUR bn[^s14] |
| Public administration employment (NACE O) | 280.5 thousand[^s15] |
| Non-household electricity price | 198.6 EUR/MWh[^s16] |
| Renewables share of electricity | 90.8 %[^s17] |
| Land area | 82 494 km²[^s18] |

## 3. Critical data holdings, by priority

The holdings Austria cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 31 of 39 holding classes have a verified source; 5 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Hosting (as sourced) | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Zentrales Melderegister (ZMR) - Central Register of Residents[^s19] | Federal Minister of the Interior acts as processor of the ZPR[^s20][^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Disputed: the fact check (claude-fable-5-1, run wf_72f99a66-4e9) did not confirm this: All three quotes are present, but SPG § 75 establishes a 'Zentrale erkennungsdienstliche Evidenz' in which security authorities jointly process identification data that § 64(2) defines to include Papillarlinienabdrücke (fingerprints), and…. It is withheld until the fact or its source is corrected and checked again* | — | — | — | — |
| Critical | Breeder document scans (tier 0) | Supporting documents underlying civil status entries are kept by the civil status authority that made the entry (decentralised)[^s21] | *Not yet sourced* | Documents may be kept on microfilm or electronic media instead of paper[^s21] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Facial biometric (tier 0) | Central evidence under § 22b Passport Act holds passport/ID card data including the facial image (lit. j) but not fingerprints (lit. k)[^s22] | *Not yet sourced* | *Disputed: the fact check (claude-fable-5-1, run wf_e9645602-884) did not confirm this: § 16(6) Passgesetz 1992 says verbatim that Bundesrechenzentrum GmbH participates as processor in the data processing under §§ 22a and 22b, which supports the processor role; but the cited page says nothing about BRZ's ownership, so the…. It is withheld until the fact or its source is corrected and checked again* | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: The Passgesetz says verbatim that Bundesrechenzentrum GmbH takes part as processor in the § 22a/§ 22b processing; it names a federal body as processor but says nothing about where the infrastructure runs, so 'National infrastructure' rests…. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Elektronischer Identitätsnachweis (E-ID), branded ID Austria[^s23][^s6] | Federal Minister of the Interior and the Source PIN Register Authority process E-ID registration data[^s6] | The private trust service provider runs the certificate database in its own data centre[^s4] | *Not stated in sources* | *Not yet sourced* |
| High | Electoral roll entry (tier 0) | Zentrales Wählerregister (ZeWaeR) - Central Voter Register[^s24] | Federal Minister of the Interior acts as processor of ZeWaeR for each municipality[^s24] | *Not yet sourced* | *Not stated in sources* | 6,346,059 persons entitled to vote in the 2024 National Council election[^s25] |
| High | State PKI and qualified trust services (tier 0) | Austrian Country Signing CA (CSCA) operated by the Federal Ministry of the Interior[^s3] | RTR-GmbH compiles and publishes the national trust list[^s26][^s27] | *Not yet sourced* | *Not stated in sources* | fast 6,3 Millionen ID Austria-Registrierungen (almost 6.3 million ID Austria registrations) as of 1 September 2026[^s28] |
| High | Land & property registry (tier 1) | Grundbuch (land register)[^s29] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Strafregister (criminal record register)[^s30] | Landespolizeidirektion Wien (Vienna Provincial Police Directorate)[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | PAD - Protokollieren Anzeigen Daten (police case and report logging system)[^s31] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | Datenverarbeitung mittels operativer oder strategischer Analyse (state-protection analysis data processing, jointly controlled by the Federal Minister of the Interior and the provincial police directorates)[^s32] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Identitätsdokumentenregister (IDR) - Identity Document Register[^s33][^s4] | *Not yet sourced* | BRZ GmbH is the statutory processor of the Identity Document Register[^s4] | *Disputed: the fact check (claude-fable-5-1, run wf_da123db1-a4e) could not confirm this: Both quotes are present (the RH sentence is split by a line-break hyphen 'Identitätsdokumentenregis- ters') and establish that BRZ GmbH, a federal body, is the statutory processor of the register; neither source says where the…. It is withheld until the fact or its source is corrected and checked again* | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Disputed: sources disagree. Bundeskanzleramt (RIS) — BFA-Verfahrensgesetz (BFA-VG), consolidated version gives the value this report printed; Bundesministerium für Inneres — Information zu der Verarbeitung „Zentrales Fremdenregister“ gives “Zentrales Fremdenregister (Central Register of Foreigners)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | Federal Minister of the Interior acts as processor of the Central Register of Foreigners[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | FinanzOnline[^s35] | Bundesrechenzentrum GmbH (BRZ) for the Bundesministerium für Finanzen (Federal Computing Centre, for the Federal Ministry of Finance)[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | e-zoll (electronic customs)[^s36] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | mehr als 4,5 Mio. Zollanmeldungen pro Jahr (more than 4,5 million customs declarations per year)[^s36] |
| High | Benefits & pensions (tier 1) | Pensionskonto (pension account)[^s37] | Dachverband der Sozialversicherungsträger (Umbrella Association of Austrian Social Insurance Institutions)[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Elektronisches Verwaltungssystem (ELSY) (electronic administration system, the e-card system)[^s38] | Dachverband (der Sozialversicherungsträger) (Umbrella Association of Social Insurance Institutions)[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Firmenbuch (companies register)[^s29] | BRZ (Bundesrechenzentrum GmbH) for the Justizministerium (Federal Computing Centre for the Ministry of Justice)[^s29] | *Not yet sourced* | *Not stated in sources* | etwa 545.000 Firmen (about 545,000 companies)[^s29] |
| High | Beneficial ownership register (tier 1) | Register der wirtschaftlichen Eigentümer (Register of Beneficial Owners)[^s39] | WiEReG–Registerbehörde im Bundesministerium für Finanzen (WiEReG register authority in the Federal Ministry of Finance)[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Zentrale Zulassungsevidenz - Kraftfahrzeugzentralregister (KZR) (Central Motor Vehicle Register)[^s40] | Bundesminister für Inneres (Federal Minister of the Interior)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Nationales Schengener Informationssystem (N-SIS II) (National Schengen Information System)[^s41] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Zentrales Waffenregister (Central Weapons Register)[^s42] | Bundesminister für Inneres as processor, with IBM Österreich Internationale Büromaschinen GmbH, Microsoft Österreich GmbH and Bundesrechenzentrum GmbH as further processors[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Haushaltsverrechnungssystem HV-SAP (federal budget accounting system)[^s43] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Personalverrechnungssystem PM-SAP (federal payroll system)[^s43] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | Modulares Wahlpaket (modular election package)[^s44] | Bundeswahlbehörde p.A. Bundesministerium für Inneres (Federal Electoral Board, c/o Federal Ministry of the Interior)[^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET Services (RTGS, TIPS, T2S, CLM)[^s45] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | BOS-Digitalfunk, österreichweites Digitalfunksystem für Behörden und Organisationen mit Sicherheitsaufgaben (nationwide public-safety digital radio system)[^s46] | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Bundeslagezentrum (Federal Situation Centre)[^s47] | Bundesministerium für Inneres (Federal Ministry of the Interior)[^s47] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | APG-Steuerzentrale, Power Grid Control (APG control centre)[^s48] | APG (Austrian Power Grid AG)[^s48] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* | *—* |
| High | Education (tier 1) | Gesamtevidenz der Schülerinnen und Schüler (national overall register of pupils)[^s49] | Bundesanstalt „Statistik Österreich“ (Statistics Austria), as processor[^s49] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Rechtsinformationssystem des Bundes (RIS) (Federal Legal Information System)[^s50] | Bundeskanzler (Federal Chancellor / Federal Chancellery)[^s50] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 30 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 28 |

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

> Not yet sized. Capacity for Austria will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 5 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Austria without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
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

### The verdict on each fact about Austria

65 of 65 printed facts about Austria pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:AT:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:AT:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:AT:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:AT:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| indicator:AT:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:AT:population_m | param:AT:population_m | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_5fd3e22d-b86 |
| param:AT:gdp_eur_bn | param:AT:gdp_eur_bn | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:AT:gov_employment_k | param:AT:gov_employment_k | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:AT:elec_price_eur_mwh | param:AT:elec_price_eur_mwh | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:AT:renewables_pct | param:AT:renewables_pct | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| param:AT:land_km2 | param:AT:land_km2 | program:fetch_eurostat.py | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:breeder_documents:hosting | Breeder document scans: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:AT:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:digital_identity_credentials:hosting | Digital identity credentials: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:AT:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:electoral_roll:count | Electoral roll entry: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:trust_services_pki:count | State PKI and qualified trust services: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:land_property:register | Land & property registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:police_records:register | Police information systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:intelligence:register | Intelligence services: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:issuance_history:hosting | Document issuance history: hosting | unrecorded | claude-fable-5-1 | supported | wf_e9645602-884 |
| record:AT:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:tax:register | Tax: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:tax:operator | Tax: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:customs:register | Customs declarations: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:customs:count | Customs declarations: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:business_registry:register | Business registry: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:business_registry:operator | Business registry: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:business_registry:count | Business registry: how many records it holds | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:border_control:register | Border and visa systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:firearms_register:register | Firearms register: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:firearms_register:operator | Firearms register: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:electoral_management:register | Election management and results: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:electoral_management:operator | Election management and results: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:central_bank:register | Central bank systems: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:crisis_management:operator | Crisis management and civil protection: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:education:register | Education: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:education:operator | Education: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |
| record:AT:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | claude-fable-5-1 | supported | wf_da123db1-a4e |

### Withheld after the fact check: Austria

| Claim | What it answers | Checked by | Verdict | Reason |
|---|---|---|---|---|
| record:AT:facial_biometric:foreign_dependency | Facial biometric: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | unclear | The Passgesetz says verbatim that Bundesrechenzentrum GmbH takes part as processor in the § 22a/§ 22b processing; it names a federal body as processor but says nothing about where the infrastructure runs, so 'National infrastructure' rests on an inference the statute does not state. |
| record:AT:facial_biometric:hosting | Facial biometric: hosting | claude-fable-5-1 | not supported | § 16(6) Passgesetz 1992 says verbatim that Bundesrechenzentrum GmbH participates as processor in the data processing under §§ 22a and 22b, which supports the processor role; but the cited page says nothing about BRZ's ownership, so the printed '(state-owned)' is added from outside the source. |
| record:AT:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | claude-fable-5-1 | not supported | All three quotes are present, but SPG § 75 establishes a 'Zentrale erkennungsdienstliche Evidenz' in which security authorities jointly process identification data that § 64(2) defines to include Papillarlinienabdrücke (fingerprints), and the BMI sheet names the Federal Minister of the Interior as its controller. Only passport fingerprints are excluded (Passgesetz § 22b), so 'No central register'  |
| record:AT:issuance_history:foreign_dependency | Document issuance history: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | claude-fable-5-1 | unclear | Both quotes are present (the RH sentence is split by a line-break hyphen 'Identitätsdokumentenregis- ters') and establish that BRZ GmbH, a federal body, is the statutory processor of the register; neither source says where the infrastructure runs or rules out further (possibly foreign) sub-processors, so 'National infrastructure' is an inference from the processor's identity rather than a statemen |

---

[^s1]: Bundeskanzleramt (RIS) — Sicherheitspolizeigesetz (SPG), consolidated version, § 55, 2026-10-03. Sicherheitspolizeigesetz (SPG), consolidated version, § 55. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005792> ([archived](https://web.archive.org/web/20260208105744/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005792))
[^s2]: Bundeskanzleramt (RIS) — Informationssicherheitsgesetz (InfoSiG), consolidated…. Informationssicherheitsgesetz (InfoSiG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20001740> ([archived](https://web.archive.org/web/20250823130719/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Gesetzesnummer=20001740&Abfrage=Bundesnormen))
[^s3]: Bundesministerium für Inneres — The Austrian Country Signing CA (CSCA). The Austrian Country Signing CA (CSCA). <https://www.bmi.gv.at/downloads/csca.html> ([archived](https://web.archive.org/web/20260608085339/https://www.bmi.gv.at/downloads/csca.html))
[^s4]: Rechnungshof Österreich — Umstellung von der Bürgerkarte/Handysignatur auf den…, 2023. Umstellung von der Bürgerkarte/Handysignatur auf den elektronischen Identitätsnachweis (E-ID), Reihe Bund 2023/7. <https://www.rechnungshof.gv.at/rh/home/home/2023_7_E-ID.pdf>
[^s5]: Rechnungshof Österreich — Elektronischer Identitätsnachweis: Hohe Abhängigkeit von…, 2023. Elektronischer Identitätsnachweis: Hohe Abhängigkeit von externen Unternehmen. <https://www.rechnungshof.gv.at/rh/home/news/news/news_3/Umstellung_von_Handysignatur_auf_E-ID.html> ([archived](https://web.archive.org/web/20230331220531/https://www.rechnungshof.gv.at/rh/home/news/news/news_3/Umstellung_von_Handysignatur_auf_E-ID.html))
[^s6]: Bundeskanzleramt (RIS) — E-Government-Gesetz (E-GovG), consolidated version. E-Government-Gesetz (E-GovG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003230> ([archived](https://web.archive.org/web/20260414095127/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003230))
[^s7]: Bundesrechenzentrum GmbH (BRZ) — Trusted Data Center. Trusted Data Center. <https://www.brz.gv.at/was-wir-tun/geschaeftsfelder/trusted-data-center.html> ([archived](https://web.archive.org/web/20260613053800/https://www.brz.gv.at/was-wir-tun/geschaeftsfelder/trusted-data-center.html))
[^s8]: Bundesrechenzentrum GmbH — Was wir tun. Was wir tun. <https://www.brz.gv.at/was-wir-tun.html>
[^s9]: Bundeskanzleramt (RIS) — Bundesgesetz über die Bundesrechenzentrum GmbH…. Bundesgesetz über die Bundesrechenzentrum GmbH (BRZ-Gesetz), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001466>
[^s10]: Bundesrechenzentrum GmbH (BRZ) — Cloud Solutions & Shared Services. Cloud Solutions & Shared Services. <https://www.brz.gv.at/was-wir-tun/geschaeftsfelder/cloud-solutions.html> ([archived](https://web.archive.org/web/20260613063223/https://www.brz.gv.at/was-wir-tun/geschaeftsfelder/cloud-solutions.html))
[^s11]: Bundesrechenzentrum GmbH — Geschäftsfelder. Geschäftsfelder. <https://www.brz.gv.at/was-wir-tun/geschaeftsfelder.html> ([archived](https://web.archive.org/web/20250916204831/https://www.brz.gv.at/was-wir-tun/geschaeftsfelder.html))
[^s12]: Bundesrechenzentrum GmbH — Cloud Storage - BRZ GoverDrive. Cloud Storage - BRZ GoverDrive. <https://www.brz.gv.at/was-wir-tun/services-produkte/cloud-storage_brz_goverdrive.html> ([archived](https://web.archive.org/web/20260313144351/https://www.brz.gv.at/was-wir-tun/services-produkte/cloud-storage_brz_goverdrive.html))
[^s13]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s14]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s15]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s16]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s17]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s18]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s19]: Bundeskanzleramt (RIS) — Meldegesetz 1991 (MeldeG), consolidated version. Meldegesetz 1991 (MeldeG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005799>
[^s20]: Bundesministerium für Inneres — Zentrales Melderegister - ZMR, 2025-03-27. Zentrales Melderegister - ZMR. <https://www.bmi.gv.at/413/start.html> ([archived](https://web.archive.org/web/20260828130334/https://www.bmi.gv.at/413/start.html))
[^s21]: Bundeskanzleramt (RIS) — Personenstandsgesetz 2013 (PStG 2013), consolidated version. Personenstandsgesetz 2013 (PStG 2013), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008228> ([archived](https://web.archive.org/web/20260407203750/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008228))
[^s22]: Bundeskanzleramt (RIS) — Passgesetz 1992, consolidated version, 2026-09-30. Passgesetz 1992, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005798> ([archived](https://web.archive.org/web/20260123224358/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005798))
[^s23]: Bundesrechenzentrum GmbH (BRZ) — ID Austria. ID Austria. <https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html> ([archived](https://web.archive.org/web/20260610144149/https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html))
[^s24]: Bundeskanzleramt (RIS) — Wählerevidenzgesetz 2018 (WEviG), consolidated version. Wählerevidenzgesetz 2018 (WEviG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009720> ([archived](https://web.archive.org/web/20260208002104/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Gesetzesnummer=20009720&Abfrage=Bundesnormen))
[^s25]: Bundesministerium für Inneres — Nationalratswahl 2024, 2024. Nationalratswahl 2024. <https://www.bmi.gv.at/412/nationalratswahlen/nationalratswahl_2024/start.html>
[^s26]: Bundeskanzleramt (RIS) — Signatur- und Vertrauensdienstegesetz (SVG),…. Signatur- und Vertrauensdienstegesetz (SVG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009585> ([archived](https://web.archive.org/web/20260211052418/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009585))
[^s27]: Rundfunk und Telekom Regulierungs-GmbH (RTR) — Vertrauensliste der beaufsichtigten…. Vertrauensliste der beaufsichtigten Vertrauensdiensteanbieter. <https://www.rtr.at/TKP/was_wir_tun/vertrauensdienste/Signatur/vertrauensliste/VertrListe.de.html> ([archived](https://web.archive.org/web/20260908033759/https://www.rtr.at/TKP/was_wir_tun/vertrauensdienste/Signatur/vertrauensliste/VertrListe.de.html))
[^s28]: Bundeskanzleramt Österreich — Pröll: 6,3 Millionen ausgestellte "ID Austria" nach…, 2026-09-08. Pröll: 6,3 Millionen ausgestellte "ID Austria" nach erfolgreicher ID Austria Servicetour. <https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/09/proell-6-3-millionen-ausgestellte-id-austria-nach-erfolgreicher-id-austria-servicetour.html>
[^s29]: Bundesrechenzentrum GmbH (BRZ) — Registerlösungen wie Grundbuch und Firmenbuch. Registerlösungen wie Grundbuch und Firmenbuch. <https://www.brz.gv.at/was-wir-tun/services-produkte/registerloesungen.html> ([archived](https://web.archive.org/web/20260519193214/https://www.brz.gv.at/was-wir-tun/services-produkte/registerloesungen.html))
[^s30]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Strafregistergesetz 1968, consolidated version, 2026-09-30. Strafregistergesetz 1968, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002116> ([archived](https://web.archive.org/web/20251105105153/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002116))
[^s31]: Bundesministerium für Inneres — Information zu der Verarbeitung „PAD - Protokollieren…. Information zu der Verarbeitung „PAD - Protokollieren Anzeigen Daten“. <https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_pad-protkollieren_anzeigen_daten_v2.pdf> ([archived](https://web.archive.org/web/20260508105548/https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_pad-protkollieren_anzeigen_daten_v2.pdf))
[^s32]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Staatsschutz- und Nachrichtendienst-Gesetz (SNG),…. Staatsschutz- und Nachrichtendienst-Gesetz (SNG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009486> ([archived](https://web.archive.org/web/20251211035839/https://www.ris.bka.gv.at/geltendefassung.wxe?abfrage=bundesnormen&gesetzesnummer=20009486))
[^s33]: Landespolizeidirektion Burgenland (Bundespolizei) — Information zu der Verarbeitung „Zentrales…, 2021-01. Information zu der Verarbeitung „Zentrales Identitätsdokumentenregister (IDR)“. <https://www.polizei.gv.at/bgld/files_bgld/datenschutz/2023/zentrales_identitaetsdokumentenregister_idr_012023_bf.pdf> ([archived](https://web.archive.org/web/20241125081919/https://www.polizei.gv.at/BGLD/files_bgld/datenschutz/2023/Zentrales_Identitaetsdokumentenregister_IDR_012023_bf.pdf))
[^s34]: Bundeskanzleramt (RIS) — BFA-Verfahrensgesetz (BFA-VG), consolidated version. BFA-Verfahrensgesetz (BFA-VG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20007944> ([archived](https://web.archive.org/web/20260723072308/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20007944))
[^s35]: Bundesrechenzentrum GmbH (BRZ) — FinanzOnline. FinanzOnline. <https://www.brz.gv.at/was-wir-tun/services-produkte/finanzonline.html> ([archived](https://web.archive.org/web/20260516205141/https://www.brz.gv.at/was-wir-tun/services-produkte/finanzonline.html))
[^s36]: Bundesrechenzentrum GmbH (BRZ) — e-zoll. e-zoll. <https://www.brz.gv.at/was-wir-tun/services-produkte/e-zoll.html> ([archived](https://web.archive.org/web/20260519182925/https://www.brz.gv.at/was-wir-tun/services-produkte/e-zoll.html))
[^s37]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Allgemeines Pensionsgesetz § 10. Allgemeines Pensionsgesetz § 10. <https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003831&Paragraf=10>
[^s38]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Allgemeines Sozialversicherungsgesetz § 31a, 2026-01-01. Allgemeines Sozialversicherungsgesetz § 31a. <https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=31a> ([archived](https://web.archive.org/web/20260612022848/https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=31a))
[^s39]: Bundesministerium für Finanzen — Register der wirtschaftlichen Eigentümer. Register der wirtschaftlichen Eigentümer. <https://www.bmf.gv.at/services/wiereg.html> ([archived](https://web.archive.org/web/20260723020928/https://www.bmf.gv.at/services/wiereg.html))
[^s40]: Bundesministerium für Inneres — Information zu der Verarbeitung „Zentrale…. Information zu der Verarbeitung „Zentrale Zulassungsevidenz - Kraftfahrzeugzentralregister (KZR)“. <https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_zentrale_zulassungsevidenz-kraftfahrzeugzentralregister-kzr_v2.pdf> ([archived](https://web.archive.org/web/20260508152304/https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_zentrale_zulassungsevidenz-kraftfahrzeugzentralregister-kzr_v2.pdf))
[^s41]: Bundesministerium für Inneres — Information zu der Verarbeitung „Nationales Schengener…. Information zu der Verarbeitung „Nationales Schengener Informationssystem (N-SIS II)“. <https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_nationales_schengener_informationssystem-n-sis_ii_v2.pdf> ([archived](https://web.archive.org/web/20260508105448/https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_nationales_schengener_informationssystem-n-sis_ii_v2.pdf))
[^s42]: Landespolizeidirektion Steiermark (Bundespolizei) — Information zu der gemeinsamen Verarbeitung „Zentrales…, 2020-02-24. Information zu der gemeinsamen Verarbeitung „Zentrales Waffenregister“. <https://www.polizei.gv.at/stmk/files_stmk/datenschutz/2020/BF_Zentrales%20Waffenregister_20200224.pdf> ([archived](https://web.archive.org/web/20260505131709/https://www.polizei.gv.at/stmk/files_stmk/datenschutz/2020/bf_zentrales%20waffenregister_20200224.pdf))
[^s43]: Rechnungshof Österreich — Bundesrechnungsabschluss für das Jahr 2024, Textteil Band 4, 2025. Bundesrechnungsabschluss für das Jahr 2024, Textteil Band 4. <https://rechnungshof.gv.at/rh/home/home_1/home_9/BRA_2024_Band_4.pdf>
[^s44]: Bundeswahlbehörde / Bundesministerium für Inneres — Information zu der Verarbeitung Modulares Wahlpaket, 2025-04-10. Information zu der Verarbeitung Modulares Wahlpaket. <https://www.bmi.gv.at/402/files/informationen/wahlen/informationsblatt_modulares_wahlpaket_bf_20250410.pdf> ([archived](https://web.archive.org/web/20260616054805/https://www.bmi.gv.at/402/files/informationen/wahlen/informationsblatt_modulares_wahlpaket_bf_20250410.pdf))
[^s45]: Oesterreichische Nationalbank (OeNB) — TARGET Services. TARGET Services. <https://www.oenb.at/Zahlungsverkehr/target-services.html> ([archived](https://web.archive.org/web/20260312220131/https://www.oenb.at/Zahlungsverkehr/target-services.html))
[^s46]: Bundesministerium für Inneres — Abteilung IV/DDS/12 (Kritische…. Abteilung IV/DDS/12 (Kritische Kommunikationsinfrastrukturen). <https://www.bmi.gv.at/113/Sektion_IV/Gruppe_IV_DDS/CTO/Abteilung_IV_DDS_12/start.aspx>
[^s47]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Bundes-Krisensicherheitsgesetz (B-KSG), consolidated version. Bundes-Krisensicherheitsgesetz (B-KSG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20012321>
[^s48]: Austrian Power Grid AG (APG) — Steuerzentrale. Steuerzentrale. <https://www.apg.at/ueber-uns/steuerzentrale/> ([archived](https://web.archive.org/web/20260522164325/https://www.apg.at/ueber-uns/steuerzentrale/))
[^s49]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Bildungsdokumentationsgesetz 2020, consolidated version. Bildungsdokumentationsgesetz 2020, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011451> ([archived](https://web.archive.org/web/20260730015701/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011451))
[^s50]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Bundesgesetzblattgesetz, consolidated version, 2026-09-30. Bundesgesetzblattgesetz, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002988> ([archived](https://web.archive.org/web/20230506214536/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002988))

**Evidence grades:** 4 Strong, 61 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
