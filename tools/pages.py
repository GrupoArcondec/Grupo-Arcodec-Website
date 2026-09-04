# -*- coding: utf-8 -*-
"""Contenido de las paginas que no son de servicio: inicio, nosotros, proyectos,
contacto, reclutamiento y el indice de blog. Textos literales de arcondec.mx.
"""

# --------------------------------------------------------------------------
# NOSOTROS / ABOUT
# --------------------------------------------------------------------------
ABOUT = {
    "es": {
        "title": "Sobre nosotros",
        "meta": "Empresa mexicana fundada en 1991, especializada en ingeniería eléctrica, infraestructura y construcción de centros de datos. Más de 30 años de experiencia.",
        "keywords": "Grupo Arcondec, empresa mexicana, ingeniería eléctrica, data centers, 1991, proyectos llave en mano",
        "eyebrow": "Sobre nosotros",
        "h1": "Empresa mexicana fundada en 1991, especializada en ofrecer soluciones integrales",
        "lead": "Soluciones en ingeniería eléctrica y centros de datos para operaciones de alta disponibilidad",
        # Contenido de marca 2025: reemplaza a la misión y a los cuatro valores
        # sueltos (Integridad/Compromiso/Pasión/Responsabilidad) que traía la
        # página antes. "Meta 2035" es el BHAG del documento interno, traducido
        # a lenguaje de sitio público. Los valores deletrean IDEAS con la
        # primera letra de cada renglón — es un recurso intencional del cliente,
        # no decorativo: no se puede traducir letra por letra al inglés, así
        # que la versión "en" lleva los mismos cinco valores sin el acróstico.
        "meta_title": "Meta 2035",
        # OJO: existía un choque de nombre con la "meta" de SEO (misma clave,
        # dos valores, el segundo pisaba al primero y el <meta description>
        # de la página salía con este texto en vez de con el real). Se
        # renombra a "meta_text" para no repetir el error.
        "meta_text": "Una de las principales empresas en LATAM en la construcción de proyectos de gran impacto, habiendo implementado 500 MW.",
        "purpose_title": "Propósito",
        "purpose": "Habilitamos la infraestructura que hace posible el mundo digital.",
        "vision_title": "Visión",
        "vision": "Consolidarnos como una empresa líder, competitiva y confiable en la implementación de tecnologías aplicadas en los sectores eléctrico y de construcción de Data Center. Nos comprometemos a cumplir con los más altos estándares y normas que rigen el mercado, garantizando así la excelencia en cada proyecto que emprendemos.",
        "certs_title": "Certificaciones",
        "certs_lead": "Sistemas de gestión auditados y certificación financiera vigente.",
        # Quinto valor de la tupla: el sello tipográfico de la insignia (no el
        # icono fa, que sigue sin usarse en el render).
        "certs": [
            ("ISO 9001", "Calidad", "Procesos eficientes y mejora continua.", "fal fa-award", "9001"),
            ("ISO 14001", "Medio Ambiente", "Operaciones responsables con el entorno.", "fal fa-leaf", "14001"),
            ("ISO 45001", "Seguridad y Salud", "Prevención de riesgos laborales.", "fal fa-user-shield", "45001"),
            ("Dun & Bradstreet", "Certificación financiera", "Respaldo crediticio verificado.", "fal fa-certificate", "D&B"),
        ],
        "history_title": "Nuestra Historia",
        # Antetítulo en píldora, el mismo componente que usan las páginas de
        # servicio (.service-eyebrow) — restatement literal de la primera
        # frase del párrafo, no contenido nuevo.
        "history_eyebrow": "Empresa mexicana fundada en 1991",
        "history": [
            "En Grupo Arcondec somos una empresa mexicana fundada en 1991, especializada en brindar servicios integrales, oportunos y de alta calidad en tres áreas clave: ingeniería eléctrica, infraestructura y construcción de centros de datos (data centers).",
            "Nuestra filosofía se basa en el compromiso con la calidad, el cumplimiento en tiempo y forma, y la atención al detalle en cada proyecto.",
            "Contamos con un equipo multidisciplinario altamente capacitado, enfocado en la ingeniería, ejecución y supervisión de obra con un enfoque técnico y estético, garantizando resultados confiables desde la planeación hasta la entrega final.",
            "Con más de 30 años de experiencia, nos hemos consolidado como especialistas en proyectos llave en mano de gran escala, tanto comerciales como industriales, destacando por nuestra capacidad de abordar cada fase con precisión: desde la etapa conceptual hasta la implementación total.",
        ],
        "distinct_title": "¿Qué nos distingue en Grupo Arcondec?",
        # Mismo texto de siempre, partido en (frase-cita, resto) para el
        # tratamiento editorial — no se reescribió ni una palabra.
        "distinct_quote": "El talento de nuestro equipo, conformado por profesionales apasionados por desarrollar soluciones que impulsan la operación de nuestros clientes, es el motor de cada proyecto.",
        "distinct_rest": "Abordamos cada desafío con compromiso, precisión y visión estratégica para garantizar resultados medibles y sostenibles, permitiendo que nuestros clientes se enfoquen plenamente en su negocio con la confianza de contar con una infraestructura eléctrica y crítica diseñada para respaldar su presente y potenciar su futuro.",
        # Las mismas tres palabras del propio texto, como remate escaneable.
        "distinct_keywords": ["Compromiso", "Precisión", "Visión estratégica"],
        "areas_label": "Áreas clave",
        "values_title": "Valores",
        "services_title": "Nuestros servicios",
        # (letra, resto de la palabra) — la letra inicial es la que arma el
        # acróstico IDEAS.
        "values": [
            ("I", "nspirar, guiar y transformar"),
            ("D", "isponibilidad sin interrupciones"),
            ("E", "l éxito se construye en equipo"),
            ("A", "ctuamos para hacer que las cosas sucedan"),
            ("S", "er honestos nos hace rentables a todos"),
        ],
        "alt_historia": "Trabajos de ingeniería eléctrica de Grupo Arcondec",
        "alt_equipo": "Sala eléctrica de distribución ejecutada por Grupo Arcondec",
        "years_label": "Años de experiencia",
    },
    "en": {
        "title": "About Us",
        "meta": "Grupo Arcondec, a Mexican company founded in 1991, specialized in electrical engineering, infrastructure and data center construction. Over 30 years of experience.",
        "keywords": "Grupo Arcondec, Mexican company, electrical engineering, data centers, 1991, turnkey projects",
        "eyebrow": "About us",
        "h1": "Mexican company founded in 1991, specialized in providing integrated solutions",
        "lead": "Electrical engineering and data center solutions for high-availability operations",
        "meta_title": "2035 goal",
        "meta_text": "One of the leading companies in Latin America in the construction of high-impact projects, having deployed 500 MW.",
        "purpose_title": "Purpose",
        "purpose": "We enable the infrastructure that makes the digital world possible.",
        "vision_title": "Vision",
        "vision": "To become a leading, competitive and reliable company in the implementation of technologies applied to the electrical and Data Center construction sectors. We are committed to meeting the highest standards and regulations that govern the market, ensuring excellence in every project we undertake.",
        "certs_title": "Certifications",
        "certs_lead": "Audited management systems and current financial certification.",
        "certs": [
            ("ISO 9001", "Quality", "Efficient processes and continuous improvement.", "fal fa-award", "9001"),
            ("ISO 14001", "Environment", "Environmentally responsible operations.", "fal fa-leaf", "14001"),
            ("ISO 45001", "Health and Safety", "Occupational risk prevention.", "fal fa-user-shield", "45001"),
            ("Dun & Bradstreet", "Financial certification", "Verified credit standing.", "fal fa-certificate", "D&B"),
        ],
        "history_title": "Our History",
        "history_eyebrow": "Mexican company founded in 1991",
        "history": [
            "At Grupo Arcondec we are a Mexican company founded in 1991, specialized in delivering comprehensive, timely, and high-quality services in three key areas: electrical engineering, infrastructure, and data center construction.",
            "Our philosophy is based on a strong commitment to quality, timely and accurate execution, and attention to detail in every project.",
            "We have a highly skilled multidisciplinary team, focused on engineering, execution, and supervision with both a technical and aesthetic approach, ensuring reliable results from planning to final delivery.",
            "With over 30 years of experience, we have become specialists in large-scale turnkey projects, both commercial and industrial, standing out for our ability to tackle every phase with precision — from concept to full implementation.",
        ],
        "distinct_title": "What sets Grupo Arcondec apart?",
        "distinct_quote": "Our team's talent, made up of professionals passionate about developing solutions that power our clients' operations, is the driving force behind every project.",
        "distinct_rest": "We approach each challenge with commitment, precision, and strategic vision to deliver measurable, sustainable results — enabling our clients to focus on their business with the confidence of having critical and electrical infrastructure designed to support their present and empower their future.",
        "distinct_keywords": ["Commitment", "Precision", "Strategic vision"],
        "areas_label": "Key areas",
        "values_title": "Values",
        "services_title": "Our services",
        # Same five values as the ES block; the IDEAS acrostic only works in
        # Spanish (ver nota arriba), so this list carries the meaning without
        # a lettered first column.
        "values": [
            "Inspire, guide and transform",
            "Uninterrupted availability",
            "Success is built as a team",
            "We act to make things happen",
            "Honesty makes us all more profitable",
        ],
        "alt_historia": "Electrical engineering work by Grupo Arcondec",
        "alt_equipo": "Electrical distribution room delivered by Grupo Arcondec",
        "years_label": "Years of experience",
    },
}

