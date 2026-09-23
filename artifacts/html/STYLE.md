# HTML style

Covers the React + Vite app in `web/`, which is also the renderer behind two of the PDF/PNG
outputs — the 27 briefing PDFs and the 27 posters are headless Chrome printing the `/country/:iso`
and `/poster/:iso` routes (#42). **A change to the app's styling changes tracked binaries.** See
[`../pdf/STYLE.md`](../pdf/STYLE.md) and [`../png/STYLE.md`](../png/STYLE.md).

Stack is pinned and not negotiable per-feature: React 19, Vite 6, TypeScript 5.7, Vitest 3,
ESLint 9 flat config (#18), Tailwind (#20). Known bugs in the upstream template were deliberately
not copied (#19).

## Colour

The design system is **upstream**: "Warm Neutral + Terracotta", defined in
`~/dev/design/DESIGN_SYSTEMS.md` (#21). `web/src/styles/index.css` implements it. This guide
records only the project's deltas and the rules for working inside it.

**Raw → semantic token split.** Raw hexes are defined once in the `@theme` block; everything
downstream refers to a *role*, never a colour name.

```css
--color-clay: #d97757;               /* raw: defined once */
--color-accent: var(--color-clay);   /* semantic: what everything else uses */
```

Writing a hex value anywhere outside that block is a bug. Swapping the palette should touch one
block.

**Delta from the upstream system, with its measurement.** The system lists `#898781` for muted
foreground. On this page that measures **3.21:1** — acceptable for axis ticks, which are graphical
and need 3:1, but failing WCAG AA as body text. It is darkened to `#6f6d66` (**4.63:1**) so the
same token is safe everywhere it is used. Any further delta gets the same treatment: measure,
record the ratio, say what it is safe for.

**Dark mode is selected, not inverted.** Its steps are re-derived and separately validated against
the dark surface. Every token is redefined in both the `prefers-color-scheme` block *and* the
`[data-theme='dark']` block, so an explicit toggle wins over the OS in both directions. Adding a
token means adding it three times — light, media-query dark, attribute dark. Missing one is
invisible until someone toggles.

## Charts

`web/src/utils/palette.ts` is validated, not eyeballed, and its header records the actual
validator output. Two constraints the validation imposed, which constrain how the slots may be
used:

- Dark tritan separation for yellow↔aqua is dE 4.0, below the 6–8 floor. Legal **only** with
  secondary encoding, so any chart using both slots must also carry direct labels or a table view.
- Light-mode contrast warns for aqua (2.67) and yellow (2.06). Same relief applies.

Every chart in the app ships with a table view, which is what satisfies both. **Re-run the
validator before changing any value**; `test.sh` checks the recorded checksum, so a silent edit
fails.

Categorical order is fixed and never cycled. A fifth series folds into "Other" rather than
extending the ramp.

Other chart rules, each a decision:

- **Heatmaps are `<table>` elements with a `<button>` per cell, not SVG `<rect>` grids** (#29).
  They get keyboard navigation, screen-reader semantics and text zoom for free.
- **D3 is a maths library here, not a charting library** (#30). Use its scales and shape
  generators; render with React. No `d3.select` into the DOM.
- **No Three.js and no 3D** (#31).
- **No composite sovereignty score** (#10). Show the columns; do not add them up. Any rating shown
  is labelled as the author's judgement in the same view.

## Layout and type

- Body is Inter with a system fallback stack, `--text-body` 14px; `--text-axis` 11px for ticks,
  `--text-stat` 30px for the single large figure in a stat tile.
- **The page never scrolls sideways.** Wide content goes in a `.scroll-x` container that scrolls
  inside itself.
- Numeric columns use `tabular-nums` and right alignment, so figures compare down the column.

## Accessibility

The floor is **zero axe violations at wcag2a, wcag2aa, wcag21a and wcag21aa**, asserted across
every route in `web/e2e/app.spec.ts`. This is a gate, not an aspiration — accessibility defects
here are found by testing rather than by review (#35), because review kept missing them.

Working rules that follow from it:

- Heading levels never skip. One `<h1>` per page.
- `:focus-visible` is styled globally; do not remove an outline without replacing it.
- Every interactive element has an accessible name. Icons and decorative glyphs —
  **including country flag emoji** — take `aria-hidden="true"` and sit beside a real text label,
  never instead of one.
- A new route must be added to the `ROUTES` array in `web/e2e/app.spec.ts` or it is untested.
  `/poster/:iso` is deliberately absent: it is an export target, not a page.
- Colour is never the only encoding. See the chart constraints above.

## Print

`@media print` hides `.no-print` and forces a white background with black text, because these
routes are printed to PDF. Anything added to the page that should not appear in the briefing PDF
needs `.no-print`.

## Verify

```
cd web && npm run lint && npm run type-check && npm run test
./test.sh                # includes the full e2e + axe sweep
./run.sh artefacts       # re-render the 54 tracked binaries if the app's rendering changed
```
