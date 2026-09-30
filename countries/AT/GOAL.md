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
| Population | 9.22 million[^s13] |
| GDP, current prices | 514.3 EUR bn[^s14] |
| Public administration employment (NACE O) | 280.5 thousand[^s15] |
| Non-household electricity price | 198.6 EUR/MWh[^s16] |
| Renewables share of electricity | 90.8 %[^s17] |
| Land area | 82 494 km²[^s18] |

## 3. Critical data holdings, by priority

The holdings Austria cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 31 of 39 holding classes have a verified source; 5 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Zentrales Melderegister (ZMR) - Central Register of Residents[^s19] | Federal Minister of the Interior acts as processor of the ZPR[^s20][^s21] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s22][^s23] | — | — | — |
| Critical | Breeder document scans (tier 0) | Supporting documents underlying civil status entries are kept by the civil status authority that made the entry (decentralised)[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Facial biometric (tier 0) | Central evidence under § 22b Passport Act holds passport/ID card data including the facial image (lit. j) but not fingerprints (lit. k)[^s23] | *Not yet sourced* | National infrastructure[^s23] | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Elektronischer Identitätsnachweis (E-ID), branded ID Austria[^s24][^s6] | Federal Minister of the Interior and the Source PIN Register Authority process E-ID registration data[^s6] | *Not stated in sources* | *Not yet sourced* |
| High | Electoral roll entry (tier 0) | Zentrales Wählerregister (ZeWaeR) - Central Voter Register[^s25] | Federal Minister of the Interior acts as processor of ZeWaeR for each municipality[^s25] | *Not stated in sources* | 6,346,059 persons entitled to vote in the 2024 National Council election[^s26] |
| High | State PKI and qualified trust services (tier 0) | Austrian Country Signing CA (CSCA) operated by the Federal Ministry of the Interior[^s3] | RTR-GmbH compiles and publishes the national trust list[^s27][^s28] | *Not stated in sources* | fast 6,3 Millionen ID Austria-Registrierungen (almost 6.3 million ID Austria registrations) as of 1 September 2026[^s29] |
| High | Land & property registry (tier 1) | Grundbuch (land register)[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Strafregister (criminal record register)[^s31] | Landespolizeidirektion Wien (Vienna Provincial Police Directorate)[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | PAD - Protokollieren Anzeigen Daten (police case and report logging system)[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | Datenverarbeitung mittels operativer oder strategischer Analyse (state-protection analysis data processing, jointly controlled by the Federal Minister of the Interior and the provincial police directorates)[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Identitätsdokumentenregister (IDR) - Identity Document Register[^s34][^s4] | *Not yet sourced* | National infrastructure[^s4][^s23] | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Disputed: sources disagree. Bundeskanzleramt (RIS) — BFA-Verfahrensgesetz (BFA-VG), consolidated version gives the value this report printed; Bundesministerium für Inneres — Information zu der Verarbeitung „Zentrales Fremdenregister“ gives “Zentrales Fremdenregister (Central Register of Foreigners)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | Federal Minister of the Interior acts as processor of the Central Register of Foreigners[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | FinanzOnline[^s36] | Bundesrechenzentrum GmbH (BRZ) for the Bundesministerium für Finanzen (Federal Computing Centre, for the Federal Ministry of Finance)[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | e-zoll (electronic customs)[^s37] | *Not yet sourced* | *Not stated in sources* | mehr als 4,5 Mio. Zollanmeldungen pro Jahr (more than 4,5 million customs declarations per year)[^s37] |
| High | Benefits & pensions (tier 1) | Pensionskonto (pension account)[^s38] | Dachverband der Sozialversicherungsträger (Umbrella Association of Austrian Social Insurance Institutions)[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Elektronisches Verwaltungssystem (ELSY) (electronic administration system, the e-card system)[^s39] | Dachverband (der Sozialversicherungsträger) (Umbrella Association of Social Insurance Institutions)[^s39] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Firmenbuch (companies register)[^s30] | BRZ (Bundesrechenzentrum GmbH) for the Justizministerium (Federal Computing Centre for the Ministry of Justice)[^s30] | *Not stated in sources* | etwa 545.000 Firmen (about 545,000 companies)[^s30] |
| High | Beneficial ownership register (tier 1) | Register der wirtschaftlichen Eigentümer (Register of Beneficial Owners)[^s40] | WiEReG–Registerbehörde im Bundesministerium für Finanzen (WiEReG register authority in the Federal Ministry of Finance)[^s40] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Zentrale Zulassungsevidenz - Kraftfahrzeugzentralregister (KZR) (Central Motor Vehicle Register)[^s41] | Bundesminister für Inneres (Federal Minister of the Interior)[^s41] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Nationales Schengener Informationssystem (N-SIS II) (National Schengen Information System)[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Zentrales Waffenregister (Central Weapons Register)[^s43] | Bundesminister für Inneres as processor, with IBM Österreich Internationale Büromaschinen GmbH, Microsoft Österreich GmbH and Bundesrechenzentrum GmbH as further processors[^s43] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Haushaltsverrechnungssystem HV-SAP (federal budget accounting system)[^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Personalverrechnungssystem PM-SAP (federal payroll system)[^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | Modulares Wahlpaket (modular election package)[^s45] | Bundeswahlbehörde p.A. Bundesministerium für Inneres (Federal Electoral Board, c/o Federal Ministry of the Interior)[^s45] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET Services (RTGS, TIPS, T2S, CLM)[^s46] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | BOS-Digitalfunk, österreichweites Digitalfunksystem für Behörden und Organisationen mit Sicherheitsaufgaben (nationwide public-safety digital radio system)[^s47] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Bundeslagezentrum (Federal Situation Centre)[^s48] | Bundesministerium für Inneres (Federal Ministry of the Interior)[^s48] | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | APG-Steuerzentrale, Power Grid Control (APG control centre)[^s49] | APG (Austrian Power Grid AG)[^s49] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Gesamtevidenz der Schülerinnen und Schüler (national overall register of pupils)[^s50] | Bundesanstalt „Statistik Österreich“ (Statistics Austria), as processor[^s50] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Rechtsinformationssystem des Bundes (RIS) (Federal Legal Information System)[^s51] | Bundeskanzler (Federal Chancellor / Federal Chancellery)[^s51] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

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

---

[^s1]: Bundeskanzleramt (RIS) — Sicherheitspolizeigesetz (SPG), consolidated version, § 55. Sicherheitspolizeigesetz (SPG), consolidated version, § 55. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005792> ([archived](https://web.archive.org/web/20260208105744/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005792))
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
[^s22]: Bundesministerium für Inneres — Information zu der Verarbeitung „Erkennungsdienstliche…. Information zu der Verarbeitung „Erkennungsdienstliche Evidenz-EDE“. <https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_erkennungsdienstliche_evidenz-ede_v3.pdf> ([archived](https://web.archive.org/web/20260508140958/https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_erkennungsdienstliche_evidenz-ede_v3.pdf))
[^s23]: Bundeskanzleramt (RIS) — Passgesetz 1992, consolidated version, 2026-09-30. Passgesetz 1992, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005798> ([archived](https://web.archive.org/web/20260123224358/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005798))
[^s24]: Bundesrechenzentrum GmbH (BRZ) — ID Austria. ID Austria. <https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html> ([archived](https://web.archive.org/web/20260610144149/https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html))
[^s25]: Bundeskanzleramt (RIS) — Wählerevidenzgesetz 2018 (WEviG), consolidated version. Wählerevidenzgesetz 2018 (WEviG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009720> ([archived](https://web.archive.org/web/20260208002104/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Gesetzesnummer=20009720&Abfrage=Bundesnormen))
[^s26]: Bundesministerium für Inneres — Nationalratswahl 2024, 2024. Nationalratswahl 2024. <https://www.bmi.gv.at/412/nationalratswahlen/nationalratswahl_2024/start.html>
[^s27]: Bundeskanzleramt (RIS) — Signatur- und Vertrauensdienstegesetz (SVG),…. Signatur- und Vertrauensdienstegesetz (SVG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009585> ([archived](https://web.archive.org/web/20260211052418/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009585))
[^s28]: Rundfunk und Telekom Regulierungs-GmbH (RTR) — Vertrauensliste der beaufsichtigten…. Vertrauensliste der beaufsichtigten Vertrauensdiensteanbieter. <https://www.rtr.at/TKP/was_wir_tun/vertrauensdienste/Signatur/vertrauensliste/VertrListe.de.html> ([archived](https://web.archive.org/web/20260908033759/https://www.rtr.at/TKP/was_wir_tun/vertrauensdienste/Signatur/vertrauensliste/VertrListe.de.html))
[^s29]: Bundeskanzleramt Österreich — Pröll: 6,3 Millionen ausgestellte "ID Austria" nach…, 2026-09-08. Pröll: 6,3 Millionen ausgestellte "ID Austria" nach erfolgreicher ID Austria Servicetour. <https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/09/proell-6-3-millionen-ausgestellte-id-austria-nach-erfolgreicher-id-austria-servicetour.html>
[^s30]: Bundesrechenzentrum GmbH (BRZ) — Registerlösungen wie Grundbuch und Firmenbuch. Registerlösungen wie Grundbuch und Firmenbuch. <https://www.brz.gv.at/was-wir-tun/services-produkte/registerloesungen.html> ([archived](https://web.archive.org/web/20260519193214/https://www.brz.gv.at/was-wir-tun/services-produkte/registerloesungen.html))
[^s31]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Strafregistergesetz 1968, consolidated version, 2026-09-30. Strafregistergesetz 1968, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002116> ([archived](https://web.archive.org/web/20251105105153/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002116))
[^s32]: Bundesministerium für Inneres — Information zu der Verarbeitung „PAD - Protokollieren…. Information zu der Verarbeitung „PAD - Protokollieren Anzeigen Daten“. <https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_pad-protkollieren_anzeigen_daten_v2.pdf> ([archived](https://web.archive.org/web/20260508105548/https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_pad-protkollieren_anzeigen_daten_v2.pdf))
[^s33]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Staatsschutz- und Nachrichtendienst-Gesetz (SNG),…. Staatsschutz- und Nachrichtendienst-Gesetz (SNG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009486> ([archived](https://web.archive.org/web/20251211035839/https://www.ris.bka.gv.at/geltendefassung.wxe?abfrage=bundesnormen&gesetzesnummer=20009486))
[^s34]: Landespolizeidirektion Burgenland (Bundespolizei) — Information zu der Verarbeitung „Zentrales…, 2021-01. Information zu der Verarbeitung „Zentrales Identitätsdokumentenregister (IDR)“. <https://www.polizei.gv.at/bgld/files_bgld/datenschutz/2023/zentrales_identitaetsdokumentenregister_idr_012023_bf.pdf> ([archived](https://web.archive.org/web/20241125081919/https://www.polizei.gv.at/BGLD/files_bgld/datenschutz/2023/Zentrales_Identitaetsdokumentenregister_IDR_012023_bf.pdf))
[^s35]: Bundeskanzleramt (RIS) — BFA-Verfahrensgesetz (BFA-VG), consolidated version. BFA-Verfahrensgesetz (BFA-VG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20007944> ([archived](https://web.archive.org/web/20260723072308/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20007944))
[^s36]: Bundesrechenzentrum GmbH (BRZ) — FinanzOnline. FinanzOnline. <https://www.brz.gv.at/was-wir-tun/services-produkte/finanzonline.html> ([archived](https://web.archive.org/web/20260516205141/https://www.brz.gv.at/was-wir-tun/services-produkte/finanzonline.html))
[^s37]: Bundesrechenzentrum GmbH (BRZ) — e-zoll. e-zoll. <https://www.brz.gv.at/was-wir-tun/services-produkte/e-zoll.html> ([archived](https://web.archive.org/web/20260519182925/https://www.brz.gv.at/was-wir-tun/services-produkte/e-zoll.html))
[^s38]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Allgemeines Pensionsgesetz § 10. Allgemeines Pensionsgesetz § 10. <https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003831&Paragraf=10>
[^s39]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Allgemeines Sozialversicherungsgesetz § 31a, 2026-01-01. Allgemeines Sozialversicherungsgesetz § 31a. <https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=31a> ([archived](https://web.archive.org/web/20260612022848/https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=31a))
[^s40]: Bundesministerium für Finanzen — Register der wirtschaftlichen Eigentümer. Register der wirtschaftlichen Eigentümer. <https://www.bmf.gv.at/services/wiereg.html> ([archived](https://web.archive.org/web/20260723020928/https://www.bmf.gv.at/services/wiereg.html))
[^s41]: Bundesministerium für Inneres — Information zu der Verarbeitung „Zentrale…. Information zu der Verarbeitung „Zentrale Zulassungsevidenz - Kraftfahrzeugzentralregister (KZR)“. <https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_zentrale_zulassungsevidenz-kraftfahrzeugzentralregister-kzr_v2.pdf> ([archived](https://web.archive.org/web/20260508152304/https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_zentrale_zulassungsevidenz-kraftfahrzeugzentralregister-kzr_v2.pdf))
[^s42]: Bundesministerium für Inneres — Information zu der Verarbeitung „Nationales Schengener…. Information zu der Verarbeitung „Nationales Schengener Informationssystem (N-SIS II)“. <https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_nationales_schengener_informationssystem-n-sis_ii_v2.pdf> ([archived](https://web.archive.org/web/20260508105448/https://www.bmi.gv.at/402/files/informationen/sektion_ii/bf_nationales_schengener_informationssystem-n-sis_ii_v2.pdf))
[^s43]: Landespolizeidirektion Steiermark (Bundespolizei) — Information zu der gemeinsamen Verarbeitung „Zentrales…, 2020-02-24. Information zu der gemeinsamen Verarbeitung „Zentrales Waffenregister“. <https://www.polizei.gv.at/stmk/files_stmk/datenschutz/2020/BF_Zentrales%20Waffenregister_20200224.pdf> ([archived](https://web.archive.org/web/20260505131709/https://www.polizei.gv.at/stmk/files_stmk/datenschutz/2020/bf_zentrales%20waffenregister_20200224.pdf))
[^s44]: Rechnungshof Österreich — Bundesrechnungsabschluss für das Jahr 2024, Textteil Band 4, 2025. Bundesrechnungsabschluss für das Jahr 2024, Textteil Band 4. <https://rechnungshof.gv.at/rh/home/home_1/home_9/BRA_2024_Band_4.pdf>
[^s45]: Bundeswahlbehörde / Bundesministerium für Inneres — Information zu der Verarbeitung Modulares Wahlpaket, 2025-04-10. Information zu der Verarbeitung Modulares Wahlpaket. <https://www.bmi.gv.at/402/files/informationen/wahlen/informationsblatt_modulares_wahlpaket_bf_20250410.pdf> ([archived](https://web.archive.org/web/20260616054805/https://www.bmi.gv.at/402/files/informationen/wahlen/informationsblatt_modulares_wahlpaket_bf_20250410.pdf))
[^s46]: Oesterreichische Nationalbank (OeNB) — TARGET Services. TARGET Services. <https://www.oenb.at/Zahlungsverkehr/target-services.html> ([archived](https://web.archive.org/web/20260312220131/https://www.oenb.at/Zahlungsverkehr/target-services.html))
[^s47]: Bundesministerium für Inneres — Abteilung IV/DDS/12 (Kritische…. Abteilung IV/DDS/12 (Kritische Kommunikationsinfrastrukturen). <https://www.bmi.gv.at/113/Sektion_IV/Gruppe_IV_DDS/CTO/Abteilung_IV_DDS_12/start.aspx>
[^s48]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Bundes-Krisensicherheitsgesetz (B-KSG), consolidated version. Bundes-Krisensicherheitsgesetz (B-KSG), consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20012321>
[^s49]: Austrian Power Grid AG (APG) — Steuerzentrale. Steuerzentrale. <https://www.apg.at/ueber-uns/steuerzentrale/> ([archived](https://web.archive.org/web/20260522164325/https://www.apg.at/ueber-uns/steuerzentrale/))
[^s50]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Bildungsdokumentationsgesetz 2020, consolidated version. Bildungsdokumentationsgesetz 2020, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011451> ([archived](https://web.archive.org/web/20260730015701/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011451))
[^s51]: Bundeskanzleramt – Rechtsinformationssystem des Bundes (RIS) — Bundesgesetzblattgesetz, consolidated version, 2026-09-30. Bundesgesetzblattgesetz, consolidated version. <https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002988> ([archived](https://web.archive.org/web/20230506214536/https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002988))

**Evidence grades:** 4 Strong, 61 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
