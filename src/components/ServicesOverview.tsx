import { Link } from 'react-router-dom'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { SERVICE_CATS } from '../lib/data'

/** Servicios (homepage) — lista editorial numerada estilo Editorial ("Services.").
 *  Aplana las 2 disciplinas en 7 servicios; cada fila enlaza a /servicios/:slug. */
const SERVICES = SERVICE_CATS.flatMap((cat) =>
  cat.services.map((s) => ({ ...s, disc: cat.label })),
)

export function ServicesOverview() {
  return (
    <section className="section services" id="servicios">
      <div className="wrap">
        <Reveal className="section-head srv-fab-head">
          <span className="eyebrow"><i>01</i>Servicios en detalle</span>
          <div className="srv-fab-title">
            <RevealText tag="h2" text="Servicios." />
            <span className="srv-fab-count">({SERVICES.length})</span>
          </div>
          <p className="lead">Dos disciplinas · siete servicios especializados.</p>
        </Reveal>

        <div className="srv-fab-list">
          {SERVICES.map((s, i) => (
            <Reveal delay={i * 0.06} key={s.slug}>
              <Link to={`/servicios/${s.slug}`} className="srv-fab-row">
                <span className="srv-fab-ix" aria-hidden="true">
                  ({String(i + 1).padStart(3, '0')})
                </span>

                <div className="srv-fab-main">
                  <h3 className="srv-fab-t">{s.title}</h3>
                  <p className="srv-fab-tag">{s.tagline}</p>
                  <div className="srv-fab-caps">
                    <span className="srv-fab-caps-label">Categorías</span>
                    <ul className="srv-fab-caps-list">
                      {s.capabilities.map((c) => (
                        <li key={c}>{c}</li>
                      ))}
                    </ul>
                  </div>
                </div>

                <span className="srv-fab-n" aria-hidden="true">
                  {s.capabilities.length}
                  <i>+</i>
                </span>
              </Link>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  )
}
