import { WHATSAPP, projImg, HUBS, CLIENTS, img } from '../../lib/data'
import { Label, LogoArcondec, Reveal } from './ui'

const AREAS = [
  'Ingeniería eléctrica',
  'Centros de datos',
  'Corriente directa (DC)',
  'Gestión de proyectos',
]

export function HeroStudio() {
  return (
    <>
      <section className="st-hero" id="top">
        <div className="st-hero-top">
          <div className="st-hero-brand">
            <Reveal as="h1" mask className="st-hero-word">
              <LogoArcondec withR />
            </Reveal>
            <Reveal as="span" delay={140} mask className="st-hero-sub">
              Ingeniería
            </Reveal>
          </div>
          <div className="st-hero-services">
            {AREAS.map((a, i) => (
              <Reveal as="span" key={a} delay={220 + i * 90}>
                {a}
              </Reveal>
            ))}
          </div>
        </div>

        <div className="st-hero-plus" aria-hidden="true">
          {Array.from({ length: 4 }).map((_, i) => (
            <span key={i} />
          ))}
        </div>

        <div className="st-hero-bottom">
          <Reveal delay={300} className="st-hero-tag">
            <strong>Nada de promesas vacías.</strong> Infraestructura crítica, ingeniería
            eléctrica y data centers que mantienen tu operación encendida 24/7.
          </Reveal>
          <Reveal delay={380} className="st-hero-copy">
            © 2025 Grupo Arcondec
          </Reveal>
          <Reveal delay={440}>
            <div className="st-hero-card-wrap">
              <div className="st-hero-card-img">
                <img
                  src={projImg(HUBS[5].file)}
                  alt="Equipo Arcondec en obra"
                  loading="eager"
                />
              </div>
              <div className="st-hero-card">
                <div className="st-hero-card-info">
                  <span className="st-small">Asesoría técnica</span>
                  <span className="st-small" style={{ display: 'block' }}>
                    en arcondec®
                  </span>
                  <b>Grupo Arcondec</b>
                </div>
                <a
                  className="st-pill st-pill--dark"
                  href={WHATSAPP}
                  target="_blank"
                  rel="noreferrer"
                >
                  <span className="st-pill-flip">
                    <span>Hablemos</span>
                    <span aria-hidden="true">Hablemos</span>
                  </span>
                  <i className="st-dot" />
                </a>
              </div>
            </div>
          </Reveal>
        </div>
      </section>

      <div className="st-clients">
        <div className="st-clients-top">
          <Reveal>
            <Label>Nuestros clientes</Label>
          </Reveal>
          <Reveal as="p" delay={120}>
            (2025©)
          </Reveal>
        </div>
        <div className="st-clients-grid">
          {CLIENTS.slice(0, 6).map((c, i) => (
            <Reveal
              key={c.f}
              delay={i * 70}
              className="st-client-card st-reveal--drop"
            >
              <img src={img(`clients/${c.f}.png`)} alt={c.n} loading="lazy" />
            </Reveal>
          ))}
        </div>
      </div>
    </>
  )
}
