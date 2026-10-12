import { useEffect } from 'react'
import { NavLink, Outlet, useLocation, useNavigationType } from 'react-router-dom'

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
  const { pathname, hash } = useLocation()
  const home = pathname === '/'

  // A client-side route change neither scrolls to a #section nor returns to the top, as a page load would.
  // Do both, one frame later, once the new page has rendered. Back and forward keep the browser's own
  // restored position.
  const back = useNavigationType() === 'POP'
  useEffect(() => {
    if (back && !hash) return
    const frame = requestAnimationFrame(() => {
      const target = hash ? document.getElementById(hash.slice(1)) : null
      if (target) target.scrollIntoView()
      else window.scrollTo(0, 0)
    })
    return () => cancelAnimationFrame(frame)
  }, [pathname, hash, back])

  return (
    <div className="min-h-screen">
      <a
        href="#main"
        className="sr-only focus:not-sr-only focus:absolute focus:m-2 focus:rounded focus:bg-[var(--color-bg-card)] focus:p-2"
      >
        Skip to content
      </a>

      {/* The header of the EU27.CLOUD landing design (#101): white, 68 px, a soft shadow. */}
      <header className="no-print relative z-10 bg-[var(--color-bg-card)] shadow-[0_2px_10px_rgb(11_27_63/0.08)]">
        <div className="mx-auto flex min-h-[68px] max-w-[1440px] flex-wrap items-center gap-x-10 gap-y-3 py-1 pr-6 pl-3">
          <NavLink
            to="/"
            end
            aria-label="EU27.CLOUD home"
            className="flex shrink-0 items-center gap-3.5"
          >
            <img
              src="/brand/eu27-badge.png"
              alt=""
              width={200}
              height={200}
              className="block h-[62px] w-[62px]"
            />
            <span aria-hidden="true" className="h-11 w-px bg-[var(--color-border)]" />
            <img
              src="/brand/eu27-wordmark.png"
              alt="EU27.CLOUD — European Union Data Sovereignty Initiative"
              width={1200}
              height={236}
              className="logo-light h-9 w-auto"
            />
            <img
              src="/brand/eu27-wordmark-white.png"
              alt="EU27.CLOUD — European Union Data Sovereignty Initiative"
              width={1200}
              height={236}
              className="logo-dark h-9 w-auto"
            />
          </NavLink>
          <nav
            aria-label="Main"
            className="ml-auto flex flex-wrap items-center gap-x-7 gap-y-2 text-[15px] font-medium"
          >
            {NAV.map(n => (
              <NavLink
                key={n.to}
                to={n.to}
                end={n.end}
                // py-1: a 30 px tap target, over WCAG 2.2's 24 px minimum (#92).
                className={({ isActive }) =>
                  'inline-block py-1 ' +
                  (isActive
                    ? 'text-[var(--color-accent-text)] underline decoration-[var(--color-eu-gold)] decoration-2 underline-offset-8'
                    : 'text-[var(--color-fg-secondary)] hover:text-[var(--color-accent-text)]')
                }
              >
                {n.label}
              </NavLink>
            ))}
          </nav>
          <div className="flex items-center gap-3">
            {/* English is the only language so far: the control states it and does nothing yet. */}
            <button
              type="button"
              aria-label="Language: English"
              className="inline-flex min-h-11 items-center gap-2.5 rounded-lg border-[1.5px] border-[var(--color-accent-text)] bg-[var(--color-bg-card)] px-4 text-[15px] font-semibold text-[var(--color-accent-text)]"
            >
              EN
              <svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true">
                <path
                  d="M3 5l4 4 4-4"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </button>
            {/* Shows the mode it switches to: a sun while dark, a moon while light. */}
            <button
              type="button"
              onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}
              aria-label={mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
              title={mode === 'dark' ? 'Light mode' : 'Dark mode'}
              className="grid h-11 w-11 place-items-center rounded-lg border border-[var(--color-border)] text-[var(--color-fg-secondary)] hover:border-[var(--color-accent-text)] hover:text-[var(--color-accent-text)]"
            >
              {mode === 'dark' ? <SunIcon /> : <MoonIcon />}
            </button>
          </div>
        </div>
      </header>

      {/* The front page lays out its own full-width hero and band; every other page sits in the column. */}
      <main id="main" className={home ? '' : 'mx-auto max-w-6xl px-4 py-8'}>
        <Outlet />
      </main>

      {/* The footer prints its provenance notice; the rest of it is screen-only. */}
      <footer className="border-t border-[var(--color-border)] bg-[var(--color-bg-card)] px-4 py-8 text-xs text-[var(--color-fg-secondary)]">
        <div className="mx-auto max-w-6xl">
          <ProvenanceNotice generated={generated} provenance={provenance} />
          <div className="no-print">
            <NavLink
              to="/"
              end
              aria-label="EU27.CLOUD, European Union Data Sovereignty Initiative"
              className="mb-4 flex items-center gap-3"
            >
              <img
                src="/brand/eu27-badge.png"
                alt=""
                width={200}
                height={200}
                className="h-12 w-12"
              />
              <img
                src="/brand/eu27-wordmark.png"
                alt=""
                width={1200}
                height={236}
                className="logo-light h-9 w-auto"
              />
              <img
                src="/brand/eu27-wordmark-white.png"
                alt=""
                width={1200}
                height={236}
                className="logo-dark h-9 w-auto"
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
