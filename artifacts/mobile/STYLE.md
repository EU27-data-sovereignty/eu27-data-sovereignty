# Mobile style

Covers the Expo Router reader in `mobile/` (#109). It renders the content model from the split edition inside
its binary and learns of a newer edition from one public, read-only bucket (#110, #111). It is not released:
no build, no store listing, no EAS, until the launch gate (#25, #50). The tokens are those of
[`../STYLE.md`](../STYLE.md), generated into `src/constants/Colors.ts` by `design/build_tokens.py`.

## The parity contract

This is the defining constraint of the app and the first thing to understand before editing it. Four things in
`mobile/` are derived from elsewhere and pinned:

| `mobile/` | derived from | pinned how |
|---|---|---|
| `assets/data/manifest.json` + 28 generated parts | `web/public/data/eu27.json`, by `model/export_json.py --split` | the manifest's `edition` is the bundle's sha256; each part's sha256 and size; `tests/test_export_split.py` (round trip) and `__tests__/parity.test.ts` (the binary ships what the manifest names) |
| `src/data/types.ts` | `web/src/data/types.ts` | byte for byte **below the header comment** |
| `src/data/format.ts` | `web/src/utils/format.ts` | byte for byte below the header comment |
| `src/data/sources.ts` | `web/src/data/sources.ts` | byte for byte below the header comment |
| `src/constants/Colors.ts` | `design/tokens.json`, by `design/build_tokens.py` | `build_tokens.py --check`, run by `tests/test_tokens.py` and `mobile/test.sh` |

Consequences:

- **Editing a pinned web file means copying it here in the same commit.** A helper added to `sources.ts` or
  `format.ts` is inherited by the app for free; that is the intended way to share presentation logic.
- **`./run.sh data` writes the parts and both manifests.** The parts are gitignored; a fresh checkout runs
  `mobile/run.sh parts` (or `init.sh`, or `test.sh`) before Metro can bundle them.
- **The suite runs in the gate.** `./test.sh --only mobile` and the `mobile` job of `gate.yml` run
  `mobile/test.sh --ci` (#113). A bundle change is not done until that passes.

## Structure

- **Five tabs:** Countries, Hosting (the infrastructure overview), Ranking, Method, Edition. The app is a
  reader, not the site: no `/ask`, no guides, no map.
- `app/(tabs)/index.tsx` is the index: a `FlatList` of all 27 from the edition's `index`, with a live text
  filter, sorted **alphabetically by name** (a filtered phone list is scanned by name), each row with the
  evidence counts the web's Countries page shows.
- `app/country/[iso].tsx` is a state's report: `DocumentView` over `documents[ISO]`, then its numbered sources.
  The state's part is loaded on demand (`useCountry`).
- `src/components/DocumentView.tsx` is the renderer, the port of the web's. **Nothing here adds a sentence.**
  `__tests__/document-view.test.tsx` checks that the text on screen minus the `[n]` marks is the spans' text.
- Every screen renders inside `Screen` (or a list with `ScreenFooter`), which appends `ProvenanceNotice` in the
  edition's own words. `tests/test_evidence.py` fails on a route without it.

## Presentation

- **Roles, drawn the same as on the web:** a fact in the primary colour with `[n]` marks in the accent, a gap
  in muted italics, a disputed value in muted italics with a dashed underline, a label or method sentence plain.
- **Tables are cards.** Each row of a content-model table is a card: the first column's label as a kicker, the
  first cell as the title, every other cell as a `column: cell` line, each through `SpanView`.
- **Callouts** keep the web's three tones: method (teal wash), gap (the gap mark), notice (the accent).
- **No score anywhere.** The ranking shows groups by label and each state's range as a five-cell bar; no chip
  carries a numeral (`__tests__/screens.test.tsx`).
- Figures are formatted with the inherited `format.ts` helpers, never re-implemented.
- **Flag emoji** appear in the country list only, beside the name, never instead of it, and hidden from the
  screen reader (#61). No state emblem anywhere else. The icons are plain EU-blue tiles with a gold square, not
  the circle of stars (#76).
- Fonts are the system's in this cut; the web's Manrope is a follow-up.

## Data access

`src/data/bundled.ts` `require()`s the 28 parts, each behind a function. The one network path is
`src/edition/expoFiles.ts` (`File.downloadFileAsync`), with URLs built only in `src/services/channel.ts` from
the configured Supabase project, and only when the reader taps "Check for a newer edition" or has opted in to
the check at launch. Every downloaded file is hashed before it is parsed; a downloaded part is re-hashed on
every read (`src/edition/EditionStore.ts`). `__tests__/security.test.ts` holds these as the lines they are.

## Verify

```
./test.sh --only mobile                       # from the repo root: the gate's stage
cd mobile && ./test.sh --quick                # the developer loop
cd mobile && ./test.sh --integration          # the edition channel against local Supabase (colima start; supabase start)
cd mobile && npx expo start                   # then `w` for web, or `i` for the iOS simulator
```

After any bundle change: `./run.sh data`, then `./test.sh --only mobile`.
