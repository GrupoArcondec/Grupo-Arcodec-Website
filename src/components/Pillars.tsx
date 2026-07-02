import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { ClipReveal } from './ClipReveal'
import { photo } from '../lib/data'

const IE = [
  'Proyectos eléctricos integrales',
  'Corriente alterna (AC) y directa (DC)',
  'Estudios eléctricos especializados',
  'Diseño de red de tierras',
  'Sistemas fotovoltaicos',
  'Mantenimiento preventivo y correctivo',
]
const DC = [
  'Construcción llave en mano',
  'Sistema de respaldo UPS (Power System)',
  'Tablero de distribución DC tipo BDCBB',
  'Generadores de emergencia',
  'Plantas de corriente directa',
  'Inversores y banco de baterías',
  'Sistema de tierras física y pararrayos',
  'Ingeniería civil para data center',
]

export function Pillars() {
  return (
    <section className="section" id="servicios">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow">Lo que hacemos</span>
          <RevealText tag="h2" text="Dos disciplinas, una sola corriente." accent="una sola corriente." />
          <p className="lead">
            De la subestación al rack: ingeniería eléctrica e implementación de data centers
            ejecutadas por un mismo equipo, llave en mano, desde la etapa conceptual hasta la
            entrega final.
          </p>
        </Reveal>

        <div className="pillars">
          <Reveal>
            <article className="pillar" style={{ ['--accent' as string]: 'var(--electric)' }}>
              <div className="pillar-media">
                <ClipReveal className="clip-fill">
                  <img src={photo('potencia-segura-y-eficiente.jpg')} alt="Potencia segura y eficiente" loading="lazy" />
                </ClipReveal>
              </div>
              <div className="pillar-top">
                <div className="pillar-ico">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinejoin="round">
                    <path d="M13 2 4.5 13.5H11l-1 8L19.5 9.5H13z" />
                  </svg>
                </div>
                <span className="pillar-ix">01 / Ingeniería</span>
              </div>
              <h3>Ingeniería eléctrica</h3>
              <p>Sistemas eléctricos diseñados para operar desde el primer día: potencia segura,
                eficiente y normada para infraestructura crítica e industria.</p>
              <div className="svc-list">
                {IE.map((s, i) => (
                  <div className="svc" key={s}><i>{String(i + 1).padStart(2, '0')}</i>{s}</div>
                ))}
              </div>
            </article>
          </Reveal>

          <Reveal delay={0.1}>
            <article className="pillar" style={{ ['--accent' as string]: 'var(--amp)' }}>
              <div className="pillar-media">
                <ClipReveal className="clip-fill">
                  <img src={photo('infraestructura-que-conecta.jpg')} alt="Infraestructura que conecta" loading="lazy" />
                </ClipReveal>
              </div>
              <div className="pillar-top">
                <div className="pillar-ico">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2} strokeLinejoin="round">
                    <rect x="3" y="4" width="18" height="6" rx="1.5" />
                    <rect x="3" y="14" width="18" height="6" rx="1.5" />
                    <path d="M7 7h.01M7 17h.01" />
                  </svg>
                </div>
                <span className="pillar-ix">02 / Centro de datos</span>
              </div>
              <h3>Data centers</h3>
              <p>Construcción llave en mano e infraestructura crítica que respalda tu operación
                24/7: energía, respaldo y continuidad sin puntos únicos de falla.</p>
              <div className="svc-list">
                {DC.map((s, i) => (
                  <div className="svc" key={s}><i>{String(i + 1).padStart(2, '0')}</i>{s}</div>
                ))}
              </div>
            </article>
          </Reveal>
        </div>
      </div>
    </section>
  )
}
