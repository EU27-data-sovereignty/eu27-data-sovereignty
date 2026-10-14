/**
 * Which edition the app renders, and how a newer one arrives (#110, #111).
 *
 * The app ships an edition inside its binary: `assets/data/manifest.json` and the 28 parts it names. The
 * edition channel is one public, read-only bucket holding `latest.json`, a pointer to the edition the deploy
 * last published, and under each edition id the same manifest and parts. This store:
 *
 * - renders the bundled edition unless a downloaded edition was installed and verified;
 * - hashes every downloaded part on **every read**, before it is parsed, and on a mismatch deletes that
 *   edition, falls back to the bundled one and records the failure by part name;
 * - checks for a newer edition only when asked (a tap in About, or the opt-in automatic check), downloads
 *   it into a temporary directory, verifies the manifest against `latest.json` and every part against the
 *   manifest, and only then moves it into place. A failure leaves nothing behind and names the part.
 *
 * Trust boundary, stated once: the hash chain (latest.json -> manifest -> parts) proves that what arrived is
 * what the deploy published and that it was not altered in transit or on disk. It does not prove who
 * published, since the pointer and the manifest come from the same origin; until a signed manifest exists,
 * the Supabase project is a trusted party (DECISIONS.md #111). Bundled parts are not hashed at runtime: they
 * are inside the code-signed binary, and `__tests__/parity.test.ts` pins them to the committed manifest.
 *
 * Three ports are injected (files, sha256, channel), so Jest and the Node integration test drive the same
 * code the device runs. Nothing here reaches the network except through `FileStore.download`, and the only
 * URLs it is given come from `src/services/channel.ts`.
 */
import type { CorePart, CountryPart } from '@/data/parts';
import type { Channel } from '@/services/channel';
import type { Sha256 } from './hash';
import {
  CORE_PART,
  LATEST,
  MANIFEST,
  PUBLISHED,
  isHex64,
  parseLatest,
  parseManifest,
  parsePublished,
  partName,
  type Latest,
  type Manifest,
  type Published,
} from './manifest';
import { utf8Decode } from './utf8';

export interface FileStore {
  /** The file's bytes, or null when it does not exist. */
  read(path: string): Promise<Uint8Array | null>;
  write(path: string, data: Uint8Array | string): Promise<void>;
  /** Fetch a URL into a file; rejects on a network or HTTP failure. The one way bytes enter the device. */
  download(url: string, path: string): Promise<void>;
  exists(path: string): Promise<boolean>;
  /** Remove a file or a directory tree; a missing path is not an error. */
  remove(path: string): Promise<void>;
  /** Rename a directory. */
  move(from: string, to: string): Promise<void>;
}

export type EditionSource = 'bundled' | 'downloaded';

export interface Edition {
  id: string;
  manifest: Manifest;
  source: EditionSource;
  /** The deploy's record, when the edition came through the channel. */
  published: Published | null;
}

export type UpdateState =
  | { kind: 'unconfigured' }
  | { kind: 'idle' }
  | { kind: 'checking' }
  | { kind: 'up-to-date' }
  | { kind: 'downloading'; name: string; done: number; total: number }
  | { kind: 'ready'; edition: string }
  | { kind: 'rejected'; reason: string; name?: string }
  | { kind: 'unreachable' };

export interface StoreDeps {
  files: FileStore;
  sha256: Sha256;
  channel: () => Channel | null;
  bundled: { manifest: Manifest; part: (name: string) => unknown };
}

export class EditionIntegrityError extends Error {
  constructor(
    readonly name: string,
    readonly edition: string
  ) {
    super(
      `${name} in edition ${edition.slice(0, 16)} does not match its manifest; the edition was discarded`
    );
  }
}

const POINTER = 'current.json';
const SETTINGS = 'settings.json';
const dir = (edition: string) => `editions/${edition}`;

