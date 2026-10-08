import type { ReactNode } from 'react'

import type { Block, Bundle, Document, Span } from '@/data/types'

/**
 * Renders the content model (model/document.py) -- the same document the PDF typesets.
 *
 * A fact carries superscript links to its numbered sources in the list below the page; a gap
 * is set in muted italics, so a withheld value reads as a gap and never as a fact (#75).
 * Nothing here adds a sentence: a renderer that writes content becomes a second source.
 */
export function SpanView({ span, numbers, bundle }: SpanProps) {
  if (span.role === 'gap') {
    return <em className="text-[var(--color-fg-muted)]">{span.t}</em>
  }
  if (span.role === 'disputed') {
    return (
      <em className="border-b border-dashed border-[var(--color-highlight)] text-[var(--color-fg-muted)]">
        {span.t}
      </em>
    )
  }
  if (span.role !== 'fact') return <>{span.t}</>
  const ids = [
    ...new Set((span.c ?? []).flatMap(claim => (bundle.claims[claim] ?? []).map(c => c.source_id))),
  ]
  return (
    <>
      {span.t}
      {ids.map(sid => {
        const n = numbers.get(sid)
        return (
          <sup key={sid} className="ml-0.5">
            <a
              href={`#src-${n}`}
              className="text-[var(--color-accent-text)] no-underline hover:underline"
              aria-label={`Source ${n}: ${bundle.sources[sid]?.label ?? sid}. Evidence: ${span.g ?? ''}`}
            >
              [{n}]
            </a>
          </sup>
        )
      })}
    </>
  )
}

interface SpanProps {
  span: Span
  numbers: Map<string, number>
  bundle: Bundle
}

function Spans({ spans, ...rest }: { spans: Span[] } & Omit<SpanProps, 'span'>) {
  return (
    <>
      {spans.map((s, i) => (
        <span key={i}>
          {i > 0 ? ' ' : null}
          <SpanView span={s} {...rest} />
        </span>
      ))}
    </>
  )
}

function BlockView({ block, ...rest }: { block: Block } & Omit<SpanProps, 'span'>) {
  switch (block.type) {
    case 'p':
      return (
        <p className="mb-3 max-w-3xl">
          <Spans spans={block.spans} {...rest} />
        </p>
      )
    case 'callout':
      return (
        <div
          className={`mb-4 max-w-3xl rounded border-l-4 px-4 py-3 text-sm ${
            block.tone === 'gap'
              ? 'border-[var(--color-highlight)] bg-[var(--color-bg-emphasis)]'
              : block.tone === 'method'
                ? 'border-[var(--color-method)] bg-[var(--color-method-wash)]'
                : 'border-[var(--color-accent)] bg-[var(--color-bg-emphasis)]'
          }`}
        >
          <Spans spans={block.spans} {...rest} />
        </div>
      )
    case 'list':
      return (
        <ul className="mb-3 max-w-3xl list-disc pl-5 text-sm">
          {block.items.map((item, i) => (
            <li key={i}>
              <Spans spans={item} {...rest} />
            </li>
          ))}
        </ul>
      )
    case 'table':
      return (
        // Focusable, so a keyboard user can scroll a table wider than the page (WCAG 2.1.1).
        <div
          className="scroll-x rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] mb-5"
          tabIndex={0}
          role="region"
          aria-label={block.columns.map(c => c.t).join(', ')}
        >
          <table className="w-full min-w-[32rem] border-collapse text-sm">
            <thead>
              <tr className="bg-[var(--color-bg-emphasis)] text-xs tracking-wider text-[var(--color-fg-muted)] uppercase shadow-[inset_0_-2px_0_var(--color-eu-blue)]">
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
              {block.rows.map((row, r) => (
                <tr key={r} className="border-t border-[var(--color-border)] align-top">
                  {row.map((cell, i) => {
                    const Cell = i === 0 ? 'th' : 'td'
                    return (
                      <Cell
                        key={i}
                        scope={i === 0 ? 'row' : undefined}
                        className={`px-3.5 py-2.5 ${i === 0 ? 'font-normal' : ''} ${
                          block.align?.[i] === 'right' ? 'text-right tabular-nums' : 'text-left'
                        }`}
                      >
                        <SpanView span={cell} {...rest} />
                      </Cell>
                    )
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )
  }
}

export function DocumentView({
  doc,
  bundle,
  numbers,
  tables = {},
}: {
  doc: Document
  bundle: Bundle
  numbers: Map<string, number>
  /** A page's own layout for one section's table, by section id; it must render the same spans. */
  tables?: Record<string, (block: Extract<Block, { type: 'table' }>) => ReactNode>
}) {
  return (
    <>
      {doc.sections.map((s, i) => (
        <section key={s.id} id={s.id} className="mb-10 scroll-mt-4">
          <h2 className="mb-4 font-display text-2xl font-bold tracking-tight">
            <span className="mb-1 block font-sans text-xs font-semibold tracking-[0.14em] text-[var(--color-accent-text)] uppercase">
              Section {i + 1}
            </span>
            {s.title}
          </h2>
          {s.blocks.map((b, j) =>
            b.type === 'table' && tables[s.id] ? (
              <div key={j}>{tables[s.id]!(b)}</div>
            ) : (
              <BlockView key={j} block={b} bundle={bundle} numbers={numbers} />
            ),
          )}
        </section>
      ))}
    </>
  )
}
