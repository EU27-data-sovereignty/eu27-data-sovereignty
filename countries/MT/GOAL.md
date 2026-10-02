# Malta: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Malta could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | *Not yet sourced* |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s1] |
| State-controlled national eID | Yes[^s2][^s3][^s4][^s5] |
| Government data centres | *Disputed: the cited source is gone (HTTP 404, rechecked 2026-09-30)* |
| Government cloud in operation | *Disputed: the cited source is gone (HTTP 404, rechecked 2026-09-30)* |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Malta described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 0.59 million[^s6] |
| GDP, current prices | 24.7 EUR bn[^s7] |
| Public administration employment (NACE O) | 20.1 thousand[^s8] |
| Non-household electricity price | 135.2 EUR/MWh[^s9] |
| Renewables share of electricity | 11.2 %[^s10] |
| Land area | 313 km²[^s11] |

## 3. Critical data holdings, by priority

The holdings Malta cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 18 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Civil Status Section of the Public Registry holds acts of birth, marriage, civil union and death registered in Malta[^s12][^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Facial images captured for the e-ID card are passed to the Electoral Office for voting documents and electoral registers[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Live biometrics including fingerprints are captured at the Passport Office for passport applications[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Archives of the Public Registry[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Biometric passports have been issued since 30 September 2008[^s17] | The Identity Cards Unit issues electronic ID cards and registers e-ID accounts[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | The e-ID virtual account is required to access Government online services[^s2][^s19] | Identity Cards Unit registers e-ID (virtual) accounts[^s2][^s18] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | The Act refers to the Electoral Register database[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | e-ID cards carry an Authentication Certificate and a Signature Certificate[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Land Registration System (LRS)[^s21][^s22] | Land Registration Agency[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Named authorities (Attorney General, Commissioner of Police, Security Service) have continuous direct access to criminal conviction records[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | The Service's function is protecting national security against organised crime, espionage, terrorism and sabotage[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Residence and migration status (tier 1) | Biometrics are captured from non-EU applicants for residence documents[^s26] | Expatriates Unit processes and issues residence documentation[^s27][^s2] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | Health Act defines insured persons as those included in a list established by regulations[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Business Automation Registry Online System (BAROS)[^s29] | Malta Business Registry (MBR)[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Register of Beneficial Owners[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | Entry-Exit System (EES)[^s30] | Central Visa Unit (CVU)[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Legislation Malta portal holds all Maltese laws including consolidated subsidiary legislation[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Census of population and housing held by order under the Act[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 18 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 18 |

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

> Not yet sized. Capacity for Malta will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Malta without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Vehicle & licensing (tier 1)
- Police information systems (tier 1)
- Firearms register (tier 1)
- Treasury and state accounts (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Crisis management and civil protection (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

## Appendix: fact check

### What was checked, and by whom

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. The check below is made by a second model, not by a person.

Every printed fact is put, exactly as printed, to a checker that is a different model from the one that wrote it. The checker fetches the cited source and decides whether it supports the statement as printed: the same value, name, unit, date, country and scope. A production deploy is refused unless every printed fact has a current verdict of supported from an eligible checker.

In this build, 0 of 1390 printed facts pass.

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
- Before every production deploy, factcheck.py gate requires a current supported verdict from an eligible checker for every printed fact, and this file to be current. A disagreement blocks the deploy until the fact or its source is fixed and checked again; nothing is changed automatically.

A verdict holds for one fact exactly as printed: a SHA-256 of the claim, the question it answers, the printed text and every citation behind it. If any of these changes, the verdict lapses and the fact must be checked again before the next deploy.

### Fact-check runs

No fact-check run has been recorded yet, so no printed fact has been checked.

### The verdict on each fact about Malta

0 of 32 printed facts about Malta pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:MT:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:MT:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| param:MT:population_m | param:MT:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:MT:gdp_eur_bn | param:MT:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:MT:gov_employment_k | param:MT:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:MT:elec_price_eur_mwh | param:MT:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:MT:renewables_pct | param:MT:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:MT:land_km2 | param:MT:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:MT:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | none | never checked |  |
| record:MT:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | none | never checked |  |
| record:MT:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:land_property:register | Land & property registry: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:land_property:operator | Land & property registry: the body that operates it | unrecorded | none | never checked |  |
| record:MT:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:intelligence:register | Intelligence services: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | none | never checked |  |
| record:MT:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:business_registry:register | Business registry: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:business_registry:operator | Business registry: the body that operates it | unrecorded | none | never checked |  |
| record:MT:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:border_control:register | Border and visa systems: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:border_control:operator | Border and visa systems: the body that operates it | unrecorded | none | never checked |  |
| record:MT:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | none | never checked |  |
| record:MT:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | none | never checked |  |

---

[^s1]: Malta Communications Authority — Malta Trusted List (TSL). Malta Trusted List (TSL). <https://tsl.mca.org.mt/MT_TSL.xml> ([archived](https://web.archive.org/web/20260908033511/https://tsl.mca.org.mt/MT_TSL.xml))
[^s2]: Identità — Get to Know Identità, 2025-11-13. Get to Know Identità. <https://identita.gov.mt/get-to-know-identita/> ([archived](https://web.archive.org/web/20260415233523/https://identita.gov.mt/get-to-know-identita/))
[^s3]: Identità (formerly Identity Malta Agency) — About Us - Identità. About Us - Identità. <https://identita.gov.mt/about-us/> ([archived](https://web.archive.org/web/20260928102340/https://identita.gov.mt/about-us/))
[^s4]: European Commission, Interoperable Europe / NIFO — Digital Public Administration Factsheet 2024 - Malta…. Digital Public Administration Factsheet 2024 - Malta (Supporting Document). <https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024%20Supporting%20Document_Malta_vFinal.pdf> ([archived](https://web.archive.org/web/20260128014217/https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024%20Supporting%20Document_Malta_vFinal.pdf))
[^s5]: Government of Malta – Legislation Malta — Identity Malta Agency (Establishment) Order (S.L. 595.07), 2025-07-22. Identity Malta Agency (Establishment) Order (S.L. 595.07). <https://legislation.mt/getpdf/689061f044ed663ec0f22f07>
[^s6]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s7]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s8]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s9]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s10]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s11]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s12]: Identità — Public Registry – Civil Status. Public Registry – Civil Status. <https://identita.gov.mt/public-registry-sec-page-civil-status/> ([archived](https://web.archive.org/web/20260811142151/https://identita.gov.mt/public-registry-sec-page-civil-status/))
[^s13]: Government of Malta – Legislation Malta — Civil Code (Cap. 16), 2026-07-17. Civil Code (Cap. 16). <https://legislation.mt/getpdf/6a7c3f2652fe431ca8f9b4f1> ([archived](https://web.archive.org/web/20260813100609/https://legislation.mt/getpdf/6a7c3f2652fe431ca8f9b4f1))
[^s14]: Identità — Identity Cards Unit – Electoral Office. Identity Cards Unit – Electoral Office. <https://identita.gov.mt/identity-cards-unit-electoral-office/> ([archived](https://web.archive.org/web/20260415222752/https://identita.gov.mt/identity-cards-unit-electoral-office/))
[^s15]: Identità — Passport Office – Adults Renewals. Passport Office – Adults Renewals. <https://identita.gov.mt/passport-office-adults-renewals/> ([archived](https://web.archive.org/web/20260928102340/https://identita.gov.mt/passport-office-adults-renewals/))
[^s16]: Identità — Public Registry – Main Page, 2026-06-02. Public Registry – Main Page. <https://identita.gov.mt/public-registry-main-page/> ([archived](https://web.archive.org/web/20260928102340/https://identita.gov.mt/public-registry-main-page/))
[^s17]: Identità — Passport Office. Passport Office. <https://identita.gov.mt/passport-office-main-page/>
[^s18]: Identità — Identity Cards Unit. Identity Cards Unit. <https://identita.gov.mt/identity-cards-unit/> ([archived](https://web.archive.org/web/20260516233554/https://identita.gov.mt/identity-cards-unit/))
[^s19]: Identità — e-ID Virtual Account. e-ID Virtual Account. <https://identita.gov.mt/identity-cards-unit/eid-virtual-account/> ([archived](https://web.archive.org/web/20260811140802/https://identita.gov.mt/identity-cards-unit/eid-virtual-account/))
[^s20]: Government of Malta – Legislation Malta — General Elections Act (Cap. 354). General Elections Act (Cap. 354). <https://legislation.mt/getpdf/661645c07403ed16fcf9eb8e>
[^s21]: Legislation Malta — Land Registration Act (Cap. 296), 2021-07-06. Land Registration Act (Cap. 296). <https://legislation.mt/getpdf/60efe5f532d0f719d442f08c>
[^s22]: Land Registration Agency — A Leap Forward in Digital Transformation – Launch of the…, 2026-07-30. A Leap Forward in Digital Transformation – Launch of the New Digital Platform LRS. <https://lra.mt/news/a-leap-forward-in-digital-transformation-launch-of-the-new-digital-platform-lrs/>
[^s23]: Land Registration Agency — Land Registration Agency – Home, 2026-09-04. Land Registration Agency – Home. <https://lra.mt/> ([archived](https://web.archive.org/web/20260729135459/https://lra.mt/))
[^s24]: Government of Malta – Legislation Malta — Conduct Certificates Ordinance (Cap. 77). Conduct Certificates Ordinance (Cap. 77). <https://legislation.mt/getpdf/6aa1090e5ca02023e4009067>
[^s25]: Government of Malta – Legislation Malta — Security Service Act (Cap. 391). Security Service Act (Cap. 391). <https://legislation.mt/getpdf/6022ba1cbc827214c09ac4a7>
[^s26]: Identità — Expatriates Unit – Biometrics and Interim Receipt. Expatriates Unit – Biometrics and Interim Receipt. <https://identita.gov.mt/expatriates-unit-main-page/noneu-nationals/useful-information/finalising-application-process/biometrics-and-interim-receipt/> ([archived](https://web.archive.org/web/20260606020509/https://identita.gov.mt/expatriates-unit-main-page/noneu-nationals/useful-information/finalising-application-process/biometrics-and-interim-receipt/))
[^s27]: Identità — Expatriates Unit. Expatriates Unit. <https://identita.gov.mt/expatriates-unit-main-page/> ([archived](https://web.archive.org/web/20260928102340/https://identita.gov.mt/expatriates-unit-main-page/))
[^s28]: Government of Malta – Legislation Malta — Health Act (Cap. 528). Health Act (Cap. 528). <https://legislation.mt/getpdf/677e3ecacc8e8e3d102ff18a>
[^s29]: Malta Business Registry — Malta Business Registry – About Us. Malta Business Registry – About Us. <https://mbr.mt/>
[^s30]: Identità — Expatriates Unit Non-EU Nationals – Entry Exit System, 2025-07-17. Expatriates Unit Non-EU Nationals – Entry Exit System. <https://identita.gov.mt/expatriates-unit-main-page/noneu-nationals/entry-exit-system/> ([archived](https://web.archive.org/web/20260302171515/https://identita.gov.mt/expatriates-unit-main-page/noneu-nationals/entry-exit-system/))
[^s31]: Identità — Central Visa Unit – Main Page, 2026-08-12. Central Visa Unit – Main Page. <https://identita.gov.mt/central-visa-unit-main-page/> ([archived](https://web.archive.org/web/20260811143611/https://identita.gov.mt/central-visa-unit-main-page/))
[^s32]: Legislation Malta — FAQs – Leġiżlazzjoni Malta. FAQs – Leġiżlazzjoni Malta. <https://legislation.mt/Home/FAQList> ([archived](https://web.archive.org/web/20260918104521/https://legislation.mt/Home/FAQList))
[^s33]: Government of Malta – Legislation Malta — Malta Statistics Authority Act (Cap. 422). Malta Statistics Authority Act (Cap. 422). <https://legislation.mt/getpdf/6022c0cfbc827214c09b08e1>

**Evidence grades:** 14 Strong, 18 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
