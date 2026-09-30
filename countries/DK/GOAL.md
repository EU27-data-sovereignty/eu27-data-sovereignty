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

> Not demonstrated. Confidence: Medium. With the evidence still open, Denmark could be anywhere from 'Not demonstrated' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1] |
| Classification in law | Partly[^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4][^s5] |
| State-controlled national eID | Partly[^s6] |
| Government data centres | Yes[^s7][^s8][^s9] |
| Government cloud in operation | Yes[^s10][^s8] |

What could move this placement:

- If any of the 30 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Denmark described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 6.03 million[^s11] |
| GDP, current prices | 417.8 EUR bn[^s12] |
| Public administration employment (NACE O) | 169.8 thousand[^s13] |
| Non-household electricity price | 121.6 EUR/MWh[^s14] |
| Renewables share of electricity | 77.7 %[^s15] |
| Land area | 41 987 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Denmark cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 28 of 39 holding classes have a verified source; 4 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Det Centrale Personregister (CPR) - the Central Person Register[^s17] | CPR-administrationen (CPR Office), placed in the department of the Ministry of Research, Education and Digitalisation[^s18][^s17] | *Not stated in sources* | About 11.4 million persons, of which just under 6.1 million living persons[^s19] |
| Critical | Facial biometric (tier 0) | Immigration authorities' biometric register (facial photos and fingerprints of foreign nationals for residence cards); retained 20 years (10 years for visa cases)[^s20] | Ministry of Immigration and Integration, Udlændingestyrelsen and SIRI[^s20][^s21] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Immigration authorities' biometric register (fingerprints and facial photos of foreign nationals, captured for residence cards and identity control)[^s20] | Ministry of Immigration and Integration, Danish Immigration Service (Udlændingestyrelsen) and SIRI are responsible for the register[^s20][^s21] | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Kirkeministeriet's common systems for personregistrering (church registration of births, names and deaths), used by parish registrars[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | NemLog-in - the joint public digital login infrastructure through which authentications to public self-service solutions pass[^s23][^s24] | Digitaliseringsstyrelsen; NemLog-in described as a society-critical part of public digital infrastructure[^s25][^s26] | *Not stated in sources* | On average around 35 million logins per month through NemLog-in[^s27] |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | Den Danske Stat Tillidstjenester (CA1) - Danish State trust services, delivered by Digitaliseringsstyrelsen on behalf of the Danish State[^s3] | Digitaliseringsstyrelsen; CA1 is a qualified trust service provider under eIDAS on the EU trusted list[^s3] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | Politiets Efterretningstjeneste (PET) - domestic security intelligence; may collect information relevant to its activities[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Det Centrale Pasregister (Pasregistret) - Central Passport Register, with Rigspolitiet (Danish National Police) as data controller[^s29][^s30] | Rigspolitiet; retention: deleted two years after passport expiry or holder's death[^s29] | National infrastructure[^s1] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Information systems in the immigration field incl. Udlændinge Informations Systemet (UIS), used for data exchange between authorities (formerly UIP portal)[^s31] | Udlændingestyrelsen (Danish Immigration Service) receives and processes asylum and other residence permit applications[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | DMS (Declaration Management System) - customs system for import, export and transit declarations[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | sundhedskort and sikringsgruppe enrolment based on Det Centrale Personregister (CPR) (health insurance card and coverage group registration)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | Beneficial ownership data held in CVR: legal persons and trusts obliged to register beneficial owners must be registered in CVR[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Køretøjsregisteret - the national vehicle register (DMR) covering every vehicle and its ownership[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Det Centrale Kriminalregister (Kriminalregistret) - Central Criminal Register[^s29][^s37] | Rigspolitiet is data controller; regulated by the kriminalregisterbekendtgørelse[^s29] | National infrastructure[^s1] | *Not yet measured* |
| High | Police information systems (tier 1) | POLSAS - the police case management system[^s29][^s1] | *Not yet sourced* | National infrastructure[^s1] | *Not yet measured* |
| High | Border and visa systems (tier 1) | Schengeninformationssystemet (SIS, Schengen Information System)[^s38] | Udlændingestyrelsen (Danish Immigration Service), for SIS return alerts[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Politiets Våbenregister (Police Firearms Register), Rigspolitiet data controller[^s29][^s39] | Rigspolitiet (data controller); police may also use the register for investigation and supervision of permits[^s29][^s39] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Statens Bevillings- og Regnskabsløsning (SBRL) - state appropriation and accounts solution supporting Finance Act and state accounts from FY2025[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Statens Lønløsning (the State Payroll Solution)[^s41] | Økonomistyrelsen (Agency for Public Finance and Management)[^s42] | *Not stated in sources* | ca. 180.000 statslige ansatte (state employees paid each month)[^s41] |
| High | Election management and results (tier 1) | Election results system: municipalities enter manually counted vote totals into an IT system developed by KMD; Danmarks Statistik compiles results[^s43] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET DKK - Nationalbanken's payment system for krone settlement (via T2 and TIPS on TARGET Services, plus SPI for monetary-policy instruments and collateral)[^s44][^s45] | *Not yet sourced* | EU provider[^s44][^s45] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | SINE (Sikkerhedsnettet) - Denmark's radio network for emergency communications; use mandatory under beredskabsloven § 29[^s46] | Center for Beredskabskommunikation (CFB), part of the Ministry of Civil Security and Emergency Preparedness; network operation by Dansk Beredskabskommunikation A/S[^s47] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Sirenevarslingssystemet (the national siren warning system)[^s48] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Energinet carries out system-responsibility (TSO) activities, electricity transmission and gas transmission[^s49] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | STADS (the university student administration system)[^s50] | *Not yet sourced* | *Not stated in sources* | Omkring 100.000 studerende (students)[^s50] |
| High | Health records (tier 2) | Fælles Medicinkort (FMK) - Sundhedsdatastyrelsen's electronic register of every citizen's medication data (prescription, purchase, dispensing, dose changes)[^s51][^s52] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Det Danske Vaccinationsregister - national register of citizens' vaccinations, run by Statens Serum Institut[^s51] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Danmarks Adresseregister (DAR) - authoritative register of road names and addresses[^s53] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 28 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 3 |
| EU provider | 1 |
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

> Not yet sized. Capacity for Denmark will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 4 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Denmark without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Electoral roll entry (tier 0)
- Tax (tier 1)
- Benefits & pensions (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Official gazette and legislation (tier 1)
- Defence command and logistics (tier 1)
- Water management control (tier 1)

---

[^s1]: Retsinformation / Justitsministeriet — Bekendtgørelse om hel eller delvis opbevaring her i…, 2025-03-20. Bekendtgørelse om hel eller delvis opbevaring her i landet af personoplysninger (Lokationskravsbekendtgørelsen, BEK nr 291 af 20/03/2025). <https://www.retsinformation.dk/eli/lta/2025/291/xml>
[^s2]: Statsministeriet / Retsinformation — Cirkulære om sikkerhedsbeskyttelse af informationer af…, 2014-12-17. Cirkulære om sikkerhedsbeskyttelse af informationer af fælles interesse for landene i NATO eller EU, andre klassificerede informationer samt informationer af sikkerhedsmæssig beskyttelsesinteresse i øvrigt (Sikkerhedscirkulæret), CIR nr. 10338 af 17/12/2014. <https://www.retsinformation.dk/eli/retsinfo/2014/10338/xml>
[^s3]: Digitaliseringsstyrelsen / Den Danske Stat Tillidstjenester — Forside - Den Danske Stat Tillidstjenester. Forside - Den Danske Stat Tillidstjenester. <https://www.ca1.gov.dk/> ([archived](https://web.archive.org/web/20260608195922/https://www.ca1.gov.dk/))
[^s4]: Digitaliseringsstyrelsen — Tilsynsorgan for Danske tillidstjenester. Tilsynsorgan for Danske tillidstjenester. <https://certifikat.gov.dk/> ([archived](https://web.archive.org/web/20251210103253/https://certifikat.gov.dk/))
[^s5]: Digitaliseringsstyrelsen (Den Danske Stat Tillidstjenester) — Den Danske Stat Tillidstjenester - Vilkår for…. Den Danske Stat Tillidstjenester - Vilkår for kvalificerede personsignaturer 1.2. <https://cms.nemlog-in.dk/media/jqebfp5j/vilka-r-kvalificerede-personsignaturer-1-2.pdf> ([archived](https://web.archive.org/web/20240630032003/https://cms.nemlog-in.dk/media/jqebfp5j/vilka-r-kvalificerede-personsignaturer-1-2.pdf))
[^s6]: Digitaliseringsstyrelsen — Om MitID. Om MitID. <https://digst.dk/it-loesninger/mitid/om-mitid/> ([archived](https://web.archive.org/web/20260417215119/https://digst.dk/it-loesninger/mitid/om-mitid/))
[^s7]: Statens It — Om GovCloud. Om GovCloud. <https://govcloud.dk/om-govcloud/> ([archived](https://web.archive.org/web/20260121215411/https://govcloud.dk/om-govcloud/))
[^s8]: Statens It (Agency for Governmental IT Services, Ministry of Finance) — Statens It Årsrapport 2025, 2026. Statens It Årsrapport 2025. <https://statens-it.dk/media/0iwny3lc/statens-it-aaarsrapport-2025.pdf> ([archived](https://web.archive.org/web/20260904155709/https://statens-it.dk/media/0iwny3lc/statens-it-aaarsrapport-2025.pdf))
[^s9]: Statens It — Om Statens It. Om Statens It. <https://statens-it.dk/om-os/om-statens-it/>
[^s10]: Statens It — GovCloud fra Statens It. GovCloud fra Statens It. <https://govcloud.dk/> ([archived](https://web.archive.org/web/20260520192843/https://govcloud.dk/))
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Retsinformation / Forsknings-, Uddannelses- og Digitaliseringsministeriet — Bekendtgørelse af lov om Det Centrale Personregister…, 2023-06-23. Bekendtgørelse af lov om Det Centrale Personregister (LBK nr 1010 af 23/06/2023). <https://www.retsinformation.dk/eli/lta/2023/1010/xml>
[^s18]: CPR-kontoret — Om CPR-kontoret. Om CPR-kontoret. <https://www.cpr.dk/om-cpr-kontoret> ([archived](https://web.archive.org/web/20260517144602/https://www.cpr.dk/om-cpr-kontoret))
[^s19]: CPR-kontoret — CPR-kontoret (forside). CPR-kontoret (forside). <https://www.cpr.dk/> ([archived](https://web.archive.org/web/20260831062401/https://www.cpr.dk/))
[^s20]: Udlændingestyrelsen / SIRI (nyidanmark.dk) — Biometri – Opbevaring af fingeraftryk og ansigtsfoto. Biometri – Opbevaring af fingeraftryk og ansigtsfoto. <https://www.nyidanmark.dk/da/Ord-og-begreber/F%C3%A6lles/Biometri---Opbevaring-af-fingeraftryk-og-ansigtsfoto>
[^s21]: Retsinformation / Udlændinge- og Integrationsministeriet — Bekendtgørelse af udlændingeloven (LBK nr 1183 af…, 2025-09-25. Bekendtgørelse af udlændingeloven (LBK nr 1183 af 25/09/2025). <https://www.retsinformation.dk/eli/lta/2025/1183/xml>
[^s22]: Retsinformation / Kirkeministeriet — Cirkulære om fælles dataansvar ... Kirkeministeriets…, 2021-06-15. Cirkulære om fælles dataansvar ... Kirkeministeriets fælles systemer vedrørende personregistrering (CIR1H nr 9447 af 15/06/2021). <https://www.retsinformation.dk/eli/retsinfo/2021/9447/xml>
[^s23]: Agency for Digital Government (Digitaliseringsstyrelsen) — NemLog-in. NemLog-in. <https://en.digst.dk/systems/nemlog-in/> ([archived](https://web.archive.org/web/20260910172930/https://en.digst.dk/systems/nemlog-in/))
[^s24]: Retsinformation / Digitaliseringsministeriet — Bekendtgørelse af lov om MitID og NemLog-in (LBK nr 333…, 2025-03-19. Bekendtgørelse af lov om MitID og NemLog-in (LBK nr 333 af 19/03/2025). <https://www.retsinformation.dk/eli/lta/2025/333/xml>
[^s25]: Digitaliseringsstyrelsen — Drift af NemLog-in sendes i udbud, 2026-01-26. Drift af NemLog-in sendes i udbud. <https://digst.dk/nyheder/nyhedsarkiv/2026/januar/drift-af-nemlog-in-sendes-i-udbud/> ([archived](https://web.archive.org/web/20260514131623/https://digst.dk/nyheder/nyhedsarkiv/2026/januar/drift-af-nemlog-in-sendes-i-udbud/))
[^s26]: Digitaliseringsstyrelsen — NemLog-in Privatlivspolitik, 2025-12-08. NemLog-in Privatlivspolitik. <https://digst.dk/it-loesninger/nemlog-in/om-loesningen/persondata/> ([archived](https://web.archive.org/web/20260514133820/https://digst.dk/it-loesninger/nemlog-in/om-loesningen/persondata/))
[^s27]: Digitaliseringsstyrelsen — Tal og statistik for Digitaliseringsstyrelsens produkter, 2026-03-06. Tal og statistik for Digitaliseringsstyrelsens produkter. <https://digst.dk/tal-og-statistik/>
[^s28]: Retsinformation / Justitsministeriet — Bekendtgørelse af lov om Politiets Efterretningstjeneste…, 2017-03-07. Bekendtgørelse af lov om Politiets Efterretningstjeneste (PET) (LBK nr 231 af 07/03/2017). <https://www.retsinformation.dk/eli/lta/2017/231/xml>
[^s29]: Politi (Rigspolitiet) — Politiets brug af personoplysninger. Politiets brug af personoplysninger. <https://politi.dk/om-hjemmesiden/politiets-brug-af-personoplysninger> ([archived](https://web.archive.org/web/20260915161055/https://politi.dk/om-hjemmesiden/politiets-brug-af-personoplysninger))
[^s30]: Retsinformation / Justitsministeriet — Bekendtgørelse om pas m.v. (BEK nr 2693 af 28/12/2021), 2021-12-28. Bekendtgørelse om pas m.v. (BEK nr 2693 af 28/12/2021). <https://www.retsinformation.dk/eli/lta/2021/2693/xml>
[^s31]: Udlændingestyrelsen (nyidanmark.dk) — Informationssystemer på udlændingeområdet. Informationssystemer på udlændingeområdet. <https://nyidanmark.dk/da/Collaborators/uip>
[^s32]: Danmarks Statistik — Asylansøgninger og opholdstilladelser: Statistisk behandling. Asylansøgninger og opholdstilladelser: Statistisk behandling. <https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/asylansoegninger-og-opholdstilladelser/statistisk-behandling>
[^s33]: Toldstyrelsen — DMS (Declaration Management System). DMS (Declaration Management System). <https://toldst.dk/erhverv/toldsystemer/dms>
[^s34]: Retsinformation / Indenrigs- og Sundhedsministeriet — Bekendtgørelse om valgfri indplacering i sikringsgrupper…, 2025-05-21. Bekendtgørelse om valgfri indplacering i sikringsgrupper og udstedelse af sundhedskort m.v.. <https://www.retsinformation.dk/eli/lta/2025/529/xml>
[^s35]: Retsinformation / Erhvervsministeriet — Bekendtgørelse af lov om Det Centrale…, 2026-02-05. Bekendtgørelse af lov om Det Centrale Virksomhedsregister (LBK nr 246 af 05/02/2026). <https://www.retsinformation.dk/eli/lta/2026/246/xml>
[^s36]: Retsinformation / Skatteministeriet — Bekendtgørelse af lov om registrering af køretøjer (LBK…, 2023-02-22. Bekendtgørelse af lov om registrering af køretøjer (LBK nr 179 af 22/02/2023). <https://www.retsinformation.dk/eli/lta/2023/179/xml>
[^s37]: Retsinformation / Justitsministeriet — Bekendtgørelse om behandling af personoplysninger i Det…, 2026-06-22. Bekendtgørelse om behandling af personoplysninger i Det Centrale Kriminalregister (Kriminalregisteret). <https://www.retsinformation.dk/eli/lta/2026/589/xml>
[^s38]: Retsinformation / Udlændinge- og Integrationsministeriet — Bekendtgørelse om udlændingemyndighedernes kompetence…, 2025-09-30. Bekendtgørelse om udlændingemyndighedernes kompetence til at indberette tilbagesendelsesafgørelser ... i medfør af SIS-tilbagesendelsesforordningen. <https://www.retsinformation.dk/eli/lta/2025/1201/xml>
[^s39]: Retsinformation / Justitsministeriet — Cirkulære om våben og ammunition m.v., 2025-10-29. Cirkulære om våben og ammunition m.v.. <https://www.retsinformation.dk/eli/retsinfo/2025/10066/xml>
[^s40]: Økonomistyrelsen — Statens Bevillings- og Regnskabsløsning. Statens Bevillings- og Regnskabsløsning. <https://oes.dk/digitale-loesninger/statens-bevillings-og-regnskabsloesning/> ([archived](https://web.archive.org/web/20260606021813/https://oes.dk/digitale-loesninger/statens-bevillings-og-regnskabsloesning/))
[^s41]: Økonomistyrelsen — Lønudbetaling med Statens Lønløsning. Lønudbetaling med Statens Lønløsning. <https://oes.dk/digitale-loesninger/statens-loenloesning/> ([archived](https://web.archive.org/web/20260629120521/https://oes.dk/digitale-loesninger/statens-loenloesning/))
[^s42]: Økonomistyrelsen — Statens nye lønsystem under udvikling. Statens nye lønsystem under udvikling. <https://oes.dk/digitale-loesninger/udvikling-og-udbud/statens-nye-loensystem-under-udvikling/>
[^s43]: Danmarks Statistik — Folketingsvalg, folkeafstemninger og…. Folketingsvalg, folkeafstemninger og Europa-parlamentsvalg: Præcision og pålidelighed. <https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/folketingsvalg--folkeafstemninger-og-europa-parlamentsvalg/praecision-og-paalidelighed> ([archived](https://web.archive.org/web/20260611190526/https://www.dst.dk/da/Statistik/dokumentation/statistikdokumentation/folketingsvalg--folkeafstemninger-og-europa-parlamentsvalg/praecision-og-paalidelighed))
[^s44]: European Central Bank — Danish krone now available in all TARGET Services, 2025-04-23. Danish krone now available in all TARGET Services. <https://www.ecb.europa.eu/press/pr/date/2025/html/ecb.pr250423~096ce05219.en.html>
[^s45]: Danmarks Nationalbank — Overvågning af den finansielle infrastruktur 2025, 2026. Overvågning af den finansielle infrastruktur 2025. <https://www.nationalbanken.dk/da/viden-og-nyheder/publikationer-og-taler/rapport/2026/overvaagning-af-den-finansielle-infrastruktur-2025> ([archived](https://web.archive.org/web/20260513094446/https://www.nationalbanken.dk/da/viden-og-nyheder/publikationer-og-taler/rapport/2026/overvaagning-af-den-finansielle-infrastruktur-2025))
[^s46]: Center for Beredskabskommunikation — Om SINE. Om SINE. <https://sikkerhedsnet.dk/om-sine> ([archived](https://web.archive.org/web/20260710203543/https://sikkerhedsnet.dk/om-sine))
[^s47]: Center for Beredskabskommunikation — Om CFB. Om CFB. <https://sikkerhedsnet.dk/om-cfb>
[^s48]: Beredskabsstyrelsen — Sirenevarsling. Sirenevarsling. <https://www.brs.dk/da/borger/var-klar-nar-krisen-rammer/det-skal-du-gore-nar-du-horer-sirenerne/> ([archived](https://web.archive.org/web/20260617225444/https://www.brs.dk/da/borger/var-klar-nar-krisen-rammer/det-skal-du-gore-nar-du-horer-sirenerne/))
[^s49]: Retsinformation / Klima-, Energi- og Forsyningsministeriet — Bekendtgørelse af lov om Energinet (LBK nr 271 af…, 2023-03-09. Bekendtgørelse af lov om Energinet (LBK nr 271 af 09/03/2023). <https://www.retsinformation.dk/eli/lta/2023/271/xml>
[^s50]: Uddannelses- og Forskningsstyrelsen — STADS. STADS. <https://ufsn.dk/institutioner-og-drift/studieadministrative-systemer/stads/> ([archived](https://web.archive.org/web/20260519213542/https://ufsn.dk/institutioner-og-drift/studieadministrative-systemer/stads/))
[^s51]: Retsinformation / Indenrigs- og Sundhedsministeriet — Bekendtgørelse af sundhedsloven (LBK nr 275 af 12/03/2025), 2025-03-12. Bekendtgørelse af sundhedsloven (LBK nr 275 af 12/03/2025). <https://www.retsinformation.dk/eli/lta/2025/275/xml>
[^s52]: Sundhedsdatastyrelsen — Fælles Medicinkort. Fælles Medicinkort. <https://sundhedsdatastyrelsen.dk/digitale-loesninger/faelles-medicinkort> ([archived](https://web.archive.org/web/20260616035826/https://sundhedsdatastyrelsen.dk/digitale-loesninger/faelles-medicinkort))
[^s53]: Retsinformation / Styrelsen for Dataforsyning og Effektivisering — Adresseloven (LOV nr 136 af 01/02/2017), 2017-02-01. Adresseloven (LOV nr 136 af 01/02/2017). <https://www.retsinformation.dk/eli/lta/2017/136/xml>

**Evidence grades:** 5 Strong, 55 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