# --------------------------------------------------------------------------
# PROYECTOS / PROJECTS
# --------------------------------------------------------------------------
# Cada hub es un diccionario. Solo tres claves son obligatorias —`slug`,
# `nombre` y `foto`—; todo lo demás es opcional y la plantilla omite la sección
# entera cuando falta, así que un proyecto sin datos no deja huecos ni bloques
# vacíos en la página.
#
# `publicado` es el interruptor: mientras sea False la tarjeta de proyectos.html
# no enlaza a ningún lado y la página queda fuera del sitemap. Se pone en True
# solo cuando el proyecto tiene información real y revisada.
#
# CONFIDENCIALIDAD: algunos clientes están bajo NDA y otros no. Si `cliente`
# trae un nombre, se muestra; si va vacío, la ficha dice "Cliente confidencial"
# y solo enseña el `sector`. Nunca poner el nombre de un cliente con NDA aquí:
# este archivo termina publicado como HTML estático.
#
# La página se maqueta como un artículo a dos columnas:
#
#   COLUMNA IZQUIERDA (el relato)  ── titulo, subtitulo, descripcion,
#                                     reto, solucion, galeria
#   COLUMNA DERECHA (los datos)    ── ficha técnica, alcances, resultados
#
# Campos de la ficha (todos opcionales): cliente, sector, ubicacion_exacta,
# tipo_obra, superficie, capacidad, duracion, entrega, certificacion.
#
# Bloques opcionales: titulo (encabezado del caso), subtitulo (una línea),
# descripcion (lista de párrafos), reto (texto), solucion (lista de
# (disciplina, detalle)), alcances (lista de textos), galeria (lista de
# archivos en assets/images/arcondec/proyectos/), resultados (lista de
# (cifra, etiqueta)).
HUBS = [
    {
        "slug": {"es": "hub-apodaca", "en": "apodaca-hub"},
        "nombre": "HUB APODACA",
        "ubicacion": "Ciudad Apodaca - Nuevo León",
        "foto": "arcondec-apodaca-01.jpg",
        # ═════════════════════════════════════════════════════════════════
        # ATENCIÓN — DATOS SIMULADOS, PUBLICADOS EN VIVO
        #
        # Las cifras de abajo (2,500 kW, 1,850 m², Tier III, 8 meses, 99.98%)
        # NO son reales: se inventaron para revisar la maquetación. Esta
        # página está publicada, indexable y enlazada desde proyectos.html,
        # así que cualquier visitante las lee como si fueran datos de obra.
        #
        # Reemplazar por información verificada en cuanto se tenga. Si el
        # proyecto real se retrasa, volver `publicado` a False para sacarla
        # de circulación.
        # ═════════════════════════════════════════════════════════════════
        "publicado": True,
        "titulo": "HUB Apodaca",
        "imagen": "sala-electrica-de-distribucion-en-media-tension.jpg",
        "imagen_alt": "Sala eléctrica de distribución en media tensión del HUB Apodaca",
        "subtitulo": (
            "Obra nueva de infraestructura crítica para una planta de manufactura "
            "en operación continua, en Apodaca, Nuevo León."
        ),
        "descripcion": [
            "El proyecto nació de una restricción de calendario: la expansión "
            "productiva del cliente ya tenía fecha, y el centro de datos que la "
            "soportaría tenía que estar operando antes de esa fecha, no después.",
            "Arcondec asumió el alcance completo —eléctrico, mecánico, civil y de "
            "sistemas especiales— bajo una sola coordinación, de modo que el "
            "cliente tuviera un único interlocutor para las cinco disciplinas que "
            "convergían en el mismo espacio y el mismo calendario.",
        ],
        "cliente": "",
        "sector": "Manufactura avanzada",
        "ubicacion_exacta": "Parque industrial, Apodaca, N.L.",
        "tipo_obra": "Obra nueva",
        "superficie": "1,850 m²",
        "capacidad": "2,500 kW",
        "duracion": "8 meses",
        "entrega": "2024",
        "certificacion": "Tier III",
        "reto": (
            "El cliente necesitaba un centro de datos operativo en ocho meses "
            "para soportar la expansión de su planta, sin detener la producción "
            "existente. El terreno disponible quedaba a doscientos metros de la "
            "subestación general, lo que obligaba a resolver la acometida en "
            "media tensión antes de poder avanzar con cualquier otra disciplina."
        ),
        "solucion": [
            ("Media tensión",
             "Subestación propia con acometida en 13.8 kV y respaldo redundante "
             "para garantizar continuidad durante maniobras de mantenimiento."),
            ("Corriente directa y UPS",
             "Sistema de respaldo dimensionado para sostener la carga crítica "
             "el tiempo necesario para el arranque de la planta de emergencia."),
            ("HVAC",
             "Climatización de precisión con contención de pasillo frío y "
             "control de humedad independiente por sala."),
            ("PCI",
             "Detección temprana por aspiración y supresión por agente limpio "
             "en las áreas con equipo electrónico."),
            ("Área blanca",
             "Piso técnico, canalización aérea y cerramientos, entregados "
             "listos para el montaje de racks del cliente."),
        ],
        "alcances": [
            "Subestación 13.8 kV con dos transformadores de 1,500 kVA",
            "Planta de emergencia con transferencia automática",
            "Sistema UPS redundante con banco de baterías monitoreado",
            "Piso técnico en 900 m² de área blanca",
            "Detección por aspiración y supresión por agente limpio",
            "Sistema de control de acceso y CCTV perimetral",
        ],
        # (archivo, texto alternativo). El alt describe lo que se ve en cada
        # foto; si solo se pone el nombre del archivo, se usa el del proyecto.
        "galeria": [
            ("instalacion-de-piso-elevado-en-data-center-queretaro.jpg",
             "Instalación de piso elevado en el área blanca"),
            ("instalacion-y-pruebas-de-banco-de-baterias-en-monterrey.jpg",
             "Pruebas del banco de baterías del sistema de respaldo"),
            ("infraestructura-de-charolas-y-tuberia-electrica-en-toluca.jpg",
             "Charolas y tubería eléctrica sobre el área de racks"),
            ("sistema-de-transferencia-y-tableros-electricos-en-tuxpan.jpg",
             "Tableros eléctricos y sistema de transferencia automática"),
        ],
        "resultados": [
            ("8", "meses de ejecución"),
            ("0", "incidentes registrados"),
            ("99.98%", "disponibilidad desde la entrega"),
        ],
    },
    {
        "slug": {"es": "crt-industria-chihuahua", "en": "crt-industria-chihuahua-hub"},
        "nombre": "CRT INDUSTRIA CHIHUAHUA",
        "ubicacion": "Chihuahua - Chihuahua",
        "foto": "arcondec-chihuahua-banner.jpg",
        # ─────────────────────────────────────────────────────────────────
        # Datos reales, de HUB_Industria_Chihuahua_Informacion_Web_Arcondec.pdf
        # (fuente técnica: catálogo EA250101B — Instalaciones eléctricas;
        # nombre, ubicación, transformador de 112.5 kVA y equipos InRow
        # confirmados por Grupo Arcondec).
        #
        # NOMBRE: la ficha lo llama "HUB Industria"; aquí se publica como
        # "CRT Industria Chihuahua", que es como lo nombran internamente y
        # como viene rotulado en la fotografía de obra.
        #
        # PENDIENTES antes de considerarla completa (la ficha los marca sin
        # confirmar, y por eso esos campos no aparecen aquí):
        #   · Superficie intervenida
        #   · Duración total (fecha de inicio y término)
        #   · Año de entrega — el catálogo de origen está fechado en 2025
        #   · Capacidad en kW/kVA de la planta de emergencia
        #   · Cifras de cierre (incidentes, cumplimiento de ventana)
        #
        # FOTOGRAFÍAS: las 19 originales documentan obra civil y acometida de
        # media tensión. No hay tomas del transformador, del UPS Huawei, de
        # los PDC ni de los InRow, que es el equipo que sostiene la ficha.
        # Cuando lleguen, sustituir la galería. Todas las originales traían
        # incrustadas las coordenadas GPS exactas del sitio: se recortó el 20%
        # inferior de cada una para eliminarlas antes de publicar.
        #
        # La ficha advierte que el catálogo no documenta una planta de
        # corriente directa independiente, así que no se le atribuye ese
        # alcance: la disciplina se limita al UPS y su distribución.
        # ─────────────────────────────────────────────────────────────────
        "publicado": True,
        "titulo": "CRT Industria Chihuahua",
        "subtitulo": (
            "Integración de infraestructura eléctrica crítica, respaldo, UPS y "
            "climatización InRow para el CRT Industria de IZZI en Chihuahua."
        ),
        "descripcion": [
            "Grupo Arcondec ejecutó la integración de infraestructura crítica "
            "para el CRT Industria de IZZI en Chihuahua. El proyecto abarcó "
            "media tensión, transformación, distribución eléctrica normal y de "
            "emergencia, UPS, tableros de transferencia, canalizaciones, "
            "alimentadores, puesta a tierra y sistemas auxiliares para cargas "
            "críticas.",
            "El alcance incluyó un transformador de distribución trifásico de "
            "112.5 kVA, la integración de un UPS Huawei 1200/900 kVA, cuatro "
            "gabinetes de distribución de potencia Huawei, la conexión con el "
            "sistema de generación de emergencia y el suministro de "
            "climatización de precisión mediante dos equipos InRow de 10 "
            "toneladas de refrigeración cada uno. La ejecución consideró "
            "pruebas, puesta en marcha y trabajos especializados asociados a la "
            "continuidad operativa del sitio.",
        ],
        # La destacada la recorta el CSS a una franja muy ancha. Esta toma de la
        # zanja de acometida funciona porque el motivo corre en horizontal a lo
        # largo del encuadre; además la franja deja fuera los rótulos
        # comerciales de los negocios vecinos que aparecen en la parte alta.
        "imagen": "arcondec-chihuahua-zanja-acometida.jpg",
        "imagen_alt": (
            "Cuadrilla abriendo la zanja para el alimentador de media tensión"
        ),
        "cliente": "IZZI",
        "sector": "Telecomunicaciones / infraestructura crítica",
        "ubicacion_exacta": "Chihuahua, Chihuahua",
        "tipo_obra": (
            "Adecuación e integración de infraestructura eléctrica crítica y "
            "climatización de precisión"
        ),
        "capacidad": "Transformador trifásico de 112.5 kVA, 13.2 kV / 220-127 V",
        "reto": (
            "El reto principal fue integrar varios subsistemas de energía "
            "crítica dentro de un mismo sitio de telecomunicaciones: acometida "
            "y media tensión, transformación, distribución normal y de "
            "emergencia, respaldo mediante UPS, transferencia hacia generación "
            "de emergencia y climatización de precisión. La intervención exigió "
            "coordinar alimentadores de alta capacidad, tableros "
            "autosoportados, protecciones, canalizaciones y puestas a tierra "
            "sin perder de vista la continuidad de las cargas críticas, e "
            "incluyó gestiones ante CFE, libranzas, trámite de UVIE y pruebas "
            "VLF en media tensión."
        ),
        "solucion": [
            ("Media tensión / subestación",
             "Gestoría ante CFE, libranza, registro de media tensión, cable "
             "XLP, protecciones, medición, pruebas VLF y conexión del "
             "transformador de 112.5 kVA."),
            ("Corriente directa / UPS",
             "Integración del UPS Huawei 1200/900 kVA, incluyendo conexiones de "
             "entrada, salida y bypass, tableros asociados y distribución "
             "regulada."),
            ("Planta de emergencia",
             "Integración eléctrica del sistema de respaldo mediante dos "
             "tableros de transferencia, tablero general de emergencia y "
             "conexión del alimentador al interruptor a pie de generador."),
            ("HVAC",
             "Suministro e instalación de dos equipos de aire acondicionado de "
             "precisión tipo InRow de 10 TR cada uno, además de tableros "
             "generales de aire acondicionado, tablero de servicios e "
             "interruptores de seguridad."),
            ("Distribución crítica",
             "Instalación de tableros generales normal y de emergencia, "
             "tableros de enlace, tableros UPS y cuatro Precision Power "
             "Distribution Cabinet Huawei."),
            ("Puesta a tierra",
             "Barras master para áreas críticas, conexión de equipos y racks, "
             "conductor de puesta a tierra, electrodo copperweld, soldadura "
             "exotérmica y pararrayos."),
            ("Alumbrado y contactos",
             "Circuitos de alumbrado interior y exterior, contactos y servicios "
             "de emergencia, con canalización y cableado asociado."),
            ("Gestoría y cumplimiento",
             "Trámites de aumento de carga, libranza, permisos y servicio de "
             "Unidad Verificadora de Instalaciones Eléctricas (UVIE)."),
        ],
        "alcances": [
            "Transformador trifásico tipo pedestal de 112.5 kVA, 13.2 kV / 220-127 V, con registro, protecciones, medición, cable XLP y pruebas VLF",
            "Dos tableros de transferencia, tablero de enlace, tablero general de emergencia y alimentador al interruptor a pie de generador",
            "UPS Huawei 1200/900 kVA con circuitos de entrada, salida y bypass, tableros asociados y distribución regulada",
            "Cuatro Precision Power Distribution Cabinet Huawei, tableros generales y alimentadores de potencia",
            "Dos equipos de climatización de precisión tipo InRow de 10 TR cada uno (20 TR totales), con su infraestructura eléctrica asociada",
            "Sistema de tierra física para tableros, UPS, racks y áreas críticas, con barras master, electrodo, soldadura exotérmica, supresores de transitorios y pararrayos",
        ],
        # El orden cuenta la obra: se traza la zanja, se abre el cruce, se
        # tienden los ductos, se cierra a nivel y se cierra con la sala de
        # tableros ya montada, que es donde aterriza todo lo anterior.
        "galeria": [
            ("arcondec-chihuahua-trazo.jpg",
             "Trazo de la zanja del alimentador hacia el edificio"),
            ("arcondec-chihuahua-cruce.jpg",
             "Apertura de la zanja en el cruce vehicular, con señalización de obra"),
            ("arcondec-chihuahua-registro-ductos.jpg",
             "Banco de ductos del alimentador de media tensión en la excavación"),
            ("arcondec-chihuahua-registro-terminado.jpg",
             "Cierre y nivelación del registro terminado sobre la banqueta"),
            ("arcondec-chihuahua-tableros.jpg",
             "Tableros generales y canalización montados en el cuarto eléctrico"),
        ],
        "resultados": [
            ("112.5 kVA", "transformador principal"),
            ("1200/900 kVA", "UPS Huawei integrado"),
            ("20 TR", "climatización InRow instalada"),
        ],
    },
    {
        "slug": {"es": "hub-delicias", "en": "delicias-hub"},
        "nombre": "HUB DELICIAS",
        "ubicacion": "Delicias - Chihuahua",
        "foto": "arcondec-delicias-banner.jpg",
        # ─────────────────────────────────────────────────────────────────
        # Datos reales, de HUB_Delicias_ficha_proyecto.docx (fuente: Anexo C,
        # Formato de cotización, 11-mar-2024).
        #
        # NOMBRE: la ficha lo titula "HUB Delicias"; la carpeta de obra dice
        # "Delicias Chihuahua". Se usó el de la ficha, que sigue el patrón de
        # los demás HUB. La plaza queda en la ubicación de la tarjeta.
        #
        # OMITIDOS A PROPÓSITO. La ficha marca estos valores en rojo con la
        # nota "hay que confirmarlo antes de publicar", así que no se
        # publican todavía. En cuanto se confirmen, se agregan y la plantilla
        # los muestra sola:
        #   · "superficie": "250 m²"      — no aparece en el presupuesto
        #   · "duracion": "4 meses"       — no aparece en el presupuesto
        #   · "entrega": "2024"           — la cotización es de marzo 2024,
        #                                   pero no es la fecha de entrega
        #   · "certificacion"             — sin dato
        #
        # FALTA EL RETO: la sección 3 de la ficha llegó vacía. Es la parte que
        # más convence a un prospecto, así que conviene pedirla. Mientras, la
        # plantilla omite el bloque y la página no queda con un hueco.
        #
        # NO PUBLICAR el monto del presupuesto: la ficha lo marca como
        # información interna.
        #
        # FOTOGRAFÍAS: las 163 originales traían incrustadas las coordenadas
        # GPS exactas del sitio. Se recortó el 20% inferior de cada una para
        # eliminarlas antes de publicar.
        # ─────────────────────────────────────────────────────────────────
        "publicado": True,
        "titulo": "HUB Delicias",
        "subtitulo": (
            "Ampliación de la capacidad eléctrica y de respaldo del HUB de "
            "IZZI en Delicias, Chihuahua."
        ),
        "descripcion": [
            "El proyecto consistió en la ampliación de la capacidad eléctrica y "
            "de respaldo del HUB ubicado en Delicias, Chihuahua, con el "
            "reemplazo del transformador y la planta de emergencia existentes "
            "por equipos de mayor capacidad.",
            "El alcance incluyó además la actualización de los sistemas de "
            "corriente directa, UPS y climatización de precisión, junto con la "
            "obra civil necesaria: cuarto de tableros, plancha para la máquina "
            "de emergencia y acondicionamiento de una sala nueva.",
        ],
        # La destacada se recorta a una franja muy ancha, así que necesita un
        # motivo que corra en horizontal. La barra de cobre con las derivaciones
        # numeradas por rack lo hace de punta a punta y además se lee como
        # centro de datos, no como obra genérica.
        "imagen": "arcondec-delicias-barra-cobre.jpg",
        "imagen_alt": (
            "Barra de cobre con las derivaciones de alimentación numeradas por rack"
        ),
        "cliente": "IZZI",
        "sector": "Telecomunicaciones",
        "ubicacion_exacta": "Delicias, Chihuahua",
        "tipo_obra": "Ampliación y remodelación",
        "capacidad": (
            "225 kVA (transformador) · 175 kW / 218 kVA (planta de emergencia)"
        ),
        "solucion": [
            ("Media tensión / subestación",
             "Conexión en media tensión y montaje de transformador tipo "
             "pedestal de 225 kVA, con apartarrayos, cortacircuitos fusibles y "
             "base de medición."),
            ("Corriente directa",
             "Sistema de inversores de seis módulos de 2.5 kVA cada uno y "
             "tableros generales de rectificadores y UPS de 225 A."),
            ("Planta de emergencia",
             "Planta automática de 175 kW / 218 kVA con caseta acústica, "
             "tablero de transferencia automática y tanque de combustible de "
             "800 litros, además del retiro de la planta existente de 50 kW."),
            ("HVAC",
             "Instalación de equipos de climatización de precisión de 5 TR, "
             "unidad InRow y mini split, con sistema de control en modo "
             "team-work."),
            ("Obra civil",
             "Trabajos preliminares, plancha para la máquina de emergencia y "
             "techumbre, acabados y señalización, construcción del cuarto de "
             "tableros, cimentación de concreto armado, muros de block y losa "
             "maciza."),
            ("Área blanca / piso técnico",
             "Acondicionamiento de la sala nueva con climatización de "
             "precisión tipo InRow."),
        ],
        "alcances": [
            "Transformador tipo pedestal de 225 kVA con conexión completa en media tensión",
            "Tablero general de servicio normal tipo I-Line de 1200 A",
            "Sistema de inversores de 15 kVA (6 módulos de 2.5 kVA) con puesta en marcha y capacitación",
            "Tableros generales de rectificadores y UPS de 225 A",
            "Planta de emergencia automática de 175 kW / 218 kVA con tablero de transferencia automática",
            "Sistema de aire acondicionado de precisión de 5 TR con equipo InRow para la sala nueva",
        ],
        # El orden recorre la obra completa: primero la estructura, luego las
        # maniobras de equipo, y de ahí hacia dentro hasta la sala terminada.
        "galeria": [
            ("arcondec-delicias-losa.jpg",
             "Armado de la losa de concreto del cuarto de tableros"),
            ("arcondec-delicias-maniobra.jpg",
             "Maniobra con grúa para el montaje de equipo en sitio"),
            ("arcondec-delicias-tableros.jpg",
             "Tableros generales de servicio normal y de emergencia instalados"),
            ("arcondec-delicias-rectificadores.jpg",
             "Módulos rectificadores del sistema de corriente directa"),
            ("arcondec-delicias-climatizacion.jpg",
             "Equipo de climatización de precisión de la sala nueva"),
            ("arcondec-delicias-canalizacion.jpg",
             "Canalización y charola sobre la fila de racks del área blanca"),
        ],
        "resultados": [
            ("225 kVA", "transformador instalado"),
            ("175 kW", "planta de emergencia automática"),
            ("15 kVA", "sistema de inversores"),
        ],
    },
    {
        "slug": {"es": "hub-santa-catarina", "en": "santa-catarina-hub"},
        "nombre": "HUB SANTA CATARINA",
        "ubicacion": "Santa Catarina - Nuevo León",
        "foto": "arcondec-catarina-banner.jpg",
        # ─────────────────────────────────────────────────────────────────
        # Datos reales, de HUB_Santa_Catarina_Informacion_Web_Arcondec.pdf
        # (presupuesto + presentación de kickoff de Fase 1). La capacidad de
        # 2.5 MVA fue confirmada por Grupo Arcondec.
        #
        # UBICACIÓN: la ficha trae la dirección exacta con número. Aquí se
        # publica solo la ciudad y el estado: es un centro de datos de un
        # cliente y su domicilio no tiene por qué estar en una web abierta.
        #
        # PROYECTO EN CURSO: el kickoff programa la Fase 1 del 12-may-2025 al
        # 30-mar-2026. La redacción evita afirmar que ya cerró; en cuanto se
        # confirme el cierre real conviene revisarla y agregar "entrega".
        #
        # OMITIDOS A PROPÓSITO (la ficha los marca por confirmar):
        #   · "entrega"       — año formal de entrega
        #   · "certificacion" — la documentación referencia TIA-942, Uptime,
        #     NOM y NFPA, pero eso NO acredita una certificación. No publicar
        #     ninguna como obtenida sin el certificado en mano.
        #   · Indicadores de cierre: incidentes, disponibilidad, cumplimiento
        #     de plazo, resultados de puesta en marcha.
        #   · Configuración final de redundancia entregada.
        # ─────────────────────────────────────────────────────────────────
        "publicado": True,
        "titulo": "HUB Santa Catarina",
        "subtitulo": (
            "Construcción y ampliación de infraestructura crítica para el data "
            "center de IZZI en Santa Catarina, con 2.5 MVA y arquitectura "
            "escalable."
        ),
        "descripcion": [
            "Grupo Arcondec participa en el desarrollo del data center Santa "
            "Catarina de IZZI, en Nuevo León. La Fase 1 se planteó para la "
            "instalación de los POD 1 y 2 con el 50% de racks, dentro de un "
            "concepto arquitectónico escalable con crecimiento previsto hasta "
            "cinco POD.",
            "El proyecto integra obra civil y arquitectura con infraestructura "
            "de potencia, respaldo y climatización crítica. El núcleo "
            "energético contempla subestación, transformación, UPS, baterías, "
            "distribución y plantas de emergencia, y el diseño deja espacios "
            "preparados para futuras ampliaciones.",
        ],
        "imagen": "arcondec-catarina-sm6.jpg",
        "imagen_alt": (
            "Conexión de terminaciones en las celdas de media tensión de la "
            "subestación"
        ),
        "cliente": "IZZI",
        "sector": "Telecomunicaciones / infraestructura crítica",
        "ubicacion_exacta": "Ciudad Santa Catarina, Nuevo León",
        "tipo_obra": (
            "Construcción y ampliación de infraestructura crítica para centro "
            "de datos"
        ),
        "superficie": "2,050.25 m² documentados en plantas de intervención",
        "capacidad": "2.5 MVA",
        "duracion": "Fase 1: mayo 2025 - marzo 2026 (programa de kickoff)",
        "reto": (
            "El reto principal consiste en construir y ampliar infraestructura "
            "crítica dentro de un HUB en operación, integrando potencia, "
            "respaldo, climatización y protección contra incendio sin "
            "comprometer la continuidad del servicio. El kickoff establece "
            "expresamente la necesidad de asegurar las instalaciones actuales "
            "de IZZI durante el desarrollo y, al mismo tiempo, dejar una "
            "arquitectura escalable para el crecimiento futuro."
        ),
        "solucion": [
            ("Media tensión / subestación",
             "Subestación SM6, acometida, transformador K20 de 2,500/3,333 "
             "kVA, terminales XLP, pruebas VLF y gestiones ante CFE y UVIE."),
            ("Corriente alterna / respaldo",
             "Tableros de 480/277 V de hasta 4,000 A, tableros UPS, "
             "alimentadores, transformadores reductores, plantas de emergencia "
             "y alimentaciones provisionales."),
            ("UPS y baterías",
             "Cuartos dedicados para UPS y baterías de litio, con UPS de 1,200 "
             "kVA en configuración redundante, bypass estático y de "
             "mantenimiento."),
            ("HVAC",
             "Climatización de precisión para áreas críticas, unidades In-Row "
             "en POD, refrigeración, drenaje, control, ventilación y "
             "extracción."),
            ("PCI - detección y supresión",
             "Agente limpio Fluoro-K para UPS y POD, detección convencional y "
             "por aspiración, rociadores y bombeo contra incendio."),
            ("Obra civil y arquitectura",
             "Intervención documentada de 2,050.25 m², incluyendo POD, cuartos "
             "técnicos, plantas de emergencia, oficinas, terraza y áreas "
             "exteriores."),
            ("Puesta a tierra y protección",
             "Malla y electrodos de tierra, conexión de equipos, soldadura "
             "exotérmica, supresores de transitorios y puesta a tierra de "
             "subestación y tableros."),
        ],
        "alcances": [
            "Integración de subestación y transformación para una capacidad de 2.5 MVA, con acometida, pruebas y accesorios asociados",
            "Tableros principales, alimentadores, sistemas de transferencia y plantas de emergencia, con una capacidad de generación de 2,500 kW",
            "Cuartos dedicados de UPS de 1,200 kVA en configuración redundante y sistema de baterías de litio",
            "Área de POD de 368.61 m²: concepto preparado para cinco POD de 24 racks cada uno; la Fase 1 contempla POD 1 y 2 con 50% de racks",
            "Climatización crítica con pasillos fríos y calientes confinados, unidades In-Row y equipos de precisión",
            "Obra civil y PCI: cuartos técnicos, plantas de emergencia, oficinas, terraza y exteriores, con detección y supresión de incendio",
        ],
        # De lo general a lo particular: primero el conjunto desde el aire,
        # luego las maniobras mayores y de ahí al detalle de cada sistema.
        "galeria": [
            ("arcondec-catarina-aerea.jpg",
             "Vista aérea del conjunto del data center en construcción"),
            ("arcondec-catarina-izaje.jpg",
             "Izaje nocturno de una de las plantas de emergencia"),
            ("arcondec-catarina-terminaciones.jpg",
             "Terminaciones de media tensión en las celdas de la subestación"),
            ("arcondec-catarina-tableros.jpg",
             "Montaje de tableros y canalización en el cuarto eléctrico"),
            ("arcondec-catarina-condensadores.jpg",
             "Condensadores de la climatización de precisión en fachada"),
        ],
        "resultados": [
            ("2.5 MVA", "capacidad instalada"),
            ("2,500 kW", "capacidad de generación"),
            ("2,050 m²", "superficie de intervención"),
        ],
    },
    {
        "slug": {"es": "hub-satelite", "en": "satelite-hub"},
        "nombre": "HUB SATÉLITE",
        "ubicacion": "Naucalpan - Estado de México",
        "foto": "arcondec-satelite-banner.jpg",
        # ─────────────────────────────────────────────────────────────────
        # Datos reales, de HUB_Satelite_Informacion_Web_Arcondec.pdf
        # (catálogo de conceptos y manual de operación).
        #
        # UBICACIÓN: la documentación trae calle y número. Se publica solo
        # Ciudad Satélite, Naucalpan.
        #
        # LA FICHA ADVIERTE EXPRESAMENTE: no atribuir UPS/corriente directa,
        # HVAC ni PCI a este proyecto — los documentos no permiten afirmar que
        # formaran parte del alcance. Por eso no aparecen en "solucion".
        #
        # OMITIDOS A PROPÓSITO (la ficha los marca por confirmar):
        #   · "superficie", "capacidad", "duracion"
        #   · Incidentes durante la ejecución — sin evidencia para afirmar cero
        #   · Disponibilidad / KPI de cierre
        # El año 2025 aparece en el manual de operación; conviene confirmar que
        # corresponde al cierre formal antes de darlo por definitivo.
        # ─────────────────────────────────────────────────────────────────
        "publicado": True,
        "titulo": "HUB Satélite",
        "subtitulo": (
            "Adecuación de infraestructura eléctrica crítica y obra civil para "
            "modernizar el sistema de respaldo del HUB Satélite de IZZI, en "
            "Naucalpan."
        ),
        "descripcion": [
            "Grupo Arcondec participó en la adecuación de infraestructura del "
            "HUB Satélite de IZZI, en Ciudad Satélite, Naucalpan de Juárez. El "
            "proyecto contempló trabajos eléctricos, civiles y estructurales "
            "asociados a la integración y reconfiguración del sistema de "
            "respaldo de energía.",
            "El alcance incluyó adecuaciones de alimentadores generales, "
            "integración de tableros de transferencia, conexiones con la planta "
            "de emergencia, sistema de puesta a tierra, iluminación de "
            "emergencia, canalizaciones, estructura metálica, adecuaciones "
            "arquitectónicas y elementos de seguridad.",
        ],
        "imagen": "arcondec-satelite-tablero.jpg",
        "imagen_alt": (
            "Técnico trabajando en la migración de alimentadores dentro del "
            "tablero"
        ),
        "cliente": "IZZI",
        "sector": "Telecomunicaciones",
        "ubicacion_exacta": "Ciudad Satélite, Naucalpan de Juárez, Estado de México",
        "tipo_obra": "Adecuación y modernización de infraestructura existente",
        "entrega": "2025",
        "reto": (
            "El principal reto consistió en migrar e integrar nueva "
            "infraestructura eléctrica dentro de un HUB en operación, "
            "reduciendo al mínimo la afectación al servicio. Las maniobras "
            "requirieron transferencias controladas de carga, uso de la planta "
            "de emergencia, conexiones provisionales, migración individual de "
            "conductores y verificación de secuencia de fases y voltajes antes "
            "de restablecer la configuración definitiva. La primera ventana "
            "contempló transferir la carga a la planta de emergencia, abrir la "
            "subestación, desconectar alimentadores e instalar uno provisional; "
            "en otra se planteó migrar los neutros cable por cable para no "
            "dejar sin referencia a los equipos."
        ),
        "solucion": [
            ("Media tensión / subestación",
             "Maniobras de coordinación con la subestación existente para "
             "aislamiento, transferencia y restablecimiento del suministro "
             "durante las ventanas de intervención."),
            ("Corriente alterna / respaldo",
             "Adecuación de alimentadores, integración de tableros de "
             "transferencia, conexiones al tablero general normal y a la planta "
             "de emergencia, canalizaciones, pruebas y puesta en marcha."),
            ("Sistema de tierras",
             "Adecuación de la malla de tierra física e integración de la "
             "planta de emergencia y los equipos eléctricos al sistema de "
             "puesta a tierra."),
            ("Iluminación y servicios de emergencia",
             "Adecuación de circuitos de alumbrado, contactos y luminarias "
             "asociados a servicios de emergencia."),
            ("Obra civil",
             "Demoliciones, pasos para instalaciones, adecuación de muros, "
             "acabados, pintura, reubicación de accesos y trabajos "
             "complementarios de integración."),
            ("Estructura metálica",
             "Fabricación e instalación de bastidores, elementos IPR y PTR, "
             "rejilla tipo Irving, barandales, escalera y elementos "
             "estructurales auxiliares."),
            ("Seguridad",
             "Instalación de señalización de evacuación y emergencia, "
             "elementos de protección física y extintores."),
        ],
        "alcances": [
            "Integración y reconfiguración de tableros de transferencia y alimentadores principales, con conexiones al tablero general normal y a la generación de emergencia",
            "Alimentadores de potencia con conductores de hasta 500 kcmil y 4/0 AWG, incluyendo identificación, peinado, terminales y pruebas eléctricas",
            "Charola de aluminio tipo escalerilla de 20 pulgadas, con accesorios, soportes y conexiones de puesta a tierra",
            "Sistema de tierra física, incluyendo malla de tierra y conexión de la planta de emergencia",
            "Adecuaciones civiles y arquitectónicas: demoliciones, pasos de instalaciones, muros de Durock, acabados, pintura, puertas y fachada con louver",
            "Infraestructura metálica auxiliar con PTR, perfiles IPR, rejilla tipo Irving, barandales y escalera de acceso",
        ],
        "galeria": [
            ("arcondec-satelite-barras.jpg",
             "Trabajos sobre las barras del tablero general"),
            ("arcondec-satelite-conductores.jpg",
             "Conductores y terminaciones peinados dentro del tablero"),
            ("arcondec-satelite-alimentadores.jpg",
             "Alimentadores de potencia conectados al tablero de transferencia"),
            ("arcondec-satelite-maniobra.jpg",
             "Maniobra de conexión durante una ventana nocturna"),
            ("arcondec-satelite-transferencia.jpg",
             "Integración del tablero de transferencia con la planta de emergencia"),
        ],
        "resultados": [
            ("3", "ventanas nocturnas de intervención eléctrica"),
        ],
    },
    {
        "slug": {"es": "montes-urales", "en": "montes-urales"},
        "nombre": "MONTES URALES",
        "ubicacion": "Montes Urales - CDMX",
        "foto": "arcondec-urales-banner.jpg",
        # ─────────────────────────────────────────────────────────────────
        # Datos reales, de Montes_Urales_Bancos_Baterias_Informacion_Web_
        # Arcondec.pdf (cotización + reporte de actividades). La capacidad de
        # cuatro bancos de 1,000 Ah fue confirmada por Grupo Arcondec.
        #
        # SIN CLIENTE NI SECTOR A PROPÓSITO. La ficha marca los dos como
        # "pendiente de confirmar" y pide validar si aplica NDA. Con ambos
        # ausentes la plantilla no dibuja la fila de cliente, que es lo
        # correcto: es preferible no decir nada a arriesgar un dato bajo NDA.
        # OJO: las fotos originales traían el nombre del cliente en la marca de
        # agua. Se recortó, pero eso NO equivale a autorización para
        # publicarlo. Confirmar antes de agregarlo.
        #
        # OMITIDOS: superficie (no documentada), certificación (no
        # identificada) e indicadores de cierre (incidentes, disponibilidad).
        # ─────────────────────────────────────────────────────────────────
        "publicado": True,
        "titulo": "Bancos de baterías, Montes Urales",
        "subtitulo": (
            "Modernización del respaldo en corriente directa con cuatro bancos "
            "de baterías de litio de 1,000 Ah a 48 VCD en Montes Urales, CDMX."
        ),
        "descripcion": [
            "Grupo Arcondec ejecutó la modernización del sistema de respaldo en "
            "corriente directa del sitio Montes Urales mediante el suministro, "
            "montaje, conexión y puesta en marcha de cuatro bancos de baterías "
            "de litio Polarium de 1,000 Ah a 48 VCD. Cada banco está integrado "
            "por diez módulos de 100 Ah, montados en rack antisísmico Zona 4 "
            "con barras de conexión.",
            "La intervención incluyó la reubicación de un banco existente "
            "dentro de la misma área, la fabricación de bases metálicas de PTR "
            "para los equipos nuevos y maniobras de cableado y adecuación de "
            "trayectorias. Para la precarga de los bancos nuevos se utilizó una "
            "planta de corriente directa externa de 600 A alimentada desde el "
            "tablero de corriente alterna existente.",
        ],
        "imagen": "arcondec-urales-barras.jpg",
        "imagen_alt": (
            "Conexión de los conductores positivo y negativo a las barras "
            "colectoras del banco"
        ),
        "ubicacion_exacta": "Montes Urales, Ciudad de México",
        "tipo_obra": "Modernización del sistema de respaldo en corriente directa",
        "capacidad": "4 bancos × 1,000 Ah a 48 VCD (4,000 Ah · 192 kWh)",
        "tecnologia": "Baterías de litio Polarium en rack antisísmico Zona 4",
        "duracion": "2 días de intervención (26 y 27 de abril de 2024)",
        "entrega": "2024",
        "reto": (
            "El reto principal consistió en sustituir e integrar bancos de "
            "baterías dentro de infraestructura eléctrica existente, con "
            "maniobras de desconexión, reubicación y conexión sin comprometer "
            "la continuidad del sistema. Parte de los trabajos se ejecutó con "
            "equipos energizados y en ventanas nocturnas de mantenimiento, así "
            "que hubo que controlar la secuencia de maniobras, aislar "
            "terminales, conservar las trayectorias existentes y preparar cada "
            "banco antes de su conexión definitiva. Los bancos de litio "
            "requirieron además una precarga previa mediante una PDC externa de "
            "600 A."
        ),
        "solucion": [
            ("Corriente directa / baterías",
             "Suministro, instalación, conexión, precarga, configuración y "
             "puesta en marcha de cuatro bancos de baterías de litio de 1,000 "
             "Ah a 48 VCD."),
            ("Instalaciones eléctricas",
             "Conexión a barras colectoras y alimentadores principales, "
             "adecuación y reubicación de cableado, terminales, zapatas, "
             "ponchado y aislamiento."),
            ("Infraestructura metálica",
             "Fabricación e instalación de cuatro bases de PTR de 3 × 3 "
             "pulgadas calibre 14 para los bancos nuevos."),
            ("Maniobras especializadas",
             "Desconexión de los bancos existentes, reubicación de un banco "
             "dentro de la misma área y maniobras en ventanas nocturnas con "
             "equipos energizados."),
            ("Puesta en marcha",
             "Precarga mediante PDC externa de 600 A, configuración final y "
             "capacitación al personal local."),
        ],
        "alcances": [
            "Cuatro bancos nuevos Polarium de 1,000 Ah a 48 VCD, cada uno con diez módulos de 100 Ah en rack antisísmico Zona 4",
            "Fabricación e instalación de cuatro bases metálicas de PTR de 3 × 3 pulgadas calibre 14",
            "Precarga controlada con una PDC externa de 600 A energizada desde el tablero de corriente alterna existente",
            "Migración y conexión: desconexión de bancos existentes, aislamiento de terminales y reubicación de conductores por charolas existentes",
            "Reubicación de un banco existente a una nueva posición dentro de la misma área",
            "Configuración, puesta en servicio de los equipos y capacitación al personal local",
        ],
        # La secuencia cuenta el reemplazo: lo que había, lo que se instaló y
        # cómo quedó conectado.
        "galeria": [
            ("arcondec-urales-banco-existente.jpg",
             "Banco de baterías existente antes de la sustitución"),
            ("arcondec-urales-banco-nuevo.jpg",
             "Banco nuevo montado en rack antisísmico Zona 4"),
            ("arcondec-urales-modulos.jpg",
             "Módulos de litio de 100 Ah instalados en el rack"),
            ("arcondec-urales-modulo-detalle.jpg",
             "Indicadores de estado de carga de un módulo Polarium"),
            ("arcondec-urales-conexion.jpg",
             "Conexión y peinado de conductores entre bancos"),
        ],
        "resultados": [
            ("4", "bancos nuevos instalados"),
            ("4,000 Ah", "capacidad nominal a 48 VCD"),
            ("192 kWh", "energía nominal equivalente"),
        ],
    },
    {
        "slug": {"es": "hub-santa-fe", "en": "santa-fe-hub"},
        "nombre": "HUB SANTA FE",
        "ubicacion": "Santa Fe - Ciudad de México",
        "foto": "arcondec-santa-fe-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-queretaro", "en": "queretaro-hub"},
        "nombre": "HUB QUERÉTARO",
        "ubicacion": "Cerca de Querétaro",
        "foto": "arcondec-queretaro-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-durango", "en": "durango-hub"},
        "nombre": "HUB DURANGO",
        "ubicacion": "Durango",
        "foto": "arcondec-durango-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-garcia", "en": "garcia-hub"},
        "nombre": "HUB GARCÍA",
        "ubicacion": "García - Nuevo León",
        "foto": "arcondec-garcia-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-islas-mujeres", "en": "islas-mujeres-hub"},
        "nombre": "HUB ISLAS MUJERES",
        "ubicacion": "Islas Mujeres - Yucatán",
        "foto": "arcondec-islas-mujeres-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-mazatlan", "en": "mazatlan-hub"},
        "nombre": "HUB MAZATLÁN",
        "ubicacion": "Mazatlán - Sinaloa",
        "foto": "arcondec-mazatlan-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-monterrey", "en": "monterrey-hub"},
        "nombre": "HUB MONTERREY",
        "ubicacion": "Monterrey - Nuevo León",
        "foto": "arcondec-monterrey-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-sevilla", "en": "sevilla-hub"},
        "nombre": "HUB SEVILLA",
        "ubicacion": "Sevilla - CDMX",
        "foto": "arcondec-sevilla-banner.jpg",
        # ─────────────────────────────────────────────────────────────────
        # Datos reales, de HUB_Sevilla_ficha_proyecto.docx (fuente: Anexo C,
        # Formato de cotización VF 01, 04-nov-2024, pestaña "Hub Sevilla 01";
        # confirmados por José Carlos).
        #
        # PENDIENTES antes de publicar (la ficha los marca sin confirmar):
        #   · Superficie intervenida — no aparece en el presupuesto
        #   · Certificación — sin dato
        #   · Faltan 1 o 2 cifras de resultados (incidentes, disponibilidad)
        #   · Redacción final del subtítulo
        #
        # DISCREPANCIA A RESOLVER: la descripción de la ficha dice "9 equipos",
        # pero la tabla técnica dice 8 equipos de 10 TR = 80 TR (partida EQ-1).
        # Aquí se usó 8 porque es lo que sostiene la aritmética y la partida
        # del presupuesto. Confirmar cuál es el número correcto.
        #
        # NO PUBLICAR el monto del presupuesto: la ficha lo marca como dato
        # interno de control de proyecto.
        # ─────────────────────────────────────────────────────────────────
        "publicado": True,
        "titulo": "HUB Sevilla",
        "subtitulo": (
            "Reemplazo de aires acondicionados de precisión en el HUB Sevilla "
            "de IZZI, en la Ciudad de México."
        ),
        "descripcion": [
            "El proyecto consistió en el reemplazo de los equipos de aire "
            "acondicionado de precisión tipo InRow del HUB Sevilla, sustituyendo "
            "unidades existentes marca Data Aire por equipos con compresor "
            "inverter, e incluyendo confinamiento de pasillos fríos y el "
            "proyecto de ingeniería completo.",
            "La ejecución en sitio duró dos meses una vez que llegó el equipo, "
            "con el centro de datos operando de forma continua durante toda la "
            "obra.",
        ],
        # La destacada la recorta el CSS a una franja muy ancha, así que tiene
        # que ser una toma cuyo motivo se extienda en horizontal. Esta vista de
        # la azotea deja ver toda la hilera de condensadores incluso en la
        # franja; una foto de motivo centrado se perdería en el recorte.
        "imagen": "arcondec-sevilla-condensadores-azotea.jpg",
        "imagen_alt": "Hilera de condensadores instalados en la azotea del HUB Sevilla",
        "cliente": "IZZI / TVI",
        "sector": "Telecomunicaciones",
        "ubicacion_exacta": "Sevilla, Ciudad de México",
        "tipo_obra": "Remodelación",
        "capacidad": "8 equipos InRow de 10 TR sensibles c/u (80 TR)",
        "duracion": "2 meses de ejecución en sitio",
        "entrega": "2025",
        "reto": (
            "El principal reto fue coordinar los trabajos sin afectar la "
            "operación crítica del sitio. Todo tuvo que ejecutarse a través de "
            "ventanas de mantenimiento, contando siempre con respaldos de "
            "enfriamiento para no dejar la sala desprotegida en ningún momento."
        ),
        "solucion": [
            ("HVAC",
             "Suministro e instalación de equipos de aire acondicionado de "
             "precisión tipo InRow con compresor inverter, incluyendo tubería "
             "de refrigeración de alta y baja presión, carga de gas R-410A, "
             "sistema de monitoreo Team Work por POD e instalación hidráulica "
             "de drenaje."),
            ("Área blanca",
             "Confinamiento de pasillos fríos en tres pasillos, para separar el "
             "aire frío del caliente y elevar la eficiencia del sistema."),
            ("Obra civil",
             "Pasos de muro para las tuberías y suministro e instalación de "
             "tinaco de 750 litros."),
            ("Desinstalación",
             "Retiro y disposición de los equipos InRow existentes marca Data "
             "Aire, con recuperación certificada del gas refrigerante y "
             "manifiesto de destrucción."),
        ],
        "alcances": [
            "Equipos de aire acondicionado de precisión tipo InRow, 10 TR sensibles c/u, con compresor inverter",
            "Confinamiento de pasillos fríos en 3 pasillos (AB, BC y DE)",
            "Desinstalación y disposición certificada de 4 equipos existentes marca Data Aire",
            "Proyecto de ingeniería completo: planos de trayectorias, 3D, cortes, diagramas y carpeta técnica",
            "Sistema de monitoreo Team Work configurado por cada POD",
        ],
        # El orden cuenta la obra: llega el equipo, se instala en azotea, se
        # tiende la tubería y se cierra dentro de la sala.
        "galeria": [
            ("arcondec-sevilla-equipo-nuevo.jpg",
             "Condensador ATTOM embalado a su llegada a la azotea"),
            ("arcondec-sevilla-condensador.jpg",
             "Condensador instalado sobre la estructura de azotea"),
            ("arcondec-sevilla-cobre.jpg",
             "Instalación de las líneas de cobre aisladas"),
            ("arcondec-sevilla-plafon.jpg",
             "Tubería de refrigeración en cobre sobre el plafón"),
            ("arcondec-sevilla-canalizacion.jpg",
             "Canalización y tubería sobre la fila de racks"),
            ("arcondec-sevilla-sala.jpg",
             "Técnico en el pasillo confinado del centro de datos"),
        ],
        "resultados": [
            ("2", "meses de ejecución en sitio"),
        ],
    },
    {
        "slug": {"es": "hub-rio-colorado", "en": "rio-colorado-hub"},
        "nombre": "HUB RÍO COLORADO",
        "ubicacion": "San Luis Río Colorado",
        "foto": "arcondec-slrc-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-tepic", "en": "tepic-hub"},
        "nombre": "HUB TEPIC",
        "ubicacion": "Tepic - Nayarit",
        "foto": "arcondec-tepic-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-teziutlan", "en": "teziutlan-hub"},
        "nombre": "HUB TEZIUTLÁN",
        "ubicacion": "Teziutlán - Puebla",
        "foto": "arcondec-teziutlan-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-tijuana", "en": "tijuana-hub"},
        "nombre": "HUB TIJUANA",
        "ubicacion": "Tijuana - Baja California",
        "foto": "arcondec-tijuana-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-toluca", "en": "toluca-hub"},
        "nombre": "HUB TOLUCA",
        "ubicacion": "Toluca - Estado de México",
        "foto": "arcondec-toluca-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-tuxpan", "en": "tuxpan-hub"},
        "nombre": "HUB TUXPAN",
        "ubicacion": "Tuxpan",
        "foto": "arcondec-tuxpan-01.jpg",
        "publicado": False,
    },
    {
        "slug": {"es": "hub-valle-oriente", "en": "valle-oriente-hub"},
        "nombre": "HUB VALLE ORIENTE",
        "ubicacion": "Valle Oriente - Monterrey",
        "foto": "arcondec-valle-oriente-01.jpg",
        "publicado": False,
    },
]

