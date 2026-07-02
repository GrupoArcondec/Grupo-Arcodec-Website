import { useState } from 'react'
import { Reveal } from './Button'
import { RevealText } from './RevealText'

const FAQS: { q: string; a: string }[] = [
  {
    q: '¿Qué tipo de proyectos ejecutan?',
    a: 'Proyectos eléctricos integrales llave en mano —industriales y comerciales—, construcción e ingeniería de data centers, subestaciones y media tensión, soluciones en corriente directa y gestión integral de proyectos, desde la etapa conceptual hasta la puesta en marcha.',
  },
  {
    q: '¿Bajo qué normas y estándares trabajan?',
    a: 'Diseñamos y ejecutamos conforme a la normativa vigente: NOM (NOM-001-SEDE), lineamientos CFE y estándares NFPA e internacionales de misión crítica. Incluimos verificación UVIE y trámites/gestorías ante CFE.',
  },
  {
    q: '¿En qué zonas del país tienen cobertura?',
    a: 'Operamos desde Monterrey con cobertura nacional: hemos desplegado proyectos en más de 13 estados de la República, con capacidad para atender obra en todo México.',
  },
  {
    q: '¿Qué tan rápido responden una solicitud?',
    a: 'Te contactamos en menos de 24 horas hábiles. Tras una primera consulta entregamos un plan de trabajo y tiempos por escrito, con un ingeniero responsable como único interlocutor de tu proyecto.',
  },
  {
    q: '¿Incluyen supervisión y puesta en marcha?',
    a: 'Sí. Acompañamos el ciclo completo: ingeniería, instalación, supervisión de obra y puesta en marcha con memorias técnicas, diagramas y documentación de entrega.',
  },
  {
    q: '¿Manejan infraestructura de misión crítica 24/7?',
    a: 'Sí. En data centers implementamos redundancia, respaldo UPS y plantas de emergencia, tierras físicas y pararrayos, climatización de precisión y monitoreo, para disponibilidad continua.',
  },
]

/** FAQ — acordeón editorial con contenido real (proceso, normas, cobertura, tiempos). */
export function Faq() {
  const [open, setOpen] = useState<number | null>(0)

  return (
    <section className="section faq" id="faq">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow"><i>05</i>Preguntas frecuentes</span>
          <RevealText tag="h2" text="Preguntas." />
          <p className="lead">Lo que necesitas saber antes de arrancar tu proyecto.</p>
        </Reveal>

        <div className="faq-list">
          {FAQS.map((f, i) => {
            const isOpen = open === i
            return (
              <Reveal key={f.q} delay={(i % 3) * 0.06}>
                <div className={`faq-row${isOpen ? ' is-open' : ''}`}>
                  <button
                    type="button"
                    className="faq-q"
                    aria-expanded={isOpen}
                    onClick={() => setOpen(isOpen ? null : i)}
                  >
                    <span className="faq-ix" aria-hidden="true">
                      ({String(i + 1).padStart(2, '0')})
                    </span>
                    <span className="faq-qt">{f.q}</span>
                    <span className="faq-plus" aria-hidden="true" />
                  </button>
                  <div className="faq-a">
                    <div className="faq-a-inner">
                      <p>{f.a}</p>
                    </div>
                  </div>
                </div>
              </Reveal>
            )
          })}
        </div>
      </div>
    </section>
  )
}
