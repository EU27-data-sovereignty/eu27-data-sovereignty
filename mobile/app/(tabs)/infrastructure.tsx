/**
 * Where each state's key registers are hosted, and by whom (#95). The body is the generated overview
 * (document.infrastructure in eu27.core.json), whose cells are the spans the country reports print, so a fact
 * here carries the same source and the same fact check as on its country screen. Nothing is written here.
 */
import { StyleSheet, Text } from 'react-native';

import { DocumentView } from '@/components/DocumentView';
import { Heading, Loading, Screen } from '@/components/Screen';
import { SourceList } from '@/components/SourceList';
import { SPACE, Type, useTheme } from '@/components/theme';
import { bundleView } from '@/data/parts';
import { claimsBySource, numberSources } from '@/data/sources';
import { useEdition } from '@/edition/EditionContext';

export default function Infrastructure() {
  const theme = useTheme();
  const { core, loadError } = useEdition();
  if (!core) return <Loading error={loadError} />;
  const bundle = bundleView(core);
  const doc = core.infrastructure;
  const numbers = numberSources([doc], bundle);
  const claims = claimsBySource([doc], bundle);
  const table = doc.sections
    .find((s) => s.id === 'hosting')
    ?.blocks.find((b) => b.type === 'table');
  const hosting = table?.type === 'table' ? table.rows : [];
  return (
    <Screen>
      <Heading kicker="EU-27 · Key infrastructure" title={doc.name} />
      <Text style={[styles.facts, { color: theme.fgSecondary }]}>
        {hosting.filter((r) => r[4]?.role === 'fact').length} hosting facts printed ·{' '}
        {hosting.filter((r) => r[4]?.role === 'disputed').length} withheld as disputed ·{' '}
        {new Set(hosting.map((r) => r[0]!.t)).size} of 27 states with any sourced hosting
      </Text>
      <Text style={[styles.notice, { color: theme.fgSecondary }]}>{bundle.notice.disclaimer}</Text>
      <DocumentView doc={doc} bundle={bundle} numbers={numbers} />
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </Screen>
  );
}

const styles = StyleSheet.create({
  facts: { fontSize: Type.body - 1, lineHeight: 19, marginBottom: SPACE.sm },
  notice: { fontSize: Type.body - 1, lineHeight: 19, marginBottom: SPACE.lg },
});