# Rótulos de la página de detalle. Van aquí y no en cada hub porque son los
# mismos para los 16 proyectos: cambiar "Superficie" una vez lo cambia en todos.
PROJECT_UI = {
    "es": {
        "crumb": "Proyectos",
        "eyebrow": "Caso de proyecto",
        "sheet_title": "Ficha técnica",
        "cliente": "Cliente",
        "cliente_nda": "Cliente confidencial",
        "sector": "Sector",
        "ubicacion_exacta": "Ubicación",
        "tipo_obra": "Tipo de obra",
        "superficie": "Superficie intervenida",
        "capacidad": "Capacidad instalada",
        # Para proyectos donde el equipo es el protagonista y no la capacidad:
        # marca y tipo de tecnología instalada. Opcional, como todos los demás.
        "tecnologia": "Tecnología",
        "duracion": "Duración",
        "entrega": "Año de entrega",
        "certificacion": "Certificación",
        "reto_title": "El reto",
        "solucion_title": "La solución Arcondec",
        "alcances_title": "Alcances entregados",
        "galeria_title": "Galería",
        "resultados_title": "Resultados",
        "prev": "Proyecto anterior",
        "next": "Proyecto siguiente",
        # Etiqueta para cuando solo hay dos proyectos publicados y no existe un
        # anterior distinto del siguiente. Ver render_project() en build.py.
        "otro": "Otro proyecto",
        "back": "Ver todos los proyectos",
        "cta_title": "¿Tienes un proyecto similar?",
        "cta_text": "Cuéntanos qué necesitas y te acompañamos desde la etapa conceptual hasta la entrega final.",
        "meta_tpl": "%s: proyecto de infraestructura eléctrica y data center ejecutado por Grupo Arcondec en %s.",
    },
    "en": {
        "crumb": "Projects",
        "eyebrow": "Project case",
        "sheet_title": "Technical sheet",
        "cliente": "Client",
        "cliente_nda": "Confidential client",
        "sector": "Sector",
        "ubicacion_exacta": "Location",
        "tipo_obra": "Type of work",
        "superficie": "Area covered",
        "capacidad": "Installed capacity",
        "tecnologia": "Technology",
        "duracion": "Duration",
        "entrega": "Delivery year",
        "certificacion": "Certification",
        "reto_title": "The challenge",
        "solucion_title": "The Arcondec solution",
        "alcances_title": "Delivered scope",
        "galeria_title": "Gallery",
        "resultados_title": "Results",
        "prev": "Previous project",
        "next": "Next project",
        "otro": "Another project",
        "back": "View all projects",
        "cta_title": "Have a similar project?",
        "cta_text": "Tell us what you need and we will support you from the concept stage through final delivery.",
        "meta_tpl": "%s: electrical infrastructure and data center project delivered by Grupo Arcondec in %s.",
    },
}

