import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '@playwright/test'

import type { Bundle } from '../src/data/types'

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

const ROUTES = [
  '/',
  '/countries',
  '/country/DE',
  '/country/NL',
  '/holdings',
  '/holdings/civil_registry',
  '/sources',
  '/sovereignty',
  '/methodology',
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
    await expect(page.locator('#src-1')).toContainText('Eurostat')
  })

  test('a value with no checked source is shown as a gap, not a fact', async ({ page }) => {
    await page.goto('/country/DE')
    await expect(page.getByText('Not yet verified').first()).toBeVisible()
    await expect(page.getByText('Not yet sized').first()).toBeVisible()
  })

  test('countries sort by verified holdings and link to their PDF', async ({ page }) => {
    await page.goto('/countries')
    await expect(page.locator('tbody tr')).toHaveCount(27)
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

test.describe('accessibility', () => {
  for (const route of ROUTES) {
    test(`${route} has no detectable violations`, async ({ page }) => {
      await page.goto(route)
      await expect(page.locator('main')).toBeVisible()
      const results = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
        .analyze()
      expect(results.violations).toEqual([])
    })
  }
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
})
