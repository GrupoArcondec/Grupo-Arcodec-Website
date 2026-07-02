import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { CountUp } from './CountUp'

export function Market() {
  return (
    <section className="section market" id="contexto">
      <div className="wrap">
        <Reveal className="section-head">
          <span className="eyebrow"><i>03</i>Por qué importa ahora</span>
          <RevealText tag="h2" text="El cuello de botella ya no es el cómputo: es la energía." accent="es la energía." />
          <p className="lead">
            El auge de la IA y el nearshoring disparan la demanda de procesamiento. La
            infraestructura eléctrica se está convirtiendo en el verdadero cuello de botella — y
            en la ventaja competitiva de quien la resuelve a tiempo.
          </p>
        </Reveal>
        <div className="market-grid">
          <Reveal className="mcell">
            <div className="num">US$<span><CountUp value={82.5} decimals={1} /></span>B</div>
            <div className="k">Inversión 2026 – 2031</div>
            <p>Lo que México destinará a construcción y equipamiento de data centers de aquí a 2031.</p>
            <cite>Fuente: Asociación Mexicana de Data Centers (MEXDC)</cite>
          </Reveal>
          <Reveal delay={0.1} className="mcell">
            <div className="num"><span><CountUp value={7} prefix="×" /></span></div>
            <div className="k">Querétaro · capacidad</div>
            <p>10 data centers operando y 12 en construcción: hasta 1,300 MW acumulados en 2031, casi 7 veces la capacidad actual.</p>
            <cite>Polo nacional de data centers</cite>
          </Reveal>
          <Reveal delay={0.2} className="mcell">
            <div className="num"><span>24/7</span></div>
            <div className="k">Continuidad crítica</div>
            <p>Cada proyecto se diseña con respaldo, redundancia y tierras físicas para sostener la operación sin interrupciones.</p>
            <cite>Estándar de ejecución Arcondec</cite>
          </Reveal>
        </div>
      </div>
    </section>
  )
}
