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
          className={`mb-3 max-w-3xl border-l-4 bg-[var(--color-bg-emphasis)] px-3 py-2 text-sm ${
            block.tone === 'gap'
              ? 'border-[var(--color-highlight)]'
              : 'border-[var(--color-accent)]'
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
        <div className="scroll-x mb-4">
          <table className="w-full min-w-[32rem] border-collapse text-sm">
            <thead>
              <tr className="border-b-2 border-[var(--color-accent)] bg-[var(--color-bg-emphasis)]">
                {block.columns.map((c, i) => (
                  <th
                    key={i}
                    scope="col"
                    className={`px-2 py-1.5 font-semibold ${block.align?.[i] === 'right' ? 'text-right' : 'text-left'}`}
                  >
                    {c.t}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {block.rows.map((row, r) => (
                <tr key={r} className="border-b border-[var(--color-border)] align-top">
                  {row.map((cell, i) => {
                    const Cell = i === 0 ? 'th' : 'td'
                    return (
                      <Cell
                        key={i}
                        scope={i === 0 ? 'row' : undefined}
                        className={`px-2 py-1.5 ${i === 0 ? 'font-normal' : ''} ${
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
}: {
  doc: Document
  bundle: Bundle
  numbers: Map<string, number>
}) {
  return (
    <>
      {doc.sections.map((s, i) => (
        <section key={s.id} id={s.id} className="mb-10 scroll-mt-4">
          <h2 className="mb-3 border-b-2 border-[var(--color-highlight)] pb-1 text-lg font-semibold text-[var(--color-accent-text)]">
            {i + 1}. {s.title}
          </h2>
          {s.blocks.map((b, j) => (
            <BlockView key={j} block={b} bundle={bundle} numbers={numbers} />
          ))}
        </section>
      ))}
    </>
  )
}
