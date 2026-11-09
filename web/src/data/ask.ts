import { m } from '@/i18n'

/** What the Ask box accepts and suggests, shared by the front page and the Ask page (#78, #101). */

/** The longest question the answering function takes. */
export const ASK_MAX = 500

/** Questions the sourced findings can answer, offered as starting points. Marked for the site catalog (#113): render with tx. */
export const ASK_EXAMPLES = [
  m('Which member states have a law keeping government data under national jurisdiction?'),
  m('Who operates Germany’s population register, and under which law?'),
  m('Which holdings are still unverified for Estonia?'),
  m('How does the data-sovereignty ranking work, and how confident is it?'),
  m('Is it known where Belgium’s critical registers are hosted?'),
  m('What does "not demonstrated" mean in the ranking?'),
]
