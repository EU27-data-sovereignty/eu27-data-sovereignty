/** Two tabs: the 27 countries, and how the numbers were produced. */
import { Tabs } from 'expo-router';
import { useColorScheme } from 'react-native';

import { themeFor } from '@/constants/Colors';

export default function TabsLayout() {
  const theme = themeFor(useColorScheme());

  return (
    <Tabs
      screenOptions={{
        headerStyle: { backgroundColor: theme.bgPage },
        headerTintColor: theme.fgPrimary,
        headerShadowVisible: false,
        tabBarActiveTintColor: theme.accentText,
        tabBarInactiveTintColor: theme.fgMuted,
        tabBarStyle: { backgroundColor: theme.bgCard, borderTopColor: theme.border },
        sceneStyle: { backgroundColor: theme.bgPage },
      }}
    >
      <Tabs.Screen name="index" options={{ title: 'Countries' }} />
      <Tabs.Screen name="methodology" options={{ title: 'Methodology' }} />
    </Tabs>
  );
}
