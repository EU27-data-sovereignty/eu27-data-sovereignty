import type { ReactNode } from 'react'

/**
 * How-we-know material — the methodology and the fact check — set apart in the method teal, with the same
 * kicker the PDFs and briefs carry, so a reader never mistakes method for findings (#88).
 */
export function MethodFrame({ title, children }: { title: string; children: ReactNode }) {
  return (
    <article className="max-w-5xl border-l-4 border-[var(--color-method)] pl-4">
      <p className="mb-1 text-xs font-semibold tracking-widest text-[var(--color-method)] uppercase">
        Method · how this was made
      </p>
      <h1 className="mb-4 text-2xl font-semibold">{title}</h1>
      {children}
    </article>
  )
}
