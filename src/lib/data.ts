/* ============================================================
   ARCONDEC · datos y material real
   Único punto de origen de assets. Para empaquetar local, cambia
   ASSET a '' y sirve /assets junto al build.
   ============================================================ */
export const ASSET = 'https://arcondec.mx'
export const img = (p: string) => `${ASSET}/assets/custom/images/${p}`
export const photo = (file: string) => img(`Blogs/${file}`)

export const WHATSAPP =
  'https://wa.me/525530326595?text=Hola%2C%20estoy%20interesado%20en%20los%20servicios%20de%20Grupo%20Arcondec.'

/* ---------- Clientes (logos reales) ---------- */
export interface Client { n: string; f: string }
export const CLIENTS: Client[] = [
  { n: 'Izzi', f: 'izzi' },
  { n: 'Cablemás', f: 'cablemas' },
  { n: 'Bestel', f: 'bestel' },
  { n: 'FEMSA', f: 'femsa' },
  { n: 'Totalplay', f: 'totalplay' },
  { n: 'GTAC', f: 'gtac' },
  { n: 'Delta', f: 'delta' },
  { n: 'Mabe', f: 'mabe' },
  { n: 'Vant', f: 'vant' },
  { n: 'Logrand', f: 'logrand' },
]

/* ---------- Galería "Obra real" (fotografía real) ---------- */
export interface GalleryItem { f: string; t: string; k: string; cls: string }
export const GALLERY: GalleryItem[] = [
  { f: 'soluciones-en-ingenier%C3%ADa-el%C3%A9ctrica.jpg', t: 'Soluciones en ingeniería eléctrica', k: 'Ingeniería', cls: 'w4 h2' },
  { f: 'instalaciones-normadas.jpg', t: 'Instalaciones normadas', k: 'Normatividad', cls: 'w2' },
  { f: 'comunicaci%C3%B3n-eficiente.jpg', t: 'Comunicación eficiente', k: 'Conectividad', cls: 'w2' },
  { f: 'potencia-segura-y-eficiente.jpg', t: 'Potencia segura y eficiente', k: 'Energía', cls: 'w2' },
  { f: 'infraestructura-que-conecta.jpg', t: 'Infraestructura que conecta', k: 'Data center', cls: 'w2' },
  { f: 'infraestructura-cr%C3%ADtica-data-center.jpg', t: 'Infraestructura crítica 24/7', k: 'Continuidad', cls: 'w2' },
]

/* Los archivos de fotografía (para marquee y trail) */
export const PHOTO_FILES = GALLERY.map((g) => g.f)

/* ---------- Proyectos (carrusel) — obra real por capacidad ---------- */
export interface Project { tag: string; title: string; desc: string; f: string }
export const PROJECTS: Project[] = [
  { tag: 'Data center', title: 'Infraestructura crítica 24/7', desc: 'Energía, respaldo y continuidad para área blanca sin puntos únicos de falla.', f: 'infraestructura-cr%C3%ADtica-data-center.jpg' },
  { tag: 'Ingeniería eléctrica', title: 'Potencia segura y eficiente', desc: 'Diseño e instalación de potencia para industria e infraestructura crítica.', f: 'potencia-segura-y-eficiente.jpg' },
  { tag: 'Conectividad', title: 'Infraestructura que conecta', desc: 'Redes y comunicación industrial sobre infraestructura eléctrica especializada.', f: 'infraestructura-que-conecta.jpg' },
  { tag: 'Normatividad', title: 'Instalaciones normadas', desc: 'Cumplimiento de normas y estándares nacionales e internacionales.', f: 'instalaciones-normadas.jpg' },
  { tag: 'Telecom', title: 'Comunicación eficiente', desc: 'Sistemas de comunicación eficientes para infraestructura tecnológica.', f: 'comunicaci%C3%B3n-eficiente.jpg' },
]

/* ---------- Mapa 3D · cobertura por estado ---------- */
export interface Cat { label: string; color: string }
export const CATS: Record<string, Cat> = {
  dc: { label: 'Centro de datos / Hubs', color: '#1B3FA0' },
  telecom: { label: 'Telecom / Redes', color: '#3D6BF5' },
  energy: { label: 'Energía crítica y continuidad', color: '#6E96FF' },
  hvac: { label: 'HVAC / Enfriamiento', color: '#0C2238' },
  mv: { label: 'Media tensión y transformadores', color: '#FFC20E' },
}

