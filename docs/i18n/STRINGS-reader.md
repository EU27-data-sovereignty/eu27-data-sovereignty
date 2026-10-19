# The reader's strings

The mobile reader's own wording, and the content model's table labels and gap markers, which the reader shows in
the reader's language once that language is admitted (#117). Facts, quotes, glosses, explanations and sources are
never translated here; a printed fact stays in its original-language quote with its machine gloss (#82).

A draft (`drafts/<ISO>.md`) covers this file in its "Reader strings" and "Reader review" sections, every key below,
in this order, one column per official language of that state, exactly as it covers `STRINGS.md` in "Strings" and
"Review". Placeholders in braces (`{name}`) are kept as they are, untranslated; the reader fills them in.

The reader also uses these keys of `STRINGS.md`: `country.sources`, `fact.check_this`, `fact.gloss`, every
`section.*` title, and `notice.disclaimer`.

## App strings

Written by hand. The `en` column is the text the reader prints; `mobile/__tests__/i18n.test.tsx` fails on a key the
app uses that is not here.

| key | en | where it prints |
|---|---|---|
| app.tab.countries | Countries | tab |
| app.tab.hosting | Hosting | tab |
| app.tab.ranking | Ranking | tab |
| app.tab.method | Method | tab |
| app.tab.edition | Edition | tab |
| app.title.country | Country report | screen title |
| app.title.factcheck | Fact check | screen title |
| app.loading | Loading the edition… | before a part of the edition is read |
| app.load_error | This part of the edition could not be read: {error} | a part failed its read |
| app.error.title | Something went wrong | render error |
| app.error.hint | Please try again. | render error |
| app.error.retry | Try again | render error, button |
| app.section_no | SECTION {n} | above each section title |
| app.provenance.generated | Generated {date}. | provenance notice, every screen |
| app.provenance.how_built | How this was built | provenance notice, link |
| app.provenance.how_checked | How every fact was checked | provenance notice, link |
| app.countries.kicker | EU-27 · Member states | Countries tab |
| app.countries.intro | Each member state analysed on its own fundamentals. The rows count verified evidence; they are not a ranking of how sovereign a state is. | Countries tab |
| app.countries.find | Find a country | Countries tab, search field |
| app.countries.all | 27 member states | Countries tab |
| app.countries.some | {n} of 27 member states | Countries tab, filtered |
| app.countries.none | No member state matches that name. | Countries tab, no match |
| app.countries.row | {name}, country report | Countries tab, screen-reader label |
| app.countries.counts | Holdings verified {hv} of {ht} · Tier 0 {tv} of {tt} · Sourced facts {facts} | Countries tab, each row |
| app.countries.withheld | {n} withheld as disputed | Countries tab, each row |
| app.countries.none_withheld | Nothing withheld as disputed | Countries tab, each row |
| app.hosting.kicker | EU-27 · Key infrastructure | Hosting tab |
| app.hosting.counts | {facts} hosting facts printed · {withheld} withheld as disputed · {states} of 27 states with any sourced hosting | Hosting tab |
| app.method.kicker | EU-27 · How we know | Method tab |
| app.method.title | Methodology | Method tab |
| app.method.factcheck | How every printed fact was checked by the model that did not write it: | Method tab, before the link |
| app.method.factcheck_link | the fact-check appendix | Method tab, link |
| app.ranking.kicker | EU-27 · Ranking by published rule | Ranking tab |
| app.ranking.title | Data-sovereignty ranking | Ranking tab |
| app.ranking.intro | States are placed in groups by a published rule, not scored. An input without a checked source counts as not demonstrated. The bar beside each state shows the groups it could still reach once its open evidence is settled; that range is its confidence. | Ranking tab |
| app.ranking.chip | {name}, {confidence} confidence, open its report | Ranking tab, screen-reader label |
| app.ranking.none | None | Ranking tab, an empty group |
| app.ranking.indicators | The indicators | Ranking tab, heading |
| app.ranking.findings | Each state’s findings per indicator are in the Placement section of its report. | Ranking tab, legend |
| app.ranking.gap | a gap, never a no. | Ranking tab, legend, after the gap marker |
| app.ranking.disputed_word | Disputed | Ranking tab, legend |
| app.ranking.disputed | withheld until corrected and checked again. | Ranking tab, legend |
| app.country.kicker | EU-27 · Country report · {iso} | country screen |
| app.country.summary | {verified} of {total} critical holding classes verified · {facts} sourced facts shown · {gaps} values withheld until sourced · capacity not yet sized | country screen |
| app.country.contribute | Know a public source for one of the {gaps} withheld values, or a better one for a fact? | country screen |
| app.country.submit | Submit a source | country screen, link |
| app.country.check_hint | Every fact also has a “Check this fact” link in its source entry. | country screen |
| app.country.factcheck | Fact check for {name} | country screen, link |
| app.factcheck.kicker | EU-27 · Cross-model check | fact-check screen |
| app.factcheck.by_state | By member state | fact-check screen, heading |
| app.factcheck.country_kicker | EU-27 · Cross-model check · {iso} | a state's fact-check screen |
| app.factcheck.country_title | Fact check: {name} | a state's fact-check screen |
| app.factcheck.back | Back to {name} | a state's fact-check screen, link |
| app.factcheck.all | All member states | a state's fact-check screen, link |
| app.sources.intro | Each source is listed once. The hash identifies the exact document that was fetched; the quote under each claim is text found in it by machine, in its original language, then a machine translation where the source is not in English, then the checks the claim passed. | source list |
| app.sources.grades | Evidence grades. | source list, before the grade rule |
| app.sources.open | Open source | source list, link |
| app.sources.archived | Archived copy | source list, link |
| app.sources.value_at | Value {value} at {locator} | source list, a value without a quote |
| app.sources.retrieved | retrieved {date} | source list |
| app.sources.mark | Source {n}: {label}. Evidence: {grade} | a fact's source mark, screen-reader label |
| app.about.kicker | EU-27 · This edition | Edition tab |
| app.about.title | About this edition | Edition tab |
| app.about.edition | Edition (sha256 of the bundle) | Edition tab, row |
| app.about.generated | Generated | Edition tab, row |
| app.about.schema | Schema | Edition tab, row |
| app.about.source | Source | Edition tab, row |
| app.about.source_bundled | Inside the app, as installed | Edition tab, row value |
| app.about.source_downloaded | Downloaded from the edition channel | Edition tab, row value |
| app.about.published | published {date} | Edition tab, row value |
| app.about.commit | commit {commit} | Edition tab, row value |
| app.about.facts | Facts shown | Edition tab, row |
| app.about.facts_value | {n} across 27 member states | Edition tab, row value |
| app.about.withheld | Withheld as disputed | Edition tab, row |
| app.about.app | App | Edition tab, row |
| app.about.build | App build | Edition tab, row |
| app.about.build_update | Update {id} on runtime {runtime} | Edition tab, row value |
| app.about.build_installed | The code inside the app as installed | Edition tab, row value |
| app.about.build_runtime | runtime {runtime} | Edition tab, row value |
| app.about.evidence | What this edition can say about its evidence | Edition tab, heading |
| app.about.newer | Newer editions | Edition tab, heading |
| app.about.check | Check for a newer edition | Edition tab, button |
| app.about.use_now | Use it now | Edition tab, button |
| app.about.restart | Restart to apply | Edition tab, button |
| app.about.auto | Check automatically at launch | Edition tab, switch |
| app.about.privacy_note | A check sends one request for a 200-byte pointer to the project’s edition channel, and up to 29 more for the files of a newer edition; then one request to Expo’s update service for a newer build of this app. Each host sees the network address, the app’s user agent and the time, in its request logs. Nothing identifies the reader; nothing about the reader is stored; no request is made unless you tap, or switch the automatic check on. Every downloaded edition file is checked against its published hash before a single value from it is shown. | Edition tab |
| app.about.privacy | Privacy policy | Edition tab, link |
| app.update.idle | Not checked since launch. | Edition tab, edition check |
| app.update.unconfigured | This build has no edition channel configured; it reads only the edition inside the app. | Edition tab, edition check |
| app.update.checking | Checking… | Edition tab, edition check |
| app.update.up_to_date | This is the latest published edition. | Edition tab, edition check |
| app.update.downloading | Downloading {name} ({done} of {total})… | Edition tab, edition check |
| app.update.ready | A newer edition ({edition}…) is downloaded and verified. | Edition tab, edition check |
| app.update.rejected | Rejected: {reason}. Nothing of it was kept. | Edition tab, edition check |
| app.update.unreachable | The edition channel could not be reached. The app keeps the edition it has. | Edition tab, edition check |
| app.appupdate.disabled | Over-the-air app updates are not enabled in this build. | Edition tab, app check |
| app.appupdate.idle | App build not checked since launch. | Edition tab, app check |
| app.appupdate.checking | Checking for a newer app build… | Edition tab, app check |
| app.appupdate.up_to_date | This is the latest app build for this version. | Edition tab, app check |
| app.appupdate.downloading | Downloading a newer app build… | Edition tab, app check |
| app.appupdate.ready | A newer app build is downloaded. Restart to use it. | Edition tab, app check |
| app.appupdate.unreachable | The update service could not be reached. The app keeps the build it has. | Edition tab, app check |
| app.language.heading | Language | Edition tab, heading |
| app.language.scope | Headings, table labels and the app’s own text are translated; explanations, facts and sources stay in English, each fact with its original-language quote. | Edition tab, language section |
| app.language.pending | Other languages appear here once a native speaker has read the translation. | Edition tab, language section |
| app.language.provenance | Translated by {drafted}, reviewed by {reviewed}, read by {read}. | Edition tab, language section |
| app.language.read_in | Read in {language} | country screen, button |

## Content labels and gaps

Generated by `python3 model/i18n.py strings` from the bundle (`web/public/data/eu27.json`): every distinct label and
gap span the content model prints. The reader matches a span to its key by its exact English text, so a label
whose wording changes falls back to English until it is drafted again. Never edit this table by hand.

<!-- generated:start -->
| key | en | where it prints |
|---|---|---|
| gap.not_stated_in_sources | Not stated in sources | a gap marker in the content model |
| gap.not_yet_measured | Not yet measured | a gap marker in the content model |
| gap.not_yet_sourced | Not yet sourced | a gap marker in the content model |
| gap.not_yet_verified | Not yet verified | a gap marker in the content model |
| label.austria | Austria | a table label in the content model |
| label.authentication_audit_log_tier_0 | Authentication audit log (tier 0) | a table label in the content model |
| label.belgium | Belgium | a table label in the content model |
| label.beneficial_ownership_register_tier_1 | Beneficial ownership register (tier 1) | a table label in the content model |
| label.benefits_pensions_tier_1 | Benefits & pensions (tier 1) | a table label in the content model |
| label.border_and_visa_systems_tier_1 | Border and visa systems (tier 1) | a table label in the content model |
| label.breeder_document_scans_tier_0 | Breeder document scans (tier 0) | a table label in the content model |
| label.bulgaria | Bulgaria | a table label in the content model |
| label.business_registry_tier_1 | Business registry (tier 1) | a table label in the content model |
| label.central_bank_systems_tier_1 | Central bank systems (tier 1) | a table label in the content model |
| label.civil_registry_core_tier_0 | Civil registry core (tier 0) | a table label in the content model |
| label.classification_in_law | Classification in law | a table label in the content model |
| label.cloud_certification | Cloud certification | a table label in the content model |
| label.crisis_management_and_civil_protection_tier_1 | Crisis management and civil protection (tier 1) | a table label in the content model |
| label.critical | Critical | a table label in the content model |
| label.croatia | Croatia | a table label in the content model |
| label.customs_declarations_tier_1 | Customs declarations (tier 1) | a table label in the content model |
| label.cyprus | Cyprus | a table label in the content model |
| label.czechia | Czechia | a table label in the content model |
| label.data_classification | Data classification | a table label in the content model |
| label.defence_command_and_logistics_tier_1 | Defence command and logistics (tier 1) | a table label in the content model |
| label.denmark | Denmark | a table label in the content model |
| label.digital_identity_credentials_tier_0 | Digital identity credentials (tier 0) | a table label in the content model |
| label.dimension | Dimension | a table label in the content model |
| label.document_issuance_history_tier_0 | Document issuance history (tier 0) | a table label in the content model |
| label.education_tier_1 | Education (tier 1) | a table label in the content model |
| label.election_management_and_results_tier_1 | Election management and results (tier 1) | a table label in the content model |
| label.electoral_roll_entry_tier_0 | Electoral roll entry (tier 0) | a table label in the content model |
| label.electricity_grid_control_tier_1 | Electricity grid control (tier 1) | a table label in the content model |
| label.emergency_calls_and_public_safety_radio_tier_1 | Emergency calls and public-safety radio (tier 1) | a table label in the content model |
| label.estonia | Estonia | a table label in the content model |
| label.eu_provider | EU provider | a table label in the content model |
| label.facial_biometric_tier_0 | Facial biometric (tier 0) | a table label in the content model |
| label.finding | Finding | a table label in the content model |
| label.fingerprint_biometric_tier_0 | Fingerprint biometric (tier 0) | a table label in the content model |
| label.finland | Finland | a table label in the content model |
| label.firearms_register_tier_1 | Firearms register (tier 1) | a table label in the content model |
| label.france | France | a table label in the content model |
| label.gdp_current_prices | GDP, current prices | a table label in the content model |
| label.geospatial_base_data_tier_3 | Geospatial base data (tier 3) | a table label in the content model |
| label.germany | Germany | a table label in the content model |
| label.governing_instrument | Governing instrument | a table label in the content model |
| label.government_cloud_in_operation | Government cloud in operation | a table label in the content model |
| label.government_data_centres | Government data centres | a table label in the content model |
| label.government_payroll_and_personnel_tier_1 | Government payroll and personnel (tier 1) | a table label in the content model |
| label.greece | Greece | a table label in the content model |
| label.health_records_tier_2 | Health records (tier 2) | a table label in the content model |
| label.high | High | a table label in the content model |
| label.holding | Holding | a table label in the content model |
| label.holdings | Holdings | a table label in the content model |
| label.hosting_as_sourced | Hosting (as sourced) | a table label in the content model |
| label.hosting_sourced | Hosting sourced | a table label in the content model |
| label.hungary | Hungary | a table label in the content model |
| label.hyperscaler_regions_in_country | Hyperscaler regions in country | a table label in the content model |
| label.indicator | Indicator | a table label in the content model |
| label.infrastructure | Infrastructure | a table label in the content model |
| label.infrastructure_dependency | Infrastructure dependency | a table label in the content model |
| label.intelligence_services_tier_1 | Intelligence services (tier 1) | a table label in the content model |
| label.internet_exchange | Internet exchange | a table label in the content model |
| label.ireland | Ireland | a table label in the content model |
| label.italy | Italy | a table label in the content model |
| label.judicial_criminal_justice_tier_1 | Judicial & criminal justice (tier 1) | a table label in the content model |
| label.jurisdiction_requirement | Jurisdiction requirement | a table label in the content model |
| label.land_area | Land area | a table label in the content model |
| label.land_property_registry_tier_1 | Land & property registry (tier 1) | a table label in the content model |
| label.latvia | Latvia | a table label in the content model |
| label.lithuania | Lithuania | a table label in the content model |
| label.luxembourg | Luxembourg | a table label in the content model |
| label.malta | Malta | a table label in the content model |
| label.mixed | Mixed | a table label in the content model |
| label.national_archives_digital_tier_3 | National archives (digital) (tier 3) | a table label in the content model |
| label.national_digital_identity | National digital identity | a table label in the content model |
| label.national_infrastructure | National infrastructure | a table label in the content model |
| label.netherlands | Netherlands | a table label in the content model |
| label.non_eu_provider | Non-EU provider | a table label in the content model |
| label.non_household_electricity_price | Non-household electricity price | a table label in the content model |
| label.not_stated | Not stated | a table label in the content model |
| label.official_gazette_and_legislation_tier_1 | Official gazette and legislation (tier 1) | a table label in the content model |
| label.operator | Operator | a table label in the content model |
| label.poland | Poland | a table label in the content model |
| label.police_information_systems_tier_1 | Police information systems (tier 1) | a table label in the content model |
| label.population | Population | a table label in the content model |
| label.portugal | Portugal | a table label in the content model |
| label.position | Position | a table label in the content model |
| label.priority | Priority | a table label in the content model |
| label.procurement_route | Procurement route | a table label in the content model |
| label.public_administration_employment_nace_o | Public administration employment (NACE O) | a table label in the content model |
| label.public_health_surveillance_tier_2 | Public health surveillance (tier 2) | a table label in the content model |
| label.records_size | Records / size | a table label in the content model |
| label.register_or_system | Register or system | a table label in the content model |
| label.registers_sourced | Registers sourced | a table label in the content model |
| label.renewables_share_of_electricity | Renewables share of electricity | a table label in the content model |
| label.residence_and_migration_status_tier_1 | Residence and migration status (tier 1) | a table label in the content model |
| label.romania | Romania | a table label in the content model |
| label.slovakia | Slovakia | a table label in the content model |
| label.slovenia | Slovenia | a table label in the content model |
| label.sovereign_cloud_certification | Sovereign cloud certification | a table label in the content model |
| label.sovereign_or_government_cloud | Sovereign or government cloud | a table label in the content model |
| label.spain | Spain | a table label in the content model |
| label.standard | Standard | a table label in the content model |
| label.state | State | a table label in the content model |
| label.state_controlled_national_eid | State-controlled national eID | a table label in the content model |
| label.state_controlled_trust_anchor | State-controlled trust anchor | a table label in the content model |
| label.state_pki_and_qualified_trust_services_tier_0 | State PKI and qualified trust services (tier 0) | a table label in the content model |
| label.statistical_microdata_tier_2 | Statistical microdata (tier 2) | a table label in the content model |
| label.statutory_health_insurance_tier_1 | Statutory health insurance (tier 1) | a table label in the content model |
| label.sweden | Sweden | a table label in the content model |
| label.tax_tier_1 | Tax (tier 1) | a table label in the content model |
| label.treasury_and_state_accounts_tier_1 | Treasury and state accounts (tier 1) | a table label in the content model |
| label.value | Value | a table label in the content model |
| label.vehicle_licensing_tier_1 | Vehicle & licensing (tier 1) | a table label in the content model |
| label.water_management_control_tier_1 | Water management control (tier 1) | a table label in the content model |
<!-- generated:end -->