export class EditionStore {
  active: Edition;
  /** A downloaded edition verified and in place, not yet the one rendered. */
  installed: Edition | null = null;
  lastIntegrityError: EditionIntegrityError | null = null;
  private readonly cache = new Map<string, unknown>();

  constructor(private readonly deps: StoreDeps) {
    this.active = this.bundled();
  }

  get bundledId(): string {
    return this.deps.bundled.manifest.edition;
  }

  private bundled(): Edition {
    return {
      id: this.bundledId,
      manifest: this.deps.bundled.manifest,
      source: 'bundled',
      published: null,
    };
  }

  /** At launch: the installed edition if its manifest is in place and names it, else the bundled one. */
  async resolve(): Promise<Edition> {
    const pointer = await this.readJson(POINTER);
    const id =
      pointer && typeof pointer === 'object' ? (pointer as { edition?: unknown }).edition : null;
    if (isHex64(id) && id !== this.bundledId) {
      const edition = await this.readInstalled(id);
      if (edition) {
        this.active = edition;
        this.cache.clear();
        return edition;
      }
      await this.deps.files.remove(POINTER);
    }
    this.active = this.bundled();
    this.cache.clear();
    return this.active;
  }

  private async readInstalled(id: string): Promise<Edition | null> {
    const manifest = parseManifest(await this.readJson(`${dir(id)}/${MANIFEST}`));
    if (!manifest || manifest.edition !== id) return null;
    const published = parsePublished(await this.readJson(`${dir(id)}/${PUBLISHED}`));
    return { id, manifest, source: 'downloaded', published };
  }

  async core(): Promise<CorePart> {
    return (await this.part(CORE_PART)) as CorePart;
  }

  async country(iso: string): Promise<CountryPart> {
    return (await this.part(partName(iso.toUpperCase()))) as CountryPart;
  }

  /** A part of the active edition, verified on every read when it was downloaded. */
  private async part(name: string): Promise<unknown> {
    const key = `${this.active.id}/${name}`;
    const cached = this.cache.get(key);
    if (cached !== undefined) return cached;
    if (!(name in this.active.manifest.parts))
      throw new Error(`no part named ${name} in this edition`);
    let value: unknown;
    if (this.active.source === 'bundled') {
      value = this.deps.bundled.part(name);
      if (value === undefined) throw new Error(`${name} is in the manifest but not in the binary`);
    } else {
      const bytes = await this.deps.files.read(`${dir(this.active.id)}/${name}`);
      const entry = this.active.manifest.parts[name]!;
      if (
        !bytes ||
        bytes.length !== entry.bytes ||
        (await this.deps.sha256(bytes)) !== entry.sha256
      ) {
        // Never render a part whose hash fails: discard the edition and serve the bundled one.
        const failed = new EditionIntegrityError(name, this.active.id);
        await this.deps.files.remove(dir(this.active.id));
        await this.deps.files.remove(POINTER);
        this.lastIntegrityError = failed;
        this.active = this.bundled();
        this.cache.clear();
        return this.part(name);
      }
      value = JSON.parse(utf8Decode(bytes));
    }
    this.cache.set(key, value);
    return value;
  }

  /**
   * Ask the channel for a newer edition and, if there is one, download and verify it. Every state change
   * is reported; the final state is returned. Nothing of a rejected edition stays on disk.
   */
  async checkForUpdate(onState: (s: UpdateState) => void = () => {}): Promise<UpdateState> {
    const report = (s: UpdateState) => {
      onState(s);
      return s;
    };
    const channel = this.deps.channel();
    if (!channel) return report({ kind: 'unconfigured' });
    report({ kind: 'checking' });
    let latest: Latest | null;
    try {
      await this.deps.files.download(channel.latestUrl(), LATEST);
      latest = parseLatest(await this.readJson(LATEST));
    } catch {
      return report({ kind: 'unreachable' });
    }
    if (!latest) return report({ kind: 'rejected', reason: `${LATEST} is not an edition pointer` });
    if (latest.edition === this.active.id) return report({ kind: 'up-to-date' });
    if (this.installed?.id === latest.edition)
      return report({ kind: 'ready', edition: latest.edition });
    const already = await this.readInstalled(latest.edition);
    if (already) {
      this.installed = already;
      return report({ kind: 'ready', edition: latest.edition });
    }
    return this.install(channel, latest, report);
  }

