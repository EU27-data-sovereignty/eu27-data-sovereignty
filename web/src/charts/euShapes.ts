import { useEffect, useState } from 'react'
import { feature } from 'topojson-client'
import type { Feature, FeatureCollection, MultiPolygon, Polygon } from 'geojson'
import type { GeometryCollection, Topology } from 'topojson-specification'

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
export const ISO_OF: Record<string, string> = Object.fromEntries(
  Object.entries(NUMERIC).map(([iso, n]) => [n, iso]),
)

export type Shape = Feature<Polygon | MultiPolygon, { name: string }>

/** Keep only the polygons inside a European frame, so overseas territories do not shrink the map. */
function european(f: Shape): Shape {
  const inFrame = (ring: number[][]) =>
    ring.every(([lon, lat]) => lon! > -25 && lon! < 45 && lat! > 34 && lat! < 72)
  if (f.geometry.type === 'Polygon') return f
  const polys = f.geometry.coordinates.filter(p => p[0] && inFrame(p[0] as number[][]))
  return { ...f, geometry: { type: 'MultiPolygon', coordinates: polys } }
}

// One load for every caller: the Ranking map and the 27 country cards share the same ~740 KB chunk.
let pending: Promise<Shape[]> | null = null
function load(): Promise<Shape[]> {
  pending ??= import('world-atlas/countries-50m.json').then(mod => {
    const topo = mod.default as unknown as Topology<{ countries: GeometryCollection }>
    const all = feature(topo, topo.objects.countries) as FeatureCollection<
      Polygon | MultiPolygon,
      { name: string }
    >
    return all.features.filter(f => ISO_OF[String(f.id)]).map(european)
  })
  return pending
}

/** The EU-27's outlines, or null until the geometry chunk has loaded. */
export function useEuShapes(): Shape[] | null {
  const [shapes, setShapes] = useState<Shape[] | null>(null)
  useEffect(() => {
    let live = true
    void load().then(s => {
      if (live) setShapes(s)
    })
    return () => {
      live = false
    }
  }, [])
  return shapes
}
