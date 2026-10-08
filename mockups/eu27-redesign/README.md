# EU27.CLOUD redesign mockup

A static, clickable design mockup of the eu27.cloud web app: the overview and every page in the header
navigation (Ranking, Countries, Critical holdings, Hosting, Sources, Ask, Methodology, Fact check).

It is a design proposal, not part of the build. Nothing here is read by `web/`, the content model or the
deploy, and no fact here is a source of truth: the figures were copied from eu27.cloud and from
`web/public/data/eu27.json` (generated 2026-09-29) when the mockup was made, and will drift from the data.

## View it

Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server -d mockups/eu27-redesign 8000   # then http://localhost:8000
```

Fonts load from Google Fonts, so the type falls back to system faces offline.

## What it shows

- Brand: EU blue `#003399` (Pantone 661 C) and EU gold `#FFCC00` (Pantone 116 C) as highlight and accent
  over the header artwork's night navy `#0a0f1d`; the EU27.CLOUD wordmark and badge; Montserrat headings,
  Inter body, Libertinus Serif for quoted source text; 10px corners.
- Dark mode by default with a light mode, following the system setting, with a sun/moon toggle.
- Overview: a tile map of the 27 member states shaded by verified holdings, Tier 0 or sourced facts.
- Hosting: all 69 rows of the infrastructure table (65 printed, 4 withheld by the fact check).
- Sources: all 1,012 sources and their 1,728 citations, searchable and filterable by country, tier and grade.
- Ask: the composer and suggested questions; answers are placeholders and nothing is sent anywhere.

## Files

| File | What it is |
|---|---|
| `index.html`, `*.html` | One page per navigation item |
| `site.css`, `site.js` | Shared tokens, navigation, footer, theme toggle and per-country figures |
| `hosting-data.js` | The infrastructure table rows |
| `sources-data.js` | Sources and citations, derived from `eu27.json` |
| `badge.png`, `wordmark*.png`, `lockup*.png` | Logo badge and wordmark, light and dark variants |
| `hero-bg.webp` | Header background (EU silhouette) |
| `favicon*`, `apple-touch-icon.png` | Favicon set built from the flag "27" artwork |
