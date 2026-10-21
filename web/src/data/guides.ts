import { m } from '@/i18n'
import type { FigureId } from './guideFigures'

/**
 * The twelve guide pages behind the front page's selector (#102): six audiences ("I am…") and six tasks
 * ("I need to…"). A guide is this project's own advice on using the site, drafted from the requester's
 * note on use cases for decision makers. It states no finding: every figure on a guide is counted from
 * the bundle (guideFigures.ts), and every step links to the page where the sourced facts are. Claims in
 * that note that no checked source supports were left out.
 */

/** A section of a country report a link opens at, once a state is chosen on Countries. */
export type ReportSection = 'exposure' | 'holdings' | 'gaps'

export interface GuideLink {
  label: string
  /** A route in the app, or a file such as the report PDF. */
  to: string
  section?: ReportSection
}

export interface Guide {
  slug: string
  /**
   * The button's label, one string so it is translated whole; a newline marks where a wide screen breaks it.
   */
  label: string
  title: string
  lede: string
  /** Situations in which a reader comes to the site; audiences only. */
  when?: string[]
  steps: { title: string; text: string; link: GuideLink }[]
  takeaways?: string[]
  /** What the site does not offer yet for this reader or task. */
  missing: string[]
  figures: FigureId[]
  /** Slugs of the guides of the other kind that go with this one. */
  related: string[]
}

const COUNTRIES = '/countries'
const HOLDINGS = '/holdings'
const HOSTING = '/infrastructure'
const INDICATORS = '/sovereignty#indicators'
const SOURCES = '/sources'
const PRIORITY_RULE = '/methodology#m-calculations'

const MACHINE_ONLY = m(
  'Review by a person. Every finding here is machine-checked only, which limits how it can be cited in formal documents.',
)