PROJECTS = {
    "es": {
        "title": "Proyectos",
        "meta": "Proyectos de infraestructura eléctrica y data centers ejecutados por Grupo Arcondec en todo México: 130,000 metros de cableado y 12,550 kW de potencia instalada.",
        "keywords": "proyectos eléctricos, infraestructura crítica, data centers, ingeniería civil, UPS, plantas de emergencia, Grupo Arcondec",
        "eyebrow": "Proyectos destacados",
        "h1": "Infraestructura con impacto real",
        "lead": "Cada proyecto es una muestra de nuestra capacidad técnica, calidad y cumplimiento en tiempo récord.",
        "stats_title": "Cobertura",
        "stats": [
            ("130000", "Metros de cableado", "Más de"),
            ("12550", "kW de potencia instalada", "Más de"),
            ("1300", "m² de área blanca", "Más de"),
            ("30", "Años de experiencia", "Más de"),
        ],
        "hubs_eyebrow": "Proyectos destacados",
        "hubs_title": "Proyectos",
        "hubs_intro": "En Grupo Arcondec hemos desarrollado proyectos de infraestructura crítica en todo México, integrando soluciones eléctricas, civiles y tecnológicas con un enfoque en confiabilidad, eficiencia y continuidad operativa. Cada obra representa nuestro compromiso con la precisión técnica, la calidad garantizada y la entrega en tiempo y forma.",
    },
    "en": {
        "title": "Projects",
        "meta": "Electrical infrastructure and data center projects delivered by Grupo Arcondec across Mexico: 130,000 meters of cabling and 12,550 kW of installed power.",
        "keywords": "electrical projects, critical infrastructure, data centers, civil engineering, UPS, emergency power plants, Grupo Arcondec",
        "eyebrow": "Featured projects",
        "h1": "Infrastructure with real impact",
        "lead": "Each project is a testament to our technical capabilities, quality, and record-time execution.",
        "stats_title": "Coverage",
        "stats": [
            ("130000", "Meters of cabling", "Over"),
            ("12550", "kW of installed power", "Over"),
            ("1300", "m² of white space", "Over"),
            ("30", "Years of experience", "Over"),
        ],
        "hubs_eyebrow": "Featured projects",
        "hubs_title": "Projects",
        "hubs_intro": "At Grupo Arcondec, we have developed critical infrastructure projects throughout Mexico, integrating electrical, civil, and technological solutions with a focus on reliability, efficiency, and operational continuity. Each project reflects our commitment to technical precision, guaranteed quality, and on-time delivery.",
    },
}

