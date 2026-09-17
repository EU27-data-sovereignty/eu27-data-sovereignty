/**
 * Warm Neutral + Terracotta, ported from `web/src/styles/index.css`.
 *
 * The web app defines these as CSS custom properties in an `@theme` block; React Native has
 * no cascade, so the same tokens are plain objects here. The raw -> semantic split is kept:
 * raw hexes are named once, everything downstream refers to a role (`fgSecondary`), never to
 * a colour name, so swapping palettes touches one block.
 *
 * Dark mode is re-derived rather than inverted, exactly as on the web — see the note on
 * `fgMuted`, which the design system lists as #898781 and which measures 3.21:1 on the light
 * page: fine for axis ticks, failing AA as body text, so it is darkened.
 */

const raw = {
  ivory: '#f5f2e9',
  cloud: '#faf9f5',
  clay: '#d97757',
  clayDark: '#a8462b',
  slate: '#262625',
  sage: '#b5b2a4',
  rule: '#e3ded0',
} as const;

export interface Theme {
  bgPage: string;
  bgCard: string;
  bgEmphasis: string;
  fgPrimary: string;
  fgSecondary: string;
  fgMuted: string;
  border: string;
  accent: string;
  accentText: string;
}

export const light: Theme = {
  bgPage: raw.ivory,
  bgCard: raw.cloud,
  bgEmphasis: '#f7e9e3',
  fgPrimary: raw.slate,
  fgSecondary: '#6b6a63',
  fgMuted: '#6f6d66',
  border: raw.rule,
  accent: raw.clay,
  accentText: raw.clayDark,
};

export const dark: Theme = {
  bgPage: '#0d0d0d',
  bgCard: '#1a1a19',
  bgEmphasis: '#2a1a13',
  fgPrimary: '#ffffff',
  fgSecondary: '#c3c2b7',
  fgMuted: '#898781',
  border: '#3a3a38',
  accent: raw.clay,
  accentText: '#e8a58b',
};

/** Type scale, matching `--text-axis`, `--text-body` and `--text-stat`. */
export const Text = {
  axis: 11,
  body: 14,
  stat: 30,
  title: 22,
  heading: 17,
} as const;

/**
 * `useColorScheme()` returns 'unspecified' as well as 'light', 'dark' and null, so the parameter
 * is deliberately wider than the two themes: anything that is not dark renders light.
 */
export const themeFor = (scheme: string | null | undefined): Theme =>
  scheme === 'dark' ? dark : light;
