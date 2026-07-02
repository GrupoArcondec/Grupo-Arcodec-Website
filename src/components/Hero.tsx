import { useEffect, useRef } from 'react'
import { photo } from '../lib/data'
import { RevealText } from './RevealText'
import { Slide } from './Button'

export function Hero() {
  const photoRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const h = photoRef.current
    if (!h) return
    const url = photo('soluciones-en-ingenier%C3%ADa-el%C3%A9ctrica.jpg')
    const pre = new Image()
    pre.onload = () => {
      h.style.backgroundImage = `url('${url}')`
      requestAnimationFrame(() => h.classList.add('in'))
    }
    pre.src = url
  }, [])

  return (
    <section className="hero">
      <div className="hero-bg">
        <div className="hero-photo" ref={photoRef} />
      </div>
      <div className="hero-inner">
        <span className="eyebrow fade-up in-view"><i>00</i>Grupo Arcondec · Enciende tus ideas</span>
        <RevealText
          tag="h1"
          delay={0.15}
          text="Infraestructura eléctrica industrial y data centers listos para operar."
          accent="listos para operar."
        />
        <p className="lead fade-up in-view" style={{ animationDelay: '.2s' }}>
          Diseñamos, instalamos y supervisamos infraestructura crítica: ingeniería eléctrica e
          implementación de data centers, con más de 30 años de experiencia.
        </p>
        <div className="hero-cta fade-up in-view" style={{ animationDelay: '.3s' }}>
          <a className="btn btn-amp" href="tel:+528119341192">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z" />
            </svg>
            <Slide>Hablar con un asesor</Slide>
          </a>
        </div>
      </div>
    </section>
  )
}
