// The EU-27 country report — one A4 PDF, every member state, in EU colours.
//
// Separate from style.typ on purpose: that file is mono by decision (DECISIONS.md #28),
// and #28 keeps full colour for the PDF and web editions, which is what this is. Colour
// here is decoration and wayfinding only — no figure, rating or state is told apart by
// hue, so the report still reads correctly when printed in black and white.
//
// EU flag colours: Reflex Blue #003399 and Yellow #FFCC00 (the European Commission's
// published flag specification).

#let eu-blue   = rgb("#003399")
#let eu-gold   = rgb("#FFCC00")
#let eu-deep   = rgb("#00205B")
#let eu-wash   = rgb("#EEF2FA")
#let ink       = luma(20)
#let quiet     = luma(120)
#let rule      = luma(205)

// A five-pointed star centred at (0, 0) with outer radius r.
#let _star(r, fill) = {
  let pts = range(10).map(i => {
    let a = -90deg + i * 36deg
    let rr = if calc.rem(i, 2) == 0 { r } else { r * 0.382 }
    (rr * calc.cos(a), rr * calc.sin(a))
  })
  polygon(fill: fill, stroke: none, ..pts)
}

// The twelve stars in a circle, as on the flag. `size` is the ring's diameter.
#let eu-stars(size: 60mm, fill: eu-gold) = box(width: size, height: size, {
  let ring = size / 3
  let r = size / 18
  for i in range(12) {
    let a = -90deg + i * 30deg
    place(
      dx: size / 2 + ring * calc.cos(a) - r,
      dy: size / 2 + ring * calc.sin(a) - r,
      box(width: 2 * r, height: 2 * r, place(dx: r, dy: r, _star(r, fill))),
    )
  }
})

#let report(title: "", subtitle: "", generated: "", provenance: "", body) = {
  set document(title: title, author: "Pieter de Jong")
  set text(font: ("Libertinus Serif", "Georgia", "Times New Roman"), size: 10pt, fill: ink, lang: "en")
  set par(justify: true, leading: 0.62em, spacing: 0.95em)
  set heading(numbering: none)

  show link: set text(fill: eu-blue)
  show raw: set text(font: ("Menlo", "DejaVu Sans Mono"), size: 8.5pt)
  show strong: set text(fill: eu-deep)

  // ---- Cover: full-bleed EU blue, the circle of stars, no footer. ----
  page(paper: "a4", margin: 0pt, fill: eu-blue)[
    #set text(fill: white)
    #v(38mm)
    #align(center, eu-stars(size: 74mm))
    #v(22mm)
    #pad(x: 26mm)[
      #block[
        #set text(size: 9pt, tracking: 2pt, fill: eu-gold)
        #upper("EU-27 · Country report")
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
    fill: (x, y) => if y == 0 { eu-wash } else { none },
    inset: (x: 5pt, y: 3.6pt),
  )
  show table.cell.where(y: 0): set text(weight: "bold", size: 8.5pt, fill: eu-deep)
  show table: set text(size: 8.5pt)
  show table: set par(justify: false)
  show figure.where(kind: table): set block(breakable: true)
  show figure: set align(left)

  show quote.where(block: true): it => block(
    width: 100%, fill: eu-wash, inset: (left: 9pt, right: 8pt, y: 7pt),
    stroke: (left: 2.5pt + eu-gold),
    text(size: 9pt, it.body),
  )

  // Contents: countries only, with dotted leaders and the page in blue.
  show outline.entry.where(level: 1): it => {
    set text(size: 10.5pt)
    link(it.element.location(), it.indented(none, it.body() + box(width: 1fr, repeat[.#h(3pt)]) + text(fill: eu-blue, weight: "bold", it.page())))
  }

  body
}

#let standfirst(body) = {
  block(
    fill: eu-wash,
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
  width: 100%, fill: eu-wash, inset: 10pt, radius: 1.5pt,
  stroke: 0.5pt + eu-blue,
  text(size: 9pt, body),
)
