/** Root layout: the edition store, the theme, the status bar, and the stack the tabs sit inside. */
import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { useMemo } from 'react';
import { SafeAreaProvider } from 'react-native-safe-area-context';

import { ErrorBoundary } from '@/components/ErrorBoundary';
import { useTheme } from '@/components/theme';
import { EditionProvider } from '@/edition/EditionContext';
import { createEditionStore } from '@/edition/defaults';

export default function RootLayout() {
  const theme = useTheme();
  const store = useMemo(() => createEditionStore(), []);
  return (
    <ErrorBoundary>
      <SafeAreaProvider>
        <EditionProvider store={store}>
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
            <Stack.Screen name="country/[iso]" options={{ title: 'Country report' }} />
            <Stack.Screen name="fact-check/index" options={{ title: 'Fact check' }} />
            <Stack.Screen name="fact-check/[iso]" options={{ title: 'Fact check' }} />
          </Stack>
        </EditionProvider>
      </SafeAreaProvider>
    </ErrorBoundary>
  );
}
