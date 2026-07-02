import { useRef } from 'react'
import { Button } from './Button'
import { LottieMark } from './LottieMark'
import { RevealText } from './RevealText'
import { PHOTO_FILES, photo, WHATSAPP } from '../lib/data'

export function Partner() {
  const boxRef = useRef<HTMLDivElement>(null)
  const trailRef = useRef<HTMLDivElement>(null)
  const lastSpawn = useRef(0)
  const i = useRef(0)

  const onMove = (e: React.MouseEvent) => {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduce) return
    const now = performance.now()
    if (now - lastSpawn.current < 80) return
    lastSpawn.current = now
    const box = boxRef.current
    const trail = trailRef.current
    if (!box || !trail) return
    const r = box.getBoundingClientRect()
    const x = e.clientX - r.left
    const y = e.clientY - r.top

    const im = document.createElement('img')
    im.src = photo(PHOTO_FILES[i.current % PHOTO_FILES.length])
    i.current++
    im.className = 'trail-img'
    const rot = (Math.random() * 20 - 10).toFixed(1)
    im.style.left = `${x - 60}px`
    im.style.top = `${y - 42}px`
    im.style.transform = `rotate(${rot}deg) scale(1)`
    im.style.opacity = '1'
    trail.appendChild(im)

    requestAnimationFrame(() => {
      im.style.opacity = '0'
      im.style.transform = `rotate(${rot}deg) scale(.6)`
    })
    window.setTimeout(() => im.remove(), 1000)
  }

  return (
    <section className="section partner">
      <div className="partner-box" ref={boxRef} onMouseMove={onMove}>
        <div className="partner-trail" ref={trailRef} aria-hidden="true" />
        <div className="partner-inner">
          <LottieMark />
          <RevealText tag="h2" text="Enciende tu próximo proyecto." accent="próximo proyecto." />
          <p>
            Aliados estratégicos en ingeniería eléctrica y centros de datos. Cuéntanos qué quieres
            energizar y lo ejecutamos llave en mano.
          </p>
          <Button href={WHATSAPP} external variant="amp">
            <svg viewBox="0 0 24 24" fill="currentColor" style={{ width: 18, height: 18 }}>
              <path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 4.8-1.3A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.8.7.8-2.7-.2-.3A8 8 0 1 1 12 20z" />
            </svg>
            Iniciar conversación
          </Button>
        </div>
      </div>
    </section>
  )
}
