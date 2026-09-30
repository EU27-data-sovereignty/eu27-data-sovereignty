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
| Classification in law | Yes[^s3][^s1] |
| Sovereign cloud certification | Partly[^s1] |
| State-controlled trust anchor | Yes[^s4] |
| State-controlled national eID | Yes[^s4] |
| Government data centres | Yes[^s2] |
| Government cloud in operation | *Not yet sourced* |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Italy described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 58.94 million[^s5] |
| GDP, current prices | 2 265.0 EUR bn[^s6] |
| Public administration employment (NACE O) | 1 213.1 thousand[^s7] |
| Non-household electricity price | 220.3 EUR/MWh[^s8] |
| Renewables share of electricity | 43.5 %[^s9] |
| Land area | 297 823 km²[^s10] |

## 3. Critical data holdings, by priority

The holdings Italy cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | ANPR (National Register of the Resident Population) is the Ministry of the Interior's single database for population data[^s11][^s12] | Ministry of the Interior; Sogei S.p.A. provides the technical operation[^s11][^s13] | *Not stated in sources* | *Not yet sourced* |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | ANSC - national computerised archive of civil-status registers (births, marriages, deaths)[^s14][^s12] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Facial biometric (tier 0) | The CIE electronic record card (cartellino elettronico), kept by SSCE, holds the holder's photograph, signature scan and registry data[^s15] | Centro Nazionale dei Servizi Demografici (CNSD), Ministry of the Interior[^s15] | National infrastructure[^s15] | *Not yet measured* |
| High | Digital identity credentials (tier 0) | SPID (sistema pubblico per la gestione dell'identità digitale di cittadini e imprese – public digital identity system)[^s16] | Open set of public and private entities accredited by AgID[^s16] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Anagrafe Immobiliare Integrata (Integrated Property Register)[^s17] | Agenzia del Territorio (Land Agency)[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | casellario giudiziale (criminal records register)[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Centro elaborazione dati (Data Processing Centre, the inter-force police database)[^s19] | Ministero dell'interno (Ministry of the Interior)[^s19] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The CIE database is part of the CNSD infrastructure[^s15] | Only the Ministry of the Interior may issue the CIE[^s20] | National infrastructure[^s15] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | The CNSD 'CA Autenticazione' is the Ministry of the Interior's certification authority that issues online-authentication certificates for the CIE[^s15] | AgID is Italy's supervisory authority for qualified trust service providers[^s21] | National infrastructure[^s15] | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | Anagrafe tributaria (national tax register)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | AIDA (Integrated Customs and Excise Automation) data warehouse of the Customs and Monopolies Agency[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | casellario centrale dei pensionati (central register of pensioners)[^s24] | Istituto nazionale della previdenza sociale (INPS)[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | The National Register of Patients (ANA) is the reference register for public health, run within Sistema Tessera Sanitaria[^s25][^s26] | ANA is built by the Ministry of Economy and Finance in agreement with the Ministry of Health[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Registro delle imprese (Register of Companies)[^s27] | Camera di commercio (chambers of commerce)[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Apposita sezione del Registro delle imprese (dedicated beneficial-ownership section of the Register of Companies)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | archivio nazionale dei veicoli (national vehicle archive)[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | SIOPE monitors the receipts and payments made by the treasurers of all public administrations[^s30][^s31] | The SIOPE+ infrastructure is operated by the Banca d'Italia[^s30][^s31] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | NoiPA[^s32] | Dipartimento dell'Amministrazione Generale del personale e dei servizi (DAG), Ministero dell'Economia e delle Finanze (MEF)[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | The historical election archive is an online database of election results down to municipality level[^s33] | The Central Directorate for Electoral Services publishes turnout and results data[^s33][^s34] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | BI‑Comp (national multilateral clearing system)[^s35] | Banca d'Italia[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | IT-alert is the public warning service that sends messages to devices in an area hit by a serious emergency[^s36][^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Anagrafe nazionale dell'istruzione (ANIST) (National Education Register)[^s38] | Ministero dell'istruzione (Ministry of Education)[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | The electronic health record (FSE) holds the patient's clinical data and documents[^s39][^s40] | The FSE is set up by the regions and autonomous provinces[^s39][^s40] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The printed Gazzetta Ufficiale is the only definitive text and prevails over the digital version[^s41] | IPZS publishes the Gazzetta Ufficiale in digital form[^s41] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | The Central State Archive is building the repository for digital archives produced by central state bodies[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet sourced* | ISTAT is the main producer of official statistics[^s43][^s44] | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 27 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 3 |
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

> Not yet sized. Capacity for Italy will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Italy without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Fingerprint biometric (tier 0)
- Authentication audit log (tier 0)
- Residence and migration status (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Agenzia per la cybersicurezza nazionale (ACN) — Regolamento per le infrastrutture digitali e per i…, 2024. Regolamento per le infrastrutture digitali e per i servizi cloud per la pubblica amministrazione (Regolamento ACN n. 21007/2024), Allegato 2, sezione 2. <https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud> ([archived](https://web.archive.org/web/20260807151428/https://www.acn.gov.it/portale/documents/d/guest/regolamentocloud))
[^s2]: Normattiva (Istituto Poligrafico e Zecca dello Stato / Presidenza del Consiglio dei ministri) — Decreto-legge 18 ottobre 2012, n. 179, art. 33-septies…, 2012-10-18. Decreto-legge 18 ottobre 2012, n. 179, art. 33-septies (Consolidamento e razionalizzazione dei siti e delle infrastrutture digitali del Paese). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art33septies>
[^s3]: Agenzia per la cybersicurezza nazionale (ACN) — Strategia Cloud Italia. Strategia Cloud Italia. <https://www.acn.gov.it/portale/strategia-cloud-italia> ([archived](https://web.archive.org/web/20240918060056/https://www.acn.gov.it/portale/strategia-cloud-italia))
[^s4]: Agenzia per l'Italia Digitale (AgID), trusted list scheme operator — Italian Trusted List (TSL-IT), trust service provider…. Italian Trusted List (TSL-IT), trust service provider entry: Ministero dell'Interno. <https://eidas.agid.gov.it/TL/TSL-IT.xml> ([archived](https://web.archive.org/web/20260925060906/https://eidas.agid.gov.it/TL/TSL-IT.xml))
[^s5]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s6]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s7]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s8]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s9]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s10]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s11]: Ministero dell'Interno - Anagrafe Nazionale — Conosci l'ANPR. Conosci l'ANPR. <https://www.anagrafenazionale.interno.it/anpr/> ([archived](https://web.archive.org/web/20260927003857/https://www.anagrafenazionale.interno.it/anpr/))
[^s12]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto legislativo 7 marzo 2005, n. 82 (Codice…, 2005. Decreto legislativo 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale), art. 62. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62> ([archived](https://web.archive.org/web/20260125120137/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62))
[^s13]: Ministero dell'Interno — Missione – ANPR. Missione – ANPR. <https://www.anagrafenazionale.interno.it/anpr/missione/> ([archived](https://web.archive.org/web/20260906012128/https://www.anagrafenazionale.interno.it/anpr/missione/))
[^s14]: Ministero dell'Interno - Anagrafe Nazionale — Guida all'ANSC. Guida all'ANSC. <https://www.anagrafenazionale.interno.it/area-tecnica/guida-ansc/> ([archived](https://web.archive.org/web/20260918002926/https://www.anagrafenazionale.interno.it/area-tecnica/guida-ansc/))
[^s15]: Gazzetta Ufficiale della Repubblica Italiana - Istituto Poligrafico e Zecca dello Stato — Decreto del Ministero dell'Interno 23 dicembre 2015 -…, 2015-12-30. Decreto del Ministero dell'Interno 23 dicembre 2015 - Modalità tecniche di emissione della Carta d'identità elettronica (GU Serie Generale n. 302 del 30-12-2015). <https://www.gazzettaufficiale.it/eli/gu/2015/12/30/302/sg/pdf>
[^s16]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 82/2005 (CAD), art. 64, 2022-06-30. D.Lgs. 82/2005 (CAD), art. 64. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art64> ([archived](https://web.archive.org/web/20251111011946/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art64))
[^s17]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DL 78/2010, art. 19 (Aggiornamento del catasto), 2011-02-27. DL 78/2010, art. 19 (Aggiornamento del catasto). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art19> ([archived](https://web.archive.org/web/20251116145932/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art19))
[^s18]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DPR 313/2002 (Testo unico casellario giudiziale), art. 2, 2024-05-01. DPR 313/2002 (Testo unico casellario giudiziale), art. 2. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2002-11-14;313~art2>
[^s19]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — Legge 121/1981, art. 8 (Istituzione del Centro…, 2005-06-01. Legge 121/1981, art. 8 (Istituzione del Centro elaborazione dati). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1981-04-01;121~art8> ([archived](https://web.archive.org/web/20250709093424/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1981-04-01;121~art8))
[^s20]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto-legge 31 gennaio 2005, n. 7, art. 7-vicies ter, 2005. Decreto-legge 31 gennaio 2005, n. 7, art. 7-vicies ter. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2005-01-31;7~art7viciester>
[^s21]: Agenzia per l'Italia Digitale (AgID) — Servizi fiduciari qualificati / Firma elettronica…, 2024-04-23. Servizi fiduciari qualificati / Firma elettronica qualificata. <https://www.agid.gov.it/it/piattaforme/firma-elettronica-qualificata> ([archived](https://web.archive.org/web/20260924003149/https://www.agid.gov.it/it/piattaforme/firma-elettronica-qualificata))
[^s22]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DPR 605/1973, art. 1, 1976-12-04. DPR 605/1973, art. 1. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;605~art1!vig=2026-09-30>
[^s23]: Agenzia delle Dogane e dei Monopoli — Libro Blu 2024 - Relazione, 2025. Libro Blu 2024 - Relazione. <https://www.adm.gov.it/portale/documents/20182/261920520/Libro+blu+2024+-+Relazione.pdf/e46989ce-b39f-a404-3b4b-2af3196cba43?t=1784560697678>
[^s24]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — DPR 1388/1971 – Istituzione del casellario centrale dei…, 1998-01-01. DPR 1388/1971 – Istituzione del casellario centrale dei pensionati. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1971-12-31;1388~art1>
[^s25]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto legislativo 7 marzo 2005, n. 82 (Codice…, 2005. Decreto legislativo 7 marzo 2005, n. 82 (Codice dell'amministrazione digitale), art. 62-ter. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62ter> ([archived](https://web.archive.org/web/20251012072920/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62ter))
[^s26]: MEF - Ragioneria Generale dello Stato — Sistema Tessera Sanitaria - Home. Sistema Tessera Sanitaria - Home. <https://www.sistemats.it/> ([archived](https://web.archive.org/web/20160502181750/http://www.sistemats.it:80/))
[^s27]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — Legge 580/1993, art. 8 (Registro delle imprese), 2016-12-10. Legge 580/1993, art. 8 (Registro delle imprese). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1993-12-29;580~art8>
[^s28]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 231/2007, art. 21, 2026-07-23. D.Lgs. 231/2007, art. 21. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art21> ([archived](https://web.archive.org/web/20260106152255/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2007-11-21;231~art21))
[^s29]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 285/1992 (Codice della strada), art. 226, 2018-07-01. D.Lgs. 285/1992 (Codice della strada), art. 226. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1992-04-30;285~art226> ([archived](https://web.archive.org/web/20251011185708/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1992-04-30;285~art226))
[^s30]: Agenzia per l'Italia Digitale (AgID) — SIOPE. SIOPE. <https://www.agid.gov.it/it/piattaforme/siope> ([archived](https://web.archive.org/web/20260923012741/https://www.agid.gov.it/it/piattaforme/siope))
[^s31]: MEF – Ragioneria Generale dello Stato — SIOPE+. SIOPE+. <https://www.rgs.mef.gov.it/VERSIONE-I/e_government/amministrazioni_pubbliche/siope/siope_/> ([archived](https://web.archive.org/web/20260921013404/https://www.rgs.mef.gov.it/VERSIONE-I/e_government/amministrazioni_pubbliche/siope/siope_/))
[^s32]: Ministero dell'Economia e delle Finanze — Chi siamo – NoiPA. Chi siamo – NoiPA. <https://noipa.mef.gov.it/cl/chi-siamo> ([archived](https://web.archive.org/web/20250413225956/https://noipa.mef.gov.it/cl/chi-siamo))
[^s33]: Ministero dell'Interno - Dipartimento per gli Affari Interni e Territoriali — Le elezioni. Le elezioni. <https://dait.interno.gov.it/elezioni> ([archived](https://web.archive.org/web/20260929012749/https://dait.interno.gov.it/elezioni))
[^s34]: Ministero dell'Interno – DAIT — Archivio Storico delle Elezioni. Archivio Storico delle Elezioni. <https://elezionistorico.interno.gov.it/> ([archived](https://web.archive.org/web/20260924110557/https://elezionistorico.interno.gov.it/))
[^s35]: Banca d'Italia — Gestione dei sistemi di pagamento. Gestione dei sistemi di pagamento. <https://www.bancaditalia.it/compiti/sistema-pagamenti/index.html>
[^s36]: Presidenza del Consiglio dei Ministri – Dipartimento della Protezione Civile — IT-alert – Cos'è. IT-alert – Cos'è. <https://www.it-alert.it/it/cose/> ([archived](https://web.archive.org/web/20260629070727/https://www.it-alert.it/it/cose/))
[^s37]: Presidenza del Consiglio dei Ministri - Dipartimento della Protezione Civile — Come funziona | IT-alert. Come funziona | IT-alert. <https://www.it-alert.it/it/come-funziona/>
[^s38]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 82/2005 (CAD), art. 62-quater, 2021-07-31. D.Lgs. 82/2005 (CAD), art. 62-quater. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62quater> ([archived](https://web.archive.org/web/20250713135628/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82~art62quater))
[^s39]: Ministero della Salute / Dipartimento per la trasformazione digitale — Fascicolo Sanitario Elettronico, 2026. Fascicolo Sanitario Elettronico. <https://www.fascicolosanitario.gov.it/>
[^s40]: Normattiva - Istituto Poligrafico e Zecca dello Stato — Decreto-legge 18 ottobre 2012, n. 179, art. 12, 2012. Decreto-legge 18 ottobre 2012, n. 179, art. 12. <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art12> ([archived](https://web.archive.org/web/20250819092310/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-10-18;179~art12))
[^s41]: Istituto Poligrafico e Zecca dello Stato — Gazzetta Ufficiale - Home. Gazzetta Ufficiale - Home. <https://www.gazzettaufficiale.it/> ([archived](https://web.archive.org/web/20260913204754/https://www.gazzettaufficiale.it/))
[^s42]: Archivio Centrale dello Stato — Polo di conservazione digitale. Polo di conservazione digitale. <https://acs.cultura.gov.it/piano-nazionale-di-ripresa-e-resilienza-del-ministero-della-cultura/polo-di-conservazione-digitale/>
[^s43]: Istituto nazionale di statistica (ISTAT) — L'Istituto: organizzazione e attività. L'Istituto: organizzazione e attività. <https://www.istat.it/listituto/> ([archived](https://web.archive.org/web/20260927005502/https://www.istat.it/listituto/))
[^s44]: Normattiva (Istituto Poligrafico e Zecca dello Stato) — D.Lgs. 322/1989, art. 15 (Compiti dell'ISTAT), 1989-10-07. D.Lgs. 322/1989, art. 15 (Compiti dell'ISTAT). <https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1989-09-06;322~art15> ([archived](https://web.archive.org/web/20250906141609/https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1989-09-06;322~art15))

**Evidence grades:** 1 Strong, 57 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
