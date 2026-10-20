import { useEffect, useId, useRef, useState, type FocusEvent } from 'react'
import { useLocation } from 'react-router-dom'

/**
 * A header disclosure: a button that shows and hides a short list of links. It closes on Escape (focus back
 * on the button), on a click outside, when focus leaves it, and on every route change, because it is open
 * only on the page it was opened on, with no effect needed to reset it. "About the data" and the language
 * switch share it.
 */
export function useDisclosure() {
  const { pathname } = useLocation()
  const [openAt, setOpenAt] = useState<string | null>(null)
  const open = openAt === pathname
  const root = useRef<HTMLDivElement>(null)
  const button = useRef<HTMLButtonElement>(null)
  const panel = useId()

  useEffect(() => {
    if (!open) return
    const outside = (e: PointerEvent) => {
      if (!root.current?.contains(e.target as Node)) setOpenAt(null)
    }
    const escape = (e: KeyboardEvent) => {
      if (e.key !== 'Escape') return
      setOpenAt(null)
      button.current?.focus()
    }
    document.addEventListener('pointerdown', outside)
    document.addEventListener('keydown', escape)
    return () => {
      document.removeEventListener('pointerdown', outside)
      document.removeEventListener('keydown', escape)
    }
  }, [open])

  return {
    open,
    rootProps: {
      ref: root,
      onBlur: (e: FocusEvent) => {
        if (!root.current?.contains(e.relatedTarget as Node | null)) setOpenAt(null)
      },
    },
    buttonProps: {
      ref: button,
      type: 'button' as const,
      'aria-expanded': open,
      'aria-controls': panel,
      onClick: () => setOpenAt(open ? null : pathname),
    },
    panelProps: { id: panel, hidden: !open },
  }
}
