import { useEffect, useRef, useState } from 'react'
import { gsap } from 'gsap'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { GALLERY, photo } from '../lib/data'

/** Obra real — lista editorial estilo Editorial: filas Proyecto / Categoría
 *  con una imagen que sigue el cursor y se revela al pasar por cada fila. */
export function Gallery() {
  const previewRef = useRef<HTMLImageElement>(null)
  const [src, setSrc] = useState(photo(GALLERY[0].f))
  const xTo = useRef<((v: number) => void) | null>(null)
  const yTo = useRef<((v: number) => void) | null>(null)

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
    setSrc(photo(file))
    const el = previewRef.current
    if (el) gsap.to(el, { autoAlpha: 1, scale: 1, rotate: -3, duration: 0.5, ease: 'power3.out' })
  }
  const hide = () => {
    const el = previewRef.current
    if (el) gsap.to(el, { autoAlpha: 0, scale: 0.86, rotate: -6, duration: 0.4, ease: 'power3.out' })
  }

  return (
    <section className="section obra" id="obra" onPointerMove={onMove}>
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow"><i>02</i>Obra real</span>
          <RevealText tag="h2" text="Lo que construimos, en sitio." accent="en sitio." />
          <p className="lead">
            Instalaciones, potencia y data centers ejecutados por Grupo Arcondec. Fotografía de
            proyectos reales, no renders.
          </p>
        </Reveal>

        <div className="obra-list">
          {GALLERY.map((it, i) => (
            <a
              className="obra-row"
              key={it.f}
              href="#contacto"
              onMouseEnter={() => show(it.f)}
              onMouseLeave={hide}
            >
              <span className="obra-ix">{String(i + 1).padStart(2, '0')}</span>
              <span className="obra-title">{it.t}</span>
              <span className="obra-cat">{it.k}</span>
              <span className="obra-thumb">
                <img src={photo(it.f)} alt="" loading="lazy" />
              </span>
              <span className="obra-arrow" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                  <path d="M7 17 17 7M9 7h8v8" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              </span>
            </a>
          ))}
        </div>
      </div>

      {/* imagen flotante que sigue el cursor (desktop) */}
      <img className="obra-preview" ref={previewRef} src={src} alt="" aria-hidden="true" />
    </section>
  )
}
