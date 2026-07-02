import { HUBS, projImg, WHATSAPP, PROJECT_STATS, CLIENTS, img } from '../../lib/data'
import { Counter, Label, Pill, Reveal, SectionHead } from './ui'

/* años reales aproximados de cada hub para el pie de tarjeta */
const FEATURED = HUBS.slice(0, 6)

export function ProjectsStudio() {
  return (
    <section className="st-section" id="proyectos">
      <div className="st-wrap">
        <SectionHead
          title="Proyectos."
          meta={`(${HUBS.length})`}
          aside={
            <p>
              Hemos acompañado a empresas de telecom, industria y misión crítica en todo
              México. Esta es una muestra de nuestra obra reciente.
            </p>
          }
        />

        <div className="st-proj-grid">
          {FEATURED.map((h, i) => (
            <Reveal key={h.city} delay={(i % 2) * 90} className="st-proj-card">
              <div className="st-proj-head">
                <span>
                  {h.city}.<span className="st-year">/{h.state}</span>
                </span>
                <span className="st-proj-dots" aria-hidden="true">
                  <i />
                  <i />
                  <i />
                </span>
              </div>
              <figure className="st-proj-media">
                <img src={projImg(h.file)} alt={h.desc} loading="lazy" />
                <span className="st-proj-logo">{h.cat}</span>
              </figure>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  )
}

/* ---------- Ventajas + bento de cifras ---------- */
export function AdvantagesStudio() {
  return (
    <section className="st-section st-section--flush" id="estudio">
      <div className="st-wrap">
        <div className="st-adv-top">
          <Reveal>
            <Label>Por qué elegirnos</Label>
          </Reveal>
          <div>
            <Reveal as="h2" className="st-h2">
              Resultados probados en cada proyecto,{' '}
              <span className="st-h2-dim">
                con foco en seguridad, norma y continuidad operativa.
              </span>
            </Reveal>
          </div>
        </div>

        <div className="st-adv-bento">
          <Reveal className="st-adv-photo">
            <img
              src={projImg(HUBS[2].file)}
              alt="Centro de datos con charolas de fibra y racks"
              loading="lazy"
            />
            <span className="st-plus-btn" aria-hidden="true" />
            <div className="st-adv-photo-txt">
              <p>Tu proyecto comienza con una conversación. Hablemos hoy.</p>
              <Pill href={WHATSAPP}>Hablemos</Pill>
            </div>
          </Reveal>

          <div aria-hidden="true" className="st-adv-filler" />

          <div className="st-adv-items">
            <Reveal as="p" className="st-adv-intro">
              <span>Sin relleno, solo resultados:</span> más de tres décadas entregando
              infraestructura que genera resultados reales.
            </Reveal>

            <div className="st-adv-cards">
              <Reveal delay={100} className="st-stat-col">
                <div className="st-stat-top">
                  <div className="st-stat-big">
                    <Counter to={30} prefix="+" />
                  </div>
                  <span className="st-idx">01</span>
                </div>
                <div className="st-stat-card">
                  <p className="st-stat-title">Años de experiencia</p>
                  <p className="st-stat-foot">
                    Ingeniería eléctrica, data centers e infraestructura crítica operando
                    24/7 en todo México.
                  </p>
                </div>
              </Reveal>

              <Reveal delay={180} className="st-stat-col">
                <div className="st-stat-top">
                  <div className="st-stat-big">
                    <Counter to={PROJECT_STATS[1].count ?? 16} />
                  </div>
                  <span className="st-idx">02</span>
                </div>
                <div className="st-stat-card">
                  <p className="st-stat-title">
                    Hubs de proyecto
                    <br />
                    en todo México
                  </p>
                  <div className="st-logo-row">
                    {CLIENTS.slice(0, 3).map((c) => (
                      <img
                        key={c.f}
                        src={img(`clients/${c.f}.png`)}
                        alt={c.n}
                        loading="lazy"
                      />
                    ))}
                  </div>
                </div>
              </Reveal>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
