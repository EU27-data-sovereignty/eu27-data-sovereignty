/**
 * Visual regression (#92): screenshots of the pages a reader sees first, compared with committed
 * baselines. Fonts render slightly differently per operating system, so the baselines are macOS ones and
 * this runs only there, in Chrome; CI (Linux) skips it. Update deliberately after a design change:
 *   npx playwright test e2e/visual.spec.ts --project=chrome --update-snapshots
 */
import { expect, test } from '@playwright/test'

const PAGES = ['/', '/country/DE', '/methodology', '/fact-check/DE']

test.skip(
  ({ browserName }) => browserName !== 'chromium' || process.platform !== 'darwin',
  'baselines are macOS Chrome',
)

// The report previews exist only in a build that also made the PDFs; without them the front page drops
// the thumbnails. Block them so every build renders the same page.
test.beforeEach(async ({ page }) => {
  await page.route('**/previews/**', route => route.abort())
})

for (const scheme of ['light', 'dark'] as const) {
  test.describe(`${scheme} mode`, () => {
    test.use({ colorScheme: scheme })
    for (const route of PAGES) {
      test(`${route} at 1280 px`, async ({ page }) => {
        await page.setViewportSize({ width: 1280, height: 900 })
        await page.goto(route)
        await expect(page.locator('main')).toBeVisible()
        await page.evaluate(() => document.fonts.ready)
        await expect(page).toHaveScreenshot({ maxDiffPixelRatio: 0.01 })
      })
    }
  })
}

for (const route of ['/', '/country/DE']) {
  test(`${route} at 375 px`, async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 812 })
    await page.goto(route)
    await expect(page.locator('main')).toBeVisible()
    await page.evaluate(() => document.fonts.ready)
    await expect(page).toHaveScreenshot({ maxDiffPixelRatio: 0.01 })
  })
}
