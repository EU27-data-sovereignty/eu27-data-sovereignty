# Mobile style

Covers the Expo Router reader in `mobile/`. It is local only — never built for a store, never
deployed. It exists so the same document can be read on a phone without a network.

## The parity contract

This is the defining constraint of the mobile app and the first thing to understand before
editing it. Three files in `mobile/` are **copies** of files in `web/`:

| `mobile/` | copied from | pinned how |
|---|---|---|
| `assets/data/eu27.json` | `web/public/data/eu27.json` | byte for byte |
| `src/data/types.ts` | `web/src/data/types.ts` | byte for byte **below the header comment** |
| `src/data/format.ts` | `web/src/utils/format.ts` | byte for byte **below the header comment** |

`mobile/__tests__/parity.test.ts` turns drift into a failed test instead of an app that quietly
reports last month's figures. Only the leading block comment may differ, since each copy says
where it came from.

Two consequences:

- **Editing `web/src/utils/format.ts` or `web/src/data/types.ts` means editing the mobile copy in
  the same commit.** A shared helper added to `format.ts` is inherited by mobile for free — that
  is the intended way to share presentation logic between the two renderers.
- **`./run.sh data` does not copy the bundle.** Nothing does: `run.sh`, `init.sh`, `test.sh` and
  `.github/workflows/ci.yml` contain no reference to `mobile/`. After any bundle change, copy it
  by hand and run the mobile suite, or the drift ships.

**The mobile suite runs in neither `./test.sh` nor CI.** It runs only from `mobile/`. Treat
`cd mobile && npm test` as a required step of any change that touches the bundle or the two
pinned TypeScript files, not as an optional extra.

## Structure

- Two tabs and no more: **Countries** and **Methodology**. The app is a reader, not the site.
- `app/(tabs)/index.tsx` is the index — a `FlatList` of all 27 with a live text filter, sorted
  **alphabetically by name**, with an EU-27 totals header. Note this differs from the web
  `/countries` table and the book gazetteer, which both sort by descending design MW. That is
  deliberate: a filtered phone list is scanned by name, a ranked table is read by size.
- `app/country/[iso].tsx` is the country screen: numbered sections via a local `Section`
  component.

**The section list is asserted, not just rendered.** `mobile/__tests__/screens.test.tsx` iterates
an explicit list of section titles and fails if one is missing. Adding, renaming or reordering a
section means editing that list in the same commit. This is a feature — it is what keeps the
mobile screen from silently falling behind the web page.

Section parity with web is the goal but not currently exact. As of 2026-09-21 mobile has ten
sections and web nine: mobile carries **Sovereignty matrix**, which the web country page does not,
so the numbering diverges from there on. Both end with **Critical national data in scope**. Do not
widen that gap without deciding to.

## Presentation

- Figures are formatted with the inherited `format.ts` helpers — never re-implemented locally,
  never hand-formatted inline. That file is the parity-pinned one, so a local reimplementation is
  both a drift risk and invisible to the test that would catch it.
- The country list may carry **country flag emoji** beside the name: it is an index, which is the
  one place flags are permitted (#47, extended). The flag is decorative and sits beside the name,
  never instead of it — the filter matches on the name, and a screen reader must announce the
  name.
- No state emblems anywhere else in the app.

## Data access

`src/data/bundle.ts` `require()`s the committed JSON at module scope. There is no fetch, no API
and no network path for model data; `src/services/supabase.ts` exists but the bundle deliberately
does not go through it. Keep it that way — the offline property is the reason the app exists.

## Verify

```
cd mobile && npm test        # parity + screens; NOT run by ./test.sh or CI
cd mobile && npx expo start  # then `w` for web, or scan the QR code
```

After any bundle change:

```
cp web/public/data/eu27.json mobile/assets/data/eu27.json
cd mobile && npm test
```
