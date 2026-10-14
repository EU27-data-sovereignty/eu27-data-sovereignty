/**
 * A state's group range as five cells, the placed group outlined: the confidence, drawn, as on the web's
 * ranking page. Ids and labels only; there is no score anywhere in the edition (#77, tests/test_sovereignty.py).
 */
import { StyleSheet, View } from 'react-native';

import type { GroupId, Placement } from '@/data/types';
import { useTheme } from './theme';

export function groupFill(theme: ReturnType<typeof useTheme>): Record<GroupId, string> {
  return {
    law_and_practice: theme.rank1,
    practice_only: theme.rank2,
    law_only: theme.rank3,
    not_demonstrated: theme.rank4,
    dependent: theme.rank5,
  };
}

export function RangeBar({ p, order }: { p: Placement; order: GroupId[] }) {
  const theme = useTheme();
  const fill = groupFill(theme);
  return (
    <View
      style={styles.bar}
      accessibilityElementsHidden
      importantForAccessibility="no-hide-descendants"
    >
      {order.map((g) => (
        <View
          key={g}
          style={[
            styles.cell,
            { backgroundColor: p.range.includes(g) ? fill[g] : theme.bgEmphasis },
            g === p.group ? { borderWidth: 1.5, borderColor: theme.fgPrimary } : null,
          ]}
        />
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  bar: { flexDirection: 'row', gap: 1 },
  cell: { width: 10, height: 8 },
});
