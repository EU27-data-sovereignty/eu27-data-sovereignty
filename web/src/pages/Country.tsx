import { Link, useParams } from 'react-router-dom'

import { DocumentView } from '@/components/DocumentView'
import { SourceList } from '@/components/SourceList'
import { submitLink } from '@/data/contribute'
import { claimsBySource, coverage, factCounts, numberSources } from '@/data/sources'
import type { Bundle } from '@/data/types'
import { NotFound } from './NotFound'
import { PageBand } from '@/components/PageBand'
import { spanText, useT, useTx } from '@/i18n'

/**
 * One member state, analysed on its own fundamentals (#72). The body is the content model --
 * the same document as /report/<ISO>.pdf and countries/<ISO>/GOAL.md -- so the sections, facts
 * and gaps are identical across all three; only the presentation differs.
 */
export function Country({ bundle }: { bundle: Bundle }) {
  const { iso = '' } = useParams()
  const t = useT()
  const { tx, txr } = useTx()
  const code = iso.toUpperCase()
  const doc = bundle.documents[code]
  const country = bundle.countries[code]
  if (!doc || !country) return <NotFound />

  const numbers = numberSources([doc], bundle)
  const claims = claimsBySource([doc], bundle)
  const cov = coverage(country)
  const { facts, gaps } = factCounts(doc)

  return (
    <article className="lg:grid lg:grid-cols-[12rem_1fr] lg:gap-8">
      <nav
        aria-label={t('country.contents')}
        className="mb-6 text-sm lg:sticky lg:top-4 lg:mb-0 lg:self-start"
      >
        <h2 className="mb-2 font-semibold text-[var(--color-fg-secondary)]">
          {t('country.contents')}
        </h2>
        <ol className="space-y-1">
          {doc.sections.map((s, i) => (
            <li key={s.id}>
              <a className="text-[var(--color-accent-text)] hover:underline" href={`#${s.id}`}>
                {i + 1}. {spanText({ t: s.title, key: s.key }, t)}
              </a>
            </li>
          ))}
          <li>
            <a className="text-[var(--color-accent-text)] hover:underline" href="#sources">
              {t('country.sources')}
            </a>
          </li>
        </ol>
      </nav>

      <div>
        <p className="text-xs tracking-widest text-[var(--color-fg-muted)] uppercase">
          <Link to="/countries" className="hover:underline">
            {t('nav.countries')}
          </Link>{' '}
          · {code}
        </p>
        <PageBand
          kicker={`${t('site.kicker')} · ${t('country.kicker')} · ${doc.iso}`}
          title={doc.name}
        />
        <p className="mb-4 text-sm text-[var(--color-fg-secondary)]">
          {tx('{verified} of {total} critical holding classes verified', {
            verified: cov.verified,
            total: cov.total,
          })}{' '}
          ·{' '}
          {tx('{n, plural, one {# sourced fact shown} other {# sourced facts shown}}', {
            n: facts,
          })}{' '}
          · {t('fact.withheld', gaps)} · {tx('capacity not yet sized')}
        </p>
        <p className="mb-8">
          <a
            href={`/report/${code}.pdf`}
            className="inline-block rounded bg-[var(--color-accent)] px-3 py-1.5 text-sm font-semibold text-[var(--color-fg-on-accent)]"
          >
            {tx('Download the {name} report (PDF)', { name: doc.name })}
          </a>
        </p>

        <p className="mb-8 max-w-3xl rounded border border-[var(--color-border)] px-3 py-2 text-sm">
          {tx(
            '{n, plural, one {Know a public source for the withheld value, or a better one for a fact?} other {Know a public source for one of the # withheld values, or a better one for a fact?}}',
            {
              n: gaps,
            },
          )}{' '}
          <a className="underline" href={submitLink(bundle, code)} rel="noreferrer">
            {tx('Submit a source')}
          </a>
          .{' '}
          {txr('Every fact also has a {label} link in its source entry.', {
            label: <em>{t('fact.check_this')}</em>,
          })}{' '}
          {txr(
            'Submissions are checked by machine and then by a different person who reads the language ({link}).',
            {
              link: (
                <Link to="/methodology" className="underline">
                  {tx('methodology')}
                </Link>
              ),
            },
          )}
        </p>

        <DocumentView doc={doc} bundle={bundle} numbers={numbers} />
        <p className="my-6 max-w-3xl text-sm">
          {txr(
            'How each fact above was checked by a second model, the one that did not write it: {link}.',
            {
              link: (
                <Link to={`/fact-check/${code}`} className="underline">
                  {tx('fact check for {name}', { name: doc.name })}
                </Link>
              ),
            },
          )}
        </p>
        <SourceList bundle={bundle} numbers={numbers} claims={claims} />
      </div>
    </article>
  )
}
