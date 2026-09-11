# -*- coding: utf-8 -*-
"""Contenido del sitio de Grupo Arcondec, en espanol e ingles.

Los textos son los de arcondec.mx, transcritos literalmente. Si hay que
cambiar una frase, se cambia AQUI y se vuelve a ejecutar `python3 tools/build.py`.

Cada pagina existe en dos idiomas con URL propia:
    ES  ->  /nosotros.html
    EN  ->  /en/about.html
"""

# --------------------------------------------------------------------------
# Datos de contacto (identicos en ambos idiomas salvo el correo de ventas)
# --------------------------------------------------------------------------
CONTACT = {
    "address": "Calle del Gran Parque 419, Cumbres 2o, 64610 Monterrey, N.L.",
    "street": "Calle del Gran Parque 419, Cumbres 2o",
    "city": "Monterrey",
    "region": "NL",
    "zip": "64610",
    "phone1": "81 1934 1192",
    "phone2": "81 1934 1194",
    "mobile": "(55) 3032 6595",
    "phone1_tel": "+528119341192",
    "phone2_tel": "+528119341194",
    "mobile_tel": "+525530326595",
    "mail_info": "info@arcondec.mx",
    "mail_sales_es": "ventas@arcondec.mx",
    "mail_sales_en": "sales@arcondec.mx",
    "mail_rh": "rh@arcondec.mx",
    "mail_quejas": "quejasysugerencias@arcondec.mx",
    "mail_proveedores": "proveedores@arcondec.mx",
    "mail_talento": "talento@arcondec.mx",
    "maps": "https://www.google.com/maps/place/Grupo+Arcondec+S.A.+de+C.V./@25.7124378,-100.3761168,17z",
}

WHATSAPP = (
    "https://wa.me/525530326595?text=Hola,%20Estoy%20interesado%20en%20conocer%20m%C3%A1s"
    "%20sobre%20los%20servicios%20que%20ofrece%20GRUPO%20ARCONDEC.%20%C2%BFPodr%C3%ADan"
    "%20proporcionarme%20informaci%C3%B3n%20adicional%3F%20Agradezco%20de%20antemano%20su"
    "%20atenci%C3%B3n."
)

SOCIAL = [
    ("facebook-f", "Facebook", "https://www.facebook.com/grupoarcondec"),
    ("instagram", "Instagram", "https://www.instagram.com/grupoarcondec"),
    ("linkedin-in", "LinkedIn", "https://www.linkedin.com/company/grupoarcondec/"),
    ("youtube", "YouTube", "https://www.youtube.com/@grupoarcondec"),
]

PRIVACY_PDF = "https://www.arcondec.mx/AvisoPrivacidad.pdf"
LOGIN_URL = "https://apps.arcondec.mx/"
VIDEO_URL = "https://www.youtube.com/watch?v=Q9PNm51CVK8"

# --------------------------------------------------------------------------
# Los servicios, en el orden en que salen en el menú y agrupados por área.
# `key` da el nombre de las fotos: servicios/<key>-N.jpg
#
# Los grupos son solo títulos del menú, no páginas: agrupan visualmente y no
# llevan a ningún lado. Sus etiquetas viven en SERVICE_GROUPS, una sola vez,
# porque las usan tanto la cabecera como el pie.
#
# Corriente Alterna y Diseño de Tierras están dados de alta con TEXTO
# PROVISIONAL, marcado en cada bloque: describe el servicio con exactitud pero
# sin cifras, marcas ni certificaciones, para no afirmar nada sin confirmar.
#
# DADOS DE BAJA en esta reestructura: Estudios Eléctricos, Gestión de Proyectos
# y Servicios de Ingeniería Integral. Sus páginas se eliminaron del sitio.
# --------------------------------------------------------------------------
SERVICE_GROUPS = [
    ("llave", {"es": "Construcción llave en mano", "en": "Turnkey construction"}),
    ("ie",    {"es": "Ingeniería eléctrica",       "en": "Electrical engineering"}),
]

