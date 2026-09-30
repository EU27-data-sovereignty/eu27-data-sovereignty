// The EU-27 country report — one A4 PDF, every member state, in EU colours.
//
// Separate from style.typ on purpose: that file is mono by decision (DECISIONS.md #28),
// and #28 keeps full colour for the PDF and web editions, which is what this is. Colour
// here is decoration and wayfinding only — no figure, rating or state is told apart by
// hue, so the report still reads correctly when printed in black and white.
//
// Colours and type come from tokens.typ, generated from design/tokens.json (#74). EU blue and
// gold only: no circle of stars, flag or other official mark (#50, #76).
#import "/templates/tokens.typ": *

#let report(title: "", subtitle: "", generated: "", provenance: "", kicker: "EU-27 · Country report", body) = {
  set document(title: title, author: "Pieter de Jong")
  set text(font: ("Libertinus Serif", "Georgia", "Times New Roman"), size: 10pt, fill: ink, lang: "en")
  set par(justify: true, leading: 0.62em, spacing: 0.95em)
  set heading(numbering: none)

  show link: set text(fill: eu-blue)
  show raw: set text(font: ("Menlo", "DejaVu Sans Mono"), size: 8.5pt)
  show strong: set text(fill: eu-deep)

  // ---- Cover: full-bleed EU blue, a gold rule, no emblem (#76). ----
  page(paper: "a4", margin: 0pt, fill: eu-blue)[
    #set text(fill: white)
    #v(92mm)
    #block(width: 100%, height: 2.4mm, fill: eu-gold)
    #v(20mm)
    #pad(x: 26mm)[
      #block[
        #set text(size: 9pt, tracking: 2pt, fill: eu-gold)
        #upper(kicker)
      ]
      #v(3mm)
      #block[
        #set text(size: 30pt, weight: "regular", tracking: 0.2pt)
        #set par(justify: false, leading: 0.45em)
        #title
      ]
      #v(4mm)
      #block[
        #set text(size: 12pt)
        #set par(justify: false)
        #subtitle
      ]
      #v(1fr)
    ]
    #place(bottom + left, dx: 26mm, dy: -22mm)[
      #set text(size: 8pt)
      #set par(justify: false)
      #box(width: 158mm)[
        Independent research, not affiliated with the European Union or any member-state
        government. Scaled working assumptions, not sourced forecasts. Generated #generated.
      ]
    ]
  ]

  // ---- Interior ----
  set page(
    paper: "a4",
    margin: (x: 22mm, top: 24mm, bottom: 24mm),
    // Decision #25: provenance on every page, not only in the front matter.
    header: context {
      let here-page = here().page()
      let chapters = query(heading.where(level: 1)).filter(h => h.location().page() <= here-page)
      set text(size: 7pt, fill: quiet, tracking: 0.8pt)
      grid(
        columns: (auto, 1fr, auto),
        align: (left + horizon, center, right + horizon),
        box(width: 8mm, height: 2.2mm, fill: eu-blue),
        [],
        if chapters.len() > 0 { upper(chapters.last().body) },
      )
    },
    footer: context {
      set text(size: 6.5pt, fill: quiet)
      line(length: 100%, stroke: 0.3pt + rule)
      v(2pt)
      grid(
        columns: (1fr, auto),
        align: (left, right),
        text(provenance),
        text(fill: eu-blue, weight: "bold", str(counter(page).get().first())),
      )
    },
  )
  counter(page).update(1)

  // Chapter: one per country, always on a new page, with a blue band and gold rule.
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    block(width: 100%, fill: eu-blue, inset: (x: 8mm, y: 7mm), radius: 1.5pt)[
      #set text(fill: white, size: 22pt, weight: "regular")
      #it.body
    ]
    v(-1.2mm)
    block(width: 100%, height: 1.6mm, fill: eu-gold)
    v(4mm)
  }
  show heading.where(level: 2): it => {
    v(4mm)
    block(breakable: false, sticky: true)[
      #set text(size: 12.5pt, weight: "bold", fill: eu-blue)
      #it.body
      #v(-2.5mm)
      #line(length: 100%, stroke: 0.5pt + eu-gold)
    ]
    v(0.5mm)
  }
  show heading.where(level: 3): it => {
    v(2mm)
    block(sticky: true, text(size: 10.5pt, weight: "bold", fill: eu-deep, it.body))
  }
  show heading.where(level: 4): it => block(sticky: true, text(weight: "bold", it.body))

  // Tables: blue header row, light wash banding, thin rules — readable in mono too.
  set table(
    stroke: (x, y) => if y == 0 { (bottom: 0.8pt + eu-blue) } else { (bottom: 0.3pt + rule) },
    fill: (x, y) => if y == 0 { wash } else { none },
    inset: (x: 5pt, y: 3.6pt),
  )
  show table.cell.where(y: 0): set text(weight: "bold", size: 8.5pt, fill: eu-deep)
  show table: set text(size: 8.5pt)
  show table: set par(justify: false)
  show figure.where(kind: table): set block(breakable: true)
  show figure: set align(left)

  show quote.where(block: true): it => block(
    width: 100%, fill: wash, inset: (left: 9pt, right: 8pt, y: 7pt),
    stroke: (left: 2.5pt + eu-gold),
    text(size: 9pt, it.body),
  )

  // Contents: countries only, with dotted leaders and the page in blue.
  // Footnotes carry the sources (#75): small, ruled off, numbered in blue.
  set footnote.entry(separator: line(length: 30%, stroke: 0.5pt + eu-blue), gap: 0.35em, indent: 0em)
  show footnote.entry: set text(size: 7pt, fill: ink)
  show footnote: set text(fill: eu-blue)

  show outline.entry.where(level: 1): it => {
    set text(size: 10.5pt)
    link(it.element.location(), it.indented(none, it.body() + box(width: 1fr, repeat[.#h(3pt)]) + text(fill: eu-blue, weight: "bold", it.page())))
  }

  body
}

#let standfirst(body) = {
  block(
    fill: wash,
    inset: (x: 8pt, y: 6pt),
    width: 100%,
    stroke: (left: 2.5pt + eu-blue),
    text(size: 8.5pt, body),
  )
  v(2mm)
}

// A table with no header row: labels in the first column, values beside them.
#let kvtable(..args) = {
  set table(fill: none, stroke: (x, y) => (bottom: 0.3pt + rule))
  show table.cell.where(y: 0): set text(weight: "regular", size: 8.5pt, fill: ink)
  show table.cell.where(x: 0): set text(weight: "bold", fill: eu-deep)
  table(..args)
}

#let notice(body) = block(
  width: 100%, fill: wash, inset: 10pt, radius: 1.5pt,
  stroke: 0.5pt + eu-blue,
  text(size: 9pt, body),
)

