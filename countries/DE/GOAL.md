# Germany: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Germany could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s6][^s7] |
| Government data centres | Yes[^s8][^s9][^s10] |
| Government cloud in operation | Yes[^s11][^s12][^s10] |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Germany described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 83.47 million[^s13] |
| GDP, current prices | 4 529.7 EUR bn[^s14] |
| Public administration employment (NACE O) | 2 915.0 thousand[^s15] |
| Non-household electricity price | 226.4 EUR/MWh[^s16] |
| Renewables share of electricity | 57.9 %[^s17] |
| Land area | 353 260 km²[^s18] |

## 3. Critical data holdings, by priority

The holdings Germany cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Melderegister (population/residence registers) kept by the Meldebehörden[^s19] | The Federal Central Tax Office (BZSt) stores the national personal identification number (Identifikationsnummer) with core identity data for every natural person (Abgabenordnung § 139b(3))[^s20] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | Biometric features may be stored only at the issuing ID-card authorities[^s21] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s21] | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet sourced* | Each Standesamt keeps the birth register (Geburtenregister) and other civil status registers[^s22] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The ID-card register records serial number, revocation password/sum and expiry date[^s23] | A central store of all ID-card serial numbers is permitted only at the card manufacturer, solely to trace the cards[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Wählerverzeichnis (electoral roll)[^s24] | Gemeindebehörden (municipal authorities)[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | Bundeszentralregister (Federal Central Criminal Register)[^s25] | Bundesamt für Justiz (Federal Office of Justice)[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | polizeilicher Informationsverbund zwischen Bund und Ländern (federal-state police information network)[^s26] | Bundeskriminalamt (Federal Criminal Police Office)[^s26] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | BundID is to become the single central citizen account 'DeutschlandID' under the OZG[^s27][^s28] | *Not yet sourced* | National infrastructure[^s28] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | V-PKI provides certificate-based security services to federal and state authorities, municipalities and public institutions[^s4] | *Not yet sourced* | National infrastructure[^s4] | *Not yet measured* |
| High | Residence and migration status (tier 1) | The AZR consists of a general data stock and a separately kept visa file[^s29] | The AZR is kept by BAMF; the Federal Office of Administration (BVA) processes the data on BAMF's behalf[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | ELSTER (ELektronische STeuerERklärung; electronic tax return)[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | ATLAS is the customs IT procedure for automated clearance and monitoring of cross-border goods traffic[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Versichertenverzeichnis (register of insured persons)[^s32] | die Krankenkasse (each statutory health insurance fund)[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Handelsregister (commercial register)[^s33] | die Gerichte (the courts)[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Transparenzregister (transparency register)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Zentrales Fahrzeugregister des Kraftfahrt-Bundesamtes (Central Vehicle Register)[^s35][^s36] | Kraftfahrt-Bundesamt (Federal Motor Transport Authority)[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet sourced* | The BKA is the central national authority operating the national part of the Schengen Information System[^s37] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Nationales Waffenregister (National Firearms Register)[^s38] | Bundesverwaltungsamt (Federal Office of Administration)[^s39] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | automatisierte Verfahren für das Haushalts-, Kassen- und Rechnungswesen des Bundes (automated federal budget, cash and accounting procedure, HKR)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | TARGET (Eurosystem real-time gross settlement payment system)[^s41] | Deutsche Bundesbank[^s42] | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Digitalfunk BOS (nationwide digital radio for public-safety authorities)[^s43] | Bundesanstalt für den Digitalfunk der BOS (BDBOS)[^s43] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | MoWaS is a highly available, hardened system for warning the population in Germany[^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Bundesgesetzblatt (Federal Law Gazette)[^s45] | Bundesamt für Justiz (Federal Office of Justice)[^s46] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | The Bundesarchiv provides the Digital Intermediate Archive of the Federation (DZAB) as a central service to all federal public bodies[^s47] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 26 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
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

> Not yet sized. Capacity for Germany will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Germany without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- Land & property registry (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Bundesamt für Sicherheit in der Informationstechnik (BSI) — Mindeststandard des BSI zur Nutzung externer…, 2022-12. Mindeststandard des BSI zur Nutzung externer Cloud-Dienste, Version 2.1 (NCD.2.2.03 Gerichtsbarkeit). <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_Nutzung_externer_Cloud-Dienste_Version_2_1.pdf?__blob=publicationFile&v=4> ([archived](https://web.archive.org/web/20260701150216/https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_Nutzung_externer_Cloud-Dienste_Version_2_1.pdf?__blob=publicationFile&v=4))
[^s2]: Bundesministerium des Innern und für Heimat — Allgemeine Verwaltungsvorschrift zum materiellen…, 2023-03-13. Allgemeine Verwaltungsvorschrift zum materiellen Geheimschutz (Verschlusssachenanweisung - VSA), § 34. <https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_13032023_SII554001405.htm> ([archived](https://web.archive.org/web/20260928140800/https://www.verwaltungsvorschriften-im-internet.de/bsvwvbund_13032023_SII554001405.htm))
[^s3]: Bundesministerium der Justiz (gesetze-im-internet.de) — Sicherheitsüberprüfungsgesetz (SÜG) § 4 Allgemeine…. Sicherheitsüberprüfungsgesetz (SÜG) § 4 Allgemeine Grundsätze zum Schutz von Verschlusssachen. <https://www.gesetze-im-internet.de/s_g/__4.html> ([archived](https://web.archive.org/web/20250821134415/https://www.gesetze-im-internet.de/s_g/__4.html))
[^s4]: Bundesamt für Sicherheit in der Informationstechnik — Verwaltungs-PKI. Verwaltungs-PKI. <https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Moderner-Staat/Verwaltungs-PKI/verwaltungs-pki_node.html> ([archived](https://web.archive.org/web/20260213021318/https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Moderner-Staat/Verwaltungs-PKI/verwaltungs-pki_node.html))
[^s5]: D-Trust GmbH — Über uns - D-Trust. Über uns - D-Trust. <https://www.d-trust.net/de/ueber-uns> ([archived](https://web.archive.org/web/20260902212705/https://www.d-trust.net/de/ueber-uns))
[^s6]: Bundesdruckerei Gruppe GmbH — Konzern - Bundesdruckerei-Gruppe. Konzern - Bundesdruckerei-Gruppe. <https://www.bundesdruckerei.de/de/konzern> ([archived](https://web.archive.org/web/20260727120331/https://www.bundesdruckerei.de/de/konzern))
[^s7]: Bundesministerium der Justiz (gesetze-im-internet.de) — Personalausweisgesetz (PAuswG) § 4 Eigentum am Ausweis;…. Personalausweisgesetz (PAuswG) § 4 Eigentum am Ausweis; Ausweishersteller; Vergabestelle für Berechtigungszertifikate. <https://www.gesetze-im-internet.de/pauswg/__4.html> ([archived](https://web.archive.org/web/20260309012726/https://www.gesetze-im-internet.de/pauswg/__4.html))
[^s8]: Informationstechnikzentrum Bund (ITZBund) — Informationstechnikzentrum Bund (ITZBund) - Über uns. Informationstechnikzentrum Bund (ITZBund) - Über uns. <https://www.itzbund.de/DE/dasitzbund/ueber-uns/ueber-uns.html> ([archived](https://web.archive.org/web/20260302061921/https://www.itzbund.de/DE/dasitzbund/ueber-uns/ueber-uns.html))
[^s9]: Informationstechnikzentrum Bund (ITZBund) — Hosting und Betrieb - Die Rechenzentren des ITZBund. Hosting und Betrieb - Die Rechenzentren des ITZBund. <https://www.itzbund.de/DE/leistungsportfolio/hostingundbetrieb/hostingundbetrieb.html> ([archived](https://web.archive.org/web/20260223163818/https://www.itzbund.de/DE/leistungsportfolio/hostingundbetrieb/hostingundbetrieb.html))
[^s10]: Informationstechnikzentrum Bund (ITZBund) — ITZBund - Facts & Figures 2024, 2025. ITZBund - Facts & Figures 2024. <https://www.itzbund.de/Webs/GB2024/DE/home/home_node.html?__site=GB2024> ([archived](https://web.archive.org/web/20251029102820/https://www.itzbund.de/Webs/GB2024/DE/home/home_node.html?__site=GB2024))
[^s11]: IT-Planungsrat — Digitalisierung der Verwaltung: Deutsche…, 2025-03-27. Digitalisierung der Verwaltung: Deutsche Verwaltungscloud startet in den Produktivbetrieb. <https://www.it-planungsrat.de/aktuelles/details/digitalisierung-der-verwaltung-deutsche-verwaltungscloud-startet-in-den-produktivbetrieb>
[^s12]: Informationstechnikzentrum Bund (ITZBund) — Die Bundescloud – eine exklusive, private Cloud für die…. Die Bundescloud – eine exklusive, private Cloud für die Bundesverwaltung. <https://www.itzbund.de/DE/itloesungen/egovernment/bundescloud/bundescloud.html> ([archived](https://web.archive.org/web/20260708195922/https://www.itzbund.de/DE/itloesungen/egovernment/bundescloud/bundescloud.html))
[^s13]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s14]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s15]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s16]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s17]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s18]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s19]: Bundesministerium der Justiz / gesetze-im-internet.de — § 2 BMG - Aufgaben und Befugnisse der Meldebehörden. § 2 BMG - Aufgaben und Befugnisse der Meldebehörden. <https://www.gesetze-im-internet.de/bmg/__2.html> ([archived](https://web.archive.org/web/20260102165107/https://www.gesetze-im-internet.de/bmg/__2.html))
[^s20]: Bundesministerium der Justiz / gesetze-im-internet.de — § 139b AO - Identifikationsnummer. § 139b AO - Identifikationsnummer. <https://www.gesetze-im-internet.de/ao_1977/__139b.html> ([archived](https://web.archive.org/web/20260227090600/https://www.gesetze-im-internet.de/ao_1977/__139b.html))
[^s21]: Bundesministerium der Justiz / gesetze-im-internet.de — § 26 PAuswG - Sonstige Speicherung personenbezogener Daten. § 26 PAuswG - Sonstige Speicherung personenbezogener Daten. <https://www.gesetze-im-internet.de/pauswg/__26.html> ([archived](https://web.archive.org/web/20251117090709/https://www.gesetze-im-internet.de/pauswg/__26.html))
[^s22]: Bundesministerium der Justiz / gesetze-im-internet.de — § 3 PStG - Personenstandsregister. § 3 PStG - Personenstandsregister. <https://www.gesetze-im-internet.de/pstg/__3.html>
[^s23]: Bundesministerium der Justiz / gesetze-im-internet.de — § 23 PAuswG - Personalausweisregister. § 23 PAuswG - Personalausweisregister. <https://www.gesetze-im-internet.de/pauswg/__23.html> ([archived](https://web.archive.org/web/20251009222823/https://www.gesetze-im-internet.de/pauswg/__23.html))
[^s24]: Bundesamt für Justiz (gesetze-im-internet.de) — Bundeswahlgesetz § 17. Bundeswahlgesetz § 17. <https://www.gesetze-im-internet.de/bwahlg/__17.html> ([archived](https://web.archive.org/web/20260113161029/https://www.gesetze-im-internet.de/bwahlg/__17.html))
[^s25]: Bundesamt für Justiz (gesetze-im-internet.de) — Bundeszentralregistergesetz § 1. Bundeszentralregistergesetz § 1. <https://www.gesetze-im-internet.de/bzrg/__1.html> ([archived](https://web.archive.org/web/20251225083011/https://www.gesetze-im-internet.de/bzrg/__1.html))
[^s26]: Bundesamt für Justiz (gesetze-im-internet.de) — Bundeskriminalamtgesetz § 29. Bundeskriminalamtgesetz § 29. <https://www.gesetze-im-internet.de/bkag_2018/__29.html> ([archived](https://web.archive.org/web/20260908002421/https://www.gesetze-im-internet.de/bkag_2018/__29.html))
[^s27]: Bundesministerium der Justiz / Bundesamt für Justiz (gesetze-im-internet.de) — Onlinezugangsgesetz (OZG) § 3. Onlinezugangsgesetz (OZG) § 3. <https://www.gesetze-im-internet.de/ozg/__3.html> ([archived](https://web.archive.org/web/20260213222849/https://www.gesetze-im-internet.de/ozg/__3.html))
[^s28]: Land Brandenburg, OZG-Portal — BundID (Nutzerkonto) - DeutschlandID. BundID (Nutzerkonto) - DeutschlandID. <https://ozg.brandenburg.de/ozg/de/it-infrastrukturen/it-basiskomponenten/bundid-nutzerkonto-deutschlandid/>
[^s29]: Bundesministerium der Justiz / gesetze-im-internet.de — § 1 AZR-Gesetz. § 1 AZR-Gesetz. <https://www.gesetze-im-internet.de/azrg/__1.html> ([archived](https://web.archive.org/web/20250215034909/https://www.gesetze-im-internet.de/azrg/__1.html))
[^s30]: Bayerisches Landesamt für Steuern — ELSTER - Bayerisches Landesamt für Steuern. ELSTER - Bayerisches Landesamt für Steuern. <https://www.lfst.bayern.de/elster> ([archived](https://web.archive.org/web/20260725175431/https://www.lfst.bayern.de/elster))
[^s31]: Generalzolldirektion (Zoll online) — ATLAS. ATLAS. <https://www.zoll.de/DE/Fachthemen/Zoelle/ATLAS/atlas_node.html> ([archived](https://web.archive.org/web/20260618015312/https://www.zoll.de/DE/Fachthemen/Zoelle/ATLAS/atlas_node.html))
[^s32]: Bundesamt für Justiz (gesetze-im-internet.de) — SGB V § 288 Versichertenverzeichnis. SGB V § 288 Versichertenverzeichnis. <https://www.gesetze-im-internet.de/sgb_5/__288.html> ([archived](https://web.archive.org/web/20260329171945/https://www.gesetze-im-internet.de/sgb_5/__288.html))
[^s33]: Bundesamt für Justiz (gesetze-im-internet.de) — Handelsgesetzbuch § 8. Handelsgesetzbuch § 8. <https://www.gesetze-im-internet.de/hgb/__8.html> ([archived](https://web.archive.org/web/20260128064431/https://www.gesetze-im-internet.de/hgb/__8.html))
[^s34]: Bundesamt für Justiz (gesetze-im-internet.de) — Geldwäschegesetz § 18. Geldwäschegesetz § 18. <https://www.gesetze-im-internet.de/gwg_2017/__18.html> ([archived](https://web.archive.org/web/20241226225736/https://www.gesetze-im-internet.de/gwg_2017/__18.html))
[^s35]: Bundesamt für Justiz (gesetze-im-internet.de) — Straßenverkehrsgesetz § 48. Straßenverkehrsgesetz § 48. <https://www.gesetze-im-internet.de/stvg/__48.html> ([archived](https://web.archive.org/web/20250219144555/https://www.gesetze-im-internet.de/stvg/__48.html))
[^s36]: Bundesamt für Justiz (gesetze-im-internet.de) — Straßenverkehrsgesetz § 31. Straßenverkehrsgesetz § 31. <https://www.gesetze-im-internet.de/stvg/__31.html> ([archived](https://web.archive.org/web/20251117061329/https://www.gesetze-im-internet.de/stvg/__31.html))
[^s37]: Bundesministerium der Justiz / gesetze-im-internet.de — § 3 BKAG. § 3 BKAG. <https://www.gesetze-im-internet.de/bkag_2018/__3.html> ([archived](https://web.archive.org/web/20260227115654/https://www.gesetze-im-internet.de/bkag_2018/__3.html))
[^s38]: Bundesamt für Justiz (gesetze-im-internet.de) — Waffenregistergesetz § 1. Waffenregistergesetz § 1. <https://www.gesetze-im-internet.de/waffrg/__1.html> ([archived](https://web.archive.org/web/20240806132426/https://www.gesetze-im-internet.de/waffrg/__1.html))
[^s39]: Bundesamt für Justiz (gesetze-im-internet.de) — Waffenregistergesetz § 3 Registerbehörde. Waffenregistergesetz § 3 Registerbehörde. <https://www.gesetze-im-internet.de/waffrg/__3.html> ([archived](https://web.archive.org/web/20240806134530/https://www.gesetze-im-internet.de/waffrg/__3.html))
[^s40]: Zentrum für Finanzen des Bundes (ZFB) / Bundeskasse (zrb.bund.de) — HKR-Verfahren. HKR-Verfahren. <https://zrb.bund.de/vorschriften/hkr-verfahren>
[^s41]: Deutsche Bundesbank — TARGET - Der Entwicklungsprozess. TARGET - Der Entwicklungsprozess. <https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/target/target-603342> ([archived](https://web.archive.org/web/20260724075900/https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/target/target-603342))
[^s42]: Bundesamt für Justiz (gesetze-im-internet.de) — Gesetz über die Deutsche Bundesbank § 3. Gesetz über die Deutsche Bundesbank § 3. <https://www.gesetze-im-internet.de/bbankg/__3.html> ([archived](https://web.archive.org/web/20241206140449/https://www.gesetze-im-internet.de/bbankg/__3.html))
[^s43]: Bundesamt für Justiz (gesetze-im-internet.de) — BDBOS-Gesetz § 1. BDBOS-Gesetz § 1. <https://www.gesetze-im-internet.de/bdbosg/__1.html> ([archived](https://web.archive.org/web/20211207215735/https://www.gesetze-im-internet.de/bdbosg/__1.html))
[^s44]: Bundesamt für Bevölkerungsschutz und Katastrophenhilfe — MoWaS. MoWaS. <https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/MoWaS/mowas_node.html> ([archived](https://web.archive.org/web/20260924105236/https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/MoWaS/mowas_node.html))
[^s45]: Bundesamt für Justiz (gesetze-im-internet.de) — Verkündungs- und Bekanntmachungsgesetz § 1. Verkündungs- und Bekanntmachungsgesetz § 1. <https://www.gesetze-im-internet.de/vkbkmg/__1.html>
[^s46]: Bundesamt für Justiz (gesetze-im-internet.de) — Verkündungs- und Bekanntmachungsgesetz § 2. Verkündungs- und Bekanntmachungsgesetz § 2. <https://www.gesetze-im-internet.de/vkbkmg/__2.html> ([archived](https://web.archive.org/web/20260113175356/https://www.gesetze-im-internet.de/vkbkmg/__2.html))
[^s47]: Bundesarchiv — Nutzung des Digitalen Zwischenarchivs (DZAB). Nutzung des Digitalen Zwischenarchivs (DZAB). <https://www.bundesarchiv.de/unterlagen-abgeben/behoerdenberatung-zu-schriftgut-und-informationsverwaltung/nutzung-des-digitalen-zwischenarchivs-dzab/> ([archived](https://web.archive.org/web/20260618022322/https://www.bundesarchiv.de/unterlagen-abgeben/behoerdenberatung-zu-schriftgut-und-informationsverwaltung/nutzung-des-digitalen-zwischenarchivs-dzab/))

**Evidence grades:** 0 Strong, 52 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
