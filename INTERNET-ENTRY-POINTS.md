# Where the internet enters each member state

An authored note, 2026-10-14. Not generated, not in the bundle, the web app, the PDFs or /ask. Every row cites a
page a reader can open and the date it was fetched, or is marked [unverified]; a state with no row of a kind has one
row that says so. It ranks nothing: the order within a state is by Kind then Name, and every entry the cited lists
give is a row, with no selection.

Review status: drafted on 2026-10-14 by claude-fable-5-1 in Claude Code, the rows written by a script from the
fetched pages rather than by hand; the same-model review and the cross-model check are recorded in the Method
section as they happen. No person has read it.

## Definitions

- E1: a subsea cable landing point the Submarine Cable Map labels with the state's name (which includes offshore
  platforms such as Denmark's Tyra and Halfdan), per the map's
  index https://www.submarinecablemap.com/api/v3/landing-point/landing-point-geo.json, accessed 2026-10-14. The
  map is TeleGeography's. Its code states one licence, in these words: "Any reference to TeleGeography's Submarine
  Cable Map, URL, or any screencapture of the map is made available under the Creative Commons License:
  Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)", and the page that sentence links to
  (https://www2.telegeography.com/cite-telegeography-map, accessed 2026-10-14) says that access to the underlying
  databases remains restricted to paying subscribers. The licence of the JSON pages the rows cite is not stated. Each
  E1 row is a reference to the map by URL, and the names it reproduces are offered under CC BY-SA 4.0 with
  attribution to TeleGeography as the conservative reading; `LICENSE-DATA` records that, and the owner's ruling on
  the wording is open in `TODO.md`.
  Each row cites the map's JSON page for the point, which names it and its cables; the map's HTML pages are an
  application shell with no text in them and are never cited. The label decides the state, and the note does not
  re-draw the map's line: "Kralendijk, Bonaire, Netherlands" is NL although Bonaire is outside EU territory, and the
  map's four other points labelled "Bonaire, Sint Eustatius and Saba" are no state's rows; "Girne, Cyprus" is CY; the
  Canary Islands are ES and Madeira and the Azores are PT because the map labels them so, while the French outermost
  regions (Guadeloupe, Martinique, French Guiana, Réunion, Mayotte) are labelled under their own names and so are not
  FR rows, an asymmetry the map's labels make and the note reports. The checker refuses an E1 row whose label does
  not end with the state's name. The
  Place cell of an E1 row is the middle part of a three-part label ("Bonaire", "Canary Islands"), else —. A cable the
  map marks as planned is suffixed (planned, RFS <year>), or (planned) where the map gives no year.
- E2: an internet exchange point in the state as PeeringDB lists it, per PeeringDB's exchange list for the state's
  country code, https://www.peeringdb.com/api/ix?country=NL&depth=0 for the Netherlands and GR for Greece, accessed
  2026-10-14. Each row cites the exchange's PeeringDB page. The name is PeeringDB's own, including its separate
  records for one exchange's LANs; the website is PeeringDB's field, fetched once for the link register and never a
  basis, so its answer in the register is not a claim about the row. Euro-IX's IXP-DB is the cross-check in the
  Method section and never a row's basis, because it has no page per exchange.
- E3: a statute or regulator page that names a landing station or an exchange point, cited on the row; in this
  version only where the project's source register already holds the page.
- Satellite gateways are out: no published list names the earth stations per state in a way a row could cite, so
  every such row would be the note's own word.
- Derived terms, counted from the rows by the checker and written in each state's Counts line, which no hand writes:
  no-landing, a state with no E1 row whose cables include one in service; single-landing, a state with exactly one
  such row; single-exchange, a state with one E2 row or none. In a Counts line, "unverified" counts the E1 rows
  marked [unverified] or without a cable cell to read; such a row is not in service. Rows are ordered by Kind, then
  by Name with case folded, by code point. The figures in the Method section are the checker's printed totals,
  copied on the date given; the Counts lines are the ones the gate holds.
  The owner asked for the "key entry and choke points"; this note does not judge which entry carries the traffic
  or what would follow if one failed, it counts what the cited lists give, and those three terms are the only
  reading of "choke point" it offers.

## Austria (AT)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | (none on the map) | — | — | none: searched 2026-10-14 |
| E2 | AAIX | Klagenfurt | https://ixp-manager.aaix.at | E2: https://www.peeringdb.com/ix/377, accessed 2026-10-14 |
| E2 | ALPSiX | Klagenfurt/Villach | https://breitbandinfrastruktur.at/alpsix | E2: https://www.peeringdb.com/ix/5054, accessed 2026-10-14 |
| E2 | ERA-IX Vienna | Vienna | https://www.era-ix.com | E2: https://www.peeringdb.com/ix/5029, accessed 2026-10-14 |
| E2 | GraX | Graz | http://www.grax.at | E2: https://www.peeringdb.com/ix/430, accessed 2026-10-14 |
| E2 | SAIX | Salzburg | https://www.saix.at | E2: https://www.peeringdb.com/ix/1073, accessed 2026-10-14 |
| E2 | Tirol-IX | Innsbruck/Tirol | http://www.tirol-ix.at | E2: https://www.peeringdb.com/ix/1009, accessed 2026-10-14 |
| E2 | VIX | Vienna | http://www.vix.at | E2: https://www.peeringdb.com/ix/50, accessed 2026-10-14 |

Counts: E1 0 (in service 0, planned-only 0, unverified 0), E2 7, E3 0; no-landing yes; single-landing no; single-exchange no.

## Belgium (BE)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Bredene, Belgium | — | Pan European Crossing (UK-Belgium) | E1: https://www.submarinecablemap.com/api/v3/landing-point/bredene-belgium.json, accessed 2026-10-14 |
| E1 | Ostend, Belgium | — | Mercator, Q&E North, Tangerine | E1: https://www.submarinecablemap.com/api/v3/landing-point/ostend-belgium.json, accessed 2026-10-14 |
| E2 | BelgiumIX | Brussels, Ghent, Leuven, Antwerp, Hasselt | https://belgiumix.net | E2: https://www.peeringdb.com/ix/2496, accessed 2026-10-14 |
| E2 | BNIX | Brussels | https://www.bnix.net | E2: https://www.peeringdb.com/ix/59, accessed 2026-10-14 |

Counts: E1 2 (in service 2, planned-only 0, unverified 0), E2 2, E3 0; no-landing no; single-landing no; single-exchange no.

## Bulgaria (BG)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Aheloy, Bulgaria | — | Kardesa (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/aheloy-bulgaria.json, accessed 2026-10-14 |
| E1 | Balchik, Bulgaria | — | Caucasus Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/balchik-bulgaria.json, accessed 2026-10-14 |
| E1 | Varna, Bulgaria | — | KAFOS | E1: https://www.submarinecablemap.com/api/v3/landing-point/varna-bulgaria.json, accessed 2026-10-14 |
| E2 | 1-BG FREE | Sofia | https://1-ix.eu/1bg | E2: https://www.peeringdb.com/ix/4996, accessed 2026-10-14 |
| E2 | B-IX | Sofia | https://www.b-ix.net | E2: https://www.peeringdb.com/ix/326, accessed 2026-10-14 |
| E2 | BIX.BG | Sofia | https://www.bix.bg | E2: https://www.peeringdb.com/ix/331, accessed 2026-10-14 |
| E2 | MegaIX Sofia | Sofia | https://megaport.com | E2: https://www.peeringdb.com/ix/1056, accessed 2026-10-14 |
| E2 | NetIX | Sofia | http://www.netix.net | E2: https://www.peeringdb.com/ix/699, accessed 2026-10-14 |
| E2 | T-CIX | Sofia | http://www.t-cix.net | E2: https://www.peeringdb.com/ix/1089, accessed 2026-10-14 |
| E2 | TurkIX Sofia | Sofia | https://www.turkix.bg | E2: https://www.peeringdb.com/ix/4186, accessed 2026-10-14 |
| E2 | VarnaIX | Varna | http://www.varnaix.net | E2: https://www.peeringdb.com/ix/2675, accessed 2026-10-14 |

Counts: E1 3 (in service 2, planned-only 1, unverified 0), E2 8, E3 0; no-landing no; single-landing no; single-exchange no.

## Croatia (HR)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Dubrovnik, Croatia | — | Adria-1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/dubrovnik-croatia.json, accessed 2026-10-14 |
| E1 | Umag, Croatia | — | Italy-Croatia | E1: https://www.submarinecablemap.com/api/v3/landing-point/umag-croatia.json, accessed 2026-10-14 |
| E2 | ADRIA-IX | Rijeka | https://adria-ix.org | E2: https://www.peeringdb.com/ix/4085, accessed 2026-10-14 |
| E2 | CIX | Zagreb | http://www.cix.hr | E2: https://www.peeringdb.com/ix/303, accessed 2026-10-14 |

Counts: E1 2 (in service 2, planned-only 0, unverified 0), E2 2, E3 0; no-landing no; single-landing no; single-exchange no.

## Cyprus (CY)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Girne, Cyprus | — | Turcyos-1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/girne-cyprus.json, accessed 2026-10-14 |
| E1 | Iskele, Cyprus | — | Turcyos-2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/iskele-cyprus.json, accessed 2026-10-14 |
| E1 | Pentaskhinos, Cyprus | — | CADMOS, CADMOS-2 (planned, RFS 2027), Ebla (planned, RFS 2028), MedNautilus Submarine System, POSEIDON, TE North/TGN-Eurasia/SEACOM/Alexandros/Medex, UGARIT | E1: https://www.submarinecablemap.com/api/v3/landing-point/pentaskhinos-cyprus.json, accessed 2026-10-14 |
| E1 | Yeroskipos, Cyprus | — | Blue, Exelera North, Hawk, Medusa Submarine Cable System, PEACE Cable, POSEIDON | E1: https://www.submarinecablemap.com/api/v3/landing-point/yeroskipos-cyprus.json, accessed 2026-10-14 |
| E2 | CyIX | Nicosia / Cyprus | http://www.cytanet.com.cy/network/cyix | E2: https://www.peeringdb.com/ix/487, accessed 2026-10-14 |
| E2 | JumboIX Cyprus | Limassol | https://www.iptp.net/en_US/jumbo-internet-exchange/jumboix-cyprus-pricing-plans | E2: https://www.peeringdb.com/ix/3541, accessed 2026-10-14 |

Counts: E1 4 (in service 4, planned-only 0, unverified 0), E2 2, E3 0; no-landing no; single-landing no; single-exchange no.

## Czechia (CZ)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | (none on the map) | — | — | none: searched 2026-10-14 |
| E2 | 1-CZ FREE | Prague | https://1-ix.eu/1cz | E2: https://www.peeringdb.com/ix/4995, accessed 2026-10-14 |
| E2 | BR-IX | Brno | http://www.br-ix.cz | E2: https://www.peeringdb.com/ix/864, accessed 2026-10-14 |
| E2 | CBIX | Brno | http://www.cbix.cz/en | E2: https://www.peeringdb.com/ix/477, accessed 2026-10-14 |
| E2 | NIX.CZ | Prague | http://www.nix.cz | E2: https://www.peeringdb.com/ix/71, accessed 2026-10-14 |
| E2 | NIX.CZ FENIX | Prague | http://www.nix.cz | E2: https://www.peeringdb.com/ix/2848, accessed 2026-10-14 |
| E2 | Peering.cz | Prague, Bratislava, Vienna, Frankfurt | http://www.peering.cz | E2: https://www.peeringdb.com/ix/713, accessed 2026-10-14 |

Counts: E1 0 (in service 0, planned-only 0, unverified 0), E2 6, E3 0; no-landing yes; single-landing no; single-exchange no.

## Denmark (DK)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Alsgarde, Denmark | — | Denmark-Sweden 17 | E1: https://www.submarinecablemap.com/api/v3/landing-point/alsgarde-denmark.json, accessed 2026-10-14 |
| E1 | Blaabjerg, Denmark | — | Aurora (planned, RFS 2028), CANTAT-3, DANICE, Havfrue/AEC-2, IOEMA-1 (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/blaabjerg-denmark.json, accessed 2026-10-14 |
| E1 | Bogense, Denmark | — | GlobalConnect 6 (GC6) | E1: https://www.submarinecablemap.com/api/v3/landing-point/bogense-denmark.json, accessed 2026-10-14 |
| E1 | Brondby, Denmark | — | GlobalConnect Aurora, GlobalConnect Denmark-Sweden | E1: https://www.submarinecablemap.com/api/v3/landing-point/brondby-denmark.json, accessed 2026-10-14 |
| E1 | Dragor, Denmark | — | Scandinavian Ring South | E1: https://www.submarinecablemap.com/api/v3/landing-point/dragor-denmark.json, accessed 2026-10-14 |
| E1 | Endrup, Denmark | — | COBRAcable | E1: https://www.submarinecablemap.com/api/v3/landing-point/endrup-denmark.json, accessed 2026-10-14 |
| E1 | Esbjerg, Denmark | — | Verena (planned, RFS 2028) | E1: https://www.submarinecablemap.com/api/v3/landing-point/esbjerg-denmark.json, accessed 2026-10-14 |
| E1 | Fano, Denmark | — | Hronn | E1: https://www.submarinecablemap.com/api/v3/landing-point/fano-denmark.json, accessed 2026-10-14 |
| E1 | Gedser, Denmark | — | Baltica, Elektra-GlobalConnect 1 (GC1), Germany-Denmark 3, GlobalConnect-KPN | E1: https://www.submarinecablemap.com/api/v3/landing-point/gedser-denmark.json, accessed 2026-10-14 |
| E1 | Hanstholm, Denmark | — | Havsil | E1: https://www.submarinecablemap.com/api/v3/landing-point/hanstholm-denmark.json, accessed 2026-10-14 |
| E1 | Hasle, Denmark | — | GlobalConnect Aurora | E1: https://www.submarinecablemap.com/api/v3/landing-point/hasle-denmark.json, accessed 2026-10-14 |
| E1 | Helsingør, Denmark | — | Denmark-Sweden 18, Scandinavian Ring North | E1: https://www.submarinecablemap.com/api/v3/landing-point/helsingr-denmark.json, accessed 2026-10-14 |
| E1 | Hirtshals, Denmark | — | Skagenfiber West | E1: https://www.submarinecablemap.com/api/v3/landing-point/hirtshals-denmark.json, accessed 2026-10-14 |
| E1 | Houstrup, Denmark | — | Havhingsten/North Sea Connect (NSC) | E1: https://www.submarinecablemap.com/api/v3/landing-point/houstrup-denmark.json, accessed 2026-10-14 |
| E1 | Juelsminde, Denmark | — | GlobalConnect 6 (GC6) | E1: https://www.submarinecablemap.com/api/v3/landing-point/juelsminde-denmark.json, accessed 2026-10-14 |
| E1 | Korsor, Denmark | — | GlobalConnect 3 (GC3) | E1: https://www.submarinecablemap.com/api/v3/landing-point/korsor-denmark.json, accessed 2026-10-14 |
| E1 | Laeso, Denmark | — | Energinet Laeso-Varberg, Energinet Lyngsa-Laeso | E1: https://www.submarinecablemap.com/api/v3/landing-point/laeso-denmark.json, accessed 2026-10-14 |
| E1 | Lyngsa, Denmark | — | Energinet Lyngsa-Laeso, Kattegat 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/lyngsa-denmark.json, accessed 2026-10-14 |
| E1 | Nybor, Denmark | — | GlobalConnect 3 (GC3) | E1: https://www.submarinecablemap.com/api/v3/landing-point/nybor-denmark.json, accessed 2026-10-14 |
| E1 | Osterby, Denmark | — | Kattegat 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/osterby-denmark.json, accessed 2026-10-14 |
| E1 | Pedersker, Denmark | — | Baltica | E1: https://www.submarinecablemap.com/api/v3/landing-point/pedersker-denmark.json, accessed 2026-10-14 |
| E1 | Rodbyhavn, Denmark | — | Fehmarn Bält | E1: https://www.submarinecablemap.com/api/v3/landing-point/rodbyhavn-denmark.json, accessed 2026-10-14 |
| E1 | Rødvig, Denmark | — | Rønne-Rødvig | E1: https://www.submarinecablemap.com/api/v3/landing-point/rdvig-denmark.json, accessed 2026-10-14 |
| E1 | Rønne, Denmark | — | GlobalConnect Aurora, Rønne-Rødvig | E1: https://www.submarinecablemap.com/api/v3/landing-point/rnne-denmark.json, accessed 2026-10-14 |
| E1 | Saeby, Denmark | — | GlobalConnect 2 (GC2), Kattegat Cable (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/saeby-denmark.json, accessed 2026-10-14 |
| E1 | South Arne, Denmark | — | CANTAT-3 | E1: https://www.submarinecablemap.com/api/v3/landing-point/south-arne-denmark.json, accessed 2026-10-14 |
| E1 | Tejn, Denmark | — | GlobalConnect Aurora | E1: https://www.submarinecablemap.com/api/v3/landing-point/tejn-denmark.json, accessed 2026-10-14 |
| E1 | Tjele, Denmark | — | Skagerrak 4 | E1: https://www.submarinecablemap.com/api/v3/landing-point/tjele-denmark.json, accessed 2026-10-14 |
| E1 | TotalEnergies Halfdan, Denmark | — | Hronn | E1: https://www.submarinecablemap.com/api/v3/landing-point/totalenergies-halfdan-denmark.json, accessed 2026-10-14 |
| E1 | TotalEnergies Tyra, Denmark | — | Hronn | E1: https://www.submarinecablemap.com/api/v3/landing-point/totalenergies-tyra-denmark.json, accessed 2026-10-14 |
| E1 | Tuborg, Denmark | — | Danica North | E1: https://www.submarinecablemap.com/api/v3/landing-point/tuborg-denmark.json, accessed 2026-10-14 |
| E1 | Tyra, Denmark | — | CANTAT-3 | E1: https://www.submarinecablemap.com/api/v3/landing-point/tyra-denmark.json, accessed 2026-10-14 |
| E1 | Valdemar, Denmark | — | CANTAT-3 | E1: https://www.submarinecablemap.com/api/v3/landing-point/valdemar-denmark.json, accessed 2026-10-14 |
| E1 | Vestero, Denmark | — | Kattegat 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/vestero-denmark.json, accessed 2026-10-14 |
| E2 | DE-CIX Copenhagen | Copenhagen | https://www.de-cix.net/en/locations/copenhagen | E2: https://www.peeringdb.com/ix/4043, accessed 2026-10-14 |
| E2 | DE-CIX Esbjerg | Esbjerg | https://www.de-cix.net/en/locations/esbjerg | E2: https://www.peeringdb.com/ix/4069, accessed 2026-10-14 |
| E2 | DIX | Copenhagen | http://www.dix.dk | E2: https://www.peeringdb.com/ix/78, accessed 2026-10-14 |
| E2 | LabIX | Copenhagen | https://ix.labitat.dk | E2: https://www.peeringdb.com/ix/4193, accessed 2026-10-14 |
| E2 | Netnod Copenhagen BLUE -- MTU9K | Malmo / Copenhagen | http://www.netnod.se | E2: https://www.peeringdb.com/ix/2868, accessed 2026-10-14 |
| E2 | Netnod Copenhagen GREEN -- MTU9K | Malmo / Copenhagen | http://www.netnod.se | E2: https://www.peeringdb.com/ix/193, accessed 2026-10-14 |
| E2 | NorthIX | Copenhagen | https://northix.dk | E2: https://www.peeringdb.com/ix/4154, accessed 2026-10-14 |
| E2 | STHIX - Copenhagen | Copenhagen | http://www.sthix.net | E2: https://www.peeringdb.com/ix/1869, accessed 2026-10-14 |

Counts: E1 34 (in service 33, planned-only 1, unverified 0), E2 8, E3 0; no-landing no; single-landing no; single-exchange no.

## Estonia (EE)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Kihelkonna, Estonia | — | Mjolner East (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/kihelkonna-estonia.json, accessed 2026-10-14 |
| E1 | Kärdla, Estonia | — | Sweden-Estonia (EE-S 1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/krdla-estonia.json, accessed 2026-10-14 |
| E1 | Meremöisa, Estonia | — | Finland-Estonia 3 (EESF-3) | E1: https://www.submarinecablemap.com/api/v3/landing-point/meremisa-estonia.json, accessed 2026-10-14 |
| E1 | Tallinn, Estonia | — | Baltic Sea Submarine Cable, E-FINEST, Finland-Estonia 2 (EESF-2), Finland Estonia Connection 1 (FEC-1), Finland Estonia Connection 2 (FEC-2), Mjolner East (planned, RFS 2027), Sweden-Estonia (EE-S 1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/tallinn-estonia.json, accessed 2026-10-14 |
| E2 | IIX Estonia | Tallinn | http://iix.ee | E2: https://www.peeringdb.com/ix/3751, accessed 2026-10-14 |
| E2 | PITER-IX Tallinn | Tallinn | https://piter-ix.eu | E2: https://www.peeringdb.com/ix/3018, accessed 2026-10-14 |
| E2 | RTIX | Tallinn | https://www.ria.ee/en/state-information-system/state-network-services/data-communication-services-state-network | E2: https://www.peeringdb.com/ix/538, accessed 2026-10-14 |
| E2 | TLLIX | Tallinn | http://www.tllix.net | E2: https://www.peeringdb.com/ix/190, accessed 2026-10-14 |

Counts: E1 4 (in service 3, planned-only 1, unverified 0), E2 4, E3 0; no-landing no; single-landing no; single-exchange no.

## Finland (FI)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Espoo, Finland | — | E-FINEST, Eastern Light Sweden-Finland II (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/espoo-finland.json, accessed 2026-10-14 |
| E1 | Hamnäs, Finland | — | STO-HEL-One | E1: https://www.submarinecablemap.com/api/v3/landing-point/hamns-finland.json, accessed 2026-10-14 |
| E1 | Hanko, Finland | — | BCS North - Phase 1, C-Lion1, Eastern Light Sweden-Finland I, Eastern Light Sweden-Finland II (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/hanko-finland.json, accessed 2026-10-14 |
| E1 | Haradsholm, Finland | — | BCS North - Phase 1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/haradsholm-finland.json, accessed 2026-10-14 |
| E1 | Helsinki, Finland | — | Baltic Sea Submarine Cable, BCS North - Phase 1, BCS North - Phase 2, C-Lion1, Eastern Light Sweden-Finland I, Finland-Estonia 2 (EESF-2), Finland-Estonia 3 (EESF-3), Finland Estonia Connection 1 (FEC-1), Finland Estonia Connection 2 (FEC-2), Mjolner East (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/helsinki-finland.json, accessed 2026-10-14 |
| E1 | Kotka, Finland | — | BCS North - Phase 2, Eastern Light Sweden-Finland I | E1: https://www.submarinecablemap.com/api/v3/landing-point/kotka-finland.json, accessed 2026-10-14 |
| E1 | Kökar, Finland | — | Eastern Light Sweden-Finland II (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/kkar-finland.json, accessed 2026-10-14 |
| E1 | Lokalahti, Finland | — | Mjolner West (planned, RFS 2027), STO-HEL-One | E1: https://www.submarinecablemap.com/api/v3/landing-point/lokalahti-finland.json, accessed 2026-10-14 |
| E1 | Mariehamn, Finland | — | BCS North - Phase 1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/mariehamn-finland.json, accessed 2026-10-14 |
| E1 | Skatörarna, Finland | — | STO-HEL-One | E1: https://www.submarinecablemap.com/api/v3/landing-point/skatrarna-finland.json, accessed 2026-10-14 |
| E1 | Vaasa, Finland | — | Botnia | E1: https://www.submarinecablemap.com/api/v3/landing-point/vaasa-finland.json, accessed 2026-10-14 |
| E2 | DE-CIX Helsinki | Helsinki | https://www.de-cix.net/en/locations/helsinki | E2: https://www.peeringdb.com/ix/4044, accessed 2026-10-14 |
| E2 | Equinix Helsinki | Helsinki | https://www.equinix.fi/services/interconnection-connectivity/internet-exchange | E2: https://www.peeringdb.com/ix/1464, accessed 2026-10-14 |
| E2 | FICIX 1 (Espoo) | Espoo | https://www.ficix.fi | E2: https://www.peeringdb.com/ix/1332, accessed 2026-10-14 |
| E2 | FICIX 1 (Espoo) IPv6 MTU 9000 | Espoo | https://www.ficix.fi | E2: https://www.peeringdb.com/ix/2963, accessed 2026-10-14 |
| E2 | FICIX 2 (Helsinki) | Helsinki | https://www.ficix.fi | E2: https://www.peeringdb.com/ix/98, accessed 2026-10-14 |
| E2 | FICIX 2 (Helsinki) IPv6 MTU 9000 | Helsinki | https://www.ficix.fi | E2: https://www.peeringdb.com/ix/2853, accessed 2026-10-14 |
| E2 | FICIX 3 (Oulu) | Oulu | http://www.ficix.fi | E2: https://www.peeringdb.com/ix/492, accessed 2026-10-14 |
| E2 | FICIX 3 (Oulu) IPv6 MTU 9000 | Oulu | http://www.ficix.fi | E2: https://www.peeringdb.com/ix/2904, accessed 2026-10-14 |
| E2 | IXP FI HEL | Helsinki | https://www.ixp.cat | E2: https://www.peeringdb.com/ix/2700, accessed 2026-10-14 |
| E2 | Netnod Helsinki BLUE -- MTU9K | Helsinki | http://www.netnod.se | E2: https://www.peeringdb.com/ix/3712, accessed 2026-10-14 |
| E2 | Netnod Helsinki GREEN -- MTU9K | Helsinki | https://www.netnod.se | E2: https://www.peeringdb.com/ix/3713, accessed 2026-10-14 |
| E2 | PITER-IX Helsinki | Helsinki | http://www.piter-ix.eu | E2: https://www.peeringdb.com/ix/3299, accessed 2026-10-14 |
| E2 | TREX Tampere | Tampere | http://www.trex.fi | E2: https://www.peeringdb.com/ix/328, accessed 2026-10-14 |
| E2 | TREX turku | Turku | https://www.trex.fi/service/turku.html | E2: https://www.peeringdb.com/ix/4621, accessed 2026-10-14 |

Counts: E1 11 (in service 10, planned-only 1, unverified 0), E2 14, E3 0; no-landing no; single-landing no; single-exchange no.

## France (FR)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Ajaccio, France | — | Corse-Continent 5 (CC5), Medloop | E1: https://www.submarinecablemap.com/api/v3/landing-point/ajaccio-france.json, accessed 2026-10-14 |
| E1 | Bastia, France | — | Blue | E1: https://www.submarinecablemap.com/api/v3/landing-point/bastia-france.json, accessed 2026-10-14 |
| E1 | Bonifacio, France | — | SARCO | E1: https://www.submarinecablemap.com/api/v3/landing-point/bonifacio-france.json, accessed 2026-10-14 |
| E1 | Calvi, France | — | Calvi-St. Florent | E1: https://www.submarinecablemap.com/api/v3/landing-point/calvi-france.json, accessed 2026-10-14 |
| E1 | Cannes, France | — | Corse-Continent 4 (CC4) | E1: https://www.submarinecablemap.com/api/v3/landing-point/cannes-france.json, accessed 2026-10-14 |
| E1 | Cayeux-sur-Mer, France | — | Circe South, Q&E South | E1: https://www.submarinecablemap.com/api/v3/landing-point/cayeux-sur-mer-france.json, accessed 2026-10-14 |
| E1 | Héliopolis, France | — | Îles d'Hyères Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/hliopolis-france.json, accessed 2026-10-14 |
| E1 | La Seyne, France | — | Corse-Continent 5 (CC5) | E1: https://www.submarinecablemap.com/api/v3/landing-point/la-seyne-france.json, accessed 2026-10-14 |
| E1 | La Tour Fondue, France | — | Îles d'Hyères Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/la-tour-fondue-france.json, accessed 2026-10-14 |
| E1 | Lannion, France | — | Apollo, High-capacity Undersea Guernsey Optical-fibre (HUGO) | E1: https://www.submarinecablemap.com/api/v3/landing-point/lannion-france.json, accessed 2026-10-14 |
| E1 | Le Lavandou, France | — | Îles d'Hyères Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/le-lavandou-france.json, accessed 2026-10-14 |
| E1 | Le Porge, France | — | Amitie | E1: https://www.submarinecablemap.com/api/v3/landing-point/le-porge-france.json, accessed 2026-10-14 |
| E1 | L’Île-Rousse, France | — | Corse-Continent 4 (CC4) | E1: https://www.submarinecablemap.com/api/v3/landing-point/lle-rousse-france.json, accessed 2026-10-14 |
| E1 | Marseille, France | — | 2Africa, Africa-1 (planned, RFS 2027), Asia Africa Europe-1 (AAE-1), Atlas Offshore, Blue, EMC West-2 (planned, RFS 2027), Hawk, IMEWE, India Europe Xpress (IEX) (planned, RFS 2027), Med Cable Network, Medloop, Medusa Submarine Cable System, PEACE Cable, SeaMeWe-4, SeaMeWe-6 (planned, RFS 2027), TE North/TGN-Eurasia/SEACOM/Alexandros/Medex | E1: https://www.submarinecablemap.com/api/v3/landing-point/marseille-france.json, accessed 2026-10-14 |
| E1 | Penmarch, France | — | Africa Coast to Europe (ACE) | E1: https://www.submarinecablemap.com/api/v3/landing-point/penmarch-france.json, accessed 2026-10-14 |
| E1 | Petit Perello, France | — | Groix 4 | E1: https://www.submarinecablemap.com/api/v3/landing-point/petit-perello-france.json, accessed 2026-10-14 |
| E1 | Plerin, France | — | FLAG Atlantic-1 (FA-1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/plerin-france.json, accessed 2026-10-14 |
| E1 | Porquerolles, France | — | Îles d'Hyères Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/porquerolles-france.json, accessed 2026-10-14 |
| E1 | Port Nâl, France | — | Groix 4 | E1: https://www.submarinecablemap.com/api/v3/landing-point/port-nl-france.json, accessed 2026-10-14 |
| E1 | Port-Cros, France | — | Îles d'Hyères Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/port-cros-france.json, accessed 2026-10-14 |
| E1 | Propriano, France | — | Ruppione-Isolella | E1: https://www.submarinecablemap.com/api/v3/landing-point/propriano-france.json, accessed 2026-10-14 |
| E1 | Ruppione, France | — | Ruppione-Isolella | E1: https://www.submarinecablemap.com/api/v3/landing-point/ruppione-france.json, accessed 2026-10-14 |
| E1 | Saint-Hilaire-de-Riez, France | — | Dunant | E1: https://www.submarinecablemap.com/api/v3/landing-point/saint-hilaire-de-riez-france.json, accessed 2026-10-14 |
| E1 | St. Florent, France | — | Calvi-St. Florent | E1: https://www.submarinecablemap.com/api/v3/landing-point/st-florent-france.json, accessed 2026-10-14 |
| E1 | Surville, France | — | INGRID | E1: https://www.submarinecablemap.com/api/v3/landing-point/surville-france.json, accessed 2026-10-14 |
| E1 | Toulon, France | — | SeaMeWe-5 | E1: https://www.submarinecablemap.com/api/v3/landing-point/toulon-france.json, accessed 2026-10-14 |
| E1 | Veules-les-Roses, France | — | CrossChannel Fibre | E1: https://www.submarinecablemap.com/api/v3/landing-point/veules-les-roses-france.json, accessed 2026-10-14 |
| E2 | 1-FR FREE | Paris | https://1-ix.eu/1fr | E2: https://www.peeringdb.com/ix/4994, accessed 2026-10-14 |
| E2 | Association HwHost | Paris | https://hwhost.fr | E2: https://www.peeringdb.com/ix/4461, accessed 2026-10-14 |
| E2 | AuvernIX | Clermont-Ferrand | http://www.auvernix.org | E2: https://www.peeringdb.com/ix/1019, accessed 2026-10-14 |
| E2 | BreizhIX | Rennes | https://www.breizh-ix.net | E2: https://www.peeringdb.com/ix/1670, accessed 2026-10-14 |
| E2 | BrestIX | Brest | http://brestix.bzh | E2: https://www.peeringdb.com/ix/2726, accessed 2026-10-14 |
| E2 | BéarnIX | Pau | https://bearnix.fr | E2: https://www.peeringdb.com/ix/3384, accessed 2026-10-14 |
| E2 | DE-CIX Marseille | Marseille | https://www.de-cix.net/locations/marseille | E2: https://www.peeringdb.com/ix/1149, accessed 2026-10-14 |
| E2 | Equinix Paris | Paris | https://www.equinix-ix.fr | E2: https://www.peeringdb.com/ix/255, accessed 2026-10-14 |
| E2 | ERA-IX Paris | Paris | https://www.era-ix.com | E2: https://www.peeringdb.com/ix/4985, accessed 2026-10-14 |
| E2 | EuroRhine-IX | Strasbourg | https://www.er-ix.net | E2: https://www.peeringdb.com/ix/4968, accessed 2026-10-14 |
| E2 | France-IX AURA | Lyon and Grenoble | https://www.franceix.net/en/infrastructure/our-exchange-points-in-france/france-ix-lyon | E2: https://www.peeringdb.com/ix/69, accessed 2026-10-14 |
| E2 | France-IX Bordeaux | Bordeaux | https://www.franceix.net/en/infrastructure/our-exchange-points-in-france/france-ix-bordeaux | E2: https://www.peeringdb.com/ix/4693, accessed 2026-10-14 |
| E2 | France-IX Lille | Lille | https://www.franceix.net/en/infrastructure/our-exchange-points-in-france/france-ix-lille | E2: https://www.peeringdb.com/ix/4005, accessed 2026-10-14 |
| E2 | France-IX Marseille | Marseille | https://www.franceix.net/en/infrastructure/our-exchange-points-in-france/france-ix-marseille | E2: https://www.peeringdb.com/ix/880, accessed 2026-10-14 |
| E2 | France-IX Paris | Paris | https://www.franceix.net/en/infrastructure/our-exchange-points-in-france/france-ix-paris | E2: https://www.peeringdb.com/ix/359, accessed 2026-10-14 |
| E2 | France-IX Paris Essentiel | Paris | https://www.franceix.net/en/services/peering/peering-essentiel | E2: https://www.peeringdb.com/ix/5040, accessed 2026-10-14 |
| E2 | France-IX Toulouse | Toulouse | https://www.franceix.net/en/infrastructure/our-exchange-points-in-france/france-ix-toulouse | E2: https://www.peeringdb.com/ix/4162, accessed 2026-10-14 |
| E2 | Hopus | Paris, Lyon, Marseille, Geneva, Zurich, Amsterdam, Frankfurt | https://hopus.net | E2: https://www.peeringdb.com/ix/1320, accessed 2026-10-14 |
| E2 | ixFabric - Lyon | Lyon | https://ixfabric.net | E2: https://www.peeringdb.com/ix/4245, accessed 2026-10-14 |
| E2 | ixFabric - Paris | Paris | https://ixfabric.net | E2: https://www.peeringdb.com/ix/3913, accessed 2026-10-14 |
| E2 | Lillix | Lille | http://www.lillix.fr | E2: https://www.peeringdb.com/ix/881, accessed 2026-10-14 |
| E2 | MPLIX | Montpellier | https://sudix.fr | E2: https://www.peeringdb.com/ix/4652, accessed 2026-10-14 |
| E2 | nine | Amsterdam, Bordeaux, Frankfurt, Genève, Lille, London, Lyon, Marseille, Milano, Montpellier, Paris, Zurich | https://nine-ix.net | E2: https://www.peeringdb.com/ix/4705, accessed 2026-10-14 |
| E2 | nine - six in Paris | Paris | https://nine-ix.net | E2: https://www.peeringdb.com/ix/5011, accessed 2026-10-14 |
| E2 | NormandIX | Normandy | https://www.criann.fr/reseau-syvik | E2: https://www.peeringdb.com/ix/1040, accessed 2026-10-14 |
| E2 | Ouest.Network | Nantes | https://ouest.network | E2: https://www.peeringdb.com/ix/3436, accessed 2026-10-14 |
| E2 | SFINX | Paris | http://www.sfinx.fr | E2: https://www.peeringdb.com/ix/34, accessed 2026-10-14 |

Counts: E1 27 (in service 27, planned-only 0, unverified 0), E2 27, E3 0; no-landing no; single-landing no; single-exchange no.

## Germany (DE)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Friedrichshafen, Germany | — | Konstanz-Friedrichshafen | E1: https://www.submarinecablemap.com/api/v3/landing-point/friedrichshafen-germany.json, accessed 2026-10-14 |
| E1 | Konstanz, Germany | — | Konstanz-Friedrichshafen, Konstanz-Meersburg | E1: https://www.submarinecablemap.com/api/v3/landing-point/konstanz-germany.json, accessed 2026-10-14 |
| E1 | Markgrafenheide, Germany | — | Germany-Denmark 3 | E1: https://www.submarinecablemap.com/api/v3/landing-point/markgrafenheide-germany.json, accessed 2026-10-14 |
| E1 | Meersburg, Germany | — | Konstanz-Meersburg | E1: https://www.submarinecablemap.com/api/v3/landing-point/meersburg-germany.json, accessed 2026-10-14 |
| E1 | Puttgarden, Germany | — | Fehmarn Bält | E1: https://www.submarinecablemap.com/api/v3/landing-point/puttgarden-germany.json, accessed 2026-10-14 |
| E1 | Rostock, Germany | — | C-Lion1, Elektra-GlobalConnect 1 (GC1), GlobalConnect-KPN | E1: https://www.submarinecablemap.com/api/v3/landing-point/rostock-germany.json, accessed 2026-10-14 |
| E1 | Sassnitz, Germany | — | GlobalConnect Aurora | E1: https://www.submarinecablemap.com/api/v3/landing-point/sassnitz-germany.json, accessed 2026-10-14 |
| E1 | Sylt, Germany | — | Atlantic Crossing-1 (AC-1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/sylt-germany.json, accessed 2026-10-14 |
| E1 | Wilhelmshaven, Germany | — | IOEMA-1 (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/wilhelmshaven-germany.json, accessed 2026-10-14 |
| E2 | 1-DE FREE | Frankfurt | https://1-ix.eu/1de | E2: https://www.peeringdb.com/ix/4917, accessed 2026-10-14 |
| E2 | BCIX | Berlin | https://www.bcix.de | E2: https://www.peeringdb.com/ix/87, accessed 2026-10-14 |
| E2 | BREM-IX | Bremen | https://brem-ix.net | E2: https://www.peeringdb.com/ix/796, accessed 2026-10-14 |
| E2 | BW-IX Karlsruhe | Karlsruhe | http://www.bw-ix.net | E2: https://www.peeringdb.com/ix/1421, accessed 2026-10-14 |
| E2 | CentralIX | Bremen | http://www.centralIX.net | E2: https://www.peeringdb.com/ix/1151, accessed 2026-10-14 |
| E2 | City-IX Frankfurt | Frankfurt | https://city-ix.net | E2: https://www.peeringdb.com/ix/4175, accessed 2026-10-14 |
| E2 | Community-IX | Berlin, Frankfurt | https://www.community-ix.de | E2: https://www.peeringdb.com/ix/1329, accessed 2026-10-14 |
| E2 | CSNIX - Gudow | Gudow | https://csn.solutions/ixp | E2: https://www.peeringdb.com/ix/4416, accessed 2026-10-14 |
| E2 | CSNIX - Hamburg | Hamburg | https://csn.solutions | E2: https://www.peeringdb.com/ix/4414, accessed 2026-10-14 |
| E2 | CSNIX - Hamburg RemotePeering | Hamburg | https://csn.solutions | E2: https://www.peeringdb.com/ix/4417, accessed 2026-10-14 |
| E2 | CSNIX - Kehrsen | Kehrsen | https://csn.solutions/ixp | E2: https://www.peeringdb.com/ix/4415, accessed 2026-10-14 |
| E2 | DD-IX | Dresden | https://dd-ix.net | E2: https://www.peeringdb.com/ix/4282, accessed 2026-10-14 |
| E2 | DE-CIX Dusseldorf | Düsseldorf | https://www.de-cix.net/locations/dusseldorf | E2: https://www.peeringdb.com/ix/1214, accessed 2026-10-14 |
| E2 | DE-CIX Frankfurt | Frankfurt | https://www.de-cix.net/en/locations/germany/frankfurt | E2: https://www.peeringdb.com/ix/31, accessed 2026-10-14 |
| E2 | DE-CIX Hamburg | Hamburg | https://www.de-cix.net/locations/hamburg | E2: https://www.peeringdb.com/ix/74, accessed 2026-10-14 |
| E2 | DE-CIX Leipzig | Leipzig | https://www.de-cix.net/en/locations/leipzig | E2: https://www.peeringdb.com/ix/4004, accessed 2026-10-14 |
| E2 | DE-CIX Munich | Munich | https://www.de-cix.net/locations/munich | E2: https://www.peeringdb.com/ix/248, accessed 2026-10-14 |
| E2 | DO-IX | Dortmund | https://www.do-ix.net | E2: https://www.peeringdb.com/ix/762, accessed 2026-10-14 |
| E2 | Electron IX | Frankfurt | https://network.usercloud.host/VIXP.html | E2: https://www.peeringdb.com/ix/4036, accessed 2026-10-14 |
| E2 | Equinix Frankfurt | Frankfurt | https://www.equinix.de/services/interconnection-connectivity/internet-exchange | E2: https://www.peeringdb.com/ix/1998, accessed 2026-10-14 |
| E2 | ERA-IX Frankfurt | Frankfurt | https://www.era-ix.com/frankfurt | E2: https://www.peeringdb.com/ix/4630, accessed 2026-10-14 |
| E2 | FIX Berlin | Berlin | https://fix-berlin.net | E2: https://www.peeringdb.com/ix/4367, accessed 2026-10-14 |
| E2 | FogIXP Frankfurt | Frankfurt | https://fogixp.org/our-ixps/frankfurt | E2: https://www.peeringdb.com/ix/4200, accessed 2026-10-14 |
| E2 | frankonIX | Nuremberg | https://frankonix.de | E2: https://www.peeringdb.com/ix/4503, accessed 2026-10-14 |
| E2 | Giganet IXN Frankfurt | Frankfurt | http://giganet.ua/en | E2: https://www.peeringdb.com/ix/4233, accessed 2026-10-14 |
| E2 | GL-IX | Düsseldorf | https://www.glix.net | E2: https://www.peeringdb.com/ix/4457, accessed 2026-10-14 |
| E2 | ixFabric - Berlin | Berlin | https://ixfabric.net | E2: https://www.peeringdb.com/ix/4842, accessed 2026-10-14 |
| E2 | ixFabric - Dusseldorf | Dusseldorf | https://ixfabric.net | E2: https://www.peeringdb.com/ix/3844, accessed 2026-10-14 |
| E2 | ixFabric - Frankfurt | Frankfurt | https://ixfabric.net | E2: https://www.peeringdb.com/ix/3829, accessed 2026-10-14 |
| E2 | IXP NUR | Nürnberg | https://www.ixp.cat | E2: https://www.peeringdb.com/ix/2706, accessed 2026-10-14 |
| E2 | KA-NIX | Karlsruhe | http://ka-nix.de | E2: https://www.peeringdb.com/ix/3280, accessed 2026-10-14 |
| E2 | KleyReX | Frankfurt | https://www.kleyrex.net | E2: https://www.peeringdb.com/ix/123, accessed 2026-10-14 |
| E2 | LOCIX DUSSELDORF | Dusseldorf | https://locix.online | E2: https://www.peeringdb.com/ix/2730, accessed 2026-10-14 |
| E2 | LOCIX FRANKFURT | Frankfurt am Main | https://locix.online | E2: https://www.peeringdb.com/ix/2084, accessed 2026-10-14 |
| E2 | Lynqia IX Berlin | Berlin | https://lynqia.company | E2: https://www.peeringdb.com/ix/4819, accessed 2026-10-14 |
| E2 | MAINPORT Peer-Exchange | Frankfurt am Main | https://mainport.one/#peer-exchange | E2: https://www.peeringdb.com/ix/4879, accessed 2026-10-14 |
| E2 | MegaIX Berlin | Berlin | https://www.megaport.com/services/internet-exchange | E2: https://www.peeringdb.com/ix/209, accessed 2026-10-14 |
| E2 | MegaIX Dusseldorf | Dusseldorf | https://www.megaport.com/services/internet-exchange | E2: https://www.peeringdb.com/ix/91, accessed 2026-10-14 |
| E2 | MegaIX Frankfurt | Frankfurt | https://www.megaport.com/services/internet-exchange | E2: https://www.peeringdb.com/ix/676, accessed 2026-10-14 |
| E2 | MegaIX Hamburg | Hamburg | https://www.megaport.com/services/internet-exchange | E2: https://www.peeringdb.com/ix/291, accessed 2026-10-14 |
| E2 | MegaIX Munich | Munich | https://www.megaport.com/services/internet-exchange | E2: https://www.peeringdb.com/ix/73, accessed 2026-10-14 |
| E2 | N-IX | Nürnberg | http://www.n-ix.net | E2: https://www.peeringdb.com/ix/135, accessed 2026-10-14 |
| E2 | NextIX | Global | https://my-noc.eu | E2: https://www.peeringdb.com/ix/5005, accessed 2026-10-14 |
| E2 | OpenCarrier OCIX | Duesseldorf | http://www.opencarrier.eu | E2: https://www.peeringdb.com/ix/170, accessed 2026-10-14 |
| E2 | Pfcloud IX | Frankfurt | https://ix.pfcloud.io | E2: https://www.peeringdb.com/ix/4410, accessed 2026-10-14 |
| E2 | PITER-IX Frankfurt | Frankfurt | https://piter-ix.eu | E2: https://www.peeringdb.com/ix/3739, accessed 2026-10-14 |
| E2 | Rottweiler Internet Exchange | Rottweil | https://www.rwix.net | E2: https://www.peeringdb.com/ix/2774, accessed 2026-10-14 |
| E2 | Ruhr-CIX | Ruhr Region | https://www.ruhr-cix.net | E2: https://www.peeringdb.com/ix/3405, accessed 2026-10-14 |
| E2 | SaarCix | Saarbrücken | https://www.saarcix.de | E2: https://www.peeringdb.com/ix/3572, accessed 2026-10-14 |
| E2 | SBIX Dusseldorf | Dusseldorf | https://www.securebit.ch/internet/exchange | E2: https://www.peeringdb.com/ix/3118, accessed 2026-10-14 |
| E2 | Schleyer-IX | Düsseldorf | https://www.schleyer-ix.com | E2: https://www.peeringdb.com/ix/4858, accessed 2026-10-14 |
| E2 | SmartIX | Frankfurt | https://as203446.net/smartix | E2: https://www.peeringdb.com/ix/4594, accessed 2026-10-14 |
| E2 | SON-IX | Wolfsburg | https://son-ix.net | E2: https://www.peeringdb.com/ix/4323, accessed 2026-10-14 |
| E2 | STACIX | Frankfurt | https://stacix.net | E2: https://www.peeringdb.com/ix/3211, accessed 2026-10-14 |
| E2 | Stuttgart-IX | Stuttgart | http://www.stuttgart-ix.de | E2: https://www.peeringdb.com/ix/212, accessed 2026-10-14 |
| E2 | TievoluIX | Frankfurt | https://tievolu.net/joining-policy | E2: https://www.peeringdb.com/ix/4779, accessed 2026-10-14 |
| E2 | TMW-iX | Frankfurt am Main | https://tmw-ix.t-w.dev | E2: https://www.peeringdb.com/ix/4401, accessed 2026-10-14 |
| E2 | United Peering - UP-IXP | Wuppertal | https://united-peering.net | E2: https://www.peeringdb.com/ix/1156, accessed 2026-10-14 |
| E2 | VexIX | Frankfurt | https://vexixp.de | E2: https://www.peeringdb.com/ix/4946, accessed 2026-10-14 |

Counts: E1 9 (in service 8, planned-only 1, unverified 0), E2 59, E3 0; no-landing no; single-landing no; single-exchange no.

## Greece (EL)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Aethos, Greece | — | Italy-Greece 1 (IG-1), Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/aethos-greece.json, accessed 2026-10-14 |
| E1 | Agios Sostis, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/agios-sostis-greece.json, accessed 2026-10-14 |
| E1 | Athens, Greece | — | EMC West-1 (planned, RFS 2027), MedNautilus Submarine System, Medusa Submarine Cable System, Thetis Express (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/athens-greece.json, accessed 2026-10-14 |
| E1 | Baxedes, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/baxedes-greece.json, accessed 2026-10-14 |
| E1 | Chania, Greece | — | ANDROMEDA (planned), Asia Africa Europe-1 (AAE-1), Blue, MedNautilus Submarine System, Silphium | E1: https://www.submarinecablemap.com/api/v3/landing-point/chania-greece.json, accessed 2026-10-14 |
| E1 | Corfu, Greece | — | Adria-1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/corfu-greece.json, accessed 2026-10-14 |
| E1 | Ermoupoli, Greece | — | Cyclades A, Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/ermoupoli-greece.json, accessed 2026-10-14 |
| E1 | Filizi, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/filizi-greece.json, accessed 2026-10-14 |
| E1 | Heraklion, Greece | — | Thetis Express (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/heraklion-greece.json, accessed 2026-10-14 |
| E1 | Kalafati, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/kalafati-greece.json, accessed 2026-10-14 |
| E1 | Kardamena, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/kardamena-greece.json, accessed 2026-10-14 |
| E1 | Kavos, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/kavos-greece.json, accessed 2026-10-14 |
| E1 | Kochilari, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/kochilari-greece.json, accessed 2026-10-14 |
| E1 | Kokkini, Greece | — | OTEGLOBE Kokkini-Bari | E1: https://www.submarinecablemap.com/api/v3/landing-point/kokkini-greece.json, accessed 2026-10-14 |
| E1 | Kontokali, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/kontokali-greece.json, accessed 2026-10-14 |
| E1 | Korakia, Greece | — | Apollo East and West | E1: https://www.submarinecablemap.com/api/v3/landing-point/korakia-greece.json, accessed 2026-10-14 |
| E1 | Kremasti, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/kremasti-greece.json, accessed 2026-10-14 |
| E1 | Lavrio, Greece | — | Cyclades A | E1: https://www.submarinecablemap.com/api/v3/landing-point/lavrio-greece.json, accessed 2026-10-14 |
| E1 | Marlas, Greece | — | Cyclades A | E1: https://www.submarinecablemap.com/api/v3/landing-point/marlas-greece.json, accessed 2026-10-14 |
| E1 | Milos, Greece | — | Thetis Express (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/milos-greece.json, accessed 2026-10-14 |
| E1 | Mykonos, Greece | — | Cyclades A, Cyclades B, Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/mykonos-greece.json, accessed 2026-10-14 |
| E1 | Naousa, Greece | — | Cyclades A, Cyclades B, Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/naousa-greece.json, accessed 2026-10-14 |
| E1 | Naxos, Greece | — | Cyclades B, Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/naxos-greece.json, accessed 2026-10-14 |
| E1 | Neapoli, Greece | — | Minoas East and West | E1: https://www.submarinecablemap.com/api/v3/landing-point/neapoli-greece.json, accessed 2026-10-14 |
| E1 | Nopigeia, Greece | — | Minoas East and West | E1: https://www.submarinecablemap.com/api/v3/landing-point/nopigeia-greece.json, accessed 2026-10-14 |
| E1 | Pachi, Greece | — | Apollo East and West | E1: https://www.submarinecablemap.com/api/v3/landing-point/pachi-greece.json, accessed 2026-10-14 |
| E1 | Perivolos, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/perivolos-greece.json, accessed 2026-10-14 |
| E1 | Pirgaki, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/pirgaki-greece.json, accessed 2026-10-14 |
| E1 | Plataria, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/plataria-greece.json, accessed 2026-10-14 |
| E1 | Plimmiri, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/plimmiri-greece.json, accessed 2026-10-14 |
| E1 | Porto Rafti, Greece | — | Vodafone Greece Domestic | E1: https://www.submarinecablemap.com/api/v3/landing-point/porto-rafti-greece.json, accessed 2026-10-14 |
| E1 | Preveza, Greece | — | Ionian | E1: https://www.submarinecablemap.com/api/v3/landing-point/preveza-greece.json, accessed 2026-10-14 |
| E1 | Sitia, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/sitia-greece.json, accessed 2026-10-14 |
| E1 | Syros, Greece | — | Vodafone Greece Domestic | E1: https://www.submarinecablemap.com/api/v3/landing-point/syros-greece.json, accessed 2026-10-14 |
| E1 | Tinos, Greece | — | Thetis | E1: https://www.submarinecablemap.com/api/v3/landing-point/tinos-greece.json, accessed 2026-10-14 |
| E1 | Tympaki, Greece | — | 2Africa, EMC West-1 (planned, RFS 2027), EMC West-2 (planned, RFS 2027), India Europe Xpress (IEX) (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/tympaki-greece.json, accessed 2026-10-14 |
| E2 | DE-CIX Athens | Athens | https://www.de-cix.net/en/locations/athens | E2: https://www.peeringdb.com/ix/3184, accessed 2026-10-14 |
| E2 | Free-IX Greece | Thessaloniki & Athens | https://free-ix.gr | E2: https://www.peeringdb.com/ix/4493, accessed 2026-10-14 |
| E2 | GR-IX::Athens | Athens | http://www.gr-ix.gr | E2: https://www.peeringdb.com/ix/347, accessed 2026-10-14 |
| E2 | GR-IX::Thessaloniki | Thessaloniki | http://www.gr-ix.gr | E2: https://www.peeringdb.com/ix/2386, accessed 2026-10-14 |
| E2 | MIX Thessaloniki | Thessaloniki | https://www.mix-it.net | E2: https://www.peeringdb.com/ix/4797, accessed 2026-10-14 |
| E2 | NetIX Greece | Thessaloniki / Athens | https://www.netix.net/peering-services/netixs-regional-ixps | E2: https://www.peeringdb.com/ix/4310, accessed 2026-10-14 |
| E2 | NVL-IX | Athens | https://nvl-ix.com | E2: https://www.peeringdb.com/ix/4775, accessed 2026-10-14 |
| E2 | THESS-IX | Thessaloniki | https://www.thess-ix.net | E2: https://www.peeringdb.com/ix/3283, accessed 2026-10-14 |

Counts: E1 36 (in service 34, planned-only 2, unverified 0), E2 8, E3 0; no-landing no; single-landing no; single-exchange no.

## Hungary (HU)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | (none on the map) | — | — | none: searched 2026-10-14 |
| E2 | BIX | Budapest | https://bix.hu/en | E2: https://www.peeringdb.com/ix/55, accessed 2026-10-14 |

Counts: E1 0 (in service 0, planned-only 0, unverified 0), E2 1, E3 0; no-landing yes; single-landing no; single-exchange yes.

## Ireland (IE)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Ballinesker, Ireland | — | Pan European Crossing (UK-Ireland) | E1: https://www.submarinecablemap.com/api/v3/landing-point/ballinesker-ireland.json, accessed 2026-10-14 |
| E1 | Ballygrangans, Ireland | — | Pan European Crossing (UK-Ireland) | E1: https://www.submarinecablemap.com/api/v3/landing-point/ballygrangans-ireland.json, accessed 2026-10-14 |
| E1 | Clonshaugh, Ireland | — | Emerald Bridge Fibres | E1: https://www.submarinecablemap.com/api/v3/landing-point/clonshaugh-ireland.json, accessed 2026-10-14 |
| E1 | Cork, Ireland | — | EXA Express | E1: https://www.submarinecablemap.com/api/v3/landing-point/cork-ireland.json, accessed 2026-10-14 |
| E1 | Dublin, Ireland | — | CeltixConnect-1 (CC-1), EXA North and South, Sirius South | E1: https://www.submarinecablemap.com/api/v3/landing-point/dublin-ireland.json, accessed 2026-10-14 |
| E1 | Galway, Ireland | — | IRIS | E1: https://www.submarinecablemap.com/api/v3/landing-point/galway-ireland.json, accessed 2026-10-14 |
| E1 | Killala, Ireland | — | AEC-1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/killala-ireland.json, accessed 2026-10-14 |
| E1 | Kilmore Quay, Ireland | — | Beaufort (planned, RFS 2027), Solas | E1: https://www.submarinecablemap.com/api/v3/landing-point/kilmore-quay-ireland.json, accessed 2026-10-14 |
| E1 | Lecanvey, Ireland | — | Havfrue/AEC-2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/lecanvey-ireland.json, accessed 2026-10-14 |
| E1 | LoughShinny, Ireland | — | Havhingsten/CeltixConnect-2 (CC-2) | E1: https://www.submarinecablemap.com/api/v3/landing-point/loughshinny-ireland.json, accessed 2026-10-14 |
| E1 | Lusk, Ireland | — | Geo-Eirgrid | E1: https://www.submarinecablemap.com/api/v3/landing-point/lusk-ireland.json, accessed 2026-10-14 |
| E1 | Owenahincha, Ireland | — | Fastnet (planned, RFS 2028) | E1: https://www.submarinecablemap.com/api/v3/landing-point/owenahincha-ireland.json, accessed 2026-10-14 |
| E1 | Portrane, Ireland | — | Rockabill | E1: https://www.submarinecablemap.com/api/v3/landing-point/portrane-ireland.json, accessed 2026-10-14 |
| E1 | Sandymount, Ireland | — | ESAT-2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/sandymount-ireland.json, accessed 2026-10-14 |
| E2 | Equinix Dublin | Dublin | http://www.equinix.ie/services/interconnection-connectivity/internet-exchange | E2: https://www.peeringdb.com/ix/1926, accessed 2026-10-14 |
| E2 | ExWest | Galway | http://www.exwest.net | E2: https://www.peeringdb.com/ix/316, accessed 2026-10-14 |
| E2 | INEX Cork | Cork | https://www.inex.ie | E2: https://www.peeringdb.com/ix/1262, accessed 2026-10-14 |
| E2 | INEX LAN1 | Dublin | https://www.inex.ie | E2: https://www.peeringdb.com/ix/48, accessed 2026-10-14 |
| E2 | INEX LAN2 | Dublin | https://www.inex.ie | E2: https://www.peeringdb.com/ix/387, accessed 2026-10-14 |
| E2 | MegaIX Dublin | Dublin | https://www.megaport.com | E2: https://www.peeringdb.com/ix/4710, accessed 2026-10-14 |

Counts: E1 14 (in service 13, planned-only 1, unverified 0), E2 6, E3 0; no-landing no; single-landing no; single-exchange no.

## Italy (IT)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Alicudi Porto, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/alicudi-porto-italy.json, accessed 2026-10-14 |
| E1 | Bari, Italy | — | Asia Africa Europe-1 (AAE-1), Italy-Albania, Jonah, OTEGLOBE Kokkini-Bari | E1: https://www.submarinecablemap.com/api/v3/landing-point/bari-italy.json, accessed 2026-10-14 |
| E1 | Cagliari, Italy | — | Janna | E1: https://www.submarinecablemap.com/api/v3/landing-point/cagliari-italy.json, accessed 2026-10-14 |
| E1 | Cala d'Oliva, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/cala-doliva-italy.json, accessed 2026-10-14 |
| E1 | Canneto, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/canneto-italy.json, accessed 2026-10-14 |
| E1 | Capraia Isola, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/capraia-isola-italy.json, accessed 2026-10-14 |
| E1 | Carloforte, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/carloforte-italy.json, accessed 2026-10-14 |
| E1 | Catania, Italy | — | Epic Malta-Sicily Cable System (EMSCS), IMEWE, Italy-Malta, MedNautilus Submarine System, SeaMeWe-5 | E1: https://www.submarinecablemap.com/api/v3/landing-point/catania-italy.json, accessed 2026-10-14 |
| E1 | Civitavecchia, Italy | — | Janna, ROMSAR 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/civitavecchia-italy.json, accessed 2026-10-14 |
| E1 | Crotone, Italy | — | Ionian | E1: https://www.submarinecablemap.com/api/v3/landing-point/crotone-italy.json, accessed 2026-10-14 |
| E1 | Ditella, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/ditella-italy.json, accessed 2026-10-14 |
| E1 | Filicudi Porto, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/filicudi-porto-italy.json, accessed 2026-10-14 |
| E1 | Fiumicino, Italy | — | Unitirreno | E1: https://www.submarinecablemap.com/api/v3/landing-point/fiumicino-italy.json, accessed 2026-10-14 |
| E1 | Gaeta, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/gaeta-italy.json, accessed 2026-10-14 |
| E1 | Genoa, Italy | — | 2Africa, ANDROMEDA (planned), Barracuda (planned, RFS 2028), Blue, EMC West-1 (planned, RFS 2027), Medloop, Unitirreno | E1: https://www.submarinecablemap.com/api/v3/landing-point/genoa-italy.json, accessed 2026-10-14 |
| E1 | Giglio, Italy | — | ROMSAR 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/giglio-italy.json, accessed 2026-10-14 |
| E1 | Golfo Aranci, Italy | — | Blue | E1: https://www.submarinecablemap.com/api/v3/landing-point/golfo-aranci-italy.json, accessed 2026-10-14 |
| E1 | Isola delle Femmine, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/isola-delle-femmine-italy.json, accessed 2026-10-14 |
| E1 | La Maddalena, Italy | — | ROMSAR 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/la-maddalena-italy.json, accessed 2026-10-14 |
| E1 | Lampedusa, Italy | — | Lic-Lin-Lamp, Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/lampedusa-italy.json, accessed 2026-10-14 |
| E1 | Lecce, Italy | — | EAGLE (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/lecce-italy.json, accessed 2026-10-14 |
| E1 | Levanzo, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/levanzo-italy.json, accessed 2026-10-14 |
| E1 | Licata, Italy | — | Lic-Lin-Lamp | E1: https://www.submarinecablemap.com/api/v3/landing-point/licata-italy.json, accessed 2026-10-14 |
| E1 | Linosa, Italy | — | Lic-Lin-Lamp, Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/linosa-italy.json, accessed 2026-10-14 |
| E1 | Lipari, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/lipari-italy.json, accessed 2026-10-14 |
| E1 | Malfa, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/malfa-italy.json, accessed 2026-10-14 |
| E1 | Marettimo, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/marettimo-italy.json, accessed 2026-10-14 |
| E1 | Marina di Ragusa, Italy | — | Malta-Italy Interconnector | E1: https://www.submarinecablemap.com/api/v3/landing-point/marina-di-ragusa-italy.json, accessed 2026-10-14 |
| E1 | Marsala, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/marsala-italy.json, accessed 2026-10-14 |
| E1 | Mazara del Vallo, Italy | — | Didon, GO-1 Mediterranean Cable System, HANNIBAL System, Italy-Libya, Janna, Medusa Submarine Cable System, Middle East North Africa (MENA) Cable System/Gulf Bridge International, Unitirreno | E1: https://www.submarinecablemap.com/api/v3/landing-point/mazara-del-vallo-italy.json, accessed 2026-10-14 |
| E1 | Mestre, Italy | — | Italy-Croatia | E1: https://www.submarinecablemap.com/api/v3/landing-point/mestre-italy.json, accessed 2026-10-14 |
| E1 | Olbia, Italy | — | Janna, Unitirreno | E1: https://www.submarinecablemap.com/api/v3/landing-point/olbia-italy.json, accessed 2026-10-14 |
| E1 | Otranto, Italy | — | Italy-Greece 1 (IG-1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/otranto-italy.json, accessed 2026-10-14 |
| E1 | Palermo, Italy | — | Blue, SeaMeWe-4 | E1: https://www.submarinecablemap.com/api/v3/landing-point/palermo-italy.json, accessed 2026-10-14 |
| E1 | Pantelleria, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/pantelleria-italy.json, accessed 2026-10-14 |
| E1 | Patti, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/patti-italy.json, accessed 2026-10-14 |
| E1 | Ponza, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/ponza-italy.json, accessed 2026-10-14 |
| E1 | Portoferraio, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/portoferraio-italy.json, accessed 2026-10-14 |
| E1 | Portoscuso, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/portoscuso-italy.json, accessed 2026-10-14 |
| E1 | Pozzallo, Italy | — | Melita 1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/pozzallo-italy.json, accessed 2026-10-14 |
| E1 | Rome, Italy | — | Blue | E1: https://www.submarinecablemap.com/api/v3/landing-point/rome-italy.json, accessed 2026-10-14 |
| E1 | San Domino, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/san-domino-italy.json, accessed 2026-10-14 |
| E1 | San Foca, Italy | — | Trans Adriatic Express (TAE) | E1: https://www.submarinecablemap.com/api/v3/landing-point/san-foca-italy.json, accessed 2026-10-14 |
| E1 | San Nicola di Tremiti, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/san-nicola-di-tremiti-italy.json, accessed 2026-10-14 |
| E1 | Santa Teresa Gallura, Italy | — | SARCO | E1: https://www.submarinecablemap.com/api/v3/landing-point/santa-teresa-gallura-italy.json, accessed 2026-10-14 |
| E1 | Santo Stefano, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/santo-stefano-italy.json, accessed 2026-10-14 |
| E1 | Sassari, Italy | — | ROMSAR 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/sassari-italy.json, accessed 2026-10-14 |
| E1 | Savona, Italy | — | India Europe Xpress (IEX) (planned, RFS 2027), Italy-Monaco | E1: https://www.submarinecablemap.com/api/v3/landing-point/savona-italy.json, accessed 2026-10-14 |
| E1 | Stintino, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/stintino-italy.json, accessed 2026-10-14 |
| E1 | Stromboli, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/stromboli-italy.json, accessed 2026-10-14 |
| E1 | Torre Mileto, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/torre-mileto-italy.json, accessed 2026-10-14 |
| E1 | Trapani, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/trapani-italy.json, accessed 2026-10-14 |
| E1 | Ustica, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/ustica-italy.json, accessed 2026-10-14 |
| E1 | Ventotene, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/ventotene-italy.json, accessed 2026-10-14 |
| E1 | Vulcano Bleu, Italy | — | Piano Isole Minori | E1: https://www.submarinecablemap.com/api/v3/landing-point/vulcano-bleu-italy.json, accessed 2026-10-14 |
| E2 | DE-CIX Palermo | Palermo | https://www.de-cix.net/locations/palermo | E2: https://www.peeringdb.com/ix/1131, accessed 2026-10-14 |
| E2 | Equinix Milan | Milan | https://www.equinix.it/services/interconnection-connectivity/internet-exchange | E2: https://www.peeringdb.com/ix/1925, accessed 2026-10-14 |
| E2 | Ge-DIX | Genova | https://www.ge-dix.net | E2: https://www.peeringdb.com/ix/4172, accessed 2026-10-14 |
| E2 | HamroIX-Rome | Rome | https://ix.hamro.net | E2: https://www.peeringdb.com/ix/3430, accessed 2026-10-14 |
| E2 | ixFabric - Rome | Rome | https://ixfabric.net | E2: https://www.peeringdb.com/ix/3824, accessed 2026-10-14 |
| E2 | MegaIX Milan | Milan | https://www.megaport.com | E2: https://www.peeringdb.com/ix/5060, accessed 2026-10-14 |
| E2 | MINAP Milan | Milan | https://www.minap.it | E2: https://www.peeringdb.com/ix/240, accessed 2026-10-14 |
| E2 | MIX Bologna | Bologna | https://www.mix-it.net | E2: https://www.peeringdb.com/ix/3730, accessed 2026-10-14 |
| E2 | MIX Caserta | Caserta | https://www.mix-it.net | E2: https://www.peeringdb.com/ix/4577, accessed 2026-10-14 |
| E2 | MIX Palermo | Palermo | https://www.mix-it.net | E2: https://www.peeringdb.com/ix/3290, accessed 2026-10-14 |
| E2 | MIX Roma | Rome | https://www.mix-it.net | E2: https://www.peeringdb.com/ix/4377, accessed 2026-10-14 |
| E2 | MIX-IT | Milan | https://www.mix-it.net | E2: https://www.peeringdb.com/ix/35, accessed 2026-10-14 |
| E2 | Namex Bari | Bari | https://bari.namex.it | E2: https://www.peeringdb.com/ix/3782, accessed 2026-10-14 |
| E2 | Namex Napoli | Napoli | https://www.namex.it | E2: https://www.peeringdb.com/ix/4046, accessed 2026-10-14 |
| E2 | Namex Rome | Rome | https://www.namex.it | E2: https://www.peeringdb.com/ix/121, accessed 2026-10-14 |
| E2 | NubiHost | Casano Madeno | https://nubihost.cloud | E2: https://www.peeringdb.com/ix/5014, accessed 2026-10-14 |
| E2 | PCIX | Piacenza | https://www.pcix.it | E2: https://www.peeringdb.com/ix/1933, accessed 2026-10-14 |
| E2 | SIIX Pomezia | Pomezia | https://www.siix.it | E2: https://www.peeringdb.com/ix/3528, accessed 2026-10-14 |
| E2 | SSIX | Olbia | https://www.ssix.it | E2: https://www.peeringdb.com/ix/4970, accessed 2026-10-14 |
| E2 | STIX | Bozen/Bolzano | https://www.stix.bz | E2: https://www.peeringdb.com/ix/2537, accessed 2026-10-14 |
| E2 | TIX | Florence | http://www.tix.it | E2: https://www.peeringdb.com/ix/273, accessed 2026-10-14 |
| E2 | TOP-IX | Turin | http://www.top-ix.org | E2: https://www.peeringdb.com/ix/115, accessed 2026-10-14 |
| E2 | VSIX | Padova | https://www.vs-ix.org | E2: https://www.peeringdb.com/ix/311, accessed 2026-10-14 |

Counts: E1 55 (in service 54, planned-only 1, unverified 0), E2 23, E3 0; no-landing no; single-landing no; single-exchange no.

## Latvia (LV)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Liepaja, Latvia | — | BCS East | E1: https://www.submarinecablemap.com/api/v3/landing-point/liepaja-latvia.json, accessed 2026-10-14 |
| E1 | Ventspils, Latvia | — | Latvia-Sweden 1 (LV-SE 1), Sweden-Latvia | E1: https://www.submarinecablemap.com/api/v3/landing-point/ventspils-latvia.json, accessed 2026-10-14 |
| E2 | GLV-IX | Riga | https://glv-ix.lv/customer/details | E2: https://www.peeringdb.com/ix/3750, accessed 2026-10-14 |
| E2 | LIX-LV | Riga | http://www.lix.lv | E2: https://www.peeringdb.com/ix/383, accessed 2026-10-14 |
| E2 | MSK-IX Riga | Riga | http://www.msk-ix.ru/en/ix/rix | E2: https://www.peeringdb.com/ix/1748, accessed 2026-10-14 |
| E2 | PITER-IX Riga | Riga | https://piter-ix.eu | E2: https://www.peeringdb.com/ix/3019, accessed 2026-10-14 |
| E2 | SMILE-IXP | Riga | http://www.smile-ixp.net | E2: https://www.peeringdb.com/ix/364, accessed 2026-10-14 |
| E3 | Vienotais valsts interneta plūsmu apmaiņas punkts (the single state internet exchange point) | — | — | E3: https://likumi.lv/ta/id/353390, accessed 2026-10-14 |

Counts: E1 2 (in service 2, planned-only 0, unverified 0), E2 5, E3 1; no-landing no; single-landing no; single-exchange no.

## Lithuania (LT)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Klaipeda, Lithuania | — | NordBalt | E1: https://www.submarinecablemap.com/api/v3/landing-point/klaipeda-lithuania.json, accessed 2026-10-14 |
| E1 | Sventoji, Lithuania | — | BCS East, BCS East-West Interlink | E1: https://www.submarinecablemap.com/api/v3/landing-point/sventoji-lithuania.json, accessed 2026-10-14 |
| E2 | BALT-IX | Vilnius | http://www.balt-ix.lt | E2: https://www.peeringdb.com/ix/2005, accessed 2026-10-14 |
| E2 | LIPTAM | Vilnius | http://is.lt | E2: https://www.peeringdb.com/ix/400, accessed 2026-10-14 |
| E2 | Litix | Vilnius | https://delska.com | E2: https://www.peeringdb.com/ix/542, accessed 2026-10-14 |
| E2 | LIXP | Vilnius | http://www.lixp.lt/en | E2: https://www.peeringdb.com/ix/526, accessed 2026-10-14 |

Counts: E1 2 (in service 2, planned-only 0, unverified 0), E2 4, E3 0; no-landing no; single-landing no; single-exchange no.

## Luxembourg (LU)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | (none on the map) | — | — | none: searched 2026-10-14 |
| E2 | LU-CIX | Luxembourg | https://www.lu-cix.lu | E2: https://www.peeringdb.com/ix/297, accessed 2026-10-14 |

Counts: E1 0 (in service 0, planned-only 0, unverified 0), E2 1, E3 0; no-landing yes; single-landing no; single-exchange yes.

## Malta (MT)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Bahar ic-Caghaq, Malta | — | Malta-Italy Interconnector, Melita 1 | E1: https://www.submarinecablemap.com/api/v3/landing-point/bahar-ic-caghaq-malta.json, accessed 2026-10-14 |
| E1 | Balluta Bay, Malta | — | Epic Malta-Sicily Cable System (EMSCS) | E1: https://www.submarinecablemap.com/api/v3/landing-point/balluta-bay-malta.json, accessed 2026-10-14 |
| E1 | Golden Bay, Malta | — | Malta-Gozo Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/golden-bay-malta.json, accessed 2026-10-14 |
| E1 | Mellieha, Malta | — | Medusa Submarine Cable System, PEACE Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/mellieha-malta.json, accessed 2026-10-14 |
| E1 | Mgarr ix-Xini, Malta | — | Malta-Gozo Cable | E1: https://www.submarinecablemap.com/api/v3/landing-point/mgarr-ix-xini-malta.json, accessed 2026-10-14 |
| E1 | St. George's Bay, Malta | — | Italy-Malta | E1: https://www.submarinecablemap.com/api/v3/landing-point/st-georges-bay-malta.json, accessed 2026-10-14 |
| E1 | St. Paul's Bay, Malta | — | GO-1 Mediterranean Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/st-pauls-bay-malta.json, accessed 2026-10-14 |
| E2 | (none in PeeringDB) | — | — | none: searched 2026-10-14 |

Counts: E1 7 (in service 7, planned-only 0, unverified 0), E2 0, E3 0; no-landing no; single-landing no; single-exchange yes.

## Netherlands (NL)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Beverwijk, Netherlands | — | Atlantic Crossing-1 (AC-1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/beverwijk-netherlands.json, accessed 2026-10-14 |
| E1 | Callantsoog, Netherlands | — | Iceni | E1: https://www.submarinecablemap.com/api/v3/landing-point/callantsoog-netherlands.json, accessed 2026-10-14 |
| E1 | Domburg, Netherlands | — | Farland North | E1: https://www.submarinecablemap.com/api/v3/landing-point/domburg-netherlands.json, accessed 2026-10-14 |
| E1 | Eemshaven, Netherlands | — | COBRAcable, IOEMA-1 (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/eemshaven-netherlands.json, accessed 2026-10-14 |
| E1 | Ijmuiden, Netherlands | — | Scylla, Ulysses 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/ijmuiden-netherlands.json, accessed 2026-10-14 |
| E1 | Kralendijk, Bonaire, Netherlands | Bonaire | Amerigo Vespucci | E1: https://www.submarinecablemap.com/api/v3/landing-point/kralendijk-bonaire-netherlands.json, accessed 2026-10-14 |
| E1 | The Hague, Netherlands | — | IOEMA-1 (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/the-hague-netherlands.json, accessed 2026-10-14 |
| E1 | Zandvoort, Netherlands | — | Circe North, Concerto, Zeus | E1: https://www.submarinecablemap.com/api/v3/landing-point/zandvoort-netherlands.json, accessed 2026-10-14 |
| E2 | 1-NL FREE | Amsterdam | https://1-ix.eu/1nl | E2: https://www.peeringdb.com/ix/4918, accessed 2026-10-14 |
| E2 | 3AM Network IX | Amsterdam | https://3am.network | E2: https://www.peeringdb.com/ix/5023, accessed 2026-10-14 |
| E2 | AMS-IX | Amsterdam | http://www.ams-ix.net | E2: https://www.peeringdb.com/ix/26, accessed 2026-10-14 |
| E2 | Asteroid Amsterdam | Amsterdam | https://www.asteroidhq.com/ixp-locations/1 | E2: https://www.peeringdb.com/ix/1812, accessed 2026-10-14 |
| E2 | BBIX Amsterdam | Amsterdam | https://www.bbix.net/en | E2: https://www.peeringdb.com/ix/3190, accessed 2026-10-14 |
| E2 | Clue-IX | Amsterdam | https://coloclue.net | E2: https://www.peeringdb.com/ix/5106, accessed 2026-10-14 |
| E2 | ENS-IX | Enschede | https://ens-ix.net | E2: https://www.peeringdb.com/ix/4644, accessed 2026-10-14 |
| E2 | Equinix Amsterdam | Amsterdam | https://www.equinix.nl/services/interconnection-connectivity/internet-exchange | E2: https://www.peeringdb.com/ix/2031, accessed 2026-10-14 |
| E2 | ERA-IX Amsterdam | Amsterdam | https://www.era-ix.com/amsterdam | E2: https://www.peeringdb.com/ix/3789, accessed 2026-10-14 |
| E2 | FogIXP Amsterdam | Amsterdam | https://fogixp.nl | E2: https://www.peeringdb.com/ix/4837, accessed 2026-10-14 |
| E2 | Frys-IX | Fryslân | http://www.frys-IX.net | E2: https://www.peeringdb.com/ix/3512, accessed 2026-10-14 |
| E2 | Giganet IXN Amsterdam | Amsterdam | http://giganet.ua/en | E2: https://www.peeringdb.com/ix/4384, accessed 2026-10-14 |
| E2 | Global-IX | Amsterdam | https://gnm.net | E2: https://www.peeringdb.com/ix/1088, accessed 2026-10-14 |
| E2 | GNM-IX | Amsterdam | https://gnm-ix.net | E2: https://www.peeringdb.com/ix/358, accessed 2026-10-14 |
| E2 | GrunIX | Groningen | http://www.grunix.net | E2: https://www.peeringdb.com/ix/3288, accessed 2026-10-14 |
| E2 | Grunn-IX | Groningen | https://grunn-ix.nl | E2: https://www.peeringdb.com/ix/3968, accessed 2026-10-14 |
| E2 | HamroIX-Amsterdam | Amsterdam | https://ix.hamro.com | E2: https://www.peeringdb.com/ix/3393, accessed 2026-10-14 |
| E2 | INTERIX | Amsterdam | https://www.inter-ix.net | E2: https://www.peeringdb.com/ix/3990, accessed 2026-10-14 |
| E2 | ixFabric - Amsterdam | Amsterdam | https://ixfabric.net | E2: https://www.peeringdb.com/ix/3822, accessed 2026-10-14 |
| E2 | IXP NL DRO | Dronten | https://www.ixp.cat | E2: https://www.peeringdb.com/ix/2705, accessed 2026-10-14 |
| E2 | Kawaii IX AMS | Amsterdam | https://kawaii-ix.net | E2: https://www.peeringdb.com/ix/4973, accessed 2026-10-14 |
| E2 | LOCIX NETHERLANDS | Meppel | https://locix.online | E2: https://www.peeringdb.com/ix/2601, accessed 2026-10-14 |
| E2 | LSIX | Amsterdam, The Hague, Rotterdam, Naaldwijk | https://lsix.net | E2: https://www.peeringdb.com/ix/1308, accessed 2026-10-14 |
| E2 | NDIX | Enschede / Münster | http://www.ndix.net | E2: https://www.peeringdb.com/ix/85, accessed 2026-10-14 |
| E2 | NL-ix | Amsterdam, Rotterdam, Brussels, Luxembourg, Frankfurt, Düsseldorf, Berlin, Dublin, London, Copenhagen, Paris, Marseille | https://www.nl-ix.net | E2: https://www.peeringdb.com/ix/64, accessed 2026-10-14 |
| E2 | NL-ix 2 | Amsterdam | https://www.nl-ix.net | E2: https://www.peeringdb.com/ix/2569, accessed 2026-10-14 |
| E2 | Noord-IX | Leeuwarden | https://www.noord-ix.nl | E2: https://www.peeringdb.com/ix/4360, accessed 2026-10-14 |
| E2 | NSIX Amsterdam | Amsterdam | https://nsix.net | E2: https://www.peeringdb.com/ix/4589, accessed 2026-10-14 |
| E2 | PeersIX Amsterdam | Amsterdam | https://peersix.ovh | E2: https://www.peeringdb.com/ix/4553, accessed 2026-10-14 |
| E2 | R_iX | Rotterdam | https://www.r-ix.nl | E2: https://www.peeringdb.com/ix/313, accessed 2026-10-14 |
| E2 | SBIX Amsterdam | Amsterdam | https://www.securebit.ch | E2: https://www.peeringdb.com/ix/2753, accessed 2026-10-14 |
| E2 | SeptemberIX | Amsterdam | https://septemberix.com | E2: https://www.peeringdb.com/ix/4034, accessed 2026-10-14 |
| E2 | SN-IX | Eygelshoven | https://ix.sn-tux.it | E2: https://www.peeringdb.com/ix/4424, accessed 2026-10-14 |
| E2 | Speed-IX | Dronten | https://speed-ix.net | E2: https://www.peeringdb.com/ix/1842, accessed 2026-10-14 |
| E2 | WHY2025 IXP | Geesterambacht | https://wiki.why2025.org/IXP | E2: https://www.peeringdb.com/ix/4792, accessed 2026-10-14 |

Counts: E1 8 (in service 7, planned-only 1, unverified 0), E2 35, E3 0; no-landing no; single-landing no; single-exchange no.

## Poland (PL)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Kołobrzeg, Poland | — | Baltica | E1: https://www.submarinecablemap.com/api/v3/landing-point/koobrzeg-poland.json, accessed 2026-10-14 |
| E2 | 1-IX EU | New-York, London, Paris, Madrid, Frankfurt, Amsterdam, Warsaw, Bratislava, Hong Kong | https://1-ix.eu | E2: https://www.peeringdb.com/ix/3958, accessed 2026-10-14 |
| E2 | 1-PL FREE | Warsaw, Wroclaw, Katowice | https://1-ix.eu/1pl | E2: https://www.peeringdb.com/ix/4916, accessed 2026-10-14 |
| E2 | CePIX.pl | Mogilno | http://cepix.pl | E2: https://www.peeringdb.com/ix/524, accessed 2026-10-14 |
| E2 | CIX KR | Krakow | http://www.ix.krakow.pl | E2: https://www.peeringdb.com/ix/778, accessed 2026-10-14 |
| E2 | EPIX.Katowice | Katowice/Silesia | https://www.epix.net.pl | E2: https://www.peeringdb.com/ix/491, accessed 2026-10-14 |
| E2 | EPIX.Poznan | Poznan | https://www.epix.net.pl | E2: https://www.peeringdb.com/ix/3594, accessed 2026-10-14 |
| E2 | EPIX.Warszawa | Warsaw | https://www.epix.net.pl | E2: https://www.peeringdb.com/ix/474, accessed 2026-10-14 |
| E2 | Equinix Warsaw | Warsaw | https://www.equinix.com | E2: https://www.peeringdb.com/ix/264, accessed 2026-10-14 |
| E2 | Giganet IXN Warsaw | Warsaw | http://giganet.ua/en | E2: https://www.peeringdb.com/ix/2918, accessed 2026-10-14 |
| E2 | IX.LODZ.PL | Łódź | http://ix.lodz.pl | E2: https://www.peeringdb.com/ix/1516, accessed 2026-10-14 |
| E2 | PIONIER-IX | Białystok, Poznań, Wrocław, Szczecin, Opole, Częstochowa | https://docs.psnc.pl/display/PIONIERIX/PIONIER-IX | E2: https://www.peeringdb.com/ix/3122, accessed 2026-10-14 |
| E2 | POM-IX | Gdańsk | https://en.pomix.pl | E2: https://www.peeringdb.com/ix/4480, accessed 2026-10-14 |
| E2 | POZIX | Poznan | http://www.pozix.pl | E2: https://www.peeringdb.com/ix/230, accessed 2026-10-14 |
| E2 | RZ-IX | Rzeszow | — | E2: https://www.peeringdb.com/ix/828, accessed 2026-10-14 |
| E2 | THINX Warsaw | Warsaw | http://thinx.pl | E2: https://www.peeringdb.com/ix/481, accessed 2026-10-14 |
| E2 | TPIX PL | Warsaw | https://www.tpix.pl/en | E2: https://www.peeringdb.com/ix/482, accessed 2026-10-14 |
| E2 | WRIX | Wrocław | https://wrix.org | E2: https://www.peeringdb.com/ix/1423, accessed 2026-10-14 |

Counts: E1 1 (in service 1, planned-only 0, unverified 0), E2 17, E3 0; no-landing no; single-landing yes; single-exchange no.

## Portugal (PT)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Angra do Heroismo, Portugal | — | Azores Fiber Optic System (AFOS) | E1: https://www.submarinecablemap.com/api/v3/landing-point/angra-do-heroismo-portugal.json, accessed 2026-10-14 |
| E1 | Burgau, Portugal | — | Sagres | E1: https://www.submarinecablemap.com/api/v3/landing-point/burgau-portugal.json, accessed 2026-10-14 |
| E1 | Carcavelos, Portugal | — | 2Africa, Africa Coast to Europe (ACE), BUGIO, Columbus-III Azores-Portugal, Continente-Madeira, Medusa Submarine Cable System, New CAM Ring (planned, RFS 2027), Olisipo (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/carcavelos-portugal.json, accessed 2026-10-14 |
| E1 | Corvo, Portugal | — | Flores-Corvo Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/corvo-portugal.json, accessed 2026-10-14 |
| E1 | Faial, Portugal | — | Azores Fiber Optic System (AFOS), Flores-Corvo Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/faial-portugal.json, accessed 2026-10-14 |
| E1 | Flores, Portugal | — | Flores-Corvo Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/flores-portugal.json, accessed 2026-10-14 |
| E1 | Funchal, Portugal | — | CAM Ring, Continente-Madeira, EllaLink, New CAM Ring (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/funchal-portugal.json, accessed 2026-10-14 |
| E1 | Graciosa, Portugal | — | Azores Fiber Optic System (AFOS), Flores-Corvo Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/graciosa-portugal.json, accessed 2026-10-14 |
| E1 | Machico, Portugal | — | New CAM Ring (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/machico-portugal.json, accessed 2026-10-14 |
| E1 | Ponta Delgada, Portugal | — | Azores Fiber Optic System (AFOS), CAM Ring, Columbus-III Azores-Portugal | E1: https://www.submarinecablemap.com/api/v3/landing-point/ponta-delgada-portugal.json, accessed 2026-10-14 |
| E1 | Porto Santo, Portugal | — | CAM Ring | E1: https://www.submarinecablemap.com/api/v3/landing-point/porto-santo-portugal.json, accessed 2026-10-14 |
| E1 | Sao Mateus, Portugal | — | Azores Fiber Optic System (AFOS) | E1: https://www.submarinecablemap.com/api/v3/landing-point/sao-mateus-portugal.json, accessed 2026-10-14 |
| E1 | Seixal, Portugal | — | MainOne, Tata TGN-Western Europe, West Africa Cable System (WACS) | E1: https://www.submarinecablemap.com/api/v3/landing-point/seixal-portugal.json, accessed 2026-10-14 |
| E1 | Sesimbra, Portugal | — | BUGIO, Equiano, Europe India Gateway (EIG), Sagres, SAT-3/WASC | E1: https://www.submarinecablemap.com/api/v3/landing-point/sesimbra-portugal.json, accessed 2026-10-14 |
| E1 | Sines, Portugal | — | EllaLink, New CAM Ring (planned, RFS 2027), Nuvem (planned, RFS 2027), Olisipo (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/sines-portugal.json, accessed 2026-10-14 |
| E1 | São Miguel, Portugal | — | New CAM Ring (planned, RFS 2027), Nuvem (planned, RFS 2027), Sol (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/so-miguel-portugal.json, accessed 2026-10-14 |
| E1 | Terceira, Portugal | — | New CAM Ring (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/terceira-portugal.json, accessed 2026-10-14 |
| E1 | Velas, Portugal | — | Azores Fiber Optic System (AFOS) | E1: https://www.submarinecablemap.com/api/v3/landing-point/velas-portugal.json, accessed 2026-10-14 |
| E1 | Vila do Porto, Portugal | — | Azores Fiber Optic System (AFOS) | E1: https://www.submarinecablemap.com/api/v3/landing-point/vila-do-porto-portugal.json, accessed 2026-10-14 |
| E2 | DE-CIX Lisbon | Lisbon | https://www.de-cix.net/locations/lisbon | E2: https://www.peeringdb.com/ix/2531, accessed 2026-10-14 |
| E2 | Equinix Lisbon | Lisbon | https://ix.equinix.com/home/lisbon | E2: https://www.peeringdb.com/ix/2131, accessed 2026-10-14 |
| E2 | GigaPIX - LAN 1 | Lisbon | http://www.gigapix.pt | E2: https://www.peeringdb.com/ix/72, accessed 2026-10-14 |
| E2 | GigaPIX - LAN 2 | Lisbon | http://www.gigapix.pt | E2: https://www.peeringdb.com/ix/2849, accessed 2026-10-14 |
| E2 | ixFabric - Lisbon | Lisbon | https://ixfabric.net | E2: https://www.peeringdb.com/ix/4636, accessed 2026-10-14 |
| E2 | LIS-IX | Lisbon | https://lis-ix.pt | E2: https://www.peeringdb.com/ix/4353, accessed 2026-10-14 |

Counts: E1 19 (in service 16, planned-only 3, unverified 0), E2 6, E3 0; no-landing no; single-landing no; single-exchange no.

## Romania (RO)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Mangalia, Romania | — | KAFOS | E1: https://www.submarinecablemap.com/api/v3/landing-point/mangalia-romania.json, accessed 2026-10-14 |
| E2 | Balcan-IX | Bucharest | http://www.balcan-ix.net | E2: https://www.peeringdb.com/ix/372, accessed 2026-10-14 |
| E2 | DoljNET IX | Craiova | http://www.doljnet.ro | E2: https://www.peeringdb.com/ix/4696, accessed 2026-10-14 |
| E2 | DSIX | Bucharest | https://ix.dreamserver.ro | E2: https://www.peeringdb.com/ix/3477, accessed 2026-10-14 |
| E2 | InterLAN-IX | Bucharest | https://www.interlan.ro/en | E2: https://www.peeringdb.com/ix/270, accessed 2026-10-14 |
| E2 | RO-CIX | Braila | https://whitehat.ro/internet-exchange | E2: https://www.peeringdb.com/ix/2804, accessed 2026-10-14 |
| E2 | RO-IX | Bucharest | https://www.ix.ro | E2: https://www.peeringdb.com/ix/2732, accessed 2026-10-14 |
| E2 | RoNIX | Bucharest | https://anisp.ro | E2: https://www.peeringdb.com/ix/301, accessed 2026-10-14 |

Counts: E1 1 (in service 1, planned-only 0, unverified 0), E2 7, E3 0; no-landing no; single-landing yes; single-exchange no.

## Slovakia (SK)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | (none on the map) | — | — | none: searched 2026-10-14 |
| E2 | 1-SK FREE | Bratislava | https://1-ix.eu/1sk | E2: https://www.peeringdb.com/ix/4997, accessed 2026-10-14 |
| E2 | NIX.SK | Bratislava | https://www.nix.sk/sk | E2: https://www.peeringdb.com/ix/299, accessed 2026-10-14 |
| E2 | PoIX | Presov | https://www.poix.sk | E2: https://www.peeringdb.com/ix/3709, accessed 2026-10-14 |
| E2 | SIX.SK | Bratislava | https://www.six.sk | E2: https://www.peeringdb.com/ix/84, accessed 2026-10-14 |
| E2 | SIX.SK Košice | Košice | http://www.six.sk | E2: https://www.peeringdb.com/ix/559, accessed 2026-10-14 |

Counts: E1 0 (in service 0, planned-only 0, unverified 0), E2 5, E3 0; no-landing yes; single-landing no; single-exchange no.

## Slovenia (SI)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | (none on the map) | — | — | none: searched 2026-10-14 |
| E2 | SIX SI | Ljubljana | https://www.six.si/en/home | E2: https://www.peeringdb.com/ix/319, accessed 2026-10-14 |

Counts: E1 0 (in service 0, planned-only 0, unverified 0), E2 1, E3 0; no-landing yes; single-landing no; single-exchange yes.

## Spain (ES)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Aguimes, Canary Islands, Spain | Canary Islands | TRANSCAN-2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/aguimes-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Almería, Spain | — | Almería-Melilla (ALME) | E1: https://www.submarinecablemap.com/api/v3/landing-point/almera-spain.json, accessed 2026-10-14 |
| E1 | Alta Vista, Canary Islands, Spain | Canary Islands | CANDALTA, SAT-3/WASC, TRANSCAN-3 | E1: https://www.submarinecablemap.com/api/v3/landing-point/alta-vista-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Arrecife, Canary Islands, Spain | Canary Islands | Orient Island Ring (planned, RFS 2028), TRANSCAN-2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/arrecife-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Barcelona, Spain | — | 2Africa, Medloop, Medusa Submarine Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/barcelona-spain.json, accessed 2026-10-14 |
| E1 | Bilbao, Spain | — | Grace Hopper, MAREA, Tata TGN-Western Europe | E1: https://www.submarinecablemap.com/api/v3/landing-point/bilbao-spain.json, accessed 2026-10-14 |
| E1 | Candelaria Santa Cruz de Tenerife, Spain | — | CANDALTA, Pencan-8 | E1: https://www.submarinecablemap.com/api/v3/landing-point/candelaria-santa-cruz-de-tenerife-spain.json, accessed 2026-10-14 |
| E1 | Chipiona, Spain | — | Pencan-9, SAT-3/WASC | E1: https://www.submarinecablemap.com/api/v3/landing-point/chipiona-spain.json, accessed 2026-10-14 |
| E1 | Conil de la Frontera, Spain | — | Canalink, Pencan-8 | E1: https://www.submarinecablemap.com/api/v3/landing-point/conil-de-la-frontera-spain.json, accessed 2026-10-14 |
| E1 | Corralejo, Canary Islands, Spain | Canary Islands | Orient Island Ring (planned, RFS 2028) | E1: https://www.submarinecablemap.com/api/v3/landing-point/corralejo-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Costa Calma, Spain | — | Orient Island Ring (planned, RFS 2028) | E1: https://www.submarinecablemap.com/api/v3/landing-point/costa-calma-spain.json, accessed 2026-10-14 |
| E1 | El Goro, Canary Islands, Spain | Canary Islands | Canalink, West Africa Cable System (WACS) | E1: https://www.submarinecablemap.com/api/v3/landing-point/el-goro-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | El Médano, Canary Islands, Spain | Canary Islands | Tenerife-Gran Canaria | E1: https://www.submarinecablemap.com/api/v3/landing-point/el-mdano-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Estepona, Spain | — | Est-Tet | E1: https://www.submarinecablemap.com/api/v3/landing-point/estepona-spain.json, accessed 2026-10-14 |
| E1 | Gavá, Spain | — | Penbal-5 | E1: https://www.submarinecablemap.com/api/v3/landing-point/gav-spain.json, accessed 2026-10-14 |
| E1 | Gran Canaria, Canary Islands, Spain | Canary Islands | 2Africa, EllaLink | E1: https://www.submarinecablemap.com/api/v3/landing-point/gran-canaria-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Granadilla de Abona, Spain | — | Africa Coast to Europe (ACE), Canalink, TEGOPA | E1: https://www.submarinecablemap.com/api/v3/landing-point/granadilla-de-abona-spain.json, accessed 2026-10-14 |
| E1 | Güimar, Canary Islands, Spain | Canary Islands | Canalink | E1: https://www.submarinecablemap.com/api/v3/landing-point/gimar-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Ibiza, Spain | — | Penbal-4 | E1: https://www.submarinecablemap.com/api/v3/landing-point/ibiza-spain.json, accessed 2026-10-14 |
| E1 | La Línea, Spain | — | DOS CONTINENTES l & ll | E1: https://www.submarinecablemap.com/api/v3/landing-point/la-lnea-spain.json, accessed 2026-10-14 |
| E1 | Las Caletillas, Spain | — | Subcan Link 1, Subcan Link 2, Teide (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/las-caletillas-spain.json, accessed 2026-10-14 |
| E1 | Las Palmas, Spain | — | Orient Island Ring (planned, RFS 2028) | E1: https://www.submarinecablemap.com/api/v3/landing-point/las-palmas-spain.json, accessed 2026-10-14 |
| E1 | Los Realejos, Canary Islands, Spain | Canary Islands | Tenerife-La Palma | E1: https://www.submarinecablemap.com/api/v3/landing-point/los-realejos-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Mallorca, Spain | — | Penbal-4 | E1: https://www.submarinecablemap.com/api/v3/landing-point/mallorca-spain.json, accessed 2026-10-14 |
| E1 | Manilva, Spain | — | Medusa Submarine Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/manilva-spain.json, accessed 2026-10-14 |
| E1 | Melilla, Spain | — | Almería-Melilla (ALME), Roquetas-Melilla (CAM) | E1: https://www.submarinecablemap.com/api/v3/landing-point/melilla-spain.json, accessed 2026-10-14 |
| E1 | Morrojable, Canary Islands, Spain | Canary Islands | TRANSCAN-2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/morrojable-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Palma, Spain | — | Balalink | E1: https://www.submarinecablemap.com/api/v3/landing-point/palma-spain.json, accessed 2026-10-14 |
| E1 | Piedra Santa, Spain | — | Subcan Link 1, Subcan Link 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/piedra-santa-spain.json, accessed 2026-10-14 |
| E1 | Playa Blanca, Canary Islands, Spain | Canary Islands | Orient Island Ring (planned, RFS 2028), TRANSCAN-3 | E1: https://www.submarinecablemap.com/api/v3/landing-point/playa-blanca-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Playa de Benitez, Spain | — | DOS CONTINENTES l & ll | E1: https://www.submarinecablemap.com/api/v3/landing-point/playa-de-benitez-spain.json, accessed 2026-10-14 |
| E1 | Playa de la Ribera, Spain | — | DOS CONTINENTES l & ll | E1: https://www.submarinecablemap.com/api/v3/landing-point/playa-de-la-ribera-spain.json, accessed 2026-10-14 |
| E1 | Puerto del Rosario, Canary Islands, Spain | Canary Islands | Orient Island Ring (planned, RFS 2028), TRANSCAN-2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/puerto-del-rosario-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Roquetas de Mar, Spain | — | Roquetas-Melilla (CAM) | E1: https://www.submarinecablemap.com/api/v3/landing-point/roquetas-de-mar-spain.json, accessed 2026-10-14 |
| E1 | Rota, Spain | — | Canalink | E1: https://www.submarinecablemap.com/api/v3/landing-point/rota-spain.json, accessed 2026-10-14 |
| E1 | Sagunto, Spain | — | Barracuda (planned, RFS 2028), Romulo | E1: https://www.submarinecablemap.com/api/v3/landing-point/sagunto-spain.json, accessed 2026-10-14 |
| E1 | San Sebastian de la Gomera, Canary Islands, Spain | Canary Islands | La Gomera-El Hierro, TEGOPA | E1: https://www.submarinecablemap.com/api/v3/landing-point/san-sebastian-de-la-gomera-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Santa Cruz de La Palma, Canary Islands, Spain | Canary Islands | Canalink, TEGOPA, Tenerife-La Palma | E1: https://www.submarinecablemap.com/api/v3/landing-point/santa-cruz-de-la-palma-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Santa Ponsa, Spain | — | Romulo | E1: https://www.submarinecablemap.com/api/v3/landing-point/santa-ponsa-spain.json, accessed 2026-10-14 |
| E1 | Santander, Spain | — | Anjana, Sol (planned, RFS 2029) | E1: https://www.submarinecablemap.com/api/v3/landing-point/santander-spain.json, accessed 2026-10-14 |
| E1 | Sardina, Canary Islands, Spain | Canary Islands | Tenerife-Gran Canaria | E1: https://www.submarinecablemap.com/api/v3/landing-point/sardina-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Ses Covetes, Spain | — | Penbal-5 | E1: https://www.submarinecablemap.com/api/v3/landing-point/ses-covetes-spain.json, accessed 2026-10-14 |
| E1 | Tamaduste, Canary Islands, Spain | Canary Islands | Teide (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/tamaduste-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Tarahales, Spain | — | Pencan-9 | E1: https://www.submarinecablemap.com/api/v3/landing-point/tarahales-spain.json, accessed 2026-10-14 |
| E1 | Tarifa, Spain | — | DOS CONTINENTES l & ll | E1: https://www.submarinecablemap.com/api/v3/landing-point/tarifa-spain.json, accessed 2026-10-14 |
| E1 | Telde, Spain | — | Orient Island Ring (planned, RFS 2028) | E1: https://www.submarinecablemap.com/api/v3/landing-point/telde-spain.json, accessed 2026-10-14 |
| E1 | Tinocas, Canary Islands, Spain | Canary Islands | Canalink | E1: https://www.submarinecablemap.com/api/v3/landing-point/tinocas-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Valencia, Spain | — | Balalink, Oran-Valencia (ORVAL), Penbal-4 | E1: https://www.submarinecablemap.com/api/v3/landing-point/valencia-spain.json, accessed 2026-10-14 |
| E1 | Valverde, Canary Islands, Spain | Canary Islands | La Gomera-El Hierro | E1: https://www.submarinecablemap.com/api/v3/landing-point/valverde-canary-islands-spain.json, accessed 2026-10-14 |
| E1 | Zahara de los Atunes, Spain | — | Medusa Submarine Cable System | E1: https://www.submarinecablemap.com/api/v3/landing-point/zahara-de-los-atunes-spain.json, accessed 2026-10-14 |
| E2 | 1-ES FREE | Madrid | https://1-ix.eu/1es | E2: https://www.peeringdb.com/ix/4993, accessed 2026-10-14 |
| E2 | AxiusIX EIR | Eirenia | https://axiusix.io | E2: https://www.peeringdb.com/ix/4511, accessed 2026-10-14 |
| E2 | Barcelona-IX | Barcelona | https://barcelona-ix.net | E2: https://www.peeringdb.com/ix/4322, accessed 2026-10-14 |
| E2 | CATNIX | Barcelona | http://www.catnix.net | E2: https://www.peeringdb.com/ix/62, accessed 2026-10-14 |
| E2 | DE-CIX Barcelona | Barcelona | https://www.de-cix.net/en/locations/barcelona | E2: https://www.peeringdb.com/ix/3446, accessed 2026-10-14 |
| E2 | DE-CIX Madrid | Madrid | https://www.de-cix.net/locations/madrid | E2: https://www.peeringdb.com/ix/1277, accessed 2026-10-14 |
| E2 | ELX-IX | Elche | https://ix.mario.gdn | E2: https://www.peeringdb.com/ix/4064, accessed 2026-10-14 |
| E2 | Equinix Barcelona | Barcelona | https://www.equinix.com/data-centers/europe-colocation/spain-colocation/barcelona-data-centers | E2: https://www.peeringdb.com/ix/2633, accessed 2026-10-14 |
| E2 | Equinix Madrid | Madrid | https://ix.equinix.com/home/madrid | E2: https://www.peeringdb.com/ix/2130, accessed 2026-10-14 |
| E2 | ESpanix Barcelona Lower LAN | Barcelona | https://www.espanix.net | E2: https://www.peeringdb.com/ix/4583, accessed 2026-10-14 |
| E2 | ESpanix Barcelona Upper LAN | Barcelona | https://www.espanix.net | E2: https://www.peeringdb.com/ix/4584, accessed 2026-10-14 |
| E2 | ESpanix Madrid Lower LAN | Madrid | https://www.espanix.net | E2: https://www.peeringdb.com/ix/63, accessed 2026-10-14 |
| E2 | ESpanix Madrid Upper LAN | Madrid | https://www.espanix.net | E2: https://www.peeringdb.com/ix/1146, accessed 2026-10-14 |
| E2 | ixFabric - Barcelona | Barcelona | https://ixfabric.net | E2: https://www.peeringdb.com/ix/3832, accessed 2026-10-14 |
| E2 | IXPlay Global Peers | Madrid | https://ixplay.global | E2: https://www.peeringdb.com/ix/3149, accessed 2026-10-14 |
| E2 | Mario IX | Elche | https://ix.mario.gdn | E2: https://www.peeringdb.com/ix/4002, accessed 2026-10-14 |
| E2 | MegaIX Madrid | Madrid | https://www.megaport.com | E2: https://www.peeringdb.com/ix/5063, accessed 2026-10-14 |
| E2 | NIXVAL-IX | Valencia | https://ixp.nixval.com | E2: https://www.peeringdb.com/ix/1160, accessed 2026-10-14 |

Counts: E1 50 (in service 45, planned-only 5, unverified 0), E2 18, E3 0; no-landing no; single-landing no; single-exchange no.

## Sweden (SE)

| Kind | Name | Place | Cables or website | Basis |
|---|---|---|---|---|
| E1 | Barsebäck, Sweden | — | Danica North | E1: https://www.submarinecablemap.com/api/v3/landing-point/barsebck-sweden.json, accessed 2026-10-14 |
| E1 | Borbby Strandbad, Sweden | — | GlobalConnect Aurora | E1: https://www.submarinecablemap.com/api/v3/landing-point/borbby-strandbad-sweden.json, accessed 2026-10-14 |
| E1 | Bunkeflostand, Sweden | — | Scandinavian Ring South | E1: https://www.submarinecablemap.com/api/v3/landing-point/bunkeflostand-sweden.json, accessed 2026-10-14 |
| E1 | Byxelkrok, Sweden | — | GlobalConnect Aurora | E1: https://www.submarinecablemap.com/api/v3/landing-point/byxelkrok-sweden.json, accessed 2026-10-14 |
| E1 | Capri Strand, Sweden | — | Norfest | E1: https://www.submarinecablemap.com/api/v3/landing-point/capri-strand-sweden.json, accessed 2026-10-14 |
| E1 | Farosund, Sweden | — | GlobalConnect Aurora, Mjolner East (planned, RFS 2027), Sweden-Latvia | E1: https://www.submarinecablemap.com/api/v3/landing-point/farosund-sweden.json, accessed 2026-10-14 |
| E1 | Helsingborg, Sweden | — | Denmark-Sweden 18, Scandinavian Ring North | E1: https://www.submarinecablemap.com/api/v3/landing-point/helsingborg-sweden.json, accessed 2026-10-14 |
| E1 | Katthammarsvik, Sweden | — | BCS East-West Interlink | E1: https://www.submarinecablemap.com/api/v3/landing-point/katthammarsvik-sweden.json, accessed 2026-10-14 |
| E1 | Kista, Sweden | — | Eastern Light Sweden-Finland II (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/kista-sweden.json, accessed 2026-10-14 |
| E1 | Klagshamn, Sweden | — | GlobalConnect Aurora, GlobalConnect Denmark-Sweden | E1: https://www.submarinecablemap.com/api/v3/landing-point/klagshamn-sweden.json, accessed 2026-10-14 |
| E1 | Kristinelund, Sweden | — | Denmark-Sweden 17 | E1: https://www.submarinecablemap.com/api/v3/landing-point/kristinelund-sweden.json, accessed 2026-10-14 |
| E1 | Kungsbacka, Sweden | — | GlobalConnect 2 (GC2) | E1: https://www.submarinecablemap.com/api/v3/landing-point/kungsbacka-sweden.json, accessed 2026-10-14 |
| E1 | Lerkil, Sweden | — | Kattegat Cable (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/lerkil-sweden.json, accessed 2026-10-14 |
| E1 | Nothamnsbacken, Sweden | — | STO-HEL-One | E1: https://www.submarinecablemap.com/api/v3/landing-point/nothamnsbacken-sweden.json, accessed 2026-10-14 |
| E1 | Nybro, Sweden | — | NordBalt | E1: https://www.submarinecablemap.com/api/v3/landing-point/nybro-sweden.json, accessed 2026-10-14 |
| E1 | Nynashamn, Sweden | — | Latvia-Sweden 1 (LV-SE 1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/nynashamn-sweden.json, accessed 2026-10-14 |
| E1 | Näsby, Sweden | — | GlobalConnect Aurora | E1: https://www.submarinecablemap.com/api/v3/landing-point/nsby-sweden.json, accessed 2026-10-14 |
| E1 | Oskarshamn, Sweden | — | Oskarshamn-Visby | E1: https://www.submarinecablemap.com/api/v3/landing-point/oskarshamn-sweden.json, accessed 2026-10-14 |
| E1 | Skalvik, Sweden | — | Kattegat 2 | E1: https://www.submarinecablemap.com/api/v3/landing-point/skalvik-sweden.json, accessed 2026-10-14 |
| E1 | Stavsnas, Sweden | — | BCS North - Phase 1, Sweden-Estonia (EE-S 1) | E1: https://www.submarinecablemap.com/api/v3/landing-point/stavsnas-sweden.json, accessed 2026-10-14 |
| E1 | Stockholm, Sweden | — | Baltic Sea Submarine Cable, Eastern Light Sweden-Finland I, Sweden-Latvia | E1: https://www.submarinecablemap.com/api/v3/landing-point/stockholm-sweden.json, accessed 2026-10-14 |
| E1 | Umeå, Sweden | — | Botnia | E1: https://www.submarinecablemap.com/api/v3/landing-point/ume-sweden.json, accessed 2026-10-14 |
| E1 | Uto, Sweden | — | GlobalConnect Aurora | E1: https://www.submarinecablemap.com/api/v3/landing-point/uto-sweden.json, accessed 2026-10-14 |
| E1 | Varberg, Sweden | — | Energinet Laeso-Varberg | E1: https://www.submarinecablemap.com/api/v3/landing-point/varberg-sweden.json, accessed 2026-10-14 |
| E1 | Visby, Sweden | — | GlobalConnect Aurora, Oskarshamn-Visby, Västervik-Visby | E1: https://www.submarinecablemap.com/api/v3/landing-point/visby-sweden.json, accessed 2026-10-14 |
| E1 | Västervik, Sweden | — | Västervik-Visby | E1: https://www.submarinecablemap.com/api/v3/landing-point/vstervik-sweden.json, accessed 2026-10-14 |
| E1 | Ystad, Sweden | — | Baltica | E1: https://www.submarinecablemap.com/api/v3/landing-point/ystad-sweden.json, accessed 2026-10-14 |
| E1 | Östhammar, Sweden | — | Mjolner West (planned, RFS 2027) | E1: https://www.submarinecablemap.com/api/v3/landing-point/sthammar-sweden.json, accessed 2026-10-14 |
| E2 | DE-CIX Stockholm | Stockholm | https://www.de-cix.net/en/locations/stockholm | E2: https://www.peeringdb.com/ix/5052, accessed 2026-10-14 |
| E2 | Equinix Stockholm | Stockholm | https://www.equinix.se/services/interconnection-connectivity/internet-exchange | E2: https://www.peeringdb.com/ix/1923, accessed 2026-10-14 |
| E2 | GIX Gothenburg | Gothenburg | http://www.gix.se | E2: https://www.peeringdb.com/ix/146, accessed 2026-10-14 |
| E2 | KeFF-IX | Stockholm, Gothenburg, Malmö, Amsterdam | https://ix.se | E2: https://www.peeringdb.com/ix/4381, accessed 2026-10-14 |
| E2 | Netnod Gothenburg -- MTU1500 | Gothenburg | http://www.netnod.se | E2: https://www.peeringdb.com/ix/192, accessed 2026-10-14 |
| E2 | Netnod Gothenburg -- MTU4470 | Gothenburg | http://www.netnod.se | E2: https://www.peeringdb.com/ix/2865, accessed 2026-10-14 |
| E2 | Netnod Lulea -- MTU9K | Lulea | http://www.netnod.se | E2: https://www.peeringdb.com/ix/257, accessed 2026-10-14 |
| E2 | Netnod Stockholm BLUE -- MTU1500 | Stockholm | http://www.netnod.se | E2: https://www.peeringdb.com/ix/2846, accessed 2026-10-14 |
| E2 | Netnod Stockholm BLUE -- MTU4470 | Stockholm | http://www.netnod.se | E2: https://www.peeringdb.com/ix/2847, accessed 2026-10-14 |
| E2 | Netnod Stockholm GREEN -- MTU1500 | Stockholm | http://www.netnod.se | E2: https://www.peeringdb.com/ix/70, accessed 2026-10-14 |
| E2 | Netnod Stockholm GREEN -- MTU4470 | Stockholm | http://www.netnod.se | E2: https://www.peeringdb.com/ix/2845, accessed 2026-10-14 |
| E2 | Netnod Sundsvall -- MTU1500 | Sundsvall / Gavle | http://www.netnod.se | E2: https://www.peeringdb.com/ix/194, accessed 2026-10-14 |
| E2 | Netnod Sundsvall -- MTU4470 | Sundsvall / Gavle | http://www.netnod.se | E2: https://www.peeringdb.com/ix/2869, accessed 2026-10-14 |
| E2 | Norrnod | Umea | http://www.norrnod.se | E2: https://www.peeringdb.com/ix/258, accessed 2026-10-14 |
| E2 | SOLIX MTU1500 | Stockholm | https://www.sol-ix.net | E2: https://www.peeringdb.com/ix/128, accessed 2026-10-14 |
| E2 | SOLIX MTU4470 | Stockholm | https://www.sol-ix.net | E2: https://www.peeringdb.com/ix/3702, accessed 2026-10-14 |
| E2 | SONIX Gothenburg | Gothenburg | https://sonix.network | E2: https://www.peeringdb.com/ix/3745, accessed 2026-10-14 |
| E2 | SONIX Malmo | Malmö | https://sonix.network | E2: https://www.peeringdb.com/ix/4292, accessed 2026-10-14 |
| E2 | SONIX Stockholm | Stockholm | https://sonix.network | E2: https://www.peeringdb.com/ix/3607, accessed 2026-10-14 |
| E2 | STHIX - Gothenburg | Gothenburg | http://www.sthix.net | E2: https://www.peeringdb.com/ix/1868, accessed 2026-10-14 |
| E2 | STHIX - Stockholm | Stockholm | http://www.sthix.net | E2: https://www.peeringdb.com/ix/172, accessed 2026-10-14 |
| E2 | STHIX - Sundsvall | Sundsvall | https://www.sthix.net | E2: https://www.peeringdb.com/ix/2677, accessed 2026-10-14 |
| E2 | STHIX - Umeå | Umeå | https://www.sthix.net | E2: https://www.peeringdb.com/ix/2785, accessed 2026-10-14 |

Counts: E1 28 (in service 25, planned-only 3, unverified 0), E2 23, E3 0; no-landing no; single-landing no; single-exchange no.

## Method

- Fetched 2026-10-14 with the link checker's HTTP client (`national_ai_note.probe`'s user agent): the map's landing-point index and each of the 319 landing-point pages the index labels with a member state; PeeringDB's exchange list for each of the 27 country codes; IXP-DB's provider list; the Latvian statute page the registry already holds. Every landing point and every exchange those lists give is a row, with no selection, which is why IT has 55 E1 rows and DE 59 E2 rows. The rows were written by a script from the fetched JSON, the Counts lines by `./run.sh entry-points counts` from the rows.
- E1: 319 rows. Six states have no landing point on the map (AT, CZ, HU, LU, SK, SI) and the row says so; two have one (PL, RO). Two planned cables, ANDROMEDA at Chania and at Genoa, have no year on the map and read (planned). The map's label rule puts "Kralendijk, Bonaire, Netherlands" under NL and "Girne, Cyprus" under CY, as the Definitions say; the note does not re-draw that line.
- E2: 299 rows. The Place cell is PeeringDB's city field as written ("Klagenfurt/Villach", "Innsbruck/Tirol"). RZ-IX (PL) has no website in PeeringDB and reads —. Malta: PeeringDB lists no exchange and the row says so; IXP-DB names "MIX (Malta internet Exchange)", which no row carries because IXP-DB has no page per exchange.
- IXP-DB cross-check: its provider list, fetched the same day, was read against PeeringDB's rows state by state. The two databases name one exchange differently ("SIX (Slovenian Internet Exchange)" in IXP-DB, "SIX SI" in PeeringDB) and split or merge LANs differently, so a name match is loose and the comparison was read, not counted; no row comes from IXP-DB, and no figure from it is kept.
- E3: one row, Article 32 of Latvia's National Cybersecurity Law, whose page the registry already holds for indicator LV:L1 (the "single state internet exchange point"). No other statute or regulator page was searched for; a state without an E3 row has not been searched, which is why E3 has no "none" row.
- The `ixp` column of `model/eu27_parameters.csv`, unsourced text from the first commit, was read once as a list of names to look for and is not copied. Names in it that no fetched page carries, as a place, an exchange or a cable: Tamares (CY), Lyngby (DK), Estlink (EE, a power link), Helsinki-Rostock (FI; the map names the cable C-Lion1), Vendée and Brittany (FR), Norden (DE), Crete and Attica (EL; the map names the towns), Kinsale (IE), LVRTC (LV), Kaunas (LT), Teralink (LU), Egmond and Katwijk (NL), Constanța (RO), ARNES and Koper (SI).
- Link check: every URL in the note was fetched once into `docs/internet-entry-points-links.csv` on 2026-10-14 (`links`, six at a time); PeeringDB answered 429 to 162 of its 299 pages at that pace, and `retry` re-probed them one at a time with a pause until each answered. Every basis page (the 319 map JSON pages, the 299 PeeringDB pages, the statute) and the two definition pages answered 2xx; no row is [unverified]. Of the E2 website cells, which are PeeringDB's field and no basis, 47 did not answer (31 unreachable, 12 refused with 403, 2 not found, 2 bad request); the register holds each answer, and those rows stand on their PeeringDB page.
- Reviews. Second-agent review, same model (claude-fable-5-1, fresh context, 2026-10-14): confirmed the E1 rows against the map's live index, 319 of 319, and every Counts line; found that the licence sentence said more than the map's code and that 162 PeeringDB pages had answered 429 at the first link check, both corrected. Cross-model check (claude-opus-5-5, 2026-10-14, #87's standard): 646 fresh fetches, all 200; every E1 row's name and cable list, with planned marking, against its JSON page, 319 of 319; every E2 row's name, place and website against its PeeringDB page and the API, 299 of 299; the E3 phrase on the statute page; the seven "none" rows true; all 27 Counts lines recomputed two ways; zero discrepancies. It asked for the wording on the French outermost regions, Bonaire and the offshore platforms, now in the E1 definition. No person has read it.
