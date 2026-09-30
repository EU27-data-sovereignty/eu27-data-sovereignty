import { DocumentView } from '@/components/DocumentView'
import type { Bundle } from '@/data/types'

/**
 * The methodology, rendered from the generated document (model/methodology.py) that the PDFs carry as
 * their appendix. Nothing is written here: a hand-written method page drifts from the method.
 */
export function Methodology({ bundle }: { bundle: Bundle }) {
  return (
    <article className="max-w-3xl">
      <h1 className="mb-4 text-2xl font-semibold">Methodology</h1>
      <DocumentView doc={bundle.methodology} bundle={bundle} numbers={new Map()} />
      <p className="text-sm text-[var(--color-fg-muted)]">{bundle.national_data_note}</p>
    </article>
  )
}
