import {
  createElement,
  useEffect,
  useRef,
  useState,
  type ElementType,
  type ReactNode,
} from 'react'

/* ---------- aparición en viewport (fade + blur + rise) ----------
   margen solo inferior: con margen negativo arriba + el offset translateY(90px)
   de móvil, los reveals disparaban tardísimo (o nunca, al fondo de la página) */
export function useInViewOnce<T extends HTMLElement>(margin = '0px 0px -10% 0px') {
  const ref = useRef<T | null>(null)
  const [inView, setInView] = useState(false)
  useEffect(() => {
    const el = ref.current
    if (!el) return
    // seguro: si al observar ya está (casi) a la vista, revela directo
    if (el.getBoundingClientRect().top < window.innerHeight * 0.95) {
      setInView(true)
      return
    }
    const io = new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) {
          setInView(true)
          io.disconnect()
        }
      },
      { rootMargin: margin },
    )
    io.observe(el)
    return () => io.disconnect()
  }, [margin])
  return { ref, inView }
}

export function Reveal({
  as = 'div',
  delay = 0,
  className = '',
  mask = false,
  children,
}: {
  as?: ElementType
  delay?: number
  className?: string
  /* máscara: el contenido sube desde abajo con overflow hidden (títulos grandes, como Editorial) */
  mask?: boolean
  children?: ReactNode
}) {
  const { ref, inView } = useInViewOnce<HTMLElement>()
  return createElement(
    as,
    {
      ref,
      className: `st-reveal${mask ? ' st-reveal--mask' : ''} ${inView ? 'is-in' : ''} ${className}`,
      style: { ['--d' as string]: `${delay}ms` },
    },
    mask
      ? createElement('span', { className: 'st-mask' }, createElement('span', null, children))
      : children,
  )
}

/* ---------- wordmark oficial ARC⏻NDEC ----------
   La O es el símbolo de encendido de la marca (anillo con apertura superior
   y barra que baja por la apertura, ámbar amp). Escala en em con el
   font-size heredado. `tone`: 'light' = tinta blanca (fondos navy),
   'dark' = tinta navy (fondos claros); sin tone hereda el color. */
export function LogoArcondec({
  tone,
  withR = false,
  className = '',
}: {
  tone?: 'light' | 'dark'
  withR?: boolean
  className?: string
}) {
  return (
    <span
      className={`st-logotype${tone ? ` st-logotype--${tone}` : ''}${className ? ` ${className}` : ''}`}
      role="img"
      aria-label={withR ? 'arcondec®' : 'arcondec'}
    >
      ARC
      {/* proporciones calcadas de /brand/logo-light.png: anillo abierto arriba
          (±40° desde la vertical) + barra que asoma sobre la altura de caps */}
      <svg
        className="st-po st-po-ico"
        viewBox="0 0 24 26"
        fill="none"
        aria-hidden="true"
        focusable="false"
      >
        <path
          d="M17.79 7.61a9 9 0 1 1-11.58 0"
          stroke="currentColor"
          strokeWidth="2.9"
          strokeLinecap="round"
        />
        <path d="M12 1.6v11.4" stroke="currentColor" strokeWidth="2.9" strokeLinecap="round" />
      </svg>
      NDEC
      {withR && <sup>®</sup>}
    </span>
  )
}

/* ---------- etiqueta de sección: ⊕ Texto ---------- */
export function Label({ children, light = false }: { children: ReactNode; light?: boolean }) {
  return (
    <span className="st-label" style={light ? { color: '#fff' } : undefined}>
      <svg viewBox="0 0 16 16" fill="none" aria-hidden="true">
        <circle cx="8" cy="8" r="7.2" fill="currentColor" />
        <path d="M8 4.6v6.8M4.6 8h6.8" stroke={light ? '#08182b' : '#eef1f6'} strokeWidth="1.6" />
      </svg>
      {children}
    </span>
  )
}

