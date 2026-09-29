import { afterEach, describe, expect, it, vi } from 'vitest'

import {
  buildRequest,
  claimsFor,
  createHandler,
  MAX_QUESTION,
  MODEL,
  validate,
  type AskClient,
  type Corpus,
  type StreamEvent,
} from '../../../api/_ask-core'

/**
 * The /api/ask handler (DECISIONS.md #78), with a fake client: no network, no cost.
 * What matters here is what reaches the model, what comes back to the page, and what never
 * leaves the function (the question, in any log).
 */
const CORPUS: Corpus = {
  generated: '2026-09-29',
  documents: [
    { title: 'Method and rules', blocks: [{ text: 'Sourcing rule', claims: [], kind: 'method' }] },
    {
      title: 'Germany (DE)',
      iso: 'DE',
      blocks: [
        {
          text: 'Germany — Fundamentals — Population: 83.58 million',
          claims: ['param:DE:population_m'],
          kind: 'fact',
        },
        {
          text: 'Germany — Holdings — Tax: X',
          claims: ['record:DE:tax:register', 'record:DE:tax:operator'],
          kind: 'fact',
        },
      ],
    },
  ],
}

function fakeClient(
  events: StreamEvent[],
  seen: { params?: unknown } = {},
  fail?: unknown,
): AskClient {
  return {
    beta: {
      messages: {
        stream(params) {
          seen.params = params
          return (async function* () {
            if (fail) throw fail
            for (const e of events) yield e
          })()
        },
      },
    },
  }
}

async function read(res: Response): Promise<Record<string, unknown>[]> {
  const text = await res.text()
  return text
    .split('\n\n')
    .filter(Boolean)
    .map(chunk => JSON.parse(chunk.replace(/^data: /, '')) as Record<string, unknown>)
}

const post = (body: unknown) =>
  new Request('http://localhost/api/ask', { method: 'POST', body: JSON.stringify(body) })

afterEach(() => vi.restoreAllMocks())

describe('validate', () => {
  it('rejects a missing, empty or over-long question', () => {
    expect(validate({})).toMatchObject({ ok: false, status: 400 })
    expect(validate({ question: '   ' })).toMatchObject({ ok: false, status: 400 })
    expect(validate({ question: 'x'.repeat(MAX_QUESTION + 1) })).toMatchObject({
      ok: false,
      status: 400,
    })
    expect(validate({ question: ' Who runs the tax register? ' })).toEqual({
      ok: true,
      question: 'Who runs the tax register?',
    })
  })
})

describe('buildRequest', () => {
  it('sends only the corpus, with citations on and the question last', () => {
    const req = buildRequest(CORPUS, 'Q?')
    expect(req.model).toBe(MODEL)
    expect(req.fallbacks).toBe('default')
    const content = req.messages[0]!.content
    expect(content.at(-1)).toEqual({ type: 'text', text: 'Q?' })
    const docs = content.slice(0, -1) as {
      citations: { enabled: boolean }
      cache_control?: unknown
    }[]
    expect(docs).toHaveLength(CORPUS.documents.length)
    expect(docs.every(d => d.citations.enabled)).toBe(true)
    // One cache breakpoint, on the last document, so system + corpus cache as one prefix.
    expect(docs.filter(d => d.cache_control)).toHaveLength(1)
    expect(docs.at(-1)!.cache_control).toBeTruthy()
  })
})

describe('claimsFor', () => {
  it('maps a block range to the claims it covers, without duplicates', () => {
    expect(claimsFor(CORPUS, 1, 0, 2)).toEqual([
      'param:DE:population_m',
      'record:DE:tax:register',
      'record:DE:tax:operator',
    ])
    expect(claimsFor(CORPUS, 9, 0, 1)).toEqual([])
  })
})

describe('handler', () => {
  it('streams text, resolved citations and the stop reason', async () => {
    const handler = createHandler(
      fakeClient([
        {
          type: 'content_block_delta',
          delta: { type: 'text_delta', text: 'Germany has 83.58 million people.' },
        },
        {
          type: 'content_block_delta',
          delta: {
            type: 'citations_delta',
            citation: {
              type: 'content_block_location',
              document_index: 1,
              start_block_index: 0,
              end_block_index: 1,
              cited_text: 'Population: 83.58 million',
            },
          },
        },
        { type: 'message_delta', delta: { type: 'message_delta', stop_reason: 'end_turn' } },
      ]),
      CORPUS,
    )
    const events = await read(await handler(post({ question: 'How many people live in Germany?' })))
    expect(events).toEqual([
      { type: 'text', text: 'Germany has 83.58 million people.' },
      { type: 'cite', claims: ['param:DE:population_m'], cited_text: 'Population: 83.58 million' },
      { type: 'done', stop_reason: 'end_turn' },
    ])
  })

  it('returns 400 before calling the model for an invalid question', async () => {
    const seen: { params?: unknown } = {}
    const res = await createHandler(fakeClient([], seen), CORPUS)(post({ question: '' }))
    expect(res.status).toBe(400)
    expect(seen.params).toBeUndefined()
  })

  it('turns an API error into a message the page can show', async () => {
    const res = await createHandler(
      fakeClient([], {}, { status: 429 }),
      CORPUS,
    )(post({ question: 'Q?' }))
    expect(await read(res)).toEqual([expect.objectContaining({ type: 'error', code: 'busy' })])
  })

  it('never logs the question', async () => {
    const spies = (['log', 'info', 'warn', 'error', 'debug'] as const).map(m =>
      vi.spyOn(console, m).mockImplementation(() => {}),
    )
    const secret = 'my private question about a named person'
    await read(
      await createHandler(
        fakeClient([], {}, new Error('boom')),
        CORPUS,
      )(post({ question: secret })),
    )
    for (const spy of spies) {
      for (const call of spy.mock.calls) expect(JSON.stringify(call)).not.toContain(secret)
    }
  })
})
