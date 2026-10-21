import { useState } from 'react'
import type { ReactNode } from 'react'
import { Link } from 'react-router-dom'

import { AUDIENCE_GUIDES, TASK_GUIDES } from '@/data/guides'
import { m, useTx } from '@/i18n'

export type EntryMode = 'role' | 'need'

const STROKE = {
  fill: 'none',
  stroke: 'currentColor',
  strokeWidth: 1.8,
  strokeLinejoin: 'round',
  strokeLinecap: 'round',
} as const

/** Twelve small stars on a ring, the EU-institutions icon: the one icon filled gold. */
const STARS = [
  [18, 5],
  [24.5, 6.7],
  [29.3, 11.5],
  [31, 18],
  [29.3, 24.5],
  [24.5, 29.3],
  [18, 31],
  [11.5, 29.3],
  [6.7, 24.5],
  [5, 18],
  [6.7, 11.5],
  [11.5, 6.7],
] as const

const AUDIENCE_ICONS: { id: string; icon: ReactNode }[] = [
  {
    id: 'ministries',
    icon: (
      <path
        d="M5 13L18 6l13 7z M6 13h24 M9 16v11 M15 16v11 M21 16v11 M27 16v11 M6 27h24 M4 30.5h28"
        {...STROKE}
      />
    ),
  },
  {
    id: 'procurement',
    icon: (
      <>
        <path d="M3 7h4.5l3.5 15h16.5l3-11H9" {...STROKE} />
        <circle cx="13" cy="28" r="2.2" {...STROKE} />
        <circle cx="25" cy="28" r="2.2" {...STROKE} />
      </>
    ),
  },
  {
    id: 'parliaments',
    icon: (
      <path
        d="M18 4v3 M9 15a9 7 0 0 1 18 0z M7 15h22 M10 18v9 M14.7 18v9 M19.3 18v9 M24 18v9 M7 27h22 M5 30.5h26"
        {...STROKE}
      />
    ),
  },
  {
    id: 'cyber',
    icon: (
      <>
        <path d="M18 3.5l12 4.5v9c0 7.5-5.2 12.5-12 15.5C11.2 29.5 6 24.5 6 17V8z" {...STROKE} />
        <rect x="13.5" y="16" width="9" height="7.5" rx="1.2" {...STROKE} />
        <path d="M15.3 16v-2.3a2.7 2.7 0 0 1 5.4 0V16" {...STROKE} />
      </>
    ),
  },
  {
    id: 'eu-institutions',
    icon: (
      <g fill="var(--color-eu-gold)">
        {STARS.map(([x, y]) => (
          <polygon
            key={`${x}-${y}`}
            transform={`translate(${x},${y})`}
            points="0,-2.4 0.7,-0.7 2.4,-0.7 1,0.3 1.5,2.1 0,1 -1.5,2.1 -1,0.3 -2.4,-0.7 -0.7,-0.7"
          />
        ))}
      </g>
    ),
  },
  {
    id: 'operators',
    icon: (
      <path
        d="M5 31h27 M7 31v-8h4.5v8 M15 31v-12h4.5v12 M23 31v-16h4.5v16 M5 18l8-7 5 4 11-10 M24 5h5v5"
        {...STROKE}
      />
    ),
  },
]

/** The six tasks' icons, by guide slug (data/guides.ts holds their labels and pages). */
const TASK_ICONS: { id: string; icon: ReactNode }[] = [
  {
    id: 'exposure',
    icon: (
      <>
        <path
          d="M15 5c-4.4 0-8 3.4-8 7.7C7 18.500 15 26 15 26s8-7.5 8-13.300C23 8.400 19.400 5 15 5z"
          {...STROKE}
        />
        <circle cx="15" cy="12.5" r="2.6" {...STROKE} />
        <circle cx="25.500" cy="25.500" r="4.200" {...STROKE} />
        <path d="M28.600 28.600l3.400 3.400" {...STROKE} />
      </>
    ),
  },
  {
    id: 'migrate',
    icon: (
      <>
        <path d="M14 9h17 M14 18h17 M14 27h17" {...STROKE} />
        <path
          d="M4.500 7.500l2-1.500v6 M4 16.200c1.500-1.400 4-.6 4 1.200 0 1.400-2 2.200-4 3.800h4.200 M4.200 24.800c1.500-.9 3.800-.4 3.800 1.100 0 1-1 1.500-2 1.500 1.200 0 2.200.6 2.200 1.700 0 1.700-2.700 2.100-4.200 1"
          {...STROKE}
          strokeWidth={1.5}
        />
      </>
    ),
  },
  {
    id: 'tender',
    icon: (
      <>
        <path d="M9 4h13l6 6v22H9z M22 4v6h6" {...STROKE} />
        <path d="M13.500 21l3.500 3.500 6.500-7.500" {...STROKE} />
      </>
    ),
  },
  {
    id: 'questions',
    icon: (
      <>
        <path d="M5 7h26v18H17l-7 6v-6H5z" {...STROKE} />
        <path
          d="M14.500 13.200a3.500 3.300 0 1 1 5 3c-1.100.7-1.500 1.300-1.500 2.300 M18 21.600v.2"
          {...STROKE}
        />
      </>
    ),
  },
  {
    id: 'compare',
    icon: (
      <>
        <rect x="5" y="6" width="11" height="24" rx="1.5" {...STROKE} />
        <rect x="20" y="6" width="11" height="24" rx="1.5" {...STROKE} />
        <path
          d="M8.500 12h4 M8.500 17h4 M8.500 22h4 M23.500 12h4 M23.500 17h4 M23.500 22h4"
          {...STROKE}
        />
      </>
    ),
  },
  {
    id: 'cut-off',
    icon: (
      <>
        <path
          d="M15 21l-3.500 3.500a4.900 4.900 0 0 1-7-7L8 14 M21 15l3.500-3.500a4.900 4.900 0 0 1 7 7L28 22"
          {...STROKE}
          transform="translate(-0.500 0)"
        />
        <path d="M14 8l1 3.500 M8 14l3.500 1 M22 28l-1-3.500 M28 22l-3.500-1" {...STROKE} />
      </>
    ),
  },
]