export const AUDIENCE_GUIDES: Guide[] = [
  {
    slug: 'ministries',
    label: m('Ministries &\ngovernment CIOs'),
    title: m('For digital ministries and government CIOs'),
    lede: m(
      'You are asked to act on sovereignty without a baseline. Inventories sit in different ministries, and it is hard to say quickly what runs where. This site is an outside baseline: what a checked public source says about each of your state’s critical holdings, and where no source has been found.',
    ),
    when: [
      m('A minister asks “are we exposed?”'),
      m('A national cloud strategy is being drafted or renewed.'),
      m('A major cloud contract is up for renewal.'),
      m('A peer state announces a sovereign cloud and the press asks “why not us?”'),
    ],
    steps: [
      {
        title: m('Open your country report'),
        text: m(
          'See which holding classes have a checked source, which have documented hosting and which are gaps.',
        ),
        link: { label: m('Choose a country'), to: COUNTRIES },
      },
      {
        title: m('Read the holdings in priority order'),
        text: m(
          'Each report lists its holdings by a published score: consequence of loss, difficulty of rebuilding and known exposure to non-EU providers.',
        ),
        link: { label: m('Open a report at its holdings'), to: COUNTRIES, section: 'holdings' },
      },
      {
        title: m('See how other states host the same register'),
        text: m('Pick one kind of holding and read it across all 27 member states.'),
        link: { label: m('Compare a holding'), to: HOLDINGS },
      },
      {
        title: m('Take the country PDF into a briefing'),
        text: m(
          'Every country has its own report as a PDF, with footnoted sources and a source appendix.',
        ),
        link: { label: m('Find your country’s PDF'), to: COUNTRIES },
      },
    ],
    takeaways: [
      m('A baseline you did not have to commission, with every fact linked to its source.'),
      m(
        'An order of work you can explain: the priority score is published, and so is each of its inputs.',
      ),
      m(
        'Precedents: how other member states host the same register, in the words of their own sources.',
      ),
      m(
        'A view of where your gap lies. If government data centres are sourced but a jurisdiction requirement is not, the open work is a statute and documentation rather than buildings.',
      ),
    ],
    missing: [
      m('A “top ten priority holdings” view per country.'),
      m('A one-page country brief for decision makers.'),
      MACHINE_ONLY,
    ],
    figures: ['holdingsVerified', 'tier0Hosting', 'dataCentres', 'jurisdictionLaw'],
    related: ['exposure', 'migrate', 'compare'],
  },
  {
    slug: 'procurement',
    label: m('Procurement &\ncloud strategy'),
    title: m('For procurement and cloud-strategy leads'),
    lede: m(
      'A tender that says “data in an EU region” describes where servers sit. It does not say whose law the provider answers to. You need criteria you can cite when a losing bidder challenges the award.',
    ),
    when: [
      m('You are drafting tender specifications.'),
      m('You are evaluating bids.'),
      m('A supplier describes its offer as a “sovereign cloud”.'),
    ],
    steps: [
      {
        title: m('Read the indicator definitions'),
        text: m(
          'Seven indicators, each a precise question: a jurisdiction requirement, a certification that requires immunity from non-EU law, a state-controlled trust anchor and eID, among others.',
        ),
        link: { label: m('Open the indicators'), to: INDICATORS },
      },
      {
        title: m('See what other states have put in law'),
        text: m(
          'The same grid shows, state by state, which indicators a checked source supports, with the legal text quoted.',
        ),
        link: { label: m('Read the grid'), to: INDICATORS },
      },
      {
        title: m('See which operators peers use'),
        text: m(
          'The hosting overview names the operator and the hosting a source states for comparable holdings.',
        ),
        link: { label: m('Open hosting'), to: HOSTING },
      },
      {
        title: m('Trace a criterion to its source'),
        text: m(
          'Each source is listed with its quote in the original language, a document hash and an archived copy.',
        ),
        link: { label: m('Search the sources'), to: SOURCES },
      },
    ],
    takeaways: [
      m('Criteria you can cite rather than invent.'),
      m(
        'A way to tell an offer’s server location from its jurisdiction: the indicators ask about law and control, not region.',
      ),
    ],
    missing: [m('Copy-ready tender clauses mapped to the indicators.'), MACHINE_ONLY],
    figures: ['jurisdictionLaw', 'certification', 'statesWithHosting'],
    related: ['tender', 'compare'],
  },
  {
    slug: 'parliaments',
    label: m('Parliaments &\naudit courts'),
    title: m('For parliaments, audit courts and data-protection authorities'),
    lede: m(
      'Oversight needs visibility. It is hard to ask a precise question about where a register is hosted when nothing public says where it is. Here every missing source is shown as a gap, so the question writes itself.',
    ),
    when: [
      m('Budget scrutiny of IT spending.'),
      m('An audit of a digitalisation programme.'),
      m('A parliamentary question after a news story about cloud contracts.'),
    ],
    steps: [
      {
        title: m('Find the gaps in your country’s report'),
        text: m(
          'Every value no checked source supports is listed as open research. Each can be put as a written question: will the government publish a source stating where this register is hosted?',
        ),
        link: { label: m('Open a report at its gaps'), to: COUNTRIES, section: 'gaps' },
      },
      {
        title: m('Cite the source when a fact is contested'),
        text: m('Each fact rests on a quoted passage from a hashed, archived document.'),
        link: { label: m('Search the sources'), to: SOURCES },
      },
      {
        title: m('Compare with peer states'),
        text: m('See what other member states have documented for the same holding.'),
        link: { label: m('Compare a holding'), to: HOLDINGS },
      },
      {
        title: m('See how each fact was checked'),
        text: m(
          'Every printed fact was checked by a second model, and the verdicts are published.',
        ),
        link: { label: m('Open the fact check'), to: '/fact-check' },
      },
    ],
    takeaways: [
      m('Questions grounded in sources rather than speculation.'),
      m('A clear burden of proof: on this site a gap means “not demonstrated”, never “sovereign”.'),
      m('Peer evidence: what other states have documented for the same holding.'),
    ],
    missing: [m('An export that drafts each gap as a written question.'), MACHINE_ONLY],
    figures: ['gaps', 'sources', 'lowConfidence'],
    related: ['questions', 'exposure', 'compare'],
  },
  {
    slug: 'cyber',
    label: m('Cyber agencies\n& CISOs'),
    title: m('For national cyber agencies and CISOs'),
    lede: m(
      'You are responsible for resilience, often without a view of where critical registers sit, physically and legally. A threat model built for technical attacks may not cover a provider being ordered to suspend service.',
    ),
    when: [
      m('NIS2 implementation.'),
      m('A national risk assessment.'),
      m('Crisis-scenario planning: what happens if a provider is ordered to suspend service.'),
    ],
    steps: [
      {
        title: m('See what a source says about hosting'),
        text: m(
          'The hosting overview shows which holdings are documented on national infrastructure, with an EU provider or on mixed hosting, and which have no stated hosting.',
        ),
        link: { label: m('Open hosting'), to: HOSTING },
      },
      {
        title: m('List what would be hard to rebuild'),
        text: m(
          'The priority score counts difficulty of rebuilding. Holdings that rank high with hosting not stated make a ready scenario list.',
        ),
        link: { label: m('Open a report at its holdings'), to: COUNTRIES, section: 'holdings' },
      },
      {
        title: m('Check the trust anchor and the eID'),
        text: m(
          'Two indicators ask whether the state controls its trust anchor and its national eID. Digital services downstream depend on both.',
        ),
        link: { label: m('Open the indicators'), to: INDICATORS },
      },
      {
        title: m('Take in the whole scope'),
        text: m(
          'Identity, tax, justice, grid control, emergency calls: the holding classes span the sectors an all-hazards assessment covers.',
        ),
        link: { label: m('Browse the holding classes'), to: HOLDINGS },
      },
    ],
    takeaways: [
      m('A cross-sector map for an all-hazards assessment.'),
      m(
        'A risk class with sources behind it: jurisdictional exposure, where a holding is documented on infrastructure outside national control.',
      ),
    ],
    missing: [
      m('A filter that combines low recoverability with unknown or non-EU hosting.'),
      MACHINE_ONLY,
    ],
    figures: ['lowRecoverability', 'tier0Hosting', 'trustAnchor', 'eid'],
    related: ['cut-off', 'exposure'],
  },
  {
    slug: 'eu-institutions',
    label: m('EU institutions'),
    title: m('For EU institutions'),
    lede: m(
      'Twenty-seven national pictures that do not line up, and no shared taxonomy for “critical government data”. This site puts all 27 member states on one footing: the same holding classes, the same indicators, the same rule for what counts as evidence.',
    ),
    when: [
      m('Drafting or amending cloud, cybersecurity or data legislation.'),
      m('Revisiting the EU cloud certification scheme.'),
      m('Designing funding programmes for sovereign infrastructure.'),
    ],
    steps: [
      {
        title: m('Use the taxonomy'),
        text: m(
          'The holding classes and their tiers are the same for every state: a candidate common taxonomy.',
        ),
        link: { label: m('Browse the holding classes'), to: HOLDINGS },
      },
      {
        title: m('Read the indicator distribution'),
        text: m(
          'The grid shows, for each legal and practical safeguard, how many states have it sourced.',
        ),
        link: { label: m('Open the indicators'), to: INDICATORS },
      },
      {
        title: m('Reproduce it'),
        text: m(
          'The data and the code are open. The methodology says how every number is counted and how to rebuild every output.',
        ),
        link: { label: m('Read the methodology'), to: '/methodology#m-reproduce' },
      },
      {
        title: m('Read all 27 in one document'),
        text: m(
          'The EU-27 report has a chapter per member state, with footnoted sources and a source appendix.',
        ),
        link: { label: m('Open the EU-27 report (PDF)'), to: '/eu27-report.pdf' },
      },
    ],
    takeaways: [
      m('A baseline for an impact assessment that others can reproduce.'),
      m(
        'Evidence, indicator by indicator, of how far member states have documented each safeguard on their own.',
      ),
    ],
    missing: [MACHINE_ONLY],
    figures: ['holdingClasses', 'jurisdictionLaw', 'certification'],
    related: ['compare', 'tender'],
  },
  {
    slug: 'operators',
    label: m('Operators\ninvestors & press'),
    title: m('For operators, investors and the press'),
    lede: m(
      'For sovereign cloud and data-centre operators and their investors, the gaps show where documented national or EU hosting is missing. For journalists and NGOs, every claim links to a quote and an archived copy, so it can be reported from.',
    ),
    when: [
      m('Sizing demand for sovereign hosting.'),
      m('Checking a claim before publishing it.'),
      m('Following a procurement story.'),
    ],
    steps: [
      {
        title: m('See where hosting is undocumented'),
        text: m(
          'The hosting overview lists every holding whose hosting a source states. What is not listed has no sourced hosting yet.',
        ),
        link: { label: m('Open hosting'), to: HOSTING },
      },
      {
        title: m('See who operates what'),
        text: m(
          'For each kind of holding, read each state’s register and its operator side by side.',
        ),
        link: { label: m('Compare a holding'), to: HOLDINGS },
      },
      {
        title: m('Check a claim at its source'),
        text: m(
          'Search by publisher, country or quoted text. Each entry carries the quote, a document hash and an archived copy.',
        ),
        link: { label: m('Search the sources'), to: SOURCES },
      },
      {
        title: m('Ask in your own words'),
        text: m(
          'The Ask box answers only from the sourced findings, with a citation for every fact.',
        ),
        link: { label: m('Ask a question'), to: '/ask' },
      },
    ],
    takeaways: [
      m('A view of which top-tier holdings have no documented national or EU hosting.'),
      m('Facts you can report from: quoted in the original language, hashed and archived.'),
    ],
    missing: [MACHINE_ONLY],
    figures: ['tier0Hosting', 'statesWithHosting', 'sources'],
    related: ['compare', 'cut-off'],
  },
]

