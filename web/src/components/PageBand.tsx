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
  children,
}: {
  kicker: string
  title: ReactNode
  tone?: 'eu' | 'method'
  hero?: boolean
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
        className={hero ? 'px-6 pt-8 pb-7 sm:px-10 sm:pt-12 sm:pb-10' : 'px-5 py-5 sm:px-8 sm:py-6'}
      >
        <p
          className={`mb-2 text-xs tracking-[0.25em] uppercase sm:text-sm ${
            method ? 'text-[var(--color-method-pale)]' : 'text-[var(--color-eu-gold)]'
          }`}
        >
          {kicker}
        </p>
        <h1
          className={`font-display leading-tight font-bold tracking-tight ${
            hero ? 'text-4xl sm:text-6xl' : 'text-3xl sm:text-4xl'
          }`}
        >
          {title}
        </h1>
        {children}
      </div>
      <div
        className={`h-1.5 ${method ? 'bg-[var(--color-method-pale)]' : 'bg-[var(--color-eu-gold)]'}`}
      />
    </header>
  )
}