export interface MapNode {
  state: string
  city: string
  lon: number
  lat: number
  cat: keyof typeof CATS
  hq?: boolean
  projects: string[]
}
export const NODES: MapNode[] = [
  { state: 'Nuevo León', city: 'Monterrey · Matriz', lon: -100.316, lat: 25.686, cat: 'mv', hq: true,
    projects: ['Sector Montaña (2 fases)', 'Real del Sol (2 fases)', 'Transformador Sector Montaña', 'Torre Obispado — Obra eléctrica', 'Matriz MTY — VRF y adicionales', 'Mantenimiento a chillers'] },
  { state: 'Ciudad de México', city: 'Valle de México', lon: -99.133, lat: 19.432, cat: 'dc',
    projects: ['HUB Central (Confinamiento)', 'TVSA Hermanos Coraje (4 adicionales)', 'Control de acceso · Iztapalapa'] },
  { state: 'Jalisco', city: 'Guadalajara · Zapopan', lon: -103.349, lat: 20.659, cat: 'energy',
    projects: ['Renovación de bancos de baterías (Litio)', 'Cambio de bancos (Plomo → Litio)', 'Emergencia inversor', 'Zapopan Critical Power', 'Tepatitlán — Emergencia inversores', 'Cd. Guzmán — Cambio de bancos'] },
  { state: 'Baja California', city: 'Tijuana', lon: -117.038, lat: 32.514, cat: 'telecom',
    projects: ['Infraestructura Tijuana'] },
  { state: 'Chihuahua', city: 'Chihuahua · Juárez', lon: -106.069, lat: 28.632, cat: 'dc',
    projects: ['CTR Industries (2 fases)', 'CTR Washington', 'Instalación de tubería · intercomunicar gabinetes'] },
  { state: 'Tamaulipas', city: 'Matamoros', lon: -97.504, lat: 25.869, cat: 'energy',
    projects: ['Suministro de baterías para UPS', 'Matamoros — Bancos de baterías'] },
  { state: 'Hidalgo', city: 'Pachuca', lon: -98.736, lat: 20.121, cat: 'telecom',
    projects: ['FTTH Pachuca (2 fases)'] },
  { state: 'Tlaxcala', city: 'Tlaxcala', lon: -98.237, lat: 19.318, cat: 'dc',
    projects: ['Infraestructura Tlaxcala'] },
  { state: 'Michoacán', city: 'Melchor Ocampo', lon: -101.706, lat: 19.566, cat: 'dc',
    projects: ['Hub Melchor Ocampo'] },
]

/* ---------- Servicios en detalle (scrapeados del sitio oficial) ---------- */
/* Imágenes reales: https://arcondec.mx/Servicios/images/<CODE>/<n>.jpg  (n: 1–6) */
export const SRV_IMG_BASE = 'https://arcondec.mx/Servicios/images'
export const srvImg = (code: string, n = 1) => `${SRV_IMG_BASE}/${code}/${n}.jpg`

export interface Service {
  slug: string
  code: string      // carpeta de imágenes
  title: string
  tagline: string
  description: string
  capabilities: string[]
}
export interface ServiceCat {
  key: string
  label: string
  blurb: string
  services: Service[]
}

