import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import { ASK_EXAMPLES, ASK_MAX } from '@/data/ask'
import { coverage } from '@/data/sources'
import type { Bundle } from '@/data/types'
import { AudienceSelector } from '@/components/AudienceSelector'
import { Hero } from '@/components/Hero'
import { BUTTON, CARD, SectionHead } from '@/components/ui'

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
        <span className="mt-1.5 self-start rounded-full bg-[var(--color-bg-emphasis)] px-2.5 py-0.5 text-xs font-semibold text-[var(--color-accent-text)]">
          ● {pending}
        </span>
      ) : (
        <span className="mt-1.5 h-1.5 overflow-hidden rounded-full bg-[var(--color-bg-emphasis)]">
          <span
            className="block h-full rounded-full bg-[var(--color-accent-text)]"
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
  const go = (q: string) => navigate('/ask', { state: { question: q.trim() } })

  return (
    <article>
      {/* The landing design's top (#101): hero, then the audience selector band, both full width. */}
      <Hero />
      <AudienceSelector />

      <div className="mx-auto max-w-6xl px-4 py-10 sm:py-14">
        {/* The front page's main act (#101): ask anything, in your own words. */}
        <section aria-labelledby="ask-heading" className="mx-auto mb-14 max-w-3xl text-center">
          <h2
            id="ask-heading"
            className="font-display text-4xl leading-tight font-extrabold tracking-tight sm:text-6xl"
          >
            Hello, Europe
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-[var(--color-fg-secondary)] sm:text-xl">
            Whatever is on your mind about EU Data Sovereignty, ask any question here.
          </p>
          <form
            role="search"
            className="mt-8 rounded-2xl border border-[var(--color-border)] bg-[var(--color-bg-card)] p-2 text-left shadow-[0_8px_30px_rgb(11_27_63/0.08)] focus-within:border-[var(--color-accent-text)]"
            onSubmit={e => {
              e.preventDefault()
              if (question.trim()) go(question)
            }}
          >
            <label htmlFor="overview-ask" className="sr-only">
              Ask any question
            </label>
            <textarea
              id="overview-ask"
              value={question}
              maxLength={ASK_MAX}
              rows={3}
              onChange={e => setQuestion(e.target.value)}
              onKeyDown={e => {
                // Enter asks, as in a chat box; Shift+Enter starts a new line.
                if (e.key === 'Enter' && !e.shiftKey && question.trim()) {
                  e.preventDefault()
                  go(question)
                }
              }}
              placeholder="Ask anything, in your own words…"
              // 16 px and up: iPhone Safari zooms the whole page into any field set smaller (#92).
              className="w-full resize-none bg-transparent px-4 pt-3 text-lg outline-none placeholder:text-[var(--color-fg-muted)]"
            />
            <div className="flex items-center justify-between gap-3 px-4 pb-2">
              <span className="text-xs text-[var(--color-fg-muted)] tabular-nums">
                {question.length} / {ASK_MAX}
              </span>
              <button
                type="submit"
                disabled={!question.trim()}
                className={`${BUTTON} px-7 text-base disabled:opacity-50`}
              >
                Ask
              </button>
            </div>
          </form>
          <p className="mx-auto mt-3 max-w-2xl text-xs text-[var(--color-fg-muted)]">
            Your question is sent to Anthropic’s API to generate the answer. This site does not
            store it. Answers come only from this project’s sourced findings, with a citation for
            every fact.
          </p>
          <div className="mt-7">
            <p className="mb-3 text-xs font-bold tracking-[0.16em] text-[var(--color-accent-text)] uppercase">
              Or start from one of these
            </p>
            <ul className="flex flex-wrap justify-center gap-2">
              {ASK_EXAMPLES.map(q => (
                <li key={q}>
                  <button
                    type="button"
                    onClick={() => go(q)}
                    className="rounded-full border border-[var(--color-border)] bg-[var(--color-bg-card)] px-4 py-2 text-left text-sm text-[var(--color-fg-secondary)] hover:border-[var(--color-accent-text)] hover:text-[var(--color-fg-primary)]"
                  >
                    {q}
                  </button>
                </li>
              ))}
            </ul>
          </div>
        </section>

        <p className="mb-10 max-w-3xl text-[var(--color-fg-secondary)]">
          Each member state analysed on its own fundamentals: the critical data holdings it cannot
          let depend on infrastructure a foreign state can compel or switch off, who operates them,
          under which law, and where they run. Every fact is footnoted to its source; where no
          checked source has been found yet, the value is withheld and the gap is shown.
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
                className={`${CARD} flex flex-col gap-2.5 p-6 transition hover:-translate-y-0.5 hover:border-[var(--color-accent-text)]`}
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
                    // Not lazy: a missing preview is removed below, and removing it while a reader (or a test)
                    // scrolls past would shift the page under their tap. Loading up front settles it first.
                    decoding="async"
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
      </div>
    </article>
  )
}
