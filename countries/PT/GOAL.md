# Portugal: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Portugal could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2][^s3] |
| Classification in law | Yes[^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | *Not yet sourced* |
| State-controlled national eID | Yes[^s4][^s5] |
| Government data centres | Yes[^s6][^s7][^s8][^s9] |
| Government cloud in operation | Partly[^s10][^s6][^s2] |

What could move this placement:

- If state-controlled trust anchor is found to be no: Dependent on non-EU providers.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Portugal described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 11.42 million[^s11] |
| GDP, current prices | 308.5 EUR bn[^s12] |
| Public administration employment (NACE O) | 314.8 thousand[^s13] |
| Non-household electricity price | 132.9 EUR/MWh[^s14] |
| Renewables share of electricity | 65.6 %[^s15] |
| Land area | 90 977 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Portugal cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 4 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Civil registry database (base de dados do registo civil) holding nationality, civil status and legal capacity of citizens[^s17] | The President of IRN, I.P. is the data controller of the civil registry database[^s17] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Facial image files collected for the Citizen Card are communicated only to the civil identification database[^s18] | IRN, I.P. is the controller for Citizen Card data processing operations[^s18] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Citizen Card applications must include facial image and fingerprints[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | ID card applications and foreign-issued certificates are microfilmed or kept in secure digital storage, then the paper originals destroyed[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | Authentication records (type, date/time) and signatures are processed to manage electronic identification[^s4] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Document issuance history (tier 0) | Citizen Card data processing covers issuance, update, renewal and cancellation requests[^s18] | IRN, I.P. is the body responsible for SIPEP[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 7/2007, de 5 de Fevereiro – Cartão de Cidadão…, 2007 gives the value this report printed; ARTE - Agência para a Reforma Tecnológica do Estado (Autenticação.gov) — Chave Móvel Digital gives “Chave Móvel Digital (CMD) (Digital Mobile Key)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | Law text assigns management and security of the CMD technological infrastructure to AMA, I.P. (the predecessor of ARTE)[^s21] | *Not stated in sources* | *Not yet sourced* |
| High | Electoral roll entry (tier 0) | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 13/99, de 22 de Março – Regime Jurídico do…, 1999 gives the value this report printed; Secretaria-Geral do Ministério da Administração Interna (SGMAI) — Administração Eleitoral gives “Base de Dados do Recenseamento Eleitoral (Voter Registration Database)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | SGMAI electoral administration organises, maintains and manages BDRE and SIGRE[^s22] | *Not stated in sources* | 11 130 316 inscritos para votar (registered voters)[^s23] |
| High | State PKI and qualified trust services (tier 0) | The State Electronic Certification Entity is the state's root certification authority at the top of the SCEE chain[^s24] | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 12/2021, de 9 de fevereiro (art. 27.º), 2021 gives the value this report printed; Agência para a Reforma Tecnológica do Estado, I.P. (ARTE) — Certificação eletrónica gives “ARTE (Agência para a Reforma Tecnológica do Estado; Agency for the Technological Reform of the State)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Land registry databases hold the legal status of real property[^s25] | The President of IRN, I.P. is the controller of the land registry databases[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Electronic court case processing takes place in the courts' support information system[^s26] | DGAJ is the entity responsible for the criminal identification databases[^s27][^s28] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | centros de dados do Serviço de Informações de Segurança e do Serviço de Informações Estratégicas de Defesa (data centres of the SIS and the SIED)[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Residence and migration status (tier 1) | SII AIMA: personal-data information system holding non-police information on foreign nationals[^s30] | Administrative migration and asylum functions were transferred to the new AIMA, I.P.[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | STADA-IMP (customs import declaration processing system)[^s32] | AT (Autoridade Tributária e Aduaneira; Tax and Customs Authority)[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | All natural and legal persons dealing with social security are identified in the information system[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | The National Patient Register (RNU) is used as the patient identification reference by other national health systems[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | The commercial registry database holds the legal status of registered entities[^s35] | The Director-General of Registries and Notary (now IRN) is the database controller[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Registo Central de Beneficiário Efetivo (RCBE) (Central Register of Beneficial Ownership)[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | The vehicle registry database holds the legal status of motor vehicles[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | SII UCFE: shared police information system on borders and foreign nationals, used by security forces[^s30] | Management of former SEF systems, including the national part of SIS, passes to a security information technology unit[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | Budget data are registered in SIGO (DGO) and entered in information systems managed by ESPAP, I.P.[^s39] | Direção-Geral do Orçamento (DGO); Entidade de Serviços Partilhados da Administração Pública, I.P. (ESPAP)[^s40] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Disputed: sources disagree. Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 53/2008, de 29 de Agosto – Lei de Segurança Interna, 2008 gives the value this report printed; SIRESP, S.A. — Home - SIRESP gives “Rede Nacional de Emergência e Segurança – SIRESP (National Emergency and Security Network)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | SIRESP, S.A.[^s41] | *Not stated in sources* | mais de 40.000 utilizadores (more than 40,000 users)[^s41] |
| High | Crisis management and civil protection (tier 1) | ANEPC organises a national alert and warning system[^s42] | ANEPC plans, coordinates and executes emergency and civil protection policy, including civil emergency planning for crisis or war[^s42] | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | centro de Despacho (National Dispatch centre) of REN - Rede Elétrica Nacional[^s43] | REN - Rede Elétrica Nacional[^s43] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | The national water authority establishes and maintains the national water resources information system[^s44][^s45] | APA, I.P. is the national water authority exercising the powers of the Water Law[^s45] | *Not stated in sources* | *Not yet measured* |
| High | Education (tier 1) | Qualification diplomas and certificates under the National Qualifications System are made available in SIGO[^s46] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | National reference geographic database products include topographic mapping and orthophoto mapping[^s47] | DGT gathers territorial geographic information in the National Territorial Information System (SNIT)[^s47] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 27 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 27 |

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

> Not yet sized. Capacity for Portugal will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 4 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Portugal without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Tax (tier 1)
- Police information systems (tier 1)
- Firearms register (tier 1)
- Official gazette and legislation (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)

---

[^s1]: Agência para a Reforma Tecnológica do Estado, I.P. (ARTE) — Estratégia Digital Nacional – Plano de Ação 2026-2027…, 2025-12-29. Estratégia Digital Nacional – Plano de Ação 2026-2027 (projeto 8.2). <https://www.arte.gov.pt/wp-content/uploads/2026/05/Plano-de-Acao-2026-2027_EDN.pdf>
[^s2]: Presidência do Conselho de Ministros (Diário da República, 1.ª série, N.º 102) — Resolução do Conselho de Ministros n.º 102/2026 – Aprova…, 2026-05-27. Resolução do Conselho de Ministros n.º 102/2026 – Aprova o Plano Nacional de Nuvem Soberana. <https://bo.digital.gov.pt/api/assets/etic/2fecc6f4-b424-41c6-b2a8-722b17b1914f/> ([archived](https://web.archive.org/web/20260702232015/https://bo.digital.gov.pt/api/assets/etic/2fecc6f4-b424-41c6-b2a8-722b17b1914f/))
[^s3]: Assembleia da República (copy hosted by SIRP) — Lei Orgânica n.º 2/2014, de 6 de agosto – Regime do…, 2014-08-06. Lei Orgânica n.º 2/2014, de 6 de agosto – Regime do Segredo de Estado (Diário da República, 1.ª série, N.º 150). <https://sirp.pt/wp-content/uploads/2025/09/LEI_DO_SEGREDO_DE_ESTADO.pdf> ([archived](https://web.archive.org/web/20251108103511/https://sirp.pt/wp-content/uploads/2025/09/LEI_DO_SEGREDO_DE_ESTADO.pdf))
[^s4]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — Termos e Condições – Autenticação.gov. Termos e Condições – Autenticação.gov. <https://www.autenticacao.gov.pt/web/guest/termos-e-condicoes> ([archived](https://web.archive.org/web/20260830101400/https://www.autenticacao.gov.pt/web/guest/termos-e-condicoes))
[^s5]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — A Chave Móvel Digital. A Chave Móvel Digital. <https://www.autenticacao.gov.pt/web/guest/a-chave-movel-digital> ([archived](https://web.archive.org/web/20260914162323/https://www.autenticacao.gov.pt/web/guest/a-chave-movel-digital))
[^s6]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — Plano Nacional de Nuvem Soberana (Maio 2026), 2026-05. Plano Nacional de Nuvem Soberana (Maio 2026). <https://www.arte.gov.pt/wp-content/uploads/2026/05/Plano-Nacional-de-Nuvem-Soberana.pdf>
[^s7]: IP Telecom – Serviços de Telecomunicações, S.A. — Sobre Nós. Sobre Nós. <https://www.iptelecom.pt/pt-pt/empresa/sobre-nos> ([archived](https://web.archive.org/web/20260626202759/https://www.iptelecom.pt/pt-pt/empresa/sobre-nos))
[^s8]: IP Telecom – Serviços de Telecomunicações, S.A. — IPT Cloud & Datacenter. IPT Cloud & Datacenter. <https://www.iptelecom.pt/pt-pt/servicos/ipt-cloud-datacenter> ([archived](https://web.archive.org/web/20260626202758/https://www.iptelecom.pt/pt-pt/servicos/ipt-cloud-datacenter))
[^s9]: Sistema de Informações da República Portuguesa (SIRP) — Organização do SIRP, 2026. Organização do SIRP. <https://sirp.pt/organizacao-do-sirp/> ([archived](https://web.archive.org/web/20260608091525/https://sirp.pt/organizacao-do-sirp/))
[^s10]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — ARTE coordena elaboração do Plano Nacional de Nuvem Soberana, 2026-05-29. ARTE coordena elaboração do Plano Nacional de Nuvem Soberana. <https://www.arte.gov.pt/arte-coordena-elaboracao-do-plano-nacional-de-nuvem-soberana/>
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Código do Registo Civil (DL n.º 131/95), art. 220.º-A, 1995. Código do Registo Civil (DL n.º 131/95), art. 220.º-A. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=682A0220A&nid=682&tabela=leis&pagina=1&ficha=1&nversao=>
[^s18]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 7/2007, de 5 de Fevereiro – Cartão de Cidadão…, 2007. Lei n.º 7/2007, de 5 de Fevereiro – Cartão de Cidadão (art. 37.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2807&tabela=leis>
[^s19]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 33/99, de 18 de Maio – Identificação civil (art.…, 1999. Lei n.º 33/99, de 18 de Maio – Identificação civil (art. 21.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=334&tabela=leis> ([archived](https://web.archive.org/web/20240707043247/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=334&tabela=leis))
[^s20]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 86/2000, de 12 de Maio – SIPEP (art. 2.º), 2000. Decreto-Lei n.º 86/2000, de 12 de Maio – SIPEP (art. 2.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2056&tabela=leis>
[^s21]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 32/2017, de 1 de Junho – alteração à Lei n.º…, 2017. Lei n.º 32/2017, de 1 de Junho – alteração à Lei n.º 37/2014 (Chave Móvel Digital), art. 2.º republicado. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2809&tabela=leis>
[^s22]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 13/99, de 22 de Março – Regime Jurídico do…, 1999. Lei n.º 13/99, de 22 de Março – Regime Jurídico do Recenseamento Eleitoral (art. 10.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2545&tabela=leis>
[^s23]: Secretaria-Geral do Ministério da Administração Interna (SGMAI) — Portal da SGMAI – Números Administração Eleitoral, 2026-08. Portal da SGMAI – Números Administração Eleitoral. <https://www.sg.mai.gov.pt/> ([archived](https://web.archive.org/web/20141227112353/http://www.sg.mai.gov.pt:80/?))
[^s24]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 12/2021, de 9 de fevereiro (art. 27.º), 2021. Decreto-Lei n.º 12/2021, de 9 de fevereiro (art. 27.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3404&tabela=leis>
[^s25]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Código do Registo Predial (DL n.º 224/84), art. 106.º, 1984. Código do Registo Predial (DL n.º 224/84), art. 106.º. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=488A0106&nid=488&tabela=leis&pagina=1&ficha=1&nversao=>
[^s26]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Portaria n.º 350-A/2025/1, de 9 de outubro – tramitação…, 2025. Portaria n.º 350-A/2025/1, de 9 de outubro – tramitação eletrónica dos processos (art. 2.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3949&tabela=leis>
[^s27]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 37/2015, de 5 de Maio – Lei da Identificação…, 2015. Lei n.º 37/2015, de 5 de Maio – Lei da Identificação Criminal (art. 38.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2321&tabela=leis>
[^s28]: Direção-Geral da Administração da Justiça (DGAJ) — Certificado do Registo Criminal Online, 2026-09-10. Certificado do Registo Criminal Online. <https://registocriminal.justica.gov.pt/> ([archived](https://web.archive.org/web/20260731123603/https://registocriminal.justica.gov.pt/))
[^s29]: Sistema de Informações da República Portuguesa (SIRP) — Fiscalização, 2026. Fiscalização. <https://sirp.pt/fiscalizacao/> ([archived](https://web.archive.org/web/20260608080258/https://sirp.pt/fiscalizacao/))
[^s30]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 23/2007, de 4 de Julho – Entrada, permanência,…, 2007. Lei n.º 23/2007, de 4 de Julho – Entrada, permanência, saída e afastamento de estrangeiros (art. 3.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=920&tabela=leis> ([archived](https://web.archive.org/web/20260723065246/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=920&tabela=leis))
[^s31]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 41/2023, de 2 de junho – cria a AIMA, I.…, 2023. Decreto-Lei n.º 41/2023, de 2 de junho – cria a AIMA, I. P. (preâmbulo). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3676&tabela=leis>
[^s32]: Autoridade Tributária e Aduaneira (AT) — Relatório de Atividades 2024, 2025. Relatório de Atividades 2024. <https://info.portaldasfinancas.gov.pt/pt/at/Instrumentos_Gestao/Relatorio_atividades/Documents/Relatorio_de_Atividades_AT_2024.pdf> ([archived](https://web.archive.org/web/20260509164626/https://info.portaldasfinancas.gov.pt/pt/at/Instrumentos_Gestao/Relatorio_atividades/Documents/Relatorio_de_Atividades_AT_2024.pdf))
[^s33]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 4/2007, de 16 de Janeiro – Bases gerais do…, 2007. Lei n.º 4/2007, de 16 de Janeiro – Bases gerais do sistema de segurança social (art. 98.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2243&tabela=leis> ([archived](https://web.archive.org/web/20250430135035/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2243&tabela=leis))
[^s34]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Portaria n.º 22/2016, de 10 de fevereiro – Regulamento…, 2016. Portaria n.º 22/2016, de 10 de fevereiro – Regulamento de Notificação Obrigatória de Doenças Transmissíveis (art. 12.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=2506&tabela=leis>
[^s35]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Código do Registo Comercial (DL n.º 403/86), art. 78.º-B, 1986. Código do Registo Comercial (DL n.º 403/86), art. 78.º-B. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=506A0078B&nid=506&tabela=leis&pagina=1&ficha=1&nversao=>
[^s36]: Instituto dos Registos e do Notariado, I.P. (IRN) / Justiça.gov.pt — Registo Central do Beneficiário Efetivo, 2026-09-30. Registo Central do Beneficiário Efetivo. <https://rcbe.justica.gov.pt/> ([archived](https://web.archive.org/web/20260724173200/https://rcbe.justica.gov.pt/))
[^s37]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 54/75, de 12 de Fevereiro – Registo…, 1975. Decreto-Lei n.º 54/75, de 12 de Fevereiro – Registo automóvel (art. 27.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=598&tabela=leis> ([archived](https://web.archive.org/web/20251010024521/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=598&tabela=leis))
[^s38]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 73/2021, de 12 de novembro – reestruturação do…, 2021. Lei n.º 73/2021, de 12 de novembro – reestruturação do sistema português de controlo de fronteiras. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3468&tabela=leis> ([archived](https://web.archive.org/web/20240601081051/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3468&tabela=leis))
[^s39]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 13-A/2025, de 10 de março – normas de…, 2025. Decreto-Lei n.º 13-A/2025, de 10 de março – normas de execução do Orçamento do Estado para 2025. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3890&tabela=leis>
[^s40]: IGCP, E.P.E. — Página Inicial | IGCP. Página Inicial | IGCP. <https://www.igcp.pt/>
[^s41]: SIRESP, S.A. — Home - SIRESP. Home - SIRESP. <https://www.siresp.pt/> ([archived](https://web.archive.org/web/20260608175758/https://www.siresp.pt/))
[^s42]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 45/2019, de 1 de abril – orgânica da…, 2019. Decreto-Lei n.º 45/2019, de 1 de abril – orgânica da ANEPC (art. 3.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3049&tabela=leis>
[^s43]: REN - Redes Energéticas Nacionais — Eletricidade. Eletricidade. <https://www.ren.pt/pt-pt/atividade/eletricidade>
[^s44]: Agência Portuguesa do Ambiente (APA) — Sistema Nacional de Informação de Recursos Hídricos - SNIRH, 2026-06-05. Sistema Nacional de Informação de Recursos Hídricos - SNIRH. <https://apambiente.pt/agua/sistema-nacional-de-informacao-de-recursos-hidricos-snirh> ([archived](https://web.archive.org/web/20260617184912/https://apambiente.pt/agua/sistema-nacional-de-informacao-de-recursos-hidricos-snirh))
[^s45]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 58/2005, de 29 de Dezembro – Lei da Água (art. 7.º), 2005. Lei n.º 58/2005, de 29 de Dezembro – Lei da Água (art. 7.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1191&tabela=leis> ([archived](https://web.archive.org/web/20250712012849/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1191&tabela=leis))
[^s46]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Decreto-Lei n.º 396/2007, de 31 de Dezembro – Sistema…, 2007. Decreto-Lei n.º 396/2007, de 31 de Dezembro – Sistema Nacional de Qualificações (art. 7.º). <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1081&tabela=leis> ([archived](https://web.archive.org/web/20221206135358/https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1081&tabela=leis))
[^s47]: Procuradoria-Geral Regional de Lisboa (consolidated legislation database) — Lei n.º 99/2019, de 5 de setembro – revisão do PNPOT, 2019. Lei n.º 99/2019, de 5 de setembro – revisão do PNPOT. <https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=3139&tabela=leis>

**Evidence grades:** 3 Strong, 51 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