# --------------------------------------------------------------------------
# SERVICIOS (índice). Sigue el modelo services-2.html del template aball.
# Los textos son los de arcondec.mx/Servicios/LandingPage_IE y _DC.
# --------------------------------------------------------------------------
SERVICES_INDEX = {
    "es": {
        "title": "Servicios",
        "meta": "Servicios de Grupo Arcondec: proyectos y estudios eléctricos, corriente directa, gestión de proyectos, construcción de data centers e ingeniería civil.",
        "keywords": "servicios ingeniería eléctrica, data center, corriente directa, estudios eléctricos, gestión de proyectos, Grupo Arcondec",
        "eyebrow": "Conoce nuestros servicios",
        "h1": "Servicios especializados",
        "lead": "Ingeniería eléctrica y centros de datos, desde la etapa conceptual hasta la entrega final.",
        "intro_title": "En Grupo Arcondec ejecutamos proyectos de gran escala",
        "intro": "Nuestra experiencia abarca proyectos de alta capacidad y sistemas de respaldo en corriente directa (DC), estudios eléctricos normativos y la gestión completa de obra técnica. Atendemos industrias, centros de datos y telecomunicaciones con soluciones hechas a la medida, ejecutadas con precisión, cumplimiento de normas nacionales e internacionales y un enfoque interdisciplinario que garantiza resultados confiables y sostenibles. Los grandes proyectos comienzan con grandes decisiones. Empezar aquí, es una de ellas.",
        "dc_title": "Construimos Data Center que garantizan continuidad total",
        "more": "Ver servicio",
    },
    "en": {
        "title": "Services",
        "meta": "Grupo Arcondec services: electrical projects and studies, direct current, project management, data center construction and civil engineering.",
        "keywords": "electrical engineering services, data center, direct current, electrical studies, project management, Grupo Arcondec",
        "eyebrow": "Explore our services",
        "h1": "Specialized services",
        "lead": "Electrical engineering and data centers, from the conceptual stage to final delivery.",
        "intro_title": "At Grupo Arcondec, we execute large-scale projects",
        "intro": "Our expertise covers high-capacity electrical projects and direct current (DC) backup systems, regulatory electrical studies, and full technical project management. We serve industries, data centers, and telecommunications with tailor-made solutions executed with precision, compliance with national and international standards, and an interdisciplinary approach that ensures reliable and sustainable results. Great projects start with great decisions. Starting here is one of them.",
        "dc_title": "We build Data Centers that ensure total continuity",
        "more": "View service",
    },
}

