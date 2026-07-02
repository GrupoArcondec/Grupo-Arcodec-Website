import { useEffect, useRef, useState } from 'react'
import { useInView } from '../hooks/useInView'

/** Número que cuenta de 0 → value al entrar en viewport (estilo Editorial).
 *  Respeta prefers-reduced-motion (muestra el valor final sin animar). */
export function CountUp({
  value, decimals = 0, prefix = '', suffix = '', duration = 1.4,
}: {
  value: number
  decimals?: number
  prefix?: string
  suffix?: string
  duration?: number
}) {
  const { ref, inView } = useInView<HTMLSpanElement>(0.4)
  const [n, setN] = useState(0)
  const done = useRef(false)

  useEffect(() => {
    if (!inView || done.current) return
    done.current = true

    const reduce =
      typeof window !== 'undefined' &&
      window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
    if (reduce) {
      setN(value)
      return
    }

    let raf = 0
    let start = 0
    const step = (t: number) => {
      if (!start) start = t
      const p = Math.min((t - start) / (duration * 1000), 1)
      // ease-out cúbico
      const e = 1 - Math.pow(1 - p, 3)
      setN(value * e)
      if (p < 1) raf = requestAnimationFrame(step)
    }
    raf = requestAnimationFrame(step)
    return () => cancelAnimationFrame(raf)
  }, [inView, value, duration])

  const text = n.toLocaleString('es-MX', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  })

  return (
    <span ref={ref} className="countup">
      {prefix}
      {text}
      {suffix}
    </span>
  )
}
