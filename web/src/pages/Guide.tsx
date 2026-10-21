import { Link, useParams } from 'react-router-dom'

import { PageBand } from '@/components/PageBand'
import { BUTTON_OUTLINE, CARD, SectionHead } from '@/components/ui'
import { FIGURES } from '@/data/guideFigures'
import { AUDIENCE_GUIDES, TASK_GUIDES } from '@/data/guides'
import type { GuideLink } from '@/data/guides'
import type { Bundle } from '@/data/types'
import { useTx } from '@/i18n'
import { NotFound } from './NotFound'

/** A step's link: a route, a route with the report section to open, or a file such as the report PDF. */
function StepLink({ link }: { link: GuideLink }) {
  const { tx } = useTx()
  const text = <>{tx(link.label)} →</>
  const className =
    'mt-auto pt-2 text-sm font-semibold text-[var(--color-accent-text)] hover:underline'
  return link.to.endsWith('.pdf') ? (
    <a href={link.to} className={className}>
      {text}
    </a>
  ) : (
    <Link
      to={link.to}
      state={link.section ? { section: link.section } : undefined}
      className={className}
    >
      {text}
    </Link>
  )
}

/**
 * One guide page (#102): `/for/:slug` for an audience, `/how/:slug` for a task. The words come from
 * data/guides.ts and are this project's advice on using the site, not findings; the figures are counted
 * from the bundle as the page renders, each linked to where it can be checked.
 */
export function Guide({ bundle, kind }: { bundle: Bundle; kind: 'for' | 'how' }) {
  const { slug = '' } = useParams()
  const { tx, txr } = useTx()
  const [guides, others] =
    kind === 'for' ? [AUDIENCE_GUIDES, TASK_GUIDES] : [TASK_GUIDES, AUDIENCE_GUIDES]
  const guide = guides.find(g => g.slug === slug)
  if (!guide) return <NotFound />
  const related = others.filter(g => guide.related.includes(g.slug))
  const otherKind = kind === 'for' ? 'how' : 'for'

  return (
    <article>
      <PageBand
        kicker={kind === 'for' ? tx('EU-27 · I am…') : tx('EU-27 · I need to…')}
        title={tx(guide.title)}
      >
        <p className="mt-3 max-w-3xl text-lg text-[var(--color-fg-secondary)]">{tx(guide.lede)}</p>
      </PageBand>

      {guide.when?.length ? (
        <section className="mb-12" aria-labelledby="guide-when">
          <SectionHead
            eyebrow={tx('When this helps')}
            title={<span id="guide-when">{tx('You are here because')}</span>}
          />
          <ul className="grid gap-2.5 sm:grid-cols-2">
            {guide.when.map(w => (
              <li
                key={w}
                className="rounded border-l-4 border-[var(--color-accent-text)] bg-[var(--color-bg-emphasis)] px-4 py-3 text-sm font-medium"
              >
                {tx(w)}
              </li>
            ))}
          </ul>
        </section>
      ) : null}

      <section className="mb-12" aria-labelledby="guide-steps">
        <SectionHead
          eyebrow={kind === 'for' ? tx('What you can do here') : tx('Step by step')}
          title={
            <span id="guide-steps">
              {kind === 'for' ? tx('On this site, today') : tx('How to do it on this site')}
            </span>
          }
        />
        <ol className="grid gap-4 sm:grid-cols-2">
          {guide.steps.map((s, i) => (
            <li key={s.title} className={`${CARD} flex flex-col gap-2 p-5`}>
              <span
                aria-hidden="true"
                className="grid h-7 w-7 place-items-center rounded-full bg-[var(--color-eu-blue)] font-display text-xs font-bold text-white"
              >
                {i + 1}
              </span>
              <h3 className="font-display text-lg font-bold">{tx(s.title)}</h3>
              <p className="text-sm text-[var(--color-fg-secondary)]">{tx(s.text)}</p>
              <StepLink link={s.link} />
            </li>
          ))}
        </ol>
      </section>

      <section className="mb-12" aria-labelledby="guide-figures">
        <SectionHead
          eyebrow={tx('From the data today')}
          title={<span id="guide-figures">{tx('Where the evidence stands')}</span>}
          aside={tx(
            'Counted from the published dataset as this page loads. Each figure links to the page where it can be checked.',
          )}
        />
        {/* A list, not a <dl>: each figure carries a link, which a definition list's groups may not hold
            beside their <dt> and <dd>. */}
        <ul className="grid gap-px overflow-hidden rounded border border-[var(--color-border)] bg-[var(--color-border)] sm:grid-cols-2 lg:grid-cols-4">
          {guide.figures.map(id => {
            const f = FIGURES[id](bundle, tx)
            return (
              <li key={id} className="flex flex-col gap-1.5 bg-[var(--color-bg-card)] p-5">
                <p
                  data-figure
                  className="font-display text-3xl leading-none font-extrabold tabular-nums"
                >
                  {f.value}
                </p>
                <p className="text-sm text-[var(--color-fg-secondary)]">{f.label}</p>
                <Link
                  to={f.to}
                  className="mt-auto pt-1 text-xs font-semibold text-[var(--color-accent-text)] hover:underline"
                >
                  {txr('Check it{label}', { label: <span className="sr-only">: {f.label}</span> })}{' '}
                  →
                </Link>
              </li>
            )
          })}
        </ul>
      </section>

      <div className="mb-12 grid gap-8 lg:grid-cols-2">
        {guide.takeaways?.length ? (
          <section aria-labelledby="guide-takeaways">
            <SectionHead
              eyebrow={tx('What you take away')}
              title={<span id="guide-takeaways">{tx('What this gives you')}</span>}
            />
            <ul className="grid gap-2.5 text-sm">
              {guide.takeaways.map(t => (
                <li key={t} className="grid grid-cols-[auto_minmax(0,1fr)] gap-3">
                  <span
                    aria-hidden="true"
                    className="mt-1.5 h-2 w-2 rounded-full bg-[var(--color-accent-text)]"
                  />
                  {tx(t)}
                </li>
              ))}
            </ul>
          </section>
        ) : null}
        {guide.missing.length ? (
          <section aria-labelledby="guide-missing">
            <SectionHead
              eyebrow={tx('Not here yet')}
              title={<span id="guide-missing">{tx('What the site does not do')}</span>}
            />
            <ul className="grid gap-2.5 text-sm text-[var(--color-fg-secondary)]">
              {guide.missing.map(item => (
                <li key={item} className="grid grid-cols-[auto_minmax(0,1fr)] gap-3">
                  <span
                    aria-hidden="true"
                    className="mt-1.5 h-2 w-2 rounded-full border border-dashed border-[var(--color-gap-mark)]"
                  />
                  {tx(item)}
                </li>
              ))}
            </ul>
          </section>
        ) : null}
      </div>

      {related.length ? (
        <nav
          aria-label={kind === 'for' ? tx('Tasks for this reader') : tx('Readers who need this')}
          className="mb-4"
        >
          <p className="mb-3 text-xs font-bold tracking-[0.16em] text-[var(--color-accent-text)] uppercase">
            {kind === 'for' ? tx('Start with a task') : tx('Written for')}
          </p>
          <div className="flex flex-wrap gap-2.5">
            {related.map(g => (
              <Link key={g.slug} to={`/${otherKind}/${g.slug}`} className={BUTTON_OUTLINE}>
                {tx(g.label).replaceAll('\n', ' ')}
              </Link>
            ))}
          </div>
        </nav>
      ) : null}
    </article>
  )
}
