import { useEffect, useRef, useState } from 'react'

/** Dispara una sola vez cuando el elemento entra en viewport. */
export function useInView<T extends HTMLElement = HTMLDivElement>(threshold = 0) {
  const ref = useRef<T>(null)
  const [inView, setInView] = useState(false)

  useEffect(() => {
    const el = ref.current
    if (!el) return
    if (typeof IntersectionObserver === 'undefined') {
      setInView(true)
      return
    }
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            setInView(true)
            io.disconnect()
          }
        })
      },
      { threshold, rootMargin: '0px 0px -12% 0px' },
    )
    io.observe(el)

    // Respaldo por geometría: si el elemento ya está en viewport al montar
    // (contenido above-the-fold), lo revelamos aunque el IO no emita el
    // callback inicial. Para contenido bajo el pliegue no hace nada y sigue
    // esperando el scroll vía el observer.
    const revealIfVisible = () => {
      const r = el.getBoundingClientRect()
      if (r.top < window.innerHeight * 0.9 && r.bottom > 0) {
        setInView(true)
        io.disconnect()
      }
    }
    const raf = requestAnimationFrame(revealIfVisible)
    const t = window.setTimeout(revealIfVisible, 350)

    return () => {
      io.disconnect()
      cancelAnimationFrame(raf)
      window.clearTimeout(t)
    }
  }, [threshold])

  return { ref, inView }
}
