# PNG style

Covers the 27 `countries/<ISO>/<ISO>-infographic.png` posters — one page per member state, meant
to be shared on its own.

They are **not illustrations.** Headless Chrome screenshots the app's `/poster/:iso` route, which
renders from `web/public/data/eu27.json`, so every figure on a poster comes from the model and a
poster cannot disagree with its brief (#47). Their styling is therefore the app's styling; see
[`../html/STYLE.md`](../html/STYLE.md). `web/src/pages/Poster.tsx` is the layout.

This is the deliberate opposite of `countries/NL/Rijkscloud-…png`, whose grid routing, cable
landings and growth curves were drawn by an image model and derive from nothing in this repository
— and which still shows PUE 1.70 against the model's 1.25 (#48). That file is labelled wherever it
is referenced; see `ASSETS.md`.

## The two rules from the security audit

Both are constraints on the layout, and both hold for anything added to it.

1. **No state emblems, flags, crowns or official-looking wordmarks.** These are concept posters
   for a programme that exists in no member state, and they say so. Country flag emoji are
   permitted in tables of contents and navigation elsewhere in the project; **a poster is not
   navigation**, and they do not appear here.
2. **The caveat is printed on the poster.** An image gets shared without the page that explains
   it, so the disclaimer has to travel with the pixels. `Poster.tsx` carries it as
   *"Working assumptions, not forecasts."* plus the provenance line. Do not move it into a
   surrounding page, shrink it below legibility, or make it conditional.

## Geometry

- Width is fixed at **1024 px** (`POSTER_W`).
- **Height is measured per country, not fixed.** Region counts vary from two to five, so a fixed
  height would clip Romania or leave Malta two-thirds blank. `Poster.tsx` stamps
  `data-poster-height` on the rendered DOM and the exporter reads it back, falling back to 1400
  only if the measurement fails.
- Sections are numbered `1 ·` … `7 ·` and carry one idea each. A poster that needs an eighth
  section is a brief, not a poster.

## Rendering constraints

- The app renders client-side, so Chrome is given `--virtual-time-budget`. Without it the capture
  is a loading message — indistinguishable from success until someone opens the file.
- `/poster/:iso` renders **outside** the app's `Layout`, so it has no nav, no banner and no site
  chrome. Do not add any.
- The route is deliberately absent from the `ROUTES` array in `web/e2e/app.spec.ts`: it is an
  export target, not a page. That means **axe does not cover it** — accessibility of the poster is
  the accessibility of a picture, and the brief is the accessible equivalent.
- Chrome writes no `tIME` or `tEXt` chunk into a screenshot PNG, so unlike the PDFs these need no
  date rewriting to be byte-reproducible.

## Tracked, and detectably stale

The posters are committed (#24, #51). `countries/ARTEFACTS.csv` records each one's sha256 together
with the sha256 of the bundle it was rendered from (#52), and `tests/test_artifacts.py` fails when
the bundle has moved on — the only way to catch a tracked binary that CI cannot rebuild.

**Re-render all 27 in full, never a subset.** `write_manifest()` refreshes the bundle hash only for
the paths it actually rendered, so exporting just the PDFs leaves all 27 posters carrying a stale
`bundle_sha256` and the suite red on half the manifest.

## Verify

```
./run.sh artefacts                        # all 27 posters and 27 briefing PDFs
python3 -m unittest tests.test_artifacts -v
git diff --stat -- countries/             # expected: only the files you meant to move
```

Then open two posters by eye — one large state and one small (DE and MT) — and check the height
measurement held, the caveat is legible, and no emblem crept in.
