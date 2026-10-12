/** One five-pointed star, drawn around the origin; the flag disc places twelve of them. */
const STAR = '0,-3 0.9,-0.9 3,-0.9 1.3,0.4 1.9,2.6 0,1.3 -1.9,2.6 -1.3,0.4 -3,-0.9 -0.9,-0.9'

/** Twelve positions on a ring, the first at twelve o'clock. */
const RING = Array.from({ length: 12 }, (_, i) => {
  const a = (i / 12) * Math.PI * 2
  return [Math.round(100 + 60 * Math.sin(a)), Math.round(100 - 60 * Math.cos(a))] as const
})

/**
 * The front page's hero (#101): the landing design's headline over a pale gradient. The dot texture, the
 * EU silhouette, the circle outline and the flag disc are decoration, hidden from assistive technology
 * and kept to the right so they never sit under the text.
 */
export function Hero() {
  return (
    <section className="hero-band relative min-h-[415px] overflow-hidden">
      <div aria-hidden="true" className="hero-dots absolute inset-0" />
      <div
        aria-hidden="true"
        className="hero-map absolute top-[-6%] right-[-2%] hidden h-[125%] sm:block"
      />
      <svg
        aria-hidden="true"
        viewBox="0 0 400 400"
        className="absolute right-[8%] bottom-[-230px] hidden h-[360px] w-[360px] sm:block"
      >
        <circle cx="200" cy="200" r="190" fill="none" stroke="#B9C3D6" strokeWidth="1" />
      </svg>
      <svg
        aria-hidden="true"
        viewBox="0 0 200 200"
        className="absolute right-[-40px] bottom-[-36px] h-[120px] w-[120px] sm:h-[200px] sm:w-[200px]"
      >
        <defs>
          <linearGradient id="hero-flag" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" stopColor="#3D63C9" />
            <stop offset="1" stopColor="#6E8DDB" />
          </linearGradient>
        </defs>
        <circle cx="100" cy="100" r="98" fill="url(#hero-flag)" />
        <g fill="#FFD21F">
          {RING.map(([x, y]) => (
            <polygon key={`${x}-${y}`} transform={`translate(${x},${y}) scale(3)`} points={STAR} />
          ))}
        </g>
      </svg>
      <div className="relative mx-auto max-w-[1440px] px-6 pt-14 pb-20 sm:px-10 sm:pt-[92px] sm:pb-[110px]">
        <p className="text-sm font-bold tracking-[0.16em] text-[var(--color-accent-text)] uppercase">
          Cloud Sovereignty for Europe
        </p>
        <h1 className="mt-[18px] text-[clamp(1.9rem,8.6vw,2.75rem)] leading-[1.12] font-extrabold tracking-[-0.01em] text-[var(--color-fg-primary)] sm:text-[clamp(2.75rem,6vw,4.5rem)]">
          Navigate
          <br />
          <span className="underline decoration-[var(--color-eu-gold)] decoration-[5px] underline-offset-[12px]">
            Cloud Sovereignty
          </span>
        </h1>
        <p className="mt-7 text-[clamp(1.125rem,1.8vw,1.375rem)] font-medium text-[var(--color-fg-secondary)]">
          Understand. Comply. Decide. Stay sovereign.
        </p>
      </div>
    </section>
  )
}
