/**
 * The edition store against a real bucket (local Supabase), run only by scripts/integration-test.mjs with
 * EDITION_URL set: the same EditionStore as on the device, on an in-memory file store whose downloads go
 * through node's fetch. EDITION_EXPECT says what the bucket holds: an edition to install, or one with an
 * altered part to reject.
 */
import { BUNDLED_MANIFEST, bundledPart } from '../src/data/bundled';
import { EditionStore } from '../src/edition/EditionStore';
import { MemoryFileStore } from '../src/edition/memoryFiles';
import { sha256 } from './support';

const base = process.env.EDITION_URL ?? '';
const expectation = process.env.EDITION_EXPECT ?? 'install';

const fetcher = async (url: string) => {
  const r = await fetch(url);
  return r.ok ? new Uint8Array(await r.arrayBuffer()) : null;
};

(base ? describe : describe.skip)('the edition store against the local bucket', () => {
  it(`${expectation}s the edition latest.json points at`, async () => {
    const files = new MemoryFileStore(fetcher);
    const store = new EditionStore({
      files,
      sha256,
      channel: () => ({
        latestUrl: () => `${base}/latest.json`,
        objectUrl: (e, n) => `${base}/${e}/${n}`,
      }),
      bundled: { manifest: BUNDLED_MANIFEST, part: bundledPart },
    });
    await store.resolve();
    const final = await store.checkForUpdate();
    if (expectation === 'install') {
      expect(final.kind).toBe('ready');
      await store.useInstalled();
      expect(store.active.source).toBe('downloaded');
      expect(store.active.published?.commit).toBe('it-good');
      expect(Object.keys((await store.country('NL')) as object)).toContain('documents');
    } else {
      expect(final).toMatchObject({ kind: 'rejected', name: 'eu27.DE.json' });
      expect(store.active.source).toBe('bundled');
      expect(files.paths().filter((p) => p.startsWith('editions/'))).toEqual([]);
    }
  });
});
