import { useState, Fragment } from 'react'
import { Plus } from 'lucide-react'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { SERVICE_CATS, srvImg, WHATSAPP } from '../lib/data'

/** Lista plana de TODOS los servicios (ambas disciplinas), con su disciplina. */
const FLAT = SERVICE_CATS.flatMap((c) => c.services.map((s) => ({ s, disc: c.label })))

export function Services() {
  // un solo acordeón abierto a lo largo de toda la lista (índice global 0..n)
  const [open, setOpen] = useState(0)
  const current = open >= 0 && open < FLAT.length ? FLAT[open] : null

  let gi = -1 // índice global de servicio mientras recorremos los grupos

  return (
    <section className="section services" id="servicios">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow"><i>01</i>Servicios en detalle</span>
          <RevealText tag="h2" text="Servicios." />
          <p className="lead">
            De la subestación al tablero y del concepto al data center llave en mano. Ingeniería
            eléctrica e infraestructura crítica, normada y lista para operar.
          </p>
        </Reveal>

        <div className="srv-layout">
          <div className="srv-list">
            {SERVICE_CATS.map((cat, ci) => (
              <Fragment key={cat.key}>
                <div className="srv-group">
                  <span className="srv-group-ix">{String(ci + 1).padStart(2, '0')}</span>
                  <h3 className="srv-group-label">{cat.label}</h3>
                  <p className="srv-group-blurb">{cat.blurb}</p>
                </div>

                {cat.services.map((s) => {
                  gi += 1
                  const idx = gi
                  const isOpen = open === idx
                  return (
                    <article className={`srv-item ${isOpen ? 'open' : ''}`} key={s.slug}>
                      <button
                        className="srv-head"
                        aria-expanded={isOpen}
                        onClick={() => setOpen(isOpen ? -1 : idx)}
                      >
                        <span className="srv-ix">{String(idx + 1).padStart(2, '0')}</span>
                        <span className="srv-titles">
                          <span className="srv-title">{s.title}</span>
                          <span className="srv-tag">{s.tagline}</span>
                        </span>
                        <span className="srv-plus" aria-hidden="true"><Plus /></span>
                      </button>

                      <div className="srv-body">
                        <div>
                          <div className="srv-media-m">
                            <img src={srvImg(s.code, 1)} alt={s.title} loading="lazy" />
                          </div>
                          <p className="srv-desc">{s.description}</p>
                          <ul className="srv-caps">
                            {s.capabilities.map((c) => (
                              <li key={c}>{c}</li>
                            ))}
                          </ul>
                          <a className="srv-cta" href={WHATSAPP} target="_blank" rel="noopener">
                            Cotizar este servicio
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
                              <path d="M5 12h14M13 6l6 6-6 6" />
                            </svg>
                          </a>
                        </div>
                      </div>
                    </article>
                  )
                })}
              </Fragment>
            ))}
          </div>

          <aside className="srv-preview" aria-hidden="true">
            <div className="srv-preview-frame">
              <img
                key={current ? current.s.code : 'none'}
                src={srvImg(current ? current.s.code : FLAT[0].s.code, 1)}
                alt=""
                loading="lazy"
              />
              <div className="srv-preview-cap">
                <span>{current ? current.disc : SERVICE_CATS[0].label}</span>
                {current ? current.s.title : 'Selecciona un servicio'}
              </div>
            </div>
          </aside>
        </div>
      </div>
    </section>
  )
}
