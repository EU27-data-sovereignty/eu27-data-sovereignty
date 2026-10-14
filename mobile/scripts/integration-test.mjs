// The edition channel end to end against the LOCAL Supabase stack (`supabase start`), run by
// `./test.sh --integration` and by the deploy's gate (#112, #113). Keys come from `supabase status -o env`
// inside this process; they are handed to the publisher through its environment and never written or printed.
//
// What it proves, in order: the deploy's own publisher (model/edition.py) fills the bucket; every object is
// readable anonymously and hashes to its manifest entry; anonymous writes and deletes are refused; a re-run
// changes nothing; verify() passes; the app's edition store installs that edition; an object altered in the
// bucket with the service key is caught by verify() by name and rejected by the app, which keeps the edition
// it has; and the bucket is left empty.
import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';

const BUCKET = 'editions';
const ROOT = path.resolve(new URL('..', import.meta.url).pathname);
const MODEL = path.resolve(ROOT, '..', 'model');

function localStack() {
  const out = execFileSync('supabase', ['status', '-o', 'env'], {
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'ignore'],
  });
  const env = {};
  for (const line of out.split('\n')) {
    const match = line.match(/^([A-Z_]+)="?(.*?)"?$/);
    if (match) env[match[1]] = match[2];
  }
  const url = env.API_URL;
  const anonKey = env.ANON_KEY ?? env.PUBLISHABLE_KEY;
  const serviceKey = env.SERVICE_ROLE_KEY ?? env.SECRET_KEY;
  if (!url || !anonKey || !serviceKey) {
    throw new Error(
      'Could not read the local stack from `supabase status -o env` — is it running?'
    );
  }
  if (!/^http:\/\/(127\.0\.0\.1|localhost)/.test(url)) {
    throw new Error(`Refusing to run against a non-local API_URL (${new URL(url).host})`);
  }
  return { url, anonKey, serviceKey };
}

const { url, anonKey, serviceKey } = localStack();
const PUBLIC = `${url}/storage/v1/object/public/${BUCKET}`;
const admin = createClient(url, serviceKey, {
  auth: { persistSession: false, autoRefreshToken: false },
});
const sha256 = (bytes) => createHash('sha256').update(bytes).digest('hex');

/** A small edition on disk in the shape export_json.py --split writes, with a bundle file whose sha256 is its id. */
function fixture(label) {
  const dir = mkdtempSync(path.join(tmpdir(), 'eu27-edition-'));
  const bundle = Buffer.from(
    `{"schema_version": 2, "generated": "2026-10-15", "fixture": "${label}"}\n`
  );
  writeFileSync(path.join(dir, 'eu27.json'), bundle);
  const parts = {
    'eu27.core.json': Buffer.from(
      JSON.stringify({ schema_version: 2, generated: '2026-10-15', index: {} })
    ),
    'eu27.NL.json': Buffer.from(
      JSON.stringify({ documents: { NL: { iso: 'NL', name: 'Netherlands', sections: [] } } })
    ),
    'eu27.DE.json': Buffer.from(
      JSON.stringify({ documents: { DE: { iso: 'DE', name: 'Germany', sections: [] } } })
    ),
  };
  for (const [name, bytes] of Object.entries(parts)) writeFileSync(path.join(dir, name), bytes);
  const manifest = {
    schema_version: 2,
    generated: '2026-10-15',
    edition: sha256(bundle),
    parts: Object.fromEntries(
      Object.entries(parts).map(([n, b]) => [n, { sha256: sha256(b), bytes: b.length }])
    ),
  };
  writeFileSync(path.join(dir, 'manifest.json'), JSON.stringify(manifest, null, 1));
  return { dir, manifest, parts };
}

function python(args, extraEnv = {}) {
  const r = spawnSync('python3', [path.join(MODEL, 'edition.py'), ...args], {
    encoding: 'utf8',
    env: { ...process.env, ...extraEnv },
  });
  return { code: r.status, out: (r.stdout ?? '') + (r.stderr ?? '') };
}

const publisherEnv = { SUPABASE_URL: url, SUPABASE_SERVICE_ROLE_KEY: serviceKey };
const publish = (f, commit) =>
  python(
    ['publish', '--dir', f.dir, '--bundle', path.join(f.dir, 'eu27.json'), '--commit', commit],
    publisherEnv
  );
const verify = (f) =>
  python(['verify', '--url', PUBLIC, '--manifest', path.join(f.dir, 'manifest.json')]);

async function anon(method, objectPath, body) {
  // The app's own key: it must unlock nothing but reads.
  const target =
    method === 'GET'
      ? `${PUBLIC}/${objectPath}`
      : `${url}/storage/v1/object/${BUCKET}/${objectPath}`;
  return fetch(target, {
    method,
    headers: {
      Authorization: `Bearer ${anonKey}`,
      apikey: anonKey,
      'Content-Type': 'application/json',
    },
    body,
  });
}

