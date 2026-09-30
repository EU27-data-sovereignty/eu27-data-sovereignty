# Italy: critical data holdings and sovereign hosting

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

> Secured in law, not yet in practice. Confidence: Low. With the evidence still open, Italy could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Yes[^s1][^s2] |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | Partly[^s1] |
| State-controlled trust anchor | Yes[^s3] |
| State-controlled national eID | Yes[^s3] |
| Government data centres | Yes[^s2] |
| Government cloud in operation | *Not yet sourced* |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Italy described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 58.94 million[^s4] |
| GDP, current prices | 2 258.0 EUR bn[^s5] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 220.3 EUR/MWh[^s6] |
| Renewables share of electricity | 40.7 %[^s7] |
| Land area | 297 734 km²[^s8] |

## 3. Critical data holdings, by priority

The holdings Italy cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 15 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | ANPR (National Register of the Resident Population) is the Ministry of the Interior's single database for population data[^s9] | Ministry of the Interior; Sogei S.p.A. provides the technical operation[^s9] | *Not stated in sources* | *Not yet sourced* |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | ANSC - national computerised archive of civil-status registers (births, marriages, deaths)[^s10] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Facial biometric (tier 0) | The CIE electronic record card (cartellino elettronico), kept by SSCE, holds the holder's photograph, signature scan and registry data[^s11] | Centro Nazionale dei Servizi Demografici (CNSD), Ministry of the Interior[^s11] | National infrastructure[^s11] | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The CIE database is part of the CNSD infrastructure[^s11] | Only the Ministry of the Interior may issue the CIE[^s12] | National infrastructure[^s11] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | The CNSD 'CA Autenticazione' is the Ministry of the Interior's certification authority that issues online-authentication certificates for the CIE[^s11] | AgID is Italy's supervisory authority for qualified trust service providers[^s13] | National infrastructure[^s11] | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | AIDA (Integrated Customs and Excise Automation) data warehouse of the Customs and Monopolies Agency[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | The National Register of Patients (ANA) is the reference register for public health, run within Sistema Tessera Sanitaria[^s15] | ANA is built by the Ministry of Economy and Finance in agreement with the Ministry of Health[^s16] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | SIOPE monitors the receipts and payments made by the treasurers of all public administrations[^s17] | The SIOPE+ infrastructure is operated by the Banca d'Italia[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | The historical election archive is an online database of election results down to municipality level[^s18] | The Central Directorate for Electoral Services publishes turnout and results data[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | IT-alert is the public warning service that sends messages to devices in an area hit by a serious emergency[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | The electronic health record (FSE) holds the patient's clinical data and documents[^s20] | The FSE is set up by the regions and autonomous provinces[^s20] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The printed Gazzetta Ufficiale is the only definitive text and prevails over the digital version[^s21] | IPZS publishes the Gazzetta Ufficiale in digital form[^s21] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | The Central State Archive is building the repository for digital archives produced by central state bodies[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet sourced* | ISTAT is the main producer of official statistics[^s23] | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 15 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 3 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 12 |

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

> Not yet sized. Capacity for Italy will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Italy without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Fingerprint biometric (tier 0)
- Digital identity credentials (tier 0)
- Authentication audit log (tier 0)
- Residence and migration status (tier 1)
- Tax (tier 1)
- Benefits & pensions (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Beneficial ownership register (tier 1)
- Vehicle & licensing (tier 1)
- Judicial & criminal justice (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Government payroll and personnel (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Agenzia per la cybersicurezza nazionale (ACN) — Regolamento per le infrastrutture digitali e per i…, 2024. Regolamento per le infrastrutture digitali e per i servizi cloud per la pubblica amministrazione (Regolamento ACN n. 21007/2024), Allegato 2, sezione 2. <https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud> ([archived](https://web.archive.org/web/20260807151428/https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud))
[^s2]: Normattiva (Istituto Poligrafico e Zecca dello Stato / Presidenza del Consiglio dei ministri) — Decreto-legge 18 ottobre 2012, n. 179, art. 33-septies…, 2012-10-18. Decreto-legge 18 ottobre 2012, n. 179, art. 33-septies (Consolidamento e razionalizzazione dei siti e delle infrastrutture digitali del Paese). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art33septies>
[^s3]: Agenzia per l'Italia Digitale (AgID), trusted list scheme operator — Italian Trusted List (TSL-IT), trust service provider…. Italian Trusted List (TSL-IT), trust service provider entry: Ministero dell'Interno. <https://eidas.agid.gov.it/TL/TSL-IT.xml> ([archived](https://web.archive.org/web/20260925060906/https://eidas.agid.gov.it/TL/TSL-IT.xml))
[^s4]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s5]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s6]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s7]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s8]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s9]: Ministero dell'Interno - Anagrafe Nazionale — Conosci l'ANPR. Conosci l'ANPR. <https://www.anagrafenazionale.interno.it/anpr/> ([archived](https://web.archive.org/web/20260927003857/https://www.anagrafenazionale.interno.it/anpr/))
[^s10]: Ministero dell'Interno - Anagrafe Nazionale — Guida all'ANSC. Guida all'ANSC. <https://www.anagrafenazionale.interno.it/area-tecnica/guida-ansc/> ([archived](https://web.archive.org/web/20260918002926/https://www.anagrafenazionale.interno.it/area-tecnica/guida-ansc/))
[^s11]: Gazzetta Ufficiale della Repubblica Italiana - Istituto Poligrafico e Zecca dello Stato — Decreto del Ministero dell'Interno 23 dicembre 2015 -…, 2015-12-30. Decreto del Ministero dell'Interno 23 dicembre 2015 - Modalità tecniche di emissione della Carta d'identità elettronica (GU Serie Generale n. 302 del 30-12-2015). <https://www.gazzettaufficiale.it/eli/gu/2015/12/30/302/sg/pdf>
[^s12]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto-legge 31 gennaio 2005, n. 7, art. 7-vicies ter, 2005. Decreto-legge 31 gennaio 2005, n. 7, art. 7-vicies ter. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2005-01-31;7~art7viciester>
[^s13]: Agenzia per l'Italia Digitale (AgID) — Servizi fiduciari qualificati / Firma elettronica…, 2024-04-23. Servizi fiduciari qualificati / Firma elettronica qualificata. <https://www.agid.gov.it/it/piattaforme/firma-elettronica-qualificata> ([archived](https://web.archive.org/web/20260924003149/https://www.agid.gov.it/it/piattaforme/firma-elettronica-qualificata))
[^s14]: Agenzia delle Dogane e dei Monopoli — Libro Blu 2024 - Relazione, 2025. Libro Blu 2024 - Relazione. <https://www.adm.gov.it/portale/documents/20182/261920520/Libro+blu+2024+-+Relazione.pdf/e46989ce-b39f-a404-3b4b-2af3196cba43?t=1784560697678>
[^s15]: MEF - Ragioneria Generale dello Stato — Sistema Tessera Sanitaria - Home. Sistema Tessera Sanitaria - Home. <https://www.sistemats.it/> ([archived](https://web.archive.org/web/20160502181750/http://www.sistemats.it:80/))
[^s16]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto legislativo 7 marzo 2005, n. 82 (Codice…, 2005. Decreto legislativo 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale), art. 62-ter. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62ter> ([archived](https://web.archive.org/web/20251012072920/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62ter))
[^s17]: Agenzia per l'Italia Digitale (AgID) — SIOPE. SIOPE. <https://www.agid.gov.it/it/piattaforme/siope> ([archived](https://web.archive.org/web/20260923012741/https://www.agid.gov.it/it/piattaforme/siope))
[^s18]: Ministero dell'Interno - Dipartimento per gli Affari Interni e Territoriali — Le elezioni. Le elezioni. <https://dait.interno.gov.it/elezioni> ([archived](https://web.archive.org/web/20260929012749/https://dait.interno.gov.it/elezioni))
[^s19]: Presidenza del Consiglio dei Ministri - Dipartimento della Protezione Civile — Come funziona | IT-alert. Come funziona | IT-alert. <https://www.it-alert.it/it/come-funziona/>
[^s20]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto-legge 18 ottobre 2012, n. 179, art. 12, 2012. Decreto-legge 18 ottobre 2012, n. 179, art. 12. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art12> ([archived](https://web.archive.org/web/20250819092310/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art12))
[^s21]: Istituto Poligrafico e Zecca dello Stato — Gazzetta Ufficiale - Home. Gazzetta Ufficiale - Home. <https://www.gazzettaufficiale.it/> ([archived](https://web.archive.org/web/20260913204754/https://www.gazzettaufficiale.it/))
[^s22]: Archivio Centrale dello Stato — Polo di conservazione digitale. Polo di conservazione digitale. <https://acs.cultura.gov.it/piano-nazionale-di-ripresa-e-resilienza-del-ministero-della-cultura/polo-di-conservazione-digitale/>
[^s23]: Istituto nazionale di statistica (ISTAT) — L'Istituto: organizzazione e attività. L'Istituto: organizzazione e attività. <https://www.istat.it/listituto/> ([archived](https://web.archive.org/web/20260927005502/https://www.istat.it/listituto/))

**Evidence grades:** 0 Strong, 37 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
