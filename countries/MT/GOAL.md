# Malta: critical data holdings and sovereign hosting

> Generated 2026-09-29 by `model/generate_countries.py` from the content model (`model/document.py`). The same document is typeset as the country PDF and rendered on the web. Every fact carries a footnote to a source whose text was fetched and checked; a value in *italics* is withheld because no checked source supports it yet.

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
| State-controlled national eID | Yes[^s2][^s3] |
| Government data centres | Yes[^s3] |
| Government cloud in operation | Yes[^s3] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Malta described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 0.57 million[^s4] |
| GDP, current prices | 24.7 EUR bn[^s5] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 135.2 EUR/MWh[^s6] |
| Renewables share of electricity | 10.7 %[^s7] |
| Land area | 313 km²[^s8] |

## 3. Critical data holdings, by priority

The holdings Malta cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 13 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Civil Status Section of the Public Registry holds acts of birth, marriage, civil union and death registered in Malta[^s9] | Public Registry offices are managed by the Director of the Public Registry (Public Registry Act, Cap. 56)[^s10] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Facial images captured for the e-ID card are passed to the Electoral Office for voting documents and electoral registers[^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Live biometrics including fingerprints are captured at the Passport Office for passport applications[^s12] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Biometric passports have been issued since 30 September 2008[^s13] | The Identity Cards Unit issues electronic ID cards and registers e-ID accounts[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | The e-ID virtual account is required to access Government online services[^s15] | Identity Cards Unit registers e-ID (virtual) accounts[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | The Act refers to the Electoral Register database[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | e-ID cards carry an Authentication Certificate and a Signature Certificate[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | Named authorities (Attorney General, Commissioner of Police, Security Service) have continuous direct access to criminal conviction records[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | The Service's function is protecting national security against organised crime, espionage, terrorism and sabotage[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Residence and migration status (tier 1) | Biometrics are captured from non-EU applicants for residence documents[^s19] | Expatriates Unit processes and issues residence documentation[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | Health Act defines insured persons as those included in a list established by regulations[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
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
| Standard | Official gazette and legislation (tier 1) | Legislation Malta portal holds all Maltese laws including consolidated subsidiary legislation[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Census of population and housing held by order under the Act[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 13 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 13 |

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

- Breeder document scans (tier 0)
- Authentication audit log (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Beneficial ownership register (tier 1)
- Vehicle & licensing (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
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

---

[^s1]: Malta Communications Authority c1c4113db2. Malta Trusted List (TSL). <https://tsl.mca.org.mt/MT_TSL.xml> ([archived](https://web.archive.org/web/20260908033511/https://tsl.mca.org.mt/MT_TSL.xml))
[^s2]: Identità (formerly Identity Malta Agency) 3b09be07b4. About Us - Identità. <https://identita.gov.mt/about-us/> ([archived](https://web.archive.org/web/20260928102340/https://identita.gov.mt/about-us/))
[^s3]: European Commission, Interoperable Europe / NIFO ae4b6fe043. Digital Public Administration Factsheet 2024 - Malta (Supporting Document). <https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024%20Supporting%20Document_Malta_vFinal.pdf> ([archived](https://web.archive.org/web/20260128014217/https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024%20Supporting%20Document_Malta_vFinal.pdf))
[^s4]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s5]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s6]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s7]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s8]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s9]: Identità e91aaadc94. Public Registry – Civil Status. <https://identita.gov.mt/public-registry-sec-page-civil-status/> ([archived](https://web.archive.org/web/20260811142151/https://identita.gov.mt/public-registry-sec-page-civil-status/))
[^s10]: Government of Malta – Legislation Malta 57d033af2b. Public Registry Act (Cap. 56). <https://legislation.mt/getpdf/602e53fb8f58ad1b78f3edbe>
[^s11]: Identità d7ec3fc7a7. Identity Cards Unit – Electoral Office. <https://identita.gov.mt/identity-cards-unit-electoral-office/> ([archived](https://web.archive.org/web/20260415222752/https://identita.gov.mt/identity-cards-unit-electoral-office/))
[^s12]: Identità 393db9f62f. Passport Office – Adults Renewals. <https://identita.gov.mt/passport-office-adults-renewals/> ([archived](https://web.archive.org/web/20260928102340/https://identita.gov.mt/passport-office-adults-renewals/))
[^s13]: Identità 38e4dd4c1e. Passport Office. <https://identita.gov.mt/passport-office-main-page/>
[^s14]: Identità b58a780ace. Identity Cards Unit. <https://identita.gov.mt/identity-cards-unit/> ([archived](https://web.archive.org/web/20260516233554/https://identita.gov.mt/identity-cards-unit/))
[^s15]: Identità 9a76dd1f0b. e-ID Virtual Account. <https://identita.gov.mt/identity-cards-unit/eid-virtual-account/> ([archived](https://web.archive.org/web/20260811140802/https://identita.gov.mt/identity-cards-unit/eid-virtual-account/))
[^s16]: Government of Malta – Legislation Malta 017ae7f717. General Elections Act (Cap. 354). <https://legislation.mt/getpdf/661645c07403ed16fcf9eb8e>
[^s17]: Government of Malta – Legislation Malta f699ce2efa. Conduct Certificates Ordinance (Cap. 77). <https://legislation.mt/getpdf/6aa1090e5ca02023e4009067>
[^s18]: Government of Malta – Legislation Malta 875c5523e5. Security Service Act (Cap. 391). <https://legislation.mt/getpdf/6022ba1cbc827214c09ac4a7>
[^s19]: Identità 357a81b8b9. Expatriates Unit – Biometrics and Interim Receipt. <https://identita.gov.mt/expatriates-unit-main-page/noneu-nationals/useful-information/finalising-application-process/biometrics-and-interim-receipt/> ([archived](https://web.archive.org/web/20260606020509/https://identita.gov.mt/expatriates-unit-main-page/noneu-nationals/useful-information/finalising-application-process/biometrics-and-interim-receipt/))
[^s20]: Identità 4f6320b11b. Expatriates Unit. <https://identita.gov.mt/expatriates-unit-main-page/> ([archived](https://web.archive.org/web/20260928102340/https://identita.gov.mt/expatriates-unit-main-page/))
[^s21]: Government of Malta – Legislation Malta 99c0b7a467. Health Act (Cap. 528). <https://legislation.mt/getpdf/677e3ecacc8e8e3d102ff18a>
[^s22]: Legislation Malta 0910929420. FAQs – Leġiżlazzjoni Malta. <https://legislation.mt/Home/FAQList> ([archived](https://web.archive.org/web/20260918104521/https://legislation.mt/Home/FAQList))
[^s23]: Government of Malta – Legislation Malta 7adc09e117. Malta Statistics Authority Act (Cap. 422). <https://legislation.mt/getpdf/6022c0cfbc827214c09b08e1>
