/**
 * The components every page is built from (#92). The content rules are the model's (model/document.py);
 * these check that the renderers keep them: a fact carries its numbered source, a gap and a disputed value
 * never read as a fact, a wide table can be scrolled by keyboard, every page header carries its kicker
 * and a single h1, and the audience selector is real buttons that report their choice (#101).
 */
import { render, renderHook, act, screen, fireEvent } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { describe, expect, it, beforeEach } from 'vitest'

import { AudienceSelector } from '../components/AudienceSelector'
import { DocumentView } from '../components/DocumentView'
import { FIGURES } from '../data/guideFigures'
import { AUDIENCE_GUIDES, TASK_GUIDES } from '../data/guides'
import { PageBand } from '../components/PageBand'
import type { Bundle, Document } from '../data/types'
import { useTheme } from '../utils/theme'

const bundle = {
  claims: { 'record:XX:tax:register': [{ source_id: 's1' }] },
  sources: { s1: { label: 'Tax office' } },
} as unknown as Bundle

const doc: Document = {
  iso: 'XX',
  name: 'Testland',
  sections: [
    {
      id: 'holdings',
      title: 'Holdings',
      blocks: [
        {
          type: 'p',
          spans: [
            { t: 'Tax register', role: 'fact', c: ['record:XX:tax:register'], g: 'Standard' },
            { t: 'Not yet sourced', role: 'gap' },
            {
              t: 'Disputed: the fact check did not confirm this',
              role: 'disputed',
              c: ['record:XX:land:register'],
            },
          ],
        },
        {
          type: 'table',
          columns: [
            { t: 'Holding', role: 'label' },
            { t: 'Register', role: 'label' },
          ],
          align: ['left', 'left'],
          rows: [
            [
              { t: 'Tax', role: 'label' },
              { t: 'Not yet sourced', role: 'gap' },
            ],
          ],
        },
      ],
    },
  ],
} as unknown as Document

describe('DocumentView', () => {
  it('links a fact to its numbered source, and only a fact', () => {
    render(<DocumentView doc={doc} bundle={bundle} numbers={new Map([['s1', 1]])} />)
    const link = screen.getByRole('link', { name: /Source 1: Tax office/ })
    expect(link).toHaveAttribute('href', '#src-1')
    expect(screen.getAllByRole('link')).toHaveLength(1)
  })

  it('sets a gap and a disputed value apart from facts, in italics', () => {
    render(<DocumentView doc={doc} bundle={bundle} numbers={new Map()} />)
    expect(screen.getAllByText('Not yet sourced')[0]?.tagName).toBe('EM')
    expect(screen.getByText(/did not confirm this/).tagName).toBe('EM')
  })

  it('makes a wide table a keyboard-reachable region named by its columns', () => {
    render(<DocumentView doc={doc} bundle={bundle} numbers={new Map()} />)
    const region = screen.getByRole('region', { name: 'Holding, Register' })
    expect(region).toHaveAttribute('tabindex', '0')
  })
})

describe('AudienceSelector', () => {
  const selector = () =>
    render(
      <MemoryRouter>
        <AudienceSelector />
      </MemoryRouter>,
    )
  const links = (name: string) =>
    [...screen.getByRole('navigation', { name }).querySelectorAll('a')].map(a => [
      a.textContent?.replace(/\s+/g, ' ').trim(),
      a.getAttribute('href'),
    ])

  it('opens on "I am…" and switches the toggle with real pressed buttons', () => {
    selector()
    const group = screen.getByRole('group', { name: 'Choose entry by' })
    const [role, need] = [...group.querySelectorAll('button')]
    expect(role).toHaveAttribute('aria-pressed', 'true')
    expect(need).toHaveAttribute('aria-pressed', 'false')
    fireEvent.click(need!)
    expect(role).toHaveAttribute('aria-pressed', 'false')
    expect(need).toHaveAttribute('aria-pressed', 'true')
  })

  it('links each of the six audiences to its guide', () => {
    selector()
    expect(links('Guides by audience')).toEqual([
      ['Ministries & government CIOs', '/for/ministries'],
      ['Procurement & cloud strategy', '/for/procurement'],
      ['Parliaments & audit courts', '/for/parliaments'],
      ['Cyber agencies & CISOs', '/for/cyber'],
      ['EU institutions', '/for/eu-institutions'],
      ['Operators investors & press', '/for/operators'],
    ])
  })

  it('swaps them for six tasks under "I need to…", each linked to its guide', () => {
    selector()
    fireEvent.click(screen.getByRole('button', { name: /I need to/ }))
    expect(links('Guides by task')).toEqual([
      ['Check my country’s exposure', '/how/exposure'],
      ['Decide what to migrate first', '/how/migrate'],
      ['Write tender criteria that hold up', '/how/tender'],
      ['Turn gaps into formal questions', '/how/questions'],
      ['Compare how peers host a register', '/how/compare'],
      ['Plan for a provider cut-off', '/how/cut-off'],
    ])
  })
})

describe('guides', () => {
  it('gives every guide steps, figures that exist, and related guides that exist', () => {
    for (const [guides, others] of [
      [AUDIENCE_GUIDES, TASK_GUIDES],
      [TASK_GUIDES, AUDIENCE_GUIDES],
    ] as const) {
      expect(guides).toHaveLength(6)
      for (const g of guides) {
        expect(g.steps.length, g.slug).toBeGreaterThanOrEqual(3)
        for (const id of g.figures) expect(FIGURES, g.slug).toHaveProperty(id)
        for (const slug of g.related)
          expect(
            others.map(o => o.slug),
            g.slug,
          ).toContain(slug)
      }
    }
  })
})

describe('PageBand', () => {
  it('renders one h1 with its kicker', () => {
    render(<PageBand kicker="EU-27 · Countries" title="Countries" />)
    expect(screen.getAllByRole('heading', { level: 1 })).toHaveLength(1)
    expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('Countries')
    expect(screen.getByText('EU-27 · Countries')).toBeInTheDocument()
  })

  it('uses the method colour for method pages', () => {
    const { container } = render(<PageBand kicker="Method" title="Methodology" tone="method" />)
    expect(container.querySelector('header')?.className).toContain('--color-method-deep')
  })
})

describe('useTheme', () => {
  beforeEach(() => localStorage.clear())

  it('applies and remembers an explicit choice', () => {
    const { result } = renderHook(() => useTheme())
    act(() => result.current[1]('dark'))
    expect(document.documentElement.getAttribute('data-theme')).toBe('dark')
    expect(localStorage.getItem('eu27-theme')).toBe('dark')
  })
})
