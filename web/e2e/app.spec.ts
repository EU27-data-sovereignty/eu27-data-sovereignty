import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '@playwright/test'

import type { Bundle, Span } from '../src/data/types'

/**
 * These assert that routes render REAL DATA, not that they merely load.
 *
 * The app is client-rendered, so the failure that matters is a page that returns 200 and shows
 * a loading message forever. Every expectation is READ FROM the bundle the app serves, never
 * typed in: hardcoded figures once drifted from the model and the gate stayed red for a week.
 */
const HERE = path.dirname(fileURLToPath(import.meta.url))
const BUNDLE = JSON.parse(
  fs.readFileSync(path.resolve(HERE, '../public/data/eu27.json'), 'utf8'),
) as Bundle

/** The first sourced fact in a country's fundamentals table, as the page shows it. */
function firstFact(iso: string): string {
  const doc = BUNDLE.documents[iso]
  const table = doc?.sections
    .find(s => s.id === 'fundamentals')
    ?.blocks.find(b => b.type === 'table')
  if (!table || table.type !== 'table') throw new Error(`no fundamentals table for ${iso}`)
  const fact = table.rows.map(r => r[1]).find(s => s?.role === 'fact')
  if (!fact) throw new Error(`no sourced fundamental for ${iso}`)
  return fact.t
}

/** The title of the first source a country page cites, in reading order. */
function firstSourceTitle(iso: string): string {
  const doc = BUNDLE.documents[iso]!
  for (const s of doc.sections)
    for (const b of s.blocks) {
      const spans =
        b.type === 'table' ? b.rows.flat() : b.type === 'list' ? b.items.flat() : b.spans
      for (const sp of spans)
        for (const claim of sp.c ?? []) {
          const cite = BUNDLE.claims[claim]?.[0]
          if (cite) return BUNDLE.sources[cite.source_id]!.title
        }
    }
  throw new Error(`no cited source on ${iso}`)
}

const ROUTES = [
  '/',
  '/countries',
  '/country/DE',
  '/country/NL',
  '/holdings',
  '/holdings/civil_registry',
  '/infrastructure',
  '/sources',
  '/sovereignty',
  '/ask',
  '/methodology',
  '/fact-check',
  '/fact-check/DE',
]

test.describe('data actually renders', () => {
  test('overview reports the state of the evidence from the bundle', async ({ page }) => {
    await page.goto('/')
    const sources = Object.keys(BUNDLE.sources).length
    await expect(page.getByText(`from ${sources} checked sources`)).toBeVisible()
    await expect(page.getByRole('link', { name: /EU-27 report \(PDF\)/ })).toBeVisible()
  })

  test('a country page shows a sourced fact with a footnote that lands on its source', async ({
    page,
  }) => {
    await page.goto('/country/DE')
    await expect(page.getByRole('heading', { name: 'Germany', level: 1 })).toBeVisible()
    const fact = firstFact('DE')
    await expect(page.getByText(fact).first()).toBeVisible()
    await page
      .getByRole('link', { name: /^Source 1:/ })
      .first()
      .click()
    await expect(page.locator('#src-1')).toBeVisible()
    // Source 1 is whatever the page cites first: derived from the bundle, never assumed.
    await expect(page.locator('#src-1')).toContainText(firstSourceTitle('DE'))
  })

  test('a value with no checked source is shown as a gap, not a fact', async ({ page }) => {
    await page.goto('/country/DE')
    await expect(page.locator('main').getByText('Not yet verified').first()).toBeVisible()
    await expect(page.locator('main').getByText('Not yet sized').first()).toBeVisible()
  })

  test('countries sort by verified holdings and link to their PDF', async ({ page }) => {
    await page.goto('/countries')
    await expect(
      page.getByRole('list', { name: 'Member states' }).getByRole('listitem'),
    ).toHaveCount(27)
    await page.getByRole('button', { name: /Holdings verified/ }).click()
    await expect(page.getByRole('link', { name: 'PDF' }).first()).toHaveAttribute(
      'href',
      /\/report\/[A-Z]{2}\.pdf$/,
    )
  })

  test('one holding class compares all 27 states', async ({ page }) => {
    await page.goto('/holdings/civil_registry')
    await expect(page.getByRole('heading', { name: 'Civil registry core' })).toBeVisible()
    await expect(page.locator('tbody tr')).toHaveCount(27)
  })

  test('the sources page lists every source in the bundle', async ({ page }) => {
    await page.goto('/sources')
    await expect(page.locator('#sources li[id^="src-"]')).toHaveCount(
      Object.keys(BUNDLE.sources).length,
    )
  })
})

