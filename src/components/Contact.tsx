import { useState, type FormEvent } from 'react'
import { Reveal, Slide } from './Button'
import { RevealText } from './RevealText'

/* Número de WhatsApp de ventas (mismo celular que data.ts) */
const WA_NUMBER = '525530326595'

/* Pasos "Cómo trabajamos" — editorial, estilo Editorial */
const STEPS: { t: string; d: string }[] = [
  { t: 'Respuesta rápida.', d: 'Te contactamos en menos de 24 h hábiles.' },
  { t: 'Siguientes pasos claros.', d: 'Recibes un plan de trabajo y tiempos por escrito.' },
  { t: 'Un solo interlocutor.', d: 'Un ingeniero responsable acompaña todo tu proyecto.' },
]

export function Contact() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')

  const valid = name.trim().length > 1 && /^\S+@\S+\.\S+$/.test(email.trim())

  const bodyText = () =>
    `Nombre: ${name.trim()}\nE-mail: ${email.trim()}\n\nMensaje:\n${
      message.trim() || '(sin mensaje)'
    }`

  // NO hay backend: al enviar solo abrimos el cliente de correo del usuario.
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    if (!valid) {
      setError('Escribe tu nombre y un e-mail válido para continuar.')
      return
    }
    setError('')
    const subject = `Nuevo proyecto — ${name.trim()}`
    const href = `mailto:ventas@arcondec.mx?subject=${encodeURIComponent(
      subject,
    )}&body=${encodeURIComponent(bodyText())}`
    window.location.href = href
  }

  // Alternativa: abrir WhatsApp con el mismo texto (acción explícita del usuario).
  const handleWhats = () => {
    if (!valid) {
      setError('Escribe tu nombre y un e-mail válido para continuar.')
      return
    }
    setError('')
    const text = `Hola, soy ${name.trim()}. ${
      message.trim() || 'Me interesa una asesoría con Grupo Arcondec.'
    }`
    window.open(
      `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`,
      '_blank',
      'noopener',
    )
  }

  return (
    <section className="section contact" id="contacto">
      <div className="wrap contact-grid">
        {/* ---------- Columna izquierda: statement + formulario ---------- */}
        <Reveal>
          <span className="eyebrow"><i>07</i>Contáctanos</span>
          <RevealText
            tag="h2"
            style={{ marginTop: 18 }}
            text="Enciende tu próximo proyecto."
            accent="próximo proyecto."
          />
          <p className="lead">
            Cuéntanos qué necesitas. Somos tu aliado estratégico en ingeniería
            eléctrica y centros de datos, y te respondemos con soluciones concretas.
          </p>

          <form className="cf" onSubmit={handleSubmit} noValidate>
            <div className="cf-field">
              <label htmlFor="cf-name">Nombre*</label>
              <input
                id="cf-name"
                name="name"
                type="text"
                autoComplete="name"
                placeholder="Tu nombre"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
              />
            </div>

            <div className="cf-field">
              <label htmlFor="cf-email">E-mail*</label>
              <input
                id="cf-email"
                name="email"
                type="email"
                autoComplete="email"
                placeholder="tu@empresa.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <div className="cf-field">
              <label htmlFor="cf-msg">Mensaje</label>
              <textarea
                id="cf-msg"
                name="message"
                rows={3}
                placeholder="Cuéntanos sobre tu proyecto, ubicación y tiempos…"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
              />
            </div>

            {error && <p className="cf-error" role="alert">{error}</p>}

            <div className="cf-actions">
              <button type="submit" className="btn btn-amp">
                <Slide>Enviar mensaje</Slide>
              </button>
              <button type="button" className="btn btn-ghost" onClick={handleWhats}>
                <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                  <path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.7 4.8-1.3A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.8.7.8-2.7-.2-.3A8 8 0 1 1 12 20zm4.4-6c-.2-.1-1.4-.7-1.6-.8s-.4-.1-.5.1-.6.8-.8 1-.3.2-.5.1a6.5 6.5 0 0 1-1.9-1.2 7.2 7.2 0 0 1-1.3-1.7c-.1-.2 0-.4.1-.5l.4-.4.2-.4a.5.5 0 0 0 0-.4l-.7-1.8c-.2-.5-.4-.4-.5-.4h-.5a.9.9 0 0 0-.7.3 2.8 2.8 0 0 0-.9 2.1 4.9 4.9 0 0 0 1 2.6 11 11 0 0 0 4.3 3.8c.6.3 1.1.4 1.5.5a3.6 3.6 0 0 0 1.6.1c.5-.1 1.4-.6 1.6-1.1s.2-1 .1-1.1-.2-.2-.4-.3z" />
                </svg>
                <Slide>Enviar por WhatsApp</Slide>
              </button>
            </div>
            <p className="cf-note">
              Al enviar se abre tu correo o WhatsApp con el mensaje listo. No
              almacenamos tus datos.
            </p>
          </form>
        </Reveal>

        {/* ---------- Columna derecha: cómo trabajamos + info real ---------- */}
        <Reveal delay={0.1} className="cinfo">
          <div className="cf-steps">
            <span className="cf-steps-label">Cómo trabajamos</span>
            {STEPS.map((s, i) => (
              <div className="cf-step" key={s.t}>
                <i>{String(i + 1).padStart(2, '0')}</i>
                <div>
                  <b>{s.t}</b>
                  <span>{s.d}</span>
                </div>
              </div>
            ))}
          </div>

          <div className="cblock">
            <label>Oficina Monterrey</label>
            <a
              href="https://www.google.com/maps/place/Grupo+Arcondec+S.A.+de+C.V./@25.7124378,-100.3761168,17z"
              target="_blank"
              rel="noopener"
            >
              Calle del Gran Parque 419, Cumbres 2.º Sector,<br />64610 Monterrey, Nuevo León
            </a>
          </div>

          <div className="cblock">
            <label>Llámanos</label>
            <a href="tel:+528119341192">81 1934 1192</a>
            <a href="tel:+528119341194">81 1934 1194</a>
            <a href="tel:+525530326595">Celular: (55) 3032 6595</a>
          </div>

          <div className="cblock">
            <label>Escríbenos</label>
            <a href="mailto:info@arcondec.mx">info@arcondec.mx</a>
            <a href="mailto:ventas@arcondec.mx">ventas@arcondec.mx</a>
            <div className="socials">
              <a href="https://www.facebook.com/VentasArcondec/" target="_blank" rel="noopener" aria-label="Facebook">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V6h-3c-2 0-3.5 1.5-3.5 3.5V12H8v3h2.5v7h3v-7H16l.5-3h-3v-2.2c0-.5.4-.8.9-.8z" /></svg>
              </a>
              <a href="https://www.instagram.com/grupo_arcondec/" target="_blank" rel="noopener" aria-label="Instagram">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}><rect x="3" y="3" width="18" height="18" rx="5" /><circle cx="12" cy="12" r="4" /><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none" /></svg>
              </a>
              <a href="https://mx.linkedin.com/company/grupo-arcondec-s-a-de-c-v" target="_blank" rel="noopener" aria-label="LinkedIn">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.94 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0zM3.5 8.5h3V21h-3zM9 8.5h2.9v1.7h.04c.4-.76 1.4-1.56 2.86-1.56 3.06 0 3.6 2 3.6 4.6V21h-3v-5.2c0-1.24-.02-2.84-1.73-2.84S13.5 14.7 13.5 15.7V21h-3z" /></svg>
              </a>
              <a href="https://www.youtube.com/@GRUPO_ARCONDEC" target="_blank" rel="noopener" aria-label="YouTube">
                <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.7-1.7C19.3 5.2 12 5.2 12 5.2s-7.3 0-8.9.4A2.5 2.5 0 0 0 1.4 7.3C1 8.8 1 12 1 12s0 3.2.4 4.7a2.5 2.5 0 0 0 1.7 1.7c1.6.4 8.9.4 8.9.4s7.3 0 8.9-.4a2.5 2.5 0 0 0 1.7-1.7C23 15.2 23 12 23 12zM9.8 15.3V8.7l5.7 3.3z" /></svg>
              </a>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  )
}
