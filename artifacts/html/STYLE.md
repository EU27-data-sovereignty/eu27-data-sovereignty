# HTML style

Shared look: [`../STYLE.md`](../STYLE.md). This file covers what is specific to the React + Vite app in
`web/`. The app is also the renderer behind the 27 posters (`/poster/:iso`, see
[`../png/STYLE.md`](../png/STYLE.md)), so **a change to its styling changes tracked binaries.**

Stack: React 19, Vite, TypeScript, Vitest, ESLint flat config (#18), Tailwind 4 (#20).

## Colour

Tokens are generated into `web/src/styles/tokens.css` from `design/tokens.json`; never edit that file.
Components use role variables (`var(--color-fg-secondary)`), never hex values; `tests/test_tokens.py`
fails on a hex literal in a component. A new role is added to `design/tokens.json` in both themes and,
if it carries text, to the generator's contrast pairs.

## Pages and components

- **`DocumentView`** renders the content model; **`SpanView`** renders one span (fact with its `[n]`
  markers, or gap in muted italics); **`SourceList`** renders the numbered sources. Every page that shows
  facts uses these three, so facts, gaps and sources look the same everywhere.
- **Source numbering** is per page, in first-citation order (`numberSources` in `web/src/data/sources.ts`).
- **The ranking page** uses the map (`charts/EuMap.tsx`, shapes loaded only on that page), the group
  ladder and the indicator grid. The ladder is the table view of the map.
- **`/ask`** streams server-sent events from `/api/ask` and resolves each citation to claims and sources
  from the bundle (#78).

## Charts

- **D3 is a maths library here, not a charting library** (#30). Use its scales and projections; render
  with React. No `d3.select` into the DOM.
- **No Three.js and no 3D** (#31).
- **Tables before charts** (#29). Every chart has a text or table equivalent on the same page.
- `web/src/utils/palette.ts` still holds the validated chart palette for any future data chart; re-run
  the validator before changing it (`test.sh` checks its checksum).

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
- Long unbreakable strings (hashes, claim ids, URLs) wrap: the page never scrolls sideways at 375 px.
- Colour is never the only encoding. See the chart constraints above.

## Print

`@media print` hides `.no-print` and prints black on white. The PDFs no longer come from the web app
(#76); print styling is only for a reader printing a page.

## Verify

```
cd web && npm run lint && npm run type-check && npm run test
./test.sh                # includes the full e2e + axe sweep
./run.sh artefacts       # re-render the 27 tracked posters if the app's rendering changed
```
