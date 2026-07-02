import { useEffect, useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { HUBS } from '../lib/data'
import { startLenis, stopLenis } from '../hooks/useLenis'
import { LogoArcondec } from './studio/ui'

const LINKS: Array<[string, string, string?]> = [
  ['/#estudio', 'Estudio'],
  ['/#proyectos', 'Proyectos', String(HUBS.length)],
  ['/blog', 'Blog'],
  ['/#contacto', 'Contacto'],
]

const MENU: Array<[string, string]> = [
  ['/#estudio', 'Estudio'],
  ['/#proyectos', 'Proyectos'],
  ['/#servicios', 'Servicios'],
  ['/#faq', 'FAQ'],
  ['/blog', 'Blog'],
  ['/trabaja', 'Trabaja con nosotros'],
  ['/#contacto', 'Contacto'],
]

function toDest(href: string) {
  if (href.startsWith('/#')) return { pathname: '/', hash: href.slice(1) }
  return href
}

export function Nav() {
  const [scrolled, setScrolled] = useState(false)
  const [open, setOpen] = useState(false)
  const { pathname, hash } = useLocation()

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 30)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  useEffect(() => setOpen(false), [pathname, hash])
  useEffect(() => {
    // overflow:hidden no basta en iOS: se detiene también Lenis y el CSS de
    // .st-menu bloquea el touch-scroll del fondo (touch-action: none)
    document.body.style.overflow = open ? 'hidden' : ''
    if (open) stopLenis()
    else startLenis()
    return () => {
      document.body.style.overflow = ''
      startLenis()
    }
  }, [open])

  return (
    <>
      <header className={`st-nav ${scrolled ? 'scrolled' : ''}`}>
        <div className="st-nav-inner">
          <Link to="/" className="st-nav-logo" aria-label="Arcondec — inicio">
            <LogoArcondec tone="dark" />
          </Link>
          <nav className="st-nav-links">
            {LINKS.map(([href, label, sup]) => (
              <Link key={href} to={toDest(href)}>
                <span className="st-nav-roll">
                  <span>{label}</span>
                  <span aria-hidden="true">{label}</span>
                </span>
                {sup && <sup>{sup}</sup>}
              </Link>
            ))}
          </nav>
          <button
            className={`st-burger ${open ? 'open' : ''}`}
            aria-label={open ? 'Cerrar menú' : 'Abrir menú'}
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
          >
            <i />
            <i />
          </button>
        </div>
      </header>

      <div className={`st-menu ${open ? 'open' : ''}`} onClick={() => setOpen(false)}>
        <aside className="st-menu-panel" onClick={(e) => e.stopPropagation()}>
          <nav className="st-menu-main">
            {MENU.map(([href, label]) => (
              <Link key={href} to={toDest(href)} onClick={() => setOpen(false)}>
                {label}
              </Link>
            ))}
          </nav>
          <div className="st-menu-foot">
            <div className="st-menu-contact">
              <a href="tel:+528119341192">81 1934 1192</a>
              <a className="st-menu-mail" href="mailto:info@arcondec.mx">
                <i className="st-plus" />
                info@arcondec.mx
              </a>
            </div>
            <nav className="st-menu-legal">
              <a
                href="https://www.arcondec.mx/AvisoPrivacidad.pdf"
                target="_blank"
                rel="noopener noreferrer"
              >
                Aviso de privacidad
              </a>
            </nav>
            <p className="st-menu-copy">
              © 2026 <LogoArcondec withR />
            </p>
          </div>
        </aside>
      </div>
    </>
  )
}
