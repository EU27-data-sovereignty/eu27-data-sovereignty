/**
 * The generated tokens (`src/constants/Colors.ts`, from design/tokens.json) as a hook and a few shared text
 * styles, so every screen reads the same palette in light and dark and no component names a colour.
 */
import { useColorScheme } from 'react-native';

import { Text as Type, themeFor, type Theme } from '@/constants/Colors';

export function useTheme(): Theme {
  return themeFor(useColorScheme());
}

export { Type };

export const SPACE = { xs: 4, sm: 8, md: 12, lg: 16, xl: 24 } as const;