/** Every span of a document, in reading order. */
function docSpans(iso: string): Span[] {
  const out: Span[] = []
  for (const s of BUNDLE.documents[iso]!.sections)
    for (const b of s.blocks)
      out.push(
        ...(b.type === 'table' ? b.rows.flat() : b.type === 'list' ? b.items.flat() : b.spans),
      )
  return out
}

test.describe('evidence rules (#82, #83)', () => {
  test('every page says the findings are machine-checked, not human-verified', async ({ page }) => {
    await page.goto('/country/DE')
    // The notice heads the footer of every page, in full at every width.
    await expect(
      page.locator('footer').getByText(BUNDLE.provenance, { exact: false }),
    ).toBeVisible()
    for (const route of ['/', '/methodology']) {
      await page.goto(route)
      // exact: the footer notice on every page also contains the disclaimer, inside longer text; this
      // checks the page's own statement of it.
      await expect(page.getByText(BUNDLE.notice.disclaimer, { exact: true })).toBeVisible()
    }
  })

  test('every page links the fact check, and a country lists the verdict on each of its facts (#87)', async ({
    page,
  }) => {
    await page.goto('/country/DE')
    // Web fonts swap in after the data renders and reflow the page; tap once they have settled.
    await page.evaluate(() => document.fonts.ready)
    await page.getByRole('link', { name: 'fact check for Germany' }).click()
    await expect(page).toHaveURL(/\/fact-check\/DE$/)
    await expect(
      page.getByRole('heading', { name: 'Fact check: Germany', exact: true }),
    ).toBeVisible()
    const table = BUNDLE.factcheck.countries
      .DE!.sections.find(s => s.id === 'f-facts')!
      .blocks.find(b => b.type === 'table')
    if (table?.type !== 'table') throw new Error('no verdict table for DE')
    const rows = table.rows
    await expect(page.getByText(rows[0]![0]!.t, { exact: true })).toBeVisible()
    await page.goto('/')
    await page.evaluate(() => document.fonts.ready)
    await page.getByRole('link', { name: 'How every fact was checked' }).click()
    await expect(page).toHaveURL(/\/fact-check$/)
    await expect(page.getByText('not by a person', { exact: false }).first()).toBeVisible()
  })

  test('a fact carries its evidence grade, and its source lists the checks behind it', async ({
    page,
  }) => {
    const fact = docSpans('DE').find(sp => sp.role === 'fact')!
    const cite = BUNDLE.claims[fact.c![0]!]![0]!
    await page.goto('/country/DE')
    await expect(
      page.getByRole('link', { name: new RegExp(`Evidence: ${fact.g}$`) }).first(),
    ).toBeVisible()
    // Source 1 is the first fact's first source: its entry shows that claim's grade and checks, each as
    // its own chip (#99 layout).
    const entry = page.locator('#src-1')
    await expect(entry.getByText(cite.grade, { exact: true }).first()).toBeVisible()
    await expect(entry).toContainText(cite.checklist[0]!)
  })

  test('a non-English quote is shown in the original, with the translation labelled', async ({
    page,
  }) => {
    const iso = Object.keys(BUNDLE.documents).find(i =>
      docSpans(i).some(sp => sp.c?.some(c => BUNDLE.claims[c]?.some(x => x.gloss))),
    )!
    await page.goto(`/country/${iso}`)
    await expect(page.getByText('Machine translation:').first()).toBeVisible()
  })

  test('a disputed value is withheld, stated as disputed, and carries no footnote', async ({
    page,
  }) => {
    // Injected, so the test does not depend on the live data holding a dispute today.
    const DISPUTE = 'Disputed: sources disagree (injected by the test)'
    const bundle = structuredClone(BUNDLE)
    const holdings = bundle.documents.DE!.sections.find(s => s.id === 'holdings')!
    const table = holdings.blocks.find(b => b.type === 'table')!
    if (table.type !== 'table') throw new Error('no holdings table')
    const row = table.rows.find(r => r.some(sp => sp.role === 'fact'))!
    const i = row.findIndex(sp => sp.role === 'fact')
    const original = row[i]!.t
    row[i] = { t: DISPUTE, role: 'disputed', c: row[i]!.c }
    await page.route('**/data/eu27.json', route => route.fulfill({ json: bundle }))
    await page.goto('/country/DE')
    const cell = page.locator('td, th').filter({ hasText: DISPUTE })
    await expect(cell).toBeVisible()
    await expect(cell).not.toContainText(original)
    await expect(cell.locator('a')).toHaveCount(0)
  })
})

