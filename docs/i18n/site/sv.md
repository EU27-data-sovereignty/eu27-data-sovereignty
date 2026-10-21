# Swedish (sv): site catalog draft

- Language: sv (site catalog; reads with the home table sv-SE)
- Drafted by: agent B, claude-fable-5-1, 2026-10-21
- Status: draft, machine-translated, not yet reviewed
- Revised by: orchestrator, claude-opus-5-5, 2026-10-21 (applied 48 reviewer suggestions verbatim)

## Strings

| key | en | sv |
|---|---|---|
| s.b85a2bdd1b | Authentication audit log | Revisionslogg för autentisering |
| s.fcb532f087 | Beneficial ownership register | Register över verkliga huvudmän |
| s.96ecaa31b4 | Benefits & pensions | Förmåner och pensioner |
| s.2f1257dc51 | Border and visa systems | Gräns- och viseringssystem |
| s.ec814ead0c | Breeder document scans | Skanningar av grundhandlingar |
| s.f280e2a648 | Business registry | Företagsregister |
| s.d8d788ca5d | Central bank systems | Centralbankssystem |
| s.765efdcdc6 | Civil registry core | Befolkningsregistrets kärna |
| s.aae813dd56 | Classification in law | Klassificering i lag |
| s.3f865d6890 | Cloud certification | Molncertifiering |
| s.3427094904 | Crisis management and civil protection | Krishantering och civilskydd |
| s.04b7b26c8c | Critical | Kritisk |
| s.6b91907643 | Customs declarations | Tulldeklarationer |
| s.ca20bc6b00 | Data classification | Dataklassificering |
| s.3165449154 | Defence command and logistics | Försvarets ledning och logistik |
| s.f089a1fbed | Dependent on non-EU providers | Beroende av leverantörer utanför EU |
| s.72e58b67f4 | Digital identity credentials | Digitala identitetsbevis |
| s.171ec6a77a | Disputed: {why} | Omtvistad: {why} |
| s.04c3e89d9b | Document issuance history | Historik över utfärdade handlingar |
| s.aaf87fe57a | Education | Utbildning |
| s.4e9d205ed7 | Election management and results | Valadministration och valresultat |
| s.f19d170012 | Electoral roll entry | Post i röstlängden |
| s.042b70234d | Electricity grid control | Styrning av elnätet |
| s.f180a9ce79 | Emergency calls and public-safety radio | Nödsamtal och radiokommunikation för samhällssäkerhet |
| s.98bf3b1ffd | Facial biometric | Ansiktsbiometri |
| s.3d64ce6c47 | Fingerprint biometric | Fingeravtrycksbiometri |
| s.5343f3aabe | Firearms register | Vapenregister |
| s.3b9865356c | GDP, current prices | BNP, löpande priser |
| s.0c3b551296 | Geospatial base data | Geografiska grunddata |
| s.5dfe1bc1a0 | Governing instrument | Styrande rättsakt |
| s.c4fe29fe96 | Government cloud in operation | Statligt moln i drift |
| s.ec4f0f9f9e | Government data centres | Statliga datacenter |
| s.9704ed6cc1 | Government payroll and personnel | Statens löner och personal |
| s.982c964c83 | Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished. | Grupperna beskriver vad källorna visar, inte hur suverän en stat är. En placering med låg tillförlitlighet speglar för det mesta forskning som inte är avslutad. |
| s.8061bb6bf8 | Health records | Patientjournaler |
| s.b86fc1b412 | Hosting (as sourced) | Drift (enligt källorna) |
| s.94accd37b7 | Hyperscaler regions in country | Hyperscaler-regioner i landet |
| s.8667bf9045 | If any of the {count} tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: {group}. | {count, plural, one {Om den enda informationstillgången på nivå 0/1 vars drift ännu saknar källa visar sig drivas på infrastruktur utanför EU: {group}.} other {Om någon av de # informationstillgångarna på nivå 0/1 vars drift ännu saknar källa visar sig drivas på infrastruktur utanför EU: {group}.}} |
| s.2948d7b9da | If {indicator} is found to be {value}: {group}. | Om {indicator} visar sig vara {value}: {group}. |
| s.b3f1bf4f30 | Intelligence services | Underrättelsetjänster |
| s.f785330b4c | Internet exchange | Internetknutpunkt |
| s.a91102c85d | Judicial & criminal justice | Rättsväsende och straffrättskipning |
| s.be9109ac1b | Jurisdiction requirement | Krav på jurisdiktion |
| s.a3d31a53fb | Land & property registry | Mark- och fastighetsregister |
| s.99767669ed | Land area | Landareal |
| s.cbbacb3e80 | National archives (digital) | Nationalarkiv (digitalt) |
| s.44749b1cbc | National digital identity | Nationell digital identitet |
| s.6fb2a8a8cc | No central register | Inget centralt register |
| s.e6e1757649 | Non-EU provider | Leverantör utanför EU |
| s.b34eac40f3 | Non-household electricity price | Elpris för icke-hushållskunder |
| s.1652d30cec | Not demonstrated | Inte påvisad |
| s.114883188a | Not stated in sources | Inte angivet i källorna |
| s.fd51e343e2 | Not yet measured | Ännu inte uppmätt |
| s.2f23122d83 | Not yet sized. Capacity for {name} will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. {measured} of {total} holding classes have a sourced measurement so far. | Ännu inte dimensionerad. Kapaciteten för {name} kommer att härledas ur statens egna uppmätta informationstillgångar (antal poster och datamängder), inte skalas från ett annat land. {measured} av {total} klasser av informationstillgångar har hittills en mätning med källa. |
| s.a9b0cdd774 | Not yet verified | Ännu inte verifierad |
| s.c2cce8d695 | Nothing: every input the rule reads is settled by a source. | Inget: varje indatapost som regeln läser är avgjord av en källa. |
| s.3ad8637946 | Of the {n} verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national. | {n, plural, one {För den # verifierade informationstillgången: om en källa anger var infrastrukturen drivs.} other {Hur många av de # verifierade informationstillgångarna som har en källa som anger var infrastrukturen drivs.}} En informationstillgång räknas som beroende bara när ett citerat dokument säger det; tystnad räknas som inte angivet, aldrig som nationell. |
| s.f987414340 | Official gazette and legislation | Officiell tidning och lagstiftning |
| s.d0e687b079 | Operator | Operatör |
| s.f83b48a858 | Police information systems | Polisens informationssystem |
| s.182d37ec74 | Population | Befolkning |
| s.f2fe3e1c9e | Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5. | Prioritet = konsekvens vid förlust (nivå 0: 3, nivå 1: 2, nivå 2: 1, nivå 3: 0) + svårighet att återuppbygga (låg återställbarhet: 2, medel: 1, hög: 0) + känd exponering för leverantörer utanför EU (utanför EU eller blandad: 2, EU-leverantör eller ännu inte känd: 1, nationell: 0). Kritisk är 6 eller mer, Hög är 4 eller 5. |
| s.034dd0deff | Procurement route | Upphandlingsväg |
| s.c622853228 | Public administration employment (NACE O) | Sysselsättning i offentlig förvaltning (NACE O) |
| s.5e46f732e6 | Public health surveillance | Folkhälsoövervakning |
| s.1890a8b969 | Records / size | Poster / storlek |
| s.acb219584d | Renewables share of electricity | Andel förnybar el |
| s.62c114ace1 | Residence and migration status | Uppehålls- och migrationsstatus |
| s.110c7c517b | Secured in law, not yet in practice | Säkrad i lag, ännu inte i praktiken |
| s.5f407d41f3 | Sovereign cloud certification | Certifiering av suveränt moln |
| s.1ca90cb624 | Sovereign in law and in practice | Suverän i lag och i praktiken |
| s.0a4c313dc5 | Sovereign in practice, not secured in law | Suverän i praktiken, inte säkrad i lag |
| s.5c1505aea9 | Sovereign or government cloud | Suveränt eller statligt moln |
| s.2dfa66079d | Standard | Standard |
| s.d7e81c01c8 | State PKI and qualified trust services | Statlig PKI och kvalificerade betrodda tjänster |
| s.1e01ee18be | State-controlled national eID | Statligt kontrollerad nationell eID |
| s.967135dc53 | State-controlled trust anchor | Statligt kontrollerat tillitsankare |
| s.16b62d3922 | Statistical microdata | Statistiska mikrodata |
| s.78d71ef805 | Statutory health insurance | Lagstadgad sjukförsäkring |
| s.9be70f66f8 | Tax | Skatt |
| s.eeac96e96e | The holdings {name} cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. {verified} of {total} holding classes have a verified source; {measured} have a sourced record count or data size. | De informationstillgångar som denna stat ({name}) inte kan låta vara beroende av infrastruktur som en främmande stat kan utöva tvång mot eller stänga av, rangordnade enligt en uttalad regel. {verified} av {total} klasser av informationstillgångar har en verifierad källa; {measured} har ett antal poster eller en datamängd med källa. |
| s.1ef26968be | Tier 0 and 1 holdings for {name} without a verified source yet. Corrections and sources are welcome through the repository's issue template. | {name}: informationstillgångar på nivå 0 och 1 som ännu saknar verifierad källa. Rättelser och källor välkomnas via repositoriets ärendemall. |
| s.5e127373f3 | Treasury and state accounts | Statskassa och statens räkenskaper |
| s.5f11eb7511 | Vehicle & licensing | Fordon och körkort |
| s.7d46fdf50f | Water management control | Styrning av vattensystem |
| s.ea4e96959c | What could move this placement: | Vad som skulle kunna flytta denna placering: |
| s.fd12863535 | no | nej |
| s.fb360f9c09 | yes | ja |
| s.fff7760a9e | {group}. Confidence: {confidence}. With the evidence still open, {name} could be anywhere from '{from}' to '{to}'. | {group}. Tillförlitlighet: {confidence}. Med belägg som ännu inte är avgjorda kan denna stat ({name}) ligga var som helst från ”{from}” till ”{to}”. |
| s.fa84aa0fe2 | {holding} (tier {tier}) | {holding} (nivå {tier}) |
| s.966a5454e4 | {name} described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date. | {name}: en beskrivning utifrån statens egna uppmätta egenskaper. Varje siffra är det publicerade värdet i en låst Eurostat-serie; fotnoten anger serien, dimensionerna och hämtningsdatumet. |
| s.47c8fcf67a | {shown} of {total} posture entries have a verified source. The others were researched from public policy documents but are withheld here until each is checked against the governing instrument. | {shown} av {total} poster om ställningen har en verifierad källa. De övriga har undersökts utifrån offentliga policydokument men undanhålls här tills var och en har kontrollerats mot den styrande rättsakten. |
| s.f7a15511d4 | Counted from the facts each state's report prints: holdings with a sourced register, how many of them have sourced hosting, and the infrastructure dependency their sources state. Not stated means no printed source says; it is never counted as national. | Räknat utifrån de uppgifter som varje stats rapport visar: informationstillgångar med ett register med källa, hur många av dem som har drift med källa, och det infrastrukturberoende som deras källor anger. Inte angivet betyder att ingen visad källa säger det; det räknas aldrig som nationellt. |
| s.26e5bd9d84 | Every holding whose hosting a checked source states, by member state: {printed} printed, and any withheld by the fact check marked as disputed. Each cell is the one the state's own report prints, with the same source. A holding not listed here has no sourced hosting yet; that is a gap in the evidence, not a finding that it is hosted nationally. | Varje informationstillgång vars drift en kontrollerad källa anger, per medlemsstat: {printed} visas, och de som faktagranskningen undanhållit markeras som omtvistade. Varje cell är den som statens egen rapport visar, med samma källa. En informationstillgång som inte finns med här har ännu ingen drift med källa; det är en lucka i beläggen, inte en iakttagelse att den drivs nationellt. |
| s.3d9ef2e1a4 | Key infrastructure and hosting | Central infrastruktur och drift |
| s.3b7aee0921 | Register or system | Register eller system |
| s.ddca7ab7f4 | A gap means not yet sourced. It never means the thing does not exist. | En lucka betyder ännu utan källa. Den betyder aldrig att saken inte finns. |
| s.5d8970fa99 | A value that no checked source supports is withheld and shown as a gap. A gap means not yet sourced, never that the thing does not exist. | Ett värde som ingen kontrollerad källa stöder undanhålls och visas som en lucka. En lucka betyder ännu utan källa, aldrig att saken inte finns. |
| s.1c023ff571 | A vetting run then re-examined every printed fact, and after it the gaps. It looked for a better source, for newer information and for any source that disagrees. Each of its findings was judged by a blind reviewer, shown the quote and URL but never the proposed value. Runs: {runs}. Reviewer model: {models}, the same model as the researcher. | En efterkontrollskörning gick sedan igenom varje visad uppgift på nytt, och därefter luckorna. Den sökte efter en bättre källa, efter nyare information och efter varje källa som säger emot. Var och en av dess iakttagelser bedömdes av en blind bedömare, som fick se citatet och URL:en men aldrig det föreslagna värdet. Körningar: {runs}. Bedömarmodell: {models}, samma modell som forskaren. |
| s.eb41f68213 | Anyone in any member state may submit a source or check a printed fact, through public issue forms. A submitted source passes the same mechanical checks as agent research. A fact counts as verified by a person only under the two-person rule: confirmed by someone on the reviewer roster, who did not submit it, who reads the source's language, and who declared no conflict of interest. One such rejection makes a fact disputed; two withdraw it, unless two reviewers confirmed it. | Vem som helst i vilken medlemsstat som helst kan lämna in en källa eller kontrollera en visad uppgift via offentliga ärendeformulär. En inlämnad källa går igenom samma mekaniska kontroller som agenternas forskning. En uppgift räknas som verifierad av en person bara enligt tvåpersonsregeln: bekräftad av någon på granskarlistan som inte själv lämnade in den, som läser källans språk och som har förklarat att ingen intressekonflikt finns. Ett sådant avslag gör en uppgift omtvistad; två drar tillbaka den, såvida inte två granskare har bekräftat den. |
| s.e6c7329679 | Before anything is published, every printed fact is checked once more, exactly as printed, by a second model: the one that did not write it. The checker fetches the cited source and decides whether it supports the statement as printed. A production deploy is refused unless every printed fact has a current verdict of supported. The rule, the steps and each fact's verdict are in the fact-check appendix. | Innan något publiceras kontrolleras varje visad uppgift en gång till, exakt som den visas, av en andra modell: den som inte skrev den. Kontrollanten hämtar den citerade källan och avgör om den stöder påståendet som det visas. En driftsättning i produktion vägras om inte varje visad uppgift har ett aktuellt utlåtande om att den stöds. Regeln, stegen och varje uppgifts utlåtande finns i faktagranskningsbilagan. |
| s.05d27dcc23 | Calculations | Beräkningar |
| s.fd9f9cff11 | Categorical findings (infrastructure dependency, sovereignty indicators): admitted only when a second, independent automated reviewer reached the same value from the same quote. | Kategoriska iakttagelser (infrastrukturberoende, suveränitetsindikatorer): tas in bara när en andra, oberoende automatiserad bedömare kom fram till samma värde ur samma citat. |
| s.14a628e6d3 | Checked by | Kontrollerad av |
| s.d22fca0f44 | Citizen submissions staged | Medborgarinlämningar som hålls åtskilda |
| s.4f23e1e7f8 | Citizens and human review | Medborgare och mänsklig granskning |
| s.06e8db2dfd | Claims | Påståenden |
| s.4108482c08 | Confidence is how many groups a state could still reach if every unknown resolved for or against it: one group is High, two Medium, three or more Low. Within a group, states are alphabetical; the order carries no meaning. | Tillförlitligheten är hur många grupper en stat fortfarande skulle kunna nå om varje okänd faktor avgjordes för eller emot den: en grupp är Hög, två Medelhög, tre eller fler Låg. Inom en grupp står staterna i alfabetisk ordning; ordningen betyder ingenting. |
| s.66e12969c2 | Count | Antal |
| s.ed1c64ab57 | Data-sovereignty placement. An input without a checked source is unknown and counts as not demonstrated: never as sovereign, never as dependent. Each state is placed by the first rule it meets, in this order: | Placering i fråga om datasuveränitet. En indatapost utan kontrollerad källa är okänd och räknas som inte påvisad: aldrig som suverän, aldrig som beroende. Varje stat placeras enligt den första regel den uppfyller, i denna ordning: |
| s.1052689464 | Dataset | Datamängd |
| s.2a4e3cb3c6 | Decimals | Decimaler |
| s.eb559b8cbc | Dependent on non-EU providers: a source shows a tier 0 or 1 holding on non-EU infrastructure, or a national eID or trust anchor outside state or EU control. | Beroende av leverantörer utanför EU: en källa visar en informationstillgång på nivå 0 eller 1 på infrastruktur utanför EU, eller en nationell eID eller ett tillitsankare utanför statens eller EU:s kontroll. |
| s.d203be5dfd | English wording of a non-English source is a machine translation or machine summary. Its figures are checked against the original; its words are not. | Engelsk formulering av en icke-engelsk källa är en maskinöversättning eller en maskinell sammanfattning. Dess siffror kontrolleras mot originalet; dess ord gör det inte. |
| s.d4a05b67a6 | Eurostat figures: the value was read from a pinned Eurostat dataset through its API and compared with the table cell, within 0.5%. The raw API response is stored and its SHA-256 recorded in model/fetch_manifest.csv. The footnote names the dataset, its dimensions and the retrieval date. | Eurostat-siffror: värdet lästes från en låst Eurostat-datamängd via dess API och jämfördes med tabellcellen, inom 0,5 %. Det råa API-svaret lagras och dess SHA-256 antecknas i model/fetch_manifest.csv. Fotnoten anger datamängden, dess dimensioner och hämtningsdatumet. |
| s.188de23f5b | Every cited source is re-fetched periodically and each quote looked for again. A fact whose quote has vanished, or whose source is gone, is withheld as disputed. A refusal to serve the page changes nothing. | Varje citerad källa hämtas på nytt med jämna mellanrum och varje citat söks upp igen. En uppgift vars citat har försvunnit, eller vars källa är borta, undanhålls som omtvistad. Att servern vägrar lämna ut sidan ändrar ingenting. |
| s.2b913254a8 | Everything is built from the project's repository. `./run.sh reproduce` rebuilds every output in a fresh clone and compares it with the published one. `./run.sh reproduce --evidence` also re-fetches every cited source and checks every quote again. The git commit and the data bundle's SHA-256 this document was built from are printed on its title page. | Allt byggs från projektets repositorium. `./run.sh reproduce` bygger om varje utdata i en ny klon och jämför den med den publicerade. `./run.sh reproduce --evidence` hämtar dessutom varje citerad källa på nytt och kontrollerar varje citat igen. Den git-commit och den SHA-256 för datapaketet som detta dokument byggdes från står på dess titelsida. |
| s.84d987fe02 | Evidence grades | Beläggsgrader |
| s.04b0dda32a | Fact written by | Uppgift skriven av |
| s.228587d1aa | Facts disputed by a reviewer | Uppgifter som en granskare bestridit |
| s.18a1dacbc5 | Facts verified by a person | Uppgifter verifierade av en person |
| s.d54360e78a | Facts withdrawn after review | Uppgifter tillbakadragna efter granskning |
| s.1f20e66b17 | Figure | Siffra |
| s.96e578211a | Filters | Filter |
| s.0b134e18cb | Findings or items | Iakttagelser eller poster |
| s.252adc9f26 | Fundamentals are Eurostat values at a pinned period, read through the dissemination API. Each is multiplied into the unit shown and rounded, and must reproduce the published value within 0.5%: | Grunduppgifterna är Eurostat-värden för en låst period, lästa via spridnings-API:et. Vart och ett räknas om till den visade enheten och avrundas, och måste återge det publicerade värdet inom 0,5 %: |
| s.aecc49c153 | Grade | Grad |
| s.5012de0774 | How good is the best source behind each fact? Each cited host is classified once. An archived copy counts as the page it archived. The classification was drawn up by an agent and has not been reviewed by a person. | Hur bra är den bästa källan bakom varje uppgift? Varje citerad värd klassificeras en gång. En arkiverad kopia räknas som den sida den arkiverade. Klassificeringen upprättades av en agent och har inte granskats av någon person. |
| s.1ac6e0db9e | How sources were found | Hur källorna hittades |
| s.40176d930b | Human review | Mänsklig granskning |
| s.40f3f0b36f | In this build, {passing} of {printed} printed facts pass the fact check. | I detta bygge klarar {passing} av {printed} visade uppgifter faktagranskningen. |
| s.7539231e04 | Infrastructure exposure counts, for each state, the verified holdings whose cited source says where the infrastructure runs. Silence counts as not stated, never as national. | Infrastrukturexponering räknar, för varje stat, de verifierade informationstillgångar vars citerade källa säger var infrastrukturen drivs. Tystnad räknas som inte angivet, aldrig som nationell. |
| s.90a031edb0 | Key infrastructure and hosting, the EU-27 overview, lists every holding whose hosting a checked source states. Each cell is a copy of the one the state's own report prints, so it has the same source and the same fact check, and a withheld value stays withheld. Its counts per state are of printed facts only. | Central infrastruktur och drift, EU-27-översikten, listar varje informationstillgång vars drift en kontrollerad källa anger. Varje cell är en kopia av den som statens egen rapport visar, så den har samma källa och samma faktagranskning, och ett undanhållet värde förblir undanhållet. Dess antal per stat gäller enbart visade uppgifter. |
| s.0c448a5f23 | Latest recheck | Senaste omkontroll |
| s.51aff04e8d | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Maskinkontrollerad, inte verifierad av människor. Automatiserade agenter hittade dessa källor och kontrollerade dem mekaniskt; ingen person har granskat iakttagelserna. Engelsk formulering av en icke-engelsk källa är en maskinöversättning eller en maskinell sammanfattning av den citerade texten. Betrakta varje uppgift som ett spår till dess angivna källa, inte som fastställd. Rättelser välkomnas via repositoriets ärendemall. |
| s.8b5cf8d60c | Most states do not publish where their critical registers are hosted, so placements are mostly of low confidence. That is a finding about transparency, not about sovereignty. | De flesta stater publicerar inte var deras kritiska register driftas, så placeringarna har för det mesta låg tillförlitlighet. Det är en iakttagelse om transparens, inte om suveränitet. |
| s.b31b7fac2a | No person has verified any finding. Agents found and checked everything. | Ingen person har verifierat någon iakttagelse. Agenter hittade och kontrollerade allt. |
| s.04c299e1b3 | Not demonstrated: neither. | Inte påvisad: ingetdera. |
| s.61348d3cc0 | Not reproducible byte for byte: agent research gives different findings if run again, so what is reproducible is their admission, from the recorded outputs. Also not: the posters (browser screenshots), and the hash of a page rendered in a browser. | Inte reproducerbart byte för byte: agenternas forskning ger andra iakttagelser om den körs igen, så det som är reproducerbart är vilka av dem som togs in, utifrån de registrerade utdata. Inte heller: affischerna (skärmbilder från webbläsaren) och hashvärdet för en sida återgiven i en webbläsare. |
| s.170a28a9db | Period | Period |
| s.f7fa7832f9 | Printed facts | Visade uppgifter |
| s.bcb88598d7 | Priority of a holding. Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5. | En informationstillgångs prioritet. Prioritet = konsekvens vid förlust (nivå 0: 3, nivå 1: 2, nivå 2: 1, nivå 3: 0) + svårighet att återuppbygga (låg återställbarhet: 2, medel: 1, hög: 0) + känd exponering för leverantörer utanför EU (utanför EU eller blandad: 2, EU-leverantör eller ännu inte känd: 1, nationell: 0). Kritisk är 6 eller mer, Hög är 4 eller 5. |
| s.ee19cf967e | Questions answered on the web | Frågor besvarade på webben |
| s.ddf48497b8 | Quote check of the first research runs | Citatkontroll av de första forskningskörningarna |
| s.adeb29b097 | Reproducing this document | Att reproducera detta dokument |
| s.1338a3ee0c | Research agents, one per member state, looked for each critical holding and each indicator. Each claim needed a verbatim quote of 8 to 60 words from an exact URL. Nothing an agent returned was used until it passed the mechanical checks below. Agent output is staged separately and is never rendered. | Forskningsagenter, en per medlemsstat, sökte efter varje kritisk informationstillgång och varje indikator. Varje påstående krävde ett ordagrant citat på 8 till 60 ord från en exakt URL. Inget som en agent lämnade användes förrän det hade klarat de mekaniska kontrollerna nedan. Agenternas utdata hålls åtskilda och återges aldrig. |
| s.0d73a1c086 | Researched claims (holdings, operators, legal bases, indicators): the cited page or PDF was downloaded and its SHA-256 recorded, and the quoted text was found in the extracted document by literal matching. Every number and date in the printed value was found in the original-language quote; the English wording is a machine summary of the quote unless it appears in it verbatim. An archived copy was looked up on the Internet Archive; where none exists the footnote says so. | Undersökta påståenden (informationstillgångar, operatörer, rättsliga grunder, indikatorer): den citerade sidan eller PDF:en laddades ned och dess SHA-256 antecknades, och den citerade texten hittades i det extraherade dokumentet genom ordagrann matchning. Varje siffra och varje datum i det visade värdet hittades i citatet på originalspråket; den engelska formuleringen är en maskinell sammanfattning av citatet om den inte förekommer ordagrant i det. En arkiverad kopia söktes upp i Internet Archive; där ingen finns säger fotnoten det. |
| s.5016356d5e | Reviewers on the roster | Granskare på listan |
| s.a29f025627 | Scale | Skala |
| s.635dcfcb5a | Secured in law, not yet in practice: the statute, without the practice test. | Säkrad i lag, ännu inte i praktiken: lagen, utan praktiktestet. |
| s.926a4d7e8c | Source tiers | Källnivåer |
| s.9ad33161bb | Sovereign in law and in practice: a statute keeps government data under national or EU jurisdiction, and at least 75% of verified tier 0/1 holdings run on national or EU infrastructure, the trust anchor and eID are state-controlled, and the state runs its own data centres or government cloud. | Suverän i lag och i praktiken: en lag håller offentliga data under nationell eller EU:s jurisdiktion, och minst 75 % av de verifierade informationstillgångarna på nivå 0/1 drivs på nationell infrastruktur eller EU-infrastruktur, tillitsankaret och eID:n är statligt kontrollerade, och staten driver egna datacenter eller ett eget statligt moln. |
| s.4324ca9554 | Sovereign in practice, not secured in law: the practice test, without the statute. | Suverän i praktiken, inte säkrad i lag: praktiktestet, utan lagen. |
| s.cf84687053 | Strong | Stark |
| s.d11347ce3a | Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. | Stark: en T1- eller T2-källa (ett auktoritativt original eller ett behörigt offentligt organ); en officiell eller primär källa; citatet hittat exakt i det hashade dokumentet; en arkiverad kopia av exakt den URL:en; inget namn i värdet som saknas i citatet; och värdet antingen citerat från en engelsk källa, hittat ordagrant i originalet eller grundat på siffror som matchats i originalet. En kategorisk iakttagelse är Stark först efter en blind bedömning (en bedömare som fått se citatet och URL:en men inte det föreslagna värdet). Standard: varje obligatorisk kontroll klarad, men en av dessa inte uppfylld. Allt därunder visas inte. Verifierad: Stark, och bekräftad av en person enligt tvåpersonsregeln: någon på granskarlistan, en annan än den som lämnade in den, som läser källans språk och har förklarat att ingen intressekonflikt finns. |
| s.9f1a1d5e3e | T1 authoritative original (official law portal, statistics office, Eurostat) | T1 auktoritativt original (officiell lagportal, statistikmyndighet, Eurostat) |
| s.75974ad5f7 | T2 competent public body or audit office | T2 behörigt offentligt organ eller revisionsorgan |
| s.c342fa1f4f | T3 other institution or company | T3 annan institution eller företag |
| s.a544050c90 | T4 secondary (unofficial law mirror, press, encyclopedia) | T4 sekundär (inofficiell spegelwebbplats för lagtext, press, uppslagsverk) |
| s.f1fceee56b | The blind reviewer during research was the same model as the researcher, so the two readings can share its blind spots. The fact check before each deploy uses a different model, which narrows that risk but does not remove blind spots that models share. | Den blinda bedömaren under forskningen var samma modell som forskaren, så de två läsningarna kan dela dess blinda fläckar. Faktagranskningen före varje driftsättning använder en annan modell, vilket minskar den risken men inte tar bort blinda fläckar som modellerna har gemensamt. |
| s.61e3fb1ddf | The cross-model fact check before every deploy | Faktagranskningen med en annan modell före varje driftsättning |
| s.3882bb002a | The printed value is checked against its quote at build time. Every number and date in it must appear in the original-language quote, read in any EU number format. A number found only in the English translation does not count. An abbreviation not found in the quote is shown in the fact's checklist. A value that is not a verbatim extract is a machine summary of the quote, and is labelled as one. | Det visade värdet kontrolleras mot sitt citat vid byggtillfället. Varje siffra och varje datum i det måste förekomma i citatet på originalspråket, läst i vilket EU-talformat som helst. En siffra som bara finns i den engelska översättningen räknas inte. En förkortning som inte hittas i citatet visas i uppgiftens checklista. Ett värde som inte är ett ordagrant utdrag är en maskinell sammanfattning av citatet och märks som en sådan. |
| s.67ac669b7c | The web page's Ask feature answers questions using only these sourced findings, with a citation for every fact. Each question is sent to Anthropic's API to generate the answer and is not stored by this site. The model is told the findings are machine-checked and to say so in every answer. | Webbsidans Fråga-funktion besvarar frågor enbart utifrån dessa iakttagelser med källa, med en källhänvisning för varje uppgift. Varje fråga skickas till Anthropics API för att generera svaret och lagras inte av denna webbplats. Modellen får veta att iakttagelserna är maskinkontrollerade och ska säga det i varje svar. |
| s.4220d202c0 | There is no numeric confidence score: nothing has calibrated one. | Det finns ingen numerisk tillförlitlighetspoäng: inget har kalibrerat någon. |
| s.a0de0a20ed | This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: {facts} facts are printed, {gaps} values are withheld as gaps, and {disputed} are withheld as disputed. | Denna bilaga genereras från den kod och de data som tog fram detta dokument. Varje regel nedan är den regel som bygget kör, och varje tal är räknat från de filer det läser. I detta bygge: {facts, plural, one {# uppgift visas} other {# uppgifter visas}}, {gaps, plural, one {# värde undanhålls som lucka} other {# värden undanhålls som luckor}} och {disputed, plural, one {# undanhålls som omtvistat} other {# undanhålls som omtvistade}}. |
| s.aed3b8c6a7 | Verified | Verifierad |
| s.8524fff511 | Vetting outcome | Resultat av efterkontrollen |
| s.7c88c313f1 | What must hold for a fact to be printed | Vad som måste gälla för att en uppgift ska visas |
| s.cdba8c69aa | What this does not establish | Vad detta inte fastställer |
| s.3ef3f040f0 | What this is, and what it is not | Vad detta är, och vad det inte är |
| s.ce296c876c | anything else: unrecorded, a person, or a program | allt annat: oregistrerat, en person eller ett program |
| s.4cc558b843 | corroborated | bestyrkt |
| s.729e6ed847 | disputed | omtvistad |
| s.b55e22fe78 | exact | exakt |
| s.a6dfdeaa3a | gone | borta |
| s.67805069b9 | loose | ungefärlig |
| s.8012ff51a0 | unchanged | oförändrad |
| s.408e9edfd6 | unreachable | onåbar |
| s.625916084e | Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | Kräver en lag eller en bindande föreskrift att offentliga data (eller säkerhetsklassade offentliga data) lagras och behandlas under nationell eller EU:s jurisdiktion? |
| s.ca310cd530 | Does the state operate its own government data centres that are in operation today? | Driver staten egna statliga datacenter som är i drift i dag? |
| s.cf7088eefc | Is a cloud certification that requires immunity from non-EU law in force or adopted for government use? | Är en molncertifiering som kräver immunitet mot lagstiftning utanför EU i kraft eller antagen för offentlig användning? |
| s.a3e860461c | Is a national sovereign or government cloud platform in operation (not announced)? | Är en nationell suverän eller statlig molnplattform i drift (inte bara aviserad)? |
| s.658d6ce48a | Is the government's data classification scheme established in a statute or binding regulation? | Är statens system för dataklassificering fastställt i en lag eller en bindande föreskrift? |
| s.2d29475e37 | Is the national electronic identity scheme operated by the state or a state-controlled body? | Drivs det nationella systemet för elektronisk identitet av staten eller ett statligt kontrollerat organ? |
| s.922e29d89c | Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | Drivs roten i statens infrastruktur för öppna nycklar, eller dess kvalificerade betrodda tjänst, av staten eller ett statligt kontrollerat organ? |
| s.9e80ea69fc | Run {command} to regenerate the bundle. | Kör {command} för att generera om paketet. |
| s.c77394b252 | Loading the map… | Läser in kartan… |
| s.78afc1371f | Map of the EU-27 by data-sovereignty group | Karta över EU-27 efter datasuveränitetsgrupp |
| s.e3c6ef524e | {name}: {group}, High confidence | {name}: {group}, hög tillförlitlighet |
| s.534ce8e519 | {name}: {group}, Low confidence | {name}: {group}, låg tillförlitlighet |
| s.b60bf227ad | {name}: {group}, Medium confidence | {name}: {group}, medelhög tillförlitlighet |
| s.d523ebbd10 | Country | Land |
| s.bcf29b342c | Hide data table | Dölj datatabell |
| s.246be074fc | Hover or tab to a cell for its value and source. | Håll pekaren över en cell, eller gå till den med tabb, för att se dess värde och källa. |
| s.58fe5d4e7a | Show data table | Visa datatabell |
| s.0f8f4bbe66 | Colour scale from {low} to {high} | Färgskala från {low} till {high} |
| s.e3e89bb064 | below {value} {unit} — {label} | under {value} {unit} — {label} |
| s.dfdb505f72 | Counts of verified evidence, not a ranking of how sovereign a state is. | Antal verifierade belägg, inte en rangordning av hur suverän en stat är. |
| s.aeff1bc997 | Facts | Uppgifter |
| s.72f9d33997 | Holdings | Informationstillgångar |
| s.5bdb3bb46b | Less evidence | Färre belägg |
| s.d4fd0a232e | Measure | Mått |
| s.d868b45fe0 | Member states | Medlemsstater |
| s.4bab2d8fe1 | More | Fler |
| s.672c9e09e8 | Open country → | Öppna landet → |
| s.cada9ca9eb | Tier 0 | Nivå 0 |
| s.3a88f501b3 | Verified evidence by state | Verifierade belägg per stat |
| s.043cff352e | {holdings} of {holdingsTotal} holdings verified · {facts, plural, one {# sourced fact} other {# sourced facts}} | {holdings} av {holdingsTotal} informationstillgångar verifierade · {facts, plural, one {# uppgift med källa} other {# uppgifter med källa}} |
| s.c3679c21c3 | {name}: {holdings} of {holdingsTotal} holdings verified, {tier0} of {tier0Total} tier 0, {facts, plural, one {# sourced fact} other {# sourced facts}} | {name}: {holdings} av {holdingsTotal} informationstillgångar verifierade, {tier0} av {tier0Total} på nivå 0, {facts, plural, one {# uppgift med källa} other {# uppgifter med källa}} |
| s.835bc2011e | {tier0} of {tier0Total} tier 0 holdings verified | {tier0} av {tier0Total} informationstillgångar på nivå 0 verifierade |
| s.ce0770ac86 | Choose entry by | Välj ingång efter |
| s.05769b70b7 | Choose your entry point | Välj din ingång |
| s.81ff3110e4 | Guides by audience | Guider efter målgrupp |
| s.faad2c5c10 | Guides by task | Guider efter arbetsuppgift |
| s.3b98e97b40 | I am… | Jag är… |
| s.6f33a0a6ed | I need to… | Jag behöver… |
| s.3c90d4c91b | Section {n} | Avsnitt {n} |
| s.97d5abd9c8 | Source {n}: {label}. Evidence: {evidence} | Källa {n}: {label}. Belägg: {evidence} |
| s.83db15cb2f | Cloud Sovereignty | Molnsuveränitet |
| s.fe17d950e1 | Cloud Sovereignty for Europe | Molnsuveränitet för Europa |
| s.c2425b1244 | Navigate{br}{phrase} | Navigera i{br}{phrase} |
| s.17b90bc012 | Understand. Comply. Decide. Stay sovereign. | Förstå. Följ reglerna. Besluta. Förbli suverän. |
| s.6f50cd14eb | A source says the system runs on state infrastructure. | En källa säger att systemet drivs på statlig infrastruktur. |
| s.57e128cfba | All member states | Alla medlemsstater |
| s.f816a4e57e | All tiers | Alla nivåer |
| s.465681c687 | Disputed | Omtvistad |
| s.1303e4380a | EU provider | EU-leverantör |
| s.b7e3dcb83c | Infrastructure dependency | Infrastrukturberoende |
| s.6fb6b67ddd | Member state | Medlemsstat |
| s.c0dcb865ad | Mixed | Blandad |
| s.35e307703a | National data centres with cloud access where required. | Nationella datacenter med molnåtkomst där det krävs. |
| s.bcacbfd850 | National infrastructure | Nationell infrastruktur |
| s.d286d81d00 | No rows match these filters. | Inga rader matchar dessa filter. |
| s.c092c44522 | Not stated | Inte angivet |
| s.6cdea7451a | Run by a provider or platform based elsewhere in the EU. | Drivs av en leverantör eller plattform med säte på annan plats i EU. |
| s.f65e66aecd | Search registers, operators or providers | Sök register, operatörer eller leverantörer |
| s.1f1f4ae384 | The fact check could not confirm it; withheld until rechecked. | Faktagranskningen kunde inte bekräfta det; undanhållet tills det kontrollerats på nytt. |
| s.120772e5ec | The source names the system but not where it runs. | Källan namnger systemet men inte var det drivs. |
| s.5bd44ebe63 | Tier | Nivå |
| s.519c7b88ec | Tier {t} | Nivå {t} |
| s.01561ccd29 | {n, plural, one {# holding} other {# holdings}} | {n, plural, one {# informationstillgång} other {# informationstillgångar}} |
| s.69020dbcaa | {shown} of {total} rows | {shown} av {total} rader |
| s.eaebc1bf76 | Language: {name} | Språk: {name} |
| s.d85a8f2af0 | Corrections and sources welcome via {link}. | Rättelser och källor välkomnas via {link}. |
| s.9cf83d1f40 | Dark mode | Mörkt läge |
| s.5b9ad38e16 | EU27.CLOUD home | Startsida för EU27.CLOUD |
| s.c5a046052e | EU27.CLOUD — European Union Data Sovereignty Initiative | EU27.CLOUD — European Union Data Sovereignty Initiative |
| s.6d0b23c56b | EU27.CLOUD, European Union Data Sovereignty Initiative | EU27.CLOUD, European Union Data Sovereignty Initiative |
| s.1b7ae26250 | Independent research, not affiliated with any government or EU body. | Oberoende forskning, inte knuten till någon regering eller något EU-organ. |
| s.3d3791aae5 | Light mode | Ljust läge |
| s.6e3715ac61 | MIT licensed. | MIT-licensierad. |
| s.62bce9422f | Main | Huvudmeny |
| s.0a4470d64e | Skip to content | Hoppa till innehållet |
| s.c29220f958 | Switch to dark mode | Byt till mörkt läge |
| s.fc45091249 | Switch to light mode | Byt till ljust läge |
| s.56a5813065 | the corrections form | rättelseformuläret |
| s.26f6f10353 | Method · how this was made | Metod · hur detta gjordes |
| s.7e439c353e | On this page | På denna sida |
| s.06ec582dac | Priority = | Prioritet = |
| s.19d87d1bde | Priority of a holding | En informationstillgångs prioritet |
| s.09ca55ca52 | Share | Andel |
| s.38e9199be7 | {label}, all states | {label}, alla stater |
| s.50cb90be5a | Generated {date}. | Genererad {date}. |
| s.94cae35178 | How every fact was checked | Hur varje uppgift kontrollerades |
| s.0149001987 | How this was built | Hur detta byggdes |
| s.f834acfd05 | Archived copy | Arkiverad kopia |
| s.7ef8384426 | Each source is listed once. The hash identifies the exact document that was fetched; the quote under each claim is text found in it by machine, in its original language, then a machine translation where the source is not in English, then the checks the claim passed. | Varje källa listas en gång. Hashvärdet identifierar exakt det dokument som hämtades; citatet under varje påstående är text som en maskin hittat i det, på originalspråket, därefter en maskinöversättning där källan inte är på engelska, och därefter de kontroller påståendet klarat. |
| s.14caa5be28 | Evidence grades. | Beläggsgrader. |
| s.6cc3364a24 | Open source | Öppna källan |
| s.2eb56be3c2 | Sources | Källor |
| s.9c862eb9f0 | Value {value} at {locator} | Värde {value} ({locator}) |
| s.a52b2a1bc3 | retrieved {date} | hämtad {date} |
| s.cf676b1c20 | {value} of {max} | {value} av {max} |
| s.c5b7db8b29 | How does the data-sovereignty ranking work, and how confident is it? | Hur fungerar rangordningen efter datasuveränitet, och hur tillförlitlig är den? |
| s.a3308aeab5 | Is it known where Belgium’s critical registers are hosted? | Är det känt var Belgiens kritiska register driftas? |
| s.bb76dfbf61 | What does "not demonstrated" mean in the ranking? | Vad betyder ”inte påvisad” i rangordningen? |
| s.68478ccc35 | Which holdings are still unverified for Estonia? | Vilka informationstillgångar är fortfarande overifierade för Estland? |
| s.964ca95667 | Which member states have a law keeping government data under national jurisdiction? | Vilka medlemsstater har en lag som håller offentliga data under nationell jurisdiktion? |
| s.e851648d32 | Who operates Germany’s population register, and under which law? | Vem driver Tysklands befolkningsregister, och enligt vilken lag? |
| s.2d762b287f | checked sources, each hashed and quoted | kontrollerade källor, var och en hashad och citerad |
| s.ee2dc54c03 | critical holdings with a checked source | kritiska informationstillgångar med en kontrollerad källa |
| s.0716862035 | holding classes in {n} tiers, one taxonomy for all 27 | klasser av informationstillgångar på {n, plural, one {# nivå} other {# nivåer}}, en taxonomi för alla 27 |
| s.0d0529aac3 | holdings classed as hard to rebuild | informationstillgångar klassade som svåra att återuppbygga |
| s.91f2776860 | holdings sourced to an EU provider or mixed hosting | informationstillgångar vars källa anger en EU-leverantör eller blandad drift |
| s.8aec1d10d9 | placements still at Low confidence | placeringar som fortfarande har låg tillförlitlighet |
| s.241bbf18a2 | states with a sourced jurisdiction requirement | stater med ett krav på jurisdiktion med källa |
| s.8263673446 | states with a sourced sovereign cloud certification | stater med en certifiering av suveränt moln med källa |
| s.1722e9149a | states with a sourced state-controlled eID | stater med en statligt kontrollerad eID med källa |
| s.2fae75510d | states with a sourced state-controlled trust anchor | stater med ett statligt kontrollerat tillitsankare med källa |
| s.7211854229 | states with any sourced hosting | stater med drift med källa för minst en informationstillgång |
| s.181f5d30d2 | states with sourced government data centres | stater med statliga datacenter med källa |
| s.75a1a193a3 | tier 0 holdings whose hosting a source states | informationstillgångar på nivå 0 vars drift en källa anger |
| s.01858f5a62 | values withheld as gaps or disputed, each one a question | värden undanhållna som luckor eller omtvistade, vart och ett en fråga |
| s.c09de98f08 | {n} of 27 | {n} av 27 |
| s.0e9f7be095 | {n} of {total} | {n} av {total} |
| s.eec3fda3e7 | A baseline for an impact assessment that others can reproduce. | En utgångspunkt för en konsekvensbedömning som andra kan reproducera. |
| s.231d586afd | A baseline you did not have to commission, with every fact linked to its source. | En utgångspunkt du inte behövde beställa, med varje uppgift länkad till sin källa. |
| s.043e4c8e36 | A clear burden of proof: on this site a gap means “not demonstrated”, never “sovereign”. | En tydlig bevisbörda: på denna webbplats betyder en lucka ”inte påvisad”, aldrig ”suverän”. |
| s.800a1bab1c | A cross-sector map for an all-hazards assessment. | En sektorsövergripande karta för en bedömning av alla hot och risker. |
| s.a856f76fdf | A filter that combines low recoverability with unknown or non-EU hosting. | Ett filter som kombinerar låg återställbarhet med okänd drift eller drift utanför EU. |
| s.a22a342f8d | A major cloud contract is up for renewal. | Ett stort molnavtal ska förnyas. |
| s.fa4dadae15 | A minister asks “are we exposed?” | En minister frågar: ”Är vi exponerade?” |
| s.250ffcac56 | A national cloud strategy is being drafted or renewed. | En nationell molnstrategi håller på att tas fram eller förnyas. |
| s.b62c67154e | A national risk assessment. | En nationell riskbedömning. |
| s.475db6333a | A one-page brief per country. | En sammanfattning på en sida per land. |
| s.5c5d692d28 | A one-page country brief for decision makers. | En landssammanfattning på en sida för beslutsfattare. |
| s.ea3fdab757 | A parliamentary question after a news story about cloud contracts. | En parlamentsfråga efter en nyhet om molnavtal. |
| s.e974d7da17 | A peer state announces a sovereign cloud and the press asks “why not us?” | En jämförbar stat aviserar ett suveränt moln och pressen frågar: ”Varför inte vi?” |
| s.053f428fe0 | A risk class with sources behind it: jurisdictional exposure, where a holding is documented on infrastructure outside national control. | En riskklass med källor bakom sig: jurisdiktionell exponering, där en informationstillgång är dokumenterad på infrastruktur utanför nationell kontroll. |
| s.78610e43d5 | A supplier describes its offer as a “sovereign cloud”. | En leverantör beskriver sitt erbjudande som ett ”suveränt moln”. |
| s.10e16699d4 | A tender that says “data in an EU region” describes where servers sit. It does not say whose law the provider answers to. You need criteria you can cite when a losing bidder challenges the award. | Ett upphandlingsunderlag som anger ”data i en EU-region” beskriver var servrarna står. Det säger inte vems lag leverantören lyder under. Du behöver kriterier du kan hänvisa till när en förlorande anbudsgivare överklagar tilldelningen. |
| s.01263cd27f | A view of where your gap lies. If government data centres are sourced but a jurisdiction requirement is not, the open work is a statute and documentation rather than buildings. | En bild av var din lucka ligger. Om statliga datacenter har källa men ett krav på jurisdiktion inte har det, är det som återstår en lag och dokumentation snarare än byggnader. |
| s.227488de9f | A view of which top-tier holdings have no documented national or EU hosting. | En bild av vilka informationstillgångar på de högsta nivåerna som saknar dokumenterad nationell drift eller EU-drift. |
| s.6280a2b4d6 | A way to tell an offer’s server location from its jurisdiction: the indicators ask about law and control, not region. | Ett sätt att skilja ett erbjudandes serverplacering från dess jurisdiktion: indikatorerna frågar om lag och kontroll, inte om region. |
| s.637ed308e2 | A “top ten priority holdings” view per country. | En bild av de ”tio högst prioriterade informationstillgångarna” per land. |
| s.add10c7564 | An audit of a digitalisation programme. | En revision av ett digitaliseringsprogram. |
| s.0273336afa | An award criterion is easier to defend when it can be cited. The ranking’s indicators are precise questions about jurisdiction, certification and control, answered state by state with the legal text quoted. | Ett tilldelningskriterium är lättare att försvara när det går att hänvisa till. Rangordningens indikatorer är precisa frågor om jurisdiktion, certifiering och kontroll, besvarade stat för stat med lagtexten citerad. |
| s.9542e80c0f | An export that drafts each gap as a written question. | En export som formulerar varje lucka som en skriftlig fråga. |
| s.51a35d7d82 | An order of work you can explain: the priority score is published, and so is each of its inputs. | En arbetsordning du kan förklara: prioritetspoängen är publicerad, och det är var och en av dess indata också. |
| s.cf94bdf391 | Ask a question | Ställ en fråga |
| s.b8e3b8bd5e | Ask in your own words | Fråga med egna ord |
| s.bbc5010fac | Browse the holding classes | Bläddra bland klasserna av informationstillgångar |
| s.3aeffd96e7 | Budget scrutiny of IT spending. | Budgetgranskning av it-utgifter. |
| s.5b1841d68f | Check a claim at its source | Kontrollera ett påstående vid källan |
| s.1478731d37 | Check my country’s<br>exposure | Kontrollera mitt lands<br>exponering |
| s.bae3748df9 | Check my country’s exposure | Kontrollera mitt lands exponering |
| s.24ebc43ac7 | Check the trust anchor and the eID | Kontrollera tillitsankaret och eID:n |
| s.079984afeb | Checking a claim before publishing it. | Kontroll av ett påstående före publicering. |
| s.7843c8c20c | Choose a country | Välj ett land |
| s.24699e1898 | Choose your country | Välj ditt land |
| s.c8e71a0183 | Cite the source when a fact is contested | Hänvisa till källan när en uppgift bestrids |
| s.c79b67e3d8 | Civil registry, tax, land registry, health records and the rest, grouped by tier. | Befolkningsregister, skatt, fastighetsregister, patientjournaler och resten, grupperade efter nivå. |
| s.ef46c30d85 | Compare a holding | Jämför en informationstillgång |
| s.ede777d505 | Compare how peers<br>host a register | Jämför hur jämförbara stater<br>driftar ett register |
| s.5db4b0b098 | Compare how peers host a register | Jämför hur jämförbara stater driftar ett register |
| s.729edbd662 | Compare with peer states | Jämför med jämförbara stater |
| s.ad6f8b62f4 | Copy-ready tender clauses mapped to the indicators. | Upphandlingsklausuler klara att kopiera, kopplade till indikatorerna. |
| s.18c3611eba | Crisis-scenario planning: what happens if a provider is ordered to suspend service. | Planering av krisscenarier: vad som händer om en leverantör beordras att stänga av tjänsten. |
| s.e54c52fb78 | Criteria you can cite rather than invent. | Kriterier du kan hänvisa till i stället för att hitta på. |
| s.fd8eddd9c9 | Cyber agencies<br>& CISOs | Cybersäkerhetsmyndigheter<br>och CISO:er |
| s.cfff8d648e | Decide what to<br>migrate first | Bestäm vad som ska<br>migreras först |
| s.f691d5706f | Decide what to migrate first | Bestäm vad som ska migreras först |
| s.e675b97615 | Designing funding programmes for sovereign infrastructure. | Utformning av finansieringsprogram för suverän infrastruktur. |
| s.8f848ebe67 | Drafting or amending cloud, cybersecurity or data legislation. | Utarbetande eller ändring av lagstiftning om moln, cybersäkerhet eller data. |
| s.ce357a47b0 | EU institutions | EU-institutioner |
| s.10b1e5e62e | Each cell in a comparison is taken from that state’s own report, with the same source. | Varje cell i en jämförelse hämtas från den statens egen rapport, med samma källa. |
| s.a4725b67be | Each fact rests on a quoted passage from a hashed, archived document. | Varje uppgift vilar på ett citerat stycke ur ett hashat, arkiverat dokument. |
| s.df7a559160 | Each finding carries a footnote to its source: the statute or scheme, quoted in the original language. | Varje iakttagelse har en fotnot till sin källa: lagen eller systemet, citerad på originalspråket. |
| s.7926c21254 | Each report lists its holdings by a published score: consequence of loss, difficulty of rebuilding and known exposure to non-EU providers. | Varje rapport listar sina informationstillgångar efter en publicerad poäng: konsekvens vid förlust, svårighet att återuppbygga och känd exponering för leverantörer utanför EU. |
| s.3e33af3204 | Each report lists its holdings from the highest priority down, with what a source says about each. | Varje rapport listar sina informationstillgångar från högsta prioritet och nedåt, med vad en källa säger om var och en. |
| s.f245ee9452 | Each report ranks its holdings by a score that counts difficulty of rebuilding. | Varje rapport rangordnar sina informationstillgångar efter en poäng som räknar med svårigheten att återuppbygga. |
| s.9423bc8d6d | Each source is listed with its quote in the original language, a document hash and an archived copy. | Varje källa listas med sitt citat på originalspråket, ett hashvärde för dokumentet och en arkiverad kopia. |
| s.a1d971de10 | Every country has its own report as a PDF, with footnoted sources and a source appendix. | Varje land har en egen rapport som PDF, med källor i fotnoter och en källbilaga. |
| s.3e344387ad | Every holding whose hosting a source states, by member state, with the operator and the dependency. | Varje informationstillgång vars drift en källa anger, per medlemsstat, med operatören och beroendet. |
| s.018ce99e27 | Every printed fact was checked by a second model, and the verdicts are published. | Varje visad uppgift kontrollerades av en andra modell, och utlåtandena är publicerade. |
| s.4f908f7674 | Every value no checked source supports is listed as open research. Each can be put as a written question: will the government publish a source stating where this register is hosted? | Varje värde som ingen kontrollerad källa stöder listas som öppen forskningsfråga. Vart och ett kan ställas som en skriftlig fråga: kommer regeringen att publicera en källa som anger var detta register driftas? |
| s.52bd599c58 | Every value that no checked source supports is shown as a gap, and every value the fact check could not confirm is shown as disputed. Each is a question a government can answer by publishing a source. | Varje värde som ingen kontrollerad källa stöder visas som en lucka, och varje värde som faktagranskningen inte kunde bekräfta visas som omtvistat. Vart och ett är en fråga som en regering kan besvara genom att publicera en källa. |
| s.f0f233b509 | Evidence, indicator by indicator, of how far member states have documented each safeguard on their own. | Belägg, indikator för indikator, för hur långt medlemsstaterna på egen hand har dokumenterat varje skyddsåtgärd. |
| s.f013b5417d | Facts you can report from: quoted in the original language, hashed and archived. | Uppgifter du kan rapportera utifrån: citerade på originalspråket, hashade och arkiverade. |
| s.c5a8b8e80a | Filter hosting by dependency | Filtrera drift efter beroende |
| s.d4765d94d3 | Find a member state that has published a source for the same holding. | Hitta en medlemsstat som har publicerat en källa för samma informationstillgång. |
| s.1eff5035e1 | Find the gaps in your country’s report | Hitta luckorna i ditt lands rapport |
| s.5f0ebc535d | Find your country’s PDF | Hitta ditt lands PDF |
| s.fee06e6365 | Following a procurement story. | Uppföljning av en nyhet om en upphandling. |
| s.cda5fb4760 | For EU institutions | För EU-institutioner |
| s.993257fb5e | For any holding class, read how the other member states host it. | Välj vilken klass av informationstillgångar som helst och läs hur de andra medlemsstaterna driftar den. |
| s.17c9476d46 | For digital ministries and government CIOs | För digitaliseringsministerier och statliga it-chefer |
| s.12bec467e7 | For each kind of holding, read each state’s register and its operator side by side. | Läs, för varje slag av informationstillgång, varje stats register och dess operatör sida vid sida. |
| s.cc6ed4fb32 | For national cyber agencies and CISOs | För nationella cybersäkerhetsmyndigheter och CISO:er |
| s.3d0b3240e0 | For operators, investors and the press | För operatörer, investerare och pressen |
| s.b9a5fcd7ef | For parliaments, audit courts and data-protection authorities | För parlament, revisionsorgan och dataskyddsmyndigheter |
| s.765bf1c1cf | For procurement and cloud-strategy leads | För ansvariga för upphandling och molnstrategi |
| s.c637f2f828 | For sovereign cloud and data-centre operators and their investors, the gaps show where documented national or EU hosting is missing. For journalists and NGOs, every claim links to a quote and an archived copy, so it can be reported from. | För operatörer av suveräna moln och datacenter och deras investerare visar luckorna var dokumenterad nationell drift eller EU-drift saknas. För journalister och ideella organisationer länkar varje påstående till ett citat och en arkiverad kopia, så att det går att rapportera utifrån det. |
| s.9bdc1b8a5a | Hover over a column heading for the exact question each indicator asks. | Håll pekaren över en kolumnrubrik för att se exakt vilken fråga varje indikator ställer. |
| s.3857c8a6eb | Identity, tax, justice, grid control, emergency calls: the holding classes span the sectors an all-hazards assessment covers. | Identitet, skatt, rättsväsende, styrning av elnätet, nödsamtal: klasserna av informationstillgångar spänner över de sektorer som en bedömning av alla hot och risker täcker. |
| s.2d30c6a60a | Its report opens at the exposure table, which counts verified holdings by where their source says the infrastructure runs. | Dess rapport öppnas vid exponeringstabellen, som räknar verifierade informationstillgångar efter var deras källa säger att infrastrukturen drivs. |
| s.38e0d36aeb | Its report opens at “Research still open”: the list of what no checked source yet states. | Dess rapport öppnas vid ”Öppna forskningsfrågor”: listan över vad ingen kontrollerad källa ännu anger. |
| s.d04bdc28e4 | List what is hard to rebuild | Lista det som är svårt att återuppbygga |
| s.1776b85ee1 | List what would be hard to rebuild | Lista det som skulle vara svårt att återuppbygga |
| s.9970ff42f7 | Ministries &<br>government CIOs | Ministerier och<br>statliga it-chefer |
| s.3e1e5f805b | NIS2 implementation. | Genomförande av NIS2. |
| s.c9c4eac440 | One taxonomy, 27 member states. Pick a kind of holding and read, side by side, each state’s register, its operator and where a source says it runs. | En taxonomi, 27 medlemsstater. Välj ett slag av informationstillgång och läs, sida vid sida, varje stats register, dess operatör och var en källa säger att det drivs. |
| s.e9c8b2ea10 | Only holdings whose source says where the infrastructure runs are counted. Silence is “not stated”. | Bara informationstillgångar vars källa säger var infrastrukturen drivs räknas. Tystnad är ”inte angivet”. |
| s.fe2ef59507 | Open a report at its gaps | Öppna en rapport vid dess luckor |
| s.1dff3d34f6 | Open a report at its holdings | Öppna en rapport vid dess informationstillgångar |
| s.31dfb891c1 | Open a state’s full report | Öppna en stats fullständiga rapport |
| s.00b62aa8d7 | Open hosting | Öppna driftöversikten |
| s.7113ac8ce1 | Open the EU-27 report (PDF) | Öppna EU-27-rapporten (PDF) |
| s.f721b214f5 | Open the fact check | Öppna faktagranskningen |
| s.888e3804fd | Open the holdings behind a count | Öppna informationstillgångarna som en siffra bygger på |
| s.8ae15f6ce9 | Open the indicators | Öppna indikatorerna |
| s.b432ab8cbc | Open the legal text behind a “Yes” | Öppna lagtexten som ett ”Ja” bygger på |
| s.546d4ca1d4 | Open the ranking | Öppna rangordningen |
| s.e1cb96c8fc | Open your country report | Öppna din landrapport |
| s.cbf1967539 | Open your country’s holdings by priority | Öppna ditt lands informationstillgångar efter prioritet |
| s.30649e713e | Operators<br>investors & press | Operatörer,<br>investerare och press |
| s.eaff3ef7f6 | Oversight needs visibility. It is hard to ask a precise question about where a register is hosted when nothing public says where it is. Here every missing source is shown as a gap, so the question writes itself. | Tillsyn kräver insyn. Det är svårt att ställa en precis fråga om var ett register driftas när ingenting offentligt säger var det finns. Här visas varje saknad källa som en lucka, så att frågan skriver sig själv. |
| s.73a6bc853d | Parliaments &<br>audit courts | Parlament och<br>revisionsorgan |
| s.b076a852a1 | Peer evidence: what other states have documented for the same holding. | Belägg från jämförbara stater: vad andra stater har dokumenterat för samma informationstillgång. |
| s.88ff1bcc44 | Pick a holding class | Välj en klass av informationstillgångar |
| s.479d113628 | Pick one kind of holding and read it across all 27 member states. | Välj ett slag av informationstillgång och läs om det i alla 27 medlemsstater. |
| s.5086222ca9 | Plan for a<br>provider cut-off | Gör en beredskapsplan<br>för ett leverantörsavbrott |
| s.6a45998a0f | Plan for a provider cut-off | Gör en beredskapsplan för ett leverantörsavbrott |
| s.04db7e08ad | Precedents: how other member states host the same register, in the words of their own sources. | Förebilder: hur andra medlemsstater driftar samma register, med deras egna källors ord. |
| s.d5cdd44c91 | Procurement &<br>cloud strategy | Upphandling och<br>molnstrategi |
| s.b5e253d8db | Questions grounded in sources rather than speculation. | Frågor grundade på källor snarare än spekulation. |
| s.2d996f403f | Read all 27 in one document | Läs alla 27 i ett dokument |
| s.46cd281992 | Read how exposure is counted | Läs hur exponering räknas |
| s.38609176e5 | Read the grid | Läs indikatortabellen |
| s.d14acd3ca5 | Read the holdings in priority order | Läs informationstillgångarna i prioritetsordning |
| s.55350ab3c9 | Read the hosting overview | Läs driftöversikten |
| s.b1afc6047f | Read the indicator definitions | Läs indikatordefinitionerna |
| s.2a67691862 | Read the indicator distribution | Läs indikatorernas fördelning |
| s.83c5b8f8e3 | Read the methodology | Läs metoden |
| s.1c840c98c3 | Read the priority rule | Läs prioritetsregeln |
| s.c50b2008be | Read the rule | Läs regeln |
| s.0a56eb289b | Read the seven indicators | Läs de sju indikatorerna |
| s.40220b1e7e | Read what is documented next to the gap | Läs vad som är dokumenterat intill luckan |
| s.0f57612582 | Read your state’s placement | Läs din stats placering |
| s.d2a21b33df | Reproduce it | Reproducera det |
| s.f4a9d8a2ef | Review by a person. Every finding here is machine-checked only, which limits how it can be cited in formal documents. | Mänsklig granskning. Varje iakttagelse här är enbart maskinkontrollerad, vilket begränsar hur den kan citeras i formella dokument. |
| s.89a0f5386c | Revisiting the EU cloud certification scheme. | Översyn av EU:s system för molncertifiering. |
| s.73c9bdb1ef | Search by publisher, country or quoted text. Each entry carries the quote, a document hash and an archived copy. | Sök efter utgivare, land eller citerad text. Varje post har citatet, ett hashvärde för dokumentet och en arkiverad kopia. |
| s.5b3c690d76 | Search the sources | Sök i källorna |
| s.5cc022ab85 | See how each fact was checked | Se hur varje uppgift kontrollerades |
| s.7db4df96f9 | See how other states host the same register | Se hur andra stater driftar samma register |
| s.c83eec427b | See how peers host the top items | Se hur jämförbara stater driftar de högst prioriterade posterna |
| s.4eb6cd0604 | See what a source says about hosting | Se vad en källa säger om driften |
| s.24f9f480cb | See what other member states have documented for the same holding. | Se vad andra medlemsstater har dokumenterat för samma informationstillgång. |
| s.429dd2de76 | See what other states have put in law | Se vad andra stater har skrivit in i lag |
| s.46d0f63826 | See where hosting is undocumented | Se var driften är odokumenterad |
| s.f4d49c2a2f | See which holding classes have a checked source, which have documented hosting and which are gaps. | Se vilka klasser av informationstillgångar som har en kontrollerad källa, vilka som har dokumenterad drift och vilka som är luckor. |
| s.5121a5fdfe | See which operators peers chose | Se vilka operatörer jämförbara stater valde |
| s.18af0127b4 | See which operators peers use | Se vilka operatörer jämförbara stater använder |
| s.854aa62c7e | See who operates what | Se vem som driver vad |
| s.da2b128db7 | Seven indicators, each a precise question: a jurisdiction requirement, a certification that requires immunity from non-EU law, a state-controlled trust anchor and eID, among others. | Sju indikatorer, var och en en precis fråga: bland annat ett krav på jurisdiktion, en certifiering som kräver immunitet mot lagstiftning utanför EU, och ett statligt kontrollerat tillitsankare och en statligt kontrollerad eID. |
| s.128230821c | Show that the gap can be closed | Visa att luckan kan täppas till |
| s.bc69ac2068 | Sizing demand for sovereign hosting. | Bedömning av efterfrågan på suverän drift. |
| s.6fb27e7fbd | Take in the whole scope | Överblicka hela omfattningen |
| s.4eb735bb3f | Take the country PDF into a briefing | Ta med landets PDF till en genomgång |
| s.111fb20b29 | The Ask box answers only from the sourced findings, with a citation for every fact. | Fråga-rutan svarar enbart utifrån iakttagelserna med källa, med en källhänvisning för varje uppgift. |
| s.a93f1c11f6 | The EU-27 report has a chapter per member state, with footnoted sources and a source appendix. | EU-27-rapporten har ett kapitel per medlemsstat, med källor i fotnoter och en källbilaga. |
| s.86a78e54b8 | The data and the code are open. The methodology says how every number is counted and how to rebuild every output. | Data och kod är öppna. Metoden säger hur varje tal räknas och hur varje utdata byggs om. |
| s.2181d0e7e8 | The grid shows, for each legal and practical safeguard, how many states have it sourced. | Tabellen visar, för varje rättslig och praktisk skyddsåtgärd, hur många stater som har den med källa. |
| s.ac1d33ad53 | The holding classes and their tiers are the same for every state: a candidate common taxonomy. | Klasserna av informationstillgångar och deras nivåer är desamma för varje stat: ett förslag till gemensam taxonomi. |
| s.9fa755d8c3 | The holdings table names each register, its operator and its hosting, each with its footnote. | Tabellen över informationstillgångar namnger varje register, dess operatör och dess drift, vart och ett med sin fotnot. |
| s.31003ae899 | The holdings table shows the gap in context: the register may be sourced while its hosting is not. | Tabellen över informationstillgångar visar luckan i sitt sammanhang: registret kan ha källa medan driften saknar det. |
| s.727009e62c | The hosting overview lists every holding whose hosting a source states. What is not listed has no sourced hosting yet. | Driftöversikten listar varje informationstillgång vars drift en källa anger. Det som inte listas har ännu ingen drift med källa. |
| s.aea2d84e37 | The hosting overview names operators and hosting for comparable holdings. | Driftöversikten namnger operatörer och drift för jämförbara informationstillgångar. |
| s.e4edd0f7f7 | The hosting overview names the operator and the hosting a source states for comparable holdings. | Driftöversikten namnger den operatör och den drift som en källa anger för jämförbara informationstillgångar. |
| s.97e71dbf49 | The hosting overview shows which holdings are documented on national infrastructure, with an EU provider or on mixed hosting, and which have no stated hosting. | Driftöversikten visar vilka informationstillgångar som är dokumenterade på nationell infrastruktur, hos en EU-leverantör eller med blandad drift, och vilka som saknar angiven drift. |
| s.3881a07877 | The priority score counts difficulty of rebuilding. Holdings that rank high with hosting not stated make a ready scenario list. | Prioritetspoängen räknar med svårigheten att återuppbygga. Informationstillgångar som rankas högt och vars drift inte är angiven utgör en färdig scenariolista. |
| s.e3543005ce | The ranking places each state in a group by a published rule, and says how far open evidence could still move it. | Rangordningen placerar varje stat i en grupp enligt en publicerad regel och anger hur långt belägg som ännu inte är avgjorda fortfarande skulle kunna flytta den. |
| s.ce857fdb6d | The same grid shows, state by state, which indicators a checked source supports, with the legal text quoted. | Samma tabell visar, stat för stat, vilka indikatorer en kontrollerad källa stöder, med lagtexten citerad. |
| s.4f0e8a73c5 | The score adds three inputs: consequence of loss, difficulty of rebuilding and known exposure to non-EU providers. | Poängen lägger ihop tre indata: konsekvens vid förlust, svårighet att återuppbygga och känd exponering för leverantörer utanför EU. |
| s.7d997eb840 | The site does not tell a state what to do. It does publish a priority score for every holding, and each input to it, so an order of work can be argued from evidence. | Webbplatsen talar inte om för en stat vad den ska göra. Den publicerar däremot en prioritetspoäng för varje informationstillgång, och varje indata till den, så att en arbetsordning kan motiveras utifrån belägg. |
| s.31b0694684 | Trace a criterion to its source | Följ ett kriterium till dess källa |
| s.f7da6b0da5 | Turn gaps into<br>formal questions | Gör luckor till<br>formella frågor |
| s.f004c2e1a5 | Turn gaps into formal questions | Gör luckor till formella frågor |
| s.3e17caa890 | Twenty-seven national pictures that do not line up, and no shared taxonomy for “critical government data”. This site puts all 27 member states on one footing: the same holding classes, the same indicators, the same rule for what counts as evidence. | Tjugosju nationella bilder som inte stämmer överens, och ingen gemensam taxonomi för ”kritiska offentliga data”. Denna webbplats ställer alla 27 medlemsstater på samma grund: samma klasser av informationstillgångar, samma indikatorer, samma regel för vad som räknas som belägg. |
| s.7289dc9a3c | Two indicators ask whether the state controls its trust anchor and its national eID. | Två indikatorer frågar om staten kontrollerar sitt tillitsankare och sin nationella eID. |
| s.ad28038a5a | Two indicators ask whether the state controls its trust anchor and its national eID. Digital services downstream depend on both. | Två indikatorer frågar om staten kontrollerar sitt tillitsankare och sin nationella eID. Digitala tjänster i nästa led är beroende av båda. |
| s.bea0a2b11e | Use the cards above the list to show one kind of dependency, and the tier filter to keep to the top tiers. | Använd korten ovanför listan för att visa ett slag av beroende, och nivåfiltret för att hålla dig till de högsta nivåerna. |
| s.ada9707155 | Use the taxonomy | Använd taxonomin |
| s.988e1121a7 | What happens if a provider is ordered to suspend service? The hosting overview shows which holdings a source places on national infrastructure, with an EU provider or on mixed hosting, and which have no stated hosting at all. | Vad händer om en leverantör beordras att stänga av tjänsten? Driftöversikten visar vilka informationstillgångar en källa placerar på nationell infrastruktur, hos en EU-leverantör eller med blandad drift, och vilka som helt saknar angiven drift. |
| s.b1449815d6 | Write tender criteria<br>that hold up | Skriv upphandlingskriterier<br>som håller |
| s.253c555f4a | Write tender criteria that hold up | Skriv upphandlingskriterier som håller |
| s.2c56ec23a3 | You are asked to act on sovereignty without a baseline. Inventories sit in different ministries, and it is hard to say quickly what runs where. This site is an outside baseline: what a checked public source says about each of your state’s critical holdings, and where no source has been found. | Du förväntas agera i fråga om suveränitet utan någon utgångspunkt. Förteckningarna finns hos olika ministerier, och det är svårt att snabbt säga vad som drivs var. Denna webbplats är en extern utgångspunkt: vad en kontrollerad offentlig källa säger om var och en av din stats kritiska informationstillgångar, och var ingen källa har hittats. |
| s.1db035c98e | You are drafting tender specifications. | Du tar fram upphandlingsspecifikationer. |
| s.aa34ceb9e3 | You are evaluating bids. | Du utvärderar anbud. |
| s.05b94e02ba | You are responsible for resilience, often without a view of where critical registers sit, physically and legally. A threat model built for technical attacks may not cover a provider being ordered to suspend service. | Du ansvarar för motståndskraft, ofta utan överblick över var kritiska register finns, fysiskt och rättsligt. En hotmodell byggd för tekniska angrepp täcker kanske inte att en leverantör beordras att stänga av tjänsten. |
| s.11f7a3da3a | Your country’s report shows, for each critical holding, whether a checked source says where it runs: on national infrastructure, with an EU provider, on mixed hosting, or not stated. Silence counts as not stated, never as national. | Ditt lands rapport visar, för varje kritisk informationstillgång, om en kontrollerad källa säger var den drivs: på nationell infrastruktur, hos en EU-leverantör, med blandad drift eller inte angivet. Tystnad räknas som inte angivet, aldrig som nationell. |
| s.a16a4eda7c | Answer | Svar |
| s.fcbea7aab2 | Answering… | Svarar… |
| s.f2bd2a657e | Answers come only from this project’s sourced findings, with a citation for every fact. When the findings don’t cover a question, the answer says so. | Svaren kommer enbart från detta projekts iakttagelser med källa, med en källhänvisning för varje uppgift. När iakttagelserna inte täcker en fråga säger svaret det. |
| s.3562777bc6 | Ask | Fråga |
| s.588900c714 | Ask about a member state, a holding or the ranking | Fråga om en medlemsstat, en informationstillgång eller rangordningen |
| s.3f3a83bcc6 | Ask about data sovereignty in the EU | Fråga om datasuveränitet i EU |
| s.12e1b0f401 | Could not reach the answering service. Please try again. | Svarstjänsten kunde inte nås. Försök igen. |
| s.9003825bdf | EU-27 · Ask | EU-27 · Fråga |
| s.e4ec528b79 | Example questions | Exempelfrågor |
| s.ed1aec3980 | Reading the sourced findings… | Läser iakttagelserna med källa… |
| s.bee54c9cc3 | Something went wrong. | Något gick fel. |
| s.9a3ea0598e | Something went wrong. Please try again. | Något gick fel. Försök igen. |
| s.b947003d5c | Source {n} | Källa {n} |
| s.e08050d888 | This question could not be answered. Please rephrase it. | Frågan kunde inte besvaras. Formulera om den. |
| s.8bdca003cc | Too many questions from here right now. Please try again later. | För många frågor härifrån just nu. Försök igen senare. |
| s.72677028b4 | Try | Prova |
| s.0ba83cb8e8 | Your question | Din fråga |
| s.c8640fb95c | Your question is sent to Anthropic’s API to generate the answer. This site does not store it. Answers may be incomplete: they reflect only what has been verified so far. | Din fråga skickas till Anthropics API för att generera svaret. Denna webbplats lagrar den inte. Svaren kan vara ofullständiga: de speglar bara det som hittills har verifierats. |
| s.a11a9ee218 | Choose a member state to open its report at “{section}”. | Välj en medlemsstat för att öppna dess rapport vid ”{section}”. |
| s.8467c0d99c | Countries | Länder |
| s.50f704f3bf | EU-27 · Member states | EU-27 · Medlemsstater |
| s.57ddfe0efd | Each member state analysed on its own fundamentals. The cards count verified evidence; they are not a ranking of how sovereign a state is. | Varje medlemsstat analyserad utifrån sina egna grunduppgifter. Korten räknar verifierade belägg; de är inte en rangordning av hur suverän en stat är. |
| s.bec93ba893 | Find a country | Hitta ett land |
| s.29340e604c | Holdings verified | Informationstillgångar verifierade |
| s.34bf7b2eb8 | No member state matches that name. | Ingen medlemsstat matchar det namnet. |
| s.911fbc0f5a | Nothing withheld as disputed | Inget undanhållet som omtvistat |
| s.a2a5bdeca9 | Sort by | Sortera efter |
| s.4eb408e1b5 | Sourced facts | Uppgifter med källa |
| s.7ee0b56b76 | Tier 0 verified | Nivå 0 verifierad |
| s.b2c01838bc | holdings with a verified source | informationstillgångar med en verifierad källa |
| s.edfc76939f | {n} of {total} tier 0 holdings verified | {n} av {total} informationstillgångar på nivå 0 verifierade |
| s.3da100fd5b | {n} withheld as disputed | {n, plural, one {# undanhållen som omtvistad} other {# undanhållna som omtvistade}} |
| s.0b3bc63de0 | Download the {name} report (PDF) | Ladda ned rapporten för {name} (PDF) |
| s.ba7661f435 | Every fact also has a {label} link in its source entry. | Varje uppgift har också en ”{label}”-länk i sin källpost. |
| s.6338f7ec43 | How each fact above was checked by a second model, the one that did not write it: {link}. | Hur varje uppgift ovan kontrollerades av en andra modell, den som inte skrev den: {link}. |
| s.93d2f80ef7 | Submissions are checked by machine and then by a different person who reads the language ({link}). | Inlämningar kontrolleras maskinellt och därefter av en annan person som läser språket ({link}). |
| s.60e6d488a8 | Submit a source | Lämna in en källa |
| s.088fc2bb86 | capacity not yet sized | kapaciteten ännu inte dimensionerad |
| s.87abd9beab | fact check for {name} | faktagranskning för {name} |
| s.5e705951b3 | methodology | metod |
| s.32ea9a3579 | {n, plural, one {# sourced fact shown} other {# sourced facts shown}} | {n, plural, one {# uppgift med källa visas} other {# uppgifter med källa visas}} |
| s.f9b095cf90 | {n, plural, one {Know a public source for the withheld value, or a better one for a fact?} other {Know a public source for one of the # withheld values, or a better one for a fact?}} | {n, plural, =0 {Känner du till en bättre offentlig källa för någon uppgift?} one {Känner du till en offentlig källa för det undanhållna värdet, eller en bättre källa för någon uppgift?} other {Känner du till en offentlig källa för något av de # undanhållna värdena, eller en bättre källa för någon uppgift?}} |
| s.59a9dfcb7b | {verified} of {total} critical holding classes verified | {verified} av {total} kritiska klasser av informationstillgångar verifierade |
| s.5233d9d9bc | Back to {name} | Tillbaka till {name} |
| s.13e63611d5 | Fact check | Faktagranskning |
| s.3c558d8e40 | Fact check: {name} | Faktagranskning: {name} |
| s.66d69ab480 | No fact-check appendix for {iso}. | Ingen faktagranskningsbilaga för {iso}. |
| s.b2232452b5 | Check it{label} | Kontrollera{label} |
| s.9732ee3c8c | Counted from the published dataset as this page loads. Each figure links to the page where it can be checked. | Räknat från den publicerade datamängden när denna sida läses in. Varje siffra länkar till den sida där den kan kontrolleras. |
| s.08ca30a8e2 | EU-27 · I am… | EU-27 · Jag är… |
| s.f2e8958b8a | EU-27 · I need to… | EU-27 · Jag behöver… |
| s.c535a55f4c | From the data today | Ur uppgifterna i dag |
| s.2cb5e47964 | How to do it on this site | Så gör du det på denna webbplats |
| s.2210d472bf | Not here yet | Finns inte här ännu |
| s.059589ec92 | On this site, today | På denna webbplats, i dag |
| s.8312889825 | Readers who need this | Läsare som behöver detta |
| s.0f51795253 | Start with a task | Börja med en arbetsuppgift |
| s.c16dfd1733 | Step by step | Steg för steg |
| s.fc5a046860 | Tasks for this reader | Arbetsuppgifter för denna läsare |
| s.7c563fab97 | What the site does not do | Vad webbplatsen inte gör |
| s.5ad1c01297 | What this gives you | Vad detta ger dig |
| s.facf040ca4 | What you can do here | Vad du kan göra här |
| s.c65c8aee5a | What you take away | Vad du tar med dig |
| s.12ceb0ea2f | When this helps | När detta hjälper |
| s.ef3c791627 | Where the evidence stands | Beläggens läge |
| s.b5b404d6c1 | Written for | Skriven för |
| s.04226ffebd | You are here because | Du är här därför att |
| s.08cbf6a3a2 | All domains | Alla områden |
| s.0023b8ecba | Critical holdings | Kritiska informationstillgångar |
| s.9b10914d8b | Domain | Område |
| s.290d3b83ca | EU-27 · Critical holding | EU-27 · Kritisk informationstillgång |
| s.a9617bf1d2 | EU-27 · Critical holdings | EU-27 · Kritiska informationstillgångar |
| s.8d6c70fc9b | Faded bars: fewer than half the member states verified. A gap means not yet sourced, never that the holding does not exist. | Bleka staplar: färre än hälften av medlemsstaterna verifierade. En lucka betyder ännu utan källa, aldrig att informationstillgången inte finns. |
| s.5c0ec459d6 | Filter by domain | Filtrera efter område |
| s.8661d7d53e | Geospatial base data, digital archives | Geografiska grunddata, digitala arkiv |
| s.6a64b56ba0 | Health records, public health, statistics | Patientjournaler, folkhälsa, statistik |
| s.1df1955d61 | Holding | Informationstillgång |
| s.3902a2b7c3 | Holdings by tier | Informationstillgångar efter nivå |
| s.13df1314af | States verified | Stater verifierade |
| s.01916f8bc6 | The identity spine: civil registry, biometrics, eID, PKI | Identitetens ryggrad: befolkningsregister, biometri, eID, PKI |
| s.8ee8479c84 | The legal, fiscal and security state | Den rättsliga, fiskala och säkerhetsmässiga staten |
| s.4d8b6f0aaa | The {n} kinds of government data holding this project inventories, in tier order: tier 0 is the identity spine, tier 1 the legal, fiscal and security state. Open one to compare it across all 27 member states. | De {n} slag av offentliga informationstillgångar som detta projekt inventerar, i nivåordning: nivå 0 är identitetens ryggrad, nivå 1 den rättsliga, fiskala och säkerhetsmässiga staten. Öppna ett för att jämföra det mellan alla 27 medlemsstater. |
| s.a2c6bfc5eb | tier {t} | nivå {t} |
| s.19ef957b3d | EU-27 report | EU-27-rapporten |
| s.21ce9bdc8a | EU-27 · Key infrastructure | EU-27 · Central infrastruktur |
| s.0173c1185c | The same overview is in the {report}; each holding in full is on its {page}. | Samma översikt finns i {report}; varje informationstillgång i sin helhet finns på dess {page}. |
| s.8f8284b6b9 | country page | landssida |
| s.b72e0d077f | hosting facts printed | visade driftuppgifter |
| s.e1e7baf404 | withheld as disputed | undanhållna som omtvistade |
| s.b509d96b12 | Methodology | Metod |
| s.933fc9cce0 | 27 states × {n, plural, one {# class} other {# classes}} | 27 stater × {n, plural, one {# klass} other {# klasser}} |
| s.dae3acc17d | A country chapter: Germany | Ett landkapitel: Tyskland |
| s.56b3945e3a | All 27 member states, sortable, each with its own report and footnoted sources. | Alla 27 medlemsstater, sorterbara, var och en med egen rapport och källor i fotnoter. |
| s.aa7ef6a9ca | Ask any question | Ställ vilken fråga som helst |
| s.b124f047fe | Ask anything, in your own words… | Fråga vad som helst, med egna ord… |
| s.816afa09f1 | Browse countries | Bläddra bland länder |
| s.dc144542ae | Compare holdings | Jämför informationstillgångar |
| s.afd734c0c3 | Countries sized | Länder dimensionerade |
| s.8b656a5dd9 | Cover | Omslag |
| s.384dcfc951 | Critical holdings verified | Kritiska informationstillgångar verifierade |
| s.e5130af021 | Data-sovereignty ranking | Rangordning efter datasuveränitet |
| s.9d35a1e8b1 | EU-27 report (PDF) | EU-27-rapporten (PDF) |
| s.4be913ff63 | Each member state analysed on its own fundamentals: the critical data holdings it cannot let depend on infrastructure a foreign state can compel or switch off, who operates them, under which law, and where they run. Every fact is footnoted to its source; where no checked source has been found yet, the value is withheld and the gap is shown. | Varje medlemsstat analyserad utifrån sina egna grunduppgifter: de kritiska informationstillgångar den inte kan låta vara beroende av infrastruktur som en främmande stat kan utöva tvång mot eller stänga av, vem som driver dem, enligt vilken lag, och var de drivs. Varje uppgift har en fotnot till sin källa; där ingen kontrollerad källa ännu har hittats undanhålls värdet och luckan visas. |
| s.e3a34f794f | Every checked source, with the quoted passage and each claim it supports. | Varje kontrollerad källa, med det citerade stycket och varje påstående den stöder. |
| s.7d70fca297 | Every fact is footnoted. Where no checked source exists yet, the value is withheld and the gap stays visible. | Varje uppgift har en fotnot. Där ingen kontrollerad källa ännu finns undanhålls värdet och luckan förblir synlig. |
| s.5bfab1e2af | Every member state in one document, with a table of contents, footnoted sources and a source appendix. Each country is also available as its own PDF. | Varje medlemsstat i ett dokument, med innehållsförteckning, källor i fotnoter och en källbilaga. Varje land finns också som egen PDF. |
| s.81cca36896 | Hello, Europe | Hej, Europa |
| s.7c45e96e58 | Methodology appendix | Metodbilaga |
| s.a89a395a9c | One kind of holding, such as tax, health or land records, compared across every member state. | Ett slag av informationstillgång, till exempel skatt, hälsa eller fastighetsregister, jämfört mellan alla medlemsstater. |
| s.7cd5e5df45 | Or start from one of these | Eller börja med någon av dessa |
| s.f623f6f706 | Page from the EU-27 report: {caption} | Sida ur EU-27-rapporten: {caption} |
| s.1be38688bb | Pages from the EU-27 report | Sidor ur EU-27-rapporten |
| s.8289ec6739 | Sizing needs measured holdings | Dimensionering kräver uppmätta informationstillgångar |
| s.4d2464a036 | Sourced claims | Påståenden med källa |
| s.841efde86d | Start where your question is | Börja där din fråga finns |
| s.052bc43f37 | State of the evidence | Beläggens läge |
| s.2868ce33aa | The fact check | Faktagranskningen |
| s.fb80efb9ec | The full report | Den fullständiga rapporten |
| s.ac9aab6fea | The identity spine every state runs on | Identitetens ryggrad som varje stat vilar på |
| s.e8ca289b11 | The state of the evidence | Beläggens läge |
| s.ab08a795f2 | Three ways in | Tre vägar in |
| s.2bb9ad51b3 | Tier 0 holdings verified | Informationstillgångar på nivå 0 verifierade |
| s.09394824be | Trace sources | Följ källorna |
| s.65eb2b971d | Waiting on measured holdings | Väntar på uppmätta informationstillgångar |
| s.3326258239 | Whatever is on your mind about EU Data Sovereignty, ask any question here. | Vad du än undrar om datasuveränitet i EU kan du ställa vilken fråga som helst här. |
| s.4b63a71f07 | Where registers are hosted | Var registren driftas |
| s.38377c29fc | Where the research stands | Forskningens läge |
| s.0a4713ee3a | Your question is sent to Anthropic’s API to generate the answer. This site does not store it. Answers come only from this project’s sourced findings, with a citation for every fact. | Din fråga skickas till Anthropics API för att generera svaret. Denna webbplats lagrar den inte. Svaren kommer enbart från detta projekts iakttagelser med källa, med en källhänvisning för varje uppgift. |
| s.0a0aee6d43 | from {n, plural, one {# checked source} other {# checked sources}} | från {n, plural, one {# kontrollerad källa} other {# kontrollerade källor}} |
| s.6a82f2e67a | “What about my country?” | ”Hur är det med mitt land?” |
| s.c758448c9e | “Where does this claim come from?” | ”Var kommer detta påstående ifrån?” |
| s.2cbbd67139 | “Who holds the population register?” | ”Vem för befolkningsregistret?” |
| s.b5fccc286f | All countries | Alla länder |
| s.614d8ab38c | All grades | Alla grader |
| s.5a586011bb | EU-27 · Evidence | EU-27 · Belägg |
| s.9926bbed27 | Evidence grade | Beläggsgrad |
| s.02ebbe2a1d | Evidence grade of each citation | Beläggsgrad för varje källhänvisning |
| s.c5c4a7ee3f | No source matches these filters. | Ingen källa matchar dessa filter. |
| s.93386c6297 | Search sources | Sök källor |
| s.1e09e293d6 | Search titles, publishers, quotes or holdings | Sök i titlar, utgivare, citat eller informationstillgångar |
| s.a9da0f0cb1 | Show {n} more | Visa {n} till |
| s.e6fd3d0e07 | Showing {shown} of {total} matching sources | Visar {shown} av {total} matchande källor |
| s.02705c3bc3 | Showing {shown} of {total} sources | Visar {shown} av {total} källor |
| s.dbaab8c74f | Source tier | Källnivå |
| s.4cf8cc1c3d | Source tier of each citation | Källnivå för varje källhänvisning |
| s.62e6fc032e | T1 · authoritative original | T1 · auktoritativt original |
| s.ea39693077 | T2 · competent public body | T2 · behörigt offentligt organ |
| s.44b358d44e | T3 · other institution or company | T3 · annan institution eller företag |
| s.cd21ad2bc1 | T4 · secondary (press, mirror) | T4 · sekundär (press, spegelwebbplats) |
| s.8a0ca5acaf | checked sources | kontrollerade källor |
| s.467ec9a623 | claims graded Strong or better | påståenden graderade Stark eller bättre |
| s.456200534a | claims they support | påståenden de stöder |
| s.c7a57a02c7 | {n, plural, one {# citation} other {# citations}} | {n, plural, one {# källhänvisning} other {# källhänvisningar}} |
| s.6032e008fa | {sources, plural, one {# source supports} other {# sources support}} {claims, plural, one {# claim} other {# claims}}. A source is admitted only after its document was fetched, its SHA-256 recorded and the quoted text found in it; failures stay out and are recorded in the repository. | {sources, plural, one {# källa stöder} other {# källor stöder}} {claims, plural, one {# påstående} other {# påståenden}}. En källa tas in först när dess dokument har hämtats, dess SHA-256 antecknats och den citerade texten hittats i det; misslyckanden hålls utanför och antecknas i repositoriet. |
| s.6a72085653 | All | Alla |
| s.5674911442 | An input without a checked source counts as not demonstrated. | En indatapost utan kontrollerad källa räknas som inte påvisad. |
| s.2992013270 | Confidence: | Tillförlitlighet: |
| s.fe591c90cd | EU-27 · Ranking by published rule | EU-27 · Rangordning enligt publicerad regel |
| s.68e6d874c0 | Full analysis of {name} | Fullständig analys: {name} |
| s.ae9629f4eb | Groups | Grupper |
| s.52230cf8d0 | Hatched: Low confidence. | Skrafferat: låg tillförlitlighet. |
| s.b1a5954a48 | High | Hög |
| s.6c2943a404 | High confidence | Hög tillförlitlighet |
| s.b132b29d37 | If {indicator} is found to be {value}: {group} | Om {indicator} visar sig vara {value}: {group} |
| s.8cf71374fa | Indicators | Indikatorer |
| s.c67dd20ee8 | Key | Teckenförklaring |
| s.a124947cbd | Low | Låg |
| s.99d4ceaeba | Low confidence | Låg tillförlitlighet |
| s.ab478f3efc | Map | Karta |
| s.d404968ea9 | Medium | Medelhög |
| s.156b5ba334 | Medium confidence | Medelhög tillförlitlighet |
| s.816c52fd2b | No | Nej |
| s.6eef664840 | None | Inga |
| s.0710eb28ba | Not yet sourced | Ännu utan källa |
| s.ed03c68d9c | Partly | Delvis |
| s.3f126fd79e | Select a state for its explanation. | Välj en stat för att se dess förklaring. |
| s.8d161f96cb | Show placements by confidence | Visa placeringar efter tillförlitlighet |
| s.a725020675 | State | Stat |
| s.d6c52426c8 | States are placed in groups by a published rule, not scored. | Staterna placeras i grupper enligt en publicerad regel, de poängsätts inte. |
| s.74585765e7 | The bar beside each state shows the groups it could still reach once its open evidence is settled; that range is its confidence. | Stapeln bredvid varje stat visar de grupper den fortfarande kan nå när dess ännu oavgjorda belägg har avgjorts; det spannet är dess tillförlitlighet. |
| s.d1c641f81e | The indicators | Indikatorerna |
| s.f70f269ba2 | The rule in full | Regeln i sin helhet |
| s.bec82514ea | What could move it | Vad som skulle kunna flytta den |
| s.5397e0583f | Yes | Ja |
| s.caa1b315e5 | could still reach {from} | kan fortfarande nå {from} |
| s.fab42543cc | could still reach {from} to {to} | kan fortfarande nå allt från {from} till {to} |
| s.ad4c27b442 | {n, plural, one {If the # tier 0/1 holding with unsourced hosting runs on non-EU infrastructure: {group}} other {If any of # tier 0/1 holdings with unsourced hosting runs on non-EU infrastructure: {group}}} | {n, plural, one {Om den enda informationstillgången på nivå 0/1 med drift utan källa drivs på infrastruktur utanför EU: {group}} other {Om någon av de # informationstillgångarna på nivå 0/1 med drift utan källa drivs på infrastruktur utanför EU: {group}}} |
| s.3a6297f664 | {term}: a gap, never a no | {term}: en lucka, aldrig ett nej |
| s.f1ff2ed428 | {term}: withheld until corrected and checked again | {term}: undanhållet tills det rättats och kontrollerats igen |

## Review

- Reviewed by: reviewer A, claude-opus-5-5, 2026-10-21
- Re-read by: reviewer B, claude-fable-5-1, 2026-10-21 (48 rewritten cells, 0 fix)
- Verdict: 661 ok, 0 fix (after one fix round)

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| s.b85a2bdd1b | sv | ok | | |
| s.fcb532f087 | sv | ok | the AML directive's generic Swedish term | |
| s.96ecaa31b4 | sv | ok | | |
| s.2f1257dc51 | sv | ok | | |
| s.ec814ead0c | sv | ok | | |
| s.f280e2a648 | sv | ok | | |
| s.d8d788ca5d | sv | ok | | |
| s.765efdcdc6 | sv | ok | applied as suggested | |
| s.aae813dd56 | sv | ok | | |
| s.3f865d6890 | sv | ok | | |
| s.3427094904 | sv | ok | | |
| s.04b7b26c8c | sv | ok | | |
| s.6b91907643 | sv | ok | | |
| s.ca20bc6b00 | sv | ok | | |
| s.3165449154 | sv | ok | | |
| s.f089a1fbed | sv | ok | | |
| s.72e58b67f4 | sv | ok | | |
| s.171ec6a77a | sv | ok | | |
| s.04c3e89d9b | sv | ok | | |
| s.aaf87fe57a | sv | ok | | |
| s.4e9d205ed7 | sv | ok | | |
| s.f19d170012 | sv | ok | applied as suggested | |
| s.042b70234d | sv | ok | | |
| s.f180a9ce79 | sv | ok | | |
| s.98bf3b1ffd | sv | ok | | |
| s.3d64ce6c47 | sv | ok | | |
| s.5343f3aabe | sv | ok | | |
| s.3b9865356c | sv | ok | | |
| s.0c3b551296 | sv | ok | | |
| s.5dfe1bc1a0 | sv | ok | | |
| s.c4fe29fe96 | sv | ok | | |
| s.ec4f0f9f9e | sv | ok | | |
| s.9704ed6cc1 | sv | ok | | |
| s.982c964c83 | sv | ok | | |
| s.8061bb6bf8 | sv | ok | | |
| s.b86fc1b412 | sv | ok | | |
| s.94accd37b7 | sv | ok | | |
| s.8667bf9045 | sv | ok | one = 1 only in sv, 'den enda' fine | |
| s.2948d7b9da | sv | ok | | |
| s.b3f1bf4f30 | sv | ok | | |
| s.f785330b4c | sv | ok | | |
| s.a91102c85d | sv | ok | | |
| s.be9109ac1b | sv | ok | | |
| s.a3d31a53fb | sv | ok | generic | |
| s.99767669ed | sv | ok | | |
| s.cbbacb3e80 | sv | ok | generic (not Riksarkivet) | |
| s.44749b1cbc | sv | ok | | |
| s.6fb2a8a8cc | sv | ok | | |
| s.e6e1757649 | sv | ok | | |
| s.b34eac40f3 | sv | ok | applied as suggested | |
| s.1652d30cec | sv | ok | | |
| s.114883188a | sv | ok | | |
| s.fd51e343e2 | sv | ok | | |
| s.2f23122d83 | sv | ok | | |
| s.a9b0cdd774 | sv | ok | | |
| s.c2cce8d695 | sv | ok | applied as suggested | |
| s.3ad8637946 | sv | ok | applied as suggested | |
| s.f987414340 | sv | ok | generic (EU's own Swedish usage), not SFS | |
| s.d0e687b079 | sv | ok | | |
| s.f83b48a858 | sv | ok | | |
| s.182d37ec74 | sv | ok | | |
| s.f2fe3e1c9e | sv | ok | | |
| s.034dd0deff | sv | ok | | |
| s.c622853228 | sv | ok | | |
| s.5e46f732e6 | sv | ok | | |
| s.1890a8b969 | sv | ok | | |
| s.acb219584d | sv | ok | applied as suggested | |
| s.62c114ace1 | sv | ok | | |
| s.110c7c517b | sv | ok | | |
| s.5f407d41f3 | sv | ok | | |
| s.1ca90cb624 | sv | ok | | |
| s.0a4c313dc5 | sv | ok | | |
| s.5c1505aea9 | sv | ok | | |
| s.2dfa66079d | sv | ok | | |
| s.d7e81c01c8 | sv | ok | applied as suggested | |
| s.1e01ee18be | sv | ok | | |
| s.967135dc53 | sv | ok | | |
| s.16b62d3922 | sv | ok | | |
| s.78d71ef805 | sv | ok | | |
| s.9be70f66f8 | sv | ok | | |
| s.eeac96e96e | sv | ok | applied as suggested | |
| s.1ef26968be | sv | ok | | |
| s.5e127373f3 | sv | ok | | |
| s.5f11eb7511 | sv | ok | | |
| s.7d46fdf50f | sv | ok | applied as suggested | |
| s.ea4e96959c | sv | ok | | |
| s.fd12863535 | sv | ok | | |
| s.fb360f9c09 | sv | ok | | |
| s.fff7760a9e | sv | ok | ”…” are Swedish quotes; open evidence = unresolved, good | |
| s.fa84aa0fe2 | sv | ok | | |
| s.966a5454e4 | sv | ok | | |
| s.47c8fcf67a | sv | ok | | |
| s.f7a15511d4 | sv | ok | | |
| s.26e5bd9d84 | sv | ok | | |
| s.3d9ef2e1a4 | sv | ok | | |
| s.3b7aee0921 | sv | ok | | |
| s.ddca7ab7f4 | sv | ok | | |
| s.5d8970fa99 | sv | ok | | |
| s.1c023ff571 | sv | ok | efterkontrollskörning is clumsy but clear; bedömare (model) vs granskare (person) kept apart | |
| s.eb41f68213 | sv | ok | | |
| s.e6c7329679 | sv | ok | | |
| s.05d27dcc23 | sv | ok | | |
| s.fd9f9cff11 | sv | ok | | |
| s.14a628e6d3 | sv | ok | | |
| s.d22fca0f44 | sv | ok | applied as suggested | |
| s.4f23e1e7f8 | sv | ok | | |
| s.06e8db2dfd | sv | ok | | |
| s.4108482c08 | sv | ok | Hög/Medelhög/Låg; Medelhög distinct from the formula's 'medel' recoverability, no clash (Medium only labels confidence) | |
| s.66e12969c2 | sv | ok | | |
| s.ed1c64ab57 | sv | ok | applied as suggested | |
| s.1052689464 | sv | ok | | |
| s.2a4e3cb3c6 | sv | ok | | |
| s.eb559b8cbc | sv | ok | | |
| s.d203be5dfd | sv | ok | | |
| s.d4a05b67a6 | sv | ok | | |
| s.188de23f5b | sv | ok | applied as suggested | |
| s.2b913254a8 | sv | ok | | |
| s.84d987fe02 | sv | ok | | |
| s.04b0dda32a | sv | ok | | |
| s.228587d1aa | sv | ok | | |
| s.18a1dacbc5 | sv | ok | | |
| s.d54360e78a | sv | ok | | |
| s.1f20e66b17 | sv | ok | | |
| s.96e578211a | sv | ok | | |
| s.0b134e18cb | sv | ok | | |
| s.252adc9f26 | sv | ok | | |
| s.aecc49c153 | sv | ok | | |
| s.5012de0774 | sv | ok | | |
| s.1ac6e0db9e | sv | ok | | |
| s.40176d930b | sv | ok | | |
| s.40f3f0b36f | sv | ok | | |
| s.7539231e04 | sv | ok | | |
| s.90a031edb0 | sv | ok | | |
| s.0c448a5f23 | sv | ok | | |
| s.51aff04e8d | sv | ok | | |
| s.8b5cf8d60c | sv | ok | | |
| s.b31b7fac2a | sv | ok | | |
| s.04c299e1b3 | sv | ok | | |
| s.61348d3cc0 | sv | ok | applied as suggested | |
| s.170a28a9db | sv | ok | | |
| s.f7fa7832f9 | sv | ok | | |
| s.bcb88598d7 | sv | ok | | |
| s.ee19cf967e | sv | ok | | |
| s.ddf48497b8 | sv | ok | | |
| s.adeb29b097 | sv | ok | | |
| s.1338a3ee0c | sv | ok | | |
| s.0d73a1c086 | sv | ok | | |
| s.5016356d5e | sv | ok | | |
| s.a29f025627 | sv | ok | | |
| s.635dcfcb5a | sv | ok | | |
| s.926a4d7e8c | sv | ok | | |
| s.9ad33161bb | sv | ok | | |
| s.4324ca9554 | sv | ok | | |
| s.cf84687053 | sv | ok | | |
| s.d11347ce3a | sv | ok | | |
| s.9f1a1d5e3e | sv | ok | | |
| s.75974ad5f7 | sv | ok | | |
| s.c342fa1f4f | sv | ok | | |
| s.a544050c90 | sv | ok | applied as suggested | |
| s.f1fceee56b | sv | ok | | |
| s.61e3fb1ddf | sv | ok | applied as suggested | |
| s.3882bb002a | sv | ok | | |
| s.67ac669b7c | sv | ok | | |
| s.4220d202c0 | sv | ok | | |
| s.a0de0a20ed | sv | ok | | |
| s.aed3b8c6a7 | sv | ok | | |
| s.8524fff511 | sv | ok | | |
| s.7c88c313f1 | sv | ok | | |
| s.cdba8c69aa | sv | ok | | |
| s.3ef3f040f0 | sv | ok | | |
| s.ce296c876c | sv | ok | | |
| s.4cc558b843 | sv | ok | applied as suggested | |
| s.729e6ed847 | sv | ok | | |
| s.b55e22fe78 | sv | ok | | |
| s.a6dfdeaa3a | sv | ok | | |
| s.67805069b9 | sv | ok | | |
| s.8012ff51a0 | sv | ok | | |
| s.408e9edfd6 | sv | ok | | |
| s.625916084e | sv | ok | | |
| s.ca310cd530 | sv | ok | | |
| s.cf7088eefc | sv | ok | | |
| s.a3e860461c | sv | ok | | |
| s.658d6ce48a | sv | ok | | |
| s.2d29475e37 | sv | ok | | |
| s.922e29d89c | sv | ok | applied as suggested | |
| s.9e80ea69fc | sv | ok | | |
| s.c77394b252 | sv | ok | | |
| s.78afc1371f | sv | ok | | |
| s.e3c6ef524e | sv | ok | | |
| s.534ce8e519 | sv | ok | | |
| s.b60bf227ad | sv | ok | | |
| s.d523ebbd10 | sv | ok | | |
| s.bcf29b342c | sv | ok | | |
| s.246be074fc | sv | ok | | |
| s.58fe5d4e7a | sv | ok | | |
| s.0f8f4bbe66 | sv | ok | | |
| s.e3e89bb064 | sv | ok | | |
| s.dfdb505f72 | sv | ok | | |
| s.aeff1bc997 | sv | ok | | |
| s.72f9d33997 | sv | ok | | |
| s.5bdb3bb46b | sv | ok | | |
| s.d4fd0a232e | sv | ok | | |
| s.d868b45fe0 | sv | ok | | |
| s.4bab2d8fe1 | sv | ok | | |
| s.672c9e09e8 | sv | ok | applied as suggested | |
| s.cada9ca9eb | sv | ok | | |
| s.3a88f501b3 | sv | ok | | |
| s.043cff352e | sv | ok | | |
| s.c3679c21c3 | sv | ok | | |
| s.835bc2011e | sv | ok | | |
| s.ce0770ac86 | sv | ok | | |
| s.05769b70b7 | sv | ok | | |
| s.81ff3110e4 | sv | ok | | |
| s.faad2c5c10 | sv | ok | | |
| s.3b98e97b40 | sv | ok | | |
| s.6f33a0a6ed | sv | ok | | |
| s.3c90d4c91b | sv | ok | | |
| s.97d5abd9c8 | sv | ok | | |
| s.83db15cb2f | sv | ok | | |
| s.fe17d950e1 | sv | ok | | |
| s.c2425b1244 | sv | ok | preposition before the break is fine: 'Navigera i / Molnsuveränitet' | |
| s.17b90bc012 | sv | ok | applied as suggested | |
| s.6f50cd14eb | sv | ok | | |
| s.57e128cfba | sv | ok | | |
| s.f816a4e57e | sv | ok | | |
| s.465681c687 | sv | ok | | |
| s.1303e4380a | sv | ok | | |
| s.b7e3dcb83c | sv | ok | | |
| s.6fb6b67ddd | sv | ok | | |
| s.c0dcb865ad | sv | ok | | |
| s.35e307703a | sv | ok | | |
| s.bcacbfd850 | sv | ok | | |
| s.d286d81d00 | sv | ok | | |
| s.c092c44522 | sv | ok | | |
| s.6cdea7451a | sv | ok | | |
| s.f65e66aecd | sv | ok | | |
| s.1f1f4ae384 | sv | ok | | |
| s.120772e5ec | sv | ok | | |
| s.5bd44ebe63 | sv | ok | | |
| s.519c7b88ec | sv | ok | | |
| s.01561ccd29 | sv | ok | | |
| s.69020dbcaa | sv | ok | | |
| s.eaebc1bf76 | sv | ok | | |
| s.d85a8f2af0 | sv | ok | | |
| s.9cf83d1f40 | sv | ok | | |
| s.5b9ad38e16 | sv | ok | applied as suggested | |
| s.c5a046052e | sv | ok | | |
| s.6d0b23c56b | sv | ok | | |
| s.1b7ae26250 | sv | ok | | |
| s.3d3791aae5 | sv | ok | | |
| s.6e3715ac61 | sv | ok | | |
| s.62bce9422f | sv | ok | | |
| s.0a4470d64e | sv | ok | | |
| s.c29220f958 | sv | ok | | |
| s.fc45091249 | sv | ok | | |
| s.56a5813065 | sv | ok | | |
| s.26f6f10353 | sv | ok | | |
| s.7e439c353e | sv | ok | | |
| s.06ec582dac | sv | ok | | |
| s.19d87d1bde | sv | ok | | |
| s.09ca55ca52 | sv | ok | | |
| s.38e9199be7 | sv | ok | | |
| s.50cb90be5a | sv | ok | | |
| s.94cae35178 | sv | ok | | |
| s.0149001987 | sv | ok | | |
| s.f834acfd05 | sv | ok | | |
| s.7ef8384426 | sv | ok | | |
| s.14caa5be28 | sv | ok | | |
| s.6cc3364a24 | sv | ok | | |
| s.2eb56be3c2 | sv | ok | | |
| s.9c862eb9f0 | sv | ok | applied as suggested | |
| s.a52b2a1bc3 | sv | ok | | |
| s.cf676b1c20 | sv | ok | | |
| s.c5b7db8b29 | sv | ok | | |
| s.a3308aeab5 | sv | ok | | |
| s.bb76dfbf61 | sv | ok | | |
| s.68478ccc35 | sv | ok | | |
| s.964ca95667 | sv | ok | | |
| s.e851648d32 | sv | ok | | |
| s.2d762b287f | sv | ok | | |
| s.ee2dc54c03 | sv | ok | | |
| s.0716862035 | sv | ok | | |
| s.0d0529aac3 | sv | ok | | |
| s.91f2776860 | sv | ok | | |
| s.8aec1d10d9 | sv | ok | | |
| s.241bbf18a2 | sv | ok | | |
| s.8263673446 | sv | ok | | |
| s.1722e9149a | sv | ok | | |
| s.2fae75510d | sv | ok | | |
| s.7211854229 | sv | ok | | |
| s.181f5d30d2 | sv | ok | | |
| s.75a1a193a3 | sv | ok | | |
| s.01858f5a62 | sv | ok | | |
| s.c09de98f08 | sv | ok | | |
| s.0e9f7be095 | sv | ok | | |
| s.eec3fda3e7 | sv | ok | | |
| s.231d586afd | sv | ok | | |
| s.043e4c8e36 | sv | ok | | |
| s.800a1bab1c | sv | ok | applied as suggested | |
| s.a856f76fdf | sv | ok | | |
| s.a22a342f8d | sv | ok | | |
| s.fa4dadae15 | sv | ok | | |
| s.250ffcac56 | sv | ok | | |
| s.b62c67154e | sv | ok | | |
| s.475db6333a | sv | ok | | |
| s.5c5d692d28 | sv | ok | | |
| s.ea3fdab757 | sv | ok | | |
| s.e974d7da17 | sv | ok | | |
| s.053f428fe0 | sv | ok | | |
| s.78610e43d5 | sv | ok | | |
| s.10e16699d4 | sv | ok | applied as suggested | |
| s.01263cd27f | sv | ok | | |
| s.227488de9f | sv | ok | | |
| s.6280a2b4d6 | sv | ok | | |
| s.637ed308e2 | sv | ok | | |
| s.add10c7564 | sv | ok | | |
| s.0273336afa | sv | ok | | |
| s.9542e80c0f | sv | ok | | |
| s.51a35d7d82 | sv | ok | | |
| s.cf94bdf391 | sv | ok | | |
| s.b8e3b8bd5e | sv | ok | | |
| s.bbc5010fac | sv | ok | | |
| s.3aeffd96e7 | sv | ok | | |
| s.5b1841d68f | sv | ok | | |
| s.1478731d37 | sv | ok | | |
| s.bae3748df9 | sv | ok | | |
| s.24ebc43ac7 | sv | ok | | |
| s.079984afeb | sv | ok | | |
| s.7843c8c20c | sv | ok | | |
| s.24699e1898 | sv | ok | | |
| s.c8e71a0183 | sv | ok | | |
| s.c79b67e3d8 | sv | ok | applied as suggested | |
| s.ef46c30d85 | sv | ok | | |
| s.ede777d505 | sv | ok | | |
| s.5db4b0b098 | sv | ok | | |
| s.729edbd662 | sv | ok | | |
| s.ad6f8b62f4 | sv | ok | | |
| s.18c3611eba | sv | ok | | |
| s.e54c52fb78 | sv | ok | | |
| s.fd8eddd9c9 | sv | ok | | |
| s.cfff8d648e | sv | ok | | |
| s.f691d5706f | sv | ok | | |
| s.e675b97615 | sv | ok | | |
| s.8f848ebe67 | sv | ok | | |
| s.ce357a47b0 | sv | ok | | |
| s.10b1e5e62e | sv | ok | | |
| s.a4725b67be | sv | ok | | |
| s.df7a559160 | sv | ok | | |
| s.7926c21254 | sv | ok | | |
| s.3e33af3204 | sv | ok | | |
| s.f245ee9452 | sv | ok | | |
| s.9423bc8d6d | sv | ok | | |
| s.a1d971de10 | sv | ok | | |
| s.3e344387ad | sv | ok | | |
| s.018ce99e27 | sv | ok | | |
| s.4f908f7674 | sv | ok | | |
| s.52bd599c58 | sv | ok | | |
| s.f0f233b509 | sv | ok | | |
| s.f013b5417d | sv | ok | | |
| s.c5a8b8e80a | sv | ok | | |
| s.d4765d94d3 | sv | ok | | |
| s.1eff5035e1 | sv | ok | | |
| s.5f0ebc535d | sv | ok | | |
| s.fee06e6365 | sv | ok | | |
| s.cda5fb4760 | sv | ok | | |
| s.993257fb5e | sv | ok | applied as suggested | |
| s.17c9476d46 | sv | ok | | |
| s.12bec467e7 | sv | ok | applied as suggested | |
| s.cc6ed4fb32 | sv | ok | | |
| s.3d0b3240e0 | sv | ok | | |
| s.b9a5fcd7ef | sv | ok | | |
| s.765bf1c1cf | sv | ok | | |
| s.c637f2f828 | sv | ok | | |
| s.9bdc1b8a5a | sv | ok | | |
| s.3857c8a6eb | sv | ok | applied as suggested | |
| s.2d30c6a60a | sv | ok | | |
| s.38e0d36aeb | sv | ok | | |
| s.d04bdc28e4 | sv | ok | | |
| s.1776b85ee1 | sv | ok | | |
| s.9970ff42f7 | sv | ok | | |
| s.3e1e5f805b | sv | ok | | |
| s.c9c4eac440 | sv | ok | | |
| s.e9c8b2ea10 | sv | ok | | |
| s.fe2ef59507 | sv | ok | | |
| s.1dff3d34f6 | sv | ok | | |
| s.31dfb891c1 | sv | ok | | |
| s.00b62aa8d7 | sv | ok | | |
| s.7113ac8ce1 | sv | ok | | |
| s.f721b214f5 | sv | ok | | |
| s.888e3804fd | sv | ok | applied as suggested | |
| s.8ae15f6ce9 | sv | ok | | |
| s.b432ab8cbc | sv | ok | applied as suggested | |
| s.546d4ca1d4 | sv | ok | | |
| s.e1cb96c8fc | sv | ok | | |
| s.cbf1967539 | sv | ok | | |
| s.30649e713e | sv | ok | | |
| s.eaff3ef7f6 | sv | ok | | |
| s.73a6bc853d | sv | ok | | |
| s.b076a852a1 | sv | ok | | |
| s.88ff1bcc44 | sv | ok | | |
| s.479d113628 | sv | ok | applied as suggested | |
| s.5086222ca9 | sv | ok | applied as suggested | |
| s.6a45998a0f | sv | ok | applied as suggested | |
| s.04db7e08ad | sv | ok | applied as suggested | |
| s.d5cdd44c91 | sv | ok | | |
| s.b5e253d8db | sv | ok | | |
| s.2d996f403f | sv | ok | | |
| s.46cd281992 | sv | ok | | |
| s.38609176e5 | sv | ok | | |
| s.d14acd3ca5 | sv | ok | | |
| s.55350ab3c9 | sv | ok | | |
| s.b1afc6047f | sv | ok | | |
| s.2a67691862 | sv | ok | | |
| s.83c5b8f8e3 | sv | ok | | |
| s.1c840c98c3 | sv | ok | | |
| s.c50b2008be | sv | ok | | |
| s.0a56eb289b | sv | ok | | |
| s.40220b1e7e | sv | ok | | |
| s.0f57612582 | sv | ok | | |
| s.d2a21b33df | sv | ok | | |
| s.f4a9d8a2ef | sv | ok | applied as suggested | |
| s.89a0f5386c | sv | ok | | |
| s.73c9bdb1ef | sv | ok | | |
| s.5b3c690d76 | sv | ok | | |
| s.5cc022ab85 | sv | ok | | |
| s.7db4df96f9 | sv | ok | | |
| s.c83eec427b | sv | ok | | |
| s.4eb6cd0604 | sv | ok | | |
| s.24f9f480cb | sv | ok | | |
| s.429dd2de76 | sv | ok | | |
| s.46d0f63826 | sv | ok | | |
| s.f4d49c2a2f | sv | ok | | |
| s.5121a5fdfe | sv | ok | | |
| s.18af0127b4 | sv | ok | | |
| s.854aa62c7e | sv | ok | | |
| s.da2b128db7 | sv | ok | | |
| s.128230821c | sv | ok | applied as suggested | |
| s.bc69ac2068 | sv | ok | | |
| s.6fb27e7fbd | sv | ok | | |
| s.4eb735bb3f | sv | ok | | |
| s.111fb20b29 | sv | ok | | |
| s.a93f1c11f6 | sv | ok | | |
| s.86a78e54b8 | sv | ok | | |
| s.2181d0e7e8 | sv | ok | | |
| s.ac1d33ad53 | sv | ok | | |
| s.9fa755d8c3 | sv | ok | | |
| s.31003ae899 | sv | ok | | |
| s.727009e62c | sv | ok | | |
| s.aea2d84e37 | sv | ok | | |
| s.e4edd0f7f7 | sv | ok | | |
| s.97e71dbf49 | sv | ok | | |
| s.3881a07877 | sv | ok | | |
| s.e3543005ce | sv | ok | | |
| s.ce857fdb6d | sv | ok | | |
| s.4f0e8a73c5 | sv | ok | | |
| s.7d997eb840 | sv | ok | applied as suggested | |
| s.31b0694684 | sv | ok | | |
| s.f7da6b0da5 | sv | ok | | |
| s.f004c2e1a5 | sv | ok | | |
| s.3e17caa890 | sv | ok | | |
| s.7289dc9a3c | sv | ok | | |
| s.ad28038a5a | sv | ok | | |
| s.bea0a2b11e | sv | ok | | |
| s.ada9707155 | sv | ok | | |
| s.988e1121a7 | sv | ok | | |
| s.b1449815d6 | sv | ok | | |
| s.253c555f4a | sv | ok | | |
| s.2c56ec23a3 | sv | ok | applied as suggested | |
| s.1db035c98e | sv | ok | | |
| s.aa34ceb9e3 | sv | ok | | |
| s.05b94e02ba | sv | ok | | |
| s.11f7a3da3a | sv | ok | | |
| s.a16a4eda7c | sv | ok | | |
| s.fcbea7aab2 | sv | ok | | |
| s.f2bd2a657e | sv | ok | | |
| s.3562777bc6 | sv | ok | | |
| s.588900c714 | sv | ok | | |
| s.3f3a83bcc6 | sv | ok | | |
| s.12e1b0f401 | sv | ok | | |
| s.9003825bdf | sv | ok | | |
| s.e4ec528b79 | sv | ok | | |
| s.ed1aec3980 | sv | ok | | |
| s.bee54c9cc3 | sv | ok | | |
| s.9a3ea0598e | sv | ok | | |
| s.b947003d5c | sv | ok | | |
| s.e08050d888 | sv | ok | | |
| s.8bdca003cc | sv | ok | | |
| s.72677028b4 | sv | ok | | |
| s.0ba83cb8e8 | sv | ok | | |
| s.c8640fb95c | sv | ok | | |
| s.a11a9ee218 | sv | ok | | |
| s.8467c0d99c | sv | ok | | |
| s.50f704f3bf | sv | ok | | |
| s.57ddfe0efd | sv | ok | | |
| s.bec93ba893 | sv | ok | | |
| s.29340e604c | sv | ok | | |
| s.34bf7b2eb8 | sv | ok | | |
| s.911fbc0f5a | sv | ok | | |
| s.a2a5bdeca9 | sv | ok | | |
| s.4eb408e1b5 | sv | ok | | |
| s.7ee0b56b76 | sv | ok | | |
| s.b2c01838bc | sv | ok | | |
| s.edfc76939f | sv | ok | | |
| s.3da100fd5b | sv | ok | | |
| s.0b3bc63de0 | sv | ok | | |
| s.ba7661f435 | sv | ok | | |
| s.6338f7ec43 | sv | ok | | |
| s.93d2f80ef7 | sv | ok | applied as suggested | |
| s.60e6d488a8 | sv | ok | | |
| s.088fc2bb86 | sv | ok | | |
| s.87abd9beab | sv | ok | | |
| s.5e705951b3 | sv | ok | | |
| s.32ea9a3579 | sv | ok | | |
| s.f9b095cf90 | sv | ok | =0 branch present and reads right | |
| s.59a9dfcb7b | sv | ok | | |
| s.5233d9d9bc | sv | ok | | |
| s.13e63611d5 | sv | ok | | |
| s.3c558d8e40 | sv | ok | | |
| s.66d69ab480 | sv | ok | | |
| s.b2232452b5 | sv | ok | visible 'Kontrollera →', screen reader 'Kontrollera: …'; fine | |
| s.9732ee3c8c | sv | ok | | |
| s.08ca30a8e2 | sv | ok | | |
| s.f2e8958b8a | sv | ok | | |
| s.c535a55f4c | sv | ok | | |
| s.2cb5e47964 | sv | ok | | |
| s.2210d472bf | sv | ok | | |
| s.059589ec92 | sv | ok | | |
| s.8312889825 | sv | ok | | |
| s.0f51795253 | sv | ok | | |
| s.c16dfd1733 | sv | ok | | |
| s.fc5a046860 | sv | ok | | |
| s.7c563fab97 | sv | ok | | |
| s.5ad1c01297 | sv | ok | | |
| s.facf040ca4 | sv | ok | | |
| s.c65c8aee5a | sv | ok | | |
| s.12ceb0ea2f | sv | ok | | |
| s.ef3c791627 | sv | ok | applied as suggested | |
| s.b5b404d6c1 | sv | ok | | |
| s.04226ffebd | sv | ok | | |
| s.08cbf6a3a2 | sv | ok | | |
| s.0023b8ecba | sv | ok | | |
| s.9b10914d8b | sv | ok | | |
| s.290d3b83ca | sv | ok | | |
| s.a9617bf1d2 | sv | ok | | |
| s.8d6c70fc9b | sv | ok | | |
| s.5c0ec459d6 | sv | ok | | |
| s.8661d7d53e | sv | ok | | |
| s.6a64b56ba0 | sv | ok | | |
| s.1df1955d61 | sv | ok | | |
| s.3902a2b7c3 | sv | ok | | |
| s.13df1314af | sv | ok | | |
| s.01916f8bc6 | sv | ok | applied as suggested | |
| s.8ee8479c84 | sv | ok | | |
| s.4d8b6f0aaa | sv | ok | applied as suggested | |
| s.a2c6bfc5eb | sv | ok | | |
| s.19ef957b3d | sv | ok | | |
| s.21ce9bdc8a | sv | ok | | |
| s.0173c1185c | sv | ok | | |
| s.8f8284b6b9 | sv | ok | | |
| s.b72e0d077f | sv | ok | | |
| s.e1e7baf404 | sv | ok | | |
| s.b509d96b12 | sv | ok | | |
| s.933fc9cce0 | sv | ok | | |
| s.dae3acc17d | sv | ok | applied as suggested | |
| s.56b3945e3a | sv | ok | | |
| s.aa7ef6a9ca | sv | ok | | |
| s.b124f047fe | sv | ok | | |
| s.816afa09f1 | sv | ok | | |
| s.dc144542ae | sv | ok | | |
| s.afd734c0c3 | sv | ok | | |
| s.8b656a5dd9 | sv | ok | | |
| s.384dcfc951 | sv | ok | | |
| s.e5130af021 | sv | ok | | |
| s.9d35a1e8b1 | sv | ok | | |
| s.4be913ff63 | sv | ok | applied as suggested | |
| s.e3a34f794f | sv | ok | | |
| s.7d70fca297 | sv | ok | | |
| s.5bfab1e2af | sv | ok | | |
| s.81cca36896 | sv | ok | | |
| s.7c45e96e58 | sv | ok | | |
| s.a89a395a9c | sv | ok | applied as suggested | |
| s.7cd5e5df45 | sv | ok | | |
| s.f623f6f706 | sv | ok | | |
| s.1be38688bb | sv | ok | | |
| s.8289ec6739 | sv | ok | | |
| s.4d2464a036 | sv | ok | | |
| s.841efde86d | sv | ok | | |
| s.052bc43f37 | sv | ok | | |
| s.2868ce33aa | sv | ok | | |
| s.fb80efb9ec | sv | ok | | |
| s.ac9aab6fea | sv | ok | | |
| s.e8ca289b11 | sv | ok | | |
| s.ab08a795f2 | sv | ok | | |
| s.2bb9ad51b3 | sv | ok | | |
| s.09394824be | sv | ok | | |
| s.65eb2b971d | sv | ok | | |
| s.3326258239 | sv | ok | | |
| s.4b63a71f07 | sv | ok | | |
| s.38377c29fc | sv | ok | applied as suggested | |
| s.0a4713ee3a | sv | ok | | |
| s.0a0aee6d43 | sv | ok | | |
| s.6a82f2e67a | sv | ok | | |
| s.c758448c9e | sv | ok | | |
| s.2cbbd67139 | sv | ok | | |
| s.b5fccc286f | sv | ok | | |
| s.614d8ab38c | sv | ok | | |
| s.5a586011bb | sv | ok | | |
| s.9926bbed27 | sv | ok | | |
| s.02ebbe2a1d | sv | ok | | |
| s.c5c4a7ee3f | sv | ok | | |
| s.93386c6297 | sv | ok | | |
| s.1e09e293d6 | sv | ok | | |
| s.a9da0f0cb1 | sv | ok | | |
| s.e6fd3d0e07 | sv | ok | | |
| s.02705c3bc3 | sv | ok | | |
| s.dbaab8c74f | sv | ok | | |
| s.4cf8cc1c3d | sv | ok | | |
| s.62e6fc032e | sv | ok | | |
| s.ea39693077 | sv | ok | | |
| s.44b358d44e | sv | ok | | |
| s.cd21ad2bc1 | sv | ok | applied as suggested | |
| s.8a0ca5acaf | sv | ok | | |
| s.467ec9a623 | sv | ok | | |
| s.456200534a | sv | ok | | |
| s.c7a57a02c7 | sv | ok | | |
| s.6032e008fa | sv | ok | | |
| s.6a72085653 | sv | ok | | |
| s.5674911442 | sv | ok | applied as suggested | |
| s.2992013270 | sv | ok | | |
| s.fe591c90cd | sv | ok | | |
| s.68e6d874c0 | sv | ok | | |
| s.ae9629f4eb | sv | ok | | |
| s.52230cf8d0 | sv | ok | | |
| s.b1a5954a48 | sv | ok | same string as the priority band High | |
| s.6c2943a404 | sv | ok | | |
| s.b132b29d37 | sv | ok | | |
| s.8cf71374fa | sv | ok | | |
| s.c67dd20ee8 | sv | ok | | |
| s.a124947cbd | sv | ok | | |
| s.99d4ceaeba | sv | ok | | |
| s.ab478f3efc | sv | ok | | |
| s.d404968ea9 | sv | ok | | |
| s.156b5ba334 | sv | ok | | |
| s.816c52fd2b | sv | ok | | |
| s.6eef664840 | sv | ok | | |
| s.0710eb28ba | sv | ok | | |
| s.ed03c68d9c | sv | ok | | |
| s.3f126fd79e | sv | ok | | |
| s.8d161f96cb | sv | ok | | |
| s.a725020675 | sv | ok | | |
| s.d6c52426c8 | sv | ok | | |
| s.74585765e7 | sv | ok | | |
| s.d1c641f81e | sv | ok | | |
| s.f70f269ba2 | sv | ok | | |
| s.bec82514ea | sv | ok | | |
| s.5397e0583f | sv | ok | | |
| s.caa1b315e5 | sv | ok | | |
| s.fab42543cc | sv | ok | applied as suggested | |
| s.ad4c27b442 | sv | ok | | |
| s.3a6297f664 | sv | ok | | |
| s.f1ff2ed428 | sv | ok | | |
