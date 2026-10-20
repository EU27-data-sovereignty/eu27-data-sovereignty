import { Link, useLocation } from 'react-router-dom'

import { servedLanguages, stateOf, useLang, type Lang } from '@/i18n'
import { useDisclosure } from '@/utils/disclosure'
import { countryPath } from '@/utils/routes'

/** A language's own name for itself, "Deutsch", "français", as the reader of it would look for it. */
function endonym(l: Lang): string {
  const name = new Intl.DisplayNames([l.tag], { type: 'language' }).of(l.lang) ?? l.lang
  return name.charAt(0).toLocaleUpperCase(l.tag) + name.slice(1)
}

/**
 * The header's language switch (#111). On a member state's page it lists the languages that page can be read
 * in: the state's official languages once admitted, and English. Every other page is English only, so the
 * list holds English alone; so does a state page until a translation has been read by a person.
 */
export function LanguageSwitch() {
  const { pathname } = useLocation()
  const current = useLang()
  const iso = stateOf(pathname)
  const options = iso ? servedLanguages(iso) : [current]
  const { open, rootProps, buttonProps, panelProps } = useDisclosure()

  return (
    <div {...rootProps} className="relative">
      <button
        {...buttonProps}
        aria-label={`Language: ${endonym(current)}`}
        className="inline-flex min-h-11 items-center gap-2.5 rounded-lg border-[1.5px] border-[var(--color-accent-text)] bg-[var(--color-bg-card)] px-4 text-[15px] font-semibold text-[var(--color-accent-text)]"
      >
        {current.lang.toUpperCase()}
        <svg
          width="14"
          height="14"
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
        className="absolute top-full right-0 z-20 mt-2 min-w-44 rounded-[10px] border border-[var(--color-border)] bg-[var(--color-bg-card)] p-2 shadow-[0_8px_24px_rgb(0_0_0/0.18)]"
      >
        {options.map((l, i) => (
          <li key={l.tag}>
            {l.tag === current.tag || !iso ? (
              <span
                lang={l.tag}
                aria-current="true"
                className="block rounded-md bg-[var(--color-bg-emphasis)] px-3 py-2 text-[var(--color-accent-text)]"
              >
                {endonym(l)}
              </span>
            ) : (
              <Link
                to={countryPath(iso, i === 0 ? undefined : l.lang)}
                lang={l.tag}
                hrefLang={l.tag}
                className="block rounded-md px-3 py-2 text-[var(--color-fg-secondary)] hover:bg-[var(--color-bg-emphasis)] hover:text-[var(--color-accent-text)]"
              >
                {endonym(l)}
              </Link>
            )}
          </li>
        ))}
      </ul>
    </div>
  )
}
