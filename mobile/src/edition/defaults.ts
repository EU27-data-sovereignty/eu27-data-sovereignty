/**
 * The store the app runs on: the device's files, expo-crypto's SHA-256, the configured channel (or none) and
 * the edition inside the binary. Tests build their own from the same parts.
 */
import { BUNDLED_MANIFEST, bundledPart } from '@/data/bundled';
import { channel } from '@/services/channel';
import { EditionStore } from './EditionStore';
import { ExpoFileStore } from './expoFiles';
import { expoSha256 } from './hash';

export function createEditionStore(): EditionStore {
  return new EditionStore({
    files: new ExpoFileStore(),
    sha256: expoSha256,
    channel,
    bundled: { manifest: BUNDLED_MANIFEST, part: bundledPart },
  });
}
