/** Five tabs: the 27 countries, the infrastructure overview, the ranking, the method, and the edition. */
import { Tabs } from 'expo-router';
import { Text, type ColorValue } from 'react-native';

import { useTheme } from '@/components/theme';

function glyph(g: string) {
  return function TabGlyph({ color }: { color: ColorValue }) {
    return (
      <Text style={{ color, fontSize: 18 }} accessibilityElementsHidden>
        {g}
      </Text>
    );
  };
}

export default function TabsLayout() {
  const theme = useTheme();
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
      <Tabs.Screen name="index" options={{ title: 'Countries', tabBarIcon: glyph('▦') }} />
      <Tabs.Screen name="infrastructure" options={{ title: 'Hosting', tabBarIcon: glyph('▤') }} />
      <Tabs.Screen name="sovereignty" options={{ title: 'Ranking', tabBarIcon: glyph('▥') }} />
      <Tabs.Screen name="method" options={{ title: 'Method', tabBarIcon: glyph('◈') }} />
      <Tabs.Screen name="about" options={{ title: 'Edition', tabBarIcon: glyph('◉') }} />
    </Tabs>
  );
}
