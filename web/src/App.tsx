import { useEffect, useState } from 'react'
import { Navigate, Route, Routes, useParams } from 'react-router-dom'

import { Layout } from './components/Layout'
import { loadBundle } from './data/load'
import type { Bundle } from './data/types'
import { Ask } from './pages/Ask'
import { Countries } from './pages/Countries'
import { Country } from './pages/Country'
import { FactCheck } from './pages/FactCheck'
import { Holding, HoldingsIndex } from './pages/Holdings'
import { Infrastructure } from './pages/Infrastructure'
import { Methodology } from './pages/Methodology'
import { NotFound } from './pages/NotFound'
import { Overview } from './pages/Overview'
import { Poster } from './pages/Poster'
import { Sources } from './pages/Sources'
import { Sovereignty } from './pages/Sovereignty'
import { countryPath } from './utils/routes'

/**
 * A member state lives at its own top-level path, `/de` (#105). The code is the bundle's key, so a
 * segment that is not one of the 27 falls through to the not-found page, and an upper-case code is
 * redirected to the one canonical spelling.
 */
function CountryAtRoot({ bundle }: { bundle: Bundle }) {
  const { iso = '' } = useParams()
  if (!(iso.toUpperCase() in bundle.documents)) return <NotFound />
  if (iso !== iso.toLowerCase()) return <Navigate to={countryPath(iso)} replace />
  return <Country bundle={bundle} />
}

/** The pre-#105 path. Vercel 308s it before the app loads; this covers `vite preview` and in-app links. */
function LegacyCountry() {
  const { iso = '' } = useParams()
  return <Navigate to={countryPath(iso)} replace />
}

export function App() {
  const [bundle, setBundle] = useState<Bundle | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    loadBundle().then(setBundle, e => setError(String(e)))
  }, [])

  if (error) {
    return (
      <main className="mx-auto max-w-2xl p-6">
        <h1 className="mb-2 text-xl font-semibold">Could not load the data</h1>
        <p className="text-[var(--color-fg-secondary)]">{error}</p>
        <p className="mt-2 text-sm text-[var(--color-fg-muted)]">
          Run <code>python3 model/export_json.py</code> to regenerate the bundle.
        </p>
      </main>
    )
  }

  // Deliberately a plain message rather than a spinner: headless Chrome prints these
  // routes to PDF, and a spinner is what a broken export looks like.
  if (!bundle) {
    return (
      <main className="mx-auto max-w-2xl p-6 text-[var(--color-fg-secondary)]">
        Loading the EU-27 dataset…
      </main>
    )
  }

  return (
    <Routes>
      {/* Outside Layout: the poster is a standalone artefact exported to PNG, with no
          site chrome. Its caveat is printed on the poster itself. */}
      <Route path="poster/:iso" element={<Poster bundle={bundle} />} />
      <Route element={<Layout generated={bundle.generated} provenance={bundle.provenance} />}>
        <Route index element={<Overview bundle={bundle} />} />
        <Route path="countries" element={<Countries bundle={bundle} />} />
        <Route path="holdings" element={<HoldingsIndex bundle={bundle} />} />
        <Route path="holdings/:cls" element={<Holding bundle={bundle} />} />
        <Route path="infrastructure" element={<Infrastructure bundle={bundle} />} />
        <Route path="sources" element={<Sources bundle={bundle} />} />
        <Route path="sovereignty" element={<Sovereignty bundle={bundle} />} />
        <Route path="ask" element={<Ask bundle={bundle} />} />
        <Route path="map" element={<Sovereignty bundle={bundle} />} />
        <Route path="country/:iso" element={<LegacyCountry />} />
        <Route path="methodology" element={<Methodology bundle={bundle} />} />
        <Route path="fact-check" element={<FactCheck bundle={bundle} />} />
        <Route path="fact-check/:iso" element={<FactCheck bundle={bundle} />} />
        {/* Static segments above rank ahead of this one, so `/ask` is never read as a country. */}
        <Route path=":iso" element={<CountryAtRoot bundle={bundle} />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}
