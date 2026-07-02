import { useEffect, useRef } from 'react'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

/** Banda tipográfica gigante en marquee REACTIVO a la velocidad del scroll:
 *  acelera, cambia de dirección y se inclina (skew) según el scroll — firma de
 *  sitios premium. Fallback CSS si hay prefers-reduced-motion. */
const WORDS = [
  'Ingeniería eléctrica',
  'Data centers',
  'Energía crítica',
  'Continuidad 24/7',
  'Llave en mano',
]

export function BigBand({ invert = false }: { invert?: boolean }) {
  const bandRef = useRef<HTMLDivElement>(null)
  const trackRef = useRef<HTMLDivElement>(null)
  const seq = [...WORDS, ...WORDS]

  useEffect(() => {
    const band = bandRef.current
    const track = trackRef.current
    if (!band || !track) return
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return

    band.classList.add('js') // desactiva el marquee CSS; lo maneja GSAP
    const ctx = gsap.context(() => {
      const loop = gsap.to(track, { xPercent: -50, duration: 28, ease: 'none', repeat: -1 })
      const skewTo = gsap.quickTo(track, 'skewX', { duration: 0.5, ease: 'power3' })
      let resetTimer: number | undefined

      ScrollTrigger.create({
        trigger: band,
        start: 'top bottom',
        end: 'bottom top',
        onUpdate: (self) => {
          const v = self.getVelocity()
          // dirección + velocidad desde el scroll (clamp para no enloquecer)
          loop.timeScale(gsap.utils.clamp(-8, 8, 1 + v / 220))
          // inclinación proporcional a la velocidad
          skewTo(gsap.utils.clamp(-9, 9, v / -260))
          // al detenerse, regresa suave a la velocidad/skew base
          window.clearTimeout(resetTimer)
          resetTimer = window.setTimeout(() => {
            gsap.to(loop, { timeScale: 1, duration: 0.8, ease: 'power2.out' })
            skewTo(0)
          }, 120)
        },
      })
    }, band)

    return () => ctx.revert()
  }, [])

  return (
    <div className={`bigband ${invert ? 'invert' : ''}`} aria-hidden="true" ref={bandRef}>
      <div className="bigtrack" ref={trackRef}>
        {seq.map((w, i) => (
          <span className="bigword" key={i}>
            {i % WORDS.length === 0 ? <span className="fill">{w}</span> : w}
          </span>
        ))}
      </div>
    </div>
  )
}