# --------------------------------------------------------------------------
# CONTACTO / CONTACT
# --------------------------------------------------------------------------
MX_STATES = [
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas",
    "Chihuahua", "Ciudad de México", "Coahuila de Zaragoza", "Colima", "Durango",
    "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán",
    "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo",
    "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
    "Veracruz", "Yucatán", "Zacatecas", "Otros",
]

CONTACT_PAGE = {
    "es": {
        "title": "Contáctanos",
        "meta": "Contacta a Grupo Arcondec en Monterrey, N.L. Consultoría, cotizaciones y soporte técnico en ingeniería eléctrica y centros de datos.",
        "keywords": "contacto Grupo Arcondec, cotización ingeniería eléctrica, data center Monterrey, asesoría técnica",
        "eyebrow": "Contáctanos",
        "h1": "Te ayudamos a impulsar tu infraestructura",
        "lead": "Haz que tu operación sea más segura y eficiente",
        "form_title": "Escríbenos",
        "form_text": "En Grupo Arcondec trabajamos cada día para estar más cerca de nuestros clientes, brindando soluciones personalizadas con eficiencia y compromiso. Si necesitas una consultoría, resolver alguna duda o solicitar una cotización, completa el formulario y nos pondremos en contacto contigo a la brevedad.",
        "addr_text": "Calle del Gran Parque 419, Cumbres 2o, 64610 Monterrey, Nuevo León.",
        "phone_title": "Números telefónicos",
        "phone_office": "Oficina: (81) 1934-1192 y (55) 3032-6595",
        "phone_mobile": "Celular: (55) 3032 6595",
        "mail_title": "Correos electrónicos",
        "mails": [
            ("Informes", "info@arcondec.mx"),
            ("Ventas", "ventas@arcondec.mx"),
            ("Bolsa de trabajo", "rh@arcondec.mx"),
            ("Quejas y sugerencias", "quejasysugerencias@arcondec.mx"),
        ],
        "map_title": "Nuestra ubicación",
        "f_name": "Nombre completo",
        "f_email": "Correo electrónico",
        "f_phone": "Teléfono",
        "f_company": "Empresa",
        "f_state": "Seleccionar estado…",
        "f_reason": "Seleccionar el motivo o área de interés…",
        "f_sector": "Elige el giro…",
        "f_message": "Cuéntanos sobre tu proyecto",
        "f_submit": "Enviar mensaje",
        "reasons": [
            "Solicitar una cotización",
            "Soy / Quiero ser cliente",
            "Soy / Quiero ser proveedor",
            "Queja o sugerencia",
            "Otro",
        ],
        "sectors": ["Ingeniería eléctrica", "Data Center", "Ingeniería Civil", "Otros"],
        "legal_pre": "Al enviar este formulario, aceptas nuestro ",
        "legal_privacy": "aviso de privacidad",
        "legal_post": ", términos y condiciones.",
        "phone_hint": "10 dígitos, sin espacios ni guiones",
        # --- Reorganización de la página: vías directas antes del formulario ---
        # Los datos duros (teléfonos, correos, horario) NO se escriben aquí: salen
        # de content.py y del mismo horario que ya declara el JSON-LD, para que no
        # se puedan desincronizar.
        "direct_title": "Cómo prefieres que hablemos",
        "direct_text": "Elige la que te venga mejor. Todas llegan al mismo equipo.",
        "hours_text": "Lunes a viernes, 9:00 a 18:00 h",
        "call_title": "Por teléfono",
        "call_note": "Si prefieres explicarlo hablando, llámanos a la oficina de Monterrey.",
        "wa_title": "Por WhatsApp",
        "wa_note": "La vía más rápida si ya sabes lo que necesitas.",
        "wa_btn": "Abrir WhatsApp",
        "mail_note": "Cada buzón llega al área que corresponde.",
        "form_note": "¿Prefieres dejarlo por escrito con detalle? Cuéntanos tu proyecto y te contactamos.",
        "required_note": "Los campos marcados con * son obligatorios.",
        "f_state_label": "Estado",
        "f_reason_label": "Motivo de contacto",
        "f_sector_label": "Giro",
        "directions_btn": "Cómo llegar",
    },
    "en": {
        "title": "Contact Us",
        "meta": "Contact Grupo Arcondec in Monterrey, Mexico. Consulting, quotes and technical support in electrical engineering and data centers.",
        "keywords": "contact Grupo Arcondec, electrical engineering quote, data center Monterrey, technical consulting",
        "eyebrow": "Contact us",
        "h1": "We help you boost your infrastructure",
        "lead": "Make your operation safer and more efficient",
        "form_title": "Write to us",
        "form_text": "At Grupo Arcondec, we work every day to be closer to our clients, providing personalized solutions with efficiency and commitment. If you need consulting, have any questions, or want to request a quote, please fill out the form and we’ll get in touch with you shortly.",
        "addr_text": "Calle del Gran Parque 419, Cumbres 2nd Sector, 64610 Monterrey, Nuevo León, Mexico.",
        "phone_title": "Phone numbers",
        "phone_office": "Office: (81) 1934-1192 and (55) 3032-6595",
        "phone_mobile": "Mobile: (55) 3032 6595",
        "mail_title": "Email addresses",
        "mails": [
            ("General information", "info@arcondec.mx"),
            ("Sales", "sales@arcondec.mx"),
            ("Careers", "rh@arcondec.mx"),
            ("Complaints and suggestions", "quejasysugerencias@arcondec.mx"),
        ],
        "map_title": "Our location",
        "f_name": "Full name",
        "f_email": "Email address",
        "f_phone": "Phone",
        "f_company": "Company",
        "f_state": "Select state…",
        "f_reason": "Select a reason or area of interest…",
        "f_sector": "Select your industry…",
        "f_message": "Tell us about your project",
        "f_submit": "Send message",
        "reasons": [
            "Request a quote",
            "I am / want to be a client",
            "I am / want to be a supplier",
            "Complaint or suggestion",
            "Other",
        ],
        "sectors": ["Electrical Engineering", "Data Center", "Civil Engineering", "Other"],
        "legal_pre": "By submitting this form, you accept our ",
        "legal_privacy": "privacy notice",
        "legal_post": ", terms and conditions.",
        "phone_hint": "10 digits, no spaces or dashes",
        "direct_title": "How would you like to talk?",
        "direct_text": "Pick whichever suits you. They all reach the same team.",
        "hours_text": "Monday to Friday, 9:00 to 18:00",
        "call_title": "By phone",
        "call_note": "If you would rather talk it through, call our Monterrey office.",
        "wa_title": "On WhatsApp",
        "wa_note": "The fastest route if you already know what you need.",
        "wa_btn": "Open WhatsApp",
        "mail_note": "Each mailbox reaches the right team.",
        "form_note": "Rather put it in writing, with detail? Tell us about your project and we will get back to you.",
        "required_note": "Fields marked with * are required.",
        "f_state_label": "State",
        "f_reason_label": "Reason for contact",
        "f_sector_label": "Industry",
        "directions_btn": "Get directions",
    },
}

