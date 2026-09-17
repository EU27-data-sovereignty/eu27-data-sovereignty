/**
 * One country's case, following the same eight numbered sections as `web/src/pages/Country.tsx`.
 *
 * The section order is the argument: what the country starts with, what is structurally
 * different about it, what that implies for capacity, where it would go, what the law requires,
 * what exists today, what the migration costs, and what the geography threatens. Keeping the
 * order identical to the web page is what stops the two from becoming different documents.
 */
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Stack, useLocalSearchParams, useRouter } from 'expo-router';
import { useEffect } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, useColorScheme, View } from 'react-native';

import { Text as Type, themeFor, type Theme } from '@/constants/Colors';
import { countries, countryFor } from '@/data/bundle';
import { eur, mw, num, pct } from '@/data/format';
import { DIMENSION_LABELS, MATRIX_DIMENSIONS } from '@/data/types';

const LAST_VIEWED = 'lastViewedIso';

function Section({
  n,
  title,
  theme,
  children,
}: {
  n: number;
  title: string;
  theme: Theme;
  children: React.ReactNode;
}) {
  return (
    <View style={styles.section}>
      <Text style={[styles.sectionTitle, { color: theme.fgPrimary }]}>
        <Text style={{ color: theme.fgMuted }}>{n} </Text>
        {title}
      </Text>
      {children}
    </View>
  );
}

function Facts({ rows, theme }: { rows: [string, string][]; theme: Theme }) {
  return (
    <View>
      {rows.map(([k, v]) => (
        <View key={k} style={[styles.fact, { borderColor: theme.border }]}>
          <Text style={[styles.factKey, { color: theme.fgSecondary }]}>{k}</Text>
          <Text style={[styles.factValue, { color: theme.fgPrimary }]}>{v}</Text>
        </View>
      ))}
    </View>
  );
}

