import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import { TileMap } from '@/charts/TileMap'
import { CORRECTIONS_URL } from '@/data/contribute'
import { coverage, factCounts } from '@/data/sources'
import type { Bundle } from '@/data/types'
import { PageBand } from '@/components/PageBand'
import { CARD, SectionHead } from '@/components/ui'

/** One headline number with a bar for its share, or a pending chip when there is nothing to show yet. */
function Meter({
  label,
  value,
  of,
  sub,
  pending,
}: {
  label: string
  value: number
  of?: number
  sub: string
  pending?: string
}) {
  return (
    <div className="flex flex-col gap-1.5 bg-[var(--color-bg-card)] p-5">
      <span className="text-sm font-medium text-[var(--color-fg-secondary)]">{label}</span>
      <span className="font-display text-[2.4rem] leading-none font-bold tabular-nums">
        {value.toLocaleString('en')}
        {of !== undefined ? (
          <span className="font-sans text-base font-medium text-[var(--color-fg-muted)]">
            {' '}
            / {of.toLocaleString('en')}
          </span>
        ) : null}
      </span>
      {pending ? (
        <span className="mt-1.5 self-start rounded-full bg-[var(--color-eu-gold)]/15 px-2.5 py-0.5 text-xs font-semibold text-[var(--color-accent-text)]">
          ● {pending}
        </span>
      ) : (
        <span className="mt-1.5 h-1.5 overflow-hidden rounded-full bg-[var(--color-bg-emphasis)]">
          <span
            className="block h-full rounded-full bg-[var(--color-eu-gold)]"
            style={{ width: `${of ? Math.min(100, (value / of) * 100) : 100}%` }}
          />
        </span>
      )}
      <span className="text-xs text-[var(--color-fg-muted)]">{sub}</span>
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
  const navigate = useNavigate()
  const [question, setQuestion] = useState('')
  const countries = Object.values(bundle.countries)
  const covs = countries.map(coverage)
  const verified = covs.reduce((n, c) => n + c.verified, 0)
  const total = covs.reduce((n, c) => n + c.total, 0)
  const tier0 = covs.reduce((n, c) => n + c.tier0, 0)
  const tier0Total = covs.reduce((n, c) => n + c.tier0Total, 0)
  const sources = Object.keys(bundle.sources).length
  const claims = Object.keys(bundle.claims).length
  const tiles = countries.map((c, i) => ({
    iso: c.iso2,
    name: c.name,
    holdings: covs[i]!.verified,
    holdingsTotal: covs[i]!.total,
    tier0: covs[i]!.tier0,
    tier0Total: covs[i]!.tier0Total,
    facts: bundle.documents[c.iso2] ? factCounts(bundle.documents[c.iso2]!).facts : 0,
  }))

  return (
    <article>
      {/* The report cover, as the front page's header (#91), with the 27 beside it (#99). */}
      <PageBand
        hero
        kicker="EU-27 · Independent Research"
        title={<>Sovereign Data Centres for the EU{'\u2011'}27</>}
        aside={<TileMap states={tiles} />}
      >
        <p className="mt-4 max-w-3xl text-lg text-white/85 sm:text-xl">
          A research-backed framework for every EU member state: which critical government data
          should remain within national borders—and which sovereign data centres should host it.
        </p>
        <form
          role="search"
          className="mt-7 flex max-w-xl rounded bg-white p-1.5 shadow-lg"
          onSubmit={e => {
            e.preventDefault()
            navigate('/ask', { state: { question: question.trim() } })
          }}
        >
          <label htmlFor="overview-ask" className="sr-only">
            Ask a question
          </label>
          <input
            id="overview-ask"
            value={question}
            onChange={e => setQuestion(e.target.value)}
            placeholder="Who operates Germany’s population register?"
            className="min-w-0 flex-1 bg-transparent px-3 py-2 text-base text-[var(--color-eu-deep)] outline-none placeholder:text-[var(--color-eu-deep)]/50"
          />
          <button
            type="submit"
            className="rounded bg-[var(--color-eu-blue)] px-4 py-2 text-sm font-semibold text-white"
          >
            Ask
          </button>
        </form>
        <p className="mt-2.5 text-sm text-white/65">
          Or browse{' '}
          <Link to="/sovereignty" className="text-white underline decoration-dotted">
            the ranking
          </Link>{' '}
          ·{' '}
          <Link to="/holdings" className="text-white underline decoration-dotted">
            all {bundle.holding_classes.length} holdings
          </Link>
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          <Link
            to="/countries"
            className="rounded bg-[var(--color-eu-gold)] px-4 py-2.5 text-sm font-semibold text-[var(--color-eu-deep)]"
          >
            Explore the 27 states →
          </Link>
          <a
            href="/eu27-report.pdf"
            className="rounded border border-white/30 px-4 py-2.5 text-sm font-semibold text-white hover:bg-white/10"
          >
            Read the full report
          </a>
        </div>
      </PageBand>

      <p className="mb-6 max-w-3xl text-[var(--color-fg-secondary)]">
        Each member state analysed on its own fundamentals: the critical data holdings it cannot let
        depend on infrastructure a foreign state can compel or switch off, who operates them, under
        which law, and where they run. Every fact is footnoted to its source; where no checked
        source has been found yet, the value is withheld and the gap is shown.
      </p>

      <section aria-label="State of the evidence" className="mb-12">
        <SectionHead
          eyebrow="Where the research stands"
          title="The state of the evidence"
          aside="Every fact is footnoted. Where no checked source exists yet, the value is withheld and the gap stays visible."
        />
        <div className="grid gap-px overflow-hidden rounded border border-[var(--color-border)] bg-[var(--color-border)] sm:grid-cols-2 lg:grid-cols-4">
          <Meter
            label="Critical holdings verified"
            value={verified}
            of={total}
            sub={`27 states × ${bundle.holding_classes.length} classes`}
          />
          <Meter
            label="Tier 0 holdings verified"
            value={tier0}
            of={tier0Total}
            sub="The identity spine every state runs on"
          />
          <Meter label="Sourced claims" value={claims} sub={`from ${sources} checked sources`} />
          <Meter
            label="Countries sized"
            value={0}
            of={27}
            pending="Waiting on measured holdings"
            sub="Sizing needs measured holdings"
          />
        </div>
      </section>

      <section aria-label="Start where your question is" className="mb-12">
        <SectionHead eyebrow="Start where your question is" title="Three ways in" />
        <nav className="grid gap-4 md:grid-cols-3">
          {[
            [
              '/countries',
              '“What about my country?”',
              'Countries',
              'All 27 member states, sortable, each with its own report and footnoted sources.',
              'Browse countries',
            ],
            [
              '/holdings',
              '“Who holds the population register?”',
              'Critical holdings',
              'One kind of holding, such as tax, health or land records, compared across every member state.',
              'Compare holdings',
            ],
            [
              '/sources',
              '“Where does this claim come from?”',
              'Sources',
              'Every checked source, with the quoted passage and each claim it supports.',
              'Trace sources',
            ],
          ].map(([to, q, title, blurb, go]) => (
            <Link
              key={to}
              to={to!}
              className={`${CARD} flex flex-col gap-2.5 p-6 transition hover:-translate-y-0.5 hover:border-[var(--color-eu-blue)] hover:shadow-[inset_0_3px_0_var(--color-eu-gold)]`}
            >
              <span className="text-sm font-semibold text-[var(--color-accent-text)]">{q}</span>
              <span className="font-display text-xl font-bold">{title}</span>
              <span className="text-sm text-[var(--color-fg-secondary)]">{blurb}</span>
              <span className="mt-auto pt-2 text-sm font-semibold text-[var(--color-accent-text)]">
                {go} →
              </span>
            </Link>
          ))}
        </nav>
        <div className="mt-4 flex flex-wrap gap-2.5 text-sm">
          {[
            ['/sovereignty', 'Data-sovereignty ranking'],
            ['/infrastructure', 'Where registers are hosted'],
            ['/ask', 'Ask a question'],
            ['/fact-check', 'The fact check'],
            ['/methodology', 'Methodology'],
          ].map(([to, label]) => (
            <Link
              key={to}
              to={to!}
              className="rounded-full border border-[var(--color-border)] px-3.5 py-1.5 text-[var(--color-fg-secondary)] hover:border-[var(--color-eu-blue)] hover:bg-[var(--color-eu-blue)] hover:text-white"
            >
              {label}
            </Link>
          ))}
        </div>
      </section>

      <section className={`${CARD} mb-10 p-6 sm:p-8`}>
        <p className="mb-1.5 text-xs font-semibold tracking-[0.14em] text-[var(--color-accent-text)] uppercase">
          The full report
        </p>
        <a href="/eu27-report.pdf" className="group block">
          <span className="font-display text-2xl font-bold group-hover:underline">
            EU-27 report (PDF)
          </span>
          <span className="mt-2 block max-w-2xl text-[var(--color-fg-secondary)]">
            Every member state in one document, with a table of contents, footnoted sources and a
            source appendix. Each country is also available as its own PDF.
          </span>
        </a>
        <ul
          className="mt-5 grid grid-cols-2 gap-4 sm:grid-cols-4"
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

      <aside className="grid grid-cols-[auto_minmax(0,1fr)] gap-4 rounded border border-[var(--color-eu-gold)]/45 bg-[var(--color-bg-emphasis)] p-5">
        <span
          aria-hidden="true"
          className="grid h-8 w-8 place-items-center rounded-full bg-[var(--color-eu-gold)] font-display font-bold text-[var(--color-eu-deep)]"
        >
          i
        </span>
        <p className="text-sm font-medium">
          <span>{bundle.notice.disclaimer}</span>{' '}
          <a className="text-[var(--color-accent-text)] underline" href={CORRECTIONS_URL}>
            Open a correction
          </a>
        </p>
      </aside>
    </article>
  )
}
