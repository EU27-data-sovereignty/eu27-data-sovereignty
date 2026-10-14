/**
 * An in-memory `FileStore` for Jest and the Node integration test: the same `EditionStore` runs on it as on
 * the device. Downloads go through an injected fetcher, so a test can serve any bytes, or none, for a URL
 * and read back every request the store made.
 */
import type { FileStore } from './EditionStore';
import { utf8Encode } from './utf8';

export type Fetcher = (url: string) => Promise<Uint8Array | null>;

export class MemoryFileStore implements FileStore {
  readonly files = new Map<string, Uint8Array>();
  readonly requests: string[] = [];

  constructor(private readonly fetcher: Fetcher = async () => null) {}

  async read(path: string): Promise<Uint8Array | null> {
    return this.files.get(path) ?? null;
  }

  async write(path: string, data: Uint8Array | string): Promise<void> {
    this.files.set(path, typeof data === 'string' ? utf8Encode(data) : data);
  }

  async download(url: string, path: string): Promise<void> {
    this.requests.push(url);
    const bytes = await this.fetcher(url);
    if (!bytes) throw new Error(`download failed: ${url}`);
    this.files.set(path, bytes);
  }

  async exists(path: string): Promise<boolean> {
    return this.files.has(path) || [...this.files.keys()].some((k) => k.startsWith(path + '/'));
  }

  async remove(path: string): Promise<void> {
    for (const key of [...this.files.keys()]) {
      if (key === path || key.startsWith(path + '/')) this.files.delete(key);
    }
  }

  async move(from: string, to: string): Promise<void> {
    for (const [key, value] of [...this.files.entries()]) {
      if (key.startsWith(from + '/')) {
        this.files.delete(key);
        this.files.set(to + key.slice(from.length), value);
      }
    }
  }

  /** Paths on disk, sorted, for assertions about what an install left behind. */
  paths(): string[] {
    return [...this.files.keys()].sort();
  }
}