SERVICES = [
    {
        "key": "cosdc",
        # La 11 va primero: es la que se usa de banner y de imagen principal.
        # Entró con número nuevo y no sustituyendo a la 7 a propósito —
        # vercel.json marca /assets/images como `immutable` por un año, así que
        # reemplazar un archivo en su sitio deja a los visitantes recurrentes
        # con la versión vieja hasta 2027. Foto nueva, nombre nuevo.
        # Se retiraron la 8 y la 9: salas vacías con cajas de cartón apiladas,
        # que no muestran obra terminada. Los archivos siguen en disco por si
        # se quieren recuperar.
        "photos": [11, 10, 1, 2, 3, 4, 5, 6],
        "group": "llave",
        "icon": "fal fa-server",
        "slug": {"es": "construccion-data-center", "en": "data-center-construction"},
        "es": {
            "nav": "Construcción Data Centers",
            "title": "Asesoría y construcción de data centers",
            "meta": "Asesoría y construcción de data centers llave en mano: ingeniería, obra civil, infraestructura eléctrica crítica, MEP, sistemas especiales y comisionamiento.",
            "keywords": "construcción data center, llave en mano, proyecto ejecutivo, UPS, planta de emergencia, comisionamiento, UVIE, infraestructura crítica, Grupo Arcondec",
            "h1": "Asesoría y construcción de data centers",
            "lead": "Diseñamos, planificamos, coordinamos y ejecutamos tu centro de datos con un solo proveedor responsable de cada etapa",
            "tagline": "Ingeniería especializada para entornos de misión crítica",
            "intro_h2": "De la ingeniería a la puesta en operación de tu data center",
            "intro": [
                "En Grupo Arcondec integramos el diseño, la obra civil, la infraestructura eléctrica y los sistemas especializados necesarios para construir centros de datos preparados para las exigencias de tu operación.",
                "Partimos del levantamiento de necesidades para desarrollar el proyecto ejecutivo y coordinar cada disciplina bajo un mismo alcance. Nuestro servicio comprende la construcción, la instalación de equipos, las pruebas de integración y el comisionamiento, hasta la entrega funcional y documentada.",
                "Alineamos cada decisión con los requerimientos de capacidad, disponibilidad, seguridad y crecimiento de tu proyecto, con acompañamiento técnico durante todo el proceso.",
            ],
            "cta_btn": "Cuéntanos sobre tu proyecto",
            "list_title": "Soluciones integrales para cada etapa del proyecto",
            "list": [
                ("Ingeniería & Proyecto Ejecutivo",
                 "Definimos las bases técnicas del centro de datos a partir de sus necesidades operativas. Desarrollamos el proyecto ejecutivo integral, memorias de cálculo, planos y diagramas unifilares, con criterios de capacidad, redundancia y alta disponibilidad. Coordinamos las especialidades desde el diseño para facilitar su ejecución en obra."),
                ("Obra Civil & Estructura",
                 "Ejecutamos cimentación, estructura, albañilería, acabados y cancelería, así como instalaciones hidráulicas y sanitarias. Acondicionamos cuartos eléctricos y salas de tecnologías de la información, integrando los requerimientos de distribución, soporte y protección de la infraestructura crítica."),
                ("Infraestructura eléctrica crítica",
                 "Integramos sistemas de respaldo UPS, plantas de emergencia, plantas de corriente directa, inversores y bancos de baterías. Instalamos tableros, alimentadores, canalizaciones, sistemas de puesta a tierra y pararrayos, conforme a las necesidades de carga y continuidad operativa del proyecto."),
                ("Instalación MEP y especiales",
                 "Coordinamos los sistemas de climatización y enfriamiento, protección contra incendio y las instalaciones complementarias del centro de datos. Integramos detección temprana de humo, control de acceso, videovigilancia, cableado estructurado, fibra óptica, voz y datos, de acuerdo con el proyecto ejecutivo."),
                ("Sistemas de soporte y seguridad",
                 "Realizamos pruebas e integración de sistemas para verificar su funcionamiento conforme a los criterios del proyecto. Coordinamos la verificación de instalaciones eléctricas mediante una UVIE cuando corresponde y consolidamos la documentación para la entrega llave en mano. Complementamos el servicio con mantenimiento preventivo y correctivo para respaldar la operación."),
            ],
            "benefits_title": "Control del proyecto y respaldo para tu operación",
            "benefits_intro": "Un centro de datos requiere que la obra civil, la energía, el enfriamiento y la seguridad funcionen como un conjunto. En Arcondec coordinamos estas disciplinas desde la planeación hasta las pruebas finales, con responsabilidades claras y seguimiento técnico en cada etapa.",
            "benefits": [
                ("Un solo responsable de principio a fin", "Centralizamos la coordinación de ingeniería, construcción e instalaciones para facilitar la comunicación, el seguimiento de avances y la toma de decisiones durante el proyecto."),
                ("Ejecución coordinada entre especialidades", "Alineamos planos, requerimientos técnicos y secuencias de trabajo para identificar interferencias, reducir retrabajos y mantener el control de la ejecución."),
                ("Entrega funcional y documentada", "Verificamos la integración de los sistemas mediante pruebas y comisionamiento. Reunimos la documentación técnica del alcance ejecutado para facilitar la operación, el mantenimiento y futuras intervenciones."),
            ],
            "cta_title": "Inicia tu proyecto de Data Center con una solución profesional",
            "cta_text": "Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o construir tu centro de datos conforme a las mejores prácticas del sector.",
        },
        "en": {
            "nav": "Data Center Construction",
            "title": "Turnkey Data Center Construction",
            "meta": "Turnkey data center construction: UPS, emergency power plants, fire protection, precision cooling and BMS/DCIM monitoring for 24/7 operation.",
            "keywords": "data center construction, turnkey, UPS, emergency power plant, BMS, DCIM, critical infrastructure, Grupo Arcondec",
            "h1": "Turnkey data center construction",
            "lead": "Critical infrastructure designed for maximum availability, efficiency, and operational control",
            "tagline": "Specialized engineering for mission-critical environments",
            "intro_h2": "We implement comprehensive solutions for data center construction",
            "intro": "Covering everything from technical design to functional and fully documented delivery. Every component is developed in compliance with the most rigorous national and international standards for operation, safety, and continuity. We serve projects for companies requiring 24/7 availability, low latency, energy redundancy, and real-time monitoring. Our experience includes financial centers, digital platforms, cloud services, telecommunications, healthcare, industry, and government.",
            "list_title": "Specialized Services",
            "list": [
                "UPS Backup System (Uninterruptible Power Supply)",
                "Fire protection system (early detection, clean agent suppression)",
                "Emergency power plant with automatic transfer and synchronization",
                "Direct Current Plants (PDC) and DC distribution panels",
                "Inverters, rectifiers, and battery banks",
                "Grounding systems and lightning protection",
                "Pressure and comfort cooling (IN-ROW, CRAC/CRAH)",
                "Smart monitoring (BMS / DCIM)",
                "Access control, monitoring and video surveillance (CCTV/IP)",
                "Structured cabling category 6A or higher",
            ],
            "benefits_title": "Tangible benefits for your operation",
            "benefits_intro": "Designing and implementing a Data Center goes beyond installing equipment; it means protecting your operations, ensuring 24/7 continuity, and guaranteeing that every system functions optimally, safely, and in full compliance with regulations. We understand the complexity of modern business operations. That’s why our services are designed to deliver real value from day one—especially in sectors where availability and performance are essential.",
            "benefits": [
                ("Technical support from start to finish", "We guide you from design to implementation with direct support from our critical infrastructure engineering specialists."),
                ("Fast execution, no excuses", "We coordinate teams, regulations, and deliverables so your data center progresses without friction or delays."),
                ("Physical and logical security by design", "We incorporate access control, video surveillance, fire protection, and space segregation solutions starting from the basic engineering phase."),
            ],
            "cta_title": "Start your Data Center project with a professional solution",
            "cta_text": "Get technical advice from our specialists and discover how to design, optimize, or build your data center according to industry best practices.",
        },
    },
    {
        "key": "civdc",
        # La 10 va primero: es la que se usa de banner y de imagen principal.
        # Número nuevo y no sustitución, por la caché `immutable` de un año que
        # declara vercel.json para /assets/images (ver la nota en "cosdc").
        # Se retiró la 9 —terraza con sillas—: no es obra civil, es mobiliario.
        "photos": [10, 7, 8, 1, 2, 3, 4, 5, 6],
        "group": "llave",
        "icon": "fal fa-drafting-compass",
        "slug": {"es": "ingenieria-civil-data-center", "en": "civil-engineering-data-center"},
        "es": {
            "nav": "Obra Civil",
            "title": "Ingeniería civil para centros de datos",
            "meta": "Obra civil para data centers: cimentación, piso falso en área blanca, confinamiento de pasillos y acabados conforme a TIA-942, NEC y NFPA.",
            "keywords": "ingeniería civil, data center, piso falso, área blanca, TIA-942, obra civil especializada, Grupo Arcondec",
            "h1": "Ingeniería civil para centros de datos",
            "lead": "Infraestructura física diseñada para soportar entornos de misión crítica con precisión estructural, funcional y operativa",
            "tagline": "Construcción de data centers de alta disponibilidad",
            "intro_h2": "Implementamos soluciones integrales para la construcción de centros de datos",
            "intro": "Contamos con experiencia en proyectos de infraestructura crítica que requieren precisión estructural, cumplimiento normativo y coordinación técnica en cada detalle constructivo. Implementamos obras civiles especializadas para centros de datos en cumplimiento con las normativas más exigentes: TIA-942, NOM, Uptime Institute, NEC, NFPA y especificaciones de fabricantes de equipamiento tecnológico. Nuestros procesos constructivos están diseñados para cumplir con los estándares de disponibilidad TIER I, TIER II, TIER III y TIER IV.",
            "list_title": "Servicios especializados",
            "list": [
                "Cimentación y obra estructural especializada",
                "Albañilería técnica y acabados industriales",
                "Cancelería, puertas con control de acceso, mamparas técnicas",
                "Confinamiento de espacios de línea y fabricación a medida",
                "Desarrollo de ingenierías",
                "Cálculos y memorias estructurales",
                "Instalaciones hidráulicas y sanitarias con requerimientos especiales",
                "Piso falso en Área Blanca",
                "Aislamiento térmico y acústico",
            ],
            "benefits_title": "Beneficios de trabajar con Grupo Arcondec",
            "benefits_intro": "Nuestra experiencia nos permite ejecutar obras con precisión, pensando no solo en la solidez del edificio, sino en la continuidad operativa del entorno tecnológico que va a soportar. Desarrollamos ingeniería civil especializada, con eficiencia energética y cumplimiento con estándares nacionales e internacionales. Cada solución que entregamos está diseñada para integrarse con los sistemas eléctricos, mecánicos y de TI de forma segura, funcional y validable ante cualquier auditoría.",
            "benefits": [
                ("Obra civil alineada a normativas", "Construimos, diseñamos con base en los requerimientos de TIA-942, NEC y NFPA, asegurando compatibilidad con infraestructura TI, control ambiental y seguridad física."),
                ("Ejecución técnica sin interrupciones ni improvisaciones", "Desde la cimentación hasta el piso falso y los aislamientos, cada elemento está coordinado con ingeniería, supervisión y pruebas, evitando retrabajos y entregas parciales."),
                ("Soluciones personalizadas para entornos de alta exigencia", "Desarrollamos espacios a medida: salas blancas, pasillos confinados, mamparas técnicas, cancelerías especiales y sanitarios adaptados, todo según las necesidades reales del cliente."),
            ],
            "cta_title": "Inicia tu proyecto de Data Center con una solución profesional",
            "cta_text": "Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o construir tu centro de datos conforme a las mejores prácticas del sector.",
        },
        "en": {
            "nav": "Civil Works",
            "title": "Civil Engineering for Data Centers",
            "meta": "Civil works for data centers: foundations, raised floors in white areas, aisle containment and industrial finishes per TIA-942, NEC and NFPA.",
            "keywords": "civil engineering, data center, raised floor, white area, TIA-942, specialized civil works, Grupo Arcondec",
            "h1": "Civil engineering for data centers",
            "lead": "Physical infrastructure designed to support mission-critical environments with structural, functional, and operational precision",
            "tagline": "High-availability data center construction",
            "intro_h2": "We implement comprehensive solutions for data center construction",
            "intro": "We have experience in critical infrastructure projects that demand structural precision, regulatory compliance, and technical coordination in every construction detail. We execute specialized civil works for data centers in compliance with the most demanding standards: TIA-942, NOM, Uptime Institute, NEC, NFPA, and specifications from technology equipment manufacturers. Our construction processes are designed to meet TIER I, TIER II, TIER III, and TIER IV availability standards.",
            "list_title": "Specialized Services",
            "list": [
                "Specialized foundations and structural works",
                "Technical masonry and industrial-grade finishes",
                "Glazing systems, access-controlled doors, and technical partitions",
                "Line space containment and custom-built structures",
                "Engineering development",
                "Structural calculations and technical reports",
                "Hydraulic and sanitary installations with special requirements",
                "Raised floor in White Area",
                "Thermal and acoustic insulation",
            ],
            "benefits_title": "Benefits of working with Grupo Arcondec",
            "benefits_intro": "Our experience allows us to execute construction projects with precision, focusing not only on the structural integrity of the building but also on the operational continuity of the technological environment it will support. We develop specialized civil engineering with energy efficiency and compliance with national and international standards. Every solution we deliver is designed to integrate safely, functionally, and audit-ready with electrical, mechanical, and IT systems.",
            "benefits": [
                ("Civil works aligned with standards", "We build and design based on TIA-942, NEC, and NFPA requirements, ensuring compatibility with IT infrastructure, environmental control, and physical security."),
                ("Technical execution without interruptions or improvisation", "From foundations to raised flooring and insulation, every element is coordinated with engineering, supervision, and testing to avoid rework and partial deliveries."),
                ("Customized solutions for high-demand environments", "We develop tailor-made spaces: white rooms, confined aisles, technical partitions, special glasswork, and customized restrooms—all based on the client's real needs."),
            ],
            "cta_title": "Start your Data Center project with a professional solution",
            "cta_text": "Receive technical advice from our specialists and discover how to design, optimize, or build your data center according to industry best practices.",
        },
    },
    {
        "key": "proele",
        "photos": [7, 8, 9, 1, 2, 3, 4, 5, 6],
        "group": "ie",
        "icon": "fal fa-bolt",
        "slug": {"es": "proyectos-electricos-integrales", "en": "electrical-projects"},
        "es": {
            "nav": "Proyectos Eléctricos",
            "title": "Proyectos eléctricos integrales",
            "meta": "Desarrollamos proyectos eléctricos integrales: diseño de redes de tierras, estudios eléctricos y servicios AC/DC, con más de 30 años de experiencia.",
            "keywords": "proyectos eléctricos, redes de tierras, estudios eléctricos, servicios AC, servicios DC, ingeniería eléctrica, Grupo Arcondec, infraestructura crítica",
            "h1": "Proyectos eléctricos integrales",
            "lead": "Soluciones eléctricas de alto desempeño, listas para operar desde el primer día",
            "tagline": "Ingeniería a la medida de tu operación",
            "intro_h2": "Soluciones llave en mano",
            "intro": "Están diseñados para brindarte total certeza técnica, diagnósticos precisos y documentación completa para el desarrollo, validación o mantenimiento de tus instalaciones eléctricas. Contamos con experiencia en proyectos desde 225 kVA hasta más de 2.5 MVA, atendiendo necesidades en plantas industriales, centros logísticos, complejos comerciales y desarrollos de alta demanda energética.",
            "list_title": "Servicios especializados",
            "list": [
                "Transformadores y subestaciones",
                "Tableros auto soportados y de distribución",
                "Diseño y desarrollo de ingeniería, instalación y puesta en marcha",
                "Todo conforme a normas NOM, CFE y NFPA",
                "UVIE (Unidad de Verificación de Instalaciones Eléctricas)",
                "Trámites y gestorías ante CFE",
            ],
            "benefits_title": "Impulsa tu operación con beneficios reales",
            "benefits_intro": "Al contratar un sistema eléctrico especializado, obtienes mucho más que infraestructura: accedes a seguridad operativa, eficiencia energética y respaldo técnico desde el primer día.",
            "benefits": [
                ("Acompañamiento técnico de principio a fin", "Te guiamos antes, durante y después de la implementación con soporte directo de nuestros ingenieros."),
                ("Agilidad en la ejecución, sin excusas", "Resolvemos rápido, ejecutamos con precisión y entregamos a tiempo. Tu proyecto no se detiene."),
                ("Menos riesgos, más control", "Evita fallas, paros inesperados y problemas normativos. Diseñamos pensando en la seguridad total de tu operación."),
            ],
            "cta_title": "Inicia tu proyecto eléctrico industrial con una solución profesional",
            "cta_text": "Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o ejecutar tu sistema eléctrico de forma segura, eficiente y conforme a norma.",
        },
        "en": {
            "nav": "Electrical Projects",
            "title": "Comprehensive Electrical Projects",
            "meta": "We develop comprehensive electrical projects: grounding network design, electrical studies and AC/DC services, backed by over 30 years of experience.",
            "keywords": "electrical projects, grounding networks, electrical studies, AC services, DC services, electrical engineering, Grupo Arcondec, critical infrastructure",
            "h1": "Comprehensive electrical projects",
            "lead": "High-performance electrical solutions, ready to operate from day one",
            "tagline": "Engineering tailored to your operations",
            "intro_h2": "Turnkey solutions",
            "intro": "Designed to provide you with complete technical assurance, accurate diagnostics, and full documentation for the development, validation, or maintenance of your electrical installations. We have experience in projects ranging from 225 kVA to over 2.5 MVA, meeting the needs of industrial plants, logistics centers, commercial complexes, and developments with high energy demand.",
            "list_title": "Specialized Services",
            "list": [
                "Transformers and Substations",
                "Free-standing and Distribution Panels",
                "Engineering Design and Development, Installation and Commissioning",
                "All in compliance with NOM, CFE, and NFPA standards",
                "UVIE (Electrical Installations Verification Unit)",
                "Procedures and Management before CFE",
            ],
            "benefits_title": "Boost your operations with real benefits",
            "benefits_intro": "By hiring a specialized electrical system, you gain much more than just infrastructure: you access operational safety, energy efficiency, and technical support from day one.",
            "benefits": [
                ("Technical support and guidance from start to finish", "We guide you before, during, and after implementation with direct support from our engineers."),
                ("Agility in execution, no excuses", "We solve quickly, execute with precision, and deliver on time. Your project doesn’t stop."),
                ("Less risk, more control", "Avoid failures, unexpected shutdowns, and compliance issues. We design with your operation’s total safety in mind."),
            ],
            "cta_title": "Start your industrial electrical project with a professional solution",
            "cta_text": "Receive technical advice from our specialists and discover how to design, optimize, or execute your electrical system safely, efficiently, and in full compliance with standards.",
        },
    },
    {
        "key": "corac",
        "photos": [7, 1, 2, 3, 4, 5, 6],
        "group": "ie",
        "icon": "fal fa-battery-bolt",
        "slug": {"es": "soluciones-corriente-directa-dc", "en": "direct-current-solutions"},
        "es": {
            "nav": "Corriente Directa",
            "title": "Soluciones en corriente directa (DC)",
            "meta": "Sistemas de corriente directa (DC): diseño, instalación, bancos de baterías, tableros DC y mantenimiento para infraestructura crítica y data centers.",
            "keywords": "corriente directa, sistemas DC, baterías, tableros DC, UPS, mantenimiento eléctrico, infraestructura crítica, Grupo Arcondec",
            "h1": "Soluciones en corriente directa (DC)",
            "lead": "Energía sin interrupciones para entornos donde no se puede fallar",
            "tagline": "Corriente directa ideal para tu proyecto",
            "intro_h2": "Garantizamos continuidad operativa",
            "intro": "Diseñamos, suministramos e implementamos sistemas de corriente directa (DC) que garantizan energía continua, segura y conforme a norma para aplicaciones críticas. Nuestra experiencia abarca desde centros de datos hasta instalaciones industriales que requieren máxima disponibilidad operativa 24/7.",
            "list_title": "Servicios especializados",
            "list": [
                "Distribuidores de Corriente Directa (BDCBB)",
                "Bancos de baterías de litio",
                "Plantas de corriente directa (PDC)",
                "Inversores y rectificadores",
                "Sistemas UPS",
            ],
            "benefits_title": "Impulsa tu operación con beneficios reales",
            "benefits_intro": "Elegir un sistema eléctrico especializado significa seguridad operativa, eficiencia energética y respaldo técnico desde el primer día.",
            "benefits": [
                ("Acompañamiento técnico de principio a fin", "Te guiamos antes, durante y después de la implementación con soporte directo de nuestros ingenieros."),
                ("Agilidad en la ejecución, sin excusas", "Resolvemos rápido, ejecutamos con precisión y entregamos a tiempo. Tu proyecto no se detiene."),
                ("Menos riesgos, más control", "Evita fallas, paros inesperados y problemas normativos. Diseñamos pensando en la seguridad total de tu operación."),
            ],
            "cta_title": "Inicia tu proyecto eléctrico industrial con una solución profesional",
            "cta_text": "Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o ejecutar tu sistema eléctrico de forma segura, eficiente y conforme a norma.",
        },
        "en": {
            "nav": "Direct Current",
            "title": "Direct Current (DC) Solutions",
            "meta": "Direct current (DC) systems: design, installation, battery banks, DC panels and maintenance for critical infrastructure and data centers.",
            "keywords": "direct current, DC systems, batteries, DC panels, UPS, electrical maintenance, critical infrastructure, Grupo Arcondec",
            "h1": "Direct current (DC) solutions",
            "lead": "Uninterrupted power for environments where failure is not an option",
            "tagline": "Direct current tailored to your project",
            "intro_h2": "We ensure operational continuity",
            "intro": "We design, supply, and implement direct current (DC) systems that provide continuous, safe, and code-compliant power for critical applications. Our experience ranges from data centers to industrial facilities that demand maximum 24/7 operational availability.",
            "list_title": "Specialized Services",
            "list": [
                "Direct Current Distribution Bays (BDCBB)",
                "Lithium Battery Banks",
                "Direct Current Plants (PDC)",
                "Inverters and Rectifiers",
                "UPS Systems (Uninterruptible Power Supply Systems)",
            ],
            "benefits_title": "Boost your operations with real benefits",
            "benefits_intro": "Choosing a specialized electrical system means operational safety, energy efficiency, and technical support from day one.",
            "benefits": [
                ("Technical support from start to finish", "We guide you before, during, and after implementation with direct support from our engineers."),
                ("Agility in execution, no excuses", "We respond quickly, execute with precision, and deliver on time. Your project doesn't stop."),
                ("Fewer risks, more control", "Avoid failures, unexpected shutdowns, and regulatory issues. We design with the total safety of your operation in mind."),
            ],
            "cta_title": "Start your industrial electrical project with a professional solution",
            "cta_text": "Receive technical advice from our specialists and discover how to design, optimize, or execute your electrical system safely, efficiently, and in compliance with regulations.",
        },
    },
    {
        # ─────────────────────────────────────────────────────────────────
        # TEXTO PROVISIONAL — pendiente del definitivo del cliente.
        # Describe el servicio en términos técnicos correctos pero genéricos:
        # NO trae cifras, plazos, marcas ni certificaciones, justo para no
        # afirmar nada que no esté confirmado. Sustituir en cuanto llegue.
        # FOTOS PRESTADAS de los servicios dados de baja; sirven porque son
        # obra real de Arcondec, pero conviene una selección propia.
        # ─────────────────────────────────────────────────────────────────
        "key": "coralt",
        "photos": [1, 2, 3, 4, 5, 6, 7, 8],
        "group": "ie",
        "icon": "fal fa-plug",
        "slug": {"es": "soluciones-corriente-alterna-ca", "en": "alternating-current-solutions"},
        "es": {
            "nav": "Corriente Alterna",
            "title": "Soluciones en corriente alterna (CA)",
            "meta": "Sistemas de corriente alterna: tableros de distribución, transferencia automática, alimentadores y respaldo con planta de emergencia para infraestructura crítica.",
            "keywords": "corriente alterna, tableros de distribución, transferencia automática, alimentadores, planta de emergencia, media tensión, infraestructura crítica",
            "h1": "Soluciones en corriente alterna (CA)",
            "lead": "Distribución eléctrica confiable, desde la acometida hasta la carga",
            "tagline": "Corriente alterna a la medida de tu operación",
            "intro_h2": "Del punto de suministro a cada equipo",
            "intro": "Diseñamos, suministramos e integramos sistemas de distribución en corriente alterna para instalaciones donde la continuidad no es negociable. El alcance abarca la acometida y la transformación, los tableros generales de servicio normal y de emergencia, los sistemas de transferencia, los alimentadores de potencia y su canalización, con pruebas y puesta en marcha de principio a fin.",
            "list_title": "Servicios especializados",
            "list": [
                "Tableros generales de servicio normal y de emergencia",
                "Tableros de transferencia automática y de enlace",
                "Alimentadores de potencia, canalización y charola",
                "Integración con planta de emergencia",
                "Transformadores de distribución y reductores",
                "Pruebas eléctricas y puesta en marcha",
            ],
            "benefits_title": "Impulsa tu operación con beneficios reales",
            "benefits_intro": "Elegir un sistema eléctrico especializado significa seguridad operativa, eficiencia energética y respaldo técnico en cada etapa del proyecto.",
            "benefits": [
                ("Acompañamiento técnico de principio a fin", "Te guiamos antes, durante y después de la implementación con soporte directo de nuestros ingenieros."),
                ("Agilidad en la ejecución, sin excusas", "Resolvemos rápido, ejecutamos con precisión y entregamos a tiempo. Tu proyecto no se detiene."),
                ("Menos riesgos, más control", "Evita fallas, paros inesperados y problemas normativos. Diseñamos pensando en la seguridad total de tu operación."),
            ],
            "cta_title": "Inicia tu proyecto eléctrico industrial con una solución profesional",
            "cta_text": "Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o ejecutar tu sistema eléctrico con seguridad, eficiencia y cumplimiento normativo.",
        },
        "en": {
            "nav": "Alternating Current",
            "title": "Alternating Current (AC) Solutions",
            "meta": "Alternating current systems: distribution switchboards, automatic transfer, power feeders and emergency generator backup for critical infrastructure.",
            "keywords": "alternating current, distribution switchboards, automatic transfer, feeders, emergency generator, medium voltage, critical infrastructure",
            "h1": "Alternating current (AC) solutions",
            "lead": "Reliable electrical distribution, from the service entrance to the load",
            "tagline": "Alternating current tailored to your operation",
            "intro_h2": "From the supply point to every piece of equipment",
            "intro": "We design, supply, and integrate alternating current distribution systems for facilities where continuity is not negotiable. The scope covers the service entrance and transformation, normal and emergency main switchboards, transfer systems, power feeders and their raceways, with testing and commissioning from start to finish.",
            "list_title": "Specialized Services",
            "list": [
                "Normal and emergency main switchboards",
                "Automatic transfer and tie switchboards",
                "Power feeders, raceways and cable tray",
                "Integration with emergency generator sets",
                "Distribution and step-down transformers",
                "Electrical testing and commissioning",
            ],
            "benefits_title": "Boost your operations with real benefits",
            "benefits_intro": "Choosing a specialized electrical system means operational safety, energy efficiency, and technical support at every stage of the project.",
            "benefits": [
                ("Technical support from start to finish", "We guide you before, during, and after implementation with direct support from our engineers."),
                ("Agility in execution, no excuses", "We respond quickly, execute with precision, and deliver on time. Your project doesn't stop."),
                ("Fewer risks, more control", "Avoid failures, unexpected shutdowns, and regulatory issues. We design with the total safety of your operation in mind."),
            ],
            "cta_title": "Start your industrial electrical project with a professional solution",
            "cta_text": "Receive technical advice from our specialists and discover how to design, optimize, or execute your electrical system safely, efficiently, and in compliance with regulations.",
        },
    },
    {
        # ─────────────────────────────────────────────────────────────────
        # TEXTO PROVISIONAL — mismas condiciones que Corriente Alterna.
        # FOTOS: las prestadas muestran medición y trabajo en tablero, no
        # sistemas de tierra propiamente. Es lo más flojo de las dos páginas;
        # conviene pedir fotos de malla, electrodo y soldadura exotérmica.
        # ─────────────────────────────────────────────────────────────────
        "key": "tierra",
        "photos": [1, 2, 3, 4, 5, 6],
        "group": "ie",
        "icon": "fal fa-shield-check",
        "slug": {"es": "diseno-sistemas-de-tierras", "en": "grounding-system-design"},
        "es": {
            "nav": "Diseño de Tierras",
            "title": "Diseño de sistemas de tierras",
            "meta": "Diseño y construcción de sistemas de tierra física: malla, electrodos, soldadura exotérmica, barras master, supresión de transitorios y protección contra descargas.",
            "keywords": "sistema de tierras, tierra física, malla de tierra, soldadura exotérmica, electrodo, pararrayos, supresores de transitorios, resistividad",
            "h1": "Diseño de sistemas de tierras",
            "lead": "La referencia sobre la que se sostiene toda la instalación",
            "tagline": "Sistemas de tierra calculados, no improvisados",
            "intro_h2": "Protección de las personas y del equipo",
            "intro": "El sistema de tierras es lo que fija el potencial de referencia de una instalación y el camino por el que se descarga una falla. Lo diseñamos a partir de la medición del terreno y de las cargas a proteger, y lo construimos con malla, electrodos y conexiones verificables, integrando equipos, racks y áreas críticas a una misma referencia.",
            "list_title": "Servicios especializados",
            "list": [
                "Medición de resistividad del terreno y diagnóstico",
                "Diseño y cálculo de la malla de tierra",
                "Electrodos, registros y soldadura exotérmica",
                "Barras master e integración de equipos y racks",
                "Supresores de transitorios y protección contra descargas",
                "Pruebas de continuidad y resistencia de puesta a tierra",
            ],
            "benefits_title": "Impulsa tu operación con beneficios reales",
            "benefits_intro": "Un sistema de tierras bien calculado protege a las personas, alarga la vida del equipo y evita fallas que no dejan rastro evidente.",
            "benefits": [
                ("Acompañamiento técnico de principio a fin", "Te guiamos antes, durante y después de la implementación con soporte directo de nuestros ingenieros."),
                ("Agilidad en la ejecución, sin excusas", "Resolvemos rápido, ejecutamos con precisión y entregamos a tiempo. Tu proyecto no se detiene."),
                ("Menos riesgos, más control", "Evita fallas, paros inesperados y problemas normativos. Diseñamos pensando en la seguridad total de tu operación."),
            ],
            "cta_title": "Inicia tu proyecto eléctrico industrial con una solución profesional",
            "cta_text": "Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o ejecutar tu sistema eléctrico con seguridad, eficiencia y cumplimiento normativo.",
        },
        "en": {
            "nav": "Grounding Design",
            "title": "Grounding System Design",
            "meta": "Design and construction of grounding systems: ground grid, electrodes, exothermic welding, master bars, surge suppression and lightning protection.",
            "keywords": "grounding system, earthing, ground grid, exothermic welding, electrode, lightning protection, surge suppressors, soil resistivity",
            "h1": "Grounding system design",
            "lead": "The reference the entire installation rests on",
            "tagline": "Grounding systems that are calculated, not improvised",
            "intro_h2": "Protecting people and equipment",
            "intro": "The grounding system sets the reference potential of an installation and provides the path a fault discharges through. We design it from soil measurements and the loads to be protected, and build it with a grid, electrodes and verifiable connections, bringing equipment, racks and critical areas to a single reference.",
            "list_title": "Specialized Services",
            "list": [
                "Soil resistivity measurement and assessment",
                "Ground grid design and calculation",
                "Electrodes, pits and exothermic welding",
                "Master bars and bonding of equipment and racks",
                "Surge suppressors and lightning protection",
                "Continuity and ground resistance testing",
            ],
            "benefits_title": "Boost your operations with real benefits",
            "benefits_intro": "A properly calculated grounding system protects people, extends equipment life, and prevents failures that leave no obvious trace.",
            "benefits": [
                ("Technical support from start to finish", "We guide you before, during, and after implementation with direct support from our engineers."),
                ("Agility in execution, no excuses", "We respond quickly, execute with precision, and deliver on time. Your project doesn't stop."),
                ("Fewer risks, more control", "Avoid failures, unexpected shutdowns, and regulatory issues. We design with the total safety of your operation in mind."),
            ],
            "cta_title": "Start your industrial electrical project with a professional solution",
            "cta_text": "Receive technical advice from our specialists and discover how to design, optimize, or execute your electrical system safely, efficiently, and in compliance with regulations.",
        },
    },
]

