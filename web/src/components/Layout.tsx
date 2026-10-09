import { NavLink, Outlet } from 'react-router-dom'

import { ProvenanceNotice } from './ProvenanceNotice'
import { CORRECTIONS_URL } from '@/data/contribute'
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

      <header className="no-print border-b border-[var(--color-border)] px-4 py-3">
        <div className="mx-auto flex max-w-6xl flex-wrap items-center gap-x-4 gap-y-2">
          <NavLink
            to="/"
            end
            aria-label="EU27.CLOUD home"
            className="flex shrink-0 items-center gap-2.5"
          >
            <img
              src="/brand/badge.png"
              alt=""
              width={320}
              height={320}
              className="h-13 w-13 sm:h-[76px] sm:w-[76px]"
            />
            <img
              src="/brand/wordmark.png"
              alt="EU27.CLOUD"
              width={600}
              height={83}
              className="logo-light h-[17px] w-auto"
            />
            <img
              src="/brand/wordmark-white.png"
              alt="EU27.CLOUD"
              width={600}
              height={83}
              className="logo-dark h-[17px] w-auto"
            />
          </NavLink>
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
          {/* Shows the mode it switches to: a sun while dark, a moon while light. */}
          <button
            type="button"
            onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}
            aria-label={mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
            title={mode === 'dark' ? 'Light mode' : 'Dark mode'}
            className="ml-auto grid h-9 w-9 place-items-center rounded-full border border-[var(--color-border)] text-[var(--color-fg-secondary)] hover:border-[var(--color-eu-gold)] hover:text-[var(--color-accent-text)]"
          >
            {mode === 'dark' ? <SunIcon /> : <MoonIcon />}
          </button>
        </div>
      </header>

      <main id="main" className="mx-auto max-w-6xl px-4 py-6">
        <Outlet />
      </main>

      {/* The footer prints its provenance notice; the rest of it is screen-only. */}
      <footer className="mt-12 border-t border-[var(--color-border)] px-4 py-6 text-xs text-[var(--color-fg-secondary)]">
        <div className="mx-auto max-w-6xl">
          <ProvenanceNotice generated={generated} provenance={provenance} />
          <div className="no-print">
            <NavLink
              to="/"
              end
              aria-label="EU27.CLOUD, European Union Data Sovereignty Initiative"
              className="mb-4 flex items-center gap-3"
            >
              <img src="/brand/badge.png" alt="" width={320} height={320} className="h-12 w-12" />
              <img
                src="/brand/lockup.png"
                alt=""
                width={900}
                height={172}
                className="logo-light h-10 w-auto"
              />
              <img
                src="/brand/lockup-white.png"
                alt=""
                width={900}
                height={172}
                className="logo-dark h-10 w-auto"
              />
            </NavLink>
            MIT licensed. Independent research, not affiliated with any government or EU body.
            Corrections and sources welcome via{' '}
            <a className="underline" href={CORRECTIONS_URL}>
              the corrections form
            </a>
            .
          </div>
        </div>
      </footer>
    </div>
  )
}

function SunIcon() {
  return (
    <svg
      viewBox="0 0 24 24"
      width="18"
      height="18"
      aria-hidden="true"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
    >
      <circle cx="12" cy="12" r="4.2" />
      <path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6" />
    </svg>
  )
}

function MoonIcon() {
  return (
    <svg
      viewBox="0 0 24 24"
      width="18"
      height="18"
      aria-hidden="true"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinejoin="round"
    >
      <path d="M20.5 14.6A8.5 8.5 0 0 1 9.4 3.5a8.5 8.5 0 1 0 11.1 11.1z" />
    </svg>
  )
}
