import { useLocation, useNavigate } from 'react-router-dom'

import { chooseLang, choices, stateOf, useLang, useTx, type Lang } from '@/i18n'
import { useDisclosure } from '@/utils/disclosure'
import { countryPath } from '@/utils/routes'

/**
 * Chrome ships no names in Irish or Maltese and answers "Irish" and "Maltese", which is not what a reader of
 * either looks for in a list of languages; these are the names they would (#113).
 */
const OWN_NAME: Record<string, string> = { ga: 'Gaeilge', mt: 'Malti' }

/** A language's own name for itself, "Deutsch", "français", as the reader of it would look for it. */
function endonym(l: Lang): string {
  const named = new Intl.DisplayNames([l.tag], { type: 'language' }).of(l.lang) ?? l.lang
  const english = new Intl.DisplayNames(['en'], { type: 'language' }).of(l.lang)
  const name = l.lang !== 'en' && named === english ? (OWN_NAME[l.lang] ?? named) : named
  return name.charAt(0).toLocaleUpperCase(l.tag) + name.slice(1)
}

/**
 * The header's language switch (#111, #113). It lists what the page can be read in: on a member state's page
 * that state's admitted languages, then the site languages it lacks; elsewhere the site languages and English.
 * A choice is remembered for the whole site (`chooseLang`) and the address does not change, except that a state
 * page with an explicit language (`/be/fr`) returns to its plain address, where the choice applies.
 */
export function LanguageSwitch() {
  const { pathname } = useLocation()
  const navigate = useNavigate()
  const current = useLang()
  const { tx } = useTx()
  const iso = stateOf(pathname)
  const options = choices(iso)
  const { open, close, rootProps, buttonProps, panelProps } = useDisclosure()

  if (options.length < 2) return null
  const choose = (l: Lang) => {
    chooseLang(l.lang)
    close()
    if (iso && pathname !== countryPath(iso)) navigate(countryPath(iso))
  }
  return (
    <div {...rootProps} className="relative">
      <button
        {...buttonProps}
        aria-label={tx('Language: {name}', { name: endonym(current) })}
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
        {options.map(l => (
          <li key={l.tag}>
            <button
              type="button"
              lang={l.tag}
              aria-current={l.tag === current.tag ? 'true' : undefined}
              onClick={() => choose(l)}
              className={`block w-full rounded-md px-3 py-2 text-left ${
                l.tag === current.tag
                  ? 'bg-[var(--color-bg-emphasis)] text-[var(--color-accent-text)]'
                  : 'text-[var(--color-fg-secondary)] hover:bg-[var(--color-bg-emphasis)] hover:text-[var(--color-accent-text)]'
              }`}
            >
              {endonym(l)}
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}
