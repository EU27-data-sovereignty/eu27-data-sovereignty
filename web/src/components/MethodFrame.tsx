import type { ReactNode } from 'react'

import { PageBand } from './PageBand'

/**
 * How-we-know material — the methodology and the fact check — set apart in the method teal, with the same
 * kicker the PDFs and briefs carry, so a reader never mistakes method for findings (#88).
 */
export function MethodFrame({ title, children }: { title: string; children: ReactNode }) {
  return (
    <article className="max-w-5xl">
      <PageBand kicker="Method · how this was made" title={title} tone="method" />
      <div className="border-l-4 border-[var(--color-method)] pl-4">{children}</div>
    </article>
  )
}
