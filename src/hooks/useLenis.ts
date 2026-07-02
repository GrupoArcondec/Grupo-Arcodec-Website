import { useEffect } from 'react'
import Lenis from 'lenis'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

let lenis: Lenis | null = null

/** Desplaza suavemente a un id (#hash) usando Lenis; fallback nativo. */
export function scrollToId(id: string) {
  const sel = id.startsWith('#') ? id : `#${id}`
  const el = document.querySelector(sel) as HTMLElement | null
  if (!el) return
  if (lenis) lenis.scrollTo(el, { offset: 0 })
  else el.scrollIntoView({ behavior: 'smooth' })
}

/** Salta al tope (cambio de página). */
export function scrollToTop() {
  if (lenis) lenis.scrollTo(0, { immediate: true })
  else window.scrollTo(0, 0)
}

/** Congela/reanuda el scroll suave (p. ej. con el menú móvil abierto). */
export function stopLenis() {
  lenis?.stop()
}
export function startLenis() {
  lenis?.start()
}

/** Scroll suave (Lenis) sincronizado con GSAP ScrollTrigger. */
export function useLenis() {
  useEffect(() => {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduce) return

    lenis = new Lenis({
      lerp: 0.1,               // Editorial usa Lenis con lerp por defecto (0.1)
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 1.5,
    })
    lenis.on('scroll', ScrollTrigger.update)

    const raf = (time: number) => {
      lenis?.raf(time * 1000)
    }
    gsap.ticker.add(raf)
    gsap.ticker.lagSmoothing(0)

    return () => {
      gsap.ticker.remove(raf)
      lenis?.destroy()
      lenis = null
    }
  }, [])
}
