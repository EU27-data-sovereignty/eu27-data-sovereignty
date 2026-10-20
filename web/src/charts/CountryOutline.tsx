import { geoArea, geoAzimuthalEqualArea, geoCentroid, geoDistance, geoPath } from 'd3'
import { useId, useMemo } from 'react'
import type { Polygon, Position } from 'geojson'

import type { Shape } from './euShapes'

const W = 112
const H = 96

/**
 * A state's main landmass and the islands near it. Distant ones (Madeira, the Azores) would shrink the outline
 * to a speck, so a polygon more than ~8 degrees from the largest one is left out of the drawing.
 */
function mainland(f: Shape): Shape {
  if (f.geometry.type === 'Polygon') return f
  const polys = f.geometry.coordinates.map(
    c => ({ type: 'Polygon', coordinates: c as Position[][] }) as Polygon,
  )
  const largest = polys.reduce((a, b) => (geoArea(b) > geoArea(a) ? b : a))
  const centre = geoCentroid(largest)
  const near = polys.filter(p => geoDistance(geoCentroid(p), centre) < (8 * Math.PI) / 180)
  return { ...f, geometry: { type: 'MultiPolygon', coordinates: near.map(p => p.coordinates) } }
}

/**
 * A member state's outline, filled from the bottom to the share of its holdings with a verified source. The fill
 * is a level, not an area: the number beside it is the reading, and the outline only makes the card the
 * state's. Until the geometry has loaded, an empty box of the same size holds the card's layout.
 */
export function CountryOutline({
  shape,
  value,
  max,
}: {
  shape: Shape | undefined
  value: number
  max: number
}) {
  // useId's value has characters a url(#…) reference cannot carry.
  const clip = `outline-${useId().replace(/[^A-Za-z0-9_-]/g, '')}`
  const drawn = useMemo(() => {
    if (!shape) return null
    const land = mainland(shape)
    const [lon, lat] = geoCentroid(land)
    const projection = geoAzimuthalEqualArea()
      .rotate([-lon, -lat])
      .fitExtent(
        [
          [2, 2],
          [W - 2, H - 2],
        ],
        land,
      )
    const path = geoPath(projection)
    // The level runs over the outline's own height, not the box's: a wide state fills only part of the box.
    const [[, top], [, bottom]] = path.bounds(land)
    return { d: path(land) ?? '', top, bottom }
  }, [shape])

  const pct = max > 0 ? Math.min(1, value / max) : 0
  return (
    <svg viewBox={`0 0 ${W} ${H}`} width={W} height={H} aria-hidden="true" className="shrink-0">
      {drawn ? (
        <>
          <defs>
            <clipPath id={clip}>
              <path d={drawn.d} />
            </clipPath>
          </defs>
          <path d={drawn.d} fill="var(--color-bg-emphasis)" />
          <rect
            x={0}
            y={drawn.bottom - (drawn.bottom - drawn.top) * pct}
            width={W}
            height={(drawn.bottom - drawn.top) * pct}
            fill="var(--color-accent-text)"
            clipPath={`url(#${clip})`}
          />
          <path d={drawn.d} fill="none" stroke="var(--color-baseline)" strokeWidth={1} />
        </>
      ) : null}
    </svg>
  )
}
