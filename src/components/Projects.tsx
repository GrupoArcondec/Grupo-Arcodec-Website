import { useEffect, useRef, useState } from 'react'
import { ChevronLeft, ChevronRight, Star } from 'lucide-react'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { ClipReveal } from './ClipReveal'
import { PROJECTS, photo } from '../lib/data'

export function Projects() {
  const [idx, setIdx] = useState(0)
  const [paused, setPaused] = useState(false)
  const trackRef = useRef<HTMLDivElement>(null)
  const n = PROJECTS.length

  useEffect(() => {
    if (paused) return
    const id = window.setInterval(() => setIdx((v) => (v + 1) % n), 3000)
    return () => clearInterval(id)
  }, [paused, n])

  // ancho de tarjeta + gap para el desplazamiento
  const step = () => {
    const track = trackRef.current
    if (!track) return 0
    const card = track.querySelector<HTMLElement>('.proj-card')
    if (!card) return 0
    const gap = parseFloat(getComputedStyle(track).gap || '22')
    return card.offsetWidth + gap
  }
  // desplazamiento limitado: nunca más allá de la última tarjeta que llena el viewport
  const computeOffset = () => {
    const track = trackRef.current
    if (!track) return 0
    const viewport = track.parentElement
    const max = viewport ? Math.max(0, track.scrollWidth - viewport.clientWidth) : 0
    return Math.min(idx * step(), max)
  }
  const [offset, setOffset] = useState(0)
  useEffect(() => {
    setOffset(computeOffset())
    const onResize = () => setOffset(computeOffset())
    window.addEventListener('resize', onResize)
    return () => window.removeEventListener('resize', onResize)
  }, [idx])

  const prev = () => setIdx((v) => (v - 1 + n) % n)
  const next = () => setIdx((v) => (v + 1) % n)

  return (
    <section className="section projects" id="proyectos">
      <div className="wrap">
        <Reveal>
          <div className="proj-head">
            <div className="section-head" style={{ margin: 0 }}>
              <span className="eyebrow">Proyectos</span>
              <RevealText tag="h2" text="Capacidades probadas en obra." accent="en obra." />
            </div>
            <div className="proj-rate">
              <span className="stars">
                {Array.from({ length: 5 }).map((_, i) => (
                  <Star key={i} />
                ))}
              </span>
              30+ años de ejecución
            </div>
          </div>
        </Reveal>

        <div
          className="proj-viewport"
          onMouseEnter={() => setPaused(true)}
          onMouseLeave={() => setPaused(false)}
        >
          <div
            className="proj-track"
            ref={trackRef}
            style={{ transform: `translateX(-${offset}px)` }}
          >
            {PROJECTS.map((p) => (
              <article className="proj-card" key={p.f}>
                <div className="ph">
                  <ClipReveal className="clip-fill">
                    <img src={photo(p.f)} alt={p.title} loading="lazy" />
                  </ClipReveal>
                </div>
                <div className="proj-meta">
                  <span className="tag">{p.tag}</span>
                  <h3>{p.title}</h3>
                  <p>{p.desc}</p>
                </div>
              </article>
            ))}
          </div>
        </div>

        <div className="proj-nav" style={{ marginTop: 26 }}>
          <button className="proj-btn" onClick={prev} aria-label="Anterior">
            <ChevronLeft />
          </button>
          <button className="proj-btn" onClick={next} aria-label="Siguiente">
            <ChevronRight />
          </button>
        </div>
      </div>
    </section>
  )
}
