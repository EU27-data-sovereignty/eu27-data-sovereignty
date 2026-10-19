/** Root layout: the reader's language, the edition store, the theme, the status bar, and the stack the tabs sit inside. */
import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { useMemo } from 'react';
import { SafeAreaProvider } from 'react-native-safe-area-context';

import { ErrorBoundary } from '@/components/ErrorBoundary';
import { useTheme } from '@/components/theme';
import { EditionProvider } from '@/edition/EditionContext';
import { createEditionStore } from '@/edition/defaults';
import { ExpoFileStore } from '@/edition/expoFiles';
import { LanguageProvider, useLanguage } from '@/i18n/LanguageContext';
import { deviceLocales } from '@/i18n/deviceLocales';
import { expoAppUpdates } from '@/update/expoAppUpdates';

export default function RootLayout() {
  const files = useMemo(() => new ExpoFileStore(), []);
  const device = useMemo(() => deviceLocales(), []);
  return (
    <LanguageProvider files={files} device={device}>
      <ErrorBoundary>
        <Root />
      </ErrorBoundary>
    </LanguageProvider>
  );
}

function Root() {
  const theme = useTheme();
  const { t } = useLanguage();
  const store = useMemo(() => createEditionStore(), []);
  return (
    <SafeAreaProvider>
      <EditionProvider store={store} appUpdates={expoAppUpdates}>
        <StatusBar style="auto" />
        <Stack
          screenOptions={{
            headerStyle: { backgroundColor: theme.bgPage },
            headerTintColor: theme.fgPrimary,
            headerShadowVisible: false,
            contentStyle: { backgroundColor: theme.bgPage },
          }}
        >
          <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
          <Stack.Screen name="country/[iso]" options={{ title: t('app.title.country') }} />
          <Stack.Screen name="fact-check/index" options={{ title: t('app.title.factcheck') }} />
          <Stack.Screen name="fact-check/[iso]" options={{ title: t('app.title.factcheck') }} />
        </Stack>
      </EditionProvider>
    </SafeAreaProvider>
  );
}
