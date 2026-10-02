import type { ReactNode } from 'react'

/**
 * The page header every page opens with, after the PDF report's cover and chapter bands (#91): EU blue,
 * a gold kicker, the title in the print serif and a gold rule. Method pages use the method teal, with a
 * pale teal kicker (gold on teal is under 4.5:1). Colours are brand tokens, the same in both themes.
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
      className={`mb-6 overflow-hidden rounded text-white ${
        method ? 'bg-[var(--color-method-deep)]' : 'bg-[var(--color-eu-blue)]'
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
          className={`font-serif leading-tight font-normal ${
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
