import { useEffect, useState } from 'react'

import type { Mode } from './palette'

const KEY = 'eu27-theme'

/**
 * Theme is *selected*, not inferred: an explicit choice stamps data-theme on <html>
 * and wins in both directions. Without one the site is dark, whatever the OS prefers
 * (2026-10-20, the owner's call); index.html starts dark too, so the first paint matches.
 * Chart palettes have separately validated dark steps, so this must be readable
 * synchronously by chart code.
 */
export function useTheme(): [Mode, (m: Mode) => void] {
  const [mode, setMode] = useState<Mode>(() => {
    try {
      const stored = localStorage.getItem(KEY)
      if (stored === 'light' || stored === 'dark') return stored
    } catch {
      // Private browsing and blocked site-data both throw; fall through to the default.
    }
    return 'dark'
  })

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', mode)
    try {
      localStorage.setItem(KEY, mode)
    } catch {
      // Non-fatal: the theme still applies for this page view.
    }
  }, [mode])

  return [mode, setMode]
}
