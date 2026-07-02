import { useState } from 'react'
import { Link } from 'react-router-dom'
import { HUBS, WHATSAPP, projImg } from '../../lib/data'
import { Label, Pill, Reveal } from './ui'

const MODES = {
  proyecto: {
    price: 'A medida',
    per: '/proyecto',
    feats: [
      'Ingeniería y documentación completa',
      'Ejecución normada NOM · NEC · NFPA',
      'Entrega as-built y actas firmadas',
    ],
    lblTime: 'Tiempo de respuesta',
    time: '24–48 h',
  },
  mantenimiento: {
    price: 'Plan anual',
    per: '/continuidad',
    feats: [
      'Mantenimiento preventivo y correctivo',
      'Monitoreo y atención de emergencias',
      'Reportes técnicos periódicos',
    ],
    lblTime: 'Cobertura',
    time: 'Todo México',
  },
}

export function QuoteStudio() {
  const [mode, setMode] = useState<keyof typeof MODES>('proyecto')
  const m = MODES[mode]

  return (
    <section className="st-dark-sec" id="cotiza">
      <div className="st-wrap">
        <div className="st-sec-head" style={{ marginBottom: 0 }}>
          <Reveal>
            <Label light>Cotización simple</Label>
          </Reveal>
          <div className="st-sec-head-main">
            <Reveal as="h2" delay={80} mask className="st-display">
              Cotiza.
            </Reveal>
            <Reveal delay={140}>
              <div className="st-toggle" role="tablist">
                <button
                  className={mode === 'proyecto' ? 'on' : ''}
                  onClick={() => setMode('proyecto')}
                >
                  Por proyecto
                </button>
                <button
                  className={mode === 'mantenimiento' ? 'on' : ''}
                  onClick={() => setMode('mantenimiento')}
                >
                  Mantenimiento
                </button>
              </div>
            </Reveal>
          </div>
        </div>

        <div className="st-quote-grid">
          <Reveal>
            <div className="st-quote-side" style={{ height: '100%' }}>
              <div>
                <h4>¿Más capacidad y continuidad?</h4>
                <p className="st-body">
                  Suma estudios especializados y gestión integral desde el arranque.
                </p>
              </div>
              <div className="st-quote-side-foot">
                <b>+ Asesoría</b>
                <span className="st-switch" aria-hidden="true">
                  <i />
                </span>
              </div>
            </div>
          </Reveal>

          <Reveal delay={100}>
            <div className="st-quote-main" style={{ height: '100%' }}>
              <div className="st-quote-main-top">
                <div className="st-price">
                  {m.price}
                  <small>{m.per}</small>
                </div>
                <div className="st-feats">
                  {m.feats.map((f) => (
                    <span className="st-feat" key={f}>
                      <span className="st-plus-btn">+</span>
                      {f}
                    </span>
                  ))}
                </div>
              </div>
              <div className="st-quote-main-bot">
                <div className="st-quote-bot-row">
                  <span className="lbl">{m.lblTime}</span>
                  <span className="val">{m.time}</span>
                </div>
                <Pill href={WHATSAPP} dark={false}>
                  Contáctanos
                </Pill>
              </div>
            </div>
          </Reveal>
        </div>

        <div className="st-more">
          <Reveal>
            <span className="st-body" style={{ color: '#fff' }}>
              ¿Buscas algo más?
            </span>
          </Reveal>
          <div>
            <Reveal as="p" delay={80} className="st-more-txt">
              Suma mantenimiento, estudios eléctricos o gestión integral —{' '}
              <span className="st-dim">
                herramientas flexibles para fortalecer tu proyecto. Armamos una solución
                que se ajusta a tu operación, no al revés.
              </span>
            </Reveal>
            <Reveal delay={160}>
              <div className="st-quote-contact">
                <img src={projImg(HUBS[5].file)} alt="Asesor técnico Arcondec" loading="lazy" />
                <div>
                  <p className="nm">Grupo Arcondec</p>
                  <p className="rl">Asesor técnico</p>
                </div>
              </div>
            </Reveal>
          </div>
        </div>
      </div>
    </section>
  )
}

/* ---------- Equipo / cultura ---------- */
const CREW = [
  { img: projImg(HUBS[4].file), role: 'Ingeniería eléctrica', place: 'En obra · Durango', desc: HUBS[4].desc },
  { img: projImg(HUBS[1].file), role: 'Data center', place: 'En obra · Querétaro', desc: HUBS[1].desc },
  { img: projImg(HUBS[10].file), role: 'Obra civil', place: 'En obra · García, NL', desc: HUBS[10].desc },
  { img: projImg(HUBS[9].file), role: 'Infraestructura', place: 'En obra · Mazatlán', desc: HUBS[9].desc },
]

/* icono ⊕ invertido (círculo oscuro, cruz blanca) para las cards de equipo */
function TeamBadge() {
  return (
    <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
      <circle cx="8" cy="8" r="7.2" fill="#08182b" />
      <path d="M8 4.6v6.8M4.6 8h6.8" stroke="#fff" strokeWidth="1.6" />
    </svg>
  )
}

export function TeamStudio() {
  return (
    <section className="st-section">
      <div className="st-wrap">
        <div className="st-team-shell">
          <div className="st-team-text">
            <div className="st-team-head">
              <Reveal>
                <p className="st-team-mark">arcondec®</p>
              </Reveal>
              <Reveal as="h2" delay={80} className="st-h2">
                Las manos <span className="st-h2-dim">detrás de los proyectos.</span>
              </Reveal>
            </div>
            <div className="st-team-bottom">
              <Reveal className="st-team-cell st-team-cta">
                <span className="st-team-plus" aria-hidden="true" />
                <div>
                  <b>Sé parte de nuestra misión</b>
                  <p>
                    Si estás listo para construir infraestructura crítica, queremos
                    conocerte.
                  </p>
                  <Link to="/trabaja" className="st-pill st-pill--dark">
                    <span className="st-pill-flip">
                      <span>Postúlate</span>
                      <span aria-hidden="true">Postúlate</span>
                    </span>
                    <i className="st-dot" />
                  </Link>
                </div>
              </Reveal>
              <Reveal delay={80} className="st-team-cell">
                <span className="st-team-plus" aria-hidden="true" />
                <p className="st-team-quote">
                  Creemos que el gran trabajo nace{' '}
                  <span className="st-team-quote-hl">de la colaboración.</span> Por eso
                  trabajamos codo a codo para que cada proyecto cumpla tus objetivos y
                  supere expectativas.
                </p>
              </Reveal>
            </div>
          </div>
          <div className="st-team-strip">
            {CREW.map((c, i) => (
              <Reveal key={c.place} delay={(i + 1) * 80}>
                <figure className="st-team-card" style={{ margin: 0 }}>
                  <img src={c.img} alt={`${c.role} — ${c.place}`} loading="lazy" />
                  <span className="top-meta">
                    <TeamBadge />
                    <span className="tm-txt">
                      <b>{c.role}</b>
                      <small>en arcondec®</small>
                    </span>
                  </span>
                  <figcaption>
                    <b>{c.place}</b>
                    <p>{c.desc}</p>
                  </figcaption>
                </figure>
              </Reveal>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
