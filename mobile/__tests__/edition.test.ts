/**
 * The edition store (#110, #111): what it renders, what it accepts from the channel, and what it refuses.
 * Every case runs the real store on an in-memory file store with a channel the test stocks, so the device
 * runs exactly this logic.
 */
import { CORE_PART, LATEST, parseLatest, parseManifest } from '../src/edition/manifest';
import { utf8Encode } from '../src/edition/utf8';
import { BASE, fetcherFor, makeEdition, makeStore, serve, sha256Sync } from './support';
import { MemoryFileStore } from '../src/edition/memoryFiles';
import { BUNDLED_MANIFEST } from '../src/data/bundled';

const core = {
  schema_version: 2,
  generated: '2026-10-15',
  index: { NL: { name: 'Netherlands' } },
  notice: {},
};
const nl = {
  schema_version: 2,
  generated: '2026-10-15',
  documents: { NL: { iso: 'NL', name: 'Netherlands', sections: [] } },
};
const newer = () =>
  makeEdition({ [CORE_PART]: core, 'eu27.NL.json': nl }, utf8Encode('a newer bundle'));

describe('unconfigured', () => {
  it('renders the bundled edition and makes no request', async () => {
    const { store, files } = makeStore({ configured: false });
    await store.resolve();
    expect(store.active.source).toBe('bundled');
    expect(store.active.id).toBe(BUNDLED_MANIFEST.edition);
    expect((await store.core()).schema_version).toBe(2);
    expect(Object.keys((await store.country('DE')).documents)).toEqual(['DE']);
    expect(await store.checkForUpdate()).toEqual({ kind: 'unconfigured' });
    expect(files.requests).toEqual([]);
  });
});

describe('checking the channel', () => {
  it('is up to date when latest.json names the bundled edition', async () => {
    const latest = {
      edition: BUNDLED_MANIFEST.edition,
      manifest_sha256: 'a'.repeat(64),
      generated: 'x',
      published_at: 'y',
    };
    const { store, files } = makeStore({
      objects: { [`${BASE}/latest.json`]: utf8Encode(JSON.stringify(latest)) },
    });
    await store.resolve();
    expect(await store.checkForUpdate()).toEqual({ kind: 'up-to-date' });
    expect(files.requests).toEqual([`${BASE}/latest.json`]);
  });

  it('reports the channel unreachable and keeps what it has', async () => {
    const { store } = makeStore({ objects: {} });
    expect(await store.checkForUpdate()).toEqual({ kind: 'unreachable' });
    expect(store.active.source).toBe('bundled');
  });

  it('ignores a pointer that is not an edition pointer, including a future schema', async () => {
    const { store } = makeStore({
      objects: { [`${BASE}/latest.json`]: utf8Encode('{"edition": "not-a-hash"}') },
    });
    expect((await store.checkForUpdate()).kind).toBe('rejected');
    expect(parseLatest({ edition: 'x'.repeat(64) })).toBeNull();
    expect(parseManifest({ ...newer().manifest, schema_version: 3 })).toBeNull();
  });

  it('installs a newer edition with every part verified, writes the pointer, and renders it on request', async () => {
    const edition = newer();
    const { store, files } = makeStore({ objects: serve(edition) });
    await store.resolve();
    const states: string[] = [];
    const final = await store.checkForUpdate((s) => states.push(s.kind));
    expect(final).toEqual({ kind: 'ready', edition: edition.manifest.edition });
    expect(states).toEqual(['checking', 'downloading', 'downloading', 'ready']);
    expect(store.active.source).toBe('bundled');
    expect(files.paths()).toEqual(
      [
        `editions/${edition.manifest.edition}/eu27.NL.json`,
        `editions/${edition.manifest.edition}/eu27.core.json`,
        `editions/${edition.manifest.edition}/manifest.json`,
        'current.json',
        LATEST,
      ].sort()
    );
    await store.useInstalled();
    expect(store.active.source).toBe('downloaded');
    expect(await store.core()).toEqual(core);
    expect(await store.country('NL')).toEqual(nl);
    // The next launch resolves to it without the channel.
    const again = makeStore({ configured: false, files }).store;
    expect((await again.resolve()).id).toBe(edition.manifest.edition);
  });

  it('rejects an edition whose part has one byte altered, keeps nothing, and names the part', async () => {
    const edition = newer();
    const objects = serve(edition);
    const key = `${BASE}/${edition.manifest.edition}/eu27.NL.json`;
    objects[key] = new Uint8Array([...objects[key]!.slice(0, -1), 0x20]);
    const { store, files } = makeStore({ objects });
    const final = await store.checkForUpdate();
    expect(final).toEqual({
      kind: 'rejected',
      reason: 'eu27.NL.json does not match its manifest entry',
      name: 'eu27.NL.json',
    });
    expect(files.paths()).toEqual([LATEST]);
    expect(store.installed).toBeNull();
  });

  it('rejects a manifest that does not match latest.json', async () => {
    const edition = newer();
    const objects = serve(edition);
    const latest = JSON.parse(new TextDecoder().decode(objects[`${BASE}/latest.json`]!));
    latest.manifest_sha256 = 'b'.repeat(64);
    objects[`${BASE}/latest.json`] = utf8Encode(JSON.stringify(latest));
    const { store, files } = makeStore({ objects });
    const final = await store.checkForUpdate();
    expect(final).toMatchObject({ kind: 'rejected', name: 'manifest.json' });
    expect(files.paths()).toEqual([LATEST]);
  });

  it('leaves no temporary directory when a download fails halfway', async () => {
    const edition = newer();
    const objects = serve(edition);
    delete objects[`${BASE}/${edition.manifest.edition}/eu27.NL.json`];
    const { store, files } = makeStore({ objects });
    expect(await store.checkForUpdate()).toMatchObject({ kind: 'rejected', name: 'eu27.NL.json' });
    expect(files.paths()).toEqual([LATEST]);
  });
});

