import type { ReactNode } from 'react'

/**
 * The page header every page opens with (#91, restyled by #99): the EU silhouette artwork on night navy,
 * a gold kicker, the title in the EU27.CLOUD display sans and a gold rule. Method pages keep the method
 * teal for their kicker and rule (#88). Colours are brand tokens, the same in both themes.
 */
export function PageBand({
  kicker,
  title,
  tone = 'eu',
  hero = false,
  aside,
  facts,
  children,
}: {
  kicker: string
  title: ReactNode
  tone?: 'eu' | 'method'
  hero?: boolean
  /** A second column beside the title, on wide screens (the front page's tile map). */
  aside?: ReactNode
  /** Headline numbers under the title, each a value and what it counts. */
  facts?: [string, string][]
  children?: ReactNode
}) {
  const method = tone === 'method'
  return (
    <header
      className={`band-map mb-6 overflow-hidden rounded text-white ${
        // Method pages tint the artwork method teal, so how-we-know pages stay set apart (#88).
        method
          ? 'shadow-[inset_0_0_0_100vmax_color-mix(in_srgb,var(--color-method-deep)_62%,transparent)]'
          : ''
      }`}
    >
      <div
        className={`${hero ? 'px-6 pt-8 pb-7 sm:px-10 sm:pt-12 sm:pb-10' : 'px-5 py-6 sm:px-8 sm:py-9'} ${
          aside
            ? 'grid items-center gap-8 lg:grid-cols-[minmax(0,1.05fr)_minmax(0,1fr)] lg:gap-14'
            : ''
        }`}
      >
        <div className="min-w-0">
          <p
            className={`mb-2 text-xs tracking-[0.25em] uppercase sm:text-sm ${
              method ? 'text-[var(--color-method-pale)]' : 'text-[var(--color-eu-gold)]'
            }`}
          >
            {kicker}
          </p>
          <h1
            className={`font-display leading-tight font-bold tracking-tight ${
              hero ? 'text-4xl sm:text-5xl' : 'text-3xl sm:text-[2.6rem]'
            }`}
          >
            {title}
          </h1>
          {children}
          {facts?.length ? (
            <dl className="mt-6 flex flex-wrap gap-x-8 gap-y-3">
              {facts.map(([value, what]) => (
                <div key={what} className="flex flex-col-reverse">
                  <dt className="text-xs text-white/70">{what}</dt>
                  <dd className="font-display text-3xl leading-tight font-bold tabular-nums">
                    {value}
                  </dd>
                </div>
              ))}
            </dl>
          ) : null}
        </div>
        {aside ? <div className="min-w-0">{aside}</div> : null}
      </div>
      <div
        className={`h-1.5 ${method ? 'bg-[var(--color-method-pale)]' : 'bg-[var(--color-eu-gold)]'}`}
      />
    </header>
  )
}
