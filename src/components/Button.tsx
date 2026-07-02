import { type ReactNode } from 'react'
import { useInView } from '../hooks/useInView'

/* ---------- Button ---------- */
type Variant = 'amp' | 'ghost' | 'light'
export function Button({
  children, href, variant = 'amp', external, className = '',
}: {
  children: ReactNode
  href: string
  variant?: Variant
  external?: boolean
  className?: string
}) {
  const cls = `btn ${variant === 'amp' ? 'btn-amp' : variant === 'light' ? 'btn-light' : 'btn-ghost'} ${className}`
  const ext = external ? { target: '_blank', rel: 'noopener' } : {}
  return (
    <a className={cls} href={href} {...ext}>
      {children}
    </a>
  )
}

/* ---------- Slide (label que se desliza en hover, estilo Editorial) ---------- */
export function Slide({ children }: { children: string }) {
  return (
    <span className="btn-t">
      <span data-t={children}>{children}</span>
    </span>
  )
}

/* ---------- Reveal (fade-in-up al entrar en viewport) ---------- */
export function Reveal({
  children, delay = 0, className = '',
}: {
  children: ReactNode
  delay?: number
  className?: string
}) {
  const { ref, inView } = useInView<HTMLDivElement>()
  return (
    <div
      ref={ref}
      className={`fade-up ${inView ? 'in-view' : ''} ${className}`}
      style={{ animationDelay: `${delay}s` }}
    >
      {children}
    </div>
  )
}
