/**
 * The device's `FileStore`, on expo-file-system, under one directory of the app's own documents folder.
 * This is the only file in the app that downloads anything: `File.downloadFileAsync` is the whole network
 * surface, and the URLs it is handed come from `src/services/channel.ts` alone (`__tests__/security.test.ts`).
 */
import { Directory, File, Paths } from 'expo-file-system';

import type { FileStore } from './EditionStore';

export class ExpoFileStore implements FileStore {
  constructor(private readonly root: Directory = new Directory(Paths.document, 'eu27')) {}

  private segments(path: string): string[] {
    return path.split('/').filter(Boolean);
  }

  private file(path: string): File {
    return new File(this.root, ...this.segments(path));
  }

  private directory(path: string): Directory {
    return new Directory(this.root, ...this.segments(path));
  }

  private ensureParent(path: string): void {
    const parts = this.segments(path);
    parts.pop();
    const parent = parts.length ? new Directory(this.root, ...parts) : this.root;
    if (!parent.exists) parent.create({ intermediates: true, idempotent: true });
  }

  async read(path: string): Promise<Uint8Array | null> {
    const file = this.file(path);
    if (!file.exists) return null;
    return file.bytes();
  }

  async write(path: string, data: Uint8Array | string): Promise<void> {
    this.ensureParent(path);
    const file = this.file(path);
    if (!file.exists) file.create({ intermediates: true, overwrite: true });
    file.write(data);
  }

  async download(url: string, path: string): Promise<void> {
    this.ensureParent(path);
    const file = this.file(path);
    if (file.exists) file.delete();
    await File.downloadFileAsync(url, file);
  }

  async exists(path: string): Promise<boolean> {
    return this.file(path).exists || this.directory(path).exists;
  }

  async remove(path: string): Promise<void> {
    const file = this.file(path);
    if (file.exists) {
      file.delete();
      return;
    }
    const directory = this.directory(path);
    if (directory.exists) directory.delete();
  }

  async move(from: string, to: string): Promise<void> {
    this.ensureParent(to);
    await this.directory(from).move(this.directory(to));
  }
}
