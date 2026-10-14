/**
 * The split edition's two part shapes (#110), and the one view that lets the parity-pinned helpers in
 * `sources.ts` run unchanged: `bundleView(core, part)` is a `Bundle` whose per-state maps hold the one
 * state that is loaded. Nothing is derived here that the single bundle does not hold; `index` is the one
 * addition, counted by `model/export_json.py` with the rules `sources.ts` applies.
 */
import type { Bundle, Citation, CountryData, Document, Source } from './types';

export interface IndexEntry {
  name: string;
  facts: number;
  gaps: number;
  withheld: number;
  holdings_verified: number;
  holdings_total: number;
  tier0_verified: number;
  tier0_total: number;
}

/** eu27.core.json: everything that is not one state's, plus the index of the 27. */
export type CorePart = Omit<Bundle, 'documents' | 'countries' | 'factcheck'> & {
  factcheck: { eu: Document };
  index: Record<string, IndexEntry>;
};

/** eu27.<ISO>.json: one state, self-contained. */
export interface CountryPart {
  schema_version: number;
  generated: string;
  documents: Record<string, Document>;
  countries: Record<string, CountryData>;
  factcheck: { countries: Record<string, Document>; lines: Record<string, string> };
  claims: Record<string, Citation[]>;
  sources: Record<string, Source>;
}

export function bundleView(core: CorePart, part?: CountryPart): Bundle {
  const { index: _index, ...rest } = core;
  return {
    ...rest,
    documents: part?.documents ?? {},
    countries: part?.countries ?? {},
    claims: { ...core.claims, ...(part?.claims ?? {}) },
    sources: { ...core.sources, ...(part?.sources ?? {}) },
    factcheck: {
      eu: core.factcheck.eu,
      countries: part?.factcheck.countries ?? {},
      lines: part?.factcheck.lines ?? {},
    },
  };
}

/** The 27 states in the order the country list shows them: by name. */
export function indexRows(core: CorePart): (IndexEntry & { iso: string })[] {
  return Object.entries(core.index)
    .map(([iso, entry]) => ({ iso, ...entry }))
    .sort((a, b) => a.name.localeCompare(b.name));
}
