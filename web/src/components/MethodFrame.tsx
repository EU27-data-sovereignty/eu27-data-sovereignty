import type { ReactNode } from 'react'

import { PageBand } from './PageBand'

/**
 * How-we-know material — the methodology and the fact check — set apart in the method teal, with the same
 * kicker the PDFs and briefs carry, so a reader never mistakes method for findings (#88). A contents list
 * of the document's own sections sits beside it on wide screens (#99 layout).
 */
export function MethodFrame({
  title,
  sections = [],
  children,
}: {
  title: string
  sections?: { id: string; title: string }[]
  children: ReactNode
}) {
  return (
    <article>
      <PageBand kicker="Method · how this was made" title={title} tone="method" />
      <div
        className={
          sections.length ? 'grid items-start gap-10 lg:grid-cols-[220px_minmax(0,1fr)]' : ''
        }
      >
        {sections.length ? (
          <nav
            aria-label="On this page"
            className="flex flex-wrap gap-1.5 text-sm lg:sticky lg:top-6 lg:flex-col lg:gap-0.5"
          >
            {sections.map((s, i) => (
              <a
                key={s.id}
                href={`#${s.id}`}
                className="rounded-full border border-[var(--color-border)] px-3 py-1 text-[var(--color-fg-secondary)] hover:text-[var(--color-fg-primary)] lg:rounded-none lg:border-0 lg:border-l-2 lg:px-3 lg:py-1.5 lg:hover:border-[var(--color-method)]"
              >
                {i + 1}. {s.title}
              </a>
            ))}
          </nav>
        ) : null}
        <div className="max-w-5xl min-w-0 border-l-4 border-[var(--color-method)] pl-5">
          {children}
        </div>
      </div>
    </article>
  )
}
