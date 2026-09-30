# France: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, France could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | Yes[^s3][^s4] |
| State-controlled trust anchor | Yes[^s5][^s6] |
| State-controlled national eID | Yes[^s7][^s8] |
| Government data centres | Yes[^s9] |
| Government cloud in operation | Yes[^s9] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

France described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 68.88 million[^s10] |
| GDP, current prices | 2 991.1 EUR bn[^s11] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 153.4 EUR/MWh[^s12] |
| Renewables share of electricity | 31.3 %[^s13] |
| Land area | 633 886 km²[^s14] |

## 3. Critical data holdings, by priority

The holdings France cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 5 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | RNIPP, the register used to verify the civil status of people born in France[^s15] | Insee has managed the RNIPP since its creation[^s16] | *Not stated in sources* | Civil status of 113 million people born in or having lived in France[^s16] |
| Critical | Facial biometric (tier 0) | TES centralises the digitised facial image and fingerprints of every ID-card and passport applicant[^s17] | Ministry of the Interior is the controller of TES[^s17] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | TES holds fingerprints for issuing national ID cards and passports[^s17] | Ministry of the Interior[^s17] | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | SCEC draws up the civil-status acts of persons who acquire French nationality[^s18] | SCEC is a national-competence service of the Ministry of Foreign Affairs[^s18] | *Not stated in sources* | About 16 million civil-status acts[^s18] |
| Critical | Authentication audit log (tier 0) | FranceConnect keeps traceability records of access to the teleservice[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | TES records document number, type, and date and place of issue for each ID card and passport[^s17] | Ministry of the Interior[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | The Justice ministry root CA is to be signed by IGC/A, the administration's trust infrastructure[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | ASTREA is the information system of the national criminal record[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | TAJ is a Ministry of the Interior file shared by police and gendarmerie[^s22] | FAED is run by the Direction centrale de la police judiciaire[^s23] | *Not stated in sources* | 17 million 'persons implicated' records (2022), plus 48 million victim records[^s22] |
| High | Intelligence services (tier 1) | DRSD SIRCID information system contracted to Airbus Defence & Space[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Residence and migration status (tier 1) | AGDREF manages the right of residence of foreign nationals[^s25] | DGEF of the Ministry of the Interior is responsible[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | Customs declarations are lodged in the DELTA online service[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | RGCU is the single career register of the whole population, built by CNAV[^s27] | CNAV also runs the SNGI identifier system for the whole social-security sphere[^s27] | *Not stated in sources* | 15.3 million pensioners paid by the general scheme[^s27] |
| High | Statutory health insurance (tier 1) | CNAV runs the healthcare entitlement calculation tool (ODSS) on behalf of Cnam[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Single register covering all businesses in France[^s28] | RNE is operated by INPI[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Register of beneficial owners; discrepancies are reported to the court registry (greffe)[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | SIV, in place since April 2009, replaced the FNI[^s30] | Managed by France Titres (ANTS)[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | SIA, the national firearms information system[^s31] | Ministry of the Interior[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | PAYSAGE consolidates the payroll application for State employees[^s32] | Listed among IT projects carried by budget programmes 156 and 218[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | Artemis: AI applications for massive processing of military data[^s24] | *Not yet sourced* | National infrastructure[^s24] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | NexSIS pools the information systems of fire and rescue services[^s33] | ANSC designs, deploys and maintains NexSIS[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | FR-Alert, the public warning system over mobile telephony[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | DMP and the digital health space are State digital infrastructures[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The JO is made available electronically, permanently and free of charge[^s35] | DILA publishes the JORF[^s35] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | The notifiable-diseases system covers 38 diseases[^s36] | Data go to the ARS and to Santé publique France epidemiologists[^s36] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Secure access services for confidential data[^s37] | CASD is a GIP whose members include the State represented by Insee[^s37] | National infrastructure[^s38] | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | BAN is a State database listing all addresses in France[^s39] | IGN runs operation and distribution of the BAN[^s39] | *Not stated in sources* | 25 million addresses, 250,000 localities (beta)[^s39] |

## 4. Foreign-dependency exposure

Of the 27 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 25 |

## 5. Legal and institutional posture

1 of 8 posture entries have a verified source. The others were researched from public policy documents but are withheld here until each is checked against the governing instrument.

| Dimension | Position |
|---|---|
| Governing instrument | *Not yet sourced* |
| Sovereign or government cloud | *Not yet sourced* |
| Cloud certification | *Not yet sourced* |
| Data classification | IGI 1300: Secret / Tres Secret; 'Diffusion Restreinte' is a protection marking, not a classification level[^s40] |
| Procurement route | *Not yet sourced* |
| National digital identity | *Not yet sourced* |
| Internet exchange | *Not yet sourced* |
| Hyperscaler regions in country | *Not yet sourced* |

## 6. Capacity

> Not yet sized. Capacity for France will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 5 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for France without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Electoral roll entry (tier 0)
- Tax (tier 1)
- Land & property registry (tier 1)
- Border and visa systems (tier 1)
- Treasury and state accounts (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Secrétariat général de la défense et de la sécurité nationale (SGDSN) — Protéger le secret de la défense nationale, 2022-11-23. Protéger le secret de la défense nationale. <https://www.sgdsn.gouv.fr/nos-missions/proteger/proteger-le-secret-de-la-defense-nationale> ([archived](https://web.archive.org/web/20260702145838/https://www.sgdsn.gouv.fr/nos-missions/proteger/proteger-le-secret-de-la-defense-nationale))
[^s2]: Secrétariat général de la défense et de la sécurité nationale (SGDSN) — Réforme de la protection du secret de la défense nationale. Réforme de la protection du secret de la défense nationale. <https://www.sgdsn.gouv.fr/nos-missions/proteger/proteger-le-secret-de-la-defense-nationale/reforme-de-la-protection-du-secret>
[^s3]: Direction interministérielle du numérique (DINUM) — Cloud au centre : la doctrine de l'État. Cloud au centre : la doctrine de l'État. <https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/la-doctrine-cloud-etat/> ([archived](https://web.archive.org/web/20260825221329/https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/la-doctrine-cloud-etat/))
[^s4]: Direction interministérielle du numérique (DINUM) — Vade-mecum sur la sensibilité des données au sens de…, 2026-02-04. Vade-mecum sur la sensibilité des données au sens de l'article 31 de la loi SREN. <https://www.numerique.gouv.fr/documents/244/20260204_Vademecum_donnees_sensibles_.pdf>
[^s5]: Agence nationale de la sécurité des systèmes d'information (ANSSI) — La liste nationale de confiance. La liste nationale de confiance. <https://cyber.gouv.fr/reglementation/reglementation-identite-confiance-numerique/securite-echanges-voie-electronique/reglement-eidas/la-liste-nationale-de-confiance/> ([archived](https://web.archive.org/web/20260509192253/https://cyber.gouv.fr/reglementation/reglementation-identite-confiance-numerique/securite-echanges-voie-electronique/reglement-eidas/la-liste-nationale-de-confiance/))
[^s6]: Agence nationale de la sécurité des systèmes d'information (ANSSI) — Trusted List of France (TL-FR v6, XML). Trusted List of France (TL-FR v6, XML). <https://messervices.cyber.gouv.fr/visas/tl-fr_v6.xml>
[^s7]: France Titres (Agence nationale des titres sécurisés) — France Identité : Le service public officiel de…. France Identité : Le service public officiel de l'identité numérique. <https://france-identite.gouv.fr/presenter-france-identite/>
[^s8]: Direction interministérielle du numérique (DINUM) — Accueil - FranceConnect. Accueil - FranceConnect. <https://www.franceconnect.gouv.fr/> ([archived](https://web.archive.org/web/20260927173544/https://www.franceconnect.gouv.fr/))
[^s9]: Direction interministérielle du numérique (DINUM) — Le Cloud interministériel. Le Cloud interministériel. <https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/le-cloud-interne/> ([archived](https://web.archive.org/web/20260614102447/https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/le-cloud-interne/))
[^s10]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s11]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s12]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s13]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s14]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s15]: CNIL — RNIPP : Répertoire national d’identification des…, 2023-02-09. RNIPP : Répertoire national d’identification des personnes physiques. <https://www.cnil.fr/fr/rnipp-repertoire-national-didentification-des-personnes-physiques> ([archived](https://web.archive.org/web/20260828044632/https://www.cnil.fr/fr/rnipp-repertoire-national-didentification-des-personnes-physiques))
[^s16]: Insee — Le Répertoire national d’identification des personnes…, 2022. Le Répertoire national d’identification des personnes physiques (RNIPP) au cœur de la vie administrative française (Courrier des statistiques N8). <https://www.insee.fr/fr/information/6665188> ([archived](https://web.archive.org/web/20260607172632/https://www.insee.fr/fr/information/6665188))
[^s17]: CNIL — Le fichier des titres électroniques sécurisés (TES), 2020-11-17. Le fichier des titres électroniques sécurisés (TES). <https://www.cnil.fr/fr/le-fichier-des-titres-electroniques-securises-tes> ([archived](https://web.archive.org/web/20260515193658/https://www.cnil.fr/fr/le-fichier-des-titres-electroniques-securises-tes))
[^s18]: Ministère de l’Europe et des Affaires étrangères — Missions du Service central d’état civil. Missions du Service central d’état civil. <https://www.diplomatie.gouv.fr/fr/services-aux-francaises-et-aux-francais/vie-administrative-et-elections/etat-civil/missions-du-service-central-d-etat-civil>
[^s19]: DINUM / FranceConnect — Politique de protection des données personnelles -…, 2023-02-15. Politique de protection des données personnelles - FranceConnect / FranceConnect+. <https://www.franceconnect.gouv.fr/cgu/politique-protection-donnees-personnelles/> ([archived](https://web.archive.org/web/20260907155638/https://www.franceconnect.gouv.fr/cgu/politique-protection-donnees-personnelles/))
[^s20]: Ministère de la Justice — Politique de certification – AC Racine Justice, 2011-09-15. Politique de certification – AC Racine Justice. <https://crl.justice.gouv.fr/igc/ants/MJ-PC-AC-Racine.pdf> ([archived](https://web.archive.org/web/20240920193913/https://crl.justice.gouv.fr/igc/ants/MJ-PC-AC-Racine.pdf))
[^s21]: Sénat — Projet de loi de finances pour 2026 : Justice, 2025. Projet de loi de finances pour 2026 : Justice. <https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html> ([archived](https://web.archive.org/web/20260914153452/https://www.senat.fr/rap/l25-139-317/l25-139-317_mono.html))
[^s22]: CNIL — Traitement d’Antécédents Judiciaires - TAJ : comment…, 2025-11-20. Traitement d’Antécédents Judiciaires - TAJ : comment exercer vos droits ?. <https://www.cnil.fr/fr/taj-traitement-dantecedents-judiciaires> ([archived](https://web.archive.org/web/20251011141131/https://www.cnil.fr/fr/taj-traitement-dantecedents-judiciaires))
[^s23]: CNIL — FAED : Fichier automatisé des empreintes digitales. FAED : Fichier automatisé des empreintes digitales. <https://www.cnil.fr/fr/faed-fichier-automatise-des-empreintes-digitales> ([archived](https://web.archive.org/web/20260310135247/https://www.cnil.fr/fr/faed-fichier-automatise-des-empreintes-digitales))
[^s24]: Sénat / Assemblée nationale (Délégation parlementaire au renseignement) — Délégation parlementaire au renseignement - rapport…, 2020. Délégation parlementaire au renseignement - rapport d'activité 2019-2020. <https://www.senat.fr/rap/r19-506/r19-506_mono.html> ([archived](https://web.archive.org/web/20260312003200/https://www.senat.fr/rap/r19-506/r19-506_mono.html))
[^s25]: CNIL — Application de gestion des dossiers des ressortissants…, 2021-06-09. Application de gestion des dossiers des ressortissants étrangers en France (AGDREF). <https://www.cnil.fr/fr/application-de-gestion-des-dossiers-des-ressortissants-etrangers-en-france-agdref> ([archived](https://web.archive.org/web/20260919225732/https://www.cnil.fr/fr/application-de-gestion-des-dossiers-des-ressortissants-etrangers-en-france-agdref))
[^s26]: Direction générale des douanes et droits indirects — Demande d'accès aux données des déclarations en douane. Demande d'accès aux données des déclarations en douane. <https://www.douane.gouv.fr/professionnels/autres-demarches/demande-dacces-aux-donnees-des-declarations-en-douane> ([archived](https://web.archive.org/web/20260922143713/https://www.douane.gouv.fr/professionnels/autres-demarches/demande-dacces-aux-donnees-des-declarations-en-douane))
[^s27]: L’Assurance retraite (CNAV) — Dossier institutionnel 2025, 2025. Dossier institutionnel 2025. <https://www.lassuranceretraite.fr/portail-info/files/live/sites/pub/files/PDF/dossier-institutionnel-2025.pdf>
[^s28]: INPI — Le Guichet unique des entreprises et le Registre…. Le Guichet unique des entreprises et le Registre national des entreprises. <https://www.inpi.fr/decouvrir-inpi/formalites-dentreprises/guichet-unique-formalites-dentreprises-et-registre-national-entreprises> ([archived](https://web.archive.org/web/20260418192503/https://www.inpi.fr/decouvrir-inpi/formalites-dentreprises/guichet-unique-formalites-dentreprises-et-registre-national-entreprises))
[^s29]: INPI — Bénéficiaires effectifs. Bénéficiaires effectifs. <https://www.inpi.fr/ressources/formalites-dentreprises/beneficiaires-effectifs> ([archived](https://web.archive.org/web/20260902100357/https://www.inpi.fr/ressources/formalites-dentreprises/beneficiaires-effectifs))
[^s30]: CNIL — SIV : Système d’immatriculation des véhicules. SIV : Système d’immatriculation des véhicules. <https://www.cnil.fr/fr/siv-systeme-dimmatriculation-des-vehicules> ([archived](https://web.archive.org/web/20260913062431/https://www.cnil.fr/fr/siv-systeme-dimmatriculation-des-vehicules))
[^s31]: Ministère de l’Intérieur — Accueil, Système d'Information des Armes. Accueil, Système d'Information des Armes. <https://sia.detenteurs.interieur.gouv.fr/>
[^s32]: Sénat — Projet de loi de finances pour 2025 : Gestion des…, 2024. Projet de loi de finances pour 2025 : Gestion des finances publiques - Crédits non répartis - Transformation et fonction publiques. <https://www.senat.fr/rap/l24-144-315-1/l24-144-315-1_mono.html>
[^s33]: Sénat — Projet de loi de finances pour 2025 : Sécurités…, 2024. Projet de loi de finances pour 2025 : Sécurités (Sécurité civile). <https://www.senat.fr/rap/l24-144-329-2/l24-144-329-2_mono.html> ([archived](https://web.archive.org/web/20251207021927/https://www.senat.fr/rap/l24-144-329-2/l24-144-329-2_mono.html))
[^s34]: Sénat — Projet de loi de finances pour 2025 : Santé, 2024. Projet de loi de finances pour 2025 : Santé. <https://www.senat.fr/rap/l24-144-328/l24-144-328_mono.html> ([archived](https://web.archive.org/web/20250902143337/https://www.senat.fr/rap/l24-144-328/l24-144-328_mono.html))
[^s35]: DILA — Diffusion légale, 2026-06-26. Diffusion légale. <https://www.dila.premier-ministre.gouv.fr/institution/missions/article/diffusion-legale> ([archived](https://web.archive.org/web/20251102205650/https://www.dila.premier-ministre.gouv.fr/institution/missions/article/diffusion-legale))
[^s36]: Santé publique France — Maladies à signalement obligatoire, 2026-04-22. Maladies à signalement obligatoire. <https://www.santepubliquefrance.fr/maladies-a-declaration-obligatoire> ([archived](https://web.archive.org/web/20260305175756/https://www.santepubliquefrance.fr/maladies-a-declaration-obligatoire))
[^s37]: CASD — Gouvernance et Missions. Gouvernance et Missions. <https://www.casd.eu/le-casd/gouvernance-et-missions/>
[^s38]: CASD — Infrastructure. Infrastructure. <https://www.casd.eu/technologie/infrastructure/> ([archived](https://web.archive.org/web/20260310125751/https://www.casd.eu/technologie/infrastructure/))
[^s39]: adresse.data.gouv.fr (DINUM / IGN) — Découvrir la Base Adresse Nationale. Découvrir la Base Adresse Nationale. <https://adresse.data.gouv.fr/decouvrir-la-BAN> ([archived](https://web.archive.org/web/20260921135714/https://adresse.data.gouv.fr/decouvrir-la-BAN))
[^s40]: Secretariat general de la defense et de la securite nationale (SGDSN) igi-secret-defense, 2021-12-01. Instruction ministérielle sur la protection du secret de la défense nationale. <https://www.info.gouv.fr/upload/media/content/0001/05/1dbd413d9574bba8df1f282cab4a74f128432209.pdf>
