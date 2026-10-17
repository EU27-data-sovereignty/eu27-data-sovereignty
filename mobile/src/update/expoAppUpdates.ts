/**
 * The device's `AppUpdatePort`, on `expo-updates`. This is the only file that imports the module
 * (`__tests__/security.test.ts`), so the whole surface the app has towards Expo's update service is here:
 * the three calls below, made only from the About tab's check (#115). The URL they use is the one in
 * `app.json` (`updates.url`), written by `eas update:configure`, never by hand.
 */
import * as Updates from 'expo-updates';

import type { AppUpdatePort } from './appUpdate';

export const expoAppUpdates: AppUpdatePort = {
  enabled: Updates.isEnabled && !__DEV__,
  build: {
    runtimeVersion: Updates.runtimeVersion,
    updateId: Updates.isEmbeddedLaunch ? null : Updates.updateId,
    channel: Updates.channel,
  },
  check: async () => (await Updates.checkForUpdateAsync()).isAvailable,
  download: async () => (await Updates.fetchUpdateAsync()).isNew,
  reload: () => Updates.reloadAsync(),
};
