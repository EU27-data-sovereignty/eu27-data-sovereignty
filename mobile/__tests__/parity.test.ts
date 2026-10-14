/**
 * The app and the site must be the same document (#110).
 *
 * Three files under `src/data/` are copies of files in `web/`, and the edition under `assets/data/` is a
 * split of `web/public/data/eu27.json`. Copies drift: `./run.sh data` regenerates the bundle, the web copy is
 * committed, and the app goes on reporting last month's figures with no error anywhere. These tests turn
 * that into a failed build instead. Only the leading block comment of a copied file may differ, since each
 * copy says where it came from.
 */
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

import { BUNDLED_MANIFEST, BUNDLED_PART_NAMES } from '../src/data/bundled';
import { SCHEMA_VERSION, parseManifest } from '../src/edition/manifest';

const ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(ROOT, '..');
const read = (p: string) => fs.readFileSync(p, 'utf8');
const body = (src: string) => src.replace(/^\/\*\*[\s\S]*?\*\/\n/, '');
const sha256 = (p: string) => createHash('sha256').update(fs.readFileSync(p)).digest('hex');

describe('copies of web/', () => {
  it.each([
    ['src/data/types.ts', 'web/src/data/types.ts'],
    ['src/data/format.ts', 'web/src/utils/format.ts'],
    ['src/data/sources.ts', 'web/src/data/sources.ts'],
  ])('keeps %s identical to %s below the header comment', (mine, theirs) => {
    expect(body(read(path.join(ROOT, mine)))).toBe(body(read(path.join(REPO, theirs))));
  });
});

describe('the edition inside the binary', () => {
  const manifestPath = path.join(ROOT, 'assets/data/manifest.json');

  it('is the split of the committed bundle: the edition id is its sha256', () => {
    expect(BUNDLED_MANIFEST.edition).toBe(sha256(path.join(REPO, 'web/public/data/eu27.json')));
  });

  it('has a manifest this app can parse, at the schema the screens were written against', () => {
    expect(BUNDLED_MANIFEST.schema_version).toBe(SCHEMA_VERSION);
    expect(parseManifest(JSON.parse(read(manifestPath)))).toEqual(BUNDLED_MANIFEST);
  });

  it('is the same manifest the site publishes at /data/manifest.json', () => {
    expect(read(manifestPath)).toBe(read(path.join(REPO, 'web/public/data/manifest.json')));
  });

  it('requires exactly the parts the manifest names', () => {
    expect([...BUNDLED_PART_NAMES].sort()).toEqual(Object.keys(BUNDLED_MANIFEST.parts).sort());
    expect(BUNDLED_PART_NAMES).toHaveLength(28);
    expect(BUNDLED_PART_NAMES).toContain('eu27.EL.json');
  });

  it.each(Object.entries(BUNDLED_MANIFEST.parts))(
    'ships %s with the hash and size the manifest records',
    (name, entry) => {
      const file = path.join(ROOT, 'assets/data', name);
      expect(fs.statSync(file).size).toBe(entry.bytes);
      expect(sha256(file)).toBe(entry.sha256);
    }
  );

  it('names no individual: the app carries the institutional map only', () => {
    // DECISIONS.md #26 and #49. The parts are generated from model CSVs, which hold bodies and instruments,
    // never people -- asserted here because the app is where a leak would ship.
    for (const name of BUNDLED_PART_NAMES) {
      const text = read(path.join(ROOT, 'assets/data', name));
      expect(text).not.toMatch(/"(first_name|last_name|email|phone)"/i);
      expect(text).not.toMatch(/[\w.+-]+@[\w-]+\.[a-z]{2,}/i);
    }
  });
});