const SEGMENTS: { mode: EntryMode; label: string; icon: ReactNode }[] = [
  {
    mode: 'role',
    label: m('I am…'),
    icon: (
      <>
        <circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" strokeWidth="1.7" />
        <path
          d="M4.5 20c0-4 3.4-6.5 7.5-6.5s7.5 2.5 7.5 6.5"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.7"
          strokeLinecap="round"
        />
      </>
    ),
  },
  {
    mode: 'need',
    label: m('I need to…'),
    icon: (
      <>
        <circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" strokeWidth="1.7" />
        <path
          d="M15.5 8.5l-2 5-5 2 2-5z"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.7"
          strokeLinejoin="round"
        />
      </>
    ),
  },
]

const CHIP =
  'on-navy flex min-h-[70px] items-center gap-3.5 rounded-[18px] border px-4 py-2.5 text-left text-sm leading-[1.35] font-medium text-white transition-colors hover:border-[var(--color-eu-gold)] hover:bg-[var(--color-navy-hover)]'

function Icon({ children }: { children: ReactNode }) {
  return (
    <svg
      width="36"
      height="36"
      viewBox="0 0 36 36"
      aria-hidden="true"
      className="flex-none text-[var(--color-icon-on-navy)]"
    >
      {children}
    </svg>
  )
}

/** A label in one or two lines; the break is forced only where the buttons are wide enough for it. */
function Label({ text }: { text: string }) {
  const { tx } = useTx()
  // Translated whole; the newline in it is where a wide screen breaks the line, a space on a narrow one.
  const [first, ...rest] = tx(text).split('\n')
  return (
    <span>
      {first}
      {rest.length ? (
        <>
          {' '}
          <br className="hidden sm:block" />
          {rest.join(' ')}
        </>
      ) : null}
    </span>
  )
}

/**
 * The selector band under the hero (#101, #102). The toggle chooses between six audiences ("I am…") and
 * six tasks ("I need to…"); each is a link to its guide page, whose words live in data/guides.ts. The
 * icons are kept here, by slug.
 */
export function AudienceSelector() {
  const [mode, setMode] = useState<EntryMode>('role')
  const { tx } = useTx()
  const [guides, icons, base] =
    mode === 'role'
      ? ([AUDIENCE_GUIDES, AUDIENCE_ICONS, '/for'] as const)
      : ([TASK_GUIDES, TASK_ICONS, '/how'] as const)

  return (
    <section aria-label={tx('Choose your entry point')} className="bg-[var(--color-band)]">
      <div className="mx-auto max-w-[1440px] px-4 pt-8 pb-12 sm:px-8">
        <div
          role="group"
          aria-label={tx('Choose entry by')}
          className="inline-flex max-w-full items-center rounded-xl border border-[var(--color-navy-border)] bg-[var(--color-navy-surface)] p-1 sm:ml-2"
        >
          {SEGMENTS.map((s, i) => (
            <span key={s.mode} className="flex min-w-0 items-center">
              {i > 0 ? (
                <span
                  aria-hidden="true"
                  className="mx-1 h-[26px] w-px bg-[var(--color-navy-border)]"
                />
              ) : null}
              <button
                type="button"
                aria-pressed={mode === s.mode}
                onClick={() => setMode(s.mode)}
                className={`on-navy inline-flex min-h-11 items-center justify-center gap-3 rounded-[9px] px-4 text-base whitespace-nowrap sm:min-w-[190px] sm:px-6 ${
                  mode === s.mode
                    ? 'bg-[var(--color-eu-gold)] font-bold text-[var(--color-eu-deep)]'
                    : 'font-medium text-white'
                }`}
              >
                <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true">
                  {s.icon}
                </svg>
                {tx(s.label)}
              </button>
            </span>
          ))}
        </div>

        <nav
          aria-label={mode === 'role' ? tx('Guides by audience') : tx('Guides by task')}
          className="mt-[26px] grid grid-cols-[repeat(auto-fit,minmax(160px,1fr))] gap-2.5"
        >
          {guides.map(g => (
            <Link
              key={g.slug}
              to={`${base}/${g.slug}`}
              className={`${CHIP} border-[var(--color-navy-border)] bg-[var(--color-navy-surface)]`}
            >
              <Icon>{icons.find(x => x.id === g.slug)?.icon}</Icon>
              <Label text={g.label} />
            </Link>
          ))}
        </nav>
      </div>
    </section>
  )
}
