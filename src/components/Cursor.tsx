import { useEffect, useRef } from 'react'

/** Cursor personalizado (punto ámbar + anillo que persigue) y botones magnéticos.
 *  Solo se activa en dispositivos con puntero fino (desktop). */
export function Cursor() {
  const dotRef = useRef<HTMLDivElement>(null)
  const ringRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const dot = dotRef.current
    const ring = ringRef.current
    if (!fine || !dot || !ring) return

    document.body.classList.add('cursor-on')

    let mx = window.innerWidth / 2, my = window.innerHeight / 2
    let rx = mx, ry = my
    let raf = 0

    const move = (e: PointerEvent) => {
      mx = e.clientX; my = e.clientY
      dot.style.transform = `translate(${mx}px,${my}px) translate(-50%,-50%)`
    }
    const loop = () => {
      rx += (mx - rx) * 0.18
      ry += (my - ry) * 0.18
      ring.style.transform = `translate(${rx}px,${ry}px) translate(-50%,-50%)`
      raf = requestAnimationFrame(loop)
    }
    raf = requestAnimationFrame(loop)

    const HOVER = 'a,button,[role="button"],.lg,.gal-item,.proj-card,input,textarea,[data-cursor]'
    const over = (e: PointerEvent) => {
      if ((e.target as HTMLElement).closest?.(HOVER)) ring.classList.add('hover')
    }
    const out = (e: PointerEvent) => {
      if ((e.target as HTMLElement).closest?.(HOVER)) ring.classList.remove('hover')
    }
    const down = () => ring.classList.add('down')
    const up = () => ring.classList.remove('down')

    window.addEventListener('pointermove', move, { passive: true })
    window.addEventListener('pointerover', over, { passive: true })
    window.addEventListener('pointerout', out, { passive: true })
    window.addEventListener('pointerdown', down, { passive: true })
    window.addEventListener('pointerup', up, { passive: true })

    // --- botones magnéticos ---
    const cleanups: Array<() => void> = []
    if (!reduce) {
      const mags = Array.from(document.querySelectorAll<HTMLElement>('.btn'))
      mags.forEach((el) => {
        const onMove = (e: PointerEvent) => {
          const r = el.getBoundingClientRect()
          const dx = e.clientX - (r.left + r.width / 2)
          const dy = e.clientY - (r.top + r.height / 2)
          el.style.transform = `translate(${dx * 0.28}px,${dy * 0.4}px)`
        }
        const onLeave = () => { el.style.transform = '' }
        el.addEventListener('pointermove', onMove)
        el.addEventListener('pointerleave', onLeave)
        cleanups.push(() => {
          el.removeEventListener('pointermove', onMove)
          el.removeEventListener('pointerleave', onLeave)
        })
      })
    }

    return () => {
      cancelAnimationFrame(raf)
      document.body.classList.remove('cursor-on')
      window.removeEventListener('pointermove', move)
      window.removeEventListener('pointerover', over)
      window.removeEventListener('pointerout', out)
      window.removeEventListener('pointerdown', down)
      window.removeEventListener('pointerup', up)
      cleanups.forEach((c) => c())
    }
  }, [])

  return (
    <>
      <div className="cursor-ring" ref={ringRef} aria-hidden="true" />
      <div className="cursor-dot" ref={dotRef} aria-hidden="true" />
    </>
  )
}
