import * as THREE from 'three'
import { gsap } from 'gsap'
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js'
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js'
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js'
import { ShaderPass } from 'three/examples/jsm/postprocessing/ShaderPass.js'
import { MX_STATES } from '../lib/geo'
import { NODES, CATS, type MapNode } from '../lib/data'

const BLOOM_LAYER = 1

type OnActive = (node: MapNode) => void

/** Mapa 3D de México con nodos de proyectos, arcos de "corriente" y auto-ciclo. */
export class MexicoMap {
  private canvas: HTMLCanvasElement
  private onActive: OnActive
  private renderer?: THREE.WebGLRenderer
  private scene?: THREE.Scene
  private camera?: THREE.PerspectiveCamera
  private mapGroup?: THREE.Group
  private bloomComposer?: EffectComposer
  private finalComposer?: EffectComposer
  private raf: number | null = null
  private running = false
  private clock = new THREE.Clock()

  private nodeMeshes: THREE.Mesh[] = []
  private arcs: { curve: THREE.QuadraticBezierCurve3; pulse: THREE.Sprite; t: number }[] = []
  private igniteFn?: () => void

  private raycaster = new THREE.Raycaster()
  private mouse = new THREE.Vector2(-2, -2)
  private hovered: THREE.Mesh | null = null
  private autoIndex = 0
  private autoTimer = 0
  private dragging = false
  private lastX = 0
  private targetRotY = 0.35
  private curRotY = 0.35
  private velY = 0

  // proyección equirectangular centrada en México
  private lon0 = -102
  private lat0 = 23.6
  private SF = 6
  private cosL = Math.cos((23.6 * Math.PI) / 180)

  constructor(canvas: HTMLCanvasElement, onActive: OnActive) {
    this.canvas = canvas
    this.onActive = onActive
  }

  private proj = (lon: number, lat: number): [number, number] => [
    (lon - this.lon0) * this.cosL * this.SF,
    (lat - this.lat0) * this.SF,
  ]

  private glowTexture(color: string) {
    const c = document.createElement('canvas')
    c.width = c.height = 128
    const g = c.getContext('2d')!
    const gr = g.createRadialGradient(64, 64, 0, 64, 64, 64)
    gr.addColorStop(0, color)
    gr.addColorStop(0.25, color)
    gr.addColorStop(1, 'rgba(0,0,0,0)')
    g.fillStyle = gr
    g.fillRect(0, 0, 128, 128)
    const t = new THREE.Texture(c)
    t.needsUpdate = true
    return t
  }

  private resize = () => {
    if (!this.renderer || !this.camera) return
    const w = this.canvas.clientWidth
    const h = this.canvas.clientHeight
    this.renderer.setSize(w, h, false)
    this.bloomComposer?.setSize(w, h)
    this.finalComposer?.setSize(w, h)
    this.camera.aspect = w / h
    this.camera.updateProjectionMatrix()
  }

  /** Selective bloom: solo nodos/arcos/"corriente" brillan (capa BLOOM_LAYER),
   *  el resto del mapa se mantiene nítido. Glow estilo Ascend/Rockstar sobre fondo claro. */
  private setupPost() {
    const r = this.renderer, scene = this.scene, camera = this.camera
    if (!r || !scene || !camera) return
    const w = this.canvas.clientWidth || 1
    const h = this.canvas.clientHeight || 1

    const renderScene = new RenderPass(scene, camera)
    const bloomPass = new UnrealBloomPass(new THREE.Vector2(w, h), 0.85, 0.55, 0)
    const bloomComposer = new EffectComposer(r)
    bloomComposer.renderToScreen = false
    bloomComposer.addPass(renderScene)
    bloomComposer.addPass(bloomPass)

    const mixPass = new ShaderPass(
      new THREE.ShaderMaterial({
        uniforms: {
          baseTexture: { value: null },
          bloomTexture: { value: bloomComposer.renderTarget2.texture },
        },
        vertexShader:
          'varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
        fragmentShader:
          'uniform sampler2D baseTexture; uniform sampler2D bloomTexture; varying vec2 vUv;' +
          'void main(){ gl_FragColor = texture2D(baseTexture,vUv) + vec4(1.0)*texture2D(bloomTexture,vUv); }',
        defines: {},
      }),
      'baseTexture',
    )
    mixPass.needsSwap = true

    const finalComposer = new EffectComposer(r)
    finalComposer.addPass(renderScene)
    finalComposer.addPass(mixPass)

    this.bloomComposer = bloomComposer
    this.finalComposer = finalComposer
  }

