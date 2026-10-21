import { Link } from 'react-router-dom'

import { DocumentView } from '@/components/DocumentView'
import { HostingCards } from '@/components/HostingCards'
import { PageBand } from '@/components/PageBand'
import { SourceList } from '@/components/SourceList'
import { claimsBySource, numberSources } from '@/data/sources'
import type { Bundle } from '@/data/types'
import { lookup, useT, useTx } from '@/i18n'

/**
 * Where each state's key registers are hosted, and by whom (#95). The body is the generated overview
 * (document.infrastructure), whose cells are the spans the country reports print, so a fact here
 * carries the same source and the same fact check as on its country page. Nothing is written here.
 */
export function Infrastructure({ bundle }: { bundle: Bundle }) {
  const { tx, txr } = useTx()
  const t = useT()
  const doc = bundle.infrastructure
  const numbers = numberSources([doc], bundle)
  const claims = claimsBySource([doc], bundle)
  const table = doc.sections.find(s => s.id === 'hosting')?.blocks.find(b => b.type === 'table')
  const hosting = table?.type === 'table' ? table.rows : []

  return (
    <article>
      <PageBand
        kicker={tx('EU-27 · Key infrastructure')}
        title={tx(doc.name)}
        facts={[
          [String(hosting.filter(r => r[4]?.role === 'fact').length), tx('hosting facts printed')],
          [
            String(hosting.filter(r => r[4]?.role === 'disputed').length),
            tx('withheld as disputed'),
          ],
          [
            tx('{n} of 27', { n: new Set(hosting.map(r => r[0]!.t)).size }),
            tx('states with any sourced hosting'),
          ],
        ]}
      />
      <p className="mb-6 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        {/* The reviewed translation of the disclaimer, while the bundle's still reads word for word as the source; a
            measured disclaimer ("… of … facts verified by a person") prints as the model wrote it (#112). */}
        {bundle.notice.disclaimer === lookup('en')('notice.disclaimer')
          ? t('notice.disclaimer')
          : bundle.notice.disclaimer}{' '}
        {txr('The same overview is in the {report}; each holding in full is on its {page}.', {
          report: (
            <a className="underline" href="/eu27-report.pdf">
              {tx('EU-27 report')}
            </a>
          ),
          page: (
            <Link to="/countries" className="underline">
              {tx('country page')}
            </Link>
          ),
        })}
      </p>
      <DocumentView
        doc={doc}
        bundle={bundle}
        numbers={numbers}
        tables={{
          hosting: block => <HostingCards block={block} bundle={bundle} numbers={numbers} />,
        }}
      />
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
