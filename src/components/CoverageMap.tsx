import { useEffect, useRef, useState } from 'react'
import { Reveal } from './Button'
import { CATS, NODES, type MapNode } from '../lib/data'
import { MexicoMap } from '../three/mexicoMap'

export function CoverageMap() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const mapRef = useRef<MexicoMap | null>(null)
  const [active, setActive] = useState<MapNode>(NODES[0])

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    if (typeof window === 'undefined' || !('WebGLRenderingContext' in window)) return

    const map = new MexicoMap(canvas, (n) => setActive(n))
    mapRef.current = map

    let started = false
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            if (!started) {
              map.init()
              started = true
            }
            map.start()
          } else {
            map.stop()
          }
        })
      },
      { threshold: 0.08 },
    )
    io.observe(canvas)

    return () => {
      io.disconnect()
      map.dispose()
    }
  }, [])

  const cat = CATS[active.cat]
  const ns = active.lat >= 0 ? 'N' : 'S'
  const ew = active.lon <= 0 ? 'O' : 'E'

  return (
    <section className="section map-sec map-sec--fused" id="cobertura">
      <div className="wrap">
        <Reveal className="map-head">
          <span className="eyebrow"><i>03</i>Cobertura nacional</span>
          <p className="lead" style={{ marginTop: 18 }}>
            Los mismos proyectos, desplegados por toda la República. Pasa el cursor o toca un nodo
            para ver el detalle de cada estado.
          </p>
        </Reveal>

        <div className="map-stage">
          <Reveal className="map-canvas-wrap">
            <canvas id="mapCanvas" ref={canvasRef} />
            <div className="map-badge"><i />Red en vivo</div>
            <div className="map-hint">Arrastra para rotar · nodos = proyectos</div>
          </Reveal>

          <Reveal delay={0.12} className="map-panel">
            <div className="mp-state">{active.state}</div>
            <div className="mp-city">{active.city}</div>
            <div className="mp-coord">
              {Math.abs(active.lat).toFixed(2)}° {ns} · {Math.abs(active.lon).toFixed(2)}° {ew}
            </div>
            <div className="mp-cat">
              <i style={{ background: cat.color }} />
              <span>{cat.label.split(' / ')[0]}</span>
            </div>
            <ul className="mp-proj">
              {active.projects.map((p) => (
                <li key={p}>{p}</li>
              ))}
            </ul>
            <div className="mp-foot">
              <div className="legend">
                {Object.entries(CATS).map(([k, v]) => (
                  <span
                    key={k}
                    className={`lg ${active.cat === k ? 'active' : ''}`}
                    onClick={() => mapRef.current?.focusCategory(k)}
                  >
                    <i style={{ background: v.color }} />
                    {v.label.split(' / ')[0].split(' y ')[0]}
                  </span>
                ))}
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  )
}