// A value withheld because no checked source supports it yet (#75). Grey italics: visible as a gap,
// never mistaken for a fact.
#let gap(body) = text(style: "italic", fill: quiet, body)

// Method notes, notices and gaps. Tone changes the rule colour only; the words say which it is.
#let callout(tone: "method", body) = block(
  width: 100%, fill: wash, inset: (left: 9pt, right: 8pt, y: 7pt),
  stroke: (left: 2.5pt + (if tone == "gap" { eu-gold } else { eu-blue })),
  text(size: 9pt, body),
)

// Sources appendix: one entry per source, then the claims that cite it with their quotes.
#let source-entry(n, body) = block(above: 1.1em, below: 0.4em, breakable: false,
  grid(columns: (9mm, 1fr), column-gutter: 2mm,
    text(weight: "bold", fill: eu-blue)[S#n], text(size: 8.5pt, body)))

// The quote as found, in its original language; then the machine translation, labelled as one, when
// the source is not in English; then the grade and checks (#82).
#let claim-entry(claim, quote, gloss, meta) = pad(left: 11mm, bottom: 0.3em, block(breakable: false)[
  #set text(size: 7.5pt)
  #text(font: print-mono, size: 6.5pt, fill: quiet, claim) \
  #emph(["#quote"])
  #if gloss != [] [ \ #text(fill: quiet)[Machine translation: "#gloss"]]
  \ #text(fill: quiet)[#meta]
])