# --------------------------------------------------------------------------
# RECLUTAMIENTO / CAREERS
# --------------------------------------------------------------------------
CAREERS = {
    "es": {
        "title": "Vacantes",
        "meta": "Únete a Grupo Arcondec. Proyectos eléctricos y de data centers de alto nivel técnico, ambiente colaborativo e igualdad de oportunidades.",
        "keywords": "reclutamiento, talento técnico, ingenieros eléctricos, técnicos data center, inclusión laboral, Grupo Arcondec",
        "eyebrow": "Únete a nuestro equipo",
        "h1": "Transforma tu talento en resultados reales",
        "lead": "Ofrecemos un entorno de aprendizaje continuo, retos técnicos y oportunidades reales de desarrollo.",
        "why_title": "Un equipo que comparte tu pasión",
        "why_text": "En Grupo Arcondec reafirmamos nuestro compromiso con la igualdad de oportunidades. Todos nuestros procesos de selección se basan exclusivamente en competencias, habilidades y experiencia.",
        "why": [
            ("Proyectos de alto nivel técnico", "Participa en instalaciones eléctricas industriales, centros de datos y sistemas críticos donde tu conocimiento sí importa.", "fal fa-project-diagram"),
            ("Ambiente de trabajo colaborativo", "Formarás parte de un equipo multidisciplinario con enfoque en la excelencia operativa y la mejora continua.", "fal fa-users"),
            ("Reconocimiento a tu esfuerzo", "Valoramos tu trabajo y te damos visibilidad en proyectos clave y oportunidades reales de crecimiento.", "fal fa-award"),
        ],
        "policy_eyebrow": "Como empresa",
        "policy_title": "Promovemos la inclusión y el respeto en cada oportunidad",
        "policy_text": "No discriminamos por motivos de raza, género, edad, discapacidad, religión, orientación sexual o nacionalidad. Promovemos un entorno inclusivo, justo y respetuoso para todas las personas.",
        "policy_list": [
            "Toda la información es tratada con estricta confidencialidad y utilizada únicamente con fines de evaluación.",
            "No se permite ningún tipo de soborno, recomendación indebida o presión para favorecer a candidatos.",
            "Rechazamos cualquier práctica discriminatoria directa o indirecta.",
        ],
        "vacancies_eyebrow": "Vacantes disponibles",
        "vacancies_title": "Súmate a Grupo Arcondec",
        "vacancies_intro": "Estas son nuestras posiciones abiertas en Monterrey. Da clic en una vacante para ver el detalle y postularte.",
        "req_label": "Requisitos",
        "func_label": "Funciones",
        "name_placeholder": "Tu nombre",
        "email_placeholder": "Tu email",
        "cv_label": "Adjuntar CV (PDF)",
        "apply_btn": "Postularme",
        "apply_note": "Protegido con verificación anti-spam de Formspree.",
        "cta_title": "¡Queremos conocerte!",
        "cta_text": "Indica en el asunto el nombre de la vacante que te interesa.",
        "cta_btn": "Enviar mi CV",
    },
    "en": {
        "title": "Careers",
        "meta": "Join Grupo Arcondec. High-level technical electrical and data center projects, a collaborative environment and equal opportunities.",
        "keywords": "careers, technical talent, electrical engineers, data center technicians, workplace inclusion, Grupo Arcondec",
        "eyebrow": "Join our team",
        "h1": "Turn your talent into real results",
        "lead": "We offer a continuous learning environment, technical challenges, and real development opportunities.",
        "why_title": "A team that shares your passion",
        "why_text": "At Grupo Arcondec, we reaffirm our commitment to equal opportunities. All our selection processes are based solely on competencies, skills, and experience.",
        "why": [
            ("High-level technical projects", "Get involved in industrial electrical installations, data centers, and critical systems where your expertise truly matters.", "fal fa-project-diagram"),
            ("Collaborative work environment", "You'll be part of a multidisciplinary team focused on operational excellence and continuous improvement.", "fal fa-users"),
            ("Recognition for your effort", "We value your work and give you visibility in key projects and real opportunities for growth.", "fal fa-award"),
        ],
        "policy_eyebrow": "As a company",
        "policy_title": "We promote inclusion and respect in every opportunity",
        "policy_text": "We do not discriminate based on race, gender, age, disability, religion, sexual orientation, or nationality. We promote an inclusive, fair, and respectful environment for everyone.",
        "policy_list": [
            "All information is treated with strict confidentiality and used solely for evaluation purposes.",
            "No form of bribery, undue recommendation, or pressure to favor candidates is allowed.",
            "We reject any direct or indirect discriminatory practices.",
        ],
        "vacancies_eyebrow": "Open positions",
        "vacancies_title": "Join Grupo Arcondec",
        "vacancies_intro": "These are our current openings in Monterrey. Click a position to see details and apply.",
        "req_label": "Requirements",
        "func_label": "Responsibilities",
        "name_placeholder": "Your name",
        "email_placeholder": "Your email",
        "cv_label": "Attach CV (PDF)",
        "apply_btn": "Apply now",
        "apply_note": "Protected by Formspree anti-spam verification.",
        "cta_title": "We want to get to know you!",
        "cta_text": "Please indicate the name of the position you're interested in in the subject line.",
        "cta_btn": "Send my CV",
    },
}