describe('an installed edition that changes on disk', () => {
  it('fails on read, is discarded, and the bundled edition is served with the failure recorded', async () => {
    const edition = newer();
    const { store, files } = makeStore({ objects: serve(edition) });
    await store.checkForUpdate();
    await store.useInstalled();
    expect((await store.core()).generated).toBe('2026-10-15');
    const fresh = makeStore({ configured: false, files }).store; // a new launch: no in-memory cache
    await fresh.resolve();
    expect(fresh.active.source).toBe('downloaded');
    const path = `editions/${edition.manifest.edition}/eu27.core.json`;
    files.files.set(path, utf8Encode(JSON.stringify({ ...core, generated: 'tampered' })));
    const served = await fresh.core();
    expect(served.generated).toBe(BUNDLED_MANIFEST.generated);
    expect(fresh.active.source).toBe('bundled');
    expect(fresh.lastIntegrityError?.name).toBe('eu27.core.json');
    expect(files.paths().filter((p) => p.startsWith('editions/'))).toEqual([]);
    expect(await files.read('current.json')).toBeNull();
  });
});

describe('settings', () => {
  it('remembers the opt-in automatic check and nothing else', async () => {
    const files = new MemoryFileStore();
    const { store } = makeStore({ files, configured: false });
    expect(await store.autoCheck()).toBe(false);
    await store.setAutoCheck(true);
    expect(await store.autoCheck()).toBe(true);
    expect(files.paths()).toEqual(['settings.json']);
  });
});

describe('the fetcher helper', () => {
  it('serves what it was given and nothing else', async () => {
    const f = fetcherFor({ a: utf8Encode('x') });
    expect(await f('a')).toEqual(utf8Encode('x'));
    expect(await f('b')).toBeNull();
    expect(sha256Sync(utf8Encode(''))).toBe(
      'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    );
  });
});
