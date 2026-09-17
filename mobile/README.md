# `mobile/` — the Expo reader

A phone reader for the 27 country cases. One app, with the country as data rather than as a build
flavour: pick a member state, read its capacity, legal posture, provider landscape and migration
path, switch to another.

**Local only.** No build, no store listing, no deploy. `vercel.json` builds `web/` and
`.vercelignore` excludes this directory, so nothing here ships anywhere. A public release is gated
on the same verification work as search indexing and the `eu27.cloud` domain — see `VERIFICATION.md`
and `DECISIONS.md` #25.

```bash
./init.sh        # npm ci, and an .env.local you do not need
./run.sh web     # or ios / android / start
./run.sh test    # jest + npm audit
```

## Where the data comes from

`assets/data/eu27.json` is a copy of `web/public/data/eu27.json`, the bundle written by
`model/export_json.py` from the model CSVs. It is ~288 KB, and every screen is a pure function of
it, so the app ships it whole: no API, no first-run fetch, no difference between offline and online.
`src/data/types.ts` and `src/data/format.ts` are likewise copies, of `web/src/data/types.ts` and
`web/src/utils/format.ts`.

Copies drift, so `__tests__/parity.test.ts` fails if any of the three stops matching its original.
After `./run.sh data` at the repo root, copy the bundle across again:

```bash
cp ../web/public/data/eu27.json assets/data/eu27.json
```

## Screens

| Route | What it is |
|---|---|
| `app/(tabs)/index.tsx` | All 27 countries, filterable, with design load and CAPEX |
| `app/country/[iso].tsx` | One country in nine sections, mirroring `web/src/pages/Country.tsx` |
| `app/(tabs)/methodology.tsx` | Provenance, assumptions, and the not-yet-verified notice |

The section order on the country screen is the argument, and it is deliberately identical to the
web page's. Keeping them in step is what stops the two from becoming different documents.

Colours are the Warm Neutral + Terracotta tokens from `web/src/styles/index.css`, ported to
`src/constants/Colors.ts`. Light and dark are both defined; dark is re-derived, not inverted.

## Security and privacy

The app has no accounts, no analytics, no telemetry and no crash reporting, collects nothing, and
in its default configuration makes no network request at all. On the device it stores one thing:
the ISO code of the last country viewed.

`__tests__/security.test.ts` asserts each of those rather than trusting them:

- **No capabilities.** `android.permissions` is empty, `ios.infoPlist` declares no usage strings,
  and cleartext traffic is refused.
- **No publishable secrets.** Expo inlines every `EXPO_PUBLIC_*` variable into the shipped
  JavaScript, so only the Supabase URL and anon key may ever be named there — a service-role key
  would be published to every install. Secret-shaped names fail the test, and `.env.template` ships
  no values.
- **A dependency allowlist**, not a denylist: analytics and ad SDKs arrive under names nobody
  predicts. Anything outside the list fails the build, and `./run.sh test` also runs
  `npm audit --audit-level=high`.
- **No hardcoded hosts**, and one storage key.

`__tests__/screens.test.tsx` renders the list and the country screen and asserts the model's real
figures appear — the NL reference case at 5,691 servers and 14.2 MW — because a screen wired to a
placeholder passes any test that only checks for the absence of an exception.

`__tests__/parity.test.ts` additionally asserts the bundle names no individual. The institutional
map is public; named people live in the separate private contacts repo (`DECISIONS.md` #26, #49),
and the app is exactly where such a leak would ship.

## Supabase

`src/services/supabase.ts` is wired and idle. Nothing reads from it: unconfigured means
`getSupabase()` returns `null`, and the default configuration is unconfigured. It exists for the
roadmap path — a read-only mirror of the same bundle, so a data correction can reach installed apps
without a store release. Auth is off; there are no accounts to persist.
