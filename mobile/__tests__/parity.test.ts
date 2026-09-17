/**
 * The app and the site must be the same document.
 *
 * `assets/data/eu27.json`, `src/data/types.ts` and `src/data/format.ts` are copies of files in
 * `web/`. Copies drift: `./run.sh data` regenerates the bundle, the web copy is committed, and
 * the app goes on reporting last month's figures with no error anywhere. These tests turn that
 * into a failed build instead.
 *
 * Only the leading block comment is allowed to differ, since each copy says where it came from.
 */
import fs from 'fs';
import path from 'path';

const ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(ROOT, '..');

const read = (p: string) => fs.readFileSync(p, 'utf8');
const body = (src: string) => src.replace(/^\/\*\*[\s\S]*?\*\/\n/, '');

describe('copies of web/', () => {
  it('ships the same model bundle, byte for byte', () => {
    expect(read(path.join(ROOT, 'assets/data/eu27.json'))).toBe(
      read(path.join(REPO, 'web/public/data/eu27.json'))
    );
  });

  it.each([
    ['src/data/types.ts', 'web/src/data/types.ts'],
    ['src/data/format.ts', 'web/src/utils/format.ts'],
  ])('keeps %s identical to %s below the header comment', (mine, theirs) => {
    expect(body(read(path.join(ROOT, mine)))).toBe(body(read(path.join(REPO, theirs))));
  });
});

describe('the bundle', () => {
  const bundle = JSON.parse(read(path.join(ROOT, 'assets/data/eu27.json')));

  it('covers the 27 member states', () => {
    expect(Object.keys(bundle.countries)).toHaveLength(27);
  });

  it('is the schema the screens were written against', () => {
    expect(bundle.schema_version).toBe(1);
  });

  it('names no individual: the app carries the institutional map only', () => {
    // DECISIONS.md #26 and #49. The bundle is generated from model CSVs, which hold bodies and
    // instruments, never people -- asserted here because the app is where a leak would ship.
    const text = read(path.join(ROOT, 'assets/data/eu27.json'));
    expect(text).not.toMatch(/"(first_name|last_name|email|phone)"/i);
    expect(text).not.toMatch(/[\w.+-]+@[\w-]+\.[a-z]{2,}/i);
  });
});
