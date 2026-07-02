import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { Slide } from './Button'

const POWER = '\u23FB'

export function BottomNav() {
  const [show, setShow] = useState(false)
  useEffect(() => {
    const onScroll = () => setShow(window.scrollY > 600)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])
  return (
    <div className={`bottomnav ${show ? 'show' : ''}`}>
      <Link to="/" className="bn-mark">ARC<span className="po">{POWER}</span></Link>
      <Link className="btn btn-amp" to={{ pathname: '/', hash: '#contacto' }}><Slide>Iniciar proyecto</Slide></Link>
    </div>
  )
}
