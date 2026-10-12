import { useState } from 'react'
import type { ReactNode } from 'react'

export type EntryMode = 'role' | 'need'

/** The six audiences of the landing design, in its order. `id` is what a later content panel keys on. */
export type AudienceId =
  'ministries' | 'procurement' | 'parliaments' | 'cyber' | 'eu-institutions' | 'operators'

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

const AUDIENCES: { id: AudienceId; label: [string, string?]; icon: ReactNode }[] = [
  {
    id: 'ministries',
    label: ['Ministries &', 'government CIOs'],
    icon: (
      <path
        d="M5 13L18 6l13 7z M6 13h24 M9 16v11 M15 16v11 M21 16v11 M27 16v11 M6 27h24 M4 30.5h28"
        {...STROKE}
      />
    ),
  },
  {
    id: 'procurement',
    label: ['Procurement &', 'cloud strategy'],
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
    label: ['Parliaments &', 'audit courts'],
    icon: (
      <path
        d="M18 4v3 M9 15a9 7 0 0 1 18 0z M7 15h22 M10 18v9 M14.7 18v9 M19.3 18v9 M24 18v9 M7 27h22 M5 30.5h26"
        {...STROKE}
      />
    ),
  },
  {
    id: 'cyber',
    label: ['Cyber agencies', '& CISOs'],
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
    label: ['EU institutions'],
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
    label: ['Operators', 'investors & press'],
    icon: (
      <path
        d="M5 31h27 M7 31v-8h4.5v8 M15 31v-12h4.5v12 M23 31v-16h4.5v16 M5 18l8-7 5 4 11-10 M24 5h5v5"
        {...STROKE}
      />
    ),
  },
]

const SEGMENTS: { mode: EntryMode; label: string; icon: ReactNode }[] = [
  {
    mode: 'role',
    label: 'I am…',
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
    label: 'I need to…',
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

/**
 * The audience selector band under the hero (#101). This pass it is a control without a destination: the
 * toggle switches its own state and an audience can be marked, but no content panel exists yet, and none
 * is invented here. `onSelect` and the returned state are the hooks a later panel attaches to.
 */
export function AudienceSelector({
  onSelect,
}: {
  onSelect?: (choice: { mode: EntryMode; audience: AudienceId | null }) => void
}) {
  const [mode, setMode] = useState<EntryMode>('role')
  const [audience, setAudience] = useState<AudienceId | null>(null)

  const choose = (next: { mode: EntryMode; audience: AudienceId | null }) => {
    setMode(next.mode)
    setAudience(next.audience)
    onSelect?.(next)
  }

  return (
    <section aria-label="Choose your entry point" className="bg-[var(--color-band)]">
      <div className="mx-auto max-w-[1440px] px-4 pt-8 pb-12 sm:px-8">
        <div
          role="group"
          aria-label="Choose entry by"
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
                onClick={() => choose({ mode: s.mode, audience })}
                className={`on-navy inline-flex min-h-11 items-center justify-center gap-3 rounded-[9px] px-4 text-base whitespace-nowrap sm:min-w-[190px] sm:px-6 ${
                  mode === s.mode
                    ? 'bg-[var(--color-eu-gold)] font-bold text-[var(--color-eu-deep)]'
                    : 'font-medium text-white'
                }`}
              >
                <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true">
                  {s.icon}
                </svg>
                {s.label}
              </button>
            </span>
          ))}
        </div>

        <div
          role="group"
          aria-label="Entry points"
          className="mt-[26px] grid grid-cols-[repeat(auto-fit,minmax(160px,1fr))] gap-2.5"
        >
          {AUDIENCES.map(a => (
            <button
              key={a.id}
              type="button"
              aria-pressed={audience === a.id}
              onClick={() => choose({ mode, audience: audience === a.id ? null : a.id })}
              className={`on-navy flex min-h-[70px] items-center gap-3.5 rounded-[18px] border px-4 py-2.5 text-left text-sm leading-[1.35] font-medium text-white transition-colors hover:border-[var(--color-eu-gold)] hover:bg-[var(--color-navy-hover)] ${
                audience === a.id
                  ? 'border-[var(--color-eu-gold)] bg-[var(--color-navy-hover)]'
                  : 'border-[var(--color-navy-border)] bg-[var(--color-navy-surface)]'
              }`}
            >
              <svg
                width="36"
                height="36"
                viewBox="0 0 36 36"
                aria-hidden="true"
                className="flex-none text-[var(--color-icon-on-navy)]"
              >
                {a.icon}
              </svg>
              <span>
                {a.label[0]}
                {a.label[1] ? (
                  <>
                    {' '}
                    <br className="hidden sm:block" />
                    {a.label[1]}
                  </>
                ) : null}
              </span>
            </button>
          ))}
        </div>
      </div>
    </section>
  )
}
