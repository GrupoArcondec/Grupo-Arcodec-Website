import { useState } from 'react'
import { Link } from 'react-router-dom'
import { SERVICE_CATS, srvImg } from '../../lib/data'
import { Label, Pill, Reveal } from './ui'

const ALL = SERVICE_CATS.flatMap((c) => c.services)

export function ServicesStudio() {
  const [open, setOpen] = useState(0)

  return (
    <section className="st-dark-sec" id="servicios">
      <div className="st-wrap">
        <div className="st-sec-head">
          <div className="st-sec-head-col1">
            <Reveal>
              <Label light>Qué hacemos</Label>
            </Reveal>
          </div>
          <Reveal as="h2" delay={80} mask className="st-display">
            Servicios.<span className="st-meta">({ALL.length})</span>
          </Reveal>
        </div>

        <div className="st-srv-list">
          {ALL.map((s, i) => {
            const isOpen = open === i
            const tags = s.capabilities.slice(0, 5)
            const extra = s.capabilities.length - tags.length
            return (
              <Reveal key={s.slug} delay={Math.min(i * 40, 160)}>
                {/* is-last: cada item vive en su propio Reveal, así que el CSS
                    no puede detectar el último con :last-of-type */}
                <article
                  className={`st-srv-item ${isOpen ? 'open' : ''}${i === ALL.length - 1 ? ' is-last' : ''}`}
                  onClick={() => setOpen(isOpen ? -1 : i)}
                >
                  <span className="st-srv-num">({String(i + 1).padStart(3, '0')})</span>
                  <div className="st-srv-main">
                    {/* siempre montadas: el CSS anima fade + scale al abrir */}
                    <span className="st-srv-thumbs">
                      <img className="st-srv-thumb" src={srvImg(s.code, 1)} alt="" loading="lazy" />
                      <img className="st-srv-thumb" src={srvImg(s.code, 2)} alt="" loading="lazy" />
                    </span>
                    <div className="st-srv-right">
                      <div className="st-srv-body st-srv-descwrap">
                        <div>
                          <p className="st-srv-desc">{s.tagline}. {s.description}</p>
                        </div>
                      </div>
                      <div className="st-srv-body st-srv-catswrap">
                        <div>
                          <p className="st-srv-cats-label">Alcances</p>
                          <div className="st-srv-tags">
                            {tags.map((t) => (
                              <span className="st-tag" key={t}>
                                {t}
                              </span>
                            ))}
                            {extra > 0 && <span className="st-tag st-tag--n">{extra}+</span>}
                          </div>
                        </div>
                      </div>
                      <button
                        className="st-srv-toggle"
                        aria-label={isOpen ? 'Cerrar' : 'Abrir'}
                        onClick={(e) => {
                          e.stopPropagation()
                          setOpen(isOpen ? -1 : i)
                        }}
                      >
                        {isOpen ? '–' : '+'}
                      </button>
                      <h3 className="st-srv-title">{s.title}</h3>
                    </div>
                  </div>
                </article>
              </Reveal>
            )
          })}
        </div>

        <div className="st-srv-cta">
          <Reveal>
            <Pill href="#contacto" dark={false} lg>
              Comenzar
            </Pill>
          </Reveal>
        </div>
      </div>
    </section>
  )
}

/* ---------- Cómo trabajamos (pasos) + obra real ---------- */
import { GALLERY, photo } from '../../lib/data'

const STEPS = [
  { n: '01', t: 'Diagnóstico y planeación técnica', img: srvImg('GESPR', 1) },
  { n: '02', t: 'Ingeniería y documentación completa', img: srvImg('ESTEL', 1) },
  { n: '03', t: 'Ejecución y supervisión en sitio', img: srvImg('PROELE', 1) },
  { n: '04', t: 'Entrega as-built y puesta en marcha', img: srvImg('COSDC', 1) },
]

export function ProcessStudio() {
  return (
    <section className="st-section" id="nosotros">
      <div className="st-wrap">
        <div className="st-adv-top">
          <Reveal>
            <Label>Nosotros</Label>
          </Reveal>
          <div>
            <Reveal as="p" className="st-credit" delay={40}>
              arcondec®
            </Reveal>
            <Reveal as="h2" delay={90} className="st-h2">
              Cómo lanzamos proyectos eléctricos{' '}
              <span className="st-h2-dim">y de infraestructura crítica.</span>
            </Reveal>
            <Reveal delay={150} className="st-body">
              <p style={{ marginTop: 30, maxWidth: 375, color: 'var(--st-ink)' }}>
                Nuestro equipo combina ingeniería, normatividad y ejecución para
                construir soluciones que operan sin fallas desde el primer día.
              </p>
            </Reveal>
          </div>
        </div>

        <div className="st-steps">
          {STEPS.map((s, i) => (
            <Reveal key={s.n} delay={i * 90}>
              <div className="st-step-card">
                <div className="st-step-head">
                  <span className="st-step-dots" aria-hidden="true">
                    {STEPS.map((_, j) => (
                      <i key={j} className={j <= i ? 'on' : ''} style={{ ['--k' as string]: j }} />
                    ))}
                  </span>
                  <span className="st-step-num">{s.n}</span>
                </div>
                <div className="st-step-body">
                  <img src={s.img} alt="" loading="lazy" />
                  <p>{s.t}</p>
                </div>
              </div>
            </Reveal>
          ))}
        </div>

        <Reveal delay={120}>
          <a className="st-reel" href="#proyectos">
            <img src={photo(GALLERY[0].f)} alt="Obra real de Grupo Arcondec" loading="lazy" />
            <span className="st-reel-inner">
              <span className="st-reel-play" aria-hidden="true">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M8 5.5v13l11-6.5z" />
                </svg>
              </span>
              <span className="st-reel-txt">
                <b>Ver obra real</b>
                <span>(1994-25©)</span>
              </span>
            </span>
          </a>
        </Reveal>
      </div>
    </section>
  )
}
