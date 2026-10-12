import type { ReactNode } from 'react'

/**
 * The page header every page but the front page opens with (#91, restyled by #101): the hero's pale
 * gradient, dot texture and EU silhouette, a brand-blue kicker and the title in navy. Method pages are a
 * solid method-teal band with a pale kicker, so how-we-know pages stay set apart (#88).
 */
export function PageBand({
  kicker,
  title,
  tone = 'eu',
  facts,
  children,
}: {
  kicker: string
  title: ReactNode
  tone?: 'eu' | 'method'
  /** Headline numbers under the title, each a value and what it counts. */
  facts?: [string, string][]
  children?: ReactNode
}) {
  const method = tone === 'method'
  return (
    <header
      className={`relative mb-8 overflow-hidden rounded ${
        method
          ? 'bg-[var(--color-method-deep)] text-white'
          : 'hero-band border border-[var(--color-border)] text-[var(--color-fg-primary)]'
      }`}
    >
      {method ? null : (
        <>
          <div aria-hidden="true" className="hero-dots absolute inset-0" />
          <div
            aria-hidden="true"
            className="hero-map absolute top-[-20%] right-[2%] hidden h-[160%] sm:block"
          />
        </>
      )}
      <div className="relative px-5 py-7 sm:px-9 sm:py-10">
        <p
          className={`mb-2.5 text-xs font-bold tracking-[0.16em] uppercase sm:text-sm ${
            method ? 'text-[var(--color-method-pale)]' : 'text-[var(--color-accent-text)]'
          }`}
        >
          {kicker}
        </p>
        <h1 className="font-display text-3xl leading-tight font-extrabold tracking-[-0.01em] sm:text-[2.6rem]">
          {title}
        </h1>
        {children}
        {facts?.length ? (
          <dl className="mt-6 flex flex-wrap gap-x-8 gap-y-3">
            {facts.map(([value, what]) => (
              <div key={what} className="flex flex-col-reverse">
                <dt
                  className={`text-xs ${method ? 'text-white/75' : 'text-[var(--color-fg-secondary)]'}`}
                >
                  {what}
                </dt>
                <dd className="font-display text-3xl leading-tight font-extrabold tabular-nums">
                  {value}
                </dd>
              </div>
            ))}
          </dl>
        ) : null}
      </div>
    </header>
  )
}