export const SERVICE_CATS: ServiceCat[] = [
  {
    key: 'ingenieria',
    label: 'Ingeniería eléctrica',
    blurb: 'De la subestación al tablero: diseño, instalación y puesta en marcha de sistemas eléctricos normados para industria e infraestructura crítica.',
    services: [
      {
        slug: 'proyectos-electricos-integrales', code: 'PROELE',
        title: 'Proyectos eléctricos integrales',
        tagline: 'Sistemas eléctricos listos para operar',
        description: 'Diseñamos, desarrollamos e instalamos sistemas eléctricos de alto desempeño a la medida de tu operación, con certeza técnica y documentación completa desde el primer día. Experiencia en proyectos desde 225 kVA hasta más de 2.5 MVA, conforme a normas NOM, CFE y NFPA.',
        capabilities: [
          'Transformadores y subestaciones',
          'Tableros auto soportados y de distribución',
          'Ingeniería, instalación y puesta en marcha',
          'Cumplimiento NOM, CFE y NFPA',
          'UVIE (verificación de instalaciones eléctricas)',
          'Trámites y gestorías ante CFE',
        ],
      },
      {
        slug: 'estudios-electricos-especializados', code: 'ESTEL',
        title: 'Estudios eléctricos especializados',
        tagline: 'Diagnósticos confiables y cumplimiento normativo',
        description: 'Estudios que garantizan instalaciones seguras, eficientes y en cumplimiento con las normas más exigentes, con diagnósticos confiables y documentación técnica completa. Desde ingeniería de detalle hasta código de red, calidad de energía, Arc Flash y sistemas de tierra, bajo NOM-001-SEDE, NEC y NFPA 70E.',
        capabilities: [
          'Ingeniería básica y de detalle',
          'Memorias técnicas y de cálculo',
          'Diagramas unifilares y multifilares',
          'Código de red y calidad de energía',
          'Cortocircuito, coordinación de protecciones y Arc Flash',
          'Sistemas de tierra física con mediciones certificadas',
        ],
      },
      {
        slug: 'soluciones-en-corriente-directa-dc', code: 'CORAC',
        title: 'Soluciones en corriente directa (DC)',
        tagline: 'Energía sin interrupciones donde no se puede fallar',
        description: 'Diseñamos, suministramos e implementamos sistemas de corriente directa que aseguran energía continua y segura para aplicaciones críticas. Desde centros de datos hasta industria que requiere disponibilidad 24/7, con acompañamiento técnico de principio a fin.',
        capabilities: [
          'Distribuidores de corriente directa (BDCBB)',
          'Bancos de baterías de litio',
          'Plantas de corriente directa (PDC)',
          'Inversores y rectificadores',
          'Sistemas UPS',
        ],
      },
      {
        slug: 'gestion-integral-de-proyectos-electricos', code: 'GESPR',
        title: 'Gestión integral de proyectos',
        tagline: 'Tu proyecto gestionado como prioridad',
        description: 'Gestionamos cada proyecto con precisión técnica y visión integral, alineando tiempos, disciplinas y documentación desde el primer día. Entregamos obras sin retrabajos y expedientes completos —planos as-built, reportes técnicos y actas firmadas— en entornos donde la continuidad es esencial.',
        capabilities: [
          'Planeación estratégica y estimación técnica',
          'Catálogos, memorias técnicas y planos As-Built',
          'Supervisión técnica y coordinación interdisciplinaria',
          'Acompañamiento en sitio y a distancia',
          'Trazabilidad y entrega documental de cierre',
          'Proyectos en todo México y Latinoamérica',
        ],
      },
    ],
  },
  {
    key: 'datacenter',
    label: 'Centro de datos',
    blurb: 'Construcción llave en mano e infraestructura crítica que respalda tu operación 24/7, conforme a TIA-942, Uptime Institute, NEC y NFPA.',
    services: [
      {
        slug: 'construccion-de-data-center', code: 'COSDC',
        title: 'Construcción llave en mano',
        tagline: 'Infraestructura crítica de máxima disponibilidad',
        description: 'Construcción integral de centros de datos llave en mano, con infraestructura crítica diseñada para máxima disponibilidad, eficiencia y control operativo. Integramos energía de respaldo, climatización de precisión, seguridad física y monitoreo inteligente en una sola solución.',
        capabilities: [
          'Sistema de respaldo UPS',
          'Sistema contra incendios con supresión por gas limpio',
          'Planta de emergencia con transferencia automática',
          'Plantas de corriente directa y tableros DC',
          'Inversores, rectificadores y bancos de baterías',
          'Sistema de tierras físicas y pararrayos',
          'Climatización de precisión (IN-ROW, CRAC/CRAH)',
          'Monitoreo inteligente (BMS / DCIM)',
          'Control de acceso y videovigilancia (CCTV/IP)',
          'Cableado estructurado categoría 6A o superior',
        ],
      },
      {
        slug: 'ingenieria-civil-para-data-center', code: 'CIVDC',
        title: 'Ingeniería civil para data center',
        tagline: 'Obra civil para misión crítica',
        description: 'Infraestructura física diseñada para soportar entornos de misión crítica con precisión estructural, funcional y operativa. Obra civil especializada conforme a TIA-942, NOM, Uptime Institute, NEC y NFPA, pensada para la continuidad operativa del entorno tecnológico.',
        capabilities: [
          'Cimentación y obra estructural especializada',
          'Albañilería técnica y acabados industriales',
          'Cancelería, control de acceso y mamparas técnicas',
          'Confinamiento de espacios de línea a medida',
          'Cálculos y memorias estructurales',
          'Instalaciones hidrosanitarias especiales',
          'Piso falso en Área Blanca',
          'Aislamiento térmico y acústico',
        ],
      },
      {
        slug: 'servicios-de-ingenieria-integral', code: 'INGDC',
        title: 'Servicios de ingeniería integral',
        tagline: 'Ingeniería multidisciplinaria de alta disponibilidad',
        description: 'Ingeniería multidisciplinaria —eléctrica, mecánica y civil— orientada a la alta disponibilidad 24/7, conforme a TIA-942, Uptime Institute, NEC, NFPA 70E y NOM-001-SEDE. Una ingeniería correcta evita reprocesos y fallas, y entrega documentación que respalda decisiones durante todo el ciclo de vida del data center.',
        capabilities: [
          'Ingeniería eléctrica, mecánica y civil (TIA-942 / Uptime)',
          'Memorias técnicas, unifilares y layout electromecánico',
          'Carga térmica, coordinación de protecciones y calidad de energía',
          'Supervisión de obra y cumplimiento normativo',
          'Pruebas integrales de puesta en marcha (commissioning)',
        ],
      },
    ],
  },
]

