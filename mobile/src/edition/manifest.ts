/**
 * The edition: what `model/export_json.py --split` writes and `model/edition.py` publishes (#110, #111).
 *
 * A manifest names the sha256 of every part and of the single bundle (the edition id). latest.json, the one
 * mutable object in the bucket, names the edition the deploy last published. Nothing here trusts a shape it
 * has not checked: a malformed pointer or manifest is `null`, and null is never rendered.
 */

export const SCHEMA_VERSION = 2;
export const CORE_PART = 'eu27.core.json';
export const MANIFEST = 'manifest.json';
export const LATEST = 'latest.json';
export const PUBLISHED = 'published.json';

export interface PartEntry {
  sha256: string;
  bytes: number;
}

export interface Manifest {
  schema_version: number;
  generated: string;
  edition: string;
  parts: Record<string, PartEntry>;
}

export interface Latest {
  edition: string;
  manifest_sha256: string;
  generated: string;
  commit: string;
  published_at: string;
}

export interface Published {
  commit: string;
  run_id: string;
  run_url: string;
  published_at: string;
  manifest_sha256: string;
}

export const isHex64 = (v: unknown): v is string =>
  typeof v === 'string' && /^[0-9a-f]{64}$/.test(v);

const isRecord = (v: unknown): v is Record<string, unknown> =>
  typeof v === 'object' && v !== null && !Array.isArray(v);

export const partName = (iso: string) => `eu27.${iso}.json`;

/** A manifest with the schema this app renders, every part a 64-hex hash and a size; else null. */
export function parseManifest(json: unknown): Manifest | null {
  if (!isRecord(json) || json.schema_version !== SCHEMA_VERSION) return null;
  if (!isHex64(json.edition) || typeof json.generated !== 'string' || !isRecord(json.parts))
    return null;
  const parts: Record<string, PartEntry> = {};
  for (const [name, entry] of Object.entries(json.parts)) {
    if (!/^eu27\.[A-Za-z]+\.json$/.test(name) || !isRecord(entry)) return null;
    if (!isHex64(entry.sha256) || typeof entry.bytes !== 'number' || entry.bytes <= 0) return null;
    parts[name] = { sha256: entry.sha256, bytes: entry.bytes };
  }
  if (!(CORE_PART in parts)) return null;
  return {
    schema_version: SCHEMA_VERSION,
    generated: json.generated,
    edition: json.edition,
    parts,
  };
}

/** The pointer the deploy writes; anything else, including a future schema, is ignored. */
export function parseLatest(json: unknown): Latest | null {
  if (!isRecord(json) || !isHex64(json.edition) || !isHex64(json.manifest_sha256)) return null;
  if (typeof json.generated !== 'string' || typeof json.published_at !== 'string') return null;
  return {
    edition: json.edition,
    manifest_sha256: json.manifest_sha256,
    generated: json.generated,
    commit: typeof json.commit === 'string' ? json.commit : '',
    published_at: json.published_at,
  };
}

export function parsePublished(json: unknown): Published | null {
  if (!isRecord(json) || !isHex64(json.manifest_sha256)) return null;
  const str = (k: string) => (typeof json[k] === 'string' ? (json[k] as string) : '');
  return {
    commit: str('commit'),
    run_id: str('run_id'),
    run_url: str('run_url'),
    published_at: str('published_at'),
    manifest_sha256: json.manifest_sha256,
  };
}
