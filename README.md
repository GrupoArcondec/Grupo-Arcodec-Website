<div align="center">

# Grupo Arcondec — Sitio corporativo

**Sitio estático bilingüe (ES/EN) de 28 páginas para [Grupo Arcondec](https://arcondec.mx): ingeniería eléctrica y construcción de data centers.**

[![Demo](https://img.shields.io/badge/demo-grupo--arcondec.vercel.app-0a7?style=flat-square)](https://grupo-arcondec.vercel.app)
![HTML5](https://img.shields.io/badge/HTML5-estático-e34f26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-arcondec.css-1572b6?style=flat-square&logo=css3&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-ScrollTrigger%20%2B%20SplitText-88ce02?style=flat-square&logo=greensock&logoColor=black)
![Python](https://img.shields.io/badge/generador-Python%203-3776ab?style=flat-square&logo=python&logoColor=white)
![Vercel](https://img.shields.io/badge/deploy-Vercel-000?style=flat-square&logo=vercel)

</div>

---

Construido sobre el template **aball (index-12)** con la marca, contenido y colores oficiales de Arcondec. Cada idioma tiene **una URL real por página** (nada de conmutadores de JavaScript) y el despliegue no tiene build: Vercel sirve el repositorio tal cual.

> 📖 **Documentación completa de operación y edición:** [MANUAL.md](MANUAL.md) — cómo cambiar textos, imágenes y datos de contacto, cómo publicar, y cómo encargar cambios a una IA sin romper la estructura del proyecto. Reglas para asistentes de IA: [CLAUDE.md](CLAUDE.md).

## Inicio rápido

```bash
# Ver el sitio en local
python3 -m http.server 8080        # → http://localhost:8080

# Regenerar las páginas tras editar contenido
python3 tools/build.py

# Verificar que nada se rompió
python3 tools/check.py
```

## Estructura

```
index.html                    Inicio (ES)          en/index.html         Home (EN)
nosotros.html                                      en/about.html
proyectos.html                                     en/projects.html
contacto.html                                      en/contact.html
trabaja-con-nosotros.html                          en/careers.html
blog.html                                          en/blog.html
servicios/  (7 páginas)                            en/services/  (7 páginas)

assets/       CSS, JS, fuentes e imágenes del template + los de Arcondec
tools/        Generador de las páginas (no se publica)
sitemap.xml   robots.txt      Generados junto con las páginas
```

## Cómo cambiar un texto

Los textos **no se editan en el HTML**: las páginas se regeneran y se sobrescribirían.

1. Edita el texto en `tools/content.py` (servicios y datos de contacto) o en `tools/pages.py` (inicio, nosotros, proyectos, contacto, reclutamiento, blog).
2. Regenera: `python3 tools/build.py`
3. Comprueba: `python3 tools/check.py`

El inicio es un caso aparte: su maquetación vive en `tools/home_source.html` y sus textos ES/EN en `tools/home_i18n.js`. El generador combina ambos para producir `index.html` y `en/index.html`.

## Bilingüe y SEO

Cada página existe en dos URLs reales, lo que permite que Google indexe también la versión en inglés:

- `<link rel="canonical">` propio en cada página.
- `<link rel="alternate" hreflang="es-MX|en|x-default">` enlazando ambas versiones.
- `title`, `meta description` y `keywords` por página y por idioma.
- Open Graph y Twitter Card para cuando se comparte el enlace.
- Datos estructurados JSON-LD: `Organization` en todo el sitio, más `Service` en cada servicio, `ItemList` en proyectos y `LocalBusiness` (con horario y coordenadas) en contacto — la base de lo que leen los motores de IA.
- `sitemap.xml` y `robots.txt` generados automáticamente.

El dominio de producción está en una sola línea: `BASE_URL`, en `tools/layout.py`. Si el sitio se publica en otro dominio, se cambia ahí y se regenera.

## Estilos

`assets/css/style.css` es del template y **no se toca**, para que una actualización del template no pise el trabajo hecho. Todo lo de Arcondec —colores de marca, componentes de las páginas interiores y correcciones de responsividad— está en `assets/css/arcondec.css`.

## Animaciones

El movimiento lo lleva `assets/js/arcondec-motion.js` con **GSAP + ScrollTrigger + SplitText** (`assets/js/vendor/`, sin CDN). Sustituye a WOW.js y a las animaciones del hero del template: les quita la clase `wow` y el atributo `data-animation` antes de que `main.js` los inicialice, de modo que en la página hay un único sistema de animación.

Funciona sin marcar nada en el HTML, apoyándose en el grid de Bootstrap que ya existe:

| Qué                 | Cómo entra                                                            |
| ------------------- | --------------------------------------------------------------------- |
| Titulares grandes   | Línea a línea, subiendo por debajo de una máscara (≥32px, sin etiquetas dentro) |
| Columnas del grid   | Fundido y 32px de subida, escalonadas **por renglón visual**            |
| Fotos de tarjeta    | Zoom de salida de 1.08 a 1, solo donde el contenedor recorta            |
| Fotos de portada    | Cortina con `clip-path`, sobre la `<img>` para no comerse lo que va encima |
| Íconos de servicio  | Rebote corto, 0.2s después de su tarjeta                               |
| Hero                | Línea de tiempo por diapositiva + zoom lento sobre la foto             |
| Fondos fotográficos | Parallax suave (solo los de una capa: los que llevan degradado encima, no) |
| Barra de progreso   | Fija arriba, en el degradado de marca                                  |
| Logos de clientes   | **Solo ≤767px**: cinta continua, cada línea hacia un lado               |

El agrupado **por renglón visual** es lo que hace que funcione igual en cualquier pantalla: una fila del grid con seis tarjetas son dos renglones de tres en escritorio y seis apilados en el móvil, donde mide varias pantallas de alto. Se agrupan por la altura a la que están de verdad, así que cada tarjeta entra cuando de verdad aparece —4 disparos a 1440px, 5 a 991px y 10 a 390px sobre la misma rejilla— sin una sola media query.

La cinta de logos va en **dos capas a propósito**: `arcondec.css` deja la tira en una línea que se arrastra con el dedo —eso funciona sin JavaScript y es lo que ve quien pide movimiento reducido— y el JS la convierte en cinta continua cuando el movimiento está permitido. En los dos casos la sección baja de 1078px a 290px en un móvil de 390px. El montaje y el desmontaje al cruzar los 767px van con listener propio, no con `gsap.matchMedia()`: dejar los clones colgados en escritorio deja la sección en 1271px, peor que el problema original, así que conviene que sea explícito.

Cinco salvaguardas que conviene no perder al tocarlo:

- Si GSAP no carga, el archivo se sale sin hacer nada y las animaciones del template vuelven a funcionar como antes.
- Con `prefers-reduced-motion: reduce` no se registra ninguna animación —ni la propia ni la del template— y la página se queda quieta y visible.
- Nada se oculta hasta que la página termina de cargar **y las fuentes están listas**: partir en líneas antes de que cargue la tipografía deja los cortes donde no son.
- El punto de disparo va con `clamp()` para que en páginas cortas los bloques del final también aparezcan.
- Y como red de última instancia: al tocar fondo de página, cualquier bloque que siga sin haber entrado se muestra sin más. No depende de ningún cálculo de altura.

Para excluir un bloque a mano: `data-arc-motion="off"`.

## Accesibilidad

Contraste corregido a **WCAG AA** con ratio calculado (13 fallos resueltos), respeto a `prefers-reduced-motion` y animaciones que nunca dejan contenido oculto.

## Pendiente

Los 12 artículos del blog están listados en el índice con su título, resumen e imagen, pero marcados como «Próximamente»: las páginas de artículo completo son la siguiente tanda. El contenido ya está inventariado en `tools/pages.py` (`ARTICLES`).

---

<div align="center">

© Grupo Arcondec S.A. de C.V. · Desarrollo [JectCode](https://github.com/Juanescanar23)

</div>
