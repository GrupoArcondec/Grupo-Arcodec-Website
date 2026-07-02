import { useEffect, useRef } from 'react'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { Reveal } from './Button'
import { RevealText } from './RevealText'
import { BLOG_POSTS, photo } from '../lib/data'

gsap.registerPlugin(ScrollTrigger)

/** Extracto genérico y coherente por categoría (una línea descriptiva, sin inventar datos). */
const EXCERPT: Record<string, string> = {
  'Data center': 'Infraestructura crítica y continuidad 24/7.',
  Infraestructura: 'Protección y respaldo sobre bases confiables.',
  Ingeniería: 'Sistemas eléctricos normados, listos para operar.',
  Tendencias: 'Lo que viene en infraestructura eléctrica.',
  'IA · HPC': 'Energía para cómputo de alta densidad.',
  'Corriente directa': 'Energía DC continua para misión crítica.',
}
const excerptFor = (tag: string) =>
  EXCERPT[tag] ?? 'Ingeniería e infraestructura crítica que opera sin fallar.'

/** Blog / Insights — artículos reales del blog de arcondec.mx (enlazan al .aspx real). */
export function Insights() {
  const gridRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const root = gridRef.current
    if (!root || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    const ctx = gsap.context(() => {
      gsap.utils.toArray<HTMLElement>('.blog-media img', root).forEach((img) => {
        const card = img.closest('.blog-card-wrap') as HTMLElement
        gsap.set(img, { scale: 1.2 })
        gsap.fromTo(
          img,
          { yPercent: -9 },
          {
            yPercent: 9,
            ease: 'none',
            scrollTrigger: { trigger: card, start: 'top bottom', end: 'bottom top', scrub: true },
          },
        )
      })
    }, root)
    return () => ctx.revert()
  }, [])

  return (
    <section className="section insights" id="blog">
      <div className="wrap">
        <Reveal className="section-head insights-head">
          <div className="insights-head-lead">
            <span className="eyebrow"><i>06</i>Explora nuestro blog</span>
            <RevealText tag="h2" text="Blog." />
            <p className="lead">Novedades, tendencias y consejos técnicos.</p>
          </div>
          <a className="insights-all" href="https://arcondec.mx/Blogs.aspx" target="_blank" rel="noopener">
            Ver todo el blog
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
              <path d="M7 17 17 7M9 7h8v8" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </a>
        </Reveal>

        <div className="blog-grid" ref={gridRef}>
          {BLOG_POSTS.map((p, i) => (
            <Reveal key={p.url} delay={(i % 4) * 0.06} className="blog-card-wrap">
              <a className="blog-card" href={p.url} target="_blank" rel="noopener">
                <span className="blog-media">
                  <img
                    src={p.img}
                    alt=""
                    loading="lazy"
                    onError={(e) => { (e.currentTarget as HTMLImageElement).src = photo('BLOG_1.jpg') }}
                  />
                </span>
                <span className="blog-body">
                  <span className="blog-meta">
                    <span className="blog-date">{p.date}</span>
                    <span className="blog-dot" aria-hidden="true">·</span>
                    <span className="blog-tag">{p.tag}</span>
                  </span>
                  <h3 className="blog-title">{p.title}</h3>
                  <span className="blog-excerpt">{excerptFor(p.tag)}</span>
                </span>
              </a>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  )
}
