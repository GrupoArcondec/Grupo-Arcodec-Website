import { Reveal, Slide } from './Button'
import { RevealText } from './RevealText'

const VALUES = [
  { t: 'Un equipo que comparte tu pasión', d: 'Te integras a un grupo multidisciplinario enfocado en la excelencia operativa.' },
  { t: 'Proyectos de alto nivel técnico', d: 'Instalaciones eléctricas industriales, data centers y sistemas críticos reales.' },
  { t: 'Ambiente de trabajo colaborativo', d: 'Aprendizaje continuo, retos técnicos y oportunidades reales de desarrollo.' },
  { t: 'Reconocimiento a tu esfuerzo', d: 'Visibilidad en proyectos clave con oportunidades reales de crecimiento.' },
]

export function Careers() {
  return (
    <section className="section careers" id="trabaja">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow"><i>07</i>Trabaja con nosotros</span>
          <RevealText tag="h2" text="Transforma tu talento en resultados reales." accent="resultados reales." />
          <p className="lead">
            Únete a un equipo que comparte tu pasión por la ingeniería. Buscamos personas que
            quieran crecer resolviendo infraestructura crítica de verdad.
          </p>
        </Reveal>

        <div className="careers-grid">
          {VALUES.map((v, i) => (
            <Reveal key={v.t} delay={i * 0.06} className="career">
              <span className="career-ix">{String(i + 1).padStart(2, '0')}</span>
              <h3 className="career-t">{v.t}</h3>
              <p className="career-d">{v.d}</p>
            </Reveal>
          ))}
        </div>

        <Reveal className="careers-foot">
          <p className="careers-incl">
            Promovemos la inclusión y el respeto: igualdad de oportunidades basada exclusivamente
            en competencias, habilidades y experiencia.
          </p>
          <a className="btn btn-amp" href="mailto:talento@arcondec.mx?subject=Quiero%20unirme%20a%20Arcondec">
            <Slide>¡Queremos conocerte!</Slide>
          </a>
        </Reveal>
      </div>
    </section>
  )
}
