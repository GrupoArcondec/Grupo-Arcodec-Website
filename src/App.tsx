import { useEffect } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import { useLenis, scrollToId, scrollToTop } from './hooks/useLenis'
import { Preloader } from './components/Preloader'
import { Nav } from './components/Nav'
import { TalkStudio } from './components/studio/TalkStudio'
import { WhatsAppFab } from './components/WhatsAppFab'
import { Home } from './components/Home'
import { ServicePage } from './components/ServicePage'
import { Insights } from './components/Insights'
import { Careers } from './components/Careers'

/** Al cambiar de ruta: sube al tope; si hay #hash, desplázate a esa sección.
 *  Reintenta para corregir el desplazamiento cuando el layout se asienta
 *  (intro fijo + imágenes que cargan y cambian las alturas). */
function ScrollManager() {
  const { pathname, hash } = useLocation()
  useEffect(() => {
    if (hash) {
      const go = () => scrollToId(hash)
      const timers = [350, 700, 1100].map((ms) => window.setTimeout(go, ms))
      return () => timers.forEach(clearTimeout)
    }
    scrollToTop()
  }, [pathname, hash])
  return null
}

export default function App() {
  useLenis()

  // iOS Safari solo dispara :active en divs/figures si existe un listener
  // touchstart en el documento (los efectos de tap de las tarjetas lo requieren)
  useEffect(() => {
    const noop = () => {}
    document.addEventListener('touchstart', noop, { passive: true })
    return () => document.removeEventListener('touchstart', noop)
  }, [])

  return (
    <>
      <Preloader />
      <Nav />
      <ScrollManager />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/servicios/:slug" element={<ServicePage />} />
        <Route path="/blog" element={<div className="subpage"><Insights /></div>} />
        <Route path="/trabaja" element={<div className="subpage"><Careers /></div>} />
      </Routes>

      <TalkStudio />
      <WhatsAppFab />
    </>
  )
}
