<div align="center">

# Manual de operación y edición del sitio

### Grupo Arcondec — Sitio corporativo bilingüe

**Documento de entrega técnica**

Versión 1.0 · Agosto 2026 · Elaborado por JectCode

[grupo-arcondec.vercel.app](https://grupo-arcondec.vercel.app) · [github.com/Juanescanar23/Grupo-Arcondec](https://github.com/Juanescanar23/Grupo-Arcondec)

</div>

---

## Índice

1. [Qué es este proyecto](#1-qué-es-este-proyecto)
2. [Las tres reglas de oro](#2-las-tres-reglas-de-oro)
3. [Cómo funciona: arquitectura](#3-cómo-funciona-arquitectura)
4. [Preparar el entorno de trabajo](#4-preparar-el-entorno-de-trabajo)
5. [Recetario de ediciones](#5-recetario-de-ediciones)
   - 5.1 [Cambiar un texto o título de un servicio](#51-cambiar-un-texto-o-título-de-un-servicio)
   - 5.2 [Cambiar textos de las demás páginas interiores](#52-cambiar-textos-de-las-demás-páginas-interiores)
   - 5.3 [Cambiar la página de inicio](#53-cambiar-la-página-de-inicio)
   - 5.4 [Cambiar teléfonos, correos, dirección o redes sociales](#54-cambiar-teléfonos-correos-dirección-o-redes-sociales)
   - 5.5 [Cambiar o agregar una imagen](#55-cambiar-o-agregar-una-imagen)
   - 5.6 [Cambiar el dominio del sitio](#56-cambiar-el-dominio-del-sitio)
   - 5.7 [Publicar los artículos del blog](#57-publicar-los-artículos-del-blog)
6. [Verificar y publicar](#6-verificar-y-publicar)
7. [Cómo pedirle los cambios a una IA](#7-cómo-pedirle-los-cambios-a-una-ia)
8. [Lo que nunca se debe hacer](#8-lo-que-nunca-se-debe-hacer)
9. [Solución de problemas](#9-solución-de-problemas)
10. [Referencia rápida](#10-referencia-rápida)

---

## 1. Qué es este proyecto

El sitio corporativo de **Grupo Arcondec** son 28 páginas HTML estáticas —14 en español,
14 en inglés— construidas sobre el template *aball (index-12)* con la marca, colores y
contenido oficiales de [arcondec.mx](https://arcondec.mx).

Tres decisiones definen todo lo demás:

1. **Es un sitio generado.** Las páginas HTML no se escriben a mano: las produce el
   script `tools/build.py` a partir de los textos guardados en `tools/`. Esto garantiza
   que las 28 páginas compartan siempre el mismo menú, pie, SEO y estructura.
2. **Cada idioma tiene URL propia.** `/nosotros.html` y `/en/about.html` son dos
   archivos reales, no un conmutador de JavaScript. Por eso Google indexa ambas
   versiones.
3. **El despliegue no tiene build.** Vercel sirve el repositorio tal cual. Lo que está
   en la rama `main` de GitHub es, literalmente, lo que ve el visitante.

```
   tools/content.py  ─┐
   tools/pages.py    ─┤                        ┌─ index.html, nosotros.html …
   tools/layout.py   ─┼──► tools/build.py ────►┼─ en/index.html, en/about.html …
   tools/home_source ─┤     (generador)        ├─ sitemap.xml, robots.txt
   tools/home_i18n   ─┘                        └─ (28 páginas en total)
                                                        │
                            tools/check.py ◄────────────┘
                            (verificador: enlaces, SEO, alt, h1…)
```

---

## 2. Las tres reglas de oro

Estas tres reglas protegen todo el trabajo estructural ya hecho (SEO, bilingüe,
accesibilidad, animaciones). Todo lo demás del manual son detalles; esto es lo
innegociable.

> **Regla 1 — El HTML generado no se edita a mano.**
> Cualquier cambio hecho directamente en `index.html`, `nosotros.html`, `en/…`, etc.
> se **pierde** la próxima vez que alguien ejecute el generador. Los textos se cambian
> en `tools/` y se regenera el sitio (sección 5).

> **Regla 2 — Los archivos del template no se tocan.**
> `assets/css/style.css`, `assets/js/main.js` y `assets/js/vendor/` quedan intactos.
> Todo lo propio de Arcondec vive en `assets/css/arcondec.css` (estilos) y
> `assets/js/arcondec-motion.js` (animaciones). Así, actualizar el template nunca pisa
> el trabajo hecho.

> **Regla 3 — Nada se publica sin pasar el verificador.**
> Después de cualquier cambio: `python3 tools/build.py` y luego `python3 tools/check.py`.
> Solo cuando el verificador dice **«Sin problemas.»** se hace commit y push.

---

## 3. Cómo funciona: arquitectura

### 3.1 Mapa del repositorio

```
├── index.html, nosotros.html, proyectos.html,        ← GENERADAS (no editar)
│   contacto.html, trabaja-con-nosotros.html,
│   blog.html, servicios.html, servicios/*.html
├── en/                                                ← GENERADAS (no editar)
│   index.html, about.html, projects.html, …
├── sitemap.xml, robots.txt                            ← GENERADOS (no editar)
│
├── tools/                          ← AQUÍ SE EDITA EL CONTENIDO
│   ├── build.py                    El generador. Se ejecuta, no se suele editar.
│   ├── check.py                    El verificador. Se ejecuta, no se edita.
│   ├── content.py                  Los 7 servicios (ES/EN) + datos de contacto
│   ├── pages.py                    Nosotros, proyectos, contacto, empleo, blog
│   ├── layout.py                   Menú, pie, <head>, rutas, BASE_URL
│   ├── home_source.html            Maquetación de la página de inicio
│   ├── home_i18n.js                Textos ES/EN de la página de inicio
│   ├── measure_images.py           Mide imágenes → image_sizes.json
│   └── image_sizes.json            Dimensiones reales de cada imagen
│
├── assets/
│   ├── css/style.css               Template — NO TOCAR
│   ├── css/arcondec.css            Todos los estilos propios de Arcondec
│   ├── js/main.js                  Template — NO TOCAR
│   ├── js/vendor/                  GSAP, ScrollTrigger, SplitText — NO TOCAR
│   ├── js/arcondec-motion.js       Todas las animaciones del sitio
│   └── images/
│       ├── arcondec/               Imágenes propias: servicios/, blog/,
│       │                           proyectos/, secciones/, brand/, clients/, rh/
│       └── (resto)                 Imágenes del template
│
├── vercel.json                     Cabeceras de caché y seguridad
├── CLAUDE.md                       Reglas del proyecto para asistentes de IA
└── MANUAL.md                       Este documento
```

### 3.2 El flujo de un cambio, de principio a fin

1. Se edita el texto en el archivo de `tools/` que corresponda (tabla de la sección 10).
2. `python3 tools/build.py` reescribe las 28 páginas, el sitemap y el robots.txt.
3. `python3 tools/check.py` revisa las 28 páginas: enlaces rotos, `<h1>` único,
   `title`, `meta description`, `canonical`, `hreflang`, atributos `alt`, etiquetas
   malformadas.
4. `git add -A && git commit && git push` sube el resultado a GitHub.
5. Vercel detecta el push y publica en 1–2 minutos. Sin pasos intermedios.

### 3.3 Detalles que el generador resuelve solo

Conviene saber que existen para no «arreglarlos» a mano:

- **Versionado de CSS/JS.** El generador añade `?v=<hash>` a cada CSS y JS. Así los
  visitantes reciben los estilos nuevos al instante aunque la caché dure una hora.
- **Dimensiones de imagen.** Cada `<img>` lleva su `width`/`height` real (leído de
  `tools/image_sizes.json`) para que la página no «salte» mientras carga.
- **SEO completo por página:** canonical, hreflang ES/EN, Open Graph, Twitter Card y
  datos estructurados JSON-LD (`Organization`, `Service`, `ItemList`, `LocalBusiness`).

---

## 4. Preparar el entorno de trabajo

**Requisitos:** Python 3 (macOS ya lo trae) y git. Nada más — no hay `npm install`
ni dependencias que instalar. Solo para medir imágenes nuevas hace falta Pillow
(`pip3 install Pillow`, una sola vez).

```bash
# 1. Clonar el repositorio (solo la primera vez)
git clone https://github.com/Juanescanar23/Grupo-Arcondec.git
cd Grupo-Arcondec

# 2. Ver el sitio en local
python3 -m http.server 8080
# → abrir http://localhost:8080 en el navegador
```

Para detener el servidor local: `Ctrl+C` en la terminal.

---

## 5. Recetario de ediciones

Cada receta termina igual: **build → check → commit** (sección 6). Aquí solo se
detalla el paso de edición.

### 5.1 Cambiar un texto o título de un servicio

Los 7 servicios viven en `tools/content.py`, en la lista `SERVICES`. Cada servicio es
un bloque con dos diccionarios: `"es"` y `"en"`. Los campos:

| Campo            | Qué es                                                    |
| ---------------- | --------------------------------------------------------- |
| `nav`            | Nombre corto en el menú de navegación                     |
| `title`          | Título de la pestaña del navegador (`<title>`)            |
| `meta`           | Descripción para Google (meta description)                |
| `keywords`       | Palabras clave SEO                                        |
| `h1`             | Titular grande de la página                               |
| `lead` / `tagline` | Frases de apoyo bajo el titular                         |
| `intro_h2` / `intro` | Título y párrafo de introducción                      |
| `list_title` / `list` | Título y viñetas de «Servicios especializados»       |
| `benefits_*`     | Bloque de beneficios: título, intro y tarjetas (título, texto) |
| `cta_title` / `cta_text` | Llamada a la acción final                         |

**Ejemplo.** Para cambiar el titular de «Proyectos eléctricos integrales»: buscar en
`content.py` el bloque cuyo `key` es `"proele"`, y dentro de `"es"` editar la línea:

```python
"h1": "Proyectos eléctricos integrales",
```

**Importante:** el mismo bloque tiene su versión `"en"` unas líneas más abajo.
Todo cambio de texto se hace **en los dos idiomas** — si no se cambia el inglés,
las dos versiones del sitio dejan de decir lo mismo.

### 5.2 Cambiar textos de las demás páginas interiores

En `tools/pages.py`, organizadas por diccionarios con la misma lógica ES/EN:

| Diccionario      | Página                                        |
| ---------------- | --------------------------------------------- |
| `ABOUT`          | Nosotros / About                              |
| `HUBS`, `PROJECTS` | Proyectos / Projects                        |
| `SERVICES_INDEX` | Índice de servicios                           |
| `CONTACT_PAGE`, `MX_STATES` | Contacto / Contact (incluye el formulario) |
| `CAREERS`        | Trabaja con nosotros / Careers                |
| `BLOG`, `ARTICLES` | Blog e inventario de artículos              |

Se busca el texto a cambiar (Cmd+F con la frase actual), se edita en ES y en EN, y se
regenera.

### 5.3 Cambiar la página de inicio

El inicio es un caso especial: se genera combinando **dos** archivos.

- **Los textos** están en `tools/home_i18n.js`: un diccionario `es:` y otro `en:` con
  claves como `heroTitle`, `sec1Title`, `hub1Name`… Cambiar el texto en ambos idiomas
  y regenerar. Este es el archivo que se toca el 95 % de las veces.
- **La maquetación** (qué secciones hay y en qué orden) está en
  `tools/home_source.html`. Solo se toca para cambios estructurales del inicio.

El generador produce `index.html` (ES) y `en/index.html` (EN) a partir de ambos.

### 5.4 Cambiar teléfonos, correos, dirección o redes sociales

Todo está centralizado en `tools/content.py`, al principio del archivo:

- `CONTACT` — dirección, teléfonos (versión visible y versión `tel:` con lada),
  todos los correos (info, ventas ES/EN, RH, quejas, proveedores, talento) y el
  enlace de Google Maps.
- `SOCIAL` — Facebook, Instagram, LinkedIn, YouTube.
- `WHATSAPP` — el enlace de WhatsApp con el mensaje precargado (el texto va
  codificado para URL: los espacios son `%20`).
- `PRIVACY_PDF`, `LOGIN_URL`, `VIDEO_URL` — aviso de privacidad, portal de login y
  video corporativo.

Un solo cambio aquí se propaga a las 28 páginas al regenerar. Ojo con los teléfonos:
cada número tiene dos entradas — `phone1` (como se ve: `81 1934 1192`) y `phone1_tel`
(como se marca: `+528119341192`) — y hay que cambiar ambas.

### 5.5 Cambiar o agregar una imagen

Las imágenes propias viven en `assets/images/arcondec/`, organizadas por carpeta:

| Carpeta      | Contenido                                          |
| ------------ | -------------------------------------------------- |
| `servicios/` | Fotos de las páginas de servicio: `<key>-N.jpg`    |
| `blog/`      | Imágenes de los artículos del blog                 |
| `proyectos/` | Fotos de la página de proyectos                    |
| `secciones/` | Fondos y fotos de secciones del inicio             |
| `brand/`     | Logo y elementos de marca                          |
| `clients/`   | Logos de clientes                                  |
| `rh/`        | Imágenes de la página de reclutamiento             |

**Reemplazar una imagen existente** (el caso común):

1. Guardar la imagen nueva **con el mismo nombre y en la misma carpeta** que la que
   sustituye. Formato JPG para fotos; idealmente comprimida (< 300 KB) y de ancho
   máximo ~1600 px.
2. Medirla: `python3 tools/measure_images.py` (la primera vez: `pip3 install Pillow`).
   Esto actualiza `tools/image_sizes.json` con las dimensiones reales — si se omite y
   la imagen nueva tiene otra proporción, la página «salta» al cargar.
3. `python3 tools/build.py` y `python3 tools/check.py`.

**Las fotos de un servicio** siguen la convención `servicios/<key>-N.jpg`, donde
`<key>` es la clave del servicio en `content.py` (`proele`, `estel`, `corac`, `gespr`,
`cosdc`, `civdc`, `ingdc`) y `N` los números listados en su campo `photos`. Para que
un servicio muestre otra foto más, se añade el archivo (p. ej. `estel-7.jpg`) y se
agrega el `7` a su lista `photos`.

**Nota sobre caché:** las imágenes se sirven con caché de un año. Si se reemplaza una
imagen manteniendo el nombre, un visitante recurrente puede seguir viendo la vieja un
tiempo. Si es crítico que se vea la nueva de inmediato, mejor darle un nombre nuevo y
actualizar la referencia.

### 5.6 Cambiar el dominio del sitio

El dominio de producción está en **una sola línea**: `BASE_URL` en `tools/layout.py`
(hoy `https://grupo-arcondec.vercel.app`). Cuando el sitio se publique en el dominio
definitivo, se cambia ahí, se regenera, y todos los canonical, hreflang, sitemap y
datos estructurados quedan apuntando al dominio nuevo.

### 5.7 Publicar los artículos del blog

Los 12 artículos están inventariados en `tools/pages.py` (`ARTICLES`), con su slug,
imagen, título y resumen en ambos idiomas, y aparecen en el índice del blog marcados
como «Próximamente». Las páginas de artículo completo son la siguiente etapa del
proyecto: requieren añadir una plantilla de artículo al generador. Es trabajo de
desarrollo, no de edición — pedirlo como encargo (a JectCode o a una IA con el
contexto de este manual).

---

## 6. Verificar y publicar

La secuencia completa, después de cualquier edición:

```bash
# 1. Regenerar el sitio
python3 tools/build.py
#    → debe terminar en "28 páginas + sitemap.xml + robots.txt"

# 2. Verificar
python3 tools/check.py
#    → debe terminar en "Sin problemas."

# 3. Revisar en local (opcional pero recomendado)
python3 -m http.server 8080     # → http://localhost:8080

# 4. Publicar
git add -A
git commit -m "Describe aquí el cambio"
git push
```

Vercel publica automáticamente en 1–2 minutos tras el push a `main`. Si `check.py`
reporta problemas, **no publicar**: el mensaje dice exactamente qué página y qué
falta.

---

## 7. Cómo pedirle los cambios a una IA

El proyecto está preparado para trabajarse con asistentes de IA (Claude Code, Cursor,
etc.). El archivo **`CLAUDE.md`** en la raíz del repositorio contiene las reglas del
proyecto y los asistentes compatibles lo leen automáticamente: es el guardarraíl que
impide que una IA edite el HTML generado o toque los archivos del template.

### 7.1 Las cuatro instrucciones que siempre deben ir en el encargo

1. **Qué cambiar, con el texto literal actual.** «El titular que hoy dice X debe
   decir Y» funciona; «mejora el titular» obliga a la IA a inventar.
2. **En ambos idiomas.** Dar la versión EN del texto nuevo, o pedir explícitamente
   que la IA la traduzca.
3. **Que respete el flujo del proyecto:** editar solo en `tools/`, regenerar con
   `build.py` y verificar con `check.py`.
4. **Que muestre el resultado del verificador** antes de dar el cambio por hecho.

### 7.2 Ejemplos de encargos bien planteados

> «En este proyecto los cambios se hacen en `tools/` y se regenera con
> `python3 tools/build.py` (lee CLAUDE.md). Cambia el titular del servicio de
> estudios eléctricos: donde dice "Estudios eléctricos especializados" debe decir
> "Estudios eléctricos certificados", y en inglés "Certified electrical studies".
> Regenera, corre `tools/check.py` y muéstrame que salió sin problemas.»

> «Lee CLAUDE.md. Cambia el teléfono móvil de contacto de (55) 3032 6595 a
> (55) 1234 5678 en `tools/content.py` — recuerda que hay dos entradas, la visible
> y la versión tel: con lada +52. Regenera y verifica.»

> «Lee CLAUDE.md. Voy a reemplazar la foto `assets/images/arcondec/servicios/estel-3.jpg`
> por una nueva con el mismo nombre. Ya la copié. Corre `tools/measure_images.py`,
> regenera el sitio y verifica.»

### 7.3 Encargos mal planteados (y por qué)

| Encargo                                       | Problema                                                        |
| --------------------------------------------- | --------------------------------------------------------------- |
| «Cambia el título en `nosotros.html`»         | Edita el HTML generado: el cambio se pierde en el próximo build |
| «Mejora los textos del sitio»                 | Sin texto literal, la IA reescribe contenido oficial aprobado   |
| «Haz que los colores resalten más»            | El contraste ya está auditado WCAG AA; aclarar colores lo rompe |
| «Quita las animaciones que tardan»            | Las salvaguardas de `arcondec-motion.js` existen por accesibilidad; pedir el ajuste concreto, no la eliminación |

### 7.4 Cómo revisar lo que hizo la IA

Antes de aceptar el trabajo, tres comprobaciones — no hace falta saber programar:

1. `git status` — los archivos modificados deben ser de `tools/` **más** las páginas
   HTML regeneradas. Si solo hay HTML modificado sin nada en `tools/`, la IA editó a
   mano lo generado: rechazar y pedir que lo haga por la vía correcta.
2. `python3 tools/check.py` — debe decir «Sin problemas.»
3. Ver la página en `http://localhost:8080`, en español **y** en inglés.

---

## 8. Lo que nunca se debe hacer

- ✗ Editar a mano cualquier `.html` de la raíz o de `en/`, o `sitemap.xml`/`robots.txt`.
- ✗ Modificar `assets/css/style.css`, `assets/js/main.js` o `assets/js/vendor/`.
- ✗ Cambiar un texto en un solo idioma.
- ✗ Publicar con `check.py` en rojo.
- ✗ Subir imágenes sin pasar `measure_images.py`.
- ✗ Aclarar colores de texto sin recalcular el contraste (auditado WCAG AA).
- ✗ Quitar de `arcondec-motion.js` las salvaguardas de accesibilidad
  (`prefers-reduced-motion`, revelado forzoso al fondo de página, salida limpia sin GSAP).
- ✗ Borrar o renombrar páginas sin actualizar `ROUTES` en `tools/layout.py` — los
  hreflang y el sitemap quedarían apuntando a páginas inexistentes (check.py lo detecta).

---

## 9. Solución de problemas

| Síntoma                                            | Causa probable → solución                                                                 |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Cambié un texto y no se ve en el navegador         | Falta regenerar: `python3 tools/build.py`. Luego recargar con Cmd+Shift+R                 |
| Mi cambio desapareció                              | Se editó el HTML generado y alguien regeneró. Rehacer el cambio en `tools/`               |
| `build.py` falla con `SyntaxError`                 | Comilla o coma rota al editar un `.py`. Revisar la línea que indica el error; las comillas dentro de un texto van escapadas (`\"`) o se usa el otro tipo de comilla |
| `check.py` reporta «X roto»                        | Un enlace o imagen apunta a un archivo que no existe. Crear el archivo o corregir la ruta |
| `check.py` reporta «sin hreflang» o «sin canonical» | Se creó una página fuera del generador. Las páginas nuevas se añaden vía `tools/`         |
| La página «salta» al cargar una imagen nueva       | Falta `python3 tools/measure_images.py` + regenerar                                       |
| `measure_images.py` falla con `No module named PIL` | `pip3 install Pillow`                                                                     |
| Subí a GitHub pero el sitio no cambia              | Ver el panel de Vercel (deploy fallido) o esperar 1–2 min. Las imágenes cachean 1 año: cambio de imagen con mismo nombre tarda en verse |
| Las animaciones no funcionan                       | Es correcto si el sistema tiene «reducir movimiento» activado. Probar en ventana normal sin esa preferencia |
| Un bloque no debe animarse                         | Añadirle `data-arc-motion="off"` — pero en `tools/`, no en el HTML generado               |

---

## 10. Referencia rápida

| Quiero cambiar…                                | Archivo                                  | Después                     |
| ---------------------------------------------- | ---------------------------------------- | --------------------------- |
| Texto/título de un servicio                    | `tools/content.py` → `SERVICES`          | build + check               |
| Teléfono, correo, dirección, redes, WhatsApp   | `tools/content.py` → `CONTACT`, `SOCIAL`, `WHATSAPP` | build + check   |
| Nosotros, proyectos, contacto, empleo, blog    | `tools/pages.py`                         | build + check               |
| Textos del inicio                              | `tools/home_i18n.js` (es **y** en)       | build + check               |
| Maquetación del inicio                         | `tools/home_source.html`                 | build + check               |
| Menú, pie de página, SEO global                | `tools/layout.py`                        | build + check               |
| Dominio de producción                          | `BASE_URL` en `tools/layout.py`          | build + check               |
| Una imagen                                     | `assets/images/arcondec/…`               | measure + build + check     |
| Estilos (colores, espaciados)                  | `assets/css/arcondec.css`                | recargar (sin build)        |
| Animaciones                                    | `assets/js/arcondec-motion.js`           | recargar (sin build)        |

**Los tres comandos, siempre en este orden:**

```bash
python3 tools/build.py     # regenerar
python3 tools/check.py     # verificar → "Sin problemas."
git add -A && git commit -m "…" && git push    # publicar
```

---

<div align="center">

© Grupo Arcondec S.A. de C.V. · Documento técnico elaborado por [JectCode](https://github.com/Juanescanar23)

</div>
