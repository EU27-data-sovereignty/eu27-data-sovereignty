/**
 * The shape of `public/data/eu27.json`, schema version 2 (DECISIONS.md #74, #75).
 *
 * Written by `model/export_json.py`. The app renders `documents` -- the one content model the
 * PDFs and the markdown briefs also render -- and looks every footnote up in `claims` and
 * `sources`. It derives no fact of its own. There is no capacity here: it is withdrawn until a
 * country is sized from its own measured holdings (#73).
 */

/** label: heading or row name. method: this project's reasoning. fact: cited. gap: withheld. */
export type Role = 'label' | 'method' | 'fact' | 'gap' | 'disputed'

export interface Span {
  t: string
  role: Role
  /** Claim ids; present on facts only. */
  c?: string[]
  /** The best evidence grade among the fact's citations. */
  g?: Grade
  /** 'categorical' for a closed-vocabulary value admitted by review. */
  k?: 'categorical'
}

export type Block =
  | { type: 'p'; spans: Span[] }
  | { type: 'callout'; tone: 'method' | 'notice' | 'gap'; spans: Span[] }
  | { type: 'list'; items: Span[][] }
  | { type: 'table'; columns: Span[]; align?: ('left' | 'right')[]; rows: Span[][] }

export interface Section {
  id: string
  title: string
  blocks: Block[]
}

export interface Document {
  iso: string
  name: string
  sections: Section[]
}

export type Grade = 'Verified' | 'Strong' | 'Standard'

export interface Citation {
  source_id: string
  locator: string
  quote: string
  value_as_found: string
  confidence: string
  retrieved: string
  checked_by: string
  /** Computed by model/evidence.py from the checks; never set by hand (#82). */
  grade: Grade
  checks: Record<string, unknown>
  /** The quote in its original language, and the machine translation apart from it. */
  original: string
  gloss: string
  checklist: string[]
}

export interface Source {
  source_id: string
  label: string
  title: string
  publisher: string
  url: string
  archived_url: string
  published: string
  doc_type: string
  language: string
  notes: string
}

/** One holding class in one country, as national_data.for_country() returns it. */
export interface HoldingEntry {
  tier: number
  record_class: string
  label: string
  domain: string
  recoverability: string
  status: 'held' | 'not_held' | 'unrecorded'
  register: string
  holder: string
  holder_url: string
  legal_basis: string
  hosting: string
  foreign_dependency: string
  record_count: string
  data_size: string
  url: string
  publisher: string
  retrieved: string
  confidence: string
  quote: string
}

export interface CountryData {
  iso2: string
  name: string
  params: Record<string, string>
  national_data: HoldingEntry[]
}

export interface HoldingClass {
  class_id: string
  label: string
  tier: number
  domain: string
}

export type GroupId =
  'law_and_practice' | 'practice_only' | 'law_only' | 'not_demonstrated' | 'dependent'

/** One state's placement (#77). Ids and labels only: there is no score to quote. */
export interface Placement {
  group: GroupId
  /** The groups this state could still reach, best to worst. */
  range: GroupId[]
  confidence: 'High' | 'Medium' | 'Low'
  could_move: { input: string; if: string; group: GroupId; count?: number }[]
  indicators: Record<string, 'yes' | 'partial' | 'no' | 'unknown'>
}

export interface Sovereignty {
  groups: { id: GroupId; label: string }[]
  guardrail: string
  indicators: { id: string; dimension: string; label: string; question: string }[]
  placements: Record<string, Placement>
}

/** What the project can honestly say about its evidence (model/evidence.py). */
export interface Notice {
  disclaimer: string
  withheld: string
  grade_rule: string
  checks: { name: string; what: string }[]
}

export interface Bundle {
  schema_version: number
  generated: string
  provenance: string
  notice: Notice
  national_data_note: string
  priority_rule: string
  sovereignty: Sovereignty
  holding_classes: HoldingClass[]
  countries: Record<string, CountryData>
  documents: Record<string, Document>
  /** URL templates for checking a fact ({claim}) or submitting a source ({iso}) (#85). */
  contribute: { review: string; submit: string }
  /** How everything was sourced and calculated, generated (model/methodology.py). */
  methodology: Document
  claims: Record<string, Citation[]>
  sources: Record<string, Source>
}
