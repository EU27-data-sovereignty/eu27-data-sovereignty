import { useParams } from 'react-router-dom'

import type { Bundle } from '@/data/types'
import { eur, mw, num, pct } from '@/utils/format'
import { NotFound } from './NotFound'

/**
 * The page's sections, in order. One array drives the contents list, the headings and the
 * anchors, so the three cannot disagree — a contents list maintained beside a separate set of
 * hardcoded headings is the drift this avoids.
 *
 * The markdown brief has its own list in `model/generate_countries.py` and the mobile reader
 * its own again; the three surfaces deliberately do not show identical sections, so they are
 * not shared. See artifacts/README.md.
 */
const SECTIONS = [
  'Starting point',
  'What is structurally different',
  'Capacity',
  'Proposed geography',
  'Legal and regulatory posture',
  'Current state and provider landscape',
  'Migration path and cost',
  'Geography and threat notes',
  'Critical national data in scope',
] as const

function sectionTitle(n: number): string {
  const title = SECTIONS[n - 1]
  if (title === undefined) throw new Error(`no section ${n}`)
  return title
}

const anchor = (n: number) =>
  `s${n}-${sectionTitle(n)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')}`

function Contents() {
  return (
    <nav aria-label="Contents" className="mb-8 border-l-2 border-[var(--color-border)] pl-4">
      <h2 className="mb-2 text-sm font-semibold text-[var(--color-fg-secondary)]">Contents</h2>
      <ol className="text-sm">
        {SECTIONS.map((title, i) => (
          <li key={title} className="mb-1">
            <span className="mr-2 text-[var(--color-fg-muted)] tabular-nums">{i + 1}</span>
            <a className="text-[var(--color-accent-text)] underline" href={`#${anchor(i + 1)}`}>
              {title}
            </a>
          </li>
        ))}
      </ol>
    </nav>
  )
}

function Section({ n, children }: { n: number; children: React.ReactNode }) {
  const title = sectionTitle(n)
  return (
    <section id={anchor(n)} className="mb-8 scroll-mt-4">
      <h2 className="mb-2 text-lg font-semibold">
        <span className="mr-2 text-[var(--color-fg-muted)]">{n}</span>
        {title}
      </h2>
      {children}
    </section>
  )
}

function Facts({ rows }: { rows: [string, string][] }) {
  return (
    <dl className="grid gap-x-4 gap-y-1 text-sm sm:grid-cols-[max-content_1fr]">
      {rows.map(([k, v]) => (
        <div key={k} className="contents">
          <dt className="text-[var(--color-fg-secondary)]">{k}</dt>
          <dd className="mb-1 sm:mb-0">{v}</dd>
        </div>
      ))}
    </dl>
  )
}