# --------------------------------------------------------------------------
# Listas de servicios que aparecen en el pie y en las paginas interiores
# --------------------------------------------------------------------------
LIST_IE = {
    "es": {
        "title": "Ingeniería Eléctrica",
        "items": [
            "Proyectos eléctricos",
            "Corriente alterna (AC) y directa (DC)",
            "Estudios eléctricos",
            "Servicios eléctricos",
            "Diseño de red de tierras",
            "Sistemas fotovoltaicos",
            "Mantenimiento eléctrico preventivo y correctivo",
        ],
    },
    "en": {
        "title": "Electrical Engineering",
        "items": [
            "Electrical Projects",
            "Alternating Current (AC) and Direct Current (DC)",
            "Electrical Studies",
            "Electrical Services",
            "Grounding Network Design",
            "Photovoltaic Systems",
            "Preventive and Corrective Electrical Maintenance",
        ],
    },
}

LIST_DC = {
    "es": {
        "title": "Data Centers",
        "items": [
            "Sistema de respaldo UPS (Power System)",
            "Instalación de tablero de distribución en corriente directa tipo BDCBB",
            "Generadores de emergencia",
            "Plantas de Corriente Directa",
            "Inversores y banco de baterías",
            "Sistema de tierras física y pararrayos",
        ],
    },
    "en": {
        "title": "Data Centers",
        "items": [
            "UPS Backup System (Power System)",
            "Direct Current Distribution Board Installation (BDCBB type)",
            "Emergency Generators",
            "Direct Current Plants",
            "Inverters and Battery Banks",
            "Grounding and Lightning Protection System",
        ],
    },
}

COMMIT_TEXT = {
    "es": "Fortalecemos cada día nuestro compromiso contigo, brindando un servicio excepcional como tu aliado estratégico en ingeniería eléctrica y centros de datos.",
    "en": "We strengthen our commitment to you every day by delivering exceptional service as your strategic partner in electrical engineering and data centers.",
}
