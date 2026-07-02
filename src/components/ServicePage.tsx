import { useParams, Link } from 'react-router-dom'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { SERVICE_CATS, SERVICE_DETAIL, srvImg, WHATSAPP } from '../lib/data'

const fallbackImg = 'https://arcondec.mx/Servicios/images/PROELE/1.jpg'
const onImgErr = (e: React.SyntheticEvent<HTMLImageElement>) => {
  e.currentTarget.src = fallbackImg
}

export function ServicePage() {
  const { slug = '' } = useParams()

  let service = null
  let disc = ''
  for (const cat of SERVICE_CATS) {
    const s = cat.services.find((x) => x.slug === slug)
    if (s) {
      service = s
      disc = cat.label
      break
    }
  }

  if (!service) {
    return (
      <div className="section wrap svc-404">
        <span className="eyebrow"><i>404</i></span>
        <h1>Servicio no encontrado.</h1>
        <Link className="btn btn-amp" to="/#servicios">Ver todos los servicios</Link>
      </div>
    )
  }

  const d = SERVICE_DETAIL[service.slug]
  const others = SERVICE_CATS.flatMap((c) => c.services).filter((s) => s.slug !== slug)

  return (
    <article className="svc">
      <header className="section svc-hero">
        <div className="wrap">
          <Link className="svc-back fade-up in-view" to="/#servicios">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
              <path d="M19 12H5M11 18l-6-6 6-6" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            Servicios
          </Link>
          <span className="eyebrow fade-up in-view" style={{ animationDelay: '.05s' }}><i>{disc}</i></span>
          <RevealText tag="h1" className="svc-title" delay={0.1} text={service.title} />
          <Reveal delay={0.2}>
            <p className="svc-hero-lead">{d.hero}</p>
            {d.sub && <p className="svc-hero-sub">{d.sub}</p>}
            <div className="svc-hero-row">
              <a className="btn btn-amp" href={WHATSAPP} target="_blank" rel="noopener">Habla con un asesor</a>
              {d.range && <span className="svc-range">{d.range}</span>}
              {d.scope && <span className="svc-range">{d.scope}</span>}
            </div>
          </Reveal>
        </div>
      </header>

      <div className="wrap svc-gallery">
        {[1, 2, 3].map((n, i) => (
          <Reveal key={n} delay={i * 0.08}>
            <span className="svc-shot">
              <img src={srvImg(service!.code, n)} alt="" loading="lazy" onError={onImgErr} />
            </span>
          </Reveal>
        ))}
      </div>

      <section className="section svc-body">
        <div className="wrap svc-grid">
          <Reveal className="svc-intro">
            {d.intro.map((p, i) => (
              <p key={i}>{p}</p>
            ))}
          </Reveal>
          <Reveal delay={0.1} className="svc-caps">
            <span className="svc-caps-h">Servicios especializados</span>
            <ul>
              {service.capabilities.map((c) => (
                <li key={c}>{c}</li>
              ))}
            </ul>
            {d.norms.length > 0 && (
              <div className="svc-norms">
                {d.norms.map((n) => (
                  <span key={n}>{n}</span>
                ))}
              </div>
            )}
          </Reveal>
        </div>
      </section>

      {d.process && (
        <section className="section svc-process">
          <div className="wrap">
            <Reveal><span className="eyebrow"><i>Proceso</i></span></Reveal>
            <div className="svc-steps">
              {d.process.map((p, i) => (
                <Reveal delay={i * 0.06} key={p.t}>
                  <div className="svc-step">
                    <span className="svc-step-n">{String(i + 1).padStart(2, '0')}</span>
                    <h3>{p.t}</h3>
                    <p>{p.d}</p>
                  </div>
                </Reveal>
              ))}
            </div>
          </div>
        </section>
      )}

      <section className="section svc-benefits">
        <div className="wrap">
          <Reveal><span className="eyebrow"><i>Beneficios</i></span></Reveal>
          <div className="svc-bgrid">
            {d.benefits.map((b, i) => (
              <Reveal delay={i * 0.06} key={b.t}>
                <div className="svc-b">
                  <span className="svc-b-n">{String(i + 1).padStart(2, '0')}</span>
                  <h3>{b.t}</h3>
                  <p>{b.d}</p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

      <section className="section svc-end">
        <div className="wrap">
          <Reveal>
            <RevealText tag="h2" text={d.cta.title} />
            <p className="lead">{d.cta.copy}</p>
            <a className="btn btn-amp" href={WHATSAPP} target="_blank" rel="noopener">Habla con un asesor</a>
          </Reveal>

          <div className="svc-others">
            <span className="svc-others-h">Otros servicios</span>
            <div className="svc-others-list">
              {others.map((s) => (
                <Link className="svc-other" to={`/servicios/${s.slug}`} key={s.slug}>
                  {s.title}
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
                    <path d="M7 17 17 7M9 7h8v8" strokeLinecap="round" strokeLinejoin="round" />
                  </svg>
                </Link>
              ))}
            </div>
          </div>
        </div>
      </section>
    </article>
  )
}
