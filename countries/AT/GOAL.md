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
| Government data centres | Yes[^s7][^s8] |
| Government cloud in operation | Yes[^s9][^s10] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Austria described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 9.20 million[^s11] |
| GDP, current prices | 514.3 EUR bn[^s12] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 198.6 EUR/MWh[^s13] |
| Renewables share of electricity | 90.1 %[^s14] |
| Land area | 82 519 km²[^s15] |

## 3. Critical data holdings, by priority

The holdings Austria cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 9 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Zentrales Melderegister (ZMR) - Central Register of Residents[^s16] | Federal Minister of the Interior acts as processor of the ZPR[^s17] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s18] | — | — | — |
| Critical | Breeder document scans (tier 0) | Supporting documents underlying civil status entries are kept by the civil status authority that made the entry (decentralised)[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Facial biometric (tier 0) | Central evidence under § 22b Passport Act holds passport/ID card data including the facial image (lit. j) but not fingerprints (lit. k)[^s18] | *Not yet sourced* | National infrastructure[^s18] | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Elektronischer Identitätsnachweis (E-ID), branded ID Austria[^s6] | Federal Minister of the Interior and the Source PIN Register Authority process E-ID registration data[^s6] | *Not stated in sources* | *Not yet sourced* |
| High | Electoral roll entry (tier 0) | Zentrales Wählerregister (ZeWaeR) - Central Voter Register[^s19] | Federal Minister of the Interior acts as processor of ZeWaeR for each municipality[^s19] | *Not stated in sources* | 6,346,059 persons entitled to vote in the 2024 National Council election[^s20] |
| High | State PKI and qualified trust services (tier 0) | Austrian Country Signing CA (CSCA) operated by the Federal Ministry of the Interior[^s3] | RTR-GmbH compiles and publishes the national trust list[^s21] | *Not stated in sources* | More than 4 million persons use a qualified electronic signature from A-Trust[^s22] |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Identitätsdokumentenregister (IDR) - Identity Document Register[^s4] | *Not yet sourced* | National infrastructure[^s4] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Zentrales Fremdenregister - Central Register of Foreigners (BFA-VG § 26)[^s23] | Federal Minister of the Interior acts as processor of the Central Register of Foreigners[^s23] | *Not stated in sources* | *Not yet measured* |
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

Of the 8 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
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

> Not yet sized. Capacity for Austria will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Austria without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
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

[^s1]: Bundeskanzleramt (RIS) — Sicherheitspolizeigesetz (SPG), consolidated version, § 55. Sicherheitspolizeigesetz (SPG), consolidated version, § 55. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005792> ([archived](https://web.archive.org/web/20260208105744/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005792))
[^s2]: Bundeskanzleramt (RIS) — Informationssicherheitsgesetz (InfoSiG), consolidated…. Informationssicherheitsgesetz (InfoSiG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20001740> ([archived](https://web.archive.org/web/20250823130719/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Gesetzesnummer=20001740&Abfrage=Bundesnormen))
[^s3]: Bundesministerium für Inneres — The Austrian Country Signing CA (CSCA). The Austrian Country Signing CA (CSCA). <https://www.bmi.gv.at/downloads/csca.html> ([archived](https://web.archive.org/web/20260608085339/https://www.bmi.gv.at/downloads/csca.html))
[^s4]: Rechnungshof Österreich — Umstellung von der Bürgerkarte/Handysignatur auf den…, 2023. Umstellung von der Bürgerkarte/Handysignatur auf den elektronischen Identitätsnachweis (E-ID), Reihe Bund 2023/7. <https://www.rechnungshof.gv.at/rh/home/home/2023_7_E-ID.pdf>
[^s5]: Rechnungshof Österreich — Elektronischer Identitätsnachweis: Hohe Abhängigkeit von…, 2023. Elektronischer Identitätsnachweis: Hohe Abhängigkeit von externen Unternehmen. <https://www.rechnungshof.gv.at/rh/home/news/news/news_3/Umstellung_von_Handysignatur_auf_E-ID.html> ([archived](https://web.archive.org/web/20230331220531/https://www.rechnungshof.gv.at/rh/home/news/news/news_3/Umstellung_von_Handysignatur_auf_E-ID.html))
[^s6]: Bundeskanzleramt (RIS) — E-Government-Gesetz (E-GovG), consolidated version. E-Government-Gesetz (E-GovG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003230> ([archived](https://web.archive.org/web/20260414095127/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003230))
[^s7]: Bundesrechenzentrum GmbH — Was wir tun. Was wir tun. <https://www.brz.gv.at/was-wir-tun.html>
[^s8]: Bundeskanzleramt (RIS) — Bundesgesetz über die Bundesrechenzentrum GmbH…. Bundesgesetz über die Bundesrechenzentrum GmbH (BRZ-Gesetz), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001466>
[^s9]: Bundesrechenzentrum GmbH — Geschäftsfelder. Geschäftsfelder. <https://www.brz.gv.at/was-wir-tun/geschaeftsfelder.html> ([archived](https://web.archive.org/web/20250916204831/https://www.brz.gv.at/was-wir-tun/geschaeftsfelder.html))
[^s10]: Bundesrechenzentrum GmbH — Cloud Storage - BRZ GoverDrive. Cloud Storage - BRZ GoverDrive. <https://www.brz.gv.at/was-wir-tun/services-produkte/cloud-storage_brz_goverdrive.html> ([archived](https://web.archive.org/web/20260313144351/https://www.brz.gv.at/was-wir-tun/services-produkte/cloud-storage_brz_goverdrive.html))
[^s11]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s14]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s15]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s16]: Bundeskanzleramt (RIS) — Meldegesetz 1991 (MeldeG), consolidated version. Meldegesetz 1991 (MeldeG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005799>
[^s17]: Bundeskanzleramt (RIS) — Personenstandsgesetz 2013 (PStG 2013), consolidated version. Personenstandsgesetz 2013 (PStG 2013), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008228> ([archived](https://web.archive.org/web/20260407203750/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008228))
[^s18]: Bundeskanzleramt (RIS) — Passgesetz 1992, consolidated version. Passgesetz 1992, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005798> ([archived](https://web.archive.org/web/20260123224358/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005798))
[^s19]: Bundeskanzleramt (RIS) — Wählerevidenzgesetz 2018 (WEviG), consolidated version. Wählerevidenzgesetz 2018 (WEviG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009720> ([archived](https://web.archive.org/web/20260208002104/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Gesetzesnummer=20009720&Abfrage=Bundesnormen))
[^s20]: Bundesministerium für Inneres — Nationalratswahl 2024, 2024. Nationalratswahl 2024. <https://www.bmi.gv.at/412/nationalratswahlen/nationalratswahl_2024/start.html>
[^s21]: Bundeskanzleramt (RIS) — Signatur- und Vertrauensdienstegesetz (SVG),…. Signatur- und Vertrauensdienstegesetz (SVG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009585> ([archived](https://web.archive.org/web/20260211052418/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009585))
[^s22]: A-Trust GmbH — ID Austria | A-Trust. ID Austria | A-Trust. <https://www.a-trust.at/de/produkte/qualifizierte_signaturservices/id_austria/> ([archived](https://web.archive.org/web/20260915130050/https://www.a-trust.at/de/produkte/qualifizierte_signaturservices/id_austria/))
[^s23]: Bundeskanzleramt (RIS) — BFA-Verfahrensgesetz (BFA-VG), consolidated version. BFA-Verfahrensgesetz (BFA-VG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20007944> ([archived](https://web.archive.org/web/20260723072308/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20007944))