/* ---------- Proyectos reales (página /Proyectos.aspx — 16 "Hub [Ciudad]") ---------- */
/* Imágenes reales: https://arcondec.mx/assets/custom/images/Proyectos/<archivo> */
export const projImg = (file: string) => img(`Proyectos/${encodeURIComponent(file)}`)

export interface Hub {
  city: string
  state: string
  cat: string
  desc: string
  file: string
}
export const HUBS: Hub[] = [
  { city: 'Apodaca', state: 'Nuevo León', cat: 'Media tensión', desc: 'Sala eléctrica de distribución en media tensión', file: 'Sala-eléctrica-de-distribución-en-media-tensión.jpg' },
  { city: 'Querétaro', state: 'Querétaro', cat: 'Centro de datos', desc: 'Instalación de piso elevado en data center', file: 'Instalación-de-piso-elevado-en-data-center-Querétaro.jpg' },
  { city: 'Valle Oriente', state: 'Nuevo León', cat: 'Centro de datos', desc: 'Centro de datos con charolas de fibra y racks', file: 'Centro-de-datos-con-charolas-de-fibra-y-racks-en-Valle-Oriente.jpg' },
  { city: 'Tijuana', state: 'Baja California', cat: 'Centro de datos', desc: 'Instalación de soporte de charolas en data center', file: 'Instalación-de-soporte-de-charolas-en-data-center-Tijuana.jpg' },
  { city: 'Durango', state: 'Durango', cat: 'Ingeniería eléctrica', desc: 'Instalación eléctrica en cuarto de tableros TGE', file: 'Instalación-eléctrica-en-cuarto-de-tableros-TGE-Durango.jpg' },
  { city: 'Monterrey', state: 'Nuevo León', cat: 'Energía crítica', desc: 'Instalación y pruebas de banco de baterías', file: 'Instalación-y-pruebas-de-banco-de-baterías-en-Monterrey.jpg' },
  { city: 'Tuxpan', state: 'Veracruz', cat: 'Ingeniería eléctrica', desc: 'Sistema de transferencia y tableros eléctricos', file: 'Sistema-de-transferencia-y-tableros-eléctricos-en-Tuxpan.jpg' },
  { city: 'Toluca', state: 'Estado de México', cat: 'Ingeniería eléctrica', desc: 'Infraestructura de charolas y tubería eléctrica', file: 'Infraestructura-de-charolas-y-tubería-eléctrica-en-Toluca.jpg' },
  { city: 'Tepic', state: 'Nayarit', cat: 'Ingeniería eléctrica', desc: 'Instalación de tubería PVC verde y charola metálica', file: 'Instalación-de-tubería-PVC-verde-y-charola-metálica-en-Tepic.jpg' },
  { city: 'Mazatlán', state: 'Sinaloa', cat: 'Ingeniería eléctrica', desc: 'Tendido de cableado en charola industrial', file: 'Tendido-de-cableado-en-charola-industrial-Mazatlán.jpg' },
  { city: 'García', state: 'Nuevo León', cat: 'Obra civil', desc: 'Estructura metálica para cubierta de generador', file: 'Estructura-metálica-para-cubierta-de-generador-en-García.jpg' },
  { city: 'Teziutlán', state: 'Puebla', cat: 'Obra civil', desc: 'Montaje de estructura metálica', file: 'Montaje-de-estructura-metálica-en-proyecto-Teziutlán.jpg' },
  { city: 'San Luis Río Colorado', state: 'Sonora', cat: 'Obra civil', desc: 'Construcción de área segura interior con estructura metálica', file: 'Construcción-de-área-segura-interior-con-estructura-metálica-en-SLRC.jpg' },
  { city: 'Sevilla · CDMX', state: 'Ciudad de México', cat: 'Obra civil', desc: 'Construcción de mezzanine metálico en techo', file: 'Construcción-de-mezanine-metálico-en-techo-Sevilla-CDMX.jpg' },
  { city: 'Santa Fe', state: 'Ciudad de México', cat: 'Obra civil', desc: 'Oficinas corporativas en planta Santa Fe', file: 'Oficinas-corporativas-en-planta-Santa-Fe.jpg' },
  { city: 'Islas Mujeres', state: 'Quintana Roo', cat: 'Logística', desc: 'Traslado de equipos para proyecto', file: 'Traslado-de-equipos-para-proyecto-en-Islas-Mujeres.jpg' },
]

