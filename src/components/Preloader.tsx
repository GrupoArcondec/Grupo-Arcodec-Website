import { useEffect, useState } from 'react'
import { LogoArcondec } from './studio/ui'

/** Intro: pantalla navy con la marca centrada que se disuelve al hero. */
export function Preloader() {
  const [gone, setGone] = useState(false)

  useEffect(() => {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduce) {
      setGone(true)
      return
    }
    document.body.classList.add('loading')
    const t = window.setTimeout(() => {
      setGone(true)
      document.body.classList.remove('loading')
    }, 2100)
    return () => {
      clearTimeout(t)
      document.body.classList.remove('loading')
    }
  }, [])

  return (
    <div id="st-preloader" className={gone ? 'done' : ''} aria-hidden="true">
      <span className="st-plogo">
        <LogoArcondec tone="light" />
      </span>
    </div>
  )
}
