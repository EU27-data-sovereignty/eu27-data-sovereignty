import type { ReactNode } from 'react'

import { GROUP_FILL } from '@/charts/groups'
import type { Block, Bundle, Span } from '@/data/types'
import { SpanView } from './DocumentView'
import { CARD } from './ui'
import { num, text, verdicts } from '@/utils/blocks'

/**
 * Graphics for the methodology and fact-check documents (#99). Each one draws a block the generated
 * document already holds -- a count table as bars, the priority rule as a formula, the placement rules as
 * a ladder, the check steps as a timeline -- so every word and number still comes from
 * model/methodology.py and model/factcheck_appendix.py. Nothing here states a fact of its own (#74).
 */

type Table = Extract<Block, { type: 'table' }>
type List = Extract<Block, { type: 'list' }>

const HEAD =
  'bg-[var(--color-bg-emphasis)] text-xs tracking-wider text-[var(--color-fg-muted)] uppercase shadow-[inset_0_-2px_0_var(--color-method)]'

function Cell({ span, bundle }: { span: Span; bundle: Bundle }) {
  return <SpanView span={span} numbers={new Map()} bundle={bundle} />
}

export function Track({ share, tone = 'var(--color-method)' }: { share: number; tone?: string }) {
  return (
    <span className="block h-2 overflow-hidden rounded-full bg-[var(--color-bg-emphasis)]">
      <span
        className="block h-full rounded-full"
        style={{ width: `${Math.max(share > 0 ? 2 : 0, share * 100)}%`, background: tone }}
      />
    </span>
  )
}

