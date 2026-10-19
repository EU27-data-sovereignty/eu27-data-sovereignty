/**
 * The checks that keep this app boring: no capabilities, no telemetry, no publishable secrets, and exactly
 * one network path (#111).
 *
 * A reader of a public dataset needs nothing from the device and has nothing to collect. That is a property
 * worth asserting rather than intending, because each of these is one careless dependency or one copied
 * config block away from stopping being true -- and the failure is silent. `ROADMAP.md`'s rule applies: the
 * countermeasure for a documented rule the tree can stop matching is a check that fails the build.
 */
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(__dirname, '..');
const read = (p: string) => fs.readFileSync(path.join(ROOT, p), 'utf8');
const json = (p: string) => JSON.parse(read(p));

const SECRET_SHAPED = /secret|service_role|private|token|password|credential/i;

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
const where = (pattern: RegExp) => files.filter((f) => pattern.test(read(f))).sort();

describe('publishable configuration', () => {
  const env = read('.env.template');

  it('declares only anon Supabase values, because Expo inlines EXPO_PUBLIC_* into the bundle', () => {
    const names = [...env.matchAll(/^(EXPO_PUBLIC_[A-Z0-9_]+)=/gm)].map((m) => m[1]);
    expect(names).toEqual(['EXPO_PUBLIC_SUPABASE_URL', 'EXPO_PUBLIC_SUPABASE_ANON_KEY']);
    for (const name of names) expect(name).not.toMatch(SECRET_SHAPED);
  });

  it('ships no values in the template', () => {
    for (const [, value] of env.matchAll(/^EXPO_PUBLIC_[A-Z0-9_]+=(.*)$/gm)) {
      expect(value.trim()).toBe('');
    }
  });

  it('never checks for an over-the-air code update unless the reader asks (#115)', () => {
    const { expo } = json('app.json');
    expect(JSON.stringify(expo.extra ?? {})).not.toMatch(SECRET_SHAPED);
    // expo-updates would otherwise ask Expo's service at every launch; the About tab asks, on a tap or the
    // opt-in, through src/update/expoAppUpdates.ts alone.
    expect(expo.updates.enabled).toBe(true);
    expect(expo.updates.checkAutomatically).toBe('NEVER');
    expect(expo.updates.fallbackToCacheTimeout).toBe(0);
    const projectId = expo.extra?.eas?.projectId;
    expect(projectId).toMatch(/^[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$/);
    expect(expo.updates.url).toBe(`https://u.expo.dev/${projectId}`);
    expect(expo.runtimeVersion).toEqual({ policy: 'appVersion' });
  });

  it('declares export compliance in config, not as a usage string', () => {
    const { expo } = json('app.json');
    expect(expo.ios.config).toEqual({ usesNonExemptEncryption: false });
  });

  it('eas.json: the pinned CLI, build numbers on EAS, and no credential in the tree (#114)', () => {
    const eas = json('eas.json');
    const pkg = json('package.json');
    // One exact pin the CLI enforces on itself; never a project dependency (expo-doctor refuses it), so
    // run.sh, test.sh and deploy.yml run `npx eas-cli@<this>`, as the deploy runs the Vercel CLI.
    expect(eas.cli.version).toMatch(/^\d+\.\d+\.\d+$/);
    expect(pkg.devDependencies['eas-cli']).toBeUndefined();
    expect(pkg.dependencies['eas-cli']).toBeUndefined();
    expect(eas.cli.appVersionSource).toBe('remote');
    expect(eas.cli.requireCommit).toBe(true);
    expect(eas.build.production.autoIncrement).toBe(true);
    expect(eas.build.production.channel).toBe('production');
    expect(eas.build.production.distribution).toBe('store');
    for (const profile of Object.values(eas.build) as { env?: unknown }[]) {
      expect(profile.env ?? {}).toEqual({});
    }
    // The App Store Connect key and the Apple account are held on EAS, never pointed at from here.
    expect(eas.submit.production.ios.ascApiKeyPath).toBeUndefined();
    expect(eas.submit.production.ios.appleId).toBeUndefined();
    expect(eas.submit.production.android.serviceAccountKeyPath).toBeUndefined();
    expect(JSON.stringify(eas)).not.toMatch(SECRET_SHAPED);
  });

  it('the store listing names the privacy policy at the site and says no person verified the data (#116)', () => {
    const { expo } = json('app.json');
    const listing = json('store.config.json').apple;
    const info = listing.info['en-US'];
    expect(info.privacyPolicyUrl).toBe(`${expo.extra.siteUrl}${expo.extra.privacyPath}`);
    expect(info.marketingUrl).toBe(expo.extra.siteUrl);
    expect(info.description).toMatch(/No person has verified them/);
    expect(listing.release.automaticRelease).toBe(false);
    // Apple's review contact comes from the environment of `./run.sh metadata push` (store.config.js).
    expect(listing.review.email).toBeUndefined();
    expect(listing.review.phone).toBeUndefined();
  });

  it('is this project, not the template', () => {
    const { expo } = json('app.json');
    expect(expo.slug).toBe('eu27-data-sovereignty');
    expect(expo.scheme).toBe('eu27');
    expect(JSON.stringify(expo)).not.toMatch(/rn-supabase|rnsupabaseapp|yourcompany/);
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

  it('allows no cleartext traffic', () => {
    // Android refuses cleartext by default since API 28; the only ways to re-enable it are the
    // usesCleartextTraffic key (not in SDK 58's schema) or the expo-build-properties plugin. Neither is here.
    expect(expo.android.usesCleartextTraffic).toBeUndefined();
    expect(JSON.stringify(expo.plugins ?? [])).not.toMatch(
      /usesCleartextTraffic|expo-build-properties/
    );
  });
});

describe('dependencies', () => {
  const pkg = json('package.json');
  const deps = Object.keys(pkg.dependencies);

  // An allowlist rather than a denylist: analytics, crash reporting and ad SDKs arrive under names nobody
  // predicts, and each one would start sending device data on first launch.
  const ALLOWED = [
    '@supabase/supabase-js',
    'expo',
    'expo-constants',
    'expo-crypto',
    'expo-file-system',
    'expo-linking',
    'expo-router',
    'expo-splash-screen',
    'expo-status-bar',
    'expo-updates',
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
    const ranged = Object.entries(all).filter(([, v]) => !/^\d+\.\d+\.\d+$/.test(String(v)));
    expect(ranged).toEqual([]);
  });

  it('persists nothing about the reader: no session storage dependency', () => {
    expect(deps).not.toContain('@react-native-async-storage/async-storage');
    expect(where(/async-storage/)).toEqual([]);
  });
});

describe('network: one path, one host, every URL derived from the configured project', () => {
  it('hardcodes no remote host', () => {
    for (const f of files) {
      const urls = [...read(f).matchAll(/https?:\/\/[^\s'"`)]+/g)].map((m) => m[0]);
      expect({ file: f, urls }).toEqual({ file: f, urls: [] });
    }
  });

  it('downloads only in the device file store', () => {
    expect(where(/\bfetch\(|XMLHttpRequest|downloadFileAsync\(/)).toEqual([
      'src/edition/expoFiles.ts',
    ]);
  });

  it('reads the environment only in the Supabase client', () => {
    expect(where(/process\.env\.EXPO_PUBLIC_/)).toEqual(['src/services/supabase.ts']);
  });

  it('builds URLs only in the channel', () => {
    expect(where(/getPublicUrl\(/)).toEqual(['src/services/channel.ts']);
    expect(where(/latestUrl\(\)|objectUrl\(/).sort()).toEqual(
      ['src/edition/EditionStore.ts', 'src/services/channel.ts'].sort()
    );
  });

  it('opens external links only where a source, a form or the privacy policy is shown', () => {
    expect(where(/Linking\.openURL/)).toEqual([
      'app/(tabs)/about.tsx',
      'app/country/[iso].tsx',
      'src/components/SourceList.tsx',
    ]);
  });

  it('builds the site address only from app.json, in one file', () => {
    expect(where(/siteUrl|privacyPath/)).toEqual(['src/services/site.ts']);
    expect(where(/privacyUrl\(/)).toEqual(['app/(tabs)/about.tsx', 'src/services/site.ts']);
    expect(read('src/services/site.ts')).toMatch(/Constants\.expoConfig/);
  });

  it('reaches the update service only through its port (#115)', () => {
    expect(where(/expo-updates/)).toEqual(['src/update/expoAppUpdates.ts']);
    expect(where(/checkForUpdateAsync|fetchUpdateAsync|reloadAsync/)).toEqual([
      'src/update/expoAppUpdates.ts',
    ]);
  });

  it('touches the device file system only in the file store', () => {
    expect(where(/Paths\.document|expo-file-system/)).toEqual(['src/edition/expoFiles.ts']);
  });
});
