import { existsSync } from 'node:fs'

import { defineConfig, devices } from '@playwright/test'

/**
 * Uses a browser already installed on this machine rather than downloading
 * Playwright's own ~400 MB Chromium (see DECISIONS.md #22).
 *
 * channel: 'chrome' is not usable here: it hardcodes /Applications/Google Chrome.app,
 * and this machine has Chrome at /Applications/Chrome.app. Resolving the binary
 * explicitly also lets Brave or Edge stand in.
 */
const CANDIDATES = [
  '/Applications/Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  '/usr/bin/google-chrome',
  '/usr/bin/chromium',
]

const executablePath = process.env.CHROME_PATH ?? CANDIDATES.find(p => existsSync(p))

if (!executablePath) {
  throw new Error(
    'No Chromium-family browser found. Install Chrome, or set CHROME_PATH to its binary.',
  )
}

const AXE = /no detectable violations/

/**
 * Port 4823 rather than Vite's default 4173: another project in this workspace runs a
 * preview server on 4173, and binding against it silently failed once, so the tests
 * ran happily against a completely different application. strictPort makes that a
 * hard error rather than a confusing pass.
 */
export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? 'github' : 'list',
  use: {
    baseURL: 'http://localhost:4823',
    trace: 'on-first-retry',
  },
  /**
   * Chrome is the installed browser (#22). Firefox, Safari's engine and two iPhones (#92) use Playwright's
   * own builds, pinned with @playwright/test (`npx playwright install firefox webkit`; CI installs them).
   * The axe scans run in Chrome only: they test the markup, which every engine is served the same.
   */
  projects: [
    { name: 'chrome', use: { ...devices['Desktop Chrome'], launchOptions: { executablePath } } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] }, grepInvert: AXE },
    { name: 'webkit', use: { ...devices['Desktop Safari'] }, grepInvert: AXE },
    { name: 'iphone-se', use: { ...devices['iPhone SE (3rd gen)'] }, grepInvert: AXE },
    { name: 'iphone-17-pro', use: { ...devices['iPhone 17 Pro'] }, grepInvert: AXE },
  ],
  webServer: {
    command: 'npm run preview -- --port 4823 --strictPort',
    url: 'http://localhost:4823',
    reuseExistingServer: !process.env.CI,
    timeout: 60_000,
  },
})
