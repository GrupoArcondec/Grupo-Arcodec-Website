import { useState } from 'react'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { photo } from '../lib/data'

/* Pega aquí el ID de un video de YouTube para reproducirlo inline.
   Vacío → el botón abre el canal oficial @GRUPO_ARCONDEC. */
const YOUTUBE_ID = ''
const CHANNEL = 'https://www.youtube.com/@GRUPO_ARCONDEC'

export function Video() {
  const [playing, setPlaying] = useState(false)

  const onPlay = () => {
    if (YOUTUBE_ID) setPlaying(true)
    else window.open(CHANNEL, '_blank', 'noopener')
  }

  return (
    <section className="section video-sec" id="video">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow">En movimiento</span>
          <RevealText tag="h2" text="Mira a Arcondec en acción." accent="en acción." />
          <p className="lead">Recorre nuestros proyectos y procesos de ingeniería eléctrica en video.</p>
        </Reveal>
        <Reveal>
          <div className="video-wrap">
            {playing ? (
              <iframe
                src={`https://www.youtube.com/embed/${YOUTUBE_ID}?autoplay=1&rel=0&modestbranding=1`}
                title="Grupo Arcondec — video"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            ) : (
              <div
                className="video-poster"
                style={{ backgroundImage: `url('${photo('infraestructura-cr%C3%ADtica-data-center.jpg')}')` }}
                onClick={onPlay}
                role="button"
                aria-label="Reproducir video"
              >
                <button className="vp-play" aria-label="Reproducir video">
                  <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z" /></svg>
                </button>
              </div>
            )}
          </div>
        </Reveal>
        <div className="video-note">Canal oficial · YouTube @GRUPO_ARCONDEC</div>
      </div>
    </section>
  )
}
