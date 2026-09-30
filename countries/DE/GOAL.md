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
| Jurisdiction requirement | Partly[^s1] |
| Classification in law | Yes[^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4] |
| State-controlled national eID | Yes[^s5][^s6] |
| Government data centres | Yes[^s7][^s8] |
| Government cloud in operation | Yes[^s9] |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Germany described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 83.58 million[^s10] |
| GDP, current prices | 4 529.7 EUR bn[^s11] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 226.4 EUR/MWh[^s12] |
| Renewables share of electricity | 54.1 %[^s13] |
| Land area | 353 296 km²[^s14] |

## 3. Critical data holdings, by priority

The holdings Germany cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 14 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Melderegister (population/residence registers) kept by the Meldebehörden[^s15] | The Federal Central Tax Office (BZSt) stores the national personal identification number (Identifikationsnummer) with core identity data for every natural person (Abgabenordnung § 139b(3))[^s16] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | Biometric features may be stored only at the issuing ID-card authorities[^s17] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s17] | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet sourced* | Each Standesamt keeps the birth register (Geburtenregister) and other civil status registers[^s18] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The ID-card register records serial number, revocation password/sum and expiry date[^s19] | A central store of all ID-card serial numbers is permitted only at the card manufacturer, solely to trace the cards[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | BundID is to become the single central citizen account 'DeutschlandID' under the OZG[^s20] | *Not yet sourced* | National infrastructure[^s20] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | V-PKI provides certificate-based security services to federal and state authorities, municipalities and public institutions[^s3] | *Not yet sourced* | National infrastructure[^s3] | *Not yet measured* |
| High | Residence and migration status (tier 1) | The AZR consists of a general data stock and a separately kept visa file[^s21] | The AZR is kept by BAMF; the Federal Office of Administration (BVA) processes the data on BAMF's behalf[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | ATLAS is the customs IT procedure for automated clearance and monitoring of cross-border goods traffic[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | *Not yet sourced* | The BKA is the central national authority operating the national part of the Schengen Information System[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | MoWaS is a highly available, hardened system for warning the population in Germany[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | The Bundesarchiv provides the Digital Intermediate Archive of the Federation (DZAB) as a central service to all federal public bodies[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 13 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 11 |

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
- Electoral roll entry (tier 0)
- Tax (tier 1)
- Statutory health insurance (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Beneficial ownership register (tier 1)
- Vehicle & licensing (tier 1)
- Judicial & criminal justice (tier 1)
- Police information systems (tier 1)
- Firearms register (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Bundesamt für Sicherheit in der Informationstechnik (BSI) — Mindeststandard des BSI zur Nutzung externer…, 2022-12. Mindeststandard des BSI zur Nutzung externer Cloud-Dienste, Version 2.1 (NCD.2.2.03 Gerichtsbarkeit). <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_Nutzung_externer_Cloud-Dienste_Version_2_1.pdf?__blob=publicationFile&v=4> ([archived](https://web.archive.org/web/20260701150216/https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_Nutzung_externer_Cloud-Dienste_Version_2_1.pdf?__blob=publicationFile&v=4))
[^s2]: Bundesministerium der Justiz (gesetze-im-internet.de) — Sicherheitsüberprüfungsgesetz (SÜG) § 4 Allgemeine…. Sicherheitsüberprüfungsgesetz (SÜG) § 4 Allgemeine Grundsätze zum Schutz von Verschlusssachen. <https://www.gesetze-im-internet.de/s_g/__4.html> ([archived](https://web.archive.org/web/20250821134415/https://www.gesetze-im-internet.de/s_g/__4.html))
[^s3]: Bundesamt für Sicherheit in der Informationstechnik — Verwaltungs-PKI. Verwaltungs-PKI. <https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Moderner-Staat/Verwaltungs-PKI/verwaltungs-pki_node.html> ([archived](https://web.archive.org/web/20260213021318/https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Moderner-Staat/Verwaltungs-PKI/verwaltungs-pki_node.html))
[^s4]: D-Trust GmbH — Über uns - D-Trust. Über uns - D-Trust. <https://www.d-trust.net/de/ueber-uns> ([archived](https://web.archive.org/web/20260902212705/https://www.d-trust.net/de/ueber-uns))
[^s5]: Bundesdruckerei Gruppe GmbH — Konzern - Bundesdruckerei-Gruppe. Konzern - Bundesdruckerei-Gruppe. <https://www.bundesdruckerei.de/de/konzern> ([archived](https://web.archive.org/web/20260727120331/https://www.bundesdruckerei.de/de/konzern))
[^s6]: Bundesministerium der Justiz (gesetze-im-internet.de) — Personalausweisgesetz (PAuswG) § 4 Eigentum am Ausweis;…. Personalausweisgesetz (PAuswG) § 4 Eigentum am Ausweis; Ausweishersteller; Vergabestelle für Berechtigungszertifikate. <https://www.gesetze-im-internet.de/pauswg/__4.html> ([archived](https://web.archive.org/web/20260309012726/https://www.gesetze-im-internet.de/pauswg/__4.html))
[^s7]: Informationstechnikzentrum Bund (ITZBund) — Informationstechnikzentrum Bund (ITZBund) - Über uns. Informationstechnikzentrum Bund (ITZBund) - Über uns. <https://www.itzbund.de/DE/dasitzbund/ueber-uns/ueber-uns.html> ([archived](https://web.archive.org/web/20260302061921/https://www.itzbund.de/DE/dasitzbund/ueber-uns/ueber-uns.html))
[^s8]: Informationstechnikzentrum Bund (ITZBund) — Hosting und Betrieb - Die Rechenzentren des ITZBund. Hosting und Betrieb - Die Rechenzentren des ITZBund. <https://www.itzbund.de/DE/leistungsportfolio/hostingundbetrieb/hostingundbetrieb.html> ([archived](https://web.archive.org/web/20260223163818/https://www.itzbund.de/DE/leistungsportfolio/hostingundbetrieb/hostingundbetrieb.html))
[^s9]: Informationstechnikzentrum Bund (ITZBund) — Die Bundescloud – eine exklusive, private Cloud für die…. Die Bundescloud – eine exklusive, private Cloud für die Bundesverwaltung. <https://www.itzbund.de/DE/itloesungen/egovernment/bundescloud/bundescloud.html> ([archived](https://web.archive.org/web/20260708195922/https://www.itzbund.de/DE/itloesungen/egovernment/bundescloud/bundescloud.html))
[^s10]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s11]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s12]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s13]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s14]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s15]: Bundesministerium der Justiz / gesetze-im-internet.de — § 2 BMG - Aufgaben und Befugnisse der Meldebehörden. § 2 BMG - Aufgaben und Befugnisse der Meldebehörden. <https://www.gesetze-im-internet.de/bmg/__2.html> ([archived](https://web.archive.org/web/20260102165107/https://www.gesetze-im-internet.de/bmg/__2.html))
[^s16]: Bundesministerium der Justiz / gesetze-im-internet.de — § 139b AO - Identifikationsnummer. § 139b AO - Identifikationsnummer. <https://www.gesetze-im-internet.de/ao_1977/__139b.html> ([archived](https://web.archive.org/web/20260227090600/https://www.gesetze-im-internet.de/ao_1977/__139b.html))
[^s17]: Bundesministerium der Justiz / gesetze-im-internet.de — § 26 PAuswG - Sonstige Speicherung personenbezogener Daten. § 26 PAuswG - Sonstige Speicherung personenbezogener Daten. <https://www.gesetze-im-internet.de/pauswg/__26.html> ([archived](https://web.archive.org/web/20251117090709/https://www.gesetze-im-internet.de/pauswg/__26.html))
[^s18]: Bundesministerium der Justiz / gesetze-im-internet.de — § 3 PStG - Personenstandsregister. § 3 PStG - Personenstandsregister. <https://www.gesetze-im-internet.de/pstg/__3.html>
[^s19]: Bundesministerium der Justiz / gesetze-im-internet.de — § 23 PAuswG - Personalausweisregister. § 23 PAuswG - Personalausweisregister. <https://www.gesetze-im-internet.de/pauswg/__23.html> ([archived](https://web.archive.org/web/20251009222823/https://www.gesetze-im-internet.de/pauswg/__23.html))
[^s20]: Land Brandenburg, OZG-Portal — BundID (Nutzerkonto) - DeutschlandID. BundID (Nutzerkonto) - DeutschlandID. <https://ozg.brandenburg.de/ozg/de/it-infrastrukturen/it-basiskomponenten/bundid-nutzerkonto-deutschlandid/>
[^s21]: Bundesministerium der Justiz / gesetze-im-internet.de — § 1 AZR-Gesetz. § 1 AZR-Gesetz. <https://www.gesetze-im-internet.de/azrg/__1.html> ([archived](https://web.archive.org/web/20250215034909/https://www.gesetze-im-internet.de/azrg/__1.html))
[^s22]: Generalzolldirektion (Zoll online) — ATLAS. ATLAS. <https://www.zoll.de/DE/Fachthemen/Zoelle/ATLAS/atlas_node.html> ([archived](https://web.archive.org/web/20260618015312/https://www.zoll.de/DE/Fachthemen/Zoelle/ATLAS/atlas_node.html))
[^s23]: Bundesministerium der Justiz / gesetze-im-internet.de — § 3 BKAG. § 3 BKAG. <https://www.gesetze-im-internet.de/bkag_2018/__3.html> ([archived](https://web.archive.org/web/20260227115654/https://www.gesetze-im-internet.de/bkag_2018/__3.html))
[^s24]: Bundesamt für Bevölkerungsschutz und Katastrophenhilfe — MoWaS. MoWaS. <https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/MoWaS/mowas_node.html> ([archived](https://web.archive.org/web/20260924105236/https://www.bbk.bund.de/DE/Warnung-Vorsorge/Warnung-in-Deutschland/MoWaS/mowas_node.html))
[^s25]: Bundesarchiv — Nutzung des Digitalen Zwischenarchivs (DZAB). Nutzung des Digitalen Zwischenarchivs (DZAB). <https://www.bundesarchiv.de/unterlagen-abgeben/behoerdenberatung-zu-schriftgut-und-informationsverwaltung/nutzung-des-digitalen-zwischenarchivs-dzab/> ([archived](https://web.archive.org/web/20260618022322/https://www.bundesarchiv.de/unterlagen-abgeben/behoerdenberatung-zu-schriftgut-und-informationsverwaltung/nutzung-des-digitalen-zwischenarchivs-dzab/))

**Evidence grades:** 0 Strong, 28 Standard. Strong: an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
