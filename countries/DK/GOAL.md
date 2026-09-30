# Denmark: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Denmark could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Partly[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2][^s3] |
| State-controlled national eID | Partly[^s4] |
| Government data centres | Yes[^s5][^s6] |
| Government cloud in operation | Yes[^s5] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 30 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Denmark described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.99 million[^s7] |
| GDP, current prices | 417.8 EUR bn[^s8] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 121.6 EUR/MWh[^s9] |
| Renewables share of electricity | 79.7 %[^s10] |
| Land area | 41 987 km²[^s11] |

## 3. Critical data holdings, by priority

The holdings Denmark cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 23 of 39 holding classes have a verified source; 2 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Det Centrale Personregister (CPR) - the Central Person Register[^s12] | CPR-administrationen (CPR Office), placed in the department of the Ministry of Research, Education and Digitalisation[^s13] | *Not stated in sources* | About 11.4 million persons, of which just under 6.1 million living persons[^s14] |
| Critical | Facial biometric (tier 0) | Immigration authorities' biometric register (facial photos and fingerprints of foreign nationals for residence cards); retained 20 years (10 years for visa cases)[^s15] | Ministry of Immigration and Integration, Udlændingestyrelsen and SIRI[^s15] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Immigration authorities' biometric register (fingerprints and facial photos of foreign nationals, captured for residence cards and identity control)[^s15] | Ministry of Immigration and Integration, Danish Immigration Service (Udlændingestyrelsen) and SIRI are responsible for the register[^s15] | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Kirkeministeriet's common systems for personregistrering (church registration of births, names and deaths), used by parish registrars[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | NemLog-in - the joint public digital login infrastructure through which authentications to public self-service solutions pass[^s17] | Digitaliseringsstyrelsen; NemLog-in described as a society-critical part of public digital infrastructure[^s18] | *Not stated in sources* | On average around 35 million logins per month through NemLog-in[^s19] |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | Den Danske Stat Tillidstjenester (CA1) - Danish State trust services, delivered by Digitaliseringsstyrelsen on behalf of the Danish State[^s2] | Digitaliseringsstyrelsen; CA1 is a qualified trust service provider under eIDAS on the EU trusted list[^s2] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | Politiets Efterretningstjeneste (PET) - domestic security intelligence; may collect information relevant to its activities[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Det Centrale Pasregister (Pasregistret) - Central Passport Register, with Rigspolitiet (Danish National Police) as data controller[^s21] | Rigspolitiet; retention: deleted two years after passport expiry or holder's death[^s21] | National infrastructure[^s22] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Information systems in the immigration field incl. Udlændinge Informations Systemet (UIS), used for data exchange between authorities (formerly UIP portal)[^s23] | Udlændingestyrelsen (Danish Immigration Service) receives and processes asylum and other residence permit applications[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | DMS (Declaration Management System) - customs system for import, export and transit declarations[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | Beneficial ownership data held in CVR: legal persons and trusts obliged to register beneficial owners must be registered in CVR[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Køretøjsregisteret - the national vehicle register (DMR) covering every vehicle and its ownership[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Det Centrale Kriminalregister (Kriminalregistret) - Central Criminal Register[^s21] | Rigspolitiet is data controller; regulated by the kriminalregisterbekendtgørelse[^s21] | National infrastructure[^s22] | *Not yet measured* |
| High | Police information systems (tier 1) | POLSAS - the police case management system[^s21] | *Not yet sourced* | National infrastructure[^s22] | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | Politiets Våbenregister (Police Firearms Register), Rigspolitiet data controller[^s21] | Rigspolitiet (data controller); police may also use the register for investigation and supervision of permits[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Statens Bevillings- og Regnskabsløsning (SBRL) - state appropriation and accounts solution supporting Finance Act and state accounts from FY2025[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | Election results system: municipalities enter manually counted vote totals into an IT system developed by KMD; Danmarks Statistik compiles results[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET DKK - Nationalbanken's payment system for krone settlement (via T2 and TIPS on TARGET Services, plus SPI for monetary-policy instruments and collateral)[^s30] | *Not yet sourced* | EU provider[^s30] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | SINE (Sikkerhedsnettet) - Denmark's radio network for emergency communications; use mandatory under beredskabsloven § 29[^s31] | Center for Beredskabskommunikation (CFB), part of the Ministry of Civil Security and Emergency Preparedness; network operation by Dansk Beredskabskommunikation A/S[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | Energinet carries out system-responsibility (TSO) activities, electricity transmission and gas transmission[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | Fælles Medicinkort (FMK) - Sundhedsdatastyrelsen's electronic register of every citizen's medication data (prescription, purchase, dispensing, dose changes)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Det Danske Vaccinationsregister - national register of citizens' vaccinations, run by Statens Serum Institut[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Danmarks Adresseregister (DAR) - authoritative register of road names and addresses[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 23 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 3 |
| EU provider | 1 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 19 |

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

> Not yet sized. Capacity for Denmark will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 2 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Denmark without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Electoral roll entry (tier 0)
- Tax (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Border and visa systems (tier 1)
- Official gazette and legislation (tier 1)
- Government payroll and personnel (tier 1)
- Defence command and logistics (tier 1)
- Crisis management and civil protection (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Statsministeriet / Retsinformation — Cirkulære om sikkerhedsbeskyttelse af informationer af…, 2014-12-17. Cirkulære om sikkerhedsbeskyttelse af informationer af fælles interesse for landene i NATO eller EU, andre klassificerede informationer samt informationer af sikkerhedsmæssig beskyttelsesinteresse i øvrigt (Sikkerhedscirkulæret), CIR nr. 10338 af 17/12/2014. <https://www.retsinformation.dk/eli/retsinfo/2014/10338/xml>
[^s2]: Digitaliseringsstyrelsen / Den Danske Stat Tillidstjenester — Forside - Den Danske Stat Tillidstjenester. Forside - Den Danske Stat Tillidstjenester. <https://www.ca1.gov.dk/> ([archived](https://web.archive.org/web/20260608195922/https://www.ca1.gov.dk/))
[^s3]: Digitaliseringsstyrelsen — Tilsynsorgan for Danske tillidstjenester. Tilsynsorgan for Danske tillidstjenester. <https://certifikat.gov.dk/> ([archived](https://web.archive.org/web/20251210103253/https://certifikat.gov.dk/))
[^s4]: Digitaliseringsstyrelsen — Om MitID. Om MitID. <https://digst.dk/it-loesninger/mitid/om-mitid/> ([archived](https://web.archive.org/web/20260417215119/https://digst.dk/it-loesninger/mitid/om-mitid/))
[^s5]: Statens It (Agency for Governmental IT Services, Ministry of Finance) — Statens It Årsrapport 2025, 2026. Statens It Årsrapport 2025. <https://statens-it.dk/media/0iwny3lc/statens-it-aaarsrapport-2025.pdf> ([archived](https://web.archive.org/web/20260904155709/https://statens-it.dk/media/0iwny3lc/statens-it-aaarsrapport-2025.pdf))
[^s6]: Statens It — Om Statens It. Om Statens It. <https://statens-it.dk/om-os/om-statens-it/>
[^s7]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s8]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s9]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s10]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s11]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s12]: Retsinformation / Forsknings-, Uddannelses- og Digitaliseringsministeriet — Bekendtgørelse af lov om Det Centrale Personregister…, 2023-06-23. Bekendtgørelse af lov om Det Centrale Personregister (LBK nr 1010 af 23/06/2023). <https://www.retsinformation.dk/eli/lta/2023/1010/xml>
[^s13]: CPR-kontoret — Om CPR-kontoret. Om CPR-kontoret. <https://www.cpr.dk/om-cpr-kontoret> ([archived](https://web.archive.org/web/20260517144602/https://www.cpr.dk/om-cpr-kontoret))
[^s14]: CPR-kontoret — CPR-kontoret (forside). CPR-kontoret (forside). <https://www.cpr.dk/> ([archived](https://web.archive.org/web/20260831062401/https://www.cpr.dk/))
[^s15]: Udlændingestyrelsen / SIRI (nyidanmark.dk) — Biometri – Opbevaring af fingeraftryk og ansigtsfoto. Biometri – Opbevaring af fingeraftryk og ansigtsfoto. <https://www.nyidanmark.dk/da/Ord-og-begreber/F%C3%A6lles/Biometri---Opbevaring-af-fingeraftryk-og-ansigtsfoto>
[^s16]: Retsinformation / Kirkeministeriet — Cirkulære om fælles dataansvar ... Kirkeministeriets…, 2021-06-15. Cirkulære om fælles dataansvar ... Kirkeministeriets fælles systemer vedrørende personregistrering (CIR1H nr 9447 af 15/06/2021). <https://www.retsinformation.dk/eli/retsinfo/2021/9447/xml>
[^s17]: Retsinformation / Digitaliseringsministeriet — Bekendtgørelse af lov om MitID og NemLog-in (LBK nr 333…, 2025-03-19. Bekendtgørelse af lov om MitID og NemLog-in (LBK nr 333 af 19/03/2025). <https://www.retsinformation.dk/eli/lta/2025/333/xml>
[^s18]: Digitaliseringsstyrelsen — Drift af NemLog-in sendes i udbud, 2026-01-26. Drift af NemLog-in sendes i udbud. <https://digst.dk/nyheder/nyhedsarkiv/2026/januar/drift-af-nemlog-in-sendes-i-udbud/> ([archived](https://web.archive.org/web/20260514131623/https://digst.dk/nyheder/nyhedsarkiv/2026/januar/drift-af-nemlog-in-sendes-i-udbud/))
[^s19]: Digitaliseringsstyrelsen — Tal og statistik for Digitaliseringsstyrelsens produkter, 2026-03-06. Tal og statistik for Digitaliseringsstyrelsens produkter. <https://digst.dk/tal-og-statistik/>
[^s20]: Retsinformation / Justitsministeriet — Bekendtgørelse af lov om Politiets Efterretningstjeneste…, 2017-03-07. Bekendtgørelse af lov om Politiets Efterretningstjeneste (PET) (LBK nr 231 af 07/03/2017). <https://www.retsinformation.dk/eli/lta/2017/231/xml>
[^s21]: Politi (Rigspolitiet) — Politiets brug af personoplysninger. Politiets brug af personoplysninger. <https://politi.dk/om-hjemmesiden/politiets-brug-af-personoplysninger> ([archived](https://web.archive.org/web/20260915161055/https://politi.dk/om-hjemmesiden/politiets-brug-af-personoplysninger))
[^s22]: Retsinformation / Justitsministeriet — Bekendtgørelse om hel eller delvis opbevaring her i…, 2025-03-20. Bekendtgørelse om hel eller delvis opbevaring her i landet af personoplysninger (Lokationskravsbekendtgørelsen, BEK nr 291 af 20/03/2025). <https://www.retsinformation.dk/eli/lta/2025/291/xml>
[^s23]: Udlændingestyrelsen (nyidanmark.dk) — Informationssystemer på udlændingeområdet. Informationssystemer på udlændingeområdet. <https://nyidanmark.dk/da/Collaborators/uip>
[^s24]: Danmarks Statistik — Asylansøgninger og opholdstilladelser: Statistisk behandling. Asylansøgninger og opholdstilladelser: Statistisk behandling. <https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/asylansoegninger-og-opholdstilladelser/statistisk-behandling>
[^s25]: Toldstyrelsen — DMS (Declaration Management System). DMS (Declaration Management System). <https://toldst.dk/erhverv/toldsystemer/dms>
[^s26]: Retsinformation / Erhvervsministeriet — Bekendtgørelse af lov om Det Centrale…, 2026-02-05. Bekendtgørelse af lov om Det Centrale Virksomhedsregister (LBK nr 246 af 05/02/2026). <https://www.retsinformation.dk/eli/lta/2026/246/xml>
[^s27]: Retsinformation / Skatteministeriet — Bekendtgørelse af lov om registrering af køretøjer (LBK…, 2023-02-22. Bekendtgørelse af lov om registrering af køretøjer (LBK nr 179 af 22/02/2023). <https://www.retsinformation.dk/eli/lta/2023/179/xml>
[^s28]: Økonomistyrelsen — Statens Bevillings- og Regnskabsløsning. Statens Bevillings- og Regnskabsløsning. <https://oes.dk/digitale-loesninger/statens-bevillings-og-regnskabsloesning/> ([archived](https://web.archive.org/web/20260606021813/https://oes.dk/digitale-loesninger/statens-bevillings-og-regnskabsloesning/))
[^s29]: Danmarks Statistik — Folketingsvalg, folkeafstemninger og…. Folketingsvalg, folkeafstemninger og Europa-parlamentsvalg: Præcision og pålidelighed. <https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/folketingsvalg--folkeafstemninger-og-europa-parlamentsvalg/praecision-og-paalidelighed> ([archived](https://web.archive.org/web/20260611190526/https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/folketingsvalg--folkeafstemninger-og-europa-parlamentsvalg/praecision-og-paalidelighed))
[^s30]: Danmarks Nationalbank — Overvågning af den finansielle infrastruktur 2025, 2026. Overvågning af den finansielle infrastruktur 2025. <https://www.nationalbanken.dk/da/viden-og-nyheder/publikationer-og-taler/rapport/2026/overvaagning-af-den-finansielle-infrastruktur-2025> ([archived](https://web.archive.org/web/20260513094446/https://www.nationalbanken.dk/da/viden-og-nyheder/publikationer-og-taler/rapport/2026/overvaagning-af-den-finansielle-infrastruktur-2025))
[^s31]: Center for Beredskabskommunikation — Om SINE. Om SINE. <https://sikkerhedsnet.dk/om-sine> ([archived](https://web.archive.org/web/20260710203543/https://sikkerhedsnet.dk/om-sine))
[^s32]: Center for Beredskabskommunikation — Om CFB. Om CFB. <https://sikkerhedsnet.dk/om-cfb>
[^s33]: Retsinformation / Klima-, Energi- og Forsyningsministeriet — Bekendtgørelse af lov om Energinet (LBK nr 271 af…, 2023-03-09. Bekendtgørelse af lov om Energinet (LBK nr 271 af 09/03/2023). <https://www.retsinformation.dk/eli/lta/2023/271/xml>
[^s34]: Retsinformation / Indenrigs- og Sundhedsministeriet — Bekendtgørelse af sundhedsloven (LBK nr 275 af 12/03/2025), 2025-03-12. Bekendtgørelse af sundhedsloven (LBK nr 275 af 12/03/2025). <https://www.retsinformation.dk/eli/lta/2025/275/xml>
[^s35]: Retsinformation / Styrelsen for Dataforsyning og Effektivisering — Adresseloven (LOV nr 136 af 01/02/2017), 2017-02-01. Adresseloven (LOV nr 136 af 01/02/2017). <https://www.retsinformation.dk/eli/lta/2017/136/xml>

**Evidence grades:** 2 Strong, 47 Standard. Strong: an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
