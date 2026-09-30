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
| Sovereign cloud certification | No[^s2] |
| State-controlled trust anchor | Yes[^s3][^s4] |
| State-controlled national eID | Yes[^s3][^s5] |
| Government data centres | Yes[^s6][^s7] |
| Government cloud in operation | Yes[^s6][^s8][^s7] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 32 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Netherlands described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 18.04 million[^s9] |
| GDP, current prices | 1 170.6 EUR bn[^s10] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 199.1 EUR/MWh[^s11] |
| Renewables share of electricity | 50.5 %[^s12] |
| Land area | 34 188 km²[^s13] |

## 3. Critical data holdings, by priority

The holdings Netherlands cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 12 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Basisregistratie Personen (BRP)[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Issuing authorities keep a travel document administration containing the data of art. 3 paras 1-2 (incl. facial image)[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s15] | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | TSPs issue certificates under the State of the Netherlands trust anchor[^s4] | PKIoverheid is a trust framework managed by Logius on behalf of Ministry of BZK[^s4] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Basisregistratie Kadaster (BRK)[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | DigiD: the national means for citizens to identify digitally[^s5] | Minister of BZK is controller; DigiD is managed by Logius[^s17] | National infrastructure[^s17] | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | Current declaration system AGS is being replaced by the new DMS[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Handelsregister[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | Art. 126: driving licence register managed by RDW[^s20] | RDW manages and is controller of the vehicle registration register[^s20] | *Not stated in sources* | *Not yet measured* |
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
| High | Health records (tier 2) | LSP is a national infrastructure through which care providers exchange patients' medical data[^s21] | AORTA/LSP managed by VZVZ since 2012[^s22] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Praeventis centrally registers vaccinations of every participant in the national immunisation programme[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Microdata: linkable person, business and address-level data for authorised researchers[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 11 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 1 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 10 |

## 5. Legal and institutional posture

1 of 8 posture entries have a verified source. The others were researched from public policy documents but are withheld here until each is checked against the governing instrument.

| Dimension | Position |
|---|---|
| Governing instrument | *Not yet sourced* |
| Sovereign or government cloud | *Not yet sourced* |
| Cloud certification | *Not yet sourced* |
| Data classification | VIRBI 2013: Departementaal VERTROUWELIJK / CONFIDENTIEEL / GEHEIM / ZEER GEHEIM[^s25] |
| Procurement route | *Not yet sourced* |
| National digital identity | *Not yet sourced* |
| Internet exchange | *Not yet sourced* |
| Hyperscaler regions in country | *Not yet sourced* |

## 6. Capacity

> Not yet sized. Capacity for Netherlands will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Netherlands without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Breeder document scans (tier 0)
- Document issuance history (tier 0)
- Authentication audit log (tier 0)
- Electoral roll entry (tier 0)
- Residence and migration status (tier 1)
- Tax (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Beneficial ownership register (tier 1)
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

[^s1]: Ministerie van Algemene Zaken / Staatscourant — Besluit voorschrift informatiebeveiliging Rijksdienst…, 2025-09-08. Besluit voorschrift informatiebeveiliging Rijksdienst bijzondere informatie 2025 (VIRBI 2025), Staatscourant 2025, 30222. <https://zoek.officielebekendmakingen.nl/stcrt-2025-30222.html>
[^s2]: Tweede Kamer der Staten-Generaal (letter from the State Secretary of Economic Affairs and Climate) — Kamerstuk 26643 nr. 1542 - Nationaal beleid voor de…, 2026-07. Kamerstuk 26643 nr. 1542 - Nationaal beleid voor de Nederlandse cloudmarkt. <https://zoek.officielebekendmakingen.nl/kst-1263281.pdf>
[^s3]: Logius — Onze organisatie. Onze organisatie. <https://www.logius.nl/over-ons/onze-organisatie> ([archived](https://web.archive.org/web/20260519142506/https://www.logius.nl/over-ons/onze-organisatie))
[^s4]: Logius — Wat is PKIoverheid. Wat is PKIoverheid. <https://www.logius.nl/onze-dienstverlening/toegang/pkioverheid/wat-pkioverheid> ([archived](https://web.archive.org/web/20260618011710/https://www.logius.nl/onze-dienstverlening/toegang/pkioverheid/wat-pkioverheid))
[^s5]: Logius — DigiD. DigiD. <https://www.logius.nl/onze-dienstverlening/toegang/digid> ([archived](https://web.archive.org/web/20260826221154/https://www.logius.nl/onze-dienstverlening/toegang/digid))
[^s6]: ODC-Noord (Rijksoverheid, SSO-Noord) — Organisatie - ODC-Noord. Organisatie - ODC-Noord. <https://www.odc-noord.nl/Organisatie> ([archived](https://web.archive.org/web/20260226165411/https://www.odc-noord.nl/Organisatie))
[^s7]: Tweede Kamer der Staten-Generaal (letter from the State Secretary of the Interior and Kingdom Relations) — Kamerstuk 26643 nr. 1537 - Stand van zaken verkenning…, 2026-07-01. Kamerstuk 26643 nr. 1537 - Stand van zaken verkenning soevereine overheidscloud. <https://zoek.officielebekendmakingen.nl/kst-1263099.pdf>
[^s8]: ODC-Noord (Rijksoverheid, SSO-Noord) — Infrastructure as a Service - ODC-Noord. Infrastructure as a Service - ODC-Noord. <https://www.odc-noord.nl/diensten/infrastructure-as-a-service> ([archived](https://web.archive.org/web/20260228011002/https://www.odc-noord.nl/diensten/infrastructure-as-a-service))
[^s9]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s10]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s11]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s12]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s13]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s14]: Rijksdienst voor Identiteitsgegevens (RvIG) brp. Basisregistratie Personen | RvIG. <https://www.rvig.nl/basisregistratie-personen>
[^s15]: Overheid.nl Wettenbank — Paspoortwet, 2024-01-01. Paspoortwet. <https://wetten.overheid.nl/BWBR0005212/2024-01-01> ([archived](https://web.archive.org/web/20260928030739/https://wetten.overheid.nl/BWBR0005212/2024-01-01/))
[^s16]: Kadaster brk. Waar bestaat de BRK uit? - Kadaster.nl zakelijk. <https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk>
[^s17]: DigiD / Logius — Privacy DigiD. Privacy DigiD. <https://www.digid.nl/over-digid/privacy> ([archived](https://web.archive.org/web/20260927120423/https://www.digid.nl/over-digid/privacy))
[^s18]: Tweede Kamer der Staten-Generaal — Douane; Brief regering; Uitstel invoering nieuw…, 2022-11-07. Douane; Brief regering; Uitstel invoering nieuw aangiftesysteem van de Douane. <https://zoek.officielebekendmakingen.nl/kst-31934-61.html>
[^s19]: Kamer van Koophandel (KVK) handelsregister. Over het Handelsregister | KVK. <https://www.kvk.nl/over-het-handelsregister/>
[^s20]: Overheid.nl Wettenbank — Wegenverkeerswet 1994, 2026-09-01. Wegenverkeerswet 1994. <https://wetten.overheid.nl/BWBR0006622/2026-09-01> ([archived](https://web.archive.org/web/20260922170754/https://wetten.overheid.nl/BWBR0006622/2026-09-01))
[^s21]: VZVZ — AORTA-LSP. AORTA-LSP. <https://www.aorta-lsp.nl/> ([archived](https://web.archive.org/web/20260710165804/https://www.aorta-lsp.nl/))
[^s22]: VZVZ — Over AORTA-LSP. Over AORTA-LSP. <https://www.aorta-lsp.nl/over-aorta-lsp> ([archived](https://web.archive.org/web/20260710170946/https://www.aorta-lsp.nl/over-aorta-lsp))
[^s23]: Tweede Kamer der Staten-Generaal — Wijziging van een aantal wetten op het terrein van VWS…, 2024-10-02. Wijziging van een aantal wetten op het terrein van VWS (grondslagen gegevensverwerking); Memorie van toelichting. <https://zoek.officielebekendmakingen.nl/kst-36621-3.html> ([archived](https://web.archive.org/web/20251013160730/https://zoek.officielebekendmakingen.nl/kst-36621-3.html))
[^s24]: CBS — Microdata: Zelf onderzoek doen. Microdata: Zelf onderzoek doen. <https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen> ([archived](https://web.archive.org/web/20260923230852/https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen))
[^s25]: Overheid.nl Wettenbank bwbr0033507, 2013-06-01. Besluit Voorschrift Informatiebeveiliging Rijksdienst Bijzondere Informatie 2013 (VIRBI 2013). <https://wetten.overheid.nl/BWBR0033507/2013-06-01>
