import { Link } from 'react-router-dom'
import { Slide } from './Button'

const POWER = '⏻'

/** Enlaces grandes numerados del footer (firma editorial estilo Editorial). */
const FT_NAV = [
  ['01', 'Servicios', { pathname: '/', hash: '#servicios' }],
  ['02', 'Proyectos', { pathname: '/', hash: '#proyectos' }],
  ['03', 'Cobertura', { pathname: '/', hash: '#cobertura' }],
  ['04', 'Nosotros', { pathname: '/', hash: '#nosotros' }],
  ['05', 'Blog', '/blog'],
  ['06', 'Contacto', { pathname: '/', hash: '#contacto' }],
] as const

export function Footer() {
  return (
    <footer className="ft">
      <div className="wrap">
        <nav className="ft-nav" aria-label="Secciones">
          {FT_NAV.map(([ix, label, to]) => (
            <Link key={label} to={to} className="ft-nav-link">
              <span className="ft-nav-ix" aria-hidden="true">({ix})</span>
              <span className="ft-nav-t">{label}</span>
            </Link>
          ))}
        </nav>

        <div className="ft-grid">
          <div>
            <Link to="/" className="logo-mark">
              ARC<span className="po">{POWER}</span>NDEC
            </Link>
            <p className="ft-tag">
              Más de 30 años de experiencia y cobertura nacional. Operamos desde Monterrey,
              Nuevo León, para toda la República.
            </p>
          </div>
          <a className="btn btn-ghost" href="tel:+528119341192"><Slide>Habla con un asesor</Slide></a>
        </div>
        <div className="ft-bottom">
          <span>Grupo Arcondec S.A. de C.V. · © 2026 · Todos los derechos reservados</span>
          <a href="https://www.arcondec.mx/AvisoPrivacidad.pdf" target="_blank" rel="noopener">
            Aviso de privacidad
          </a>
        </div>
      </div>
    </footer>
  )
}
