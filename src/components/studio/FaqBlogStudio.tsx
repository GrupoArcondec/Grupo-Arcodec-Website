import { useState } from 'react'
import { Link } from 'react-router-dom'
import { BLOG_POSTS } from '../../lib/data'
import { Reveal } from './ui'

/* Preguntas reales derivadas de los servicios y forma de trabajo de Arcondec */
const FAQS = [
  {
    q: '¿Qué tipo de proyectos eléctricos atienden?',
    a: 'Diseñamos, desarrollamos e instalamos sistemas eléctricos de alto desempeño: transformadores y subestaciones, tableros auto soportados y de distribución, con experiencia en proyectos desde 225 kVA hasta más de 2.5 MVA.',
  },
  {
    q: '¿Trabajan conforme a normas oficiales?',
    a: 'Sí. Cada proyecto se desarrolla conforme a NOM-001-SEDE, NEC, NFPA 70E y lineamientos de CFE. En data centers aplicamos TIA-942 y estándares del Uptime Institute (TIER I–IV).',
  },
  {
    q: '¿Construyen centros de datos llave en mano?',
    a: 'Sí. Integramos energía de respaldo, climatización de precisión, seguridad física, sistemas contra incendios y monitoreo inteligente (BMS/DCIM) en una sola solución, desde el diseño hasta la entrega documentada.',
  },
  {
    q: '¿Qué documentación entregan al cierre?',
    a: 'Expedientes completos: planos as-built, memorias técnicas y de cálculo, reportes y actas firmadas que acreditan cada avance, listos para auditorías y certificaciones.',
  },
  {
    q: '¿Atienden proyectos fuera de Monterrey?',
    a: 'Sí. Operamos en todo México — con 16 hubs de proyecto entregados — y atendemos también proyectos en Latinoamérica.',
  },
  {
    q: '¿Cómo empiezo mi proyecto?',
    a: 'Escríbenos. Agendamos una asesoría técnica con nuestros especialistas, definimos alcances y te entregamos un plan con tiempos claros.',
  },
]

export function FaqStudio() {
  const [open, setOpen] = useState(0)
  return (
    <section className="st-section" id="faq">
      <div className="st-wrap st-faq-grid">
        <div>
          <Reveal as="h2" mask className="st-display">
            FAQ.
          </Reveal>
          <Reveal delay={100} className="st-body">
            <p className="st-faq-desc">
              ¿Tienes dudas? Aquí está todo lo que necesitas saber sobre trabajar con
              nosotros.
            </p>
          </Reveal>
        </div>
        <div className="st-faq-list">
          {FAQS.map((f, i) => (
            <Reveal key={f.q} delay={Math.min(i * 60, 180)}>
              <article
                className={`st-faq-item ${open === i ? 'open' : ''}`}
                onClick={() => setOpen(open === i ? -1 : i)}
              >
                <div className="st-faq-q">
                  {f.q}
                  <span className="st-faq-toggle" aria-hidden="true">
                    +
                  </span>
                </div>
                <div className="st-faq-a">
                  <div>
                    <p className="st-body">{f.a}</p>
                  </div>
                </div>
              </article>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  )
}

/* ---------- Blog ---------- */
export function BlogStudio() {
  const posts = BLOG_POSTS.slice(0, 2)
  const feature = BLOG_POSTS[6]
  return (
    <section className="st-section" id="blog">
      <div className="st-wrap">
        <div className="st-blog-head">
          <Reveal as="h2" delay={80} className="st-h2">
            Tendencias e ideas <span className="st-thin">de nuestro equipo.</span>
          </Reveal>
          <div className="st-blog-head-right">
            <Reveal delay={140} className="st-body">
              <p style={{ maxWidth: 310 }}>
                Mantente al día con nuestros proyectos, tendencias e ideas del sector.
              </p>
            </Reveal>
            <Reveal delay={200}>
              <Link to="/blog" className="st-pill st-pill--dark st-pill--sm">
                <span className="st-pill-flip">
                  <span>Ver todo</span>
                  <span aria-hidden="true">Ver todo</span>
                </span>
                <i className="st-dot" />
              </Link>
            </Reveal>
          </div>
        </div>

        <div className="st-blog-grid">
          {posts.map((p, i) => (
            <Reveal key={p.url} delay={i * 90}>
              <a className="st-blog-card" href={p.url} target="_blank" rel="noreferrer">
                <img src={p.img} alt="" loading="lazy" />
                <span className="st-blog-card-btn" aria-hidden="true" />
                <div className="st-blog-card-bottom">
                  <time>{p.date}</time>
                  <h4>{p.title}</h4>
                  <p className="st-body">{p.tag}</p>
                </div>
              </a>
            </Reveal>
          ))}
          <Reveal delay={180}>
            <a
              className="st-blog-feature"
              href={feature.url}
              target="_blank"
              rel="noreferrer"
            >
              <img src={feature.img} alt="" loading="lazy" />
              <div className="st-blog-feature-top">
                <span className="st-feat-mark">arcondec®</span>
                <span className="st-plus" aria-hidden="true" />
              </div>
              <b>
                ¿Qué hay de nuevo
                <br />
                en infraestructura?
              </b>
            </a>
          </Reveal>
        </div>
      </div>
    </section>
  )
}
