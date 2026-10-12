import type { ReactNode } from 'react'

import {
  BarredTable,
  CountBars,
  Pairing,
  PriorityFormula,
  RuleLadder,
  Steps,
  Totals,
  Track,
  VerdictBar,
} from '@/components/MethodGraphics'
import type { Block, Bundle } from '@/data/types'
import { num, text } from './blocks'

type Table = Extract<Block, { type: 'table' }>

const isCountTable = (b: Table) =>
  b.columns.length === 2 && b.rows.length > 1 && b.rows.every(r => !Number.isNaN(num(r[1])))

const isPairing = (b: Table) =>
  b.columns.length === 2 &&
  /written by/i.test(b.columns[0]!.t) &&
  /checked by/i.test(b.columns[1]!.t)

/** The drawing hook for DocumentView on the methodology and fact-check pages. */
export function methodBlocks(bundle: Bundle) {
  return (block: Block, section: string): ReactNode | undefined => {
    if (block.type === 'table') {
      if (isPairing(block)) return <Pairing block={block} bundle={bundle} />
      if (isCountTable(block)) return <CountBars block={block} bundle={bundle} />
      const col = (name: RegExp) => block.columns.findIndex(c => name.test(c.t))
      if (section === 'f-runs') {
        const v = col(/^Verdicts$/)
        if (v >= 0)
          return (
            <BarredTable
              block={block}
              bundle={bundle}
              bars={{ [v]: r => <VerdictBar cell={r[v]!.t} /> }}
            />
          )
      }
      if (section === 'f-states') {
        const printed = col(/^Printed facts$/)
        const withheld = col(/^Withheld$/)
        const max = Math.max(1, ...block.rows.map(r => num(r[printed])))
        const maxWithheld = Math.max(1, ...block.rows.map(r => num(r[withheld]) || 0))
        return (
          <>
            <Totals block={block} />
            <BarredTable
              block={block}
              bundle={bundle}
              bars={{
                ...(printed >= 0
                  ? { [printed]: r => <Track share={num(r[printed]) / max} /> }
                  : {}),
                ...(withheld >= 0
                  ? {
                      [withheld]: r =>
                        num(r[withheld]) ? (
                          <Track
                            share={num(r[withheld]) / maxWithheld}
                            tone="var(--color-rank-5)"
                          />
                        ) : null,
                    }
                  : {}),
              }}
            />
          </>
        )
      }
    }
    if (block.type === 'p' && section === 'm-calculations') {
      const t = text(block.spans)
      if (t.startsWith('Priority of a holding.')) return <PriorityFormula rule={t} />
    }
    if (block.type === 'list') {
      const first = text(block.items[0] ?? [])
      if (bundle.sovereignty.groups.some(g => first.startsWith(`${g.label}: `)))
        return <RuleLadder block={block} bundle={bundle} />
      if (section === 'f-steps') return <Steps block={block} />
    }
    return undefined
  }
}
