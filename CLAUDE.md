# Grupo Arcondec — Reglas del proyecto

Sitio estático **generado**. Las páginas HTML de la raíz y de `en/` las escribe
`tools/build.py`; cualquier edición manual sobre ellas se pierde en el siguiente build.

## Regla nº 1 — nunca editar el HTML generado

Todo cambio de contenido se hace en `tools/` y se regenera:

```bash
python3 tools/build.py    # regenera las 28 páginas + sitemap + robots
python3 tools/check.py    # debe terminar en "Sin problemas." antes de commitear
```

## Qué archivo controla qué

| Quiero cambiar…                                      | Archivo                             |
| ---------------------------------------------------- | ----------------------------------- |
| Textos de los 7 servicios (ES y EN)                  | `tools/content.py` → `SERVICES`     |
| Datos de contacto, teléfonos, correos, redes, WhatsApp | `tools/content.py` → `CONTACT`, `SOCIAL`, `WHATSAPP` |
| Nosotros, proyectos, contacto, reclutamiento, blog   | `tools/pages.py`                    |
| Página de inicio — maquetación                       | `tools/home_source.html`            |
| Página de inicio — textos ES/EN                      | `tools/home_i18n.js`                |
| Menú, pie, `<head>`, rutas, SEO                      | `tools/layout.py`                   |
| Dominio de producción                                | `BASE_URL` en `tools/layout.py`     |
| Estilos propios                                      | `assets/css/arcondec.css`           |
| Animaciones                                          | `assets/js/arcondec-motion.js`      |

## Intocables

- `assets/css/style.css`, `assets/js/main.js` y todo lo demás del template **no se
  modifican**: los overrides van en `arcondec.css`. `assets/js/vendor/` tampoco.
- Todo texto visible existe en **dos idiomas**: al cambiar el ES, cambia también el EN
  (mismo dict en `content.py`/`pages.py`, o la clave hermana en `home_i18n.js`).
- En `arcondec-motion.js` no eliminar las salvaguardas: salida limpia si GSAP no carga,
  respeto a `prefers-reduced-motion`, espera a fuentes, y el revelado forzoso al llegar
  al fondo de la página. Para excluir un bloque de animación: `data-arc-motion="off"`.
- Contraste WCAG AA ya auditado: no aclarar colores de texto sin recalcular el ratio.

## Imágenes

- Las de Arcondec viven en `assets/images/arcondec/` (subcarpetas `servicios/`, `blog/`,
  `proyectos/`, `secciones/`, `brand/`, `clients/`, `rh/`). El resto de `assets/images/`
  es del template.
- Fotos de servicio siguen la convención `servicios/<key>-N.jpg`, donde `<key>` y la
  lista `photos` están en `SERVICES` (`tools/content.py`).
- Tras agregar o reemplazar una imagen: `python3 tools/measure_images.py`
  (requiere `pip3 install Pillow`) y después `python3 tools/build.py`.

## Al terminar cualquier cambio

`build.py` → `check.py` en verde → commit. Vercel publica el repo tal cual al hacer
push a `main`; no hay paso de build en el despliegue.