async function listAll(prefix = '') {
  const { data, error } = await admin.storage.from(BUCKET).list(prefix, { limit: 1000 });
  if (error) throw error;
  const paths = [];
  for (const entry of data ?? []) {
    const p = prefix ? `${prefix}/${entry.name}` : entry.name;
    if (entry.id) paths.push(p);
    else paths.push(...(await listAll(p)));
  }
  return paths;
}

function jest(expectation) {
  const r = spawnSync(
    'npx',
    ['jest', '--testPathIgnorePatterns', '/node_modules/', '__tests__/edition.integration.test.ts'],
    {
      cwd: ROOT,
      encoding: 'utf8',
      env: { ...process.env, EDITION_URL: PUBLIC, EDITION_EXPECT: expectation },
    }
  );
  if (r.status !== 0) throw new Error(`jest (${expectation}) failed:\n${r.stdout}\n${r.stderr}`);
}

const steps = [];
const step = (name, fn) => steps.push({ name, fn });
const good = fixture('good');
const second = fixture('second');

step('the publisher fills the bucket with the good edition', () => {
  const r = publish(good, 'it-good');
  assert.equal(r.code, 0, r.out);
  assert.doesNotMatch(r.out, new RegExp(serviceKey), 'the key must never be printed');
});

step('every object is readable anonymously and hashes to its manifest entry', async () => {
  for (const [name, bytes] of Object.entries(good.parts)) {
    const r = await anon('GET', `${good.manifest.edition}/${name}`);
    assert.equal(r.status, 200, name);
    assert.equal(sha256(Buffer.from(await r.arrayBuffer())), sha256(bytes), name);
  }
  const latest = await (await anon('GET', 'latest.json')).json();
  assert.equal(latest.edition, good.manifest.edition);
});

step('anonymous writes and deletes are refused', async () => {
  const existing = `${good.manifest.edition}/eu27.NL.json`;
  for (const [method, target] of [
    ['POST', existing],
    ['DELETE', existing],
    ['POST', `${good.manifest.edition}/eu27.XX.json`],
    ['POST', 'latest.json'],
  ]) {
    const r = await anon(method, target, method === 'POST' ? '{}' : undefined);
    assert.ok(r.status >= 400 && r.status < 500, `${method} ${target} answered ${r.status}`);
  }
  const r = await anon('GET', `${good.manifest.edition}/eu27.NL.json`);
  assert.equal(
    sha256(Buffer.from(await r.arrayBuffer())),
    good.manifest.parts['eu27.NL.json'].sha256,
    'unchanged'
  );
});

step('a re-run of the same edition changes nothing and passes', () => {
  const r = publish(good, 'it-good');
  assert.equal(r.code, 0, r.out);
  assert.match(r.out, /already published, identical/);
});

step('verify() passes on the good edition', () => {
  const r = verify(good);
  assert.equal(r.code, 0, r.out);
});

step('the app installs the good edition from the bucket', () => jest('install'));

step('an object altered in the bucket is caught by verify() by name', async () => {
  const r = publish(second, 'it-second');
  assert.equal(r.code, 0, r.out);
  const tampered = Buffer.from(
    JSON.stringify({
      documents: { DE: { iso: 'DE', name: 'Germany', sections: [], tampered: true } },
    })
  );
  const { error } = await admin.storage
    .from(BUCKET)
    .upload(`${second.manifest.edition}/eu27.DE.json`, tampered, {
      upsert: true,
      contentType: 'application/json',
    });
  assert.ifError(error);
  const v = verify(second);
  assert.equal(v.code, 1);
  assert.match(v.out, /FAIL served eu27\.DE\.json/);
});

step('the app rejects the altered edition and keeps the one it has', () => jest('reject'));

step('cleanup: the bucket is left empty', async () => {
  const paths = await listAll();
  if (paths.length) {
    const { error } = await admin.storage.from(BUCKET).remove(paths);
    assert.ifError(error);
  }
  assert.deepEqual(await listAll(), []);
  rmSync(good.dir, { recursive: true, force: true });
  rmSync(second.dir, { recursive: true, force: true });
});

let failed = 0;
for (const { name, fn } of steps) {
  try {
    await fn();
    console.log(`ok    ${name}`);
  } catch (e) {
    failed++;
    console.log(
      `FAIL  ${name}\n      ${String(e.message ?? e)
        .split('\n')
        .join('\n      ')}`
    );
    if (name.startsWith('cleanup')) break;
  }
}
console.log(
  `${steps.length - failed} of ${steps.length} integration steps passed against ${new URL(url).host}`
);
process.exit(failed ? 1 : 0);
