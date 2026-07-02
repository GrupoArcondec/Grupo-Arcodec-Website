import { useEffect, useRef } from 'react'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

/**
 * Scroll-Linked Video — intro cinematográfica al inicio del home.
 * El video se fija (sticky) y su currentTime avanza/retrocede con el scroll (GSAP scrub).
 * Mientras se desplaza, aparecen mensajes por etapas para que el pin tenga propósito.
 *
 * Video en public/videos/scroll-arcondec.mp4 → ruta absoluta /videos/scroll-arcondec.mp4
 */
const SRC = '/videos/scroll-arcondec.mp4'
const SCROLL_LENGTH = 170 // alto de la sección en vh (mayor = scrub más largo)

const CAPS = [
  { k: 'Grupo Arcondec', t: 'Encendemos infraestructura crítica.' },
  { k: 'Ingeniería eléctrica', t: 'Del diseño a la puesta en marcha.' },
  { k: 'Data centers · 24/7', t: 'Energía que no se detiene.' },
]

export function ScrollVideo() {
  const wrapRef = useRef<HTMLDivElement>(null)
  const stageRef = useRef<HTMLDivElement>(null)
  const videoRef = useRef<HTMLVideoElement>(null)
  const barRef = useRef<HTMLSpanElement>(null)
  const capsRef = useRef<HTMLDivElement>(null)
  const hintRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const wrap = wrapRef.current
    const stage = stageRef.current
    const video = videoRef.current
    const bar = barRef.current
    const capsBox = capsRef.current
    if (!wrap || !stage || !video || !capsBox) return

    const caps = Array.from(capsBox.children) as HTMLElement[]
    const setActive = (progress: number) => {
      const idx = Math.min(CAPS.length - 1, Math.floor(progress * CAPS.length))
      caps.forEach((el, i) => el.classList.toggle('active', i === idx))
      if (hintRef.current) hintRef.current.style.opacity = progress > 0.04 ? '0' : '1'
    }
    setActive(0)

    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const isMobile = window.matchMedia('(max-width: 768px), (pointer: coarse)').matches

    if (reduce || isMobile) {
      wrap.classList.add('static')
      wrap.style.height = '100svh'
      video.loop = true
      video.muted = true
      if (!reduce) video.play().catch(() => {})
      return
    }

    let ctx: gsap.Context | null = null

    const build = () => {
      const dur = video.duration
      if (!dur || !isFinite(dur)) return false
      ctx = gsap.context(() => {
        gsap.to(video, {
          currentTime: dur,
          ease: 'none',
          scrollTrigger: {
            trigger: wrap,
            start: 'top top',
            end: 'bottom bottom',
            scrub: 0.4,
            invalidateOnRefresh: true,
            onUpdate: (self) => {
              if (bar) bar.style.transform = `scaleX(${self.progress})`
              setActive(self.progress)
            },
          },
        })
      }, wrap)
      ScrollTrigger.refresh()
      return true
    }

    const prime = () => {
      video.muted = true
      const p = video.play()
      if (p && typeof p.then === 'function') {
        p.then(() => { video.pause(); video.currentTime = 0 }).catch(() => {})
      }
    }

    const onReady = () => {
      prime()
      if (!build()) video.addEventListener('durationchange', () => build(), { once: true })
    }

    if (video.readyState >= 1) onReady()
    else video.addEventListener('loadedmetadata', onReady, { once: true })

    return () => { ctx?.revert() }
  }, [])

  return (
    <section ref={wrapRef} className="svv" style={{ height: `${SCROLL_LENGTH}vh` }}>
      <div ref={stageRef} className="svv-stage">
        <video
          ref={videoRef}
          className="svv-video"
          src={SRC}
          muted
          playsInline
          preload="auto"
          disableRemotePlayback
        />

        <div className="svv-overlay">
          <div className="svv-caps" ref={capsRef}>
            {CAPS.map((c, i) => (
              <div className={`svv-cap ${i === 0 ? 'active' : ''}`} key={c.t}>
                <span className="eyebrow">{c.k}</span>
                <h2 className="svv-title">{c.t}</h2>
              </div>
            ))}
          </div>
          <div className="svv-progress" aria-hidden="true">
            <span ref={barRef} />
          </div>
        </div>

        <div className="svv-hint" ref={hintRef} aria-hidden="true">
          <span>Desplázate</span>
          <i />
        </div>
      </div>
    </section>
  )
}
