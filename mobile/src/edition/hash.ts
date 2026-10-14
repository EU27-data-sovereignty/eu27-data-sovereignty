/**
 * SHA-256 as lowercase hex, the one hash every side of the edition channel uses: `hashlib` in
 * `model/export_json.py` and `model/edition.py`, `sha256sum` in the deploy summary, `node:crypto` in the
 * tests, and expo-crypto here. The store takes the function as a port, so Jest never needs the native module.
 */
import * as Crypto from 'expo-crypto';

export type Sha256 = (bytes: Uint8Array) => Promise<string>;

export function toHex(buffer: ArrayBuffer): string {
  return Array.from(new Uint8Array(buffer), (b) => b.toString(16).padStart(2, '0')).join('');
}

export const expoSha256: Sha256 = async (bytes) => {
  // A fresh ArrayBuffer: digest() wants a BufferSource that is not a view onto a larger buffer.
  const copy = new Uint8Array(bytes.byteLength);
  copy.set(bytes);
  return toHex(await Crypto.digest(Crypto.CryptoDigestAlgorithm.SHA256, copy.buffer));
};
