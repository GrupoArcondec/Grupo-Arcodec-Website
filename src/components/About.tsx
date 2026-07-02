import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { CountUp } from './CountUp'

const CHECKS = [
  'Ingeniería basada en normas y estándares vigentes.',
  'Entrega puntual de proyectos, en tiempo y forma.',
  'Metodologías eficientes y herramientas digitales.',
  'Cobertura nacional, operando desde Monterrey.',
]

export function About() {
  return (
    <section className="section about" id="nosotros">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow"><i>04</i>Quiénes somos</span>
          <RevealText tag="h2" text="Nosotros." />
          <p className="lead">
            Empresa mexicana con más de 30 años creando proyectos de alta calidad.
          </p>
        </Reveal>

        {/* Statement grande estilo Editorial */}
        <Reveal>
          <RevealText
            tag="p"
            className="about-statement"
            text="Combinamos ingeniería, supervisión y ejecución para entregar infraestructura crítica lista para operar."
            accent="lista para operar."
            stagger={0.035}
          />
        </Reveal>

        {/* Checklist numerado 01–04 (firma del About de Editorial) */}
        <div className="fab-check">
          {CHECKS.map((t, i) => (
            <Reveal key={i} delay={i * 0.06}>
              <div className="fab-check-row">
                <span className="fab-check-ix">{`0${i + 1}`}</span>
                <span className="fab-check-t">{t}</span>
              </div>
            </Reveal>
          ))}
        </div>

        {/* Banda de cifras — única del sitio, se conserva */}
        <Reveal delay={0.1}>
          <div className="about-stats">
            <div className="ast"><b>1991</b><span>Año de fundación</span></div>
            <div className="ast"><b><CountUp value={30} prefix="+" /></b><span>Años de experiencia</span></div>
            <div className="ast"><b>DUNS</b><span>Empresa certificada</span></div>
            <div className="ast"><b>13+</b><span>Estados con cobertura</span></div>
          </div>
        </Reveal>

        <Reveal delay={0.16}>
          <a className="about-cta" href="#cobertura">
            Ver en operación
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
              <path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" strokeWidth="1.6"
                strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </a>
        </Reveal>
      </div>
    </section>
  )
}