export default function CountryScreen() {
  const theme = themeFor(useColorScheme());
  const router = useRouter();
  const { iso } = useLocalSearchParams<{ iso: string }>();
  const c = countryFor(iso);

  useEffect(() => {
    if (c) AsyncStorage.setItem(LAST_VIEWED, c.iso2).catch(() => {});
  }, [c]);

  if (!c) {
    return (
      <View style={[styles.missing, { backgroundColor: theme.bgPage }]}>
        <Text style={{ color: theme.fgPrimary, fontSize: Type.heading }}>
          No country with code {String(iso)}.
        </Text>
      </View>
    );
  }

  const p = c.params;
  const cap = c.capacity;
  const phase1 = c.phases[0];

  return (
    <ScrollView style={{ backgroundColor: theme.bgPage }} contentContainerStyle={styles.page}>
      <Stack.Screen options={{ title: c.name }} />

      {/* Country switcher: the whole set is 27 items, so a scroller beats a picker. */}
      <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.switcher}>
        {countries.map(other => {
          const active = other.iso2 === c.iso2;
          return (
            <Pressable
              key={other.iso2}
              onPress={() => router.setParams({ iso: other.iso2 })}
              accessibilityRole="button"
              accessibilityLabel={other.name}
              accessibilityState={{ selected: active }}
              style={[
                styles.chip,
                {
                  borderColor: active ? theme.accent : theme.border,
                  backgroundColor: active ? theme.bgEmphasis : theme.bgCard,
                },
              ]}
            >
              <Text style={{ color: active ? theme.accentText : theme.fgSecondary, fontSize: Type.axis }}>
                {other.iso2}
              </Text>
            </Pressable>
          );
        })}
      </ScrollView>

      <Text style={[styles.lede, { color: theme.fgSecondary }]}>
        Sovereign government data centre network — capacity, legal posture, provider landscape and
        migration path.
      </Text>

      <Section n={1} title="Starting point" theme={theme}>
        <Facts
          theme={theme}
          rows={[
            ['Population', `${c.scale.population_m.toFixed(2)} m`],
            ['GDP', `EUR ${num(c.scale.gdp_eur_bn)} bn`],
            ['Public administration (NACE O)', `${num(c.scale.gov_employment_k)} k`],
            ['Electricity price', `${c.scale.elec_price_eur_mwh.toFixed(1)} EUR/MWh`],
            ['Renewables', `${c.scale.renewables_pct.toFixed(1)}%`],
            ['Live hyperscaler regions', String(c.flags.hyperscaler_regions_live)],
          ]}
        />
      </Section>

      <Section n={2} title="What is structurally different" theme={theme}>
        {c.structural_differences.map((d, i) => (
          <Text key={i} style={[styles.bullet, { color: theme.fgSecondary }]}>
            • {d.replace(/\*\*/g, '')}
          </Text>
        ))}
      </Section>

      <Section n={3} title="Capacity" theme={theme}>
        <Facts
          theme={theme}
          rows={[
            [
              'Servers',
              `${num(cap.total_servers)} (CPU ${num(cap.cpu_servers)} / GPU ${num(cap.gpu_servers)} / storage ${num(cap.storage_servers)})`,
            ],
            ['IT critical load', mw(cap.total_it_mw)],
            ['Facility design load', mw(cap.design_mw)],
            ['Sites', `${cap.sites} (by capacity ${cap.sites_by_mw}, floor ${c.flags.min_sites})`],
            ['Average per site', mw(cap.avg_mw_per_site)],
            [
              'Site count set by',
              cap.binding_constraint === 'min_sites'
                ? 'the minimum-sites floor, not capacity'
                : 'capacity',
            ],
            ['CAPEX', eur(cap.capex_total)],
            ['OPEX', `${eur(cap.opex_total)} / yr`],
          ]}
        />
      </Section>

      <Section n={4} title="Proposed geography" theme={theme}>
        {c.regions.map(r => (
          <View key={r.Region} style={[styles.card, { borderColor: theme.border }]}>
            <Text style={[styles.cardTitle, { color: theme.fgPrimary }]}>
              {r.Region} — {r['Design MW'].toFixed(1)} MW
            </Text>
            <Text style={[styles.cardMeta, { color: theme.fgSecondary }]}>
              {r.Role} · {pct(r['Share of design load'])} of design load
            </Text>
            <Text style={[styles.cardNote, { color: theme.fgMuted }]}>{r.Notes}</Text>
          </View>
        ))}
        <Text style={[styles.caveat, { color: theme.fgSecondary }]}>
          First-pass geographic hypotheses encoding only the obvious constraints, to be replaced by
          scored site selection.
        </Text>
      </Section>

      <Section n={5} title="Legal and regulatory posture" theme={theme}>
        <Facts
          theme={theme}
          rows={[
            ['Governing instrument', p['legal_instrument'] ?? '—'],
            ['Cloud certification', p['certification_scheme'] ?? '—'],
            ['Data classification', p['data_classification'] ?? '—'],
            ['Procurement route', p['procurement_vehicle'] ?? '—'],
          ]}
        />
        <Text style={[styles.body, { color: theme.fgSecondary }]}>
          Foreign jurisdiction exposure. {p['hyperscaler_gov_exposure']}
        </Text>
        <Text style={[styles.body, { color: theme.fgMuted }]}>
          Under the US CLOUD Act and FISA 702 a provider subject to US jurisdiction can face a
          lawful order for data it holds regardless of where that data sits. Residency is necessary
          but not sufficient; what matters is who holds the keys and who can be compelled.
        </Text>
      </Section>

      <Section n={6} title="Current state and provider landscape" theme={theme}>
        <Facts
          theme={theme}
          rows={[
            ['Government cloud', p['sovereign_cloud_initiative'] ?? '—'],
            ['Maturity', p['gov_cloud_maturity'] ?? '—'],
            ['Digital identity', p['digital_id'] ?? '—'],
            ['Interconnection', p['ixp'] ?? '—'],
          ]}
        />
      </Section>

      <Section n={7} title="Migration path and cost" theme={theme}>
        {c.phases.map(ph => (
          <View key={ph.Phase} style={[styles.card, { borderColor: theme.border }]}>
            <Text style={[styles.cardTitle, { color: theme.fgPrimary }]}>
              {ph.Phase} — {ph['Phase name']}
            </Text>
            <Text style={[styles.cardMeta, { color: theme.fgSecondary }]}>
              {ph['Design MW'].toFixed(1)} MW · {eur(ph['CAPEX (EUR mm)'])} ·{' '}
              {ph['Cumulative CAPEX %'].toFixed(0)}% cumulative
            </Text>
            <Text style={[styles.cardNote, { color: theme.fgMuted }]}>
              Hybrid eligible: {ph['Hybrid eligible']}
            </Text>
          </View>
        ))}
        {phase1 ? (
          <Text style={[styles.body, { color: theme.fgSecondary }]}>
            Phase 1 is the number that matters: {eur(phase1['CAPEX (EUR mm)'])} for{' '}
            {phase1['Design MW'].toFixed(1)} MW, {phase1['Cumulative CAPEX %'].toFixed(0)}% of total
            CAPEX. That is the floor below which no hybrid arrangement helps — and it is a small
            fraction of the full build.
          </Text>
        ) : null}
      </Section>

      <Section n={8} title="Sovereignty matrix" theme={theme}>
        <Facts
          theme={theme}
          rows={MATRIX_DIMENSIONS.map(d => [
            DIMENSION_LABELS[d],
            `${c.matrix[d].label} (${c.matrix[d].score.toFixed(2)})`,
          ])}
        />
        <Text style={[styles.caveat, { color: theme.fgMuted }]}>
          The eight dimensions are ordinal and are never summed into a ranking.
        </Text>
      </Section>

      <Section n={9} title="Geography and threat notes" theme={theme}>
        <Text style={[styles.body, { color: theme.fgSecondary }]}>{p['threat_notes']}</Text>
      </Section>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  page: { padding: 16, paddingBottom: 48 },
  missing: { flex: 1, alignItems: 'center', justifyContent: 'center', padding: 24 },
  switcher: { marginBottom: 12 },
  chip: { borderWidth: 1, borderRadius: 999, paddingHorizontal: 10, paddingVertical: 5, marginRight: 6 },
  lede: { fontSize: Type.body, lineHeight: 20, marginBottom: 12 },
  section: { marginBottom: 24 },
  sectionTitle: { fontSize: Type.heading, fontWeight: '600', marginBottom: 8 },
  fact: { borderTopWidth: 1, paddingVertical: 6 },
  factKey: { fontSize: Type.axis, marginBottom: 2 },
  factValue: { fontSize: Type.body, lineHeight: 19 },
  bullet: { fontSize: Type.body, lineHeight: 20, marginBottom: 6 },
  card: { borderWidth: 1, borderRadius: 8, padding: 10, marginBottom: 8 },
  cardTitle: { fontSize: Type.body, fontWeight: '600' },
  cardMeta: { fontSize: Type.axis, marginTop: 2 },
  cardNote: { fontSize: Type.axis, marginTop: 4, lineHeight: 16 },
  caveat: { fontSize: Type.axis, fontStyle: 'italic', marginTop: 4 },
  body: { fontSize: Type.body, lineHeight: 20, marginTop: 10 },
});
