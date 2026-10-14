/**
 * What every suite shares: a SHA-256 on node:crypto, the edition inside the binary, an EditionStore on an
 * in-memory file store with a channel a test can stock, and a render through the real EditionProvider.
 */
import { render, type RenderResult } from '@testing-library/react-native';
import { createHash } from 'node:crypto';
import type { ReactElement } from 'react';

import { BUNDLED_MANIFEST, bundledPart } from '../src/data/bundled';
import { EditionProvider } from '../src/edition/EditionContext';
import { EditionStore } from '../src/edition/EditionStore';
import { MemoryFileStore, type Fetcher } from '../src/edition/memoryFiles';
import { type Manifest } from '../src/edition/manifest';
import { utf8Encode } from '../src/edition/utf8';
import type { Channel } from '../src/services/channel';

export const sha256 = async (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex');
export const sha256Sync = (bytes: Uint8Array) => createHash('sha256').update(bytes).digest('hex');

export const BASE = 'https://channel.test/storage/v1/object/public/editions';

/** A channel whose URLs are plain, so a fetcher map can serve them. */
export const testChannel: Channel = {
  latestUrl: () => `${BASE}/latest.json`,
  objectUrl: (edition, name) => `${BASE}/${edition}/${name}`,
};

/** An edition in memory: parts as bytes, a manifest that names them, and the id of the bundle they came from. */
export function makeEdition(parts: Record<string, unknown>, bundleBytes: Uint8Array) {
  const files: Record<string, Uint8Array> = {};
  for (const [name, value] of Object.entries(parts))
    files[name] = utf8Encode(JSON.stringify(value));
  const manifest: Manifest = {
    schema_version: 2,
    generated: '2026-10-15',
    edition: sha256Sync(bundleBytes),
    parts: Object.fromEntries(
      Object.entries(files).map(([name, bytes]) => [
        name,
        { sha256: sha256Sync(bytes), bytes: bytes.length },
      ])
    ),
  };
  files['manifest.json'] = utf8Encode(JSON.stringify(manifest));
  return { manifest, files };
}

/** Serve an edition from the channel: latest.json plus every object under its id. */
export function serve(
  edition: ReturnType<typeof makeEdition>,
  extra: Record<string, Uint8Array> = {}
): Record<string, Uint8Array> {
  const id = edition.manifest.edition;
  const latest = {
    edition: id,
    manifest_sha256: sha256Sync(edition.files['manifest.json']!),
    generated: edition.manifest.generated,
    commit: 'abc1234',
    published_at: '2026-10-15T10:00:00+00:00',
  };
  const objects: Record<string, Uint8Array> = {
    [`${BASE}/latest.json`]: utf8Encode(JSON.stringify(latest)),
  };
  for (const [name, bytes] of Object.entries(edition.files))
    objects[`${BASE}/${id}/${name}`] = bytes;
  return { ...objects, ...extra };
}

export const fetcherFor =
  (objects: Record<string, Uint8Array>): Fetcher =>
  async (url) =>
    objects[url] ?? null;

export function makeStore(
  options: {
    objects?: Record<string, Uint8Array>;
    configured?: boolean;
    files?: MemoryFileStore;
  } = {}
) {
  const files = options.files ?? new MemoryFileStore(fetcherFor(options.objects ?? {}));
  const store = new EditionStore({
    files,
    sha256,
    channel: () => (options.configured === false ? null : testChannel),
    bundled: { manifest: BUNDLED_MANIFEST, part: bundledPart },
  });
  return { store, files };
}

export async function renderWithEdition(
  ui: ReactElement,
  store = makeStore({ configured: false }).store
): Promise<RenderResult> {
  return render(<EditionProvider store={store}>{ui}</EditionProvider>);
}