  init() {
    const renderer = new THREE.WebGLRenderer({ canvas: this.canvas, antialias: true, alpha: true })
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.8))
    this.renderer = renderer

    const scene = new THREE.Scene()
    scene.fog = new THREE.FogExp2(0x081428, 0.0016)
    this.scene = scene

    const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 4000)
    this.camera = camera

    scene.add(new THREE.AmbientLight(0xffffff, 0.95))
    const d1 = new THREE.DirectionalLight(0xffffff, 0.8)
    d1.position.set(60, 140, 80)
    scene.add(d1)
    const d2 = new THREE.DirectionalLight(0xc9d8f0, 0.5)
    d2.position.set(-90, 60, -40)
    scene.add(d2)

    const mapGroup = new THREE.Group()
    scene.add(mapGroup)
    this.mapGroup = mapGroup

    // estados extruidos
    const fillMat = new THREE.MeshStandardMaterial({
      color: 0xd2ddee, emissive: 0xb9c9e2, emissiveIntensity: 0.18,
      metalness: 0.1, roughness: 0.78, transparent: true, opacity: 0.95,
    })
    const edgeMat = new THREE.LineBasicMaterial({ color: 0x1b3fa0, transparent: true, opacity: 0.5 })
    const statesGroup = new THREE.Group()

    MX_STATES.forEach((st) => {
      st.p.forEach((ring) => {
        const shape = new THREE.Shape()
        ring.forEach((pt, i) => {
          const [x, y] = this.proj(pt[0], pt[1])
          i ? shape.lineTo(x, y) : shape.moveTo(x, y)
        })
        const geo = new THREE.ExtrudeGeometry(shape, { depth: 1.1, bevelEnabled: false })
        statesGroup.add(new THREE.Mesh(geo, fillMat))
        const eg = new THREE.EdgesGeometry(geo, 28)
        statesGroup.add(new THREE.LineSegments(eg, edgeMat))
      })
    })
    statesGroup.rotation.x = -Math.PI / 2
    mapGroup.add(statesGroup)

    // grid bajo el mapa
    const grid = new THREE.GridHelper(420, 42, 0x6e96ff, 0xb9c9e2)
    const gm = grid.material as THREE.Material
    gm.transparent = true
    gm.opacity = 0.4
    grid.position.y = -0.2
    mapGroup.add(grid)

    // nodos
    const nodeGroup = new THREE.Group()
    nodeGroup.rotation.x = -Math.PI / 2
    mapGroup.add(nodeGroup)
    const pulseGeo = new THREE.SphereGeometry(1, 16, 16)

    NODES.forEach((n) => {
      const [x, y] = this.proj(n.lon, n.lat)
      const col = new THREE.Color(CATS[n.cat].color)
      const z = 2.6
      const stemMat = new THREE.LineBasicMaterial({ color: col, transparent: true, opacity: 0.5 })
      const stemGeo = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(x, y, 0), new THREE.Vector3(x, y, z),
      ])
      nodeGroup.add(new THREE.Line(stemGeo, stemMat))

      const r = n.hq ? 1.7 : 1.15
      const m = new THREE.Mesh(pulseGeo, new THREE.MeshBasicMaterial({ color: col }))
      m.scale.setScalar(r)
      m.position.set(x, y, z)
      m.userData = { node: n, base: r, col }
      nodeGroup.add(m)
      this.nodeMeshes.push(m)

      const sp = new THREE.Sprite(
        new THREE.SpriteMaterial({
          map: this.glowTexture(CATS[n.cat].color), color: 0xffffff, transparent: true,
          opacity: 0.85, blending: THREE.NormalBlending, depthWrite: false,
        }),
      )
      const spBase = n.hq ? 14 : 9
      sp.scale.setScalar(spBase)
      sp.position.set(x, y, z)
      sp.userData.base = spBase
      m.userData.sprite = sp
      nodeGroup.add(sp)

      const ringS = new THREE.Sprite(
        new THREE.SpriteMaterial({
          map: this.glowTexture(CATS[n.cat].color), transparent: true, opacity: 0,
          blending: THREE.NormalBlending, depthWrite: false,
        }),
      )
      ringS.position.set(x, y, z)
      ringS.userData = { t: Math.random(), base: n.hq ? 1 : 0.7 }
      nodeGroup.add(ringS)
      m.userData.ring = ringS
    })

    // arcos desde la matriz (Monterrey)
    const hqNode = NODES.find((n) => n.hq)!
    const [hx, hy] = this.proj(hqNode.lon, hqNode.lat)
    const arcGroup = new THREE.Group()
    arcGroup.rotation.x = -Math.PI / 2
    mapGroup.add(arcGroup)

    NODES.filter((n) => !n.hq).forEach((n) => {
      const [x, y] = this.proj(n.lon, n.lat)
      const mid = new THREE.Vector3((hx + x) / 2, (hy + y) / 2, 18 + Math.hypot(hx - x, hy - y) * 0.16)
      const curve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(hx, hy, 2.6), mid, new THREE.Vector3(x, y, 2.6),
      )
      const pts = curve.getPoints(60)
      const g = new THREE.BufferGeometry().setFromPoints(pts)
      const mat = new THREE.LineBasicMaterial({ color: 0xe6a800, transparent: true, opacity: 0.4 })
      arcGroup.add(new THREE.Line(g, mat))
      const pulse = new THREE.Sprite(
        new THREE.SpriteMaterial({
          map: this.glowTexture('#E6A800'), transparent: true, opacity: 0.95,
          blending: THREE.NormalBlending, depthWrite: false,
        }),
      )
      pulse.scale.setScalar(5)
      arcGroup.add(pulse)
      this.arcs.push({ curve, pulse, t: Math.random() })
    })

    // marcar nodos + arcos + "corriente" para que brillen (selective bloom)
    nodeGroup.traverse((o) => o.layers.enable(BLOOM_LAYER))
    arcGroup.traverse((o) => o.layers.enable(BLOOM_LAYER))

    // encuadre automático
    const box = new THREE.Box3().setFromObject(statesGroup)
    const c = box.getCenter(new THREE.Vector3())
    const size = box.getSize(new THREE.Vector3())
    mapGroup.position.x = -c.x
    mapGroup.position.z = -c.z
    const maxDim = Math.max(size.x, size.z)
    const isMobile = window.innerWidth < 700
    camera.position.set(0, maxDim * (isMobile ? 1.15 : 0.92), maxDim * (isMobile ? 1.15 : 1.02))
    camera.lookAt(0, 0, 0)

    this.setupPost()
    this.resize()
    window.addEventListener('resize', this.resize)
    this.attachInteraction()

    // ignición al entrar en vista
    let ignited = false
    this.igniteFn = () => {
      if (ignited) return
      ignited = true
      this.nodeMeshes.forEach((m, i) => {
        const base = m.userData.base as number
        m.scale.setScalar(0.001)
        ;(m.userData.sprite as THREE.Sprite).material.opacity = 0
        gsap.to(m.scale, { x: base, y: base, z: base, duration: 0.8, delay: i * 0.12, ease: 'back.out(2)' })
        gsap.to((m.userData.sprite as THREE.Sprite).material, { opacity: 0.9, duration: 0.8, delay: i * 0.12 })
      })
    }
  }

  private attachInteraction() {
    const canvas = this.canvas
    canvas.addEventListener('pointermove', (e) => {
      const r = canvas.getBoundingClientRect()
      this.mouse.x = ((e.clientX - r.left) / r.width) * 2 - 1
      this.mouse.y = -((e.clientY - r.top) / r.height) * 2 + 1
      if (this.dragging) {
        this.velY = (e.clientX - this.lastX) * 0.005
        this.targetRotY += this.velY
        this.lastX = e.clientX
      }
    })
    canvas.addEventListener('pointerdown', (e) => {
      this.dragging = true
      this.lastX = e.clientX
      canvas.style.cursor = 'grabbing'
    })
    window.addEventListener('pointerup', () => {
      this.dragging = false
      canvas.style.cursor = 'grab'
    })
    canvas.style.cursor = 'grab'
    canvas.addEventListener('pointerleave', () => this.mouse.set(-2, -2))
  }

  /** Enfoca el primer nodo de una categoría (desde la leyenda). */
  focusCategory(cat: string) {
    const n = NODES.find((nn) => nn.cat === cat)
    if (n) {
      this.onActive(n)
      this.autoIndex = NODES.indexOf(n)
      this.autoTimer = 0
    }
  }

  private tick = () => {
    const dt = this.clock.getDelta()
    const et = this.clock.elapsedTime
    const { mapGroup, renderer, scene, camera } = this
    if (!mapGroup || !renderer || !scene || !camera) return

    if (!this.dragging) {
      this.targetRotY += 0.0016
      this.velY *= 0.94
    }
    this.curRotY += (this.targetRotY - this.curRotY) * 0.06
    mapGroup.rotation.y = this.curRotY
    mapGroup.rotation.z = (this.mouse.y !== -2 ? this.mouse.y : 0) * 0.04

    this.nodeMeshes.forEach((m) => {
      const sprite = m.userData.sprite as THREE.Sprite
      const ph = et * 2 + m.position.x
      sprite.scale.setScalar((sprite.userData.base as number) * (1 + Math.sin(ph) * 0.12))
      const ring = m.userData.ring as THREE.Sprite
      ring.userData.t += dt * 0.5
      if (ring.userData.t > 1) ring.userData.t = 0
      const rt = ring.userData.t as number
      ring.scale.setScalar((6 + rt * 22) * (ring.userData.base as number))
      ring.material.opacity = (1 - rt) * 0.5
    })

    this.arcs.forEach((a) => {
      a.t += dt * 0.18
      if (a.t > 1) a.t -= 1
      const p = a.curve.getPoint(a.t)
      a.pulse.position.copy(p)
      a.pulse.material.opacity = 0.85 * Math.sin(a.t * Math.PI)
    })

    this.raycaster.setFromCamera(this.mouse, camera)
    const hits = this.raycaster.intersectObjects(this.nodeMeshes, false)
    if (hits.length) {
      const m = hits[0].object as THREE.Mesh
      if (this.hovered !== m) {
        this.hovered = m
        this.onActive(m.userData.node as MapNode)
        this.autoIndex = NODES.indexOf(m.userData.node as MapNode)
        this.autoTimer = 0
      }
      this.canvas.style.cursor = this.dragging ? 'grabbing' : 'pointer'
    } else {
      if (!this.dragging) this.canvas.style.cursor = 'grab'
      this.autoTimer += dt
      if (this.autoTimer > 3.2) {
        this.autoTimer = 0
        this.autoIndex = (this.autoIndex + 1) % NODES.length
        this.onActive(NODES[this.autoIndex])
        const nm = this.nodeMeshes[this.autoIndex]
        const base = nm.userData.base as number
        gsap.fromTo(
          nm.scale,
          { x: base * 1.5, y: base * 1.5, z: base * 1.5 },
          { x: base, y: base, z: base, duration: 0.6, ease: 'power2.out' },
        )
      }
      this.hovered = null
    }

    if (this.bloomComposer && this.finalComposer) {
      // 1) pasada de brillo: solo la capa BLOOM, sin niebla para un glow puro
      const fog = scene.fog
      scene.fog = null
      camera.layers.set(BLOOM_LAYER)
      this.bloomComposer.render()
      // 2) escena completa + composición aditiva del brillo
      camera.layers.set(0)
      scene.fog = fog
      this.finalComposer.render()
    } else {
      renderer.render(scene, camera)
    }
    if (this.running) this.raf = requestAnimationFrame(this.tick)
  }

  start() {
    if (this.running) return
    this.running = true
    this.igniteFn?.()
    this.tick()
  }

  stop() {
    this.running = false
    if (this.raf) cancelAnimationFrame(this.raf)
    this.raf = null
  }

  dispose() {
    this.stop()
    window.removeEventListener('resize', this.resize)
    this.renderer?.dispose()
  }
}
