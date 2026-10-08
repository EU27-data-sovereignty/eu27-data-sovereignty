import { Link } from 'react-router-dom'

import { coverage } from '@/data/sources'
import type { Bundle } from '@/data/types'
import { PageBand } from '@/components/PageBand'

function Stat({ label, value, sub }: { label: string; value: string; sub: string }) {
  return (
    <div className="rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-3">
      <div className="text-xs text-[var(--color-fg-secondary)]">{label}</div>
      <div className="font-display text-[length:var(--text-stat)] leading-tight font-bold tabular-nums">
        {value}
      </div>
      <div className="text-xs text-[var(--color-fg-muted)]">{sub}</div>
    </div>
  )
}

/** Pages of the EU-27 report shown as previews, rendered from the report at build time
 * (book/report.py `PREVIEWS`; the names must match). */
const REPORT_PREVIEWS: [string, string][] = [
  ['cover', 'Cover'],
  ['ranking', 'Data-sovereignty ranking'],
  ['country', 'A country chapter: Germany'],
  ['methodology', 'Methodology appendix'],
]

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
      {/* The report cover, as the front page's header (#91). */}
      <PageBand
        hero
        kicker="EU-27 · Independent Research"
        title={<>Sovereign Data Centres for the EU{'\u2011'}27</>}
      >
        <p className="mt-4 max-w-3xl text-lg text-white/85 sm:text-xl">
          A research-backed framework for every EU member state: which critical government data
          should remain within national borders—and which sovereign data centres should host it.
        </p>
      </PageBand>
      <p className="mb-6 max-w-3xl text-[var(--color-fg-secondary)]">
        Each member state analysed on its own fundamentals: the critical data holdings it cannot let
        depend on infrastructure a foreign state can compel or switch off, who operates them, under
        which law, and where they run. Every fact is footnoted to its source; where no checked
        source has been found yet, the value is withheld and the gap is shown.
      </p>
      <p className="mb-6 max-w-3xl rounded border-l-4 border-[var(--color-accent)] bg-[var(--color-bg-emphasis)] px-3 py-2 text-sm font-medium">
        {bundle.notice.disclaimer}
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

      <section className="mb-6 rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-3">
        <a href="/eu27-report.pdf" className="group block">
          <div className="font-semibold text-[var(--color-accent-text)] group-hover:underline">
            EU-27 report (PDF)
          </div>
          <div className="text-sm text-[var(--color-fg-secondary)]">
            Every member state in one document, with a table of contents, footnoted sources and a
            source appendix. Each country is also available as its own PDF.
          </div>
        </a>
        <ul
          className="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-4"
          aria-label="Pages from the EU-27 report"
        >
          {REPORT_PREVIEWS.map(([name, caption]) => (
            <li key={name}>
              <a href="/eu27-report.pdf" className="block">
                <img
                  src={`/previews/report-${name}.png`}
                  alt={`Page from the EU-27 report: ${caption}`}
                  loading="lazy"
                  width={910}
                  height={1286}
                  className="h-auto w-full rounded border border-[var(--color-border)] shadow-sm transition-shadow hover:shadow-md"
                  onError={e => {
                    // Previews are built with the PDFs (book/report.py); absent in a dev build.
                    e.currentTarget.closest('li')?.remove()
                  }}
                />
                <span className="mt-1 block text-xs text-[var(--color-fg-muted)]">{caption}</span>
              </a>
            </li>
          ))}
        </ul>
      </section>

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
