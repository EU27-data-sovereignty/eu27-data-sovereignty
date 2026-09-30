# Poland: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Poland could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4][^s5] |
| State-controlled national eID | Yes[^s6][^s7][^s8] |
| Government data centres | *Not yet sourced* |
| Government cloud in operation | Yes[^s9][^s10][^s11] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Poland described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 36.33 million[^s12] |
| GDP, current prices | 922.9 EUR bn[^s13] |
| Public administration employment (NACE O) | 1 242.7 thousand[^s14] |
| Non-household electricity price | 193.5 EUR/MWh[^s15] |
| Renewables share of electricity | 32.5 %[^s16] |
| Land area | 307 236 km²[^s17] |

## 3. Critical data holdings, by priority

The holdings Poland cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 32 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Powszechny Elektroniczny System Ewidencji Ludności – rejestr PESEL (Universal Electronic Population Register System – PESEL register)[^s18] | minister właściwy do spraw informatyzacji (minister competent for computerisation)[^s18] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s19] | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Profil Zaufany is an electronic identification means notified at assurance level substantial[^s6][^s20] | The digital affairs minister manages the public electronic identification system (Art. 20ab, Act on Computerisation of Public Task Entities)[^s6] | *Not stated in sources* | Over 14 million active trusted profiles; over 27 million mObywatel app downloads[^s21] |
| High | Electoral roll entry (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | narodowe centrum certyfikacji (national certification centre), part of the krajowa infrastruktura zaufania (national trust infrastructure)[^s3] | Narodowy Bank Polski (National Bank of Poland), when authorised by the minister competent for computerisation[^s3] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | księgi wieczyste (land and mortgage registers), kept in an ICT system[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Krajowy Rejestr Karny (National Criminal Register)[^s23] | Minister Sprawiedliwości (Minister of Justice), through the Biuro Informacyjne Krajowego Rejestru Karnego (Information Office of the National Criminal Register)[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Krajowy System Informacyjny Policji – KSIP (National Police Information System)[^s24] | Komendant Główny Policji (Chief Commander of Police)[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Krajowy zbiór rejestrów, ewidencji i wykazu w sprawach cudzoziemców (National collection of registers, records and list concerning foreigners)[^s25] | Szef Urzędu (Head of the Office [for Foreigners])[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Tax identification numbers (NIP) are assigned via the Central Register of Entities – National Taxpayer Records (CRP KEP)[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | PUESC is the ICT system for electronic exchange between KAS and its clients, including declarations[^s27][^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | ZUS also keeps the Central Register of Insured Persons, of Contribution Payers and of Open Pension Fund Members[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Centralny Wykaz Ubezpieczonych (Central Register of Insured Persons)[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | CEIDG (sole-trader business register) is kept in an ICT system by the economy minister[^s31] | The Minister of Justice maintains the ICT system used to keep the KRS (Art. 3a)[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | centralna ewidencja pojazdów (central vehicle register)[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Krajowy System Informatyczny – KSI (National IT System)[^s34] | Komendant Główny Policji (Chief Commander of Police), as the central technical authority of KSI[^s34] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | Centralny Rejestr Wyborców (Central Register of Voters)[^s35] | Minister właściwy do spraw informatyzacji (minister competent for computerisation)[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | system powiadamiania ratunkowego (emergency notification system) for numbers 112, 997 and 998[^s36] | Minister właściwy do spraw administracji publicznej (minister competent for public administration)[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Council of Ministers regulation on cooperation of the RCB director with mobile network operators to warn end users (Alert RCB)[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | centralny system informacji rynku energii (central energy market information system)[^s38] | operator systemu przesyłowego elektroenergetycznego (electricity transmission system operator), acting as operator informacji rynku energii (energy market information operator)[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | System informacyjny gospodarowania wodami (water management information system)[^s39] | Wody Polskie (Polish Waters)[^s39] | *Not stated in sources* | *Not yet measured* |
| High | Education (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet sourced* | Administrator of P1 is a unit subordinate to the health minister competent for health information systems[^s40][^s41] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Dziennik Ustaw Rzeczypospolitej Polskiej (Journal of Laws of the Republic of Poland)[^s42] | Prezes Rady Ministrów (Prime Minister), with the assistance of the Rządowe Centrum Legislacji (Government Legislation Centre)[^s42] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet sourced* | The health minister designates the register's system administrator from subordinate or supervised units[^s43] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | Archival materials expressly include electronic documents[^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | State register of boundaries, integrated with the land and building cadastre and the register of localities, streets and addresses[^s45] | Geodetic and Cartographic Law Art. 7a: the Surveyor General keeps the central geodetic and cartographic resource[^s45] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 31 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 31 |

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

> Not yet sized. Capacity for Poland will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Poland without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- Firearms register (tier 1)
- Government payroll and personnel (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)

---

[^s1]: Sejm RP (Dziennik Ustaw) — Ustawa z dnia 5 sierpnia 2010 r. o ochronie informacji…, 2010-10-01. Ustawa z dnia 5 sierpnia 2010 r. o ochronie informacji niejawnych (art. 5). <https://api.sejm.gov.pl/eli/acts/DU/2010/1228/text.html> ([archived](https://web.archive.org/web/20260607080912/https://api.sejm.gov.pl/eli/acts/DU/2010/1228/text.html))
[^s2]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 11 sierpnia 2025 r.…, 2025-09-02. Obwieszczenie Marszałka Sejmu z dnia 11 sierpnia 2025 r. – jednolity tekst ustawy o ochronie informacji niejawnych. <https://api.sejm.gov.pl/eli/acts/DU/2025/1209/text.pdf>
[^s3]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 14 listopada 2024…, 2024-11-25. Obwieszczenie Marszałka Sejmu z dnia 14 listopada 2024 r. – jednolity tekst ustawy o usługach zaufania oraz identyfikacji elektronicznej. <https://api.sejm.gov.pl/eli/acts/DU/2024/1725/text.pdf>
[^s4]: Sejm RP (Dziennik Ustaw) — Ustawa z dnia 5 września 2016 r. o usługach zaufania…, 2016-09-29. Ustawa z dnia 5 września 2016 r. o usługach zaufania oraz identyfikacji elektronicznej (art. 11). <https://api.sejm.gov.pl/eli/acts/DU/2016/1579/text.html>
[^s5]: Narodowy Bank Polski (NCCert) — Narodowe Centrum Certyfikacji - strona główna. Narodowe Centrum Certyfikacji - strona główna. <https://www.nccert.pl/> ([archived](https://web.archive.org/web/20260926200010/https://www.nccert.pl/))
[^s6]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2026-09-23. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o informatyzacji działalności podmiotów realizujących zadania publiczne (Dz.U. 2026 poz. 1241). <https://api.sejm.gov.pl/eli/acts/DU/2026/1241/text.pdf>
[^s7]: Centralny Ośrodek Informatyki — Profil zaufany. Profil zaufany. <https://coi.gov.pl/realizacje/profil-zaufany>
[^s8]: Ministerstwo Cyfryzacji — Profil zaufany. Profil zaufany. <https://www.gov.pl/web/cyfryzacja/profil-zaufany> ([archived](https://web.archive.org/web/20260927131122/https://www.gov.pl/web/cyfryzacja/profil-zaufany))
[^s9]: Centralny Ośrodek Informatyki — Wspólna Infrastruktura Informatyczna Państwa. Wspólna Infrastruktura Informatyczna Państwa. <https://coi.gov.pl/realizacje/wspolna-infrastruktura-informatyczna-panstwa>
[^s10]: Centralny Ośrodek Informatyki — EZD RP w modelu SaaS - jak COI buduje technologiczne…. EZD RP w modelu SaaS - jak COI buduje technologiczne zaplecze cyfrowej administracji. <https://coi.gov.pl/strefa-wiedzy/wpis/ezd-rp-w-modelu-saas-jak-coi-buduje-technologiczne-zaplecze-cyfrowej-administracji>
[^s11]: Ministerstwo Cyfryzacji — Strategia Cyfryzacji Państwa. Strategia Cyfryzacji Państwa. <https://www.gov.pl/web/cyfryzacja/strategia-cyfryzacji-panstwa> ([archived](https://web.archive.org/web/20260927055032/https://www.gov.pl/web/cyfryzacja/strategia-cyfryzacji-panstwa))
[^s12]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s13]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s14]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s15]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s16]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s17]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s18]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 12 marca 2026 r. –…, 2026-03-20. Obwieszczenie Marszałka Sejmu z dnia 12 marca 2026 r. – jednolity tekst ustawy o ewidencji ludności. <https://api.sejm.gov.pl/eli/acts/DU/2026/384/text.pdf>
[^s19]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2025-12-10. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o dowodach osobistych (Dz.U. 2025 poz. 1753). <https://api.sejm.gov.pl/eli/acts/DU/2025/1753/text.pdf>
[^s20]: Centralny Ośrodek Informatyki — Profil zaufany, 2026-05-26. Profil zaufany. <https://www.coi.gov.pl/realizacje/profil-zaufany> ([archived](https://web.archive.org/web/20260726144422/https://www.coi.gov.pl/realizacje/profil-zaufany))
[^s21]: Centralny Ośrodek Informatyki — COI – Corporation (English version). COI – Corporation (English version). <https://www.coi.gov.pl/corporation> ([archived](https://web.archive.org/web/20260814170237/https://www.coi.gov.pl/corporation))
[^s22]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 31 lipca 2026 r. –…, 2026-08-06. Obwieszczenie Marszałka Sejmu z dnia 31 lipca 2026 r. – jednolity tekst ustawy o księgach wieczystych i hipotece. <https://api.sejm.gov.pl/eli/acts/DU/2026/1066/text.pdf>
[^s23]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 20 lutego 2024 r. –…, 2024-02-29. Obwieszczenie Marszałka Sejmu z dnia 20 lutego 2024 r. – jednolity tekst ustawy o Krajowym Rejestrze Karnym. <https://api.sejm.gov.pl/eli/acts/DU/2024/276/text.pdf> ([archived](https://web.archive.org/web/20260118051851/https://api.sejm.gov.pl/eli/acts/DU/2024/276/text.pdf))
[^s24]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 10 kwietnia 2025 r.…, 2025-05-15. Obwieszczenie Marszałka Sejmu z dnia 10 kwietnia 2025 r. – jednolity tekst ustawy o Policji. <https://api.sejm.gov.pl/eli/acts/DU/2025/636/text.pdf> ([archived](https://web.archive.org/web/20260119013525/https://api.sejm.gov.pl/eli/acts/DU/2025/636/text.pdf))
[^s25]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 25 lipca 2025 r. –…, 2025-08-07. Obwieszczenie Marszałka Sejmu z dnia 25 lipca 2025 r. – jednolity tekst ustawy o cudzoziemcach. <https://api.sejm.gov.pl/eli/acts/DU/2025/1079/text.pdf>
[^s26]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2026-02-10. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o zasadach ewidencji i identyfikacji podatników i płatników (Dz.U. 2026 poz. 151). <https://api.sejm.gov.pl/eli/acts/DU/2026/151/text.pdf>
[^s27]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 11 września 2024 r.…, 2024-09-17. Obwieszczenie Marszałka Sejmu z dnia 11 września 2024 r. – jednolity tekst ustawy – Prawo celne. <https://api.sejm.gov.pl/eli/acts/DU/2024/1373/text.pdf>
[^s28]: Ministerstwo Finansów / Krajowa Administracja Skarbowa — Jak to działa – informacje o PUESC. Jak to działa – informacje o PUESC. <https://puesc.gov.pl/web/guest/uslugi/jak-to-dziala-informacje-o-puesc> ([archived](https://web.archive.org/web/20260716090913/https://puesc.gov.pl/web/guest/uslugi/jak-to-dziala-informacje-o-puesc))
[^s29]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2026-02-23. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o systemie ubezpieczeń społecznych (Dz.U. 2026 poz. 199). <https://api.sejm.gov.pl/eli/acts/DU/2026/199/text.pdf>
[^s30]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 26 września 2025 r.…, 2025-10-24. Obwieszczenie Marszałka Sejmu z dnia 26 września 2025 r. – jednolity tekst ustawy o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych. <https://api.sejm.gov.pl/eli/acts/DU/2025/1461/text.pdf>
[^s31]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2026-01-12. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o CEIDG i Punkcie Informacji dla Przedsiębiorcy (Dz.U. 2026 poz. 30). <https://api.sejm.gov.pl/eli/acts/DU/2026/30/text.pdf>
[^s32]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2025-07-02. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o Krajowym Rejestrze Sądowym (Dz.U. 2025 poz. 869). <https://api.sejm.gov.pl/eli/acts/DU/2025/869/text.pdf> ([archived](https://web.archive.org/web/20250915063449/https://api.sejm.gov.pl/eli/acts/DU/2025/869/text.pdf))
[^s33]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 21 czerwca 2024 r.…, 2024-08-19. Obwieszczenie Marszałka Sejmu z dnia 21 czerwca 2024 r. – jednolity tekst ustawy – Prawo o ruchu drogowym. <https://api.sejm.gov.pl/eli/acts/DU/2024/1251/text.pdf> ([archived](https://web.archive.org/web/20251222005510/https://api.sejm.gov.pl/eli/acts/DU/2024/1251/text.pdf))
[^s34]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 31 lipca 2026 r. –…, 2026-08-06. Obwieszczenie Marszałka Sejmu z dnia 31 lipca 2026 r. – jednolity tekst ustawy o udziale RP w Systemie Informacyjnym Schengen oraz Wizowym Systemie Informacyjnym. <https://api.sejm.gov.pl/eli/acts/DU/2026/1061/text.pdf>
[^s35]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy…, 2026-09-28. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy Kodeks wyborczy (Dz.U. 2026 poz. 1261). <https://api.sejm.gov.pl/eli/acts/DU/2026/1261/text.pdf>
[^s36]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 26 września 2025 r.…, 2025-10-07. Obwieszczenie Marszałka Sejmu z dnia 26 września 2025 r. – jednolity tekst ustawy o systemie powiadamiania ratunkowego. <https://api.sejm.gov.pl/eli/acts/DU/2025/1354/text.pdf>
[^s37]: Rada Ministrów / Dziennik Ustaw — Rozporządzenie Rady Ministrów z dnia 31 sierpnia 2020 r.…, 2020. Rozporządzenie Rady Ministrów z dnia 31 sierpnia 2020 r. w sprawie współpracy dyrektora RCB z operatorem ruchomej publicznej sieci telekomunikacyjnej (Dz.U. 2020 poz. 1527). <https://api.sejm.gov.pl/eli/acts/DU/2020/1527/text.pdf> ([archived](https://web.archive.org/web/20260118083917/https://api.sejm.gov.pl/eli/acts/DU/2020/1527/text.pdf))
[^s38]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 5 grudnia 2025 r. –…, 2026-01-15. Obwieszczenie Marszałka Sejmu z dnia 5 grudnia 2025 r. – jednolity tekst ustawy – Prawo energetyczne. <https://api.sejm.gov.pl/eli/acts/DU/2026/43/text.pdf>
[^s39]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 26 czerwca 2025 r.…, 2025-07-21. Obwieszczenie Marszałka Sejmu z dnia 26 czerwca 2025 r. – jednolity tekst ustawy – Prawo wodne. <https://api.sejm.gov.pl/eli/acts/DU/2025/960/text.pdf>
[^s40]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2026-02-24. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o systemie informacji w ochronie zdrowia (Dz.U. 2026 poz. 208). <https://api.sejm.gov.pl/eli/acts/DU/2026/208/text.pdf>
[^s41]: Centrum e-Zdrowia — Centrum e-Zdrowia – strona główna. Centrum e-Zdrowia – strona główna. <https://cez.gov.pl/> ([archived](https://web.archive.org/web/20240619174818/https://cez.gov.pl/))
[^s42]: Sejm RP / Dziennik Ustaw (ELI API) — Obwieszczenie Marszałka Sejmu z dnia 19 lipca 2019 r. –…, 2019-08-05. Obwieszczenie Marszałka Sejmu z dnia 19 lipca 2019 r. – jednolity tekst ustawy o ogłaszaniu aktów normatywnych i niektórych innych aktów prawnych. <https://api.sejm.gov.pl/eli/acts/DU/2019/1461/text.pdf> ([archived](https://web.archive.org/web/20260110071005/https://api.sejm.gov.pl/eli/acts/DU/2019/1461/text.pdf))
[^s43]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2025-12-02. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o zapobieganiu oraz zwalczaniu zakażeń i chorób zakaźnych u ludzi (Dz.U. 2025 poz. 1675). <https://api.sejm.gov.pl/eli/acts/DU/2025/1675/text.pdf>
[^s44]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o…, 2020-02-03. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy o narodowym zasobie archiwalnym i archiwach (Dz.U. 2020 poz. 164). <https://api.sejm.gov.pl/eli/acts/DU/2020/164/text.html> ([archived](https://web.archive.org/web/20260307211347/https://api.sejm.gov.pl/eli/acts/DU/2020/164/text.html))
[^s45]: Sejm RP / Dziennik Ustaw — Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy…, 2024-07-31. Obwieszczenie Marszałka Sejmu – jednolity tekst ustawy Prawo geodezyjne i kartograficzne (Dz.U. 2024 poz. 1151). <https://api.sejm.gov.pl/eli/acts/DU/2024/1151/text.html>

**Evidence grades:** 1 Strong, 49 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