test.describe('contributing (#85)', () => {
  test('every fact has a prefilled "Check this fact" link to the review form', async ({ page }) => {
    const fact = docSpans('DE').find(sp => sp.role === 'fact')!
    const claim = fact.c![0]!
    await page.goto('/country/DE')
    const link = page.locator('#src-1').getByRole('link', { name: 'Check this fact' }).first()
    await expect(link).toBeVisible()
    const href = await link.getAttribute('href')
    expect(href).toContain('template=review-fact.yml')
    // Source 1 is the first fact's source, so its first check link is that claim's.
    expect(decodeURIComponent(href!)).toContain(`claim=${claim}`)
  })

  test('a country page invites a source for its withheld values', async ({ page }) => {
    await page.goto('/country/LU')
    const link = page.getByRole('link', { name: 'Submit a source' })
    await expect(link).toHaveAttribute('href', /template=submit-source\.yml.*country=LU/)
  })

  test('the methodology reports human review in numbers', async ({ page }) => {
    await page.goto('/methodology')
    await expect(page.getByRole('heading', { name: 'Citizens and human review' })).toBeVisible()
    await expect(page.getByText('Facts verified by a person')).toBeVisible()
  })
})

test.describe('ranking', () => {
  test('every state appears once in the groups, with its confidence', async ({ page }) => {
    await page.goto('/sovereignty')
    const groups = page.getByRole('region', { name: 'Groups' })
    await expect(groups.getByRole('button')).toHaveCount(27)
    const first = Object.entries(BUNDLE.sovereignty.placements)[0]!
    await expect(
      groups.getByRole('button', { name: new RegExp(BUNDLE.documents[first[0]]!.name) }),
    ).toContainText(first[1].confidence)
  })

  test('the map renders one shape per state and selecting one explains it', async ({ page }) => {
    await page.goto('/sovereignty')
    const map = page.getByRole('group', { name: /Map of the EU-27/ })
    await expect(map.getByRole('button')).toHaveCount(27)
    await map.getByRole('button', { name: /^Estonia:/ }).click()
    await expect(page.getByRole('heading', { name: 'Estonia', level: 2 })).toBeVisible()
    await expect(page.getByText('What could move it')).toBeVisible()
  })

  test('filtering by confidence keeps only matching states', async ({ page }) => {
    await page.goto('/sovereignty')
    await page.getByRole('button', { name: 'High', exact: true }).click()
    const high = Object.values(BUNDLE.sovereignty.placements).filter(p => p.confidence === 'High')
    await expect(page.getByRole('region', { name: 'Groups' }).getByRole('button')).toHaveCount(
      high.length,
    )
  })
})

