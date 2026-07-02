import { CLIENTS, HUBS, WHATSAPP, img, projImg } from '../../lib/data'
import { Counter, Pill, Reveal, ScrollWords, SectionHead, useInViewOnce } from './ui'

/* Compromisos reales del estudio, presentados como tarjetas de experiencia */
const CARDS = [
  {
    who: 'Acompañamiento',
    org: 'De principio a fin',
    quote: 'Te guiamos antes, durante y después de la implementación, con soporte directo de nuestros ingenieros.',
    photo: projImg(HUBS[1].file),
  },
  {
    who: 'Agilidad',
    org: 'Sin excusas',
    quote: 'Resolvemos rápido, ejecutamos con precisión y entregamos a tiempo. Tu proyecto no se detiene.',
    photo: null,
  },
  {
    who: 'Control',
    org: 'Menos riesgos',
    quote: 'Evitamos fallas, paros inesperados y problemas normativos. Diseñamos pensando en la seguridad total.',
    photo: projImg(HUBS[3].file),
  },
]

/* marca de comillas (56×12) + icono "+" de la tarjeta de cita */
function QuoteMark() {
  return (
    <svg width="56" height="12" viewBox="0 0 56 12" fill="currentColor" aria-hidden="true">
      <path d="M2.4 12C0.9 9.9 0 7.6 0 5.2 0 2.1 1.9 0 4.6 0c2.3 0 4 1.7 4 4 0 2.2-1.6 3.8-3.7 3.8-.4 0-.9-.1-1.1-.2.3 1.2 1.2 2.6 2.3 3.6L2.4 12Z" />
      <path d="M13.4 12c-1.5-2.1-2.4-4.4-2.4-6.8 0-3.1 1.9-5.2 4.6-5.2 2.3 0 4 1.7 4 4 0 2.2-1.6 3.8-3.7 3.8-.4 0-.9-.1-1.1-.2.3 1.2 1.2 2.6 2.3 3.6l-3.7 3.6Z" />
    </svg>
  )
}