export const TASK_GUIDES: Guide[] = [
  {
    slug: 'exposure',
    label: m('Check my country’s\nexposure'),
    title: m('Check my country’s exposure'),
    lede: m(
      'Your country’s report shows, for each critical holding, whether a checked source says where it runs: on national infrastructure, with an EU provider, on mixed hosting, or not stated. Silence counts as not stated, never as national.',
    ),
    steps: [
      {
        title: m('Choose your country'),
        text: m(
          'Its report opens at the exposure table, which counts verified holdings by where their source says the infrastructure runs.',
        ),
        link: { label: m('Choose a country'), to: COUNTRIES, section: 'exposure' },
      },
      {
        title: m('Open the holdings behind a count'),
        text: m(
          'The holdings table names each register, its operator and its hosting, each with its footnote.',
        ),
        link: { label: m('Open a report at its holdings'), to: COUNTRIES, section: 'holdings' },
      },
      {
        title: m('Read your state’s placement'),
        text: m(
          'The ranking places each state in a group by a published rule, and says how far open evidence could still move it.',
        ),
        link: { label: m('Open the ranking'), to: '/sovereignty' },
      },
    ],
    missing: [m('A one-page brief per country.')],
    figures: ['tier0Hosting', 'notNational', 'lowConfidence'],
    related: ['ministries', 'parliaments', 'cyber'],
  },
  {
    slug: 'migrate',
    label: m('Decide what to\nmigrate first'),
    title: m('Decide what to migrate first'),
    lede: m(
      'The site does not tell a state what to do. It does publish a priority score for every holding, and each input to it, so an order of work can be argued from evidence.',
    ),
    steps: [
      {
        title: m('Read the priority rule'),
        text: m(
          'The score adds three inputs: consequence of loss, difficulty of rebuilding and known exposure to non-EU providers.',
        ),
        link: { label: m('Read the rule'), to: PRIORITY_RULE },
      },
      {
        title: m('Open your country’s holdings by priority'),
        text: m(
          'Each report lists its holdings from the highest priority down, with what a source says about each.',
        ),
        link: { label: m('Open a report at its holdings'), to: COUNTRIES, section: 'holdings' },
      },
      {
        title: m('See how peers host the top items'),
        text: m('For any holding class, read how the other member states host it.'),
        link: { label: m('Compare a holding'), to: HOLDINGS },
      },
    ],
    missing: [m('A “top ten priority holdings” view per country.')],
    figures: ['lowRecoverability', 'tier0Hosting'],
    related: ['ministries', 'cyber'],
  },
  {
    slug: 'tender',
    label: m('Write tender criteria\nthat hold up'),
    title: m('Write tender criteria that hold up'),
    lede: m(
      'An award criterion is easier to defend when it can be cited. The ranking’s indicators are precise questions about jurisdiction, certification and control, answered state by state with the legal text quoted.',
    ),
    steps: [
      {
        title: m('Read the seven indicators'),
        text: m('Hover over a column heading for the exact question each indicator asks.'),
        link: { label: m('Open the indicators'), to: INDICATORS },
      },
      {
        title: m('Open the legal text behind a “Yes”'),
        text: m(
          'Each finding carries a footnote to its source: the statute or scheme, quoted in the original language.',
        ),
        link: { label: m('Search the sources'), to: SOURCES },
      },
      {
        title: m('See which operators peers chose'),
        text: m('The hosting overview names operators and hosting for comparable holdings.'),
        link: { label: m('Open hosting'), to: HOSTING },
      },
    ],
    missing: [m('Copy-ready tender clauses mapped to the indicators.')],
    figures: ['jurisdictionLaw', 'certification', 'trustAnchor'],
    related: ['procurement', 'eu-institutions'],
  },
  {
    slug: 'questions',
    label: m('Turn gaps into\nformal questions'),
    title: m('Turn gaps into formal questions'),
    lede: m(
      'Every value that no checked source supports is shown as a gap, and every value the fact check could not confirm is shown as disputed. Each is a question a government can answer by publishing a source.',
    ),
    steps: [
      {
        title: m('Choose your country'),
        text: m(
          'Its report opens at “Research still open”: the list of what no checked source yet states.',
        ),
        link: { label: m('Choose a country'), to: COUNTRIES, section: 'gaps' },
      },
      {
        title: m('Read what is documented next to the gap'),
        text: m(
          'The holdings table shows the gap in context: the register may be sourced while its hosting is not.',
        ),
        link: { label: m('Open a report at its holdings'), to: COUNTRIES, section: 'holdings' },
      },
      {
        title: m('Show that the gap can be closed'),
        text: m('Find a member state that has published a source for the same holding.'),
        link: { label: m('Compare a holding'), to: HOLDINGS },
      },
    ],
    missing: [m('An export that drafts each gap as a written question.')],
    figures: ['gaps', 'lowConfidence'],
    related: ['parliaments'],
  },
  {
    slug: 'compare',
    label: m('Compare how peers\nhost a register'),
    title: m('Compare how peers host a register'),
    lede: m(
      'One taxonomy, 27 member states. Pick a kind of holding and read, side by side, each state’s register, its operator and where a source says it runs.',
    ),
    steps: [
      {
        title: m('Pick a holding class'),
        text: m(
          'Civil registry, tax, land registry, health records and the rest, grouped by tier.',
        ),
        link: { label: m('Browse the holding classes'), to: HOLDINGS },
      },
      {
        title: m('Read the hosting overview'),
        text: m(
          'Every holding whose hosting a source states, by member state, with the operator and the dependency.',
        ),
        link: { label: m('Open hosting'), to: HOSTING },
      },
      {
        title: m('Open a state’s full report'),
        text: m(
          'Each cell in a comparison is taken from that state’s own report, with the same source.',
        ),
        link: { label: m('Choose a country'), to: COUNTRIES },
      },
    ],
    missing: [],
    figures: ['holdingClasses', 'statesWithHosting', 'tier0Hosting'],
    related: ['ministries', 'procurement', 'eu-institutions', 'operators'],
  },
  {
    slug: 'cut-off',
    label: m('Plan for a\nprovider cut-off'),
    title: m('Plan for a provider cut-off'),
    lede: m(
      'What happens if a provider is ordered to suspend service? The hosting overview shows which holdings a source places on national infrastructure, with an EU provider or on mixed hosting, and which have no stated hosting at all.',
    ),
    steps: [
      {
        title: m('Filter hosting by dependency'),
        text: m(
          'Use the cards above the list to show one kind of dependency, and the tier filter to keep to the top tiers.',
        ),
        link: { label: m('Open hosting'), to: HOSTING },
      },
      {
        title: m('Check the trust anchor and the eID'),
        text: m(
          'Two indicators ask whether the state controls its trust anchor and its national eID.',
        ),
        link: { label: m('Open the indicators'), to: INDICATORS },
      },
      {
        title: m('List what is hard to rebuild'),
        text: m('Each report ranks its holdings by a score that counts difficulty of rebuilding.'),
        link: { label: m('Open a report at its holdings'), to: COUNTRIES, section: 'holdings' },
      },
      {
        title: m('Read how exposure is counted'),
        text: m(
          'Only holdings whose source says where the infrastructure runs are counted. Silence is “not stated”.',
        ),
        link: { label: m('Read the rule'), to: PRIORITY_RULE },
      },
    ],
    missing: [m('A filter that combines low recoverability with unknown or non-EU hosting.')],
    figures: ['notNational', 'lowRecoverability', 'trustAnchor'],
    related: ['cyber', 'operators'],
  },
]