test.describe('ask', () => {
  /** A recorded answer stream, so CI never calls the API. The cited claim is a real one. */
  const claim = Object.keys(BUNDLE.claims)[0]!
  const stream = [
    { type: 'text', text: 'According to the sourced data, the figure is recorded.' },
    { type: 'cite', claims: [claim], cited_text: 'recorded' },
    { type: 'done', stop_reason: 'end_turn' },
  ]
    .map(e => `data: ${JSON.stringify(e)}\n\n`)
    .join('')

  test('an answer streams in with a citation that opens its source', async ({ page }) => {
    await page.route('**/api/ask', route =>
      route.fulfill({ status: 200, contentType: 'text/event-stream', body: stream }),
    )
    await page.goto('/ask')
    await page.getByRole('button', { name: /How does the data-sovereignty ranking work/ }).click()
    await expect(page.getByLabel('Your question')).toHaveValue(/ranking work/)
    await page.getByRole('button', { name: 'Ask', exact: true }).click()
    await expect(page.getByText('According to the sourced data')).toBeVisible()
    await page.getByRole('link', { name: 'Source 1' }).click()
    await expect(page.locator('#src-1')).toContainText(claim)
  })

  test('a rate-limited request shows a clear message', async ({ page }) => {
    await page.route('**/api/ask', route => route.fulfill({ status: 429, body: '{}' }))
    await page.goto('/ask')
    await page.getByLabel('Your question').fill('Who runs the tax register?')
    await page.getByRole('button', { name: 'Ask', exact: true }).click()
    await expect(page.getByText(/Too many questions/)).toBeVisible()
  })

  test('the question is capped at 500 characters', async ({ page }) => {
    await page.goto('/ask')
    await page.getByLabel('Your question').fill('x'.repeat(600))
    await expect(page.getByLabel('Your question')).toHaveValue('x'.repeat(500))
  })
})

test.describe('accessibility', () => {
  for (const route of ROUTES) {
    test(`${route} has no detectable violations`, async ({ page }) => {
      // /sources lists every claim with its checks and a "Check this fact" link (1,390 claims on
      // 2026-10-01); a full axe scan of it takes longer than the default 30 s.
      if (route === '/sources') test.setTimeout(120_000)
      await page.goto(route)
      await expect(page.locator('main')).toBeVisible()
      const results = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
        .analyze()
      expect(results.violations).toEqual([])
    })
  }
})

test.describe('accessibility in dark mode (#92)', () => {
  test.use({ colorScheme: 'dark' })
  // /sources is left out here only for time; its markup is the same in both themes.
  for (const route of ROUTES.filter(r => r !== '/sources')) {
    test(`${route} has no detectable violations in dark mode`, async ({ page }) => {
      await page.goto(route)
      await expect(page.locator('main')).toBeVisible()
      expect(await page.evaluate(() => matchMedia('(prefers-color-scheme: dark)').matches)).toBe(
        true,
      )
      const results = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
        .analyze()
      expect(results.violations).toEqual([])
    })
  }
})

test.describe('print (#92)', () => {
  test('printing a country page drops the navigation and keeps the findings', async ({ page }) => {
    await page.goto('/country/DE')
    await page.emulateMedia({ media: 'print' })
    await expect(page.getByRole('navigation', { name: 'Main' })).toBeHidden()
    await expect(page.getByRole('heading', { name: 'Germany', exact: true })).toBeVisible()
    await expect(page.locator('tbody tr').first()).toBeVisible()
  })
})

test.describe('responsive', () => {
  test('the holdings table does not force the page to scroll sideways at 375px', async ({
    page,
  }) => {
    await page.setViewportSize({ width: 375, height: 800 })
    await page.goto('/country/DE')
    await expect(page.locator('tbody tr').first()).toBeVisible()
    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
    )
    expect(overflow).toBeLessThanOrEqual(1)
  })

  for (const route of ROUTES.filter(r => r !== '/sources')) {
    test(`${route} does not scroll sideways at 375px (#92)`, async ({ page }) => {
      await page.setViewportSize({ width: 375, height: 800 })
      await page.goto(route)
      await expect(page.locator('main')).toBeVisible()
      const overflow = await page.evaluate(
        () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
      )
      expect(overflow).toBeLessThanOrEqual(1)
    })
  }
})