  private async install(
    channel: Channel,
    latest: Latest,
    report: (s: UpdateState) => UpdateState
  ): Promise<UpdateState> {
    const id = latest.edition;
    const tmp = `${dir(id)}.tmp`;
    const reject = async (reason: string, name?: string) => {
      await this.deps.files.remove(tmp);
      return report({ kind: 'rejected', reason, name });
    };
    await this.deps.files.remove(tmp);
    try {
      await this.deps.files.download(channel.objectUrl(id, MANIFEST), `${tmp}/${MANIFEST}`);
    } catch {
      return reject(`${MANIFEST} could not be downloaded`, MANIFEST);
    }
    const manifestBytes = await this.deps.files.read(`${tmp}/${MANIFEST}`);
    if (!manifestBytes || (await this.deps.sha256(manifestBytes)) !== latest.manifest_sha256) {
      return reject(`${MANIFEST} does not match ${LATEST}`, MANIFEST);
    }
    const manifest = parseManifest(JSON.parse(utf8Decode(manifestBytes)));
    if (!manifest) return reject(`${MANIFEST} is not a manifest this app can render`, MANIFEST);
    if (manifest.edition !== id) return reject(`${MANIFEST} names another edition`, MANIFEST);

    const names = Object.keys(manifest.parts).sort();
    for (const [i, name] of names.entries()) {
      report({ kind: 'downloading', name, done: i, total: names.length });
      try {
        await this.deps.files.download(channel.objectUrl(id, name), `${tmp}/${name}`);
      } catch {
        return reject(`${name} could not be downloaded`, name);
      }
      const bytes = await this.deps.files.read(`${tmp}/${name}`);
      const entry = manifest.parts[name]!;
      if (
        !bytes ||
        bytes.length !== entry.bytes ||
        (await this.deps.sha256(bytes)) !== entry.sha256
      ) {
        return reject(`${name} does not match its manifest entry`, name);
      }
    }
    try {
      await this.deps.files.download(channel.objectUrl(id, PUBLISHED), `${tmp}/${PUBLISHED}`);
    } catch {
      // The deploy's record is informative, never load-bearing: the hashes above are.
    }
    await this.deps.files.remove(dir(id));
    await this.deps.files.move(tmp, dir(id));
    await this.deps.files.write(POINTER, JSON.stringify({ edition: id }));
    const published = parsePublished(await this.readJson(`${dir(id)}/${PUBLISHED}`));
    this.installed = { id, manifest, source: 'downloaded', published };
    return report({ kind: 'ready', edition: id });
  }

  /** Render the installed edition from now on. */
  async useInstalled(): Promise<Edition> {
    if (!this.installed) return this.active;
    this.active = this.installed;
    this.installed = null;
    this.cache.clear();
    return this.active;
  }

  async autoCheck(): Promise<boolean> {
    const settings = await this.readJson(SETTINGS);
    return Boolean(
      settings &&
      typeof settings === 'object' &&
      (settings as { autoCheck?: unknown }).autoCheck === true
    );
  }

  async setAutoCheck(on: boolean): Promise<void> {
    await this.deps.files.write(SETTINGS, JSON.stringify({ autoCheck: on }));
  }

  private async readJson(path: string): Promise<unknown> {
    const bytes = await this.deps.files.read(path);
    if (!bytes) return null;
    try {
      return JSON.parse(utf8Decode(bytes));
    } catch {
      return null;
    }
  }
}
