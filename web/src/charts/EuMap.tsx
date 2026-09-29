import { geoAzimuthalEqualArea, geoPath } from 'd3'
import { useEffect, useMemo, useState } from 'react'
import { feature } from 'topojson-client'
import type { Feature, FeatureCollection, MultiPolygon, Polygon } from 'geojson'
import type { GeometryCollection, Topology } from 'topojson-specification'

import type { Placement } from '@/data/types'
import { GROUP_FILL } from './groups'

/** ISO 3166-1 numeric ids used by world-atlas, for the EU-27 (Greece is EL in EU usage). */
const NUMERIC: Record<string, string> = {
  AT: '040',
  BE: '056',
  BG: '100',
  HR: '191',
  CY: '196',
  CZ: '203',
  DK: '208',
  EE: '233',
  FI: '246',
  FR: '250',
  DE: '276',
  EL: '300',
  HU: '348',
  IE: '372',
  IT: '380',
  LV: '428',
  LT: '440',
  LU: '442',
  MT: '470',
  NL: '528',
  PL: '616',
  PT: '620',
  RO: '642',
  SK: '703',
  SI: '705',
  ES: '724',
  SE: '752',
}
const ISO_OF = Object.fromEntries(Object.entries(NUMERIC).map(([iso, n]) => [n, iso]))

type Shape = Feature<Polygon | MultiPolygon, { name: string }>

/** Keep only the polygons inside a European frame, so overseas territories do not shrink the map. */
function european(f: Shape): Shape {
  const inFrame = (ring: number[][]) =>
    ring.every(([lon, lat]) => lon! > -25 && lon! < 45 && lat! > 34 && lat! < 72)
  if (f.geometry.type === 'Polygon') return f
  const polys = f.geometry.coordinates.filter(p => p[0] && inFrame(p[0] as number[][]))
  return { ...f, geometry: { type: 'MultiPolygon', coordinates: polys } }
}

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
  const [shapes, setShapes] = useState<Shape[] | null>(null)

  useEffect(() => {
    let live = true
    // Loaded only on this page: ~740 KB raw, split into its own chunk by Vite.
    import('world-atlas/countries-50m.json').then(mod => {
      const topo = mod.default as unknown as Topology<{ countries: GeometryCollection }>
      const all = feature(topo, topo.objects.countries) as FeatureCollection<
        Polygon | MultiPolygon,
        { name: string }
      >
      const eu = all.features.filter(f => ISO_OF[String(f.id)]).map(european)
      if (live) setShapes(eu)
    })
    return () => {
      live = false
    }
  }, [])

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
              stroke={selected === iso ? 'var(--color-highlight)' : 'var(--color-bg-page)'}
              strokeWidth={selected === iso ? 2.5 : 0.8}
            />
          </g>
        )
      })}
    </svg>
  )
}
