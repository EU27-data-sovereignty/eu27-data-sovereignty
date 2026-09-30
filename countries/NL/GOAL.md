# Netherlands: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Netherlands could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | No[^s2][^s3] |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s4][^s6][^s7] |
| Government data centres | Yes[^s8][^s9][^s10][^s3] |
| Government cloud in operation | No[^s3] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 32 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Netherlands described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 18.13 million[^s11] |
| GDP, current prices | 1 170.6 EUR bn[^s12] |
| Public administration employment (NACE O) | 661.0 thousand[^s13] |
| Non-household electricity price | 199.1 EUR/MWh[^s14] |
| Renewables share of electricity | 54.7 %[^s15] |
| Land area | 33 984 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Netherlands cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 25 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s17] | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | DigiD gebruiksgeschiedenis (DigiD usage history)[^s18] | Logius[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Basisregister Reisdocumenten (BR) (Basic Register of Travel Documents)[^s19] | Rijksdienst voor Identiteitsgegevens (National Office for Identity Data, RvIG)[^s19] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | registratie van de kiesgerechtigdheid (municipal registration of voting eligibility)[^s20] | Burgemeester en wethouders (municipal executives)[^s20] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | TSPs issue certificates under the State of the Netherlands trust anchor[^s5] | PKIoverheid is a trust framework managed by Logius on behalf of Ministry of BZK[^s5] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Justitiële Documentatie (Judicial Documentation, the criminal records system)[^s21] | Justitiële Informatiedienst (Justid, Judicial Information Service)[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | DigiD: the national means for citizens to identify digitally[^s4][^s6] | Minister of BZK is controller; DigiD is managed by Logius[^s18][^s22] | National infrastructure[^s18] | *Not yet measured* |
| High | Residence and migration status (tier 1) | vreemdelingenadministratie (aliens administration)[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | Current declaration system AGS is being replaced by the new DMS[^s24][^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | polisadministratie (policy administration of employment, wages and benefits)[^s26] | Uitvoeringsinstituut werknemersverzekeringen (UWV, Employee Insurance Agency)[^s26] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | UBO-register (Ultimate Beneficial Owner register)[^s27] | handelsregister (trade register, kept by the Kamer van Koophandel)[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet sourced* | RDW manages and is controller of the vehicle registration register[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | registratiesysteem P-Direkt (P-Direkt HR/payroll registration system)[^s10] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | uitslagprogrammatuur OSV2020-U or Abacus (results-tabulation software)[^s30] | Kiesraad (Electoral Council)[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | meldkamers (emergency dispatch control rooms)[^s31] | politie (national police)[^s31] | *Not stated in sources* | tien meldkamers (ten control rooms)[^s31] |
| High | Crisis management and civil protection (tier 1) | NL-Alert (national public warning system)[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | register onderwijsdeelnemers (register of education participants)[^s33] | Onze Minister (Minister of Education, Culture and Science)[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | LSP is a national infrastructure through which care providers exchange patients' medical data[^s34] | AORTA/LSP managed by VZVZ since 2012[^s35] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Staatsblad en Staatscourant (Bulletin of Acts and Decrees; Government Gazette)[^s36] | Minister van Justitie en Veiligheid (Minister of Justice and Security, for the Staatsblad)[^s36] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Praeventis centrally registers vaccinations of every participant in the national immunisation programme[^s37][^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Microdata: linkable person, business and address-level data for authorised researchers[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 24 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 1 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 23 |

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

> Not yet sized. Capacity for Netherlands will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Netherlands without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Breeder document scans (tier 0)
- Tax (tier 1)
- Statutory health insurance (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Treasury and state accounts (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Ministerie van Algemene Zaken / Staatscourant — Besluit voorschrift informatiebeveiliging Rijksdienst…, 2025-09-08. Besluit voorschrift informatiebeveiliging Rijksdienst bijzondere informatie 2025 (VIRBI 2025), Staatscourant 2025, 30222. <https://zoek.officielebekendmakingen.nl/stcrt-2025-30222.html>
[^s2]: Tweede Kamer der Staten-Generaal (letter from the State Secretary of Economic Affairs and Climate) — Kamerstuk 26643 nr. 1542 - Nationaal beleid voor de…, 2026-07. Kamerstuk 26643 nr. 1542 - Nationaal beleid voor de Nederlandse cloudmarkt. <https://zoek.officielebekendmakingen.nl/kst-1263281.pdf>
[^s3]: Ministerie van BZK (bijlage bij Kamerstuk 26643-1537) — Notitie Verkenning Overheidsbrede Soevereine Clouddiensten, 2026-07-20. Notitie Verkenning Overheidsbrede Soevereine Clouddiensten. <https://zoek.officielebekendmakingen.nl/blg-1263102.pdf>
[^s4]: Logius — Onze organisatie. Onze organisatie. <https://www.logius.nl/over-ons/onze-organisatie> ([archived](https://web.archive.org/web/20260519142506/https://www.logius.nl/over-ons/onze-organisatie))
[^s5]: Logius — Wat is PKIoverheid. Wat is PKIoverheid. <https://www.logius.nl/onze-dienstverlening/toegang/pkioverheid/wat-pkioverheid> ([archived](https://web.archive.org/web/20260618011710/https://www.logius.nl/onze-dienstverlening/toegang/pkioverheid/wat-pkioverheid))
[^s6]: Logius — DigiD. DigiD. <https://www.logius.nl/onze-dienstverlening/toegang/digid> ([archived](https://web.archive.org/web/20260826221154/https://www.logius.nl/onze-dienstverlening/toegang/digid))
[^s7]: wetten.overheid.nl (KOOP) — Wet digitale overheid, 2025-11-11. Wet digitale overheid. <https://wetten.overheid.nl/BWBR0048156>
[^s8]: ODC-Noord (Rijksoverheid, SSO-Noord) — Organisatie - ODC-Noord. Organisatie - ODC-Noord. <https://www.odc-noord.nl/Organisatie> ([archived](https://web.archive.org/web/20260226165411/https://www.odc-noord.nl/Organisatie))
[^s9]: Tweede Kamer der Staten-Generaal (letter from the State Secretary of the Interior and Kingdom Relations) — Kamerstuk 26643 nr. 1537 - Stand van zaken verkenning…, 2026-07-01. Kamerstuk 26643 nr. 1537 - Stand van zaken verkenning soevereine overheidscloud. <https://zoek.officielebekendmakingen.nl/kst-1263099.pdf>
[^s10]: Ministerie van BZK — Jaarrapportage Bedrijfsvoering Rijk 2025, 2026-05-26. Jaarrapportage Bedrijfsvoering Rijk 2025. <https://zoek.officielebekendmakingen.nl/blg-1249197.pdf>
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Overheid.nl Wettenbank — Paspoortwet, 2024-01-01. Paspoortwet. <https://wetten.overheid.nl/BWBR0005212/2024-01-01> ([archived](https://web.archive.org/web/20260928030739/https://wetten.overheid.nl/BWBR0005212/2024-01-01/))
[^s18]: DigiD / Logius — Privacy DigiD. Privacy DigiD. <https://www.digid.nl/over-digid/privacy> ([archived](https://web.archive.org/web/20260927120423/https://www.digid.nl/over-digid/privacy))
[^s19]: Rijksdienst voor Identiteitsgegevens (RvIG) — Basisregister Reisdocumenten. Basisregister Reisdocumenten. <https://www.rvig.nl/basisregister-reisdocumenten> ([archived](https://web.archive.org/web/20260901014608/https://www.rvig.nl/basisregister-reisdocumenten))
[^s20]: wetten.overheid.nl (KOOP) — Kieswet, 2026-01-01. Kieswet. <https://wetten.overheid.nl/BWBR0004627>
[^s21]: Justitiële Informatiedienst (Justid) — Strafblad en het Justitieel Documentatie Systeem. Strafblad en het Justitieel Documentatie Systeem. <https://www.justid.nl/onderwerpen/s/strafblad-en-het-justitieel-documentatie-systeem> ([archived](https://web.archive.org/web/20260910021135/https://www.justid.nl/onderwerpen/s/strafblad-en-het-justitieel-documentatie-systeem))
[^s22]: Logius (Ministerie van BZK) — DigiD – Wie doet wat?. DigiD – Wie doet wat?. <https://www.logius.nl/onze-dienstverlening/toegang/digid/wie-doet-wat> ([archived](https://web.archive.org/web/20260413115624/https://www.logius.nl/onze-dienstverlening/toegang/digid/wie-doet-wat))
[^s23]: wetten.overheid.nl (KOOP) — Vreemdelingenwet 2000, 2026-09-01. Vreemdelingenwet 2000. <https://wetten.overheid.nl/BWBR0011823>
[^s24]: Tweede Kamer der Staten-Generaal — Douane; Brief regering; Uitstel invoering nieuw…, 2022-11-07. Douane; Brief regering; Uitstel invoering nieuw aangiftesysteem van de Douane. <https://zoek.officielebekendmakingen.nl/kst-31934-61.html>
[^s25]: Douane / Ministerie van Financiën — Douane Monitor 2024, 2025-07-08. Douane Monitor 2024. <https://zoek.officielebekendmakingen.nl/blg-1205324.pdf>
[^s26]: wetten.overheid.nl (KOOP) — Wet structuur uitvoeringsorganisatie werk en inkomen…, 2026-07-01. Wet structuur uitvoeringsorganisatie werk en inkomen (Wet SUWI). <https://wetten.overheid.nl/BWBR0013060>
[^s27]: Kamer van Koophandel (KVK) — Ultimate Beneficial Owner (UBO). Ultimate Beneficial Owner (UBO). <https://www.kvk.nl/ubo/> ([archived](https://web.archive.org/web/20260925130737/https://www.kvk.nl/ubo/))
[^s28]: wetten.overheid.nl (KOOP) — Handelsregisterwet 2007, 2025-07-16. Handelsregisterwet 2007. <https://wetten.overheid.nl/BWBR0021777>
[^s29]: Overheid.nl Wettenbank — Wegenverkeerswet 1994, 2026-09-01. Wegenverkeerswet 1994. <https://wetten.overheid.nl/BWBR0006622/2026-09-01> ([archived](https://web.archive.org/web/20260922170754/https://wetten.overheid.nl/BWBR0006622/2026-09-01))
[^s30]: Kiesraad — Evaluatieadvies Kiesraad – gemeenteraadsverkiezingen 2026, 2026-07-06. Evaluatieadvies Kiesraad – gemeenteraadsverkiezingen 2026. <https://zoek.officielebekendmakingen.nl/blg-1261396.pdf>
[^s31]: wetten.overheid.nl (KOOP) — Politiewet 2012, 2026-06-12. Politiewet 2012. <https://wetten.overheid.nl/BWBR0031788>
[^s32]: Rijksoverheid (NL-Alert / NCTV) — NL-Alert. NL-Alert. <https://www.nl-alert.nl/> ([archived](https://web.archive.org/web/20260919232645/https://www.nl-alert.nl/))
[^s33]: wetten.overheid.nl (KOOP) — Wet register onderwijsdeelnemers, 2026-08-01. Wet register onderwijsdeelnemers. <https://wetten.overheid.nl/BWBR0042012>
[^s34]: VZVZ — AORTA-LSP. AORTA-LSP. <https://www.aorta-lsp.nl/> ([archived](https://web.archive.org/web/20260710165804/https://www.aorta-lsp.nl/))
[^s35]: VZVZ — Over AORTA-LSP. Over AORTA-LSP. <https://www.aorta-lsp.nl/over-aorta-lsp> ([archived](https://web.archive.org/web/20260710170946/https://www.aorta-lsp.nl/over-aorta-lsp))
[^s36]: wetten.overheid.nl (KOOP) — Bekendmakingswet, 2024-01-01. Bekendmakingswet. <https://wetten.overheid.nl/BWBR0004287>
[^s37]: RIVM — Vaccinatiegraad Rijksvaccinatieprogramma Nederland, 2026-07-02. Vaccinatiegraad Rijksvaccinatieprogramma Nederland. <https://zoek.officielebekendmakingen.nl/blg-1258843.pdf>
[^s38]: Tweede Kamer der Staten-Generaal — Wijziging van een aantal wetten op het terrein van VWS…, 2024-10-02. Wijziging van een aantal wetten op het terrein van VWS (grondslagen gegevensverwerking); Memorie van toelichting. <https://zoek.officielebekendmakingen.nl/kst-36621-3.html> ([archived](https://web.archive.org/web/20251013160730/https://zoek.officielebekendmakingen.nl/kst-36621-3.html))
[^s39]: CBS — Microdata: Zelf onderzoek doen. Microdata: Zelf onderzoek doen. <https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen> ([archived](https://web.archive.org/web/20260923230852/https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen))

**Evidence grades:** 1 Strong, 47 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
