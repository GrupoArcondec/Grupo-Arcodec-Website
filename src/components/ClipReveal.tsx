import { type ReactNode } from 'react'
import { useInView } from '../hooks/useInView'

/** Revela su contenido con una cortina (clip-path) al entrar en viewport. */
export function ClipReveal({
  children, className = '', delay = 0,
}: {
  children: ReactNode
  className?: string
  delay?: number
}) {
  const { ref, inView } = useInView<HTMLDivElement>()
  return (
    <div
      ref={ref}
      className={`clip-reveal ${inView ? 'in' : ''} ${className}`.trim()}
      style={{ transitionDelay: `${delay}s` }}
    >
      {children}
    </div>
  )
}