export function ExperienceStudio() {
  return (
    <section className="st-section">
      <div className="st-wrap">
        <SectionHead label="Experiencias" title="Experiencias." />

        <div className="st-exp-grid">
          <Reveal className="st-exp-col">
            <div className="st-exp-card st-exp-card--intro">
              <div className="st-exp-intro-top">
                <div className="st-exp-rating">
                  <Counter to={30} prefix="+" />
                  <small> /años</small>
                </div>
                <p className="st-body">
                  Más de <b style={{ color: 'var(--st-ink)' }}>30 años</b> entregando
                  proyectos que generan resultados reales.
                </p>
              </div>
              <div className="st-exp-intro-bot">
                <div>
                  <b className="st-exp-brand">arcondec®</b>
                  <div className="st-logo-row">
                    {CLIENTS.slice(0, 3).map((c) => (
                      <img key={c.f} src={img(`clients/${c.f}.png`)} alt={c.n} loading="lazy" />
                    ))}
                  </div>
                </div>
                <Pill href={WHATSAPP}>Cuéntanos tu proyecto</Pill>
              </div>
            </div>
          </Reveal>

          {CARDS.map((c, i) => (
            <Reveal
              key={c.who}
              delay={(i + 1) * 90}
              className={`st-exp-col${i === 1 ? ' st-exp-col--rev' : ''}`}
            >
              <div className="st-exp-card st-exp-card--who">
                <div className="st-exp-who">
                  {c.photo && <img src={c.photo} alt="" loading="lazy" />}
                  <div>
                    <b>{c.who}</b>
                    <span>{c.org}</span>
                  </div>
                </div>
              </div>
              <div className="st-exp-card st-exp-card--quote">
                <div className="st-exp-qtop">
                  <QuoteMark />
                  <span className="st-plus" aria-hidden="true" />
                </div>
                <p className="st-exp-quote">{c.quote}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  )
}

/* ---------- Nuestro enfoque: cifras + texto que se enciende con el scroll ---------- */
export function ApproachStudio() {
  return (
    <section className="st-section">
      <div className="st-wrap">
        <div className="st-counters">
          {[
            { to: 30, prefix: '+', suffix: '', label: 'Años de experiencia en infraestructura' },
            { to: 16, prefix: '', suffix: '', label: 'Hubs de proyecto entregados en México' },
            { to: 2.5, prefix: '', suffix: ' MVA', label: 'Capacidad por proyecto', fixed: true },
            { to: 24, prefix: '', suffix: '/7', label: 'Continuidad crítica de operación' },
          ].map((c, i) => (
            <Reveal key={c.label} delay={i * 80} className="st-counter">
              <b>
                {c.fixed ? (
                  '2.5 MVA'
                ) : (
                  <Counter to={c.to} prefix={c.prefix} suffix={c.suffix} />
                )}
              </b>
              <p className="st-body">{c.label}</p>
            </Reveal>
          ))}
        </div>
        <div className="st-approach-divider" aria-hidden="true" />

        <div className="st-approach">
          <div className="st-approach-side">
            <Reveal>
              <b>arcondec®</b>
              <p className="st-body">
                Cada proyecto que tomamos está diseñado para operar en el largo plazo.
              </p>
            </Reveal>
          </div>
          <div className="st-approach-main">
            <ScrollWords
              className="st-approach-txt"
              dimCount={4}
              text="Nuestro enfoque es simple: funcionalidad, seguridad y claridad, asegurando que cada proyecto cumpla su propósito sin complejidad innecesaria."
            />
            <p className="st-approach-sub">
              No prometemos de más. Construimos ingeniería bien documentada,
              instalaciones normadas y soluciones que ayudan a las empresas a operar
              sin fallas.
            </p>
          </div>
        </div>
      </div>
    </section>
  )
}

/* ---------- Caso bento: métricas reales ---------- */
const REGIONS = [
  { l: 'NL', v: 4 },
  { l: 'CDMX', v: 2 },
  { l: 'Norte', v: 4 },
  { l: 'Bajío', v: 2 },
  { l: 'Centro', v: 2 },
  { l: 'Sureste', v: 2 },
]
const MAX_REGION = Math.max(...REGIONS.map((r) => r.v))

export function CaseStudio() {
  const { ref, inView } = useInViewOnce<HTMLDivElement>('-6% 0px')
  return (
    <section className="st-section st-section--flush">
      <div className="st-wrap">
        <div className="st-case-grid">
          <Reveal className="st-case-photo">
            <img src={projImg(HUBS[14].file)} alt="Oficinas corporativas en planta Santa Fe" loading="lazy" />
            <div className="st-case-photo-top">
              <div>
                <p>Caso de estudio</p>
                <p>Ingeniería eléctrica, obra civil y data centers</p>
              </div>
              <span className="st-plus" aria-hidden="true" />
            </div>
            <span className="st-case-brand">arcondec®</span>
            <div className="st-case-photo-bot">
              <a href="https://arcondec.mx" target="_blank" rel="noreferrer">
                Sitio oficial ↗
              </a>
              <div>
                <b>De la subestación al data center.</b>
                <span>Lo hacemos todo.</span>
              </div>
            </div>
          </Reveal>

          <Reveal delay={90} className="st-case-card st-case-card--tall">
            <div className="st-case-metrics">
              <div className="st-case-metric">
                <small>Rango de capacidad instalada</small>
                <b>
                  225 kVA <span className="arrow">→</span> 2.5 MVA
                </b>
              </div>
              <div className="st-case-metric">
                <small>Presencia nacional</small>
                <b>
                  16 hubs<span className="st-chip">+ LATAM</span>
                </b>
              </div>
              <div className="st-case-metric">
                <small>Normatividad aplicada</small>
                <b>NOM · NEC · NFPA</b>
              </div>
            </div>
            <div>
              <p className="st-case-quote">
                «No se trata solo de construir, sino de entregar infraestructura lista
                para operar con seguridad, eficiencia y confiabilidad.»
              </p>
              <span className="st-small" style={{ display: 'block', marginTop: 14 }}>
                Grupo Arcondec · Gestión integral
              </span>
            </div>
          </Reveal>

          <div className="st-case-col">
            <Reveal delay={160} className="st-case-card st-gauge">
              <div className="st-gauge-val">24/7</div>
              <div>
                <p style={{ fontWeight: 500, letterSpacing: '-0.04em' }}>
                  Continuidad operativa
                </p>
                <p className="st-case-quote" style={{ marginTop: 6 }}>
                  Priorizamos la disponibilidad sin sacrificar seguridad ni
                  cumplimiento normativo.
                </p>
              </div>
            </Reveal>
            <Reveal delay={200} className="st-case-card st-case-card--graph">
              <div className="st-case-metric">
                <small>Hubs de proyecto por región</small>
              </div>
              <div ref={ref} className={`st-bars ${inView ? 'is-in' : ''}`} aria-hidden="true">
                {REGIONS.map((r, i) => (
                  <div
                    key={r.l}
                    className={`bar ${r.v === MAX_REGION ? 'hi' : ''}`}
                    style={{
                      height: `${(r.v / MAX_REGION) * 100}%`,
                      ['--d' as string]: `${i * 70}ms`,
                    }}
                  >
                    <span>+{r.v}</span>
                  </div>
                ))}
              </div>
              <div className="st-bar-foot">
                {REGIONS.map((r) => (
                  <span key={r.l}>{r.l}</span>
                ))}
              </div>
            </Reveal>
          </div>
        </div>
      </div>
    </section>
  )
}
