import { useState, type FormEvent } from 'react'
import { Link } from 'react-router-dom'
import { HUBS, WHATSAPP, projImg } from '../../lib/data'
import { LogoArcondec, Reveal } from './ui'

export function TalkStudio() {
  const [sent, setSent] = useState(false)

  const submit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const fd = new FormData(e.currentTarget)
    const nombre = String(fd.get('nombre') || '')
    const email = String(fd.get('email') || '')
    const msg = String(fd.get('mensaje') || '')
    const body = `Hola, soy ${nombre} (${email}). ${msg}`
    window.open(
      `https://wa.me/525530326595?text=${encodeURIComponent(body)}`,
      '_blank',
      'noopener',
    )
    setSent(true)
  }

  const btnTxt = sent ? 'Mensaje listo en WhatsApp ✓' : 'Enviar mensaje'

  return (
    <footer id="contacto">
      {/* sección oscura "Hablemos." con tarjeta de formulario blanca (referencia) */}
      <section className="st-talk-dark">
        <div className="st-wrap">
          <div className="st-talk-grid">
            <Reveal>
              <div className="st-form-card st-form-card--white">
                <h3>
                  ¿Tienes un proyecto <span className="st-dim">en mente?</span>
                </h3>
                <form onSubmit={submit}>
                  <label htmlFor="st-nombre">Tu nombre*</label>
                  <input id="st-nombre" name="nombre" placeholder="Tu nombre*" required />
                  <label htmlFor="st-email">E-mail*</label>
                  <input
                    id="st-email"
                    name="email"
                    type="email"
                    placeholder="E-mail*"
                    required
                  />
                  <label htmlFor="st-msg">Mensaje</label>
                  <textarea
                    id="st-msg"
                    name="mensaje"
                    rows={3}
                    placeholder="Cuéntanos sobre tu proyecto"
                  />
                  <button className="st-pill st-pill--dark" type="submit">
                    <span className="st-pill-flip">
                      <span>{btnTxt}</span>
                      <span aria-hidden="true">{btnTxt}</span>
                    </span>
                    <i className="st-dot" />
                  </button>
                  <p className="fine">
                    Al enviar, tu mensaje se abre en WhatsApp directo con{' '}
                    <a href="https://arcondec.mx" target="_blank" rel="noreferrer">
                      Grupo Arcondec
                    </a>
                    .
                  </p>
                </form>
              </div>
            </Reveal>

            <div className="st-talk-right">
              <Reveal as="h2" mask className="st-display">
                Hablemos.
              </Reveal>
              <Reveal as="p" delay={100} className="st-talk-lead">
                Cuéntanos sobre tu proyecto —{' '}
                <span className="st-dim">
                  ingeniería eléctrica, data center o energía crítica.
                </span>
              </Reveal>
            </div>
          </div>
        </div>
      </section>

      {/* footer claro (referencia: lead + contacto + columnas + wordmark gigante) */}
      <div className="st-talk">
        <div className="st-wrap">
          <div className="st-talk-grid">
            <div>
              <Reveal as="p" className="st-talk-lead">
                ¿Listo para arrancar?{' '}
                <span className="st-dim">
                  Respondemos en 24–48 horas con un plan de alcances y tiempos.
                </span>
              </Reveal>
              <Reveal delay={80}>
                <div className="st-talk-person">
                  <img
                    src={projImg(HUBS[0].file)}
                    alt="Asesoría técnica Arcondec"
                    loading="lazy"
                  />
                  <div>
                    <b>Grupo Arcondec</b>
                    <span>Asesoría técnica</span>
                  </div>
                </div>
              </Reveal>
            </div>
            <div>
              <Reveal delay={120}>
                <div className="st-talk-contact">
                  <a href="tel:+528119341192">81 1934 1192</a>
                  <a className="st-talk-mail" href="mailto:info@arcondec.mx">
                    <i className="st-plus-circle" aria-hidden="true" />
                    info@arcondec.mx
                  </a>
                </div>
              </Reveal>
            </div>
          </div>

          <div className="st-talk-links">
            <Reveal className="st-talk-links-col">
              <span className="st-plus" aria-hidden="true" />
              <p className="label">Navegación</p>
              <ul>
                <li>
                  <a href="/#proyectos">Proyectos</a>
                </li>
                <li>
                  <a href="/#servicios">Servicios</a>
                </li>
                <li>
                  <a href="/#nosotros">Nosotros</a>
                </li>
                <li>
                  <Link to="/blog">Blog</Link>
                </li>
              </ul>
            </Reveal>
            <Reveal delay={80} className="st-talk-links-col">
              <span className="st-plus" aria-hidden="true" />
              <p className="label">Social</p>
              <ul>
                <li>
                  <a href={WHATSAPP} target="_blank" rel="noreferrer">
                    WhatsApp
                  </a>
                </li>
                <li>
                  <a href="https://arcondec.mx" target="_blank" rel="noreferrer">
                    arcondec.mx
                  </a>
                </li>
                <li>
                  <Link to="/trabaja">Trabaja con nosotros</Link>
                </li>
              </ul>
            </Reveal>
          </div>

          <Reveal className="st-talk-logo">
            <LogoArcondec withR />
            <p className="sub">Ingeniería</p>
          </Reveal>
        </div>
      </div>

      <div className="st-talk-foot">
        <span>© 2025 Grupo Arcondec · Monterrey, México</span>
        <nav>
          <Link to="/blog">Blog</Link>
          <Link to="/trabaja">Trabaja con nosotros</Link>
          <a href="https://arcondec.mx" target="_blank" rel="noreferrer">
            arcondec.mx
          </a>
        </nav>
      </div>
    </footer>
  )
}
