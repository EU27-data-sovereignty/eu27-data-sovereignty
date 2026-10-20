import { useEffect } from 'react'
import { NavLink, Outlet, useLocation, useNavigationType } from 'react-router-dom'

import { LanguageSwitch } from './LanguageSwitch'
import { ProvenanceNotice } from './ProvenanceNotice'
import { CORRECTIONS_URL } from '@/data/contribute'
import { useLang, useT, type Key } from '@/i18n'
import { useDisclosure } from '@/utils/disclosure'
import { useTheme } from '@/utils/theme'

// Labels are keys into the language tables (#111), so a state's page served in its language names them in it.
const NAV: { to: string; label: Key; end?: boolean }[] = [
  { to: '/', label: 'nav.overview', end: true },
  { to: '/sovereignty', label: 'nav.ranking' },
  { to: '/countries', label: 'nav.countries' },
  { to: '/holdings', label: 'nav.holdings' },
  { to: '/infrastructure', label: 'nav.hosting' },
]

// How the evidence was gathered and checked: one entry in the bar, opened as a short list, so the bar names
// what the site finds and this names how it knows.
const ABOUT_THE_DATA: { to: string; label: Key }[] = [
  { to: '/sources', label: 'nav.sources' },
  { to: '/methodology', label: 'nav.methodology' },
  { to: '/fact-check', label: 'nav.factcheck' },
]

// Last: it draws on every page before it.
const ASK: { to: string; label: Key } = { to: '/ask', label: 'nav.ask' }

// py-1: a 30 px tap target, over WCAG 2.2's 24 px minimum (#92).
const LINK = 'inline-block py-1 '
const ACTIVE =
  'text-[var(--color-accent-text)] underline decoration-[var(--color-eu-gold)] decoration-2 underline-offset-8'
const IDLE = 'text-[var(--color-fg-secondary)] hover:text-[var(--color-accent-text)]'
const navClass = ({ isActive }: { isActive: boolean }) => LINK + (isActive ? ACTIVE : IDLE)

export function Layout({ generated, provenance }: { generated: string; provenance: string }) {
  const [mode, setMode] = useTheme()
  const { pathname, hash } = useLocation()
  const home = pathname === '/'
  const { tag } = useLang()
  const t = useT()

  // The document's language is the page's: `de-DE` on a German page, so a screen reader speaks it as German.
  useEffect(() => {
    document.documentElement.lang = tag
  }, [tag])

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
              <NavLink key={n.to} to={n.to} end={n.end} className={navClass}>
                {t(n.label)}
              </NavLink>
            ))}
            <AboutTheData />
            <NavLink to={ASK.to} className={navClass}>
              {t(ASK.label)}
            </NavLink>
          </nav>
          <div className="flex items-center gap-3">
            <LanguageSwitch />
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

/**
 * "About the data": a disclosure button over Sources, Methodology and Fact check. A plain list of links, not an
 * ARIA menu, so Tab and the screen reader's link list work as they do in the rest of the bar. Opening and
 * closing is `useDisclosure`'s, shared with the language switch.
 */
function AboutTheData() {
  const { pathname } = useLocation()
  const t = useT()
  const { open, rootProps, buttonProps, panelProps } = useDisclosure()
  const here = ABOUT_THE_DATA.some(n => pathname === n.to || pathname.startsWith(`${n.to}/`))

  return (
    <div {...rootProps} className="relative">
      <button
        {...buttonProps}
        className={`${LINK}inline-flex items-center gap-1.5 ${here ? ACTIVE : IDLE}`}
      >
        {/* Not yet a key in the strings table: its drafts predate the menu (#111). */}
        About the data
        <svg
          width="12"
          height="12"
          viewBox="0 0 14 14"
          aria-hidden="true"
          className={open ? 'rotate-180' : ''}
        >
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
      <ul
        {...panelProps}
        className="absolute top-full right-0 z-20 sm:right-auto sm:left-0 mt-2 min-w-48 rounded-[10px] border border-[var(--color-border)] bg-[var(--color-bg-card)] p-2 shadow-[0_8px_24px_rgb(0_0_0/0.18)]"
      >
        {ABOUT_THE_DATA.map(n => (
          <li key={n.to}>
            <NavLink
              to={n.to}
              className={({ isActive }) =>
                'block rounded-md px-3 py-2 ' +
                (isActive
                  ? 'bg-[var(--color-bg-emphasis)] text-[var(--color-accent-text)]'
                  : 'text-[var(--color-fg-secondary)] hover:bg-[var(--color-bg-emphasis)] hover:text-[var(--color-accent-text)]')
              }
            >
              {t(n.label)}
            </NavLink>
          </li>
        ))}
      </ul>
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
