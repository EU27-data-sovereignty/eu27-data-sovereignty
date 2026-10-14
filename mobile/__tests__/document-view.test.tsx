/**
 * The renderer adds nothing (#75): the text on screen, minus the [n] source marks, is exactly the spans'
 * text; sources are numbered in first-citation order; a gap and a disputed value are set apart; every
 * table cell is drawn.
 */
import { render, screen } from '@testing-library/react-native';

import { DocumentView, SpanView } from '../src/components/DocumentView';
import { numberSources, spans } from '../src/data/sources';
import type { Bundle, Document } from '../src/data/types';

jest.mock('expo-router', () => {
  const { Text } = require('react-native');
  return { Link: ({ children }: { children: React.ReactNode }) => <Text>{children}</Text> };
});

const doc: Document = {
  iso: 'XX',
  name: 'Testland',
  sections: [
    {
      id: 'one',
      title: 'First section',
      blocks: [
        {
          type: 'p',
          spans: [
            { t: 'Population', role: 'label' },
            { t: '1,000', role: 'fact', c: ['param:XX:pop'], g: 'Standard' },
          ],
        },
        { type: 'callout', tone: 'method', spans: [{ t: 'Our reasoning.', role: 'method' }] },
        {
          type: 'list',
          items: [
            [{ t: 'Not yet sourced', role: 'gap' }],
            [{ t: 'Disputed: source gone', role: 'disputed', c: ['param:XX:gdp'] }],
          ],
        },
        {
          type: 'table',
          columns: [
            { t: 'Holding', role: 'label' },
            { t: 'Operator', role: 'label' },
          ],
          rows: [
            [
              { t: 'Civil registry', role: 'label' },
              { t: 'The Agency', role: 'fact', c: ['record:XX:civil:operator'], g: 'Strong' },
            ],
          ],
        },
      ],
    },
  ],
};

const cite = (source_id: string) => ({
  source_id,
  locator: 'p. 1',
  quote: 'q',
  value_as_found: 'v',
  confidence: 'official',
  retrieved: '2026-10-01',
  checked_by: 'x',
  grade: 'Standard' as const,
  checks: {},
  original: 'q',
  gloss: '',
  checklist: [],
});

const bundle = {
  claims: {
    'param:XX:pop': [cite('src-b')],
    'record:XX:civil:operator': [cite('src-a'), cite('src-b')],
  },
  sources: { 'src-a': { label: 'Source A' }, 'src-b': { label: 'Source B' } },
} as unknown as Bundle;

const text = (nodes: ReturnType<typeof screen.getAllByText>) => nodes.map((n) => n.props.children);

describe('DocumentView', () => {
  it('renders every span and nothing else', async () => {
    const numbers = numberSources([doc], bundle);
    await render(<DocumentView doc={doc} bundle={bundle} numbers={numbers} />);
    const want = [...spans(doc)].map((s) => s.t);
    for (const t of want)
      expect(screen.getAllByText(t, { exact: false }).length).toBeGreaterThan(0);
    expect(screen.getByText('First section')).toBeTruthy();
  });

  it('numbers sources in first-citation order', () => {
    const numbers = numberSources([doc], bundle);
    expect([...numbers.entries()]).toEqual([
      ['src-b', 1],
      ['src-a', 2],
    ]);
  });

  it('marks a fact with its source numbers and lets a reader jump to them', async () => {
    const numbers = numberSources([doc], bundle);
    const onSource = jest.fn();
    await render(<DocumentView doc={doc} bundle={bundle} numbers={numbers} onSource={onSource} />);
    const mark = screen.getByLabelText('Source 1: Source B. Evidence: Standard');
    expect(text([mark]).flat().join('')).toContain('[1]');
    mark.props.onPress();
    expect(onSource).toHaveBeenCalledWith('src-b');
  });

  it('sets a gap and a disputed value apart from a fact', async () => {
    await render(
      <>
        <SpanView
          span={{ t: 'Not yet sourced', role: 'gap' }}
          numbers={new Map()}
          bundle={bundle}
        />
        <SpanView
          span={{ t: 'Disputed: x', role: 'disputed', c: [] }}
          numbers={new Map()}
          bundle={bundle}
        />
      </>
    );
    const flat = (s: unknown): Record<string, unknown> =>
      Object.assign({}, ...(Array.isArray(s) ? s.flat(Infinity) : [s]).filter(Boolean));
    expect(flat(screen.getByText('Not yet sourced').props.style).fontStyle).toBe('italic');
    expect(flat(screen.getByText('Disputed: x').props.style).textDecorationStyle).toBe('dashed');
  });

  it('draws every table cell as a card line', async () => {
    await render(<DocumentView doc={doc} bundle={bundle} numbers={numberSources([doc], bundle)} />);
    expect(screen.getByText('Civil registry')).toBeTruthy();
    expect(screen.getByText('Operator')).toBeTruthy();
    expect(screen.getByText('The Agency', { exact: false })).toBeTruthy();
  });
});
