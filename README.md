# Grupo Arcondec — Sitio corporativo

Sitio estático (HTML/CSS/JS) sobre el template **aball (index-12)** con el contenido, logo y
colores oficiales de [arcondec.mx](https://arcondec.mx). Bilingüe ES/EN con **una URL por
idioma**. Sin build en el despliegue: Vercel sirve el repositorio tal cual.

---

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

1. Edita el texto en `tools/content.py` (servicios y datos de contacto) o en
   `tools/pages.py` (inicio, nosotros, proyectos, contacto, reclutamiento, blog).
2. Regenera el sitio:

   ```bash
   python3 tools/build.py
   ```

3. Comprueba que no se rompió nada:

   ```bash
   python3 tools/check.py
   ```

El inicio es un caso aparte: su maquetación vive en `tools/home_source.html` y sus textos
ES/EN en `tools/home_i18n.js`. El generador combina ambos para producir `index.html` y
`en/index.html`.

## Ver el sitio en local

```bash
python3 -m http.server 8080
```

Y abre <http://localhost:8080>.

## Bilingüe y SEO

Cada página existe en dos URLs reales, no con un conmutador de JavaScript. Esto es lo que
permite que Google indexe también la versión en inglés:

- `<link rel="canonical">` propio en cada página.
- `<link rel="alternate" hreflang="es-MX|en|x-default">` enlazando ambas versiones.
- `title`, `meta description` y `keywords` por página y por idioma.
- Open Graph y Twitter Card para cuando se comparte el enlace.
- Datos estructurados JSON-LD: `Organization` en todo el sitio, más `Service` en cada
  servicio, `ItemList` en proyectos y `LocalBusiness` (con horario y coordenadas) en
  contacto — la base de lo que leen los motores de IA.
- `sitemap.xml` y `robots.txt` generados automáticamente.

El dominio de producción está en una sola línea: `BASE_URL`, en `tools/layout.py`. Si el
sitio se publica en otro dominio, se cambia ahí y se regenera.

## Estilos

`assets/css/style.css` es del template y **no se toca**, para que una actualización del
template no pise el trabajo hecho. Todo lo de Arcondec —colores de marca, componentes de las
páginas interiores y correcciones de responsividad— está en `assets/css/arcondec.css`.

## Pendiente

Los 12 artículos del blog están listados en el índice con su título, resumen e imagen, pero
marcados como «Próximamente»: las páginas de artículo completo son la siguiente tanda. El
contenido ya está inventariado en `tools/pages.py` (`ARTICLES`).

---

© Grupo Arcondec S.A. de C.V. · Desarrollo JectCode
