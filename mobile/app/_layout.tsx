/** Root layout: theme, status bar, and the stack the tabs sit inside. */
import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { useColorScheme } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';

import { themeFor } from '@/constants/Colors';

export default function RootLayout() {
  const theme = themeFor(useColorScheme());

  return (
    <SafeAreaProvider>
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
      </Stack>
    </SafeAreaProvider>
  );
}