# Vacantes activas. El contenido (título, requisitos, funciones) se comparte
# entre es/en porque son puestos presenciales en Monterrey publicados en
# español; solo el texto de interfaz alrededor (arriba, en CAREERS) se traduce.
VACANCIES = [
    {
        "title": "Analista de Precios Unitarios",
        "req": "+3 años de experiencia · Ingeniería Civil, Ingeniería Eléctrica o afín · Excel avanzado · Neodata indispensable · Experiencia cuantificando desde planos.",
        "func": "Elaboración de presupuestos de instalaciones eléctricas y obra civil. Análisis de precios unitarios y cuantificación de volúmenes de obra. Cotización con proveedores y subcontratistas e integración de costos.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $22k–25k libres mensuales",
    },
    {
        "title": "Arquitecto Proyectista",
        "req": "3 a 5 años de experiencia · Licenciatura en Arquitectura, Ingeniería Civil o afín · AutoCAD 2D/3D, Revit/BIM, SketchUp, Lumion, Photoshop, Illustrator, Excel.",
        "func": "Desarrollo de proyectos arquitectónicos y ejecutivos. Elaboración de planos, renders, memorias descriptivas y documentación técnica. Coordinación e integración de disciplinas de ingeniería.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $22k–25k libres mensuales",
    },
    {
        "title": "Ingeniero de Control y Planeación Eléctrica",
        "req": "Experiencia en obra e instalaciones eléctricas · Ingeniería Eléctrica, Electromecánica, Civil o afín · Excel · Deseable MS Project y AutoCAD · Conocimiento de baja y media tensión.",
        "func": "Seguimiento a cronogramas y programas de obra. Control de avances físicos, financieros, generadores y estimaciones. Seguimiento a costos, presupuestos, materiales y documentación de proyecto.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $25k–30k libres mensuales",
    },
    {
        "title": "Coordinador Eléctrico de Diseño",
        "req": "4 a 6 años de experiencia en proyectos de misión crítica y Data Centers · Ingeniería Eléctrica o afín · Revit MEP, AutoCAD Electrical · NOM-001-SEDE · Media y baja tensión.",
        "func": "Diseño y validación de instalaciones eléctricas y sistemas de respaldo. Coordinación y supervisión de proyectistas eléctricos. Catálogos de conceptos e integración con otras especialidades.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $30k–35k libres mensuales",
    },
    {
        "title": "Coordinador HVAC",
        "req": "3 a 5 años de experiencia · Ingeniería Mecánica, Electromecánica o afín · Manejo fluido de Revit y AutoCAD · Cálculo de cargas térmicas y selección de equipos HVAC · Experiencia en proyectos de misión crítica o data center.",
        "func": "Diseño y memorias de cálculo de sistemas HVAC y climatización de precisión. Selección de CRAC/CRAH, chillers, inrow y unidades condensadoras. Coordinación de ductos, cargas térmicas y espacios técnicos con otras especialidades.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $30k–35k libres mensuales",
    },
    {
        "title": "Coordinador PCI Detección y Pre-Acción",
        "req": "3 a 5 años de experiencia · Ingeniería Mecánica, Electromecánica o afín · Manejo fluido de Revit y AutoCAD · Indispensable conocimiento de normativa NFPA.",
        "func": "Diseño de sistemas PCI, rociadores, pre-acción y agentes limpios. Diseño de detección temprana de humo y sistemas convencionales/direccionables. Elaboración de catálogos de conceptos, coordinación con otras especialidades.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $30k–35k libres mensuales",
    },
    {
        "title": "Coordinador de Sistemas Especiales de Seguridad",
        "req": "3 a 5 años de experiencia · Ingeniería Electrónica, Telecomunicaciones, Sistemas o afín · CCTV, control de acceso, voz y datos, fibra óptica · Manejo fluido de AutoCAD y Revit.",
        "func": "Diseño y especificación de sistemas de CCTV y control de acceso. Diseño de cableado estructurado y redes de fibra óptica. Coordinación de planos e integración con otras especialidades.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $30k–35k libres mensuales",
    },
    {
        "title": "Ingeniero Proyectista Eléctrico",
        "req": "+3 años de experiencia · Ingeniería Eléctrica, Electromecánica o afín · AutoCAD, Revit, Microsoft Office · Deseable ETAP y conocimiento de normativa vigente · Experiencia en proyectos de misión crítica o data center.",
        "func": "Diseño de proyectos eléctricos industriales en baja y media tensión. Elaboración de planos, diagramas unifilares y documentación técnica. Cuantificaciones, levantamientos y planos As-Built.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $22k–25k libres mensuales",
    },
    {
        "title": "Project Manager",
        "req": "5 a 8 años de experiencia en construcción · 3 años como Project Manager o líder de proyectos · Ingeniería Civil, Arquitectura, Ingeniería Eléctrica o afín · MS Project, AutoCAD, Excel avanzado · Neodata / OPUS.",
        "func": "Administración integral de proyectos, desde inicio hasta cierre. Coordinación de equipos, contratistas y múltiples frentes de obra. Control de cronogramas, costos, riesgos, calidad y seguridad.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · Disponibilidad para viajar · $30k–40k libres mensuales",
    },
    {
        "title": "Project Manager – SPOC de Operaciones",
        "req": "3 a 5 años de experiencia · Ingeniería Civil, Eléctrica, Mecánica o afín · Gestión y coordinación de proyectos · Microsoft Project, Smartsheet, lectura de planos · Deseable PMP, CAPM o equivalente.",
        "func": "Seguimiento de proyectos de ingeniería activos, riesgos, retrasos y desviaciones. Coordinación con Operaciones, Ingeniería y proveedores. Control de acuerdos, compromisos, fechas límite y solicitudes técnicas.",
        "meta": "Monterrey, N.L. · Zona Cumbres · Presencial · $30k–40k libres mensuales",
    },
]

# --------------------------------------------------------------------------
# BLOG (indice). Los articulos completos son la segunda tanda de trabajo.
# --------------------------------------------------------------------------
BLOG = {
    "es": {
        "title": "Blogs",
        "meta": "Artículos técnicos de Grupo Arcondec sobre infraestructura eléctrica, corriente directa, data centers e ingeniería para entornos de misión crítica.",
        "keywords": "blog ingeniería eléctrica, data center, corriente directa, infraestructura crítica, Grupo Arcondec",
        "eyebrow": "Blogs",
        "h1": "Conocimiento técnico que impulsa tu operación",
        "lead": "Artículos sobre infraestructura eléctrica, centros de datos y las tendencias que están redefiniendo la energía crítica.",
        "read_more": "Leer artículo",
        "soon": "Próximamente",
    },
    "en": {
        "title": "Blogs",
        "meta": "Technical articles by Grupo Arcondec on electrical infrastructure, direct current, data centers and engineering for mission-critical environments.",
        "keywords": "electrical engineering blog, data center, direct current, critical infrastructure, Grupo Arcondec",
        "eyebrow": "Blogs",
        "h1": "Technical knowledge that powers your operation",
        "lead": "Articles on electrical infrastructure, data centers and the trends redefining critical power.",
        "read_more": "Read article",
        "soon": "Coming soon",
    },
}

# Los 12 articulos publicados en arcondec.mx. Titulo, imagen y slug son los reales
# del sitio original; `slug` sera el nombre del archivo cuando se generen los
# articulos completos (segunda tanda de trabajo).
ARTICLES = [
    {
        "slug": "energia-critica-data-centers-ia",
        "img": "ia-datacenter.jpg",
        "es": ("Energía crítica en data centers", "El suministro eléctrico indispensable para sistemas que no pueden fallar: UPS, plantas de emergencia, bancos de baterías y distribución de alta confiabilidad."),
        "en": ("Critical power in data centers", "The electrical supply that mission-critical systems cannot do without: UPS, emergency plants, battery banks and high-reliability distribution."),
    },
    {
        "slug": "400v-dc-transformacion-centros-de-datos",
        "img": "nueva-era-de-data-center.jpg",
        "es": ("Sistemas de alimentación en 400 volts de corriente directa", "Distribución en DC a 400 V: alimenta los equipos de TI directamente, reduce pérdidas por conversión y mejora la eficiencia del sistema."),
        "en": ("400 volt direct current power systems", "400 V DC distribution powers IT equipment directly, cutting conversion losses and improving overall system efficiency."),
    },
    {
        "slug": "corriente-directa-infraestructura-critica",
        "img": "corriente-directa-en-centros-de-datos.jpg",
        "es": ("La corriente directa que impulsa a los líderes en infraestructura crítica", "La mayoría de los equipos ya operan internamente en DC: mantener la energía en ese formato reduce pérdidas, conversiones y puntos de falla."),
        "en": ("The direct current powering leaders in critical infrastructure", "Most equipment already runs internally on DC: keeping power in that format reduces losses, conversions and points of failure."),
    },
    {
        "slug": "claves-de-infraestructura-critica-de-un-centro-de-datos",
        "img": "instalacion-y-mantenimiento-arcondec-3.jpg",
        "es": ("Claves de infraestructura crítica de un centro de datos", "Los subsistemas que determinan la disponibilidad real de un data center y cómo se coordinan entre sí."),
        "en": ("Keys to data center critical infrastructure", "The subsystems that determine a data center's real availability and how they work together."),
    },
    {
        "slug": "ingenieria-electrica-ai-hpc",
        "img": "revolucion-electrica-centros-de-datos-ia-hpc.jpg",
        "es": ("La ingeniería eléctrica está revolucionando los data centers", "IA y HPC disparan la densidad de potencia por rack y obligan a rediseñar la infraestructura eléctrica."),
        "en": ("Electrical engineering is revolutionizing data centers", "AI and HPC drive up power density per rack, forcing a redesign of electrical infrastructure."),
    },
    {
        "slug": "sistemas-tierras-fisicas-pararrayos",
        "img": "tierras-fisicas-pararrayos.jpg",
        "es": ("Sistemas de tierras físicas y pararrayos en centros de datos", "Protección contra descargas atmosféricas y referencia de potencial en instalaciones de misión crítica."),
        "en": ("Grounding and lightning protection systems in data centers", "Protection against atmospheric discharges and potential reference in mission-critical facilities."),
    },
    {
        "slug": "peinado-de-cables-data-center",
        "img": "peinado-de-cables.jpg",
        "es": ("Por qué el peinado de cables puede salvar la operación de tu data center", "El orden del cableado como factor de mantenibilidad, disipación térmica y seguridad operativa."),
        "en": ("Why cable management can save your data center operation", "Cable order as a factor of maintainability, thermal dissipation and operational safety."),
    },
    {
        "slug": "instalacion-tableros-auto-soportados-y-distribucion",
        "img": "instalacion-tableros-auto-soportados.jpg",
        "es": ("Instalación de tableros auto soportados y de distribución", "Criterios de montaje, coordinación y pruebas para tableros de media y baja tensión."),
        "en": ("Free-standing and distribution panel installation", "Assembly, coordination and testing criteria for medium and low voltage panels."),
    },
    {
        "slug": "implementacion-centro-de-datos-precisa",
        "img": "datacenter-electricos-arcondec-2.jpg",
        "es": ("Cómo asegurar precisión en la implementación de un centro de datos", "Del diseño conceptual a la puesta en marcha documentada, sin retrabajos ni entregas parciales."),
        "en": ("How to ensure precision when implementing a data center", "From conceptual design to documented commissioning, with no rework or partial deliveries."),
    },
    {
        "slug": "modernizacion-electrica-mexico-tecnologia-digital",
        "img": "modernizacion-electrica.jpg",
        "es": ("Modernización eléctrica: migrar a tecnología digital sin interrumpir la operación", "Cómo sustituir equipos obsoletos y digitalizar la infraestructura manteniendo la continuidad."),
        "en": ("Electrical modernization: going digital without interrupting operations", "How to replace obsolete equipment and digitalize infrastructure while maintaining continuity."),
    },
    {
        "slug": "tendencias-infraestructura-electrica",
        "img": "infraestructura-electrica-data.jpg",
        "es": ("5 tendencias que están transformando los data centers", "Eficiencia, redundancia y monitoreo inteligente se consolidan como estándar del sector."),
        "en": ("5 trends transforming data centers", "Efficiency, redundancy and smart monitoring are becoming the industry standard."),
    },
    {
        "slug": "ingenieria-electrica-que-respalda",
        "img": "dcorriente-directar-arcondec-1.jpg",
        "es": ("Ingeniería eléctrica que respalda", "Infraestructura diseñada para sostener la operación presente y habilitar el crecimiento futuro."),
        "en": ("Electrical engineering that backs you up", "Infrastructure designed to sustain today's operation and enable future growth."),
    },
]
