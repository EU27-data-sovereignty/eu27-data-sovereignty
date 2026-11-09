import { DocumentView } from '@/components/DocumentView'
import { methodBlocks } from '@/utils/methodBlocks'
import { MethodFrame } from '@/components/MethodFrame'
import type { Bundle } from '@/data/types'
import { useTx } from '@/i18n'

/**
 * The methodology, rendered from the generated document (model/methodology.py) that the PDFs carry as
 * their appendix. Nothing is written here: a hand-written method page drifts from the method.
 */
export function Methodology({ bundle }: { bundle: Bundle }) {
  const { tx } = useTx()
  return (
    <MethodFrame title={tx('Methodology')} sections={bundle.methodology.sections}>
      <DocumentView
        doc={bundle.methodology}
        bundle={bundle}
        numbers={new Map()}
        blocks={methodBlocks(bundle)}
      />
      <p className="text-sm text-[var(--color-fg-muted)]">{bundle.national_data_note}</p>
    </MethodFrame>
  )
}