/* Banda de cifras — solo datos verificables (sin inventar métricas) */
export interface Stat { big: string; label: string; count?: number; prefix?: string; suffix?: string }
export const PROJECT_STATS: Stat[] = [
  { big: '+30', label: 'Años de experiencia', count: 30, prefix: '+' },
  { big: '16', label: 'Hubs de proyecto', count: 16 },
  { big: '2.5 MVA', label: 'Capacidad por proyecto' },
  { big: '24/7', label: 'Continuidad crítica' },
]

/* ---------- Blog real (página /Blogs.aspx) ---------- */
export const blogImg = (file: string) => `${ASSET}/Blog/images/BLOG/${file}`

export interface BlogPost {
  title: string
  date: string
  tag: string
  url: string
  img: string
}
export const BLOG_POSTS: BlogPost[] = [
  { title: 'Sistemas contra incendios en centros de datos', date: '8 Sep 2025', tag: 'Data center', url: 'https://arcondec.mx/Blog/Sistema-contra-incendios.aspx', img: blogImg('sistema-contra-incendios.jpg') },
  { title: 'Puesta a tierra y pararrayos en centros de datos', date: '1 Sep 2025', tag: 'Infraestructura', url: 'https://arcondec.mx/Blog/sistemas-tierras-fisicas-pararrayos.aspx', img: blogImg('tierras-fisicas-pararrayos.png') },
  { title: 'El peinado de cables puede salvar la operación', date: '25 Ago 2025', tag: 'Data center', url: 'https://arcondec.mx/Blog/peinado-de-cables-data-center.aspx', img: blogImg('peinado-de-cables_2.jpg') },
  { title: 'Modernización eléctrica y tecnología digital', date: '18 Ago 2025', tag: 'Ingeniería', url: 'https://arcondec.mx/Blog/modernizacion-electrica-mexico-tecnologia-digital.aspx', img: blogImg('modernizacion-electrica_2.jpg') },
  { title: 'Tableros auto soportados y de distribución', date: '11 Ago 2025', tag: 'Ingeniería', url: 'https://arcondec.mx/Blog/Instalacion-Tableros-Auto-Soportados-y-Distribucion.aspx', img: blogImg('Instalacion-Tableros-Auto-Soportados.jpg') },
  { title: 'Cinco tendencias en infraestructura de data centers', date: '11 Ago 2025', tag: 'Tendencias', url: 'https://arcondec.mx/Blog/tendencias-infraestructura-electrica.aspx', img: blogImg('tendencias-infraestructura.jpg') },
  { title: 'La revolución silenciosa de la ingeniería eléctrica en data centers', date: '21 Jul 2025', tag: 'IA · HPC', url: 'https://arcondec.mx/Blog/ingenieria-electrica-ai-hpc.aspx', img: blogImg('revolucion-electrica-centros-de-datos-ia-hpc.jpg') },
  { title: 'La nueva era de la energía directa (400V DC)', date: '14 Jul 2025', tag: 'Corriente directa', url: 'https://arcondec.mx/Blog/400v-dc-transformacion-centros-de-datos.aspx', img: blogImg('nueva-era-de-data-center_pq.jpg') },
]

/* ---------- Detalle real de cada página de servicio (scrapeado de /Servicios/*.aspx) ---------- */
export interface ServiceDetail {
  hero: string                 // tagline principal
  sub?: string                 // subtítulo
  intro: string[]              // párrafos narrativos reales
  benefits: { t: string; d: string }[]
  process?: { t: string; d: string }[]
  norms: string[]
  scope?: string
  range?: string
  cta: { title: string; copy: string }
}