/** A two-column table whose second column counts something: each row as a labelled bar. */
export function CountBars({ block, bundle }: { block: Table; bundle: Bundle }) {
  const max = Math.max(1, ...block.rows.map(r => num(r[1])))
  return (
    <div className={`${CARD} mb-5 max-w-3xl overflow-hidden`}>
      <table className="w-full border-collapse text-sm">
        <thead>
          <tr className={HEAD}>
            <th scope="col" className="px-4 py-2.5 text-left font-semibold">
              {block.columns[0]!.t}
            </th>
            <th scope="col" className="w-1/2 px-4 py-2.5 text-left font-semibold">
              <span className="sr-only">Share</span>
            </th>
            <th scope="col" className="px-4 py-2.5 text-right font-semibold">
              {block.columns[1]!.t}
            </th>
          </tr>
        </thead>
        <tbody>
          {block.rows.map((r, i) => (
            <tr key={i} className="border-t border-[var(--color-border)]">
              <th scope="row" className="px-4 py-2 text-left font-normal">
                <Cell span={r[0]!} bundle={bundle} />
              </th>
              <td className="px-4 py-2" aria-hidden="true">
                <Track share={num(r[1]) / max} />
              </td>
              <td className="px-4 py-2 text-right font-semibold tabular-nums">
                <Cell span={r[1]!} bundle={bundle} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

/**
 * The priority rule as a formula: "Priority = term (scale) + term (scale) + ...", then its thresholds. The
 * terms, scales and thresholds are cut from the rule's own text; if it no longer parses, the text is shown.
 */
export function PriorityFormula({ rule }: { rule: string }) {
  const m = /^(?:.*?\.\s*)?Priority = (.+?)\.\s*(.*)$/s.exec(rule)
  const terms = m?.[1]?.split(' + ').map(t => /^(.+?) \((.+)\)$/.exec(t.trim()))
  if (!m || !terms || terms.some(t => !t)) return <p className="mb-3 max-w-3xl">{rule}</p>
  return (
    <figure className={`${CARD} mb-5 max-w-4xl p-5`}>
      <figcaption className="mb-3 text-xs font-semibold tracking-[0.12em] text-[var(--color-method)] uppercase">
        Priority of a holding
      </figcaption>
      <div className="flex flex-wrap items-stretch gap-2 font-display">
        <span className="self-center text-xl font-bold">Priority =</span>
        {terms.map((t, i) => (
          <span key={i} className="flex items-stretch gap-2">
            {i > 0 ? <span className="self-center text-xl font-bold">+</span> : null}
            <span className="rounded border border-[var(--color-method)] bg-[var(--color-method-wash)] px-3 py-2">
              <span className="block font-bold">{t![1]}</span>
              <span className="block font-sans text-xs text-[var(--color-fg-secondary)]">
                {t![2]}
              </span>
            </span>
          </span>
        ))}
      </div>
      {m[2] ? <p className="mt-3 text-sm font-medium">{m[2]}</p> : null}
    </figure>
  )
}

/** The placement rules, applied first to last, as a numbered ladder in each group's colour. */
export function RuleLadder({ block, bundle }: { block: List; bundle: Bundle }) {
  const groups = bundle.sovereignty.groups
  return (
    <ol className="mb-5 grid max-w-3xl gap-2">
      {block.items.map((item, i) => {
        const t = text(item)
        const g = groups.find(x => t.startsWith(`${x.label}: `))
        return (
          <li
            key={i}
            className={`${CARD} grid grid-cols-[2rem_minmax(0,1fr)] items-start gap-3 p-3.5 text-sm`}
          >
            <span
              aria-hidden="true"
              className="grid h-7 w-7 place-items-center rounded-full font-display text-xs font-bold text-white"
              style={{ background: 'var(--color-method-deep)' }}
            >
              {i + 1}
            </span>
            <span>
              {g ? (
                <>
                  <strong className="mr-1 inline-flex items-center gap-1.5">
                    <span
                      aria-hidden="true"
                      className="inline-block h-2.5 w-2.5 rounded-sm"
                      style={{ background: GROUP_FILL[g.id] }}
                    />
                    {g.label}:
                  </strong>
                  {t.slice(g.label.length + 2)}
                </>
              ) : (
                t
              )}
            </span>
          </li>
        )
      })}
    </ol>
  )
}

/** Who checks whom: each row of the writer/checker table as a pair, so no model checks its own work. */
export function Pairing({ block, bundle }: { block: Table; bundle: Bundle }) {
  return (
    <div className="mb-5 grid max-w-3xl gap-2" role="table" aria-label={text(block.columns)}>
      <div role="row" className="sr-only">
        {block.columns.map((c, i) => (
          <span key={i} role="columnheader">
            {c.t}
          </span>
        ))}
      </div>
      {block.rows.map((r, i) => (
        <div
          key={i}
          role="row"
          className="grid grid-cols-[minmax(0,1fr)_auto_minmax(0,1fr)] items-center gap-3"
        >
          <span role="cell" className={`${CARD} px-4 py-3`}>
            <span className="block text-[0.68rem] font-semibold tracking-[0.12em] text-[var(--color-fg-muted)] uppercase">
              {block.columns[0]!.t}
            </span>
            <code className="text-sm">
              <Cell span={r[0]!} bundle={bundle} />
            </code>
          </span>
          <span aria-hidden="true" className="text-lg font-bold text-[var(--color-method)]">
            →
          </span>
          <span
            role="cell"
            className={`${CARD} border-[var(--color-method)] bg-[var(--color-method-wash)] px-4 py-3`}
          >
            <span className="block text-[0.68rem] font-semibold tracking-[0.12em] text-[var(--color-fg-muted)] uppercase">
              {block.columns[1]!.t}
            </span>
            <code className="text-sm">
              <Cell span={r[1]!} bundle={bundle} />
            </code>
          </span>
        </div>
      ))}
    </div>
  )
}

/** A list of steps as a timeline; a leading command (`factcheck.py prepare`) is set in code. */
export function Steps({ block }: { block: List }) {
  return (
    <ol className="mb-5 max-w-3xl border-l-2 border-[var(--color-method)] pl-6">
      {block.items.map((item, i) => {
        const t = text(item)
        const cmd = /^(\S+\.(?:py|js|sh|yml)(?: [a-z]+)?)\b(.*)$/s.exec(t)
        return (
          <li key={i} className="relative mb-4 text-sm last:mb-0">
            <span
              aria-hidden="true"
              className="absolute top-0 -left-[2.15rem] grid h-6 w-6 place-items-center rounded-full font-display text-xs font-bold text-white"
              style={{ background: 'var(--color-method-deep)' }}
            >
              {i + 1}
            </span>
            {cmd ? (
              <>
                <code className="rounded bg-[var(--color-method-wash)] px-1.5 py-0.5 font-semibold">
                  {cmd[1]}
                </code>
                {cmd[2]}
              </>
            ) : (
              t
            )}
          </li>
        )
      })}
    </ol>
  )
}

const VERDICT_FILL: Record<string, string> = {
  supported: 'var(--color-method)',
  'not supported': 'var(--color-rank-5)',
  unclear: 'var(--color-eu-gold)',
}

/** A table drawn as usual, with a bar beside the cells of named columns. */
export function BarredTable({
  block,
  bundle,
  bars,
}: {
  block: Table
  bundle: Bundle
  bars: Record<number, (row: Span[]) => ReactNode>
}) {
  return (
    <div
      className={`scroll-x ${CARD} mb-5`}
      tabIndex={0}
      role="region"
      aria-label={text(block.columns)}
    >
      <table className="w-full min-w-[44rem] border-collapse text-sm">
        <thead>
          <tr className={HEAD}>
            {block.columns.map((c, i) => (
              <th
                key={i}
                scope="col"
                className={`px-3.5 py-2.5 font-semibold ${block.align?.[i] === 'right' ? 'text-right' : 'text-left'}`}
              >
                {c.t}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {block.rows.map((r, ri) => (
            <tr key={ri} className="border-t border-[var(--color-border)] align-middle">
              {r.map((cell, i) => {
                const C = i === 0 ? 'th' : 'td'
                return (
                  <C
                    key={i}
                    scope={i === 0 ? 'row' : undefined}
                    className={`px-3.5 py-2.5 ${i === 0 ? 'text-left font-normal whitespace-nowrap' : ''} ${
                      block.align?.[i] === 'right' ? 'text-right tabular-nums' : ''
                    }`}
                  >
                    <Cell span={cell} bundle={bundle} />
                    {bars[i] ? <span className="mt-1.5 block">{bars[i]!(r)}</span> : null}
                  </C>
                )
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export function VerdictBar({ cell }: { cell: string }) {
  const parts = verdicts(cell)
  const total = parts.reduce((n, p) => n + p[1], 0)
  if (!total) return null
  return (
    <span aria-hidden="true" className="flex h-2 min-w-32 overflow-hidden rounded-full">
      {parts.map(([k, n]) =>
        n ? (
          <span
            key={k}
            style={{ flex: n, background: VERDICT_FILL[k] ?? 'var(--color-fg-muted)' }}
          />
        ) : null,
      )}
    </span>
  )
}

/** The per-state table's own columns summed into headline tiles above it. */
export function Totals({ block }: { block: Table }) {
  const tiles = block.columns
    .slice(1)
    .map((c, i) => [c.t, block.rows.reduce((n, r) => n + (num(r[i + 1]) || 0), 0)])
  return (
    <dl className="mb-4 grid max-w-3xl grid-cols-2 gap-px overflow-hidden rounded border border-[var(--color-border)] bg-[var(--color-border)] sm:grid-cols-4">
      {tiles.map(([label, n]) => (
        <div key={label} className="flex flex-col-reverse bg-[var(--color-bg-card)] p-4">
          <dt className="text-xs text-[var(--color-fg-muted)]">{label}, all states</dt>
          <dd className="font-display text-2xl font-bold tabular-nums">
            {Number(n).toLocaleString('en')}
          </dd>
        </div>
      ))}
    </dl>
  )
}
