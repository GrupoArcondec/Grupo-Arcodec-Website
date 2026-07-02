import { useEffect, useMemo, useRef, useState } from 'react'
import { gsap } from 'gsap'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { HUBS, projImg, photo } from '../lib/data'

const ALL = 'Todos'

/** Proyectos — los 16 "Hub [Ciudad]" reales como lista editorial estilo Editorial:
 *  nombre + meta a la derecha, filtros por categoría y la imagen que sigue el
 *  cursor en hover (gsap quickTo). */
export function Proyectos() {
  const previewRef = useRef<HTMLImageElement>(null)
  const [src, setSrc] = useState(projImg(HUBS[0].file))
  const [filter, setFilter] = useState(ALL)
  const xTo = useRef<((v: number) => void) | null>(null)
  const yTo = useRef<((v: number) => void) | null>(null)

  const cats = useMemo(() => Array.from(new Set(HUBS.map((h) => h.cat))), [])
  const rows = useMemo(
    () => (filter === ALL ? HUBS : HUBS.filter((h) => h.cat === filter)),
    [filter],
  )

  useEffect(() => {
    const el = previewRef.current
    if (!el) return
    gsap.set(el, { xPercent: -50, yPercent: -50, autoAlpha: 0, scale: 0.86, rotate: -6 })
    xTo.current = gsap.quickTo(el, 'x', { duration: 0.5, ease: 'power3.out' })
    yTo.current = gsap.quickTo(el, 'y', { duration: 0.5, ease: 'power3.out' })
  }, [])

  const onMove = (e: React.PointerEvent) => {
    xTo.current?.(e.clientX)
    yTo.current?.(e.clientY)
  }
  const show = (file: string) => {
    setSrc(projImg(file))
    const el = previewRef.current
    if (el) gsap.to(el, { autoAlpha: 1, scale: 1, rotate: -3, duration: 0.5, ease: 'power3.out' })
  }
  const hide = () => {
    const el = previewRef.current
    if (el) gsap.to(el, { autoAlpha: 0, scale: 0.86, rotate: -6, duration: 0.4, ease: 'power3.out' })
  }

  return (
    <section className="section obra" id="proyectos" onPointerMove={onMove}>
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow"><i>02</i>Proyectos destacados</span>
          <div className="obra-head">
            <RevealText tag="h2" text="Proyectos." />
            <span className="obra-count">({HUBS.length})</span>
          </div>
          <p className="lead">
            Cada proyecto es una muestra de nuestra capacidad técnica, calidad y cumplimiento —
            desplegados por todo México.
          </p>
        </Reveal>

        <div className="obra-filters" role="tablist" aria-label="Filtrar por categoría">
          {[ALL, ...cats].map((c) => (
            <button
              key={c}
              type="button"
              role="tab"
              aria-selected={filter === c}
              className={`obra-chip${filter === c ? ' is-active' : ''}`}
              onClick={() => setFilter(c)}
            >
              {c}
            </button>
          ))}
        </div>

        <div className="obra-list">
          {rows.map((h, i) => (
            <Reveal key={h.city + h.file} delay={(i % 5) * 0.05}>
              <a
                className="obra-row"
                href="#contacto"
                onMouseEnter={() => show(h.file)}
                onMouseLeave={hide}
              >
                <span className="obra-name">Hub {h.city}.</span>
                <span className="obra-meta">
                  <i aria-hidden="true">/</i>{h.cat} · {h.state}
                </span>
                <span className="obra-thumb">
                  <img
                    src={projImg(h.file)}
                    alt=""
                    loading="lazy"
                    onError={(e) => { (e.currentTarget as HTMLImageElement).src = photo('BLOG_1.jpg') }}
                  />
                </span>
              </a>
            </Reveal>
          ))}
        </div>
      </div>

      <img
        className="obra-preview"
        ref={previewRef}
        src={src}
        alt=""
        aria-hidden="true"
        onError={(e) => { (e.currentTarget as HTMLImageElement).src = photo('BLOG_1.jpg') }}
      />
    </section>
  )
}
