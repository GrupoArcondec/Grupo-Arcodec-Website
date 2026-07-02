import { Reveal } from './Button'
import { RevealText } from './RevealText'

const STEPS = [
  ['01', 'Conceptual', 'Definimos alcance, cargas y criticidad junto a tu equipo técnico.'],
  ['02', 'Diseño', 'Ingeniería eléctrica y estudios especializados, conforme a norma.'],
  ['03', 'Instalación', 'Ejecución llave en mano con materiales y pruebas certificadas.'],
  ['04', 'Supervisión', 'Puesta en marcha, validación y entrega lista para operar.'],
] as const

export function Process() {
  return (
    <section className="section process">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow">Cómo ejecutamos</span>
          <RevealText tag="h2" text="Del concepto a la entrega final." accent="entrega final." />
        </Reveal>
        <div className="steps">
          {STEPS.map(([n, t, d], i) => (
            <Reveal key={n} delay={i * 0.08} className="step">
              <div className="line" /><div className="si">{n}</div>
              <h3>{t}</h3><p>{d}</p>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  )
}