export function Country({ bundle }: { bundle: Bundle }) {
  const { iso } = useParams()
  const c = iso ? bundle.countries[iso.toUpperCase()] : undefined
  if (!c) return <NotFound />

  const p = c.params
  const cap = c.capacity
  const phase1 = c.phases[0]
  const recorded = c.national_data.filter(e => e.status !== 'unrecorded').length

  return (
    <article>
      <h1 className="mb-1 text-2xl font-semibold">{c.name}</h1>
      <p className="mb-6 max-w-3xl text-[var(--color-fg-secondary)]">
        Sovereign government data centre network — capacity, legal posture, provider landscape and
        migration path.
      </p>

      <Contents />

      <Section n={1}>
        <Facts
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

      <Section n={2}>
        <ul className="list-disc space-y-2 pl-5 text-sm text-[var(--color-fg-secondary)]">
          {c.structural_differences.map((d, i) => (
            <li key={i}>{d.replace(/\*\*/g, '')}</li>
          ))}
        </ul>
      </Section>

      <Section n={3}>
        <Facts
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

      <Section n={4}>
        <div className="scroll-x">
          <table className="w-full border-collapse text-xs">
            <thead>
              <tr className="border-b border-[var(--color-border)] text-left">
                <th scope="col" className="p-1">
                  Region
                </th>
                <th scope="col" className="p-1">
                  Role
                </th>
                <th scope="col" className="p-1 text-right">
                  Share
                </th>
                <th scope="col" className="p-1 text-right">
                  MW
                </th>
                <th scope="col" className="p-1">
                  Notes
                </th>
              </tr>
            </thead>
            <tbody>
              {c.regions.map(r => (
                <tr key={r.Region} className="border-b border-[var(--color-border)]">
                  <th scope="row" className="p-1 text-left font-normal">
                    {r.Region}
                  </th>
                  <td className="p-1 text-[var(--color-fg-secondary)]">{r.Role}</td>
                  <td className="p-1 text-right tabular-nums">{pct(r['Share of design load'])}</td>
                  <td className="p-1 text-right tabular-nums">{r['Design MW'].toFixed(1)}</td>
                  <td className="p-1 text-[var(--color-fg-muted)]">{r.Notes}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="mt-2 text-xs italic text-[var(--color-fg-secondary)]">
          First-pass geographic hypotheses encoding only the obvious constraints, to be replaced by
          scored site selection.
        </p>
      </Section>

      <Section n={5}>
        <Facts
          rows={[
            ['Governing instrument', p['legal_instrument'] ?? '—'],
            ['Cloud certification', p['certification_scheme'] ?? '—'],
            ['Data classification', p['data_classification'] ?? '—'],
            ['Procurement route', p['procurement_vehicle'] ?? '—'],
          ]}
        />
        <p className="mt-3 text-sm text-[var(--color-fg-secondary)]">
          <strong className="text-[var(--color-fg-primary)]">Foreign jurisdiction exposure.</strong>{' '}
          {p['hyperscaler_gov_exposure']}
        </p>
        <p className="mt-2 text-sm text-[var(--color-fg-muted)]">
          Under the US CLOUD Act and FISA 702 a provider subject to US jurisdiction can face a
          lawful order for data it holds regardless of where that data sits. Residency is necessary
          but not sufficient; what matters is who holds the keys and who can be compelled.
        </p>
      </Section>

      <Section n={6}>
        <Facts
          rows={[
            ['Government cloud', p['sovereign_cloud_initiative'] ?? '—'],
            ['Maturity', p['gov_cloud_maturity'] ?? '—'],
            ['Digital identity', p['digital_id'] ?? '—'],
            ['Interconnection', p['ixp'] ?? '—'],
          ]}
        />
      </Section>

      <Section n={7}>
        <div className="scroll-x">
          <table className="w-full border-collapse text-xs">
            <thead>
              <tr className="border-b border-[var(--color-border)] text-left">
                <th scope="col" className="p-1">
                  Phase
                </th>
                <th scope="col" className="p-1">
                  Scope
                </th>
                <th scope="col" className="p-1 text-right">
                  MW
                </th>
                <th scope="col" className="p-1 text-right">
                  CAPEX
                </th>
                <th scope="col" className="p-1 text-right">
                  Cumulative
                </th>
                <th scope="col" className="p-1">
                  Hybrid
                </th>
              </tr>
            </thead>
            <tbody>
              {c.phases.map(ph => (
                <tr key={ph.Phase} className="border-b border-[var(--color-border)]">
                  <th scope="row" className="p-1 text-left font-normal">
                    {ph.Phase}
                  </th>
                  <td className="p-1">{ph['Phase name']}</td>
                  <td className="p-1 text-right tabular-nums">{ph['Design MW'].toFixed(1)}</td>
                  <td className="p-1 text-right tabular-nums">{eur(ph['CAPEX (EUR mm)'])}</td>
                  <td className="p-1 text-right tabular-nums">
                    {ph['Cumulative CAPEX %'].toFixed(0)}%
                  </td>
                  <td className="p-1 text-[var(--color-fg-secondary)]">{ph['Hybrid eligible']}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {phase1 ? (
          <p className="mt-3 text-sm text-[var(--color-fg-secondary)]">
            Phase 1 is the number that matters: <strong>{eur(phase1['CAPEX (EUR mm)'])}</strong> for{' '}
            {phase1['Design MW'].toFixed(1)} MW, {phase1['Cumulative CAPEX %'].toFixed(0)}% of total
            CAPEX. That is the floor below which no hybrid arrangement helps — and it is a small
            fraction of the full build.
          </p>
        ) : null}
      </Section>

      <Section n={8}>
        <p className="text-sm text-[var(--color-fg-secondary)]">{p['threat_notes']}</p>
      </Section>

      <Section n={9}>
        <p className="mb-3 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
          What the platform would <em>hold</em>, tiered by consequence of loss rather than by
          department. Tier 0 is the identity spine; tier 1 is the enforceable relationship between
          citizen and state.{' '}
          <strong>
            {recorded} of {c.national_data.length} record classes recorded.
          </strong>
        </p>
        <div className="scroll-x">
          <table className="w-full border-collapse text-sm">
            <caption className="sr-only">
              Tier 0 and Tier 1 record classes for {c.name}, with the official page describing each
              register
            </caption>
            <thead>
              <tr className="border-b border-[var(--color-border)] text-left">
                <th scope="col" className="p-2">
                  Tier
                </th>
                <th scope="col" className="p-2">
                  Record class
                </th>
                <th scope="col" className="p-2">
                  Register
                </th>
                <th scope="col" className="p-2">
                  Official description
                </th>
              </tr>
            </thead>
            <tbody>
              {c.national_data.map(e => (
                <tr key={e.record_class} className="border-b border-[var(--color-border)]">
                  <td className="p-2 tabular-nums">{e.tier}</td>
                  <th scope="row" className="p-2 text-left font-normal">
                    {e.label}
                  </th>
                  <td className="p-2">
                    {e.status === 'held' ? (
                      e.register
                    ) : e.status === 'not_held' ? (
                      <em>no central register</em>
                    ) : (
                      /* Words, not a dash and not colour alone: a blank must not read as a
                         finding, and WCAG 1.4.1 forbids encoding this by styling only. */
                      <em className="text-[var(--color-fg-muted)]">not yet recorded</em>
                    )}
                  </td>
                  <td className="p-2">
                    {e.url ? (
                      <a
                        className="text-[var(--color-accent-text)] underline"
                        href={e.url}
                        rel="noreferrer"
                        target="_blank"
                      >
                        {e.publisher}
                      </a>
                    ) : (
                      ''
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="mt-3 max-w-3xl text-xs text-[var(--color-fg-muted)]">
          {bundle.national_data_note}
        </p>
      </Section>
    </article>
  )
}
