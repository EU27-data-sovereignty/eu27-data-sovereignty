/**
 * The edition inside the binary: the 28 parts `model/export_json.py --split` wrote next to the manifest the
 * app also ships (#110). Each part is behind a function so Metro evaluates it on first use, not at launch.
 *
 * The requires are literal because Metro resolves them statically; `__tests__/parity.test.ts` fails if this
 * list and `assets/data/manifest.json` ever name different parts. The parts are generated (gitignored), so a
 * fresh checkout runs `./run.sh parts` (or `mobile/test.sh`) before Metro can bundle them.
 *
 * Trust boundary: bundled parts are not hashed at runtime. They sit inside the code-signed binary, and the
 * parity test pins them to the committed manifest at build time; a downloaded part is hashed on every read.
 */
import type { Manifest } from '@/edition/manifest';

export const BUNDLED_MANIFEST: Manifest = require('../../assets/data/manifest.json');

const PARTS: Record<string, () => unknown> = {
  'eu27.AT.json': () => require('../../assets/data/eu27.AT.json'),
  'eu27.BE.json': () => require('../../assets/data/eu27.BE.json'),
  'eu27.BG.json': () => require('../../assets/data/eu27.BG.json'),
  'eu27.CY.json': () => require('../../assets/data/eu27.CY.json'),
  'eu27.CZ.json': () => require('../../assets/data/eu27.CZ.json'),
  'eu27.DE.json': () => require('../../assets/data/eu27.DE.json'),
  'eu27.DK.json': () => require('../../assets/data/eu27.DK.json'),
  'eu27.EE.json': () => require('../../assets/data/eu27.EE.json'),
  'eu27.EL.json': () => require('../../assets/data/eu27.EL.json'),
  'eu27.ES.json': () => require('../../assets/data/eu27.ES.json'),
  'eu27.FI.json': () => require('../../assets/data/eu27.FI.json'),
  'eu27.FR.json': () => require('../../assets/data/eu27.FR.json'),
  'eu27.HR.json': () => require('../../assets/data/eu27.HR.json'),
  'eu27.HU.json': () => require('../../assets/data/eu27.HU.json'),
  'eu27.IE.json': () => require('../../assets/data/eu27.IE.json'),
  'eu27.IT.json': () => require('../../assets/data/eu27.IT.json'),
  'eu27.LT.json': () => require('../../assets/data/eu27.LT.json'),
  'eu27.LU.json': () => require('../../assets/data/eu27.LU.json'),
  'eu27.LV.json': () => require('../../assets/data/eu27.LV.json'),
  'eu27.MT.json': () => require('../../assets/data/eu27.MT.json'),
  'eu27.NL.json': () => require('../../assets/data/eu27.NL.json'),
  'eu27.PL.json': () => require('../../assets/data/eu27.PL.json'),
  'eu27.PT.json': () => require('../../assets/data/eu27.PT.json'),
  'eu27.RO.json': () => require('../../assets/data/eu27.RO.json'),
  'eu27.SE.json': () => require('../../assets/data/eu27.SE.json'),
  'eu27.SI.json': () => require('../../assets/data/eu27.SI.json'),
  'eu27.SK.json': () => require('../../assets/data/eu27.SK.json'),
  'eu27.core.json': () => require('../../assets/data/eu27.core.json'),
};

export const BUNDLED_PART_NAMES = Object.keys(PARTS);

/** The parsed part, or undefined for a name the binary does not carry. */
export function bundledPart(name: string): unknown {
  return PARTS[name]?.();
}
