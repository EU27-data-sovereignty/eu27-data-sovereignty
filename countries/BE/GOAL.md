# Belgium: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Belgium could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2] |
| State-controlled national eID | Yes[^s3] |
| Government data centres | *Not yet sourced* |
| Government cloud in operation | *Not yet sourced* |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Belgium described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 11.88 million[^s4] |
| GDP, current prices | 642.0 EUR bn[^s5] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 186.6 EUR/MWh[^s6] |
| Renewables share of electricity | 31.3 %[^s7] |
| Land area | 30 451 km²[^s8] |

## 3. Critical data holdings, by priority

The holdings Belgium cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 7 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Rijksregister van de natuurlijke personen (National Register of Natural Persons), the central database of identification data of all registered persons[^s9] | The National Register is managed by the Directorate-General Identity and Civil Affairs of the FPS Interior[^s10] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | ID-card photos are stored and visible in the National Register[^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s3] | — | — | — |
| Critical | Breeder document scans (tier 0) | DABS: a central database holding all civil status deeds, replacing the municipal and consular registers[^s12] | DABS is governed by a DABS Management Committee responsible for its set-up and management[^s12] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Register van de Identiteitskaarten: a permanent inventory of the identity cards produced and issued in Belgium[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | Belgium Root CA (BRCA), the top of the government CA hierarchy[^s2] | The Belgian authorities are the certification service provider responsible for the Belgium Root CAs[^s2] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Evibel is the internal database of the immigration service, to be replaced by eMigration[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
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
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 6 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 6 |

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

> Not yet sized. Capacity for Belgium will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Belgium without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Authentication audit log (tier 0)
- Electoral roll entry (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Beneficial ownership register (tier 1)
- Vehicle & licensing (tier 1)
- Judicial & criminal justice (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Crisis management and civil protection (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Moniteur belge (copy on etaamb.openjustice.be); numac 1999007004 — Loi du 11 décembre 1998 relative à la classification et…, 1999-05-07. Loi du 11 décembre 1998 relative à la classification et aux habilitations de sécurité. <https://etaamb.openjustice.be/fr/loi-du-11-decembre-1998_n1999007004.html>
[^s2]: Belgian eID PKI repository — Citizen CA Certification Practice Statement (v1.4). Citizen CA Certification Practice Statement (v1.4). <https://repository.eid.belgium.be/downloads/citizen/en/CPS_CitizenCA.pdf>
[^s3]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID | IBZ - FOD Binnenlandse Zaken. eID | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid> ([archived](https://web.archive.org/web/20260617223429/https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid))
[^s4]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s5]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s6]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s7]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s8]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s9]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Rijksregister | IBZ - FOD Binnenlandse Zaken. Rijksregister | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/rijksregister-en-bevolking/rijksregister> ([archived](https://web.archive.org/web/20260911221802/https://www.ibz.rrn.fgov.be/nl/burger/rijksregister-en-bevolking/rijksregister))
[^s10]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Home | IBZ - FOD Binnenlandse Zaken. Home | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl>
[^s11]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID en GDPR | IBZ - FOD Binnenlandse Zaken. eID en GDPR | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid/eid-en-gdpr>
[^s12]: Rijksarchief in België — Het Rijksarchief is vertegenwoordigd in het…, 2023-06-14. Het Rijksarchief is vertegenwoordigd in het beheerscomité van de Databank voor Akten van de Burgerlijke Stand. <https://www.arch.be/index.php?l=nl&m=nieuws&r=alle-nieuwsberichten&a=2023-06-14-het-rijksarchief-is-vertegenwoordigd-in-het-beheerscomite-van-de-databank-voor-akten-van-de-burgerlijke-stand> ([archived](https://web.archive.org/web/20260416001407/https://www.arch.be/index.php?l=nl&m=nieuws&r=alle-nieuwsberichten&a=2023-06-14-het-rijksarchief-is-vertegenwoordigd-in-het-beheerscomite-van-de-databank-voor-akten-van-de-burgerlijke-stand))
[^s13]: Belgisch Staatsblad (copy published by etaamb.openjustice.be) — Koninklijk Besluit van 25/05/2005 tot bepaling van de…, 2005-05-25. Koninklijk Besluit van 25/05/2005 tot bepaling van de personen en instellingen die toegang hebben tot het register van de identiteitskaarten. <https://etaamb.openjustice.be/nl/koninklijk-besluit-van-25-mei-2005_n2005000390.html>
[^s14]: Gegevensbeschermingsautoriteit — Advies nr. 121/2022 van 1 juli 2022, 2022-07-01. Advies nr. 121/2022 van 1 juli 2022. <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-121-2022.pdf> ([archived](https://web.archive.org/web/20220706131107/https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-121-2022.pdf))
