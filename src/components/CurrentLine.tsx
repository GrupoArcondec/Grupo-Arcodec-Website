import { useEffect, useRef } from 'react'

/** Riel de "corriente" que recorre el costado y marca el progreso de scroll. */
export function CurrentLine() {
  const fillRef = useRef<HTMLDivElement>(null)
  const sparkRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    let raf = 0
    const update = () => {
      const h = document.documentElement
      const max = h.scrollHeight - h.clientHeight
      const p = max > 0 ? Math.min(window.scrollY / max, 1) : 0
      if (fillRef.current) fillRef.current.style.height = `${p * 100}%`
      if (sparkRef.current) sparkRef.current.style.top = `${p * 100}%`
      raf = 0
    }
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(update)
    }
    update()
    window.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', onScroll)
    return () => {
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onScroll)
      if (raf) cancelAnimationFrame(raf)
    }
  }, [])

  return (
    <div className="currentline" aria-hidden="true">
      <div className="rail" />
      <div className="fill" ref={fillRef} />
      <div className="spark" ref={sparkRef} />
    </div>
  )
}
