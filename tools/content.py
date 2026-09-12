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
        "scope_photos": [12, 13, 14, 15, 16],
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
            "list_title": "De la ingeniería a la operación.",
            "scope_eyebrow": "Solución integral",
            "scope_intro": "Cinco especialidades. Un solo responsable de tu data center.",
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
            "list_title": "From engineering to operation.",
            "scope_eyebrow": "Integrated delivery",
            "scope_intro": "Five disciplines. One accountable partner for your data center.",
            "list": [
                ("Engineering and detailed design",
                 "We define the data center's technical foundations around its operational needs. We develop coordinated detailed designs, calculations, drawings and single-line diagrams with capacity, redundancy and high availability in mind. We coordinate disciplines from the design stage to support construction."),
                ("Civil works and structures",
                 "We build foundations, structures, masonry, finishes and glazing, together with water supply and drainage installations. We prepare electrical rooms and IT spaces, incorporating the layout, support and protection requirements of critical infrastructure."),
                ("Critical electrical infrastructure",
                 "We integrate UPS backup, emergency generators, direct current power systems, inverters and battery banks. We install switchboards, feeders, cable containment, grounding and lightning protection according to the project's load and operational continuity requirements."),
                ("MEP and special installations",
                 "We coordinate air conditioning and cooling, fire protection and complementary data center installations. We integrate early smoke detection, access control, video surveillance, structured cabling, fiber optics, voice and data according to the detailed design."),
                ("Support and safety systems",
                 "We test and integrate systems to verify operation against project criteria. We coordinate electrical installation verification through a UVIE inspection body where applicable and compile documentation for turnkey handover. Preventive and corrective maintenance provide continued operational support."),
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
        "scope_photos": [11, 12, 13, 14, 15],
        "group": "llave",
        "icon": "fal fa-drafting-compass",
        "slug": {"es": "ingenieria-civil-data-center", "en": "civil-engineering-data-center"},
        "es": {
            "nav": "Obra Civil",
            "title": "Obra civil para data centers e infraestructura crítica",
            "meta": "Obra civil para centros de datos e infraestructura crítica: cimentación, estructura, albañilería, acabados, herrería, cancelería e instalaciones hidrosanitarias.",
            "keywords": "obra civil data center, cimentación, estructura, albañilería, acabados, herrería, cancelería, instalaciones hidrosanitarias, infraestructura crítica, Grupo Arcondec",
            "h1": "Obra civil para data centers e infraestructura crítica",
            "lead": "Diseñamos y construimos los espacios que dan soporte a tu operación, desde la cimentación hasta los acabados finales",
            "tagline": "Ingeniería civil integrada con la infraestructura eléctrica",
            "intro_h2": "Soluciones constructivas desde el diseño hasta la entrega",
            "intro": [
                "En Grupo Arcondec complementamos nuestra especialidad eléctrica con servicios integrales de obra civil para centros de datos y entornos de misión crítica. Desarrollamos espacios que responden a los requerimientos estructurales, técnicos y funcionales de cada proyecto.",
                "Nuestro alcance comprende estudios y memorias de cálculo, diseño y ejecución de cimentaciones y estructuras, albañilería, acabados, herrería, cancelería e instalaciones hidráulicas y sanitarias. Integramos la gestión de trámites y la visualización del proyecto mediante renders para apoyar su planeación.",
                "Coordinamos la obra civil con las instalaciones eléctricas y los sistemas especializados desde el diseño, considerando cargas de equipos, recorridos de instalaciones, accesos y necesidades de mantenimiento. Así, cada etapa constructiva contribuye a una infraestructura funcional y preparada para su uso.",
            ],
            "cta_btn": "Cuéntanos sobre tu proyecto",
            "list_title": "Solidez en cada etapa.",
            "scope_eyebrow": "Alcance constructivo",
            "scope_intro": "Cinco especialidades. Una visión integral de tu proyecto.",
            "list": [
                ("Planeación, estudios y diseño",
                 "Definimos los requerimientos constructivos y desarrollamos los estudios, memorias de cálculo y documentación técnica conforme al alcance del proyecto. Coordinamos los trámites correspondientes y elaboramos renders para visualizar la distribución, los espacios y los acabados antes de su ejecución."),
                ("Cimentación y estructura",
                 "Diseñamos y ejecutamos cimentaciones y estructuras considerando las condiciones del sitio, las cargas previstas y las necesidades de la edificación. Integramos los requerimientos de soporte para equipos e instalaciones, coordinando los elementos estructurales con las demás especialidades del proyecto."),
                ("Albañilería y acabados",
                 "Ejecutamos muros, divisiones y trabajos de albañilería para conformar salas técnicas, cuartos eléctricos y áreas complementarias. Desarrollamos acabados en pisos, muros y plafones de acuerdo con las especificaciones de uso, resistencia y mantenimiento de cada espacio."),
                ("Herrería y cancelería",
                 "Fabricamos e instalamos elementos de herrería y cancelería conforme al diseño arquitectónico y a las necesidades funcionales del inmueble. Coordinamos dimensiones, materiales y ubicación de puertas, cerramientos y elementos de protección, considerando accesos de personal, traslado de equipos y mantenimiento."),
                ("Instalaciones hidráulicas y sanitarias",
                 "Ejecutamos redes de abastecimiento de agua, desalojo sanitario y drenaje pluvial conforme a los requerimientos del proyecto. Coordinamos sus trayectorias con la estructura y las instalaciones eléctricas para facilitar su funcionamiento, inspección y mantenimiento, considerando la protección de las áreas técnicas."),
            ],
            "benefits_title": "Una base sólida para tu infraestructura",
            "benefits_intro": "La obra civil define cómo se alojan, protegen y mantienen los sistemas que sostienen la operación. En Arcondec vinculamos el diseño y la construcción con las necesidades de la infraestructura eléctrica y los equipos especializados, para que cada espacio cumpla una función dentro del proyecto.",
            "benefits": [
                ("Coordinación entre obra civil e instalaciones", "Integramos requerimientos estructurales, arquitectónicos y eléctricos desde la planeación. Esto permite anticipar interferencias, definir pasos y soportes, y reducir ajustes durante la construcción."),
                ("Espacios diseñados para su operación", "Consideramos la distribución de equipos, las circulaciones, los accesos y las necesidades de mantenimiento para desarrollar áreas funcionales y facilitar las actividades de operación e intervención."),
                ("Seguimiento técnico de principio a fin", "Coordinamos las etapas constructivas, desde los estudios iniciales hasta los acabados y la entrega. Damos seguimiento a las especificaciones y los trabajos ejecutados para mantener el control del alcance y la calidad del proyecto."),
            ],
            "cta_title": "Inicia tu proyecto de obra civil con una solución profesional",
            "cta_text": "Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar y construir la infraestructura física que tu operación necesita.",
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
            "list_title": "Strength at every stage.",
            "scope_eyebrow": "Construction scope",
            "scope_intro": "Five disciplines. One integrated vision for your project.",
            "list": [
                ("Planning, studies and design",
                 "We define construction requirements and develop studies, calculations and technical documentation to match the project scope. We coordinate the relevant permitting processes and prepare renderings to visualize layouts, spaces and finishes before construction."),
                ("Foundations and structures",
                 "We design and build foundations and structures based on site conditions, anticipated loads and building requirements. We incorporate support requirements for equipment and utilities, coordinating structural elements with the other project disciplines."),
                ("Masonry and finishes",
                 "We build walls, partitions and masonry for technical rooms, electrical rooms and supporting areas. We deliver floor, wall and ceiling finishes according to each space's requirements for use, durability and maintenance."),
                ("Metalwork and glazing",
                 "We fabricate and install metalwork and glazing to meet the architectural design and the building's functional needs. We coordinate dimensions, materials and the location of doors, enclosures and protective elements, considering personnel access, equipment movement and maintenance."),
                ("Water supply and drainage",
                 "We install water supply, sanitary drainage and stormwater networks according to project requirements. We coordinate routes with the structure and electrical installations to facilitate operation, inspection and maintenance while protecting technical areas."),
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
        "scope_photos": [10, 11, 12, 13, 14],
        "group": "ie",
        "icon": "fal fa-bolt",
        "slug": {"es": "soluciones-electricas", "en": "electrical-solutions"},
        'es': {'nav': 'Soluciones Eléctricas',
         'title': 'Soluciones eléctricas para data centers e industria',
         'meta': 'Soluciones eléctricas para data centers e industria: ingeniería, UPS, respaldo, distribución, '
                 'protecciones y puesta a tierra para tu infraestructura crítica.',
         'keywords': 'soluciones eléctricas, data centers, industria, baja y media tensión, UPS, respaldo eléctrico, '
                     'puesta a tierra, ingeniería eléctrica, Grupo Arcondec',
         'h1': 'Soluciones eléctricas para data centers e industria',
         'lead': 'Integramos ingeniería, respaldo y distribución eléctrica para sostener la continuidad, la seguridad y '
                 'el crecimiento de tu operación.',
         'tagline': 'Ingeniería eléctrica especializada para infraestructura crítica',
         'intro_h2': 'Diseñamos la infraestructura eléctrica que tu operación necesita',
         'intro': ['En Grupo Arcondec desarrollamos soluciones eléctricas en baja y media tensión para centros de datos, '
                   'industria y entornos de misión crítica. Integramos sistemas de potencia, distribución y respaldo de '
                   'acuerdo con las necesidades de carga, disponibilidad y seguridad de cada instalación.',
                   'Nuestro alcance comprende ingeniería, planos eléctricos, memorias de cálculo, estudios de carga, '
                   'coordinación de protecciones y dimensionamiento de equipos. Incorporamos sistemas UPS, plantas de '
                   'emergencia, soluciones de corriente directa e inversores, junto con sistemas de puesta a tierra y '
                   'criterios de calidad de energía.',
                   'Coordinamos cada componente con la infraestructura del proyecto y sus requerimientos de operación y '
                   'mantenimiento. Entregamos documentación técnica para orientar la construcción, facilitar la operación '
                   'y respaldar futuras ampliaciones.'],
         'cta_btn': 'Cuéntanos sobre tu proyecto',
         'list_title': 'Soluciones integrales de ingeniería eléctrica',
         'scope_eyebrow': 'Ingeniería eléctrica',
         'scope_intro': 'Cinco especialidades para respaldar tu operación.',
         'list': [('Ingeniería y diseño eléctrico',
                   'Desarrollamos proyectos eléctricos en baja y media tensión a partir de los requerimientos operativos '
                   'de cada instalación. Definimos la configuración de alimentación y distribución, elaboramos planos y '
                   'diagramas unifilares, y coordinamos las trayectorias eléctricas con la obra civil y las demás '
                   'especialidades.'),
                  ('Estudios y dimensionamiento de infraestructura',
                   'Elaboramos memorias de cálculo y estudios de carga para dimensionar equipos, alimentadores y sistemas '
                   'de distribución. Consideramos la demanda prevista, las condiciones de operación y las necesidades de '
                   'crecimiento, estableciendo las bases técnicas para seleccionar los componentes del proyecto.'),
                  ('Sistemas de respaldo y continuidad operativa',
                   'Integramos sistemas UPS, plantas de emergencia, plantas de corriente directa, inversores y bancos de '
                   'baterías conforme a las necesidades de las cargas críticas. Definimos criterios de capacidad, '
                   'autonomía y redundancia para respaldar el suministro eléctrico ante interrupciones de la fuente '
                   'principal.'),
                  ('Protecciones, puesta a tierra y calidad de energía',
                   'Desarrollamos estudios de coordinación y selectividad de protecciones para favorecer la desconexión '
                   'del circuito afectado ante una falla y limitar su impacto en el resto de la instalación. Diseñamos '
                   'sistemas de puesta a tierra y evaluamos requerimientos de calidad de energía para contribuir a la '
                   'seguridad de las personas y la protección de los equipos.'),
                  ('Integración y documentación técnica',
                   'Coordinamos la integración de los sistemas de potencia, respaldo y distribución con los '
                   'requerimientos de TI, centros de datos e instalaciones industriales. Consolidamos planos, diagramas, '
                   'especificaciones y memorias de cálculo para apoyar la construcción, la operación y el mantenimiento '
                   'de la infraestructura eléctrica.')],
         'benefits_title': 'Confiabilidad eléctrica para tu operación',
         'benefits_intro': 'La continuidad operativa depende de una infraestructura eléctrica dimensionada correctamente '
                           'y de la coordinación entre sus sistemas de alimentación, respaldo y protección. En Arcondec '
                           'integramos estas decisiones desde la ingeniería para responder a las exigencias de cada '
                           'instalación y facilitar su desarrollo a largo plazo.',
         'benefits': [('Respaldo alineado con tus cargas críticas',
                       'Definimos la capacidad, autonomía y configuración de los sistemas de respaldo conforme a las '
                       'prioridades de tu operación. Esto permite establecer una respuesta ante interrupciones del '
                       'suministro y reducir la exposición de los procesos esenciales.'),
                      ('Seguridad y protección coordinadas',
                       'Integramos criterios de protección eléctrica, puesta a tierra y calidad de energía desde el '
                       'diseño. Buscamos limitar los efectos de las fallas y favorecer un funcionamiento seguro de los '
                       'equipos y la instalación.'),
                      ('Capacidad para operar y crecer',
                       'Dimensionamos la infraestructura considerando la demanda actual y las ampliaciones previstas. La '
                       'documentación técnica facilita la planeación del mantenimiento, la evaluación de nuevas cargas y '
                       'la toma de decisiones sobre futuras intervenciones.')],
         'cta_title': 'Inicia tu proyecto eléctrico industrial con una solución profesional',
         'cta_text': 'Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o '
                     'ejecutar tu sistema eléctrico de forma segura, eficiente y conforme a norma.'},
        'en': {'nav': 'Electrical Solutions',
         'title': 'Electrical solutions for data centers and industry',
         'meta': 'Electrical solutions for data centers and industry: engineering, UPS, backup power, distribution, '
                 'protection and grounding for your critical infrastructure.',
         'keywords': 'electrical solutions, data centers, industry, low and medium voltage, UPS, backup power, grounding, '
                     'electrical engineering, Grupo Arcondec',
         'h1': 'Electrical solutions for data centers and industry',
         'lead': 'We integrate engineering, backup power and electrical distribution to support the continuity, safety '
                 'and growth of your operations.',
         'tagline': 'Specialized electrical engineering for critical infrastructure',
         'intro_h2': 'We design the electrical infrastructure your operations need',
         'intro': ['At Grupo Arcondec, we develop low- and medium-voltage electrical solutions for data centers, industry '
                   'and mission-critical environments. We integrate power, distribution and backup systems according to '
                   'each facility’s load, availability and safety requirements.',
                   'Our scope includes engineering, electrical drawings, calculation reports, load studies, protection '
                   'coordination and equipment sizing. We incorporate UPS systems, emergency generators, direct current '
                   'solutions and inverters, together with grounding systems and power quality criteria.',
                   'We coordinate each component with the project infrastructure and its operation and maintenance '
                   'requirements. We deliver technical documentation to guide construction, facilitate operation and '
                   'support future expansion.'],
         'cta_btn': 'Tell us about your project',
         'list_title': 'Integrated electrical engineering solutions',
         'scope_eyebrow': 'Electrical engineering',
         'scope_intro': 'Five disciplines to support your operations.',
         'list': [('Electrical engineering and design',
                   'We develop low- and medium-voltage electrical designs based on each facility’s operational '
                   'requirements. We define supply and distribution configurations, prepare drawings and single-line '
                   'diagrams, and coordinate electrical routes with civil works and other disciplines.'),
                  ('Infrastructure studies and sizing',
                   'We prepare calculation reports and load studies to size equipment, feeders and distribution systems. '
                   'We consider anticipated demand, operating conditions and growth requirements, establishing the '
                   'technical basis for selecting project components.'),
                  ('Backup systems and operational continuity',
                   'We integrate UPS systems, emergency generators, direct current power systems, inverters and battery '
                   'banks according to critical load requirements. We define capacity, autonomy and redundancy criteria '
                   'to support the electrical supply during interruptions to the primary source.'),
                  ('Protection, grounding and power quality',
                   'We develop protection coordination and selectivity studies to help disconnect the affected circuit '
                   'during a fault and limit its impact on the rest of the installation. We design grounding systems and '
                   'assess power quality requirements to contribute to personnel safety and equipment protection.'),
                  ('Integration and technical documentation',
                   'We coordinate the integration of power, backup and distribution systems with the requirements of IT, '
                   'data centers and industrial facilities. We compile drawings, diagrams, specifications and calculation '
                   'reports to support construction, operation and maintenance of the electrical infrastructure.')],
         'benefits_title': 'Electrical reliability for your operations',
         'benefits_intro': 'Operational continuity depends on correctly sized electrical infrastructure and coordination '
                           'between supply, backup and protection systems. At Arcondec, we integrate these decisions from '
                           'the engineering stage to meet each facility’s requirements and facilitate its long-term '
                           'development.',
         'benefits': [('Backup aligned with your critical loads',
                       'We define the capacity, autonomy and configuration of backup systems according to your '
                       'operational priorities. This establishes a response to supply interruptions and reduces the '
                       'exposure of essential processes.'),
                      ('Coordinated safety and protection',
                       'We incorporate electrical protection, grounding and power quality criteria from the design stage. '
                       'We aim to limit the effects of faults and support the safe operation of equipment and the '
                       'installation.'),
                      ('Capacity to operate and grow',
                       'We size infrastructure with current demand and planned expansions in mind. Technical '
                       'documentation facilitates maintenance planning, assessment of new loads and decisions about '
                       'future work.')],
         'cta_title': 'Start your industrial electrical project with a professional solution',
         'cta_text': 'Receive technical advice from our specialists and discover how to design, optimize, or execute your '
                     'electrical system safely, efficiently, and in full compliance with standards.'},
    },
    {
        "key": "corac",
        "photos": [7, 1, 2, 3, 4, 5, 6],
        "scope_photos": [8, 9, 10, 11, 12],
        "group": "ie",
        "icon": "fal fa-battery-bolt",
        "slug": {"es": "soluciones-corriente-directa-dc", "en": "direct-current-solutions"},
        'es': {'nav': 'Corriente Directa',
         'title': 'Soluciones de corriente directa (DC)',
         'meta': 'Soluciones de corriente directa: ingeniería, plantas DC, bancos de baterías, gabinetes de distribución, '
                 'pruebas y mantenimiento para infraestructura crítica.',
         'keywords': 'corriente directa, sistemas DC, plantas DC, bancos de baterías, distribución DC, respaldo '
                     'eléctrico, mantenimiento, Grupo Arcondec',
         'h1': 'Soluciones de corriente directa (DC)',
         'lead': 'Diseñamos e implementamos sistemas de corriente directa a la medida de tus necesidades de alimentación, '
                 'respaldo y continuidad operativa.',
         'tagline': 'Ingeniería eléctrica especializada en alimentación y respaldo DC',
         'intro_h2': 'Energía de respaldo para los sistemas que sostienen tu operación',
         'intro': ['En Grupo Arcondec desarrollamos soluciones de corriente directa para infraestructura crítica, desde '
                   'el dimensionamiento técnico hasta la instalación y puesta en marcha. Integramos plantas de corriente '
                   'directa, bancos de baterías y gabinetes de distribución conforme a los requerimientos de cada '
                   'proyecto.',
                   'Nuestro servicio comprende ingeniería, suministro, instalación y pruebas de equipos, considerando la '
                   'demanda eléctrica, la autonomía requerida y las condiciones de operación. Coordinamos los componentes '
                   'de alimentación, almacenamiento y distribución para que funcionen como un sistema integrado.',
                   'Complementamos cada solución con mantenimiento eléctrico preventivo y correctivo para identificar '
                   'deterioros, atender fallas y conservar las condiciones de funcionamiento de la infraestructura DC.'],
         'cta_btn': 'Cuéntanos sobre tu proyecto',
         'scope_eyebrow': 'Alimentación y respaldo DC',
         'scope_intro': 'Cinco especialidades para integrar tu infraestructura DC.',
         'list_title': 'Soluciones integrales de corriente directa',
         'list': [('Ingeniería y proyecto eléctrico DC',
                   'Desarrollamos el proyecto eléctrico a partir de las necesidades de alimentación y respaldo de los '
                   'equipos. Definimos capacidades, configuración y distribución del sistema, integrando planos, '
                   'diagramas y criterios técnicos para orientar la selección de componentes y su instalación.'),
                  ('Plantas de corriente directa',
                   'Suministramos e instalamos plantas de corriente directa (PDC) conforme a la capacidad y configuración '
                   'del proyecto. Integramos los equipos de rectificación con los bancos de baterías y la distribución '
                   'DC, considerando las necesidades de alimentación de las cargas y recarga del sistema de respaldo.'),
                  ('Dimensionamiento de bancos de baterías',
                   'Dimensionamos bancos de baterías en función de la carga, el tiempo de respaldo requerido y las '
                   'condiciones de operación. Definimos su capacidad y configuración, considerando la compatibilidad con '
                   'la planta de corriente directa y las necesidades de instalación, acceso y mantenimiento.'),
                  ('Gabinetes de distribución DC',
                   'Suministramos e instalamos gabinetes de distribución de corriente directa para organizar la '
                   'alimentación de los circuitos del proyecto. Integramos conexiones y protecciones conforme a las '
                   'cargas previstas, facilitando la identificación de circuitos y el acceso para inspecciones e '
                   'intervenciones.'),
                  ('Pruebas, puesta en marcha y mantenimiento',
                   'Realizamos pruebas a los equipos y verificamos su integración antes de la puesta en operación, '
                   'conforme al alcance del proyecto. Brindamos mantenimiento preventivo y correctivo a la instalación '
                   'eléctrica y los sistemas DC para evaluar su condición, atender desviaciones y respaldar su '
                   'funcionamiento.')],
         'benefits_title': 'Respaldo energético alineado con tu operación',
         'benefits_intro': 'La disponibilidad de un sistema de corriente directa depende de la capacidad de sus equipos, '
                           'la autonomía de sus baterías y el estado de sus componentes. En Arcondec integramos '
                           'ingeniería, suministro y mantenimiento para responder a estas necesidades durante la '
                           'implementación y la operación.',
         'benefits': [('Autonomía conforme a tus necesidades',
                       'Dimensionamos el banco de baterías de acuerdo con las cargas y el tiempo de respaldo requerido. '
                       'Esto permite planear la reserva de energía en función de las prioridades operativas del '
                       'proyecto.'),
                      ('Alimentación y distribución integradas',
                       'Coordinamos plantas de corriente directa, baterías y gabinetes de distribución bajo un mismo '
                       'alcance técnico. Así facilitamos la compatibilidad entre componentes y su integración con los '
                       'equipos que requieren alimentación DC.'),
                      ('Mantenimiento para conservar la confiabilidad',
                       'Combinamos revisiones preventivas y atención correctiva para identificar deterioros y resolver '
                       'fallas. Este seguimiento ayuda a tomar decisiones oportunas sobre ajustes, reparaciones y '
                       'reemplazo de componentes.')],
         'cta_title': 'Inicia tu proyecto eléctrico industrial con una solución profesional',
         'cta_text': 'Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o '
                     'ejecutar tu sistema eléctrico de forma segura, eficiente y conforme a norma.'},
        'en': {'nav': 'Direct Current',
         'title': 'Direct Current (DC) Solutions',
         'meta': 'Direct current solutions: engineering, DC power plants, battery banks, distribution cabinets, testing '
                 'and maintenance services for critical infrastructure.',
         'keywords': 'direct current, DC systems, DC power plants, battery banks, DC distribution, backup power, '
                     'maintenance, Grupo Arcondec',
         'h1': 'Direct current (DC) solutions',
         'lead': 'We design and implement direct current systems tailored to your power supply, backup and operational '
                 'continuity needs.',
         'tagline': 'Specialized electrical engineering for DC supply and backup',
         'intro_h2': 'Backup power for the systems that sustain your operations',
         'intro': ['At Grupo Arcondec, we develop direct current solutions for critical infrastructure, from technical '
                   'sizing to installation and commissioning. We integrate DC power plants, battery banks and '
                   'distribution cabinets according to each project’s requirements.',
                   'Our service includes engineering, equipment supply, installation and testing, taking electrical '
                   'demand, required autonomy and operating conditions into account. We coordinate supply, storage and '
                   'distribution components to function as an integrated system.',
                   'We complement each solution with preventive and corrective electrical maintenance to identify '
                   'deterioration, address faults and preserve the operating condition of DC infrastructure.'],
         'cta_btn': 'Tell us about your project',
         'scope_eyebrow': 'DC supply and backup',
         'scope_intro': 'Five disciplines to integrate your DC infrastructure.',
         'list_title': 'Integrated direct current solutions',
         'list': [('DC electrical engineering and design',
                   'We develop the electrical design around equipment supply and backup requirements. We define system '
                   'capacities, configuration and distribution, incorporating drawings, diagrams and technical criteria '
                   'to guide component selection and installation.'),
                  ('DC power plants',
                   'We supply and install DC power plants according to project capacity and configuration. We integrate '
                   'rectification equipment with battery banks and DC distribution, taking load supply and backup system '
                   'recharge requirements into account.'),
                  ('Battery bank sizing',
                   'We size battery banks according to the load, required backup duration and operating conditions. We '
                   'define their capacity and configuration, considering compatibility with the DC power plant and '
                   'installation, access and maintenance needs.'),
                  ('DC distribution cabinets',
                   'We supply and install direct current distribution cabinets to organize the supply to project '
                   'circuits. We integrate connections and protection according to anticipated loads, facilitating '
                   'circuit identification and access for inspections and servicing.'),
                  ('Testing, commissioning and maintenance',
                   'We test equipment and verify integration before operation, according to the project scope. We provide '
                   'preventive and corrective maintenance for electrical installations and DC systems to assess their '
                   'condition, address deviations and support their operation.')],
         'benefits_title': 'Backup power aligned with your operations',
         'benefits_intro': 'DC system availability depends on equipment capacity, battery autonomy and component '
                           'condition. At Arcondec, we integrate engineering, supply and maintenance to address these '
                           'needs during implementation and operation.',
         'benefits': [('Autonomy tailored to your needs',
                       'We size the battery bank according to loads and required backup duration. This enables energy '
                       'reserve planning around the project’s operational priorities.'),
                      ('Integrated supply and distribution',
                       'We coordinate DC power plants, batteries and distribution cabinets under a shared technical '
                       'scope. This supports component compatibility and integration with equipment requiring DC power.'),
                      ('Maintenance to preserve reliability',
                       'We combine preventive inspections and corrective attention to identify deterioration and resolve '
                       'faults. This follow-up supports timely decisions on adjustments, repairs and component '
                       'replacement.')],
         'cta_title': 'Start your industrial electrical project with a professional solution',
         'cta_text': 'Receive technical advice from our specialists and discover how to design, optimize, or execute your '
                     'electrical system safely, efficiently, and in compliance with regulations.'},
    },
    {'key': 'coralt',
     'photos': [1, 2, 3, 4, 5, 6, 7, 8],
     'group': 'ie',
     'icon': 'fal fa-plug',
     'slug': {'es': 'soluciones-corriente-alterna-ca', 'en': 'alternating-current-solutions'},
     'es': {'nav': 'Corriente Alterna',
            'title': 'Soluciones de corriente alterna AC',
            'meta': 'Sistemas de corriente alterna: tableros de distribución, transferencia automática, alimentadores y '
                    'respaldo con planta de emergencia para infraestructura crítica.',
            'keywords': 'corriente alterna, tableros de distribución, transferencia automática, alimentadores, planta de '
                        'emergencia, media tensión, infraestructura crítica',
            'h1': 'Soluciones de corriente alterna (AC)',
            'lead': 'Integramos sistemas de distribución, potencia y control en media y baja tensión para respaldar la '
                    'continuidad y eficiencia de tu operación.',
            'tagline': 'Ingeniería eléctrica para distribución y gestión de energía',
            'intro_h2': 'Infraestructura eléctrica desde la alimentación hasta cada punto de consumo',
            'intro': ['En Grupo Arcondec desarrollamos e implementamos soluciones de corriente alterna para centros de '
                      'datos, industria e infraestructura crítica. Integramos subestaciones, alimentadores, canalizaciones '
                      'y tableros para distribuir la energía de acuerdo con las necesidades de capacidad, seguridad y '
                      'disponibilidad de cada instalación.',
                      'Nuestro alcance comprende sistemas de transferencia automática, respaldo energético, protección '
                      'eléctrica, alumbrado y distribución especializada. Incorporamos monitoreo, supervisión y soluciones '
                      'de calidad de energía para facilitar el control de la infraestructura y evaluar su desempeño.',
                      'Complementamos estos servicios con diagnóstico, mantenimiento especializado y soluciones de '
                      'generación distribuida y energía renovable, conforme a las condiciones técnicas y los objetivos de '
                      'cada proyecto.'],
            'list_title': 'Soluciones integrales de corriente alterna',
            'list': [('Subestaciones y distribución eléctrica',
                      'Integramos subestaciones compactas e hipercompactas, alimentadores y canalizaciones en media y baja '
                      'tensión. Instalamos tableros de distribución, potencia y control, así como sistemas de alumbrado, '
                      'contactos regulados y circuitos especializados conforme a las cargas y los requerimientos del '
                      'proyecto.'),
                     ('Transferencia automática y respaldo energético',
                      'Implementamos sistemas de transferencia automática e integramos fuentes de respaldo para atender '
                      'las necesidades de las cargas prioritarias. Coordinamos su conexión y secuencia de funcionamiento '
                      'con la distribución eléctrica, considerando los requerimientos de continuidad y los tiempos de '
                      'respuesta de cada instalación.'),
                     ('Protección eléctrica y calidad de energía',
                      'Desarrollamos soluciones de coordinación y selectividad de protecciones, sistemas de puesta a '
                      'tierra y protección ante fallas eléctricas. Integramos filtrado de armónicos y corrección del '
                      'factor de potencia según el diagnóstico de la instalación, para atender condiciones que afectan el '
                      'desempeño de la red y sus equipos.'),
                     ('Monitoreo y supervisión eléctrica',
                      'Integramos analizadores de red, medidores de energía y protocolos de comunicación para supervisar '
                      'las variables eléctricas de la instalación. Facilitamos el seguimiento de consumos, demanda y '
                      'condiciones de operación, aportando información para detectar desviaciones y orientar decisiones de '
                      'gestión energética.'),
                     ('Mantenimiento y soluciones de generación',
                      'Realizamos diagnóstico y mantenimiento especializado de la infraestructura eléctrica para '
                      'identificar deterioros y atender necesidades de intervención. Desarrollamos soluciones de '
                      'generación distribuida y energía renovable, considerando su integración con la red interna y los '
                      'objetivos energéticos del proyecto.')],
            'benefits_title': 'Mayor control sobre tu infraestructura eléctrica',
            'benefits_intro': 'Una instalación de corriente alterna requiere distribución adecuada, protecciones '
                              'coordinadas y visibilidad sobre su funcionamiento. En Arcondec integramos estos elementos '
                              'para respaldar las cargas de tu operación, facilitar el mantenimiento y generar información '
                              'útil para administrar la energía.',
            'benefits': [('Distribución y respaldo coordinados',
                          'Integramos la alimentación principal, los tableros y los sistemas de transferencia con las '
                          'necesidades de las cargas prioritarias. Esto permite establecer una respuesta de respaldo '
                          'acorde con los requerimientos de cada proceso.'),
                         ('Información para gestionar la energía',
                          'El monitoreo de variables eléctricas permite identificar patrones de consumo y desviaciones de '
                          'funcionamiento. Estos datos facilitan la evaluación de oportunidades de eficiencia y la '
                          'planeación de ajustes en la instalación.'),
                         ('Protección y mantenimiento con criterio técnico',
                          'Combinamos coordinación de protecciones, diagnóstico y mantenimiento para atender las '
                          'condiciones de la infraestructura. Este enfoque ayuda a limitar el impacto de las fallas y a '
                          'priorizar intervenciones según el estado y la función de los equipos.')],
            'cta_title': 'Inicia tu proyecto eléctrico industrial con una solución profesional',
            'cta_text': 'Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o '
                        'ejecutar tu sistema eléctrico con seguridad, eficiencia y cumplimiento normativo.',
            'cta_btn': 'Cuéntanos sobre tu proyecto',
            'scope_eyebrow': 'Distribución y gestión de energía',
            'scope_intro': 'Cinco especialidades para integrar tu infraestructura eléctrica.'},
     'en': {'nav': 'Alternating Current',
            'title': 'Alternating Current AC Solutions',
            'meta': 'Alternating current systems: distribution switchboards, automatic transfer, power feeders and '
                    'emergency generator backup for critical infrastructure.',
            'keywords': 'alternating current, distribution switchboards, automatic transfer, feeders, emergency generator, '
                        'medium voltage, critical infrastructure',
            'h1': 'Alternating current (AC) solutions',
            'lead': 'We integrate medium- and low-voltage distribution, power and control systems to support the '
                    'continuity and efficiency of your operation.',
            'tagline': 'Electrical engineering for energy distribution and management',
            'intro_h2': 'Electrical infrastructure from the supply to every point of use',
            'intro': ['At Grupo Arcondec, we develop and implement alternating current solutions for data centers, '
                      'industry and critical infrastructure. We integrate substations, feeders, raceways and switchboards '
                      'to distribute energy according to the capacity, safety and availability requirements of each '
                      'facility.',
                      'Our scope includes automatic transfer systems, backup power, electrical protection, lighting and '
                      'specialized distribution. We incorporate monitoring, supervision and power quality solutions to '
                      'facilitate infrastructure management and assess its performance.',
                      'We complement these services with diagnostics, specialized maintenance, and distributed generation '
                      'and renewable energy solutions, according to the technical conditions and objectives of each '
                      'project.'],
            'list_title': 'Integrated alternating current solutions',
            'list': [('Substations and electrical distribution',
                      'We integrate compact and ultra-compact substations, feeders and raceways at medium and low voltage. '
                      'We install distribution, power and control switchboards, as well as lighting systems, regulated '
                      'power outlets and specialized circuits according to project loads and requirements.'),
                     ('Automatic transfer and backup power',
                      'We implement automatic transfer systems and integrate backup sources to meet the needs of priority '
                      'loads. We coordinate their connection and operating sequence with electrical distribution, '
                      'considering the continuity requirements and response times of each facility.'),
                     ('Electrical protection and power quality',
                      'We develop protection coordination and selectivity solutions, grounding systems and protection '
                      'against electrical faults. We integrate harmonic filtering and power factor correction based on the '
                      'facility assessment to address conditions affecting network and equipment performance.'),
                     ('Electrical monitoring and supervision',
                      'We integrate power analyzers, energy meters and communication protocols to monitor electrical '
                      'variables within the facility. We facilitate tracking of consumption, demand and operating '
                      'conditions, providing information to detect deviations and guide energy management decisions.'),
                     ('Maintenance and generation solutions',
                      'We perform diagnostics and specialized maintenance of electrical infrastructure to identify '
                      'deterioration and address intervention needs. We develop distributed generation and renewable '
                      'energy solutions, considering integration with the internal network and the energy objectives of '
                      'the project.')],
            'benefits_title': 'Greater control over your electrical infrastructure',
            'benefits_intro': 'An alternating current installation requires appropriate distribution, coordinated '
                              'protection and visibility into its performance. At Arcondec, we integrate these elements to '
                              'support operational loads, facilitate maintenance and provide useful information for energy '
                              'management.',
            'benefits': [('Coordinated distribution and backup',
                          'We integrate the main supply, switchboards and transfer systems with the needs of priority '
                          'loads. This establishes a backup response aligned with the requirements of each process.'),
                         ('Information for energy management',
                          'Monitoring electrical variables helps identify consumption patterns and operating deviations. '
                          'These data facilitate the assessment of efficiency opportunities and planning of adjustments to '
                          'the installation.'),
                         ('Protection and maintenance based on technical assessment',
                          'We combine protection coordination, diagnostics and maintenance to address infrastructure '
                          'conditions. This approach helps limit the impact of faults and prioritize interventions '
                          'according to equipment condition and function.')],
            'cta_title': 'Start your industrial electrical project with a professional solution',
            'cta_text': 'Receive technical advice from our specialists and discover how to design, optimize, or execute '
                        'your electrical system safely, efficiently, and in compliance with regulations.',
            'cta_btn': 'Tell us about your project',
            'scope_eyebrow': 'Energy distribution and management',
            'scope_intro': 'Five specialties to integrate your electrical infrastructure.'},
     'scope_photos': [9, 10, 11, 12, 13]},
    {'key': 'tierra',
     'main_photo': 12,
     'photos': [1, 2, 3, 4, 5, 6],
     'group': 'ie',
     'icon': 'fal fa-shield-check',
     'slug': {'es': 'diseno-sistemas-de-tierras', 'en': 'grounding-system-design'},
     'es': {'nav': 'Diseño de Tierras',
            'title': 'Diseño de redes de tierras y protección',
            'meta': 'Diseño y construcción de sistemas de tierra física: malla, electrodos, soldadura exotérmica, barras '
                    'master, supresión de transitorios y protección contra descargas.',
            'keywords': 'sistema de tierras, tierra física, malla de tierra, soldadura exotérmica, electrodo, pararrayos, '
                        'supresores de transitorios, resistividad',
            'h1': 'Diseño de redes de tierras y protección atmosférica',
            'lead': 'Integramos sistemas de puesta a tierra y protección contra descargas atmosféricas para contribuir a '
                    'la seguridad de las personas, los equipos y tu infraestructura.',
            'tagline': 'Ingeniería eléctrica especializada en sistemas de protección',
            'intro_h2': 'Protección eléctrica desde el diseño de tu infraestructura',
            'intro': ['En Grupo Arcondec diseñamos sistemas de puesta a tierra para centros de datos, industria y entornos '
                      'de misión crítica. Desarrollamos soluciones conforme a las características de cada instalación, '
                      'considerando la seguridad del personal, la protección de los equipos y su integración con la '
                      'infraestructura eléctrica.',
                      'Nuestro alcance comprende sistemas de tierra física, protección ante fallas de aislamiento, tierra '
                      'aislada para aplicaciones específicas y protección contra descargas atmosféricas. Coordinamos estos '
                      'elementos con la distribución eléctrica y los requerimientos de los equipos para establecer una '
                      'solución integral.',
                      'Definimos la configuración y los criterios técnicos del sistema desde la ingeniería, facilitando su '
                      'implementación y su coordinación con las demás especialidades del proyecto.'],
            'list_title': 'Soluciones integrales de puesta a tierra y protección',
            'list': [('Ingeniería y diseño de redes de tierras',
                      'Desarrollamos la configuración de la red de tierras de acuerdo con las características del sitio y '
                      'los requerimientos de la instalación. Definimos la disposición de conductores, electrodos y '
                      'conexiones, integrando la documentación técnica para orientar su ejecución y coordinación con la '
                      'infraestructura eléctrica.'),
                     ('Sistemas de tierra física',
                      'Diseñamos sistemas de puesta a tierra para integrar equipos, estructuras y elementos conductores de '
                      'la instalación. Consideramos las conexiones de protección y la unión equipotencial como parte del '
                      'diseño, contribuyendo a reducir diferencias de potencial que puedan representar un riesgo.'),
                     ('Protección ante fallas de aislamiento',
                      'Integramos criterios de puesta a tierra y unión de equipos para contribuir a la protección ante '
                      'fallas de aislamiento eléctrico. Coordinamos estas medidas con los dispositivos de protección de la '
                      'instalación, favoreciendo la desconexión del circuito afectado cuando corresponde.'),
                     ('Tierra aislada para equipos especializados',
                      'Desarrollamos soluciones de tierra aislada (IG) para los equipos y circuitos que lo requieren '
                      'conforme al proyecto. Definimos sus conductores y trayectorias, manteniendo su integración con el '
                      'sistema general de puesta a tierra y considerando los requerimientos técnicos de los equipos '
                      'conectados.'),
                     ('Protección contra descargas atmosféricas',
                      'Diseñamos sistemas de protección contra descargas atmosféricas, integrando elementos de captación, '
                      'conductores de bajada y su conexión al sistema de puesta a tierra. Coordinamos su disposición con '
                      'las características de la edificación y las instalaciones para reducir los riesgos asociados al '
                      'impacto de un rayo.')],
            'benefits_title': 'Protección coordinada para personas e infraestructura',
            'benefits_intro': 'La protección eléctrica requiere que la puesta a tierra, las conexiones entre elementos '
                              'conductores y los dispositivos de protección trabajen de manera coordinada. En Arcondec '
                              'integramos estos criterios desde el diseño para atender los riesgos y las necesidades '
                              'particulares de cada proyecto.',
            'benefits': [('Seguridad para el personal',
                          'Consideramos la puesta a tierra y las conexiones de protección para contribuir a reducir '
                          'riesgos por contacto con partes metálicas que puedan energizarse ante una falla.'),
                         ('Protección integrada de equipos e instalaciones',
                          'Coordinamos la red de tierras con la infraestructura eléctrica y la protección atmosférica. '
                          'Este enfoque permite atender distintos riesgos bajo un mismo criterio de ingeniería.'),
                         ('Bases técnicas para futuras intervenciones',
                          'La documentación del diseño facilita identificar conexiones, trayectorias y componentes del '
                          'sistema. Esto ayuda a planear revisiones, adecuaciones y ampliaciones conservando los criterios '
                          'de protección del proyecto.')],
            'cta_title': 'Inicia tu proyecto eléctrico industrial con una solución profesional',
            'cta_text': 'Recibe una asesoría técnica con nuestros especialistas y descubre cómo diseñar, optimizar o '
                        'ejecutar tu sistema eléctrico con seguridad, eficiencia y cumplimiento normativo.',
            'cta_btn': 'Cuéntanos sobre tu proyecto',
            'scope_eyebrow': 'Puesta a tierra y protección',
            'scope_intro': 'Cinco especialidades para proteger tu infraestructura.'},
     'en': {'nav': 'Grounding Design',
            'title': 'Grounding Design and Lightning Protection',
            'meta': 'Design and construction of grounding systems: ground grid, electrodes, exothermic welding, master '
                    'bars, surge suppression and lightning protection.',
            'keywords': 'grounding system, earthing, ground grid, exothermic welding, electrode, lightning protection, '
                        'surge suppressors, soil resistivity',
            'h1': 'Grounding network design and lightning protection',
            'lead': 'We integrate grounding and lightning protection systems to contribute to the safety of people, '
                    'equipment and your infrastructure.',
            'tagline': 'Electrical engineering specialized in protection systems',
            'intro_h2': 'Electrical protection built into your infrastructure design',
            'intro': ['At Grupo Arcondec, we design grounding systems for data centers, industry and mission-critical '
                      'environments. We develop solutions according to the characteristics of each facility, considering '
                      'personnel safety, equipment protection and integration with electrical infrastructure.',
                      'Our scope includes grounding systems, protection against insulation faults, isolated grounding for '
                      'specific applications and lightning protection. We coordinate these elements with electrical '
                      'distribution and equipment requirements to establish an integrated solution.',
                      'We define system configuration and technical criteria during engineering, facilitating '
                      'implementation and coordination with other project disciplines.'],
            'list_title': 'Integrated grounding and protection solutions',
            'list': [('Grounding network engineering and design',
                      'We develop the grounding network configuration according to site characteristics and facility '
                      'requirements. We define conductor, electrode and connection layouts, incorporating technical '
                      'documentation to guide execution and coordination with electrical infrastructure.'),
                     ('Grounding systems',
                      'We design grounding systems to connect equipment, structures and conductive elements within the '
                      'installation. We consider protective connections and equipotential bonding as part of the design, '
                      'helping reduce potential differences that could pose a risk.'),
                     ('Protection against insulation faults',
                      'We integrate grounding and equipment bonding criteria to contribute to protection against '
                      'electrical insulation faults. We coordinate these measures with the installation’s protective '
                      'devices, supporting disconnection of the affected circuit when appropriate.'),
                     ('Isolated grounding for specialized equipment',
                      'We develop isolated grounding (IG) solutions for equipment and circuits that require them according '
                      'to the project. We define conductors and routes, maintaining integration with the overall grounding '
                      'system and considering the technical requirements of connected equipment.'),
                     ('Lightning protection',
                      'We design lightning protection systems, integrating air termination devices, down conductors and '
                      'their connection to the grounding system. We coordinate their placement with building and '
                      'installation characteristics to reduce risks associated with lightning strikes.')],
            'benefits_title': 'Coordinated protection for people and infrastructure',
            'benefits_intro': 'Electrical protection requires grounding, connections between conductive elements and '
                              'protective devices to work together. At Arcondec, we integrate these criteria from the '
                              'design stage to address the risks and specific needs of each project.',
            'benefits': [('Personnel safety',
                          'We consider grounding and protective connections to help reduce risks from contact with metal '
                          'parts that may become energized during a fault.'),
                         ('Integrated protection for equipment and facilities',
                          'We coordinate the grounding network with electrical infrastructure and lightning protection. '
                          'This approach addresses different risks under a common engineering framework.'),
                         ('Technical foundations for future interventions',
                          'Design documentation facilitates identification of system connections, routes and components. '
                          'This supports planning of inspections, modifications and expansions while preserving project '
                          'protection criteria.')],
            'cta_title': 'Start your industrial electrical project with a professional solution',
            'cta_text': 'Receive technical advice from our specialists and discover how to design, optimize, or execute '
                        'your electrical system safely, efficiently, and in compliance with regulations.',
            'cta_btn': 'Tell us about your project',
            'scope_eyebrow': 'Grounding and protection',
            'scope_intro': 'Five specialties to protect your infrastructure.'},
     'scope_photos': [13, 8, 9, 10, 11]},
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