export const SERVICE_DETAIL: Record<string, ServiceDetail> = {
  'proyectos-electricos-integrales': {
    hero: 'Soluciones eléctricas de alto desempeño, listas para operar desde el primer día.',
    sub: 'Ingeniería a la medida de tu operación.',
    intro: [
      'Están diseñados para brindarte total certeza técnica, diagnósticos precisos y documentación completa para el desarrollo, validación o mantenimiento de tus instalaciones eléctricas.',
      'Contamos con experiencia en proyectos desde 225 kVA hasta más de 2.5 MVA, atendiendo necesidades en plantas industriales, centros logísticos, complejos comerciales y desarrollos de alta demanda energética.',
    ],
    benefits: [
      { t: 'Acompañamiento técnico de principio a fin', d: 'Te guiamos antes, durante y después de la implementación con soporte directo de nuestros ingenieros.' },
      { t: 'Agilidad en la ejecución, sin excusas', d: 'Resolvemos rápido, ejecutamos con precisión y entregamos a tiempo. Tu proyecto no se detiene.' },
      { t: 'Menos riesgos, más control', d: 'Evita fallas, paros inesperados y problemas normativos. Diseñamos pensando en la seguridad total de tu operación.' },
    ],
    norms: ['NOM', 'CFE', 'NFPA'],
    range: '225 kVA – 2.5 MVA',
    cta: {
      title: 'Inicia tu proyecto eléctrico industrial con una solución profesional',
      copy: 'Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o ejecutar tu sistema eléctrico de forma segura, eficiente y conforme a norma.',
    },
  },
  'estudios-electricos-especializados': {
    hero: 'Asegura el cumplimiento normativo.',
    sub: 'Tu aliado técnico para garantizar continuidad.',
    intro: [
      'Realizamos estudios eléctricos especializados que garantizan instalaciones seguras, eficientes y en cumplimiento con las normas más exigentes del sector. Ya sea en proyectos nuevos, ampliaciones o procesos de validación, te entregamos diagnósticos confiables y documentación técnica completa.',
      'Nuestra experiencia abarca desde ingeniería básica y de detalle hasta análisis de código de red, calidad de energía, coordinación de protecciones, Arc Flash y sistemas de tierra. Todo desarrollado bajo normativas como NOM-001-SEDE, NEC y NFPA 70E, garantizando respaldo legal, técnico y operativo.',
      'En entornos industriales y de misión crítica, somos el soporte que necesitas para mantener la continuidad operativa y proteger tu infraestructura frente a riesgos eléctricos.',
    ],
    benefits: [
      { t: 'Cumplimiento normativo asegurado', d: 'Nuestros estudios se desarrollan conforme a NOM-001-SEDE, NEC y NFPA 70E, facilitando auditorías, inspecciones y trámites ante CFE, CRE y UVIE.' },
      { t: 'Continuidad operativa sin interrupciones', d: 'Detectamos riesgos eléctricos, deficiencias en protecciones y condiciones críticas que podrían ocasionar paros imprevistos.' },
      { t: 'Base técnica para toma de decisiones', d: 'Entregamos documentación técnica clara, cálculos precisos y diagramas confiables que permiten planificar expansiones, mejoras o nuevas instalaciones.' },
    ],
    norms: ['NOM-001-SEDE', 'NEC', 'NFPA 70E', 'CFE', 'CRE', 'UVIE'],
    cta: {
      title: 'Solicita tu diagnóstico técnico',
      copy: 'Recibe una revisión preliminar de tu instalación para identificar riesgos y oportunidades de mejora.',
    },
  },
  'soluciones-en-corriente-directa-dc': {
    hero: 'Energía sin interrupciones para entornos donde no se puede fallar.',
    sub: 'Corriente directa ideal para tu proyecto.',
    intro: [
      'Diseñamos, suministramos e implementamos sistemas de corriente directa (DC) que garantizan energía continua, segura y conforme a norma para aplicaciones críticas.',
      'Nuestra experiencia abarca desde centros de datos hasta instalaciones industriales que requieren máxima disponibilidad operativa 24/7.',
    ],
    benefits: [
      { t: 'Acompañamiento técnico de principio a fin', d: 'Te guiamos antes, durante y después de la implementación con soporte directo de nuestros ingenieros.' },
      { t: 'Agilidad en la ejecución, sin excusas', d: 'Resolvemos rápido, ejecutamos con precisión y entregamos a tiempo. El proyecto no se detiene.' },
      { t: 'Menos riesgos, más control', d: 'Evita fallas, paros inesperados y problemas normativos. Diseñamos pensando en la seguridad total de tu operación.' },
    ],
    norms: [],
    range: '24/7',
    cta: {
      title: 'Inicia tu proyecto eléctrico industrial con una solución profesional',
      copy: 'Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o ejecutar tu sistema eléctrico de forma segura, eficiente y conforme a norma.',
    },
  },
  'gestion-integral-de-proyectos-electricos': {
    hero: 'Garantizamos control total en cada fase de tu obra.',
    sub: 'De la idea a la entrega, sin complicaciones.',
    intro: [
      'Gestionamos cada proyecto con precisión técnica y visión integral, alineando tiempos, disciplinas y documentación desde el primer día. Nuestro enfoque va más allá de supervisar: anticipamos problemas, proponemos soluciones y aseguramos el cumplimiento de normas nacionales e internacionales.',
      'Nos especializamos en entornos donde la continuidad operativa es esencial: centros de datos, plantas industriales, telecomunicaciones y sistemas 24/7. Coordinamos de forma eficaz a todos los involucrados —desde ingenierías hasta contratistas— asegurando que cada plano, cada memoria y cada avance cumpla estándares como la NOM-001-SEDE, NEC y NFPA 70E.',
      'Con nuestra gestión, tu inversión está respaldada. Recibes expedientes completos, planos as-built, reportes técnicos y actas firmadas que acreditan cada avance. Porque no se trata solo de construir, sino de entregar infraestructura lista para operar con seguridad, eficiencia y confiabilidad.',
    ],
    process: [
      { t: 'Planeación estratégica y estimación técnica', d: 'Elaboración de catálogos, memorias técnicas y planos As-Built.' },
      { t: 'Supervisión técnica y coordinación interdisciplinaria', d: 'Acompañamiento técnico real, tanto en sitio como a distancia, con respuestas inmediatas y decisiones fundamentadas.' },
      { t: 'Entrega documental y cierre del proyecto', d: 'Expedientes completos, planos as-built, reportes técnicos y actas firmadas que acreditan cada avance.' },
    ],
    benefits: [
      { t: 'Control total del proyecto desde el inicio', d: 'Planificación detallada, seguimiento técnico constante y coordinación entre disciplinas para asegurar que cada etapa avance sin contratiempos.' },
      { t: 'Acompañamiento técnico en cada fase', d: 'Para resolver imprevistos, supervisar ejecución y garantizar la correcta interpretación de la ingeniería.' },
      { t: 'Trazabilidad y transparencia en cada entrega', d: 'Cada actividad y decisión queda registrada, asegurando claridad para el cliente y control de calidad durante toda la ejecución.' },
    ],
    norms: ['NOM-001-SEDE', 'NEC', 'NFPA 70E'],
    scope: 'México y Latinoamérica',
    cta: {
      title: 'Agenda una asesoría para tu proyecto',
      copy: 'Atendemos proyectos en todo México y Latinoamérica. Habla con un asesor y lleva tu obra a un caso de éxito.',
    },
  },
  'construccion-de-data-center': {
    hero: 'Infraestructura crítica diseñada para máxima disponibilidad, eficiencia y control operativo.',
    sub: 'Ingeniería especializada para entornos de misión crítica.',
    intro: [
      'Implementamos soluciones integrales para la construcción de centros de datos abarcando desde el diseño técnico hasta la entrega funcional y documentada. Cada componente es desarrollado conforme a las más estrictas normas nacionales e internacionales de operación, seguridad y continuidad.',
      'Atendemos proyectos para empresas que requieren disponibilidad 24/7, baja latencia, redundancia energética y monitoreo en tiempo real. Nuestra experiencia incluye centros financieros, plataformas digitales, servicios en la nube, telecomunicaciones, salud, industria y gobierno.',
    ],
    benefits: [
      { t: 'Acompañamiento técnico de principio a fin', d: 'Te guiamos desde el diseño hasta la implementación con soporte directo de nuestros ingenieros especialistas en infraestructura crítica.' },
      { t: 'Agilidad en la ejecución, sin excusas', d: 'Coordinamos equipos, normativas y entregables para que tu data center avance sin fricciones ni retrasos.' },
      { t: 'Seguridad física y lógica desde el diseño', d: 'Incorporamos control de acceso, videovigilancia, sistemas contra incendios y segregación de espacios desde la ingeniería básica.' },
    ],
    norms: ['Normas nacionales e internacionales', 'Categoría 6A o superior'],
    range: '24/7',
    cta: {
      title: 'Inicia tu proyecto de Data Center con una solución profesional',
      copy: 'Solicita una sesión técnica con nuestro equipo y descubre cómo diseñar e implementar la base tecnológica que tu operación necesita.',
    },
  },
  'ingenieria-civil-para-data-center': {
    hero: 'Infraestructura física diseñada para soportar entornos de misión crítica.',
    sub: 'Construcción de data centers de alta disponibilidad.',
    intro: [
      'Contamos con experiencia en proyectos de infraestructura crítica que requieren precisión estructural, cumplimiento normativo y coordinación técnica en cada detalle constructivo.',
      'Implementamos obras civiles especializadas para centros de datos en cumplimiento con las normativas más exigentes: TIA-942, NOM, Uptime Institute, NEC, NFPA y especificaciones de fabricantes. Nuestros procesos constructivos cumplen con los estándares de disponibilidad TIER I, TIER II, TIER III y TIER IV.',
      'Cada solución que entregamos está diseñada para integrarse con los sistemas eléctricos, mecánicos y de TI de forma segura, funcional y validable ante cualquier auditoría.',
    ],
    benefits: [
      { t: 'Obra civil alineada a normativas', d: 'Diseñamos con base en los requerimientos de TIA-942, NEC y NFPA, asegurando compatibilidad con infraestructura TI, control ambiental y seguridad física.' },
      { t: 'Ejecución técnica sin interrupciones', d: 'Desde la cimentación hasta el piso falso y los aislamientos, cada elemento está coordinado con ingeniería, supervisión y pruebas, evitando retrabajos.' },
      { t: 'Soluciones personalizadas para alta exigencia', d: 'Salas blancas, pasillos confinados, mamparas técnicas, cancelerías especiales y sanitarios adaptados, según las necesidades reales del cliente.' },
    ],
    norms: ['TIA-942', 'Uptime Institute', 'NEC', 'NFPA', 'NOM', 'TIER I–IV'],
    cta: {
      title: 'Inicia tu proyecto de Data Center con una solución profesional',
      copy: 'Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o construir tu centro de datos conforme a las mejores prácticas del sector.',
    },
  },
  'servicios-de-ingenieria-integral': {
    hero: 'Nuestro trabajo va más allá del diseño.',
    sub: 'Ingeniería multidisciplinaria orientada a alta disponibilidad.',
    intro: [
      'En Grupo Arcondec desarrollamos centros de datos e infraestructura crítica, abarcando disciplinas eléctrica, mecánica y civil. Nuestro enfoque se basa en los lineamientos del TIA-942, Uptime Institute, NEC, NFPA 70E y NOM-001-SEDE, asegurando que cada sistema esté diseñado para operar con redundancia, seguridad y disponibilidad 24/7.',
    ],
    benefits: [
      { t: 'Valor estratégico de alta disponibilidad', d: 'Diseñamos soluciones con enfoque de alta disponibilidad operativa (24/7), integrando sistemas redundantes que aseguran estabilidad, control y continuidad incluso en los entornos más críticos.' },
      { t: 'Cumplimiento normativo desde el diseño', d: 'Alineados con estándares internacionales (TIA-942, Uptime Institute, NEC, NFPA) y nacionales (NOM-001-SEDE), minimizando riesgos legales y acelerando la certificación.' },
      { t: 'Reducción de riesgos y costos futuros', d: 'Una ingeniería bien ejecutada evita retrabajos, fallas y paros imprevistos, con documentación técnica sólida que respalda decisiones durante todo el ciclo de vida del data center.' },
      { t: 'Soluciones personalizadas a la medida', d: 'Salas blancas, pasillos confinados, mamparas técnicas, cancelerías especiales y sanitarios adaptados, según las necesidades reales del cliente.' },
    ],
    norms: ['TIA-942', 'Uptime Institute', 'NEC', 'NFPA 70E', 'NOM-001-SEDE'],
    range: '24/7',
    cta: {
      title: 'Inicia tu proyecto de Data Center con una solución profesional',
      copy: 'Solicita una sesión técnica con nuestro equipo y descubre cómo podemos diseñar e implementar la base tecnológica que tu operación necesita.',
    },
  },
}
