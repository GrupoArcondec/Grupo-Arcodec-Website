import { useEffect, useRef } from 'react'
import lottie, { type AnimationItem } from 'lottie-web'
import { pulseAnimation } from '../lib/pulseLottie'

/** Marca animada con Lottie (pulso eléctrico). Decorativa. */
export function LottieMark({ className = '' }: { className?: string }) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const el = ref.current
    if (!el) return
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    let anim: AnimationItem | null = null
    try {
      anim = lottie.loadAnimation({
        container: el,
        renderer: 'svg',
        loop: true,
        autoplay: !reduce,
        animationData: pulseAnimation,
      })
    } catch {
      /* si Lottie falla, el contenedor queda vacío sin romper la página */
    }
    return () => anim?.destroy()
  }, [])

  return <div ref={ref} className={`lottie-mark ${className}`} aria-hidden="true" />
}
