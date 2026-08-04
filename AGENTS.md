# Grupo Arcondec — Contexto y reglas del proyecto

Instrucciones para cualquier asistente de IA (Claude, Codex, Cursor, Gemini, Kimi…)
que trabaje sobre este repositorio. Léelas completas antes de tocar nada.
La documentación extensa para humanos está en `MANUAL.md`.

## El concepto, en un párrafo

Sitio corporativo **estático y generado** de Grupo Arcondec (ingeniería eléctrica y
data centers, Monterrey, México): 28 páginas HTML — 14 en español y sus 14 gemelas en
inglés, cada una con URL propia — construidas sobre el template comercial *aball
(index-12)*. No hay CMS, ni base de datos, ni build en el despliegue: los textos viven
en `tools/`, el generador `tools/build.py` produce las páginas terminadas con todo el
SEO incluido (canonical, hreflang ES/EN, Open Graph, JSON-LD, sitemap), y Vercel
publica el repositorio tal cual en cada push a `main`.

## Regla nº 1 — nunca editar el HTML generado

Las páginas HTML de la raíz y de `en/`, más `sitemap.xml` y `robots.txt`, son
**producto** del generador: se sobrescriben completas en cada ejecución. Todo cambio
de contenido se hace en `tools/` y se regenera:

```bash
python3 tools/build.py    # regenera las 28 páginas + sitemap + robots
python3 tools/check.py    # debe terminar en "Sin problemas." antes de commitear
```

(En Windows: `python` en lugar de `python3`.)

## Qué archivo controla qué

| Quiero cambiar… | Archivo |
|---|---|
| Textos de los 7 servicios (ES y EN) | `tools/content.py` → `SERVICES` |
| Datos de contacto, teléfonos, correos, redes, WhatsApp | `tools/content.py` → `CONTACT`, `SOCIAL`, `WHATSAPP` |
| Nosotros, proyectos, contacto, reclutamiento, blog | `tools/pages.py` |
| Página de inicio — textos ES/EN | `tools/home_i18n.js` |
| Página de inicio — maquetación | `tools/home_source.html` |
| Menú, pie, `<head>`, rutas, SEO global | `tools/layout.py` |
| Dominio de producción | `BASE_URL` en `tools/layout.py` |
| Estilos propios | `assets/css/arcondec.css` |
| Animaciones | `assets/js/arcondec-motion.js` |

## Intocables

- `assets/css/style.css`, `assets/js/main.js` y todo lo demás del template **no se
  modifican**: los overrides van en `arcondec.css`. `assets/js/vendor/` (GSAP,
  ScrollTrigger, SplitText) tampoco.
- Todo texto visible existe en **dos idiomas**: al cambiar el ES, cambia también el EN
  (mismo dict en `content.py`/`pages.py`, o la clave hermana en `home_i18n.js`).
- En `arcondec-motion.js` no eliminar las salvaguardas: salida limpia si GSAP no
  carga, respeto a `prefers-reduced-motion`, espera a fuentes, y el revelado forzoso
  al llegar al fondo de la página. Para excluir un bloque de animación:
  `data-arc-motion="off"`.
- Contraste WCAG AA ya auditado: no aclarar colores de texto sin recalcular el ratio.
- No borrar ni renombrar páginas por fuera del generador: `ROUTES` en
  `tools/layout.py` es la fuente de las rutas, hreflang y sitemap.
- `vercel.json` no se modifica: declara que no hay build, la caché escalonada
  (imágenes/fuentes 1 año inmutable; css/js 1 hora, compensada por el versionado
  `?v=<hash>` que añade el generador) y las cabeceras de seguridad (nosniff,
  X-Frame-Options, HSTS, Permissions-Policy).

## SEO — invariantes

El generador escribe automáticamente canonical, hreflang, Open Graph, Twitter Card,
JSON-LD (`Organization`, `Service`, `ItemList`, `LocalBusiness`), sitemap y robots.
Lo redactado a mano son los campos `title` (50–60 caracteres, keyword primero,
únicos por página), `meta` (150–160 caracteres) y `h1` (exactamente uno por página)
en `content.py`/`pages.py`, siempre en ambos idiomas. `check.py` verifica todo esto;
no publicar si reporta problemas.

## Imágenes

- Las de Arcondec viven en `assets/images/arcondec/` (subcarpetas `servicios/`,
  `blog/`, `proyectos/`, `secciones/`, `brand/`, `clients/`, `rh/`). El resto de
  `assets/images/` es del template.
- Fotos de servicio siguen la convención `servicios/<key>-N.jpg`, donde `<key>` y la
  lista `photos` están en `SERVICES` (`tools/content.py`).
- Tras agregar o reemplazar una imagen: `python3 tools/measure_images.py`
  (requiere `pip3 install Pillow`) y después `python3 tools/build.py`. Sin ese paso,
  el `<img>` pierde sus dimensiones reales y empeora el CLS.

## Al terminar cualquier cambio

`build.py` → `check.py` en verde → commit con mensaje descriptivo. Vercel publica el
repo tal cual al hacer push a `main`; no hay paso de build en el despliegue.
