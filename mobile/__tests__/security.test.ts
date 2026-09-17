/**
 * The checks that keep this app boring: no capabilities, no telemetry, no publishable secrets.
 *
 * A reader of a public dataset needs nothing from the device and has nothing to collect. That
 * is a property worth asserting rather than intending, because each of these is one careless
 * dependency or one copied config block away from stopping being true -- and the failure is
 * silent. `ROADMAP.md`'s rule applies: the countermeasure for a documented rule the tree can
 * stop matching is a check that fails the build.
 */
import fs from 'fs';
import path from 'path';

const ROOT = path.resolve(__dirname, '..');
const read = (p: string) => fs.readFileSync(path.join(ROOT, p), 'utf8');
const json = (p: string) => JSON.parse(read(p));

const SECRET_SHAPED = /secret|service_role|private|token|password|credential/i;

describe('publishable configuration', () => {
  const env = read('.env.template');

  it('declares only anon Supabase values, because Expo inlines EXPO_PUBLIC_* into the bundle', () => {
    const names = [...env.matchAll(/^(EXPO_PUBLIC_[A-Z0-9_]+)=/gm)].map(m => m[1]);
    expect(names).toEqual(['EXPO_PUBLIC_SUPABASE_URL', 'EXPO_PUBLIC_SUPABASE_ANON_KEY']);
    for (const name of names) expect(name).not.toMatch(SECRET_SHAPED);
  });

  it('ships no values in the template', () => {
    for (const [, value] of env.matchAll(/^EXPO_PUBLIC_[A-Z0-9_]+=(.*)$/gm)) {
      expect(value.trim()).toBe('');
    }
  });

  it('keeps credentials out of app.json', () => {
    const app = json('app.json');
    expect(JSON.stringify(app.expo.extra ?? {})).not.toMatch(SECRET_SHAPED);
  });
});

describe('device capabilities', () => {
  const { expo } = json('app.json');

  it('asks for no Android permissions', () => {
    expect(expo.android.permissions).toEqual([]);
  });

  it('declares no iOS usage strings, so no capability prompt can appear', () => {
    expect(expo.ios.infoPlist).toEqual({});
  });

  it('refuses cleartext traffic', () => {
    expect(expo.android.usesCleartextTraffic).toBe(false);
  });
});

describe('dependencies', () => {
  const pkg = json('package.json');
  const deps = Object.keys(pkg.dependencies);

  // An allowlist rather than a denylist: analytics, crash reporting and ad SDKs arrive under
  // names nobody predicts, and each one would start sending device data on first launch.
  const ALLOWED = [
    '@react-native-async-storage/async-storage',
    '@supabase/supabase-js',
    'expo',
    'expo-constants',
    'expo-linking',
    'expo-router',
    'expo-status-bar',
    'react',
    'react-dom',
    'react-native',
    'react-native-safe-area-context',
    'react-native-screens',
    'react-native-url-polyfill',
    'react-native-web',
  ];

  it('contains nothing outside the allowlist', () => {
    expect(deps.sort()).toEqual([...ALLOWED].sort());
  });

  it('pins every version exactly', () => {
    const all = { ...pkg.dependencies, ...pkg.devDependencies };
    const ranged = Object.entries(all).filter(([, v]) => /[\^~*x]|\s-\s|>|</.test(String(v)));
    expect(ranged).toEqual([]);
  });
});

describe('network', () => {
  const sources = (dir: string): string[] =>
    fs
      .readdirSync(path.join(ROOT, dir), { withFileTypes: true })
      .flatMap((e: fs.Dirent) =>
        e.isDirectory()
          ? sources(path.join(dir, e.name))
          : /\.tsx?$/.test(e.name)
            ? [path.join(dir, e.name)]
            : []
      );

  const files = [...sources('app'), ...sources('src')];

  it('hardcodes no remote host: content is a bundled asset, and the only URL is configured', () => {
    for (const f of files) {
      const body = read(f);
      const urls = [...body.matchAll(/https?:\/\/[^\s'"`)]+/g)].map(m => m[0]);
      expect({ file: f, urls }).toEqual({ file: f, urls: [] });
    }
  });

  it('stores exactly one thing on the device: the last country viewed', () => {
    const keys = files.flatMap(f => [
      ...read(f).matchAll(/AsyncStorage\.(setItem|getItem|removeItem)\(\s*([A-Za-z_]+)/g),
    ]);
    for (const [, , key] of keys) expect(key).toBe('LAST_VIEWED');
  });
});
