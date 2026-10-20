import { geoAzimuthalEqualArea, geoPath } from 'd3'
import { useMemo } from 'react'

import type { Placement } from '@/data/types'
import { GROUP_FILL } from './groups'
import { ISO_OF, useEuShapes } from './euShapes'

const W = 520
const H = 520

/**
 * A choropleth of the EU-27 by placement group. Colour is never the only cue: each state's
 * group is its accessible name, Low-confidence states are hatched, and the ladder beside the
 * map is the same information as text.
 */
export function EuMap({
  placements,
  labels,
  names,
  selected,
  onSelect,
}: {
  placements: Record<string, Placement>
  labels: Record<string, string>
  names: Record<string, string>
  selected: string | null
  onSelect: (iso: string) => void
}) {
  const shapes = useEuShapes()

  const path = useMemo(() => {
    if (!shapes) return null
    const projection = geoAzimuthalEqualArea()
      .rotate([-10, -52])
      .fitSize([W, H], { type: 'FeatureCollection', features: shapes })
    return geoPath(projection)
  }, [shapes])

  if (!shapes || !path) {
    return <p className="text-sm text-[var(--color-fg-muted)]">Loading the map…</p>
  }

  return (
    <svg
      viewBox={`0 0 ${W} ${H}`}
      role="group"
      aria-label="Map of the EU-27 by data-sovereignty group"
      className="h-auto w-full"
    >
      <defs>
        <pattern id="low-confidence" width="6" height="6" patternUnits="userSpaceOnUse">
          <path d="M0,6 L6,0" stroke="var(--color-fg-muted)" strokeWidth="1" />
        </pattern>
      </defs>
      {shapes.map(f => {
        const iso = ISO_OF[String(f.id)]!
        const p = placements[iso]
        if (!p) return null
        const d = path(f) ?? ''
        const label = `${names[iso]}: ${labels[p.group]}, ${p.confidence} confidence`
        return (
          <g
            key={iso}
            role="button"
            tabIndex={0}
            aria-label={label}
            aria-pressed={selected === iso}
            onClick={() => onSelect(iso)}
            onKeyDown={e => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault()
                onSelect(iso)
              }
            }}
            className="cursor-pointer focus:outline-none"
          >
            <title>{label}</title>
            <path d={d} fill={GROUP_FILL[p.group]} />
            {p.confidence === 'Low' ? <path d={d} fill="url(#low-confidence)" /> : null}
            <path
              d={d}
              fill="none"
              stroke={selected === iso ? 'var(--color-accent)' : 'var(--color-bg-page)'}
              strokeWidth={selected === iso ? 2.5 : 0.8}
            />
          </g>
        )
      })}
    </svg>
  )
}
