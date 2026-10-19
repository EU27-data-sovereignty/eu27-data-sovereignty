/**
 * Over-the-air updates of the app's own code (DECISIONS.md #115): a port, so the screens and the tests never
 * touch the Expo module directly (that is `expoAppUpdates.ts`, the one file that imports it), and one rule
 * that the port cannot break: a check runs only when the reader asks, in the same tap or the same opt-in as
 * the check for a newer edition. `app.json` sets `updates.checkAutomatically` to `NEVER`, so the native layer
 * never asks on its own (`__tests__/security.test.ts`).
 *
 * The data edition still comes only from the edition channel (#111): an app update carries code and the
 * edition inside the binary at the time it was published; the reader's downloaded edition stays in place.
 */
import { english, type Translator } from '@/i18n/catalogue';

export type AppUpdateState =
  | { kind: 'disabled' }
  | { kind: 'idle' }
  | { kind: 'checking' }
  | { kind: 'up-to-date' }
  | { kind: 'downloading' }
  | { kind: 'ready' }
  | { kind: 'unreachable' };

export interface AppBuild {
  /** The runtime version this binary accepts updates for (the app version, by policy). */
  runtimeVersion: string | null;
  /** The id of the update running now, or null when the code inside the binary is running. */
  updateId: string | null;
  channel: string | null;
}

export interface AppUpdatePort {
  /** False in a development client, on the web, and in a build without an update URL. */
  readonly enabled: boolean;
  readonly build: AppBuild;
  /** True when a newer update exists for this runtime version. */
  check(): Promise<boolean>;
  /** Download it; true when a new update is now on the device. */
  download(): Promise<boolean>;
  /** Restart on the downloaded update. */
  reload(): Promise<void>;
}

/** A build that cannot receive updates: the web export, a development client, the tests. */
export const noAppUpdates: AppUpdatePort = {
  enabled: false,
  build: { runtimeVersion: null, updateId: null, channel: null },
  check: async () => false,
  download: async () => false,
  reload: async () => {},
};

/** Ask for a newer build of the app and download it; every state change is reported, the last is returned. */
export async function checkForAppUpdate(
  port: AppUpdatePort,
  onState: (s: AppUpdateState) => void = () => {}
): Promise<AppUpdateState> {
  const report = (s: AppUpdateState) => {
    onState(s);
    return s;
  };
  if (!port.enabled) return report({ kind: 'disabled' });
  report({ kind: 'checking' });
  let available: boolean;
  try {
    available = await port.check();
  } catch {
    return report({ kind: 'unreachable' });
  }
  if (!available) return report({ kind: 'up-to-date' });
  report({ kind: 'downloading' });
  try {
    return report({ kind: (await port.download()) ? 'ready' : 'up-to-date' });
  } catch {
    return report({ kind: 'unreachable' });
  }
}

/** The sentence for a state, in the reader's language (`app.appupdate.*`, #117); English by default. */
export function describeAppUpdate(state: AppUpdateState, t: Translator['t'] = english.t): string {
  return t(`app.appupdate.${state.kind.replace(/-/g, '_')}`);
}
