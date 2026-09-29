import type { GroupId } from '@/data/types'

/** Group colours from the design tokens (#76, #77); never the only cue for a group. */
export const GROUP_FILL: Record<GroupId, string> = {
  law_and_practice: 'var(--color-rank-1)',
  practice_only: 'var(--color-rank-2)',
  law_only: 'var(--color-rank-3)',
  not_demonstrated: 'var(--color-rank-4)',
  dependent: 'var(--color-rank-5)',
}
