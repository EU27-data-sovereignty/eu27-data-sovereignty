# Finland: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Finland could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1] |
| Classification in law | Yes[^s2][^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s6][^s7] |
| Government data centres | Yes[^s8][^s9][^s10][^s1] |
| Government cloud in operation | Yes[^s11][^s12] |

What could move this placement:

- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Finland described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.65 million[^s13] |
| GDP, current prices | 281.8 EUR bn[^s14] |
| Public administration employment (NACE O) | 149.1 thousand[^s15] |
| Non-household electricity price | 74.8 EUR/MWh[^s16] |
| Renewables share of electricity | 56.6 %[^s17] |
| Land area | 303 109 km²[^s18] |

## 3. Critical data holdings, by priority

The holdings Finland cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 16 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Väestötietojärjestelmä (Population Information System) is the general national base register of persons, real estate, buildings and dwellings[^s19][^s20] | Digital and Population Data Services Agency (DVV) carries the controller duties for the Population Information System[^s21][^s20] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | passirekisteri (passport register)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | passirekisteri (passport register)[^s23][^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | The Population Information System includes regionally organised documentary records not taken into digital form[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | DVV must keep a log register of processing of data stored from use of the support services (incl. identification)[^s24] | *Not yet sourced* | *Not stated in sources* | About 17 million authentications per month through Suomi.fi e-Identification[^s25] |
| High | Document issuance history (tier 0) | Henkilökortti- ja passijärjestelmä, Heko-Passi (ID card and passport system)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | äänioikeusrekisteri (voting register)[^s26] | Digi- ja väestötietovirasto (Digital and Population Data Services Agency)[^s26] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | DVV keeps a certificate register of the personal certificates it issues, under the eIDAS Regulation[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | Poliisiasiaintietojärjestelmä PATJA (Police Information System)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | The aliens-affairs case management system holds data on non-visa immigration matters[^s27] | Each authority is controller for data it stores; the Finnish Immigration Service is controller for international-protection registration data[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | The registration authority keeps a public diary and document files in its information system[^s28] | The Trade Register Act names the Finnish Patent and Registration Office as registrar[^s28][^s29] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Finnish Customs receives beneficial-owner data from the PRH Trade Register[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | The national visa information system stores short- and long-term visa processing data[^s27] | *Disputed: sources disagree. Oikeusministeriö / Finlex (Ministry of Justice) — Laki henkilötietojen käsittelystä Rajavartiolaitoksessa…, 2019 gives the value this report printed; Poliisihallitus — Tietosuojaseloste; Schengenin tietojärjestelmän…, 2023-05-11 gives “Poliisihallitus (National Police Board)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Asetietojärjestelmä (firearms information system)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | The Government Shared Services Centre for Finance and HR holds data on central-government agencies' financial and HR administration[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
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
| Standard | Geospatial base data (tier 3) | Building data are recorded in the Population Information System[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 16 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 16 |

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

> Not yet sized. Capacity for Finland will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Finland without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Land & property registry (tier 1)
- Vehicle & licensing (tier 1)
- Judicial & criminal justice (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
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

[^s1]: Finlex / Oikeusministeriö — Laki turvallisuusverkkotoiminnasta (10/2015), 5 §. Laki turvallisuusverkkotoiminnasta (10/2015), 5 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2015/10/fin@>
[^s2]: Finlex / Oikeusministeriö — Valtioneuvoston asetus asiakirjojen…. Valtioneuvoston asetus asiakirjojen turvallisuusluokittelusta valtionhallinnossa (1101/2019), 3 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2019/1101/fin@>
[^s3]: Finlex / oikeusministeriö — Laki julkisen hallinnon tiedonhallinnasta 906/2019…. Laki julkisen hallinnon tiedonhallinnasta 906/2019 (ajantasainen). <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2019/906/fin@>
[^s4]: Digital and Population Data Services Agency (DVV) — CA Certificates. CA Certificates. <https://dvv.fi/en/ca-certificates> ([archived](https://web.archive.org/web/20260202204257/https://dvv.fi/en/ca-certificates))
[^s5]: Finlex / Oikeusministeriö — Laki väestötietojärjestelmästä ja…. Laki väestötietojärjestelmästä ja Väestörekisterikeskuksen varmennepalveluista (661/2009), 61 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute/2009/661/fin@>
[^s6]: Digi- ja väestötietovirasto (DVV) — Tunnistus (Suomi.fi-tunnistus). Tunnistus (Suomi.fi-tunnistus). <https://dvv.fi/suomi.fi-tunnistus>
[^s7]: Finlex / Oikeusministeriö — Laki hallinnon yhteisistä sähköisen asioinnin…. Laki hallinnon yhteisistä sähköisen asioinnin tukipalveluista (571/2016), 4 §. <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2016/571/fin@>
[^s8]: Suomen Erillisverkot Oy — Suomalainen data turvaan Suomeen, 2019-04-23. Suomalainen data turvaan Suomeen. <https://www.erillisverkot.fi/suomalainen-data-turvaan-suomeen/> ([archived](https://web.archive.org/web/20260510201952/https://www.erillisverkot.fi/suomalainen-data-turvaan-suomeen/))
[^s9]: Suomen Erillisverkot Oy — Erillisverkkojen vuosikertomus 2025, 2026. Erillisverkkojen vuosikertomus 2025. <https://www.erillisverkot.fi/vuosikertomus-2025/> ([archived](https://web.archive.org/web/20260727163800/https://www.erillisverkot.fi/vuosikertomus-2025/))
[^s10]: Suomen Erillisverkot Oy — Konesalipalvelu. Konesalipalvelu. <https://www.erillisverkot.fi/palvelut/konesali-ja-suojatilat/> ([archived](https://web.archive.org/web/20260727163800/https://www.erillisverkot.fi/palvelut/konesali-ja-suojatilat/))
[^s11]: Suomen Erillisverkot Oy — Turvapilvipalvelu (Virtuaalinen konesalipalvelu). Turvapilvipalvelu (Virtuaalinen konesalipalvelu). <https://www.erillisverkot.fi/palvelut/virtuaalinen-konesali/> ([archived](https://web.archive.org/web/20260727163800/https://www.erillisverkot.fi/palvelut/virtuaalinen-konesali/))
[^s12]: Suomen Erillisverkot Oy — Turvapilvipalvelu – täysin kotimainen pilvipalvelu ja…, 2021-12-03. Turvapilvipalvelu – täysin kotimainen pilvipalvelu ja tiedon turvasatama. <https://www.erillisverkot.fi/turvapilvipalvelu-taysin-kotimainen-pilvipalvelu-ja-tiedon-turvasatama/> ([archived](https://web.archive.org/web/20260419203958/https://www.erillisverkot.fi/turvapilvipalvelu-taysin-kotimainen-pilvipalvelu-ja-tiedon-turvasatama/))
[^s13]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s14]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s15]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s16]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s17]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s18]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s19]: Digital and Population Data Services Agency (DVV) — Population Information System. Population Information System. <https://dvv.fi/en/population-information-system> ([archived](https://web.archive.org/web/20260512125439/https://dvv.fi/en/population-information-system))
[^s20]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki väestötietojärjestelmästä ja Digi- ja…, 2009. Laki väestötietojärjestelmästä ja Digi- ja väestötietoviraston varmennepalveluista (661/2009). <https://www.finlex.fi/fi/lainsaadanto/2009/661> ([archived](https://web.archive.org/web/20260522204328/https://www.finlex.fi/fi/lainsaadanto/2009/661))
[^s21]: Digi- ja väestötietovirasto — Väestötietojärjestelmän tietosuojaseloste. Väestötietojärjestelmän tietosuojaseloste. <https://dvv.fi/vtj-tietosuoja> ([archived](https://web.archive.org/web/20260831170900/https://dvv.fi/vtj-tietosuoja))
[^s22]: Poliisihallitus — Poliisin asiakirjajulkisuuskuvaus, 2021-06-30. Poliisin asiakirjajulkisuuskuvaus. <https://poliisi.fi/documents/25235045/26823782/Poliisin+asiakirjajulkisuuskuvaus.pdf/0bc008c3-7106-fa8b-89a1-fb01b8088e8d?t=1630301434861>
[^s23]: Poliisi — Sormenjäljet matkustusoikeudelliselle henkilökortille. Sormenjäljet matkustusoikeudelliselle henkilökortille. <https://poliisi.fi/neuvontapalvelu/-/asset_publisher/ZtAEeHB39Lxr/content/sormenjaljet-matkustusoikeudelliselle-henkilokortille>
[^s24]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki hallinnon yhteisistä sähköisen asioinnin…, 2016. Laki hallinnon yhteisistä sähköisen asioinnin tukipalveluista (571/2016). <https://www.finlex.fi/fi/lainsaadanto/2016/571> ([archived](https://web.archive.org/web/20260919081102/https://www.finlex.fi/fi/lainsaadanto/2016/571))
[^s25]: Digi- ja väestötietovirasto (DVV), via STT Info — Digi- ja väestötietovirasto valitsi vahvan tunnistamisen…, 2024-01-31. Digi- ja väestötietovirasto valitsi vahvan tunnistamisen välityspalveluntarjoajaksi Telia Finland Oyj:n. <https://www.sttinfo.fi/tiedote/70085553/digi-ja-vaestotietovirasto-valitsi-vahvan-tunnistamisen-valityspalveluntarjoajaksi-telia-finland-oyjn?publisherId=3777&lang=fi> ([archived](https://web.archive.org/web/20240202092418/https://www.sttinfo.fi/tiedote/70085553/digi-ja-vaestotietovirasto-valitsi-vahvan-tunnistamisen-valityspalveluntarjoajaksi-telia-finland-oyjn?publisherId=3777&lang=fi))
[^s26]: Digi- ja väestötietovirasto — Äänioikeusrekisterin tietosuojaseloste. Äänioikeusrekisterin tietosuojaseloste. <https://dvv.fi/aanioikeusrekisterin-tietosuoja> ([archived](https://web.archive.org/web/20260529172204/https://dvv.fi/aanioikeusrekisterin-tietosuoja))
[^s27]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki henkilötietojen käsittelystä…, 2020. Laki henkilötietojen käsittelystä maahanmuuttohallinnossa (615/2020). <https://www.finlex.fi/fi/lainsaadanto/2020/615> ([archived](https://web.archive.org/web/20260421162858/https://www.finlex.fi/fi/lainsaadanto/2020/615))
[^s28]: Oikeusministeriö / Finlex (Ministry of Justice) — Kaupparekisterilaki (564/2023), 2023. Kaupparekisterilaki (564/2023). <https://www.finlex.fi/fi/lainsaadanto/2023/564> ([archived](https://web.archive.org/web/20251010152906/https://www.finlex.fi/fi/lainsaadanto/2023/564))
[^s29]: Finlex / oikeusministeriö — Kaupparekisterilaki 564/2023 (ajantasainen). Kaupparekisterilaki 564/2023 (ajantasainen). <https://opendata.finlex.fi/finlex/avoindata/v1/akn/fi/act/statute-consolidated/2023/564/fin@>
[^s30]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki henkilötietojen käsittelystä Tullissa (650/2019), 2019. Laki henkilötietojen käsittelystä Tullissa (650/2019). <https://www.finlex.fi/fi/lainsaadanto/2019/650> ([archived](https://web.archive.org/web/20260205004618/https://www.finlex.fi/fi/lainsaadanto/2019/650))
[^s31]: Oikeusministeriö / Finlex (Ministry of Justice) — Laki Valtiokonttorista (305/1991), 1991. Laki Valtiokonttorista (305/1991). <https://www.finlex.fi/fi/lainsaadanto/1991/305> ([archived](https://web.archive.org/web/20260411111736/https://www.finlex.fi/fi/lainsaadanto/1991/305))

**Evidence grades:** 2 Strong, 31 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
