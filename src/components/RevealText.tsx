import { createElement } from 'react'
import { useInView } from '../hooks/useInView'

type Tag = 'h1' | 'h2' | 'h3' | 'span' | 'p'

/** Título con reveal palabra-por-palabra (máscara que sube al entrar en viewport).
 *  `accent` es una subcadena que se pinta en ámbar (como los <em> del diseño). */
export function RevealText({
  text, accent, tag = 'h2', className = '', delay = 0, stagger = 0.05,
  style,
}: {
  text: string
  accent?: string
  tag?: Tag
  className?: string
  delay?: number
  stagger?: number
  style?: React.CSSProperties
}) {
  const { ref, inView } = useInView<HTMLHeadingElement>()

  const aStart = accent ? text.indexOf(accent) : -1
  const aEnd = aStart >= 0 ? aStart + accent!.length : -1

  // partir en palabras conservando el offset de carácter para detectar el acento
  const words: { w: string; start: number }[] = []
  let off = 0
  text.split(' ').forEach((w) => {
    words.push({ w, start: off })
    off += w.length + 1
  })

  return createElement(
    tag,
    { ref, className: `rt ${inView ? 'in' : ''} ${className}`.trim(), style },
    words.map(({ w, start }, i) => {
      const isAccent = aStart >= 0 && start < aEnd && start + w.length > aStart
      return (
        <span className="rt-w" key={i}>
          <span style={{ transitionDelay: `${delay + i * stagger}s` }}>
            {isAccent ? <em>{w}</em> : w}
          </span>
        </span>
      )
    }),
  )
}
