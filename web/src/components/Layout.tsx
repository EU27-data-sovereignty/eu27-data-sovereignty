import { NavLink, Outlet } from 'react-router-dom'

import { ProvenanceBanner } from './ProvenanceBanner'
import { useTheme } from '@/utils/theme'

const NAV = [
  { to: '/', label: 'Overview', end: true },
  { to: '/sovereignty', label: 'Ranking' },
  { to: '/countries', label: 'Countries' },
  { to: '/holdings', label: 'Critical holdings' },
  { to: '/infrastructure', label: 'Hosting' },
  { to: '/sources', label: 'Sources' },
  { to: '/ask', label: 'Ask' },
  { to: '/methodology', label: 'Methodology' },
  { to: '/fact-check', label: 'Fact check' },
]

export function Layout({ generated, provenance }: { generated: string; provenance: string }) {
  const [mode, setMode] = useTheme()

  return (
    <div className="min-h-screen">
      <a
        href="#main"
        className="sr-only focus:not-sr-only focus:absolute focus:m-2 focus:rounded focus:bg-[var(--color-bg-card)] focus:p-2"
      >
        Skip to content
      </a>

      <ProvenanceBanner generated={generated} provenance={provenance} />

      <header className="no-print border-b border-[var(--color-border)] px-4 py-3">
        <div className="mx-auto flex max-w-6xl flex-wrap items-center gap-x-4 gap-y-2">
          <span className="font-serif text-lg">EU-27 Sovereign Data Centres</span>
          <nav aria-label="Main" className="flex flex-wrap gap-x-3 gap-y-1 text-sm">
            {NAV.map(n => (
              <NavLink
                key={n.to}
                to={n.to}
                end={n.end}
                // py-1: a 28 px tap target, over WCAG 2.2's 24 px minimum (#92).
                className={({ isActive }) =>
                  'inline-block py-1 ' +
                  (isActive
                    ? 'text-[var(--color-accent-text)] underline decoration-[var(--color-eu-gold)] decoration-2 underline-offset-4'
                    : 'text-[var(--color-fg-secondary)] hover:text-[var(--color-fg-primary)]')
                }
              >
                {n.label}
              </NavLink>
            ))}
          </nav>
          <button
            type="button"
            onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}
            className="ml-auto rounded border border-[var(--color-border)] px-2 py-1 text-xs"
          >
            {mode === 'dark' ? 'Light' : 'Dark'} mode
          </button>
        </div>
      </header>

      <main id="main" className="mx-auto max-w-6xl px-4 py-6">
        <Outlet />
      </main>

      <footer className="no-print mt-12 border-t border-[var(--color-border)] px-4 py-6 text-xs text-[var(--color-fg-secondary)]">
        <div className="mx-auto max-w-6xl">
          MIT licensed. Independent research, not affiliated with any government or EU body.
          Corrections and sources welcome via{' '}
          <a
            className="underline"
            href="https://github.com/pieteradejong/sovereign-data-centers/issues/new?template=data-correction.yml"
          >
            the corrections form
          </a>
          .
        </div>
      </footer>
    </div>
  )
}
