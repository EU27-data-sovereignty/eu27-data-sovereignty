import { Link } from 'react-router-dom'

import { coverage } from '@/data/sources'
import type { Bundle } from '@/data/types'

function Stat({ label, value, sub }: { label: string; value: string; sub: string }) {
  return (
    <div className="rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-3">
      <div className="text-xs text-[var(--color-fg-secondary)]">{label}</div>
      <div className="text-[length:var(--text-stat)] leading-tight font-semibold tabular-nums">
        {value}
      </div>
      <div className="text-xs text-[var(--color-fg-muted)]">{sub}</div>
    </div>
  )
}

/**
 * The headline is the state of the evidence, not a capacity figure: capacity is withdrawn
 * until each country is sized from its own measured holdings (#73), and a site that led with
 * a number it cannot source would contradict its own rule (#75).
 */
export function Overview({ bundle }: { bundle: Bundle }) {
  const countries = Object.values(bundle.countries)
  const covs = countries.map(coverage)
  const verified = covs.reduce((n, c) => n + c.verified, 0)
  const total = covs.reduce((n, c) => n + c.total, 0)
  const tier0 = covs.reduce((n, c) => n + c.tier0, 0)
  const tier0Total = covs.reduce((n, c) => n + c.tier0Total, 0)
  const sources = Object.keys(bundle.sources).length
  const claims = Object.keys(bundle.claims).length

  return (
    <article>
      <h1 className="mb-2 text-3xl font-semibold">Sovereign data centres for the EU-27</h1>
      <p className="mb-6 max-w-3xl text-[var(--color-fg-secondary)]">
        Each member state analysed on its own fundamentals: the critical data holdings it cannot let
        depend on infrastructure a foreign state can compel or switch off, who operates them, under
        which law, and where they run. Every fact is footnoted to a document that was fetched,
        hashed and checked to contain the quoted text. Where no such document has been found yet,
        the value is withheld and the gap is shown.
      </p>

      <section aria-label="State of the evidence" className="mb-8 grid gap-3 sm:grid-cols-4">
        <Stat
          label="Critical holdings verified"
          value={`${verified}`}
          sub={`of ${total} (27 states × ${bundle.holding_classes.length} classes)`}
        />
        <Stat label="Tier 0 holdings verified" value={`${tier0}`} sub={`of ${tier0Total}`} />
        <Stat label="Sourced claims" value={`${claims}`} sub={`from ${sources} checked sources`} />
        <Stat label="Countries sized" value="0" sub="of 27; sizing needs measured holdings" />
      </section>

      <a
        href="/eu27-report.pdf"
        className="mb-6 block rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-3 hover:border-[var(--color-accent)]"
      >
        <div className="font-semibold text-[var(--color-accent-text)]">EU-27 report (PDF)</div>
        <div className="text-sm text-[var(--color-fg-secondary)]">
          Every member state in one document, with a table of contents, footnoted sources and a
          source appendix. Each country is also available as its own PDF.
        </div>
      </a>

      <nav className="grid gap-3 sm:grid-cols-3">
        {[
          ['/countries', 'Countries', 'All 27, sortable, each with its own report.'],
          ['/holdings', 'Critical holdings', 'One kind of holding across every member state.'],
          ['/sources', 'Sources', 'Every checked source and the claims it supports.'],
        ].map(([to, title, blurb]) => (
          <Link
            key={to}
            to={to!}
            className="rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-3 hover:border-[var(--color-accent)]"
          >
            <div className="font-semibold text-[var(--color-accent-text)]">{title}</div>
            <div className="text-sm text-[var(--color-fg-secondary)]">{blurb}</div>
          </Link>
        ))}
      </nav>
    </article>
  )
}