/* ---------- contador animado ---------- */
export function Counter({
  to,
  prefix = '',
  suffix = '',
  duration = 1600,
}: {
  to: number
  prefix?: string
  suffix?: string
  duration?: number
}) {
  const { ref, inView } = useInViewOnce<HTMLSpanElement>('-8% 0px')
  const [val, setVal] = useState(0)
  useEffect(() => {
    if (!inView) return
    let raf = 0
    const t0 = performance.now()
    const tick = (t: number) => {
      const p = Math.min(1, (t - t0) / duration)
      const e = 1 - Math.pow(1 - p, 3)
      setVal(Math.round(to * e))
      if (p < 1) raf = requestAnimationFrame(tick)
    }
    raf = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(raf)
  }, [inView, to, duration])
  return (
    <span ref={ref}>
      {prefix}
      {val}
      {suffix}
    </span>
  )
}

/* ---------- texto que se enciende palabra a palabra con el scroll ---------- */
export function ScrollWords({
  text,
  className = '',
  dimCount = 0,
}: {
  text: string
  className?: string
  /* nº de palabras iniciales que quedan permanentemente atenuadas (Editorial) */
  dimCount?: number
}) {
  const ref = useRef<HTMLParagraphElement | null>(null)
  const [lit, setLit] = useState(0)
  const words = text.split(' ')
  useEffect(() => {
    const el = ref.current
    if (!el) return
    const onScroll = () => {
      const r = el.getBoundingClientRect()
      const vh = window.innerHeight
      // progreso: 0 cuando el bloque entra, 1 cuando su centro pasa el 35% del viewport
      const p = (vh * 0.82 - r.top) / (r.height + vh * 0.35)
      setLit(Math.floor(Math.max(0, Math.min(1, p)) * words.length))
    }
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [words.length])
  return (
    <p ref={ref} className={`st-words ${className}`}>
      {words.map((w, i) => (
        <span key={i} className={`${i < dimCount ? 'dim' : ''} ${i < lit ? 'on' : ''}`.trim()}>
          {w}{' '}
        </span>
      ))}
    </p>
  )
}

/* ---------- botón píldora ---------- */
export function Pill({
  children,
  href,
  dark = true,
  lg = false,
  onClick,
  className = '',
}: {
  children: ReactNode
  href?: string
  dark?: boolean
  lg?: boolean
  onClick?: () => void
  className?: string
}) {
  const cls = `st-pill ${dark ? 'st-pill--dark' : 'st-pill--light'} ${lg ? 'st-pill--lg' : ''} ${className}`
  /* todos los pills llevan dos textos apilados (slide vertical al hover, como Editorial);
     el dot solo acompaña a los pills normales, no al lg */
  const inner = (
    <>
      <span className="st-pill-flip">
        <span>{children}</span>
        <span aria-hidden="true">{children}</span>
      </span>
      {!lg && <i className="st-dot" />}
    </>
  )
  if (href)
    return (
      <a
        className={cls}
        href={href}
        target={href.startsWith('http') ? '_blank' : undefined}
        rel="noreferrer"
      >
        {inner}
      </a>
    )
  return (
    <button className={cls} onClick={onClick} type="button">
      {inner}
    </button>
  )
}

/* ---------- encabezado editorial de sección ---------- */
export function SectionHead({
  label,
  title,
  aside,
  meta,
  copyright = '©2025',
}: {
  label?: ReactNode
  title: string
  aside?: ReactNode
  meta?: string
  copyright?: string | null
}) {
  return (
    <div className="st-sec-head">
      <div className="st-sec-head-col1">
        {label && (
          <Reveal>
            <Label>{label}</Label>
          </Reveal>
        )}
        {meta && (
          <Reveal delay={label ? 140 : 0}>
            <span className={label ? 'st-meta' : 'st-count'}>{meta}</span>
          </Reveal>
        )}
      </div>
      <Reveal as="h2" delay={80} mask className="st-display">
        {title}
        {copyright && <span className="st-copyright">{copyright}</span>}
      </Reveal>
      <aside>
        {aside && (
          <Reveal delay={180} className="st-body">
            {aside}
          </Reveal>
        )}
      </aside>
    </div>
  )
}
