# Portugal: critical data holdings and sovereign hosting

> Generated 2026-09-29 by `model/generate_countries.py` from the content model (`model/document.py`). The same document is typeset as the country PDF and rendered on the web. Every fact carries a footnote to a source whose text was fetched and checked; a value in *italics* is withheld because no checked source supports it yet.

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
| Government data centres | Yes[^s6][^s7][^s8] |
| Government cloud in operation | Partly[^s9][^s6][^s2] |

What could move this placement:

- If state-controlled trust anchor is found to be no: Dependent on non-EU providers.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Portugal described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 11.39 million[^s10] |
| GDP, current prices | 306.7 EUR bn[^s11] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 132.9 EUR/MWh[^s12] |
| Renewables share of electricity | 65.8 %[^s13] |
| Land area | 90 996 km²[^s14] |

## 3. Critical data holdings, by priority

The holdings Portugal cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 1 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Facial biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | Authentication records (type, date/time) and signatures are processed to manage electronic identification[^s4] | *Not yet sourced* | *Not stated in sources* | 140,783,983 total authentications through Autenticação.gov (figure shown at time of research, 2026-09-29)[^s15] |
| High | Document issuance history (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
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
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 1 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 1 |

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

> Not yet sized. Capacity for Portugal will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Portugal without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Civil registry core (tier 0)
- Facial biometric (tier 0)
- Fingerprint biometric (tier 0)
- Breeder document scans (tier 0)
- Document issuance history (tier 0)
- Digital identity credentials (tier 0)
- Electoral roll entry (tier 0)
- State PKI and qualified trust services (tier 0)
- Residence and migration status (tier 1)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Beneficial ownership register (tier 1)
- Vehicle & licensing (tier 1)
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

[^s1]: Agência para a Reforma Tecnológica do Estado, I.P. (ARTE) — Estratégia Digital Nacional – Plano de Ação 2026-2027…, 2025-12-29. Estratégia Digital Nacional – Plano de Ação 2026-2027 (projeto 8.2). <https://www.arte.gov.pt/wp-content/uploads/2026/05/Plano-de-Acao-2026-2027_EDN.pdf>
[^s2]: Presidência do Conselho de Ministros (Diário da República, 1.ª série, N.º 102) — Resolução do Conselho de Ministros n.º 102/2026 – Aprova…, 2026-05-27. Resolução do Conselho de Ministros n.º 102/2026 – Aprova o Plano Nacional de Nuvem Soberana. <https://bo.digital.gov.pt/api/assets/etic/2fecc6f4-b424-41c6-b2a8-722b17b1914f/> ([archived](https://web.archive.org/web/20260702232015/https://bo.digital.gov.pt/api/assets/etic/2fecc6f4-b424-41c6-b2a8-722b17b1914f/))
[^s3]: Assembleia da República (copy hosted by SIRP) — Lei Orgânica n.º 2/2014, de 6 de agosto – Regime do…, 2014-08-06. Lei Orgânica n.º 2/2014, de 6 de agosto – Regime do Segredo de Estado (Diário da República, 1.ª série, N.º 150). <https://sirp.pt/wp-content/uploads/2025/09/LEI_DO_SEGREDO_DE_ESTADO.pdf> ([archived](https://web.archive.org/web/20251108103511/https://sirp.pt/wp-content/uploads/2025/09/LEI_DO_SEGREDO_DE_ESTADO.pdf))
[^s4]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — Termos e Condições – Autenticação.gov. Termos e Condições – Autenticação.gov. <https://www.autenticacao.gov.pt/web/guest/termos-e-condicoes> ([archived](https://web.archive.org/web/20260830101400/https://www.autenticacao.gov.pt/web/guest/termos-e-condicoes))
[^s5]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — A Chave Móvel Digital. A Chave Móvel Digital. <https://www.autenticacao.gov.pt/web/guest/a-chave-movel-digital> ([archived](https://web.archive.org/web/20260914162323/https://www.autenticacao.gov.pt/web/guest/a-chave-movel-digital))
[^s6]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — Plano Nacional de Nuvem Soberana (Maio 2026), 2026-05. Plano Nacional de Nuvem Soberana (Maio 2026). <https://www.arte.gov.pt/wp-content/uploads/2026/05/Plano-Nacional-de-Nuvem-Soberana.pdf>
[^s7]: IP Telecom – Serviços de Telecomunicações, S.A. — Sobre Nós. Sobre Nós. <https://www.iptelecom.pt/pt-pt/empresa/sobre-nos> ([archived](https://web.archive.org/web/20260626202759/https://www.iptelecom.pt/pt-pt/empresa/sobre-nos))
[^s8]: IP Telecom – Serviços de Telecomunicações, S.A. — IPT Cloud & Datacenter. IPT Cloud & Datacenter. <https://www.iptelecom.pt/pt-pt/servicos/ipt-cloud-datacenter> ([archived](https://web.archive.org/web/20260626202758/https://www.iptelecom.pt/pt-pt/servicos/ipt-cloud-datacenter))
[^s9]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — ARTE coordena elaboração do Plano Nacional de Nuvem Soberana, 2026-05-29. ARTE coordena elaboração do Plano Nacional de Nuvem Soberana. <https://www.arte.gov.pt/arte-coordena-elaboracao-do-plano-nacional-de-nuvem-soberana/>
[^s10]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s11]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s12]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s13]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s14]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s15]: ARTE – Agência para a Reforma Tecnológica do Estado, I.P. — Estatísticas – Autenticação.gov. Estatísticas – Autenticação.gov. <https://www.autenticacao.gov.pt/web/guest/estatisticas>
