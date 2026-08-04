<div align="center">

# Manual de operación y edición del sitio

### Grupo Arcondec — Sitio corporativo bilingüe

**Documento de entrega técnica y guía del editor**

Versión 2.0 · Agosto 2026 · Elaborado por JectCode

[grupo-arcondec.vercel.app](https://grupo-arcondec.vercel.app) · [github.com/Juanescanar23/Grupo-Arcondec](https://github.com/Juanescanar23/Grupo-Arcondec)

</div>

---

## Índice

1. [Presentación de este documento](#1-presentación-de-este-documento)
2. [Qué es este proyecto y por qué funciona así](#2-qué-es-este-proyecto-y-por-qué-funciona-así)
3. [Las tres reglas de oro](#3-las-tres-reglas-de-oro)
4. [Conceptos básicos para quien no programa](#4-conceptos-básicos-para-quien-no-programa)
5. [Preparar el entorno de trabajo](#5-preparar-el-entorno-de-trabajo)
6. [Recetario de ediciones](#6-recetario-de-ediciones)
   - 6.1 [Cambiar un texto o título de un servicio](#61-cambiar-un-texto-o-título-de-un-servicio)
   - 6.2 [Cambiar textos de las demás páginas interiores](#62-cambiar-textos-de-las-demás-páginas-interiores)
   - 6.3 [Cambiar la página de inicio](#63-cambiar-la-página-de-inicio)
   - 6.4 [Cambiar teléfonos, correos, dirección o redes sociales](#64-cambiar-teléfonos-correos-dirección-o-redes-sociales)
   - 6.5 [Cambiar o agregar una imagen](#65-cambiar-o-agregar-una-imagen)
   - 6.6 [Cambiar el dominio del sitio](#66-cambiar-el-dominio-del-sitio)
   - 6.7 [Publicar los artículos del blog](#67-publicar-los-artículos-del-blog)
7. [El SEO del sitio y cómo mantenerlo](#7-el-seo-del-sitio-y-cómo-mantenerlo)
8. [Verificar y publicar](#8-verificar-y-publicar)
9. [Cómo pedirle los cambios a una inteligencia artificial](#9-cómo-pedirle-los-cambios-a-una-inteligencia-artificial)
10. [Lo que nunca se debe hacer](#10-lo-que-nunca-se-debe-hacer)
11. [Solución de problemas](#11-solución-de-problemas)
12. [Referencia rápida](#12-referencia-rápida)
13. [Glosario](#13-glosario)

---

## 1. Presentación de este documento

Este manual acompaña la entrega del sitio corporativo de **Grupo Arcondec**. Está
escrito para la persona que se hará cargo de mantenerlo y editarlo a partir de ahora,
**sin dar por hecho que sepa programar**. Cada término técnico se explica la primera
vez que aparece, y todos están reunidos al final en el [glosario](#13-glosario).

El documento tiene tres partes, pensadas para leerse en este orden:

- **Capítulos 1 a 5** — el contexto: qué es el sitio, cómo está construido, qué reglas
  lo protegen y cómo preparar la computadora para trabajar con él. Se leen una sola
  vez.
- **Capítulos 6 a 8** — el trabajo del día a día: recetas paso a paso para cada tipo
  de cambio (textos, imágenes, datos de contacto), el cuidado del posicionamiento en
  buscadores, y el procedimiento para publicar. Es la parte que se consulta cada vez
  que haya que editar algo.
- **Capítulos 9 a 13** — las herramientas de apoyo: cómo encargar los cambios a una
  inteligencia artificial de forma segura, la lista de acciones prohibidas, la guía de
  solución de problemas, la tabla de referencia rápida y el glosario.

Si solo se dispone de cinco minutos, lo esencial es esto: el capítulo 3 (las tres
reglas de oro) y la tabla del capítulo 12 (qué archivo tocar para cada cambio).

---

## 2. Qué es este proyecto y por qué funciona así

### 2.1 El sitio en una frase

El sitio corporativo de Grupo Arcondec son **28 páginas web** —14 en español y sus 14
equivalentes en inglés— construidas sobre una plantilla de diseño profesional (el
template *aball*) y adaptadas con la marca, los colores y los textos oficiales de
[arcondec.mx](https://arcondec.mx).

### 2.2 La decisión central: un sitio generado, no un CMS

Existen dos maneras habituales de mantener un sitio web:

- **Un CMS** (*Content Management System*, sistema de gestión de contenidos, como
  WordPress): un panel de administración con usuario y contraseña donde se editan los
  textos desde el navegador.
- **Un sitio estático generado**, que es lo que se eligió aquí: los textos viven en
  unos pocos archivos ordenados, y un programa llamado **generador** construye con
  ellos las 28 páginas terminadas.

Se descartó el CMS deliberadamente, por cuatro razones:

1. **Costo y mantenimiento.** Un CMS es un programa en funcionamiento permanente:
   necesita servidor, base de datos, actualizaciones de seguridad y respaldos. Un
   sitio estático no necesita nada de eso — son archivos servidos tal cual, y el
   alojamiento en Vercel es gratuito para este volumen.
2. **Seguridad.** Un CMS tiene página de inicio de sesión, y por tanto puede ser
   atacado. Aquí no hay nada que hackear: no existe panel, ni base de datos, ni
   contraseñas.
3. **Velocidad.** Las páginas ya están construidas antes de que el visitante llegue;
   no hay que armarlas en cada visita. Eso se traduce en tiempos de carga mínimos,
   que además favorecen el posicionamiento en Google.
4. **El SEO queda protegido por diseño.** Todo el trabajo de posicionamiento
   (capítulo 7) lo escribe el generador de forma automática y uniforme en las 28
   páginas. En un CMS, cada editor puede — sin querer — borrar o duplicar esas
   etiquetas. Aquí es imposible: el editor cambia el texto, y el generador recompone
   todo lo demás.

El precio de estas ventajas es que editar no se hace desde un panel web, sino
modificando archivos de texto y ejecutando dos comandos. Este manual existe
precisamente para que ese procedimiento resulte tan claro como usar un panel — y el
capítulo 9 enseña, además, a delegárselo a una inteligencia artificial.

### 2.3 Cómo se relacionan las piezas

El contenido del sitio (títulos, párrafos, teléfonos, listas de servicios) está
guardado en unos pocos archivos dentro de la carpeta `tools/`. El generador
(`tools/build.py`) los lee y escribe las 28 páginas terminadas. Un segundo programa,
el verificador (`tools/check.py`), revisa el resultado antes de publicar.

```text
   tools/content.py  ─┐
   tools/pages.py    ─┤                        ┌─ index.html, nosotros.html …
   tools/layout.py   ─┼──► tools/build.py ────►┼─ en/index.html, en/about.html …
   tools/home_source ─┤     (el generador)     ├─ sitemap.xml, robots.txt
   tools/home_i18n   ─┘                        └─ (28 páginas en total)
                                                        │
                            tools/check.py ◄────────────┘
                            (el verificador)
```

De aquí se desprende la idea más importante de todo el manual: **las 28 páginas HTML
son un producto, no una fuente**. Se regeneran completas en cada ejecución. Editarlas
directamente es como corregir un documento impreso con pluma: la corrección
desaparece en la siguiente impresión.

### 2.4 Dónde vive el sitio

- **El código y el contenido** están en GitHub, un servicio que guarda el proyecto en
  la nube y conserva el historial completo de cambios:
  [github.com/Juanescanar23/Grupo-Arcondec](https://github.com/Juanescanar23/Grupo-Arcondec).
- **El sitio publicado** lo sirve Vercel, un servicio de alojamiento conectado a ese
  repositorio: cada vez que se sube un cambio a GitHub, Vercel lo publica
  automáticamente en uno o dos minutos, sin ningún paso adicional.

---

## 3. Las tres reglas de oro

Todo el trabajo estructural ya realizado — el posicionamiento en buscadores, el
sistema bilingüe, la accesibilidad auditada, las animaciones — queda protegido si se
respetan tres reglas. El resto del manual son detalles; esto es lo innegociable.

> **Regla 1 — El HTML generado no se edita a mano.**
> Cualquier cambio hecho directamente sobre `index.html`, `nosotros.html`, la carpeta
> `en/` o cualquier otra página se **pierde** la próxima vez que se ejecute el
> generador. Los textos se cambian en los archivos de `tools/` y se regenera el sitio
> (capítulo 6 explica cómo, caso por caso).

> **Regla 2 — Los archivos de la plantilla original no se tocan.**
> `assets/css/style.css`, `assets/js/main.js` y la carpeta `assets/js/vendor/`
> permanecen intactos. Todo lo propio de Arcondec vive en dos archivos separados:
> `assets/css/arcondec.css` (los estilos) y `assets/js/arcondec-motion.js` (las
> animaciones). Gracias a esta separación, una futura actualización de la plantilla
> jamás pisará el trabajo hecho.

> **Regla 3 — Nada se publica sin pasar el verificador.**
> Después de cualquier cambio se ejecutan, en orden, `python3 tools/build.py` y
> `python3 tools/check.py`. Solo cuando el verificador termina con el mensaje
> **«Sin problemas.»** se sube el cambio. Si reporta algo, el propio mensaje indica
> qué página tiene el problema y de qué tipo es.

---

## 4. Conceptos básicos para quien no programa

Quien ya trabaje con la terminal y con git puede saltar directamente al capítulo 5.
Para el resto, estas cuatro ideas bastan para operar el sitio con seguridad.

### 4.1 La terminal

La **terminal** (en macOS: aplicación *Terminal*, dentro de *Aplicaciones →
Utilidades*) es una ventana donde se escriben órdenes para la computadora. En este
proyecto solo se usan cuatro o cinco órdenes, siempre las mismas, y todas están
escritas en este manual listas para copiar y pegar. Se pega la orden, se pulsa
Enter, y se lee la respuesta.

Una orden que se usará siempre al empezar es «situarse» en la carpeta del proyecto:

```bash
cd ruta/a/la/carpeta/del/proyecto
```

(`cd` significa *change directory*, cambiar de carpeta. Un atajo práctico en macOS:
escribir `cd `, con el espacio, y arrastrar la carpeta del proyecto desde el Finder
hasta la ventana de la terminal — la ruta se escribe sola.)

### 4.2 Los archivos de contenido

Los textos del sitio viven en archivos que se abren con cualquier editor de texto
plano. Se recomienda **Visual Studio Code** (gratuito, [code.visualstudio.com](https://code.visualstudio.com)):
resalta con colores la estructura de los archivos y avisa visualmente si una comilla
quedó sin cerrar. Los archivos de contenido tienen esta forma:

```python
"h1": "Proyectos eléctricos integrales",
```

A la izquierda, entre comillas, el **nombre del campo** (aquí `h1`, el titular de la
página): eso no se toca nunca. A la derecha, también entre comillas, **el texto
visible**: eso es lo que se edita. La coma final y las comillas deben conservarse
exactamente como están — son la puntuación que el generador necesita para leer el
archivo. Si el texto nuevo lleva comillas dobles por dentro, se usan comillas
tipográficas (« » o “ ”) para no confundir al generador.

### 4.3 Git y GitHub: el historial y la nube

**Git** es el sistema que lleva el historial del proyecto: cada vez que se «confirma»
un cambio (un **commit**), queda registrado quién cambió qué y cuándo, y siempre es
posible volver a cualquier versión anterior. Nada se pierde jamás — esa es la red de
seguridad de todo este sistema.

**GitHub** es el sitio en la nube donde vive la copia principal del proyecto. La
orden `git push` («empujar») sube los commits locales a GitHub. Y como Vercel está
conectado a GitHub, **subir es publicar**: uno o dos minutos después del push, el
cambio está en línea.

### 4.4 El generador y el verificador

Son los dos programas de la carpeta `tools/` que se ejecutan siempre en pareja:

- `python3 tools/build.py` — **el generador**: lee los archivos de contenido y
  reescribe las 28 páginas, el mapa del sitio y el archivo robots.txt. Tarda uno o
  dos segundos y termina indicando cuántas páginas produjo.
- `python3 tools/check.py` — **el verificador**: revisa las 28 páginas en busca de
  enlaces rotos, imágenes sin texto alternativo, etiquetas de SEO ausentes o
  duplicadas y errores de estructura. Es el control de calidad: su «Sin problemas.»
  es el semáforo verde para publicar.

---

## 5. Preparar el entorno de trabajo

**Requisitos:** una Mac con Python 3 (macOS ya lo incluye) y git (se instala solo la
primera vez que se usa). No hay nada más que instalar — ni paquetes, ni base de
datos, ni licencias. Únicamente, si se van a cambiar imágenes, hará falta una
biblioteca gratuita llamada Pillow: `pip3 install Pillow`, una sola vez.

```bash
# 1. Descargar el proyecto (solo la primera vez)
git clone https://github.com/Juanescanar23/Grupo-Arcondec.git
cd Grupo-Arcondec

# 2. Ver el sitio en la propia computadora
python3 -m http.server 8080
```

Con el servidor local corriendo, el sitio se ve en el navegador en
`http://localhost:8080` — es una copia privada, exacta a la publicada, donde se puede
revisar cualquier cambio antes de subirlo. Para detener el servidor: teclas `Ctrl+C`
en la terminal.

> **Nota sobre el acceso.** Para poder publicar (hacer `git push`) hay que tener
> permisos de colaborador en el repositorio de GitHub. Es un alta que hace el
> propietario del repositorio desde la web de GitHub (*Settings → Collaborators*) con
> el correo o usuario de GitHub de la persona editora.

---

## 6. Recetario de ediciones

Cada receta de este capítulo termina exactamente igual: **generar → verificar →
publicar** (la secuencia completa está en el capítulo 8). Aquí se detalla únicamente
el paso de edición, que es lo que cambia en cada caso.

### 6.1 Cambiar un texto o título de un servicio

Las siete páginas de servicio (Proyectos eléctricos, Estudios eléctricos, Corriente
directa, Gestión de proyectos, Construcción de data center, Ingeniería civil y
Servicios de ingeniería) se alimentan del archivo **`tools/content.py`**, en la lista
llamada `SERVICES`.

Cada servicio es un bloque con dos secciones gemelas: `"es"` (los textos en español)
y `"en"` (los mismos textos en inglés). Dentro de cada sección, los campos son:

| Campo | Qué controla en la página |
|---|---|
| `nav` | El nombre corto que aparece en el menú de navegación |
| `title` | El título de la pestaña del navegador (importante para SEO, ver 7.2) |
| `meta` | La descripción que Google muestra bajo el título en los resultados |
| `keywords` | Las palabras clave asociadas a la página |
| `h1` | El titular grande visible al entrar a la página |
| `lead` y `tagline` | Las frases de apoyo que acompañan al titular |
| `intro_h2` e `intro` | El título y el párrafo de la sección de introducción |
| `list_title` y `list` | El título y las viñetas de «Servicios especializados» |
| `benefits_title`, `benefits_intro`, `benefits` | El bloque de beneficios: su título, su párrafo y las tres tarjetas (cada una es un par título–texto) |
| `cta_title` y `cta_text` | La llamada a la acción del final de la página |

**Ejemplo completo.** Para cambiar el titular de la página de Proyectos eléctricos:

1. Abrir `tools/content.py` en el editor.
2. Buscar (Cmd+F) el texto actual: `Proyectos eléctricos integrales`.
3. En la sección `"es"` del bloque, editar solo lo que está entre comillas:

   ```python
   "h1": "Proyectos eléctricos integrales",
   ```

4. Bajar unas líneas hasta la sección `"en"` **del mismo bloque** y hacer el cambio
   equivalente en inglés.
5. Guardar, y seguir con la secuencia del capítulo 8.

**La regla de los dos idiomas.** Todo texto visible del sitio existe en español y en
inglés. Cambiar solo uno de los dos deja las versiones desincronizadas — el visitante
anglófono seguiría leyendo el texto viejo. Por eso cada receta de este capítulo
repite lo mismo: el cambio se hace **siempre en ambos idiomas**.

### 6.2 Cambiar textos de las demás páginas interiores

El resto de las páginas interiores se alimenta de **`tools/pages.py`**, organizado en
bloques con la misma lógica de secciones ES/EN:

| Bloque en `pages.py` | Página que alimenta |
|---|---|
| `ABOUT` | Nosotros / About |
| `HUBS` y `PROJECTS` | Proyectos / Projects |
| `SERVICES_INDEX` | El índice general de servicios |
| `CONTACT_PAGE` y `MX_STATES` | Contacto / Contact, incluido el formulario |
| `CAREERS` | Trabaja con nosotros / Careers |
| `BLOG` y `ARTICLES` | El índice del blog y su inventario de artículos |

El método es el mismo del punto anterior: buscar la frase actual con Cmd+F, editarla
entre comillas en español y en inglés, guardar y regenerar.

### 6.3 Cambiar la página de inicio

La página de inicio es un caso especial: se construye combinando **dos archivos**,
uno para los textos y otro para la estructura.

- **Los textos** están en **`tools/home_i18n.js`**: un diccionario `es:` y otro `en:`
  con claves de nombre descriptivo — `heroTitle` es el gran titular de la portada,
  `heroText` su párrafo, `sec1Title` el título de la primera sección, y así
  sucesivamente. Se edita el texto entre comillas, en ambos idiomas, y se regenera.
  **Este es el archivo que se toca el 95 % de las veces** que haya que cambiar algo
  del inicio.
- **La estructura** (qué secciones existen y en qué orden aparecen) está en
  **`tools/home_source.html`**. Solo se toca para cambios de maquetación del inicio,
  que conviene tratar como encargo de desarrollo, no como edición cotidiana.

El generador combina ambos archivos para producir `index.html` (español) y
`en/index.html` (inglés).

### 6.4 Cambiar teléfonos, correos, dirección o redes sociales

Todos los datos de contacto están centralizados al principio de
**`tools/content.py`**, de modo que un solo cambio se propaga a las 28 páginas al
regenerar:

- **`CONTACT`** — la dirección postal, los teléfonos, los siete correos electrónicos
  (información, ventas en español, ventas en inglés, recursos humanos, quejas,
  proveedores y talento) y el enlace de Google Maps.
- **`SOCIAL`** — los enlaces a Facebook, Instagram, LinkedIn y YouTube.
- **`WHATSAPP`** — el enlace del botón de WhatsApp, que lleva un mensaje precargado.
  Ese mensaje va *codificado para URL*: los espacios se escriben `%20` y los acentos
  como códigos. Para cambiarlo con comodidad, pedírselo a la IA (capítulo 9) o usar
  un codificador de URL en línea.
- **`PRIVACY_PDF`**, **`LOGIN_URL`** y **`VIDEO_URL`** — el aviso de privacidad, el
  portal de inicio de sesión y el video corporativo.

**Atención con los teléfonos:** cada número existe en dos entradas que deben cambiar
juntas. `phone1` es el formato visible (`81 1934 1192`) y `phone1_tel` es el formato
de marcación internacional (`+528119341192`) que usa el teléfono cuando alguien toca
el número desde el celular. Lo mismo ocurre con `phone2`/`phone2_tel` y
`mobile`/`mobile_tel`.

### 6.5 Cambiar o agregar una imagen

Las imágenes propias de Arcondec viven en `assets/images/arcondec/`, organizadas por
carpetas (el resto de `assets/images/` pertenece a la plantilla y no se toca):

| Carpeta | Contenido |
|---|---|
| `servicios/` | Las fotos de las páginas de servicio, nombradas `<clave>-N.jpg` |
| `blog/` | Las imágenes de los artículos del blog |
| `proyectos/` | Las fotos de la página de proyectos |
| `secciones/` | Fondos y fotografías de las secciones del inicio |
| `brand/` | El logotipo y los elementos de marca |
| `clients/` | Los logotipos de clientes |
| `rh/` | Las imágenes de la página de reclutamiento |

**Para reemplazar una imagen existente** (el caso más frecuente):

1. Preparar la imagen nueva: formato JPG para fotografías, comprimida (idealmente
   menos de 300 KB) y de no más de ~1600 píxeles de ancho. Una imagen de cámara sin
   comprimir puede pesar 8 MB y arruinar el tiempo de carga de la página.
2. Guardarla **con el mismo nombre de archivo y en la misma carpeta** que la imagen
   a la que sustituye.
3. Medirla: `python3 tools/measure_images.py`. Este paso actualiza el registro de
   dimensiones (`tools/image_sizes.json`) que el generador usa para reservar el
   espacio exacto de cada imagen en la página. Si se omite y la imagen nueva tiene
   otra proporción, la página «brinca» mientras carga — un defecto que además Google
   penaliza (ver 7.4).
4. Regenerar y verificar como siempre (capítulo 8).

**Para añadir una foto más a un servicio:** las fotos de servicio siguen la
convención `servicios/<clave>-N.jpg`, donde `<clave>` es el identificador del
servicio en `content.py` (`proele`, `estel`, `corac`, `gespr`, `cosdc`, `civdc`,
`ingdc`) y `N` un número. Cada servicio lista en su campo `photos` qué números
muestra. Para añadir una sexta foto a Estudios eléctricos, por ejemplo: guardar
`servicios/estel-7.jpg`, añadir el `7` a la lista `photos` del bloque `estel`, medir,
regenerar y verificar.

**Una particularidad de la caché.** Las imágenes se sirven con memoria de navegador
de un año (así el sitio vuela para el visitante recurrente). La contrapartida: si se
reemplaza una imagen conservando el nombre, quien ya visitó el sitio puede seguir
viendo la versión anterior durante un tiempo. Cuando sea importante que el cambio se
vea de inmediato, la vía segura es darle a la imagen un **nombre nuevo** y actualizar
la referencia en el archivo de contenido correspondiente.

### 6.6 Cambiar el dominio del sitio

El dominio de producción está escrito en **una sola línea** de todo el proyecto: la
constante `BASE_URL` en `tools/layout.py` (hoy, `https://grupo-arcondec.vercel.app`).

Cuando el sitio se mude a su dominio definitivo (por ejemplo, `arcondec.mx`), el
procedimiento es: cambiar esa línea, regenerar y publicar. Con eso, todas las
etiquetas de SEO que dependen del dominio — canonical, hreflang, mapa del sitio,
datos estructurados (capítulo 7) — quedan apuntando al dominio nuevo de una sola vez.
En paralelo hay que dar de alta el dominio en el panel de Vercel (*Settings →
Domains*), que es quien lo conecta con el sitio.

### 6.7 Publicar los artículos del blog

Los 12 artículos del blog están inventariados en `tools/pages.py` (lista `ARTICLES`),
cada uno con su dirección amigable, su imagen, y su título y resumen en ambos
idiomas. Hoy aparecen en el índice del blog marcados como «Próximamente».

Construir las páginas de artículo completo es la siguiente etapa del proyecto:
requiere añadir una plantilla nueva al generador, lo cual es **trabajo de
desarrollo, no de edición**. La recomendación es encargarlo como proyecto — a
JectCode o a una IA dándole este manual como contexto — y no improvisarlo, porque un
artículo de blog bien publicado necesita su propio SEO (título, descripción,
canonical, hreflang y datos estructurados de artículo).

---

## 7. El SEO del sitio y cómo mantenerlo

### 7.1 Qué es el SEO y qué se construyó aquí

**SEO** (*Search Engine Optimization*, optimización para motores de búsqueda) es el
conjunto de señales con las que Google — y, cada vez más, los buscadores con
inteligencia artificial — deciden si una página merece aparecer en los resultados y
en qué posición. En este sitio, el SEO no es un añadido: está integrado en el
generador, que escribe automáticamente en cada una de las 28 páginas:

- El **título** de la pestaña y la **meta descripción** propios de cada página y de
  cada idioma — el texto exacto con el que la página se presenta en los resultados
  de Google.
- La etiqueta **canonical**, que declara la dirección oficial de la página y evita
  que Google la considere contenido duplicado.
- Las etiquetas **hreflang**, que informan de que cada página tiene una versión
  hermana en el otro idioma. Son la razón de que Google pueda mostrar la versión en
  inglés a quien busca en inglés.
- Las etiquetas **Open Graph** y **Twitter Card**, que controlan la miniatura, el
  título y la descripción que aparecen al compartir un enlace en redes sociales o
  por WhatsApp.
- Los **datos estructurados JSON-LD**: fichas técnicas invisibles que describen a la
  organización (`Organization`), cada servicio (`Service`), la lista de proyectos
  (`ItemList`) y la ficha local con horario y coordenadas (`LocalBusiness`). Son el
  formato que leen los buscadores y los motores de respuesta con IA para «entender»
  quién es la empresa y qué ofrece.
- El **mapa del sitio** (`sitemap.xml`) con las 28 páginas y el archivo
  `robots.txt` que lo anuncia.

### 7.2 Lo que sí está en manos del editor

Aunque la maquinaria es automática, tres campos de cada página son texto redactado, y
de su calidad depende buena parte del posicionamiento. Están en los archivos de
contenido (capítulo 6) y conviene tratarlos con el mismo cuidado que un anuncio:

- **`title`** — el título de la pestaña, y el titular azul del resultado de Google.
  Lo recomendable: 50 a 60 caracteres, la palabra clave del servicio al principio,
  y la marca al final (por ejemplo: «Estudios eléctricos especializados — Grupo
  Arcondec»).
- **`meta`** — la meta descripción, el par de líneas grises bajo el titular en
  Google. Lo recomendable: 150 a 160 caracteres, redacción persuasiva y concreta
  (qué se ofrece, para quién, con qué respaldo), porque de ella depende que el
  usuario haga clic.
- **`h1`** — el titular grande de la página. Debe describir el servicio con las
  palabras que un cliente usaría para buscarlo, y **cada página tiene exactamente
  uno** (el verificador lo comprueba).

Dos hábitos completan el trabajo: que cada página conserve un `title` y una `meta`
**distintos de los de las demás** (dos páginas con el mismo título compiten entre sí
ante Google), y que los cambios se hagan siempre en los dos idiomas.

### 7.3 Lo que protege el verificador

Cada vez que se ejecuta `tools/check.py`, se comprueba automáticamente la parte del
SEO que suele romperse por accidente: que cada página tenga su título, su meta
descripción, su canonical y sus dos hreflang; que haya exactamente un `h1`; que
ninguna imagen carezca de texto alternativo (`alt`, que además de accesibilidad es
información que Google indexa); y que ningún enlace interno apunte a una página
inexistente. Por eso la regla de oro n.º 3 es innegociable: el verificador en verde
es la garantía de que una edición de textos no degradó el posicionamiento.

### 7.4 La velocidad también es SEO

Google mide la experiencia de carga real de las páginas (los llamados *Core Web
Vitals*) y la usa como factor de posicionamiento. Tres decisiones de este proyecto
trabajan a favor y conviene no deshacerlas:

- **Imágenes con dimensiones declaradas.** El registro `tools/image_sizes.json`
  permite al generador reservar el espacio exacto de cada imagen, evitando que la
  página «brinque» durante la carga (el defecto que Google llama *CLS*). Es la razón
  del paso «medir» en la receta de imágenes (6.5).
- **Imágenes comprimidas.** Una foto de 8 MB puede multiplicar por diez el tiempo de
  carga. De ahí la pauta de mantenerlas bajo ~300 KB.
- **Caché con versionado.** Los estilos y scripts llevan en su dirección una huella
  de su contenido (`?v=a1b2c3`), que el generador renueva solo cuando el archivo
  cambia. El visitante recurrente no vuelve a descargar nada que no haya cambiado, y
  aun así recibe cada novedad al instante. Es automático; se menciona para que no
  sorprenda al ver las direcciones.

---

## 8. Verificar y publicar

La secuencia completa, idéntica después de cualquier edición del capítulo 6. Desde la
carpeta del proyecto:

```bash
# 1. Regenerar el sitio
python3 tools/build.py
#    → debe terminar en: "28 páginas + sitemap.xml + robots.txt"

# 2. Verificar
python3 tools/check.py
#    → debe terminar en: "Sin problemas."

# 3. Revisar en local (recomendado)
python3 -m http.server 8080
#    → abrir http://localhost:8080 y revisar la página cambiada, en ES y en EN

# 4. Publicar
git add -A
git commit -m "Aquí una frase que describa el cambio"
git push
```

Sobre el mensaje del commit (el texto entre comillas del paso 4): es la bitácora del
proyecto. Una frase concreta — «Actualiza teléfono móvil de contacto», «Nueva foto en
Estudios eléctricos» — permite, meses después, entender el historial de un vistazo y
localizar cualquier cambio para revisarlo o revertirlo.

Tras el `git push`, Vercel publica automáticamente en uno o dos minutos. Si el
verificador reportó problemas en el paso 2, **no se publica**: el mensaje del
verificador indica la página y el defecto exactos; se corrige, se repiten los pasos
1 y 2, y solo entonces se continúa.

---

## 9. Cómo pedirle los cambios a una inteligencia artificial

Esta es, en la práctica, la manera más cómoda de operar el sitio: en lugar de editar
los archivos a mano, se le describe el cambio a un asistente de IA que trabaja sobre
el proyecto — como **Claude Code** o **Cursor** — y se supervisa el resultado. El
proyecto está preparado para ello.

### 9.1 El guardarraíl automático: CLAUDE.md

En la raíz del proyecto hay un archivo llamado **`CLAUDE.md`** que contiene las
reglas del proyecto en el formato que estos asistentes leen automáticamente al
empezar a trabajar: qué archivo controla cada cosa, qué está prohibido tocar, y que
todo cambio termina en generar + verificar. Es la versión condensada de este manual,
dirigida a las máquinas. Gracias a él, incluso un encargo mal formulado tiene red:
el asistente sabrá por su cuenta que no debe editar el HTML generado.

Ese archivo **se entrega junto con el proyecto y no debe borrarse**.

### 9.2 Las cuatro instrucciones de un buen encargo

1. **Decir qué cambiar citando el texto actual.** «El titular que hoy dice
   *Estudios eléctricos especializados* debe decir *X*» funciona siempre; «mejora el
   titular» obliga a la IA a inventar contenido que nadie aprobó.
2. **Dar el cambio en ambos idiomas** — o pedir explícitamente que la IA proponga la
   traducción al inglés y mostrarla antes de aplicar.
3. **Recordarle el flujo del proyecto:** que lea `CLAUDE.md`, que edite solo en
   `tools/`, y que regenere con el generador.
4. **Pedirle la prueba:** que ejecute el verificador y muestre que terminó en
   «Sin problemas.» antes de dar el cambio por hecho.

### 9.3 Encargos de ejemplo, listos para adaptar

> «En este proyecto los cambios se hacen en `tools/` y se regenera con
> `python3 tools/build.py` — lee `CLAUDE.md`. Cambia el titular del servicio de
> estudios eléctricos: donde dice “Estudios eléctricos especializados” debe decir
> “Estudios eléctricos certificados”, y en la versión en inglés, “Certified
> electrical studies”. Regenera, ejecuta `tools/check.py` y muéstrame que terminó
> sin problemas.»

> «Lee `CLAUDE.md`. Cambia el teléfono móvil de contacto de (55) 3032 6595 a
> (55) 1234 5678 en `tools/content.py`. Recuerda que el número tiene dos entradas:
> la visible y la de marcación con lada +52. Regenera y verifica.»

> «Lee `CLAUDE.md`. Reemplacé la foto
> `assets/images/arcondec/servicios/estel-3.jpg` por una nueva con el mismo nombre.
> Ejecuta `tools/measure_images.py`, regenera el sitio y verifica.»

> «Lee `CLAUDE.md`. Redacta una nueva meta descripción para la página de
> construcción de data centers: máximo 160 caracteres, debe mencionar “llave en
> mano” y “México”. Propónme primero la versión en español y en inglés, y espera mi
> visto bueno antes de aplicarla.»

### 9.4 Encargos mal planteados, y por qué fallan

| Encargo | Problema |
|---|---|
| «Cambia el título en `nosotros.html`» | Pide editar el HTML generado: el cambio se perderá en la siguiente regeneración |
| «Mejora los textos del sitio» | Sin texto literal ni criterio, la IA reescribe contenido oficial ya aprobado |
| «Haz que los colores resalten más» | El contraste de colores está auditado (norma de accesibilidad WCAG AA); aclararlo a ojo rompe la auditoría |
| «Quita las animaciones, que tardan» | Las salvaguardas de animación existen por accesibilidad; lo correcto es pedir el ajuste concreto que molesta |

### 9.5 Cómo revisar el trabajo de la IA sin saber programar

Tres comprobaciones antes de aceptar cualquier trabajo:

1. **`git status`** en la terminal: lista los archivos modificados. Lo correcto es
   ver archivos de `tools/` **acompañados** de las páginas HTML regeneradas. Si solo
   aparecen páginas HTML sin ningún archivo de `tools/`, la IA editó a mano lo
   generado: se rechaza el trabajo y se le pide hacerlo por la vía correcta.
2. **`python3 tools/check.py`**: debe terminar en «Sin problemas.»
3. **Revisión visual** en `http://localhost:8080`: la página cambiada, en español
   **y** en inglés.

Y la red de seguridad final: mientras no se haga `git push`, nada está publicado. Un
trabajo insatisfactorio se descarta por completo con `git checkout -- .` (que
restaura todos los archivos a su último estado confirmado) y se vuelve a empezar.

---

## 10. Lo que nunca se debe hacer

La lista roja. Todo lo demás tiene arreglo fácil; esto es lo que causa los problemas
serios:

- ✗ **Editar a mano cualquier página HTML** de la raíz o de `en/`, o los archivos
  `sitemap.xml` y `robots.txt`. Son productos del generador; se regeneran y el
  cambio se pierde.
- ✗ **Modificar los archivos de la plantilla**: `assets/css/style.css`,
  `assets/js/main.js` o la carpeta `assets/js/vendor/`.
- ✗ **Cambiar un texto en un solo idioma**, dejando la otra versión desactualizada.
- ✗ **Publicar con el verificador en rojo.**
- ✗ **Subir imágenes sin pasar por `measure_images.py`** — la página «brincará» al
  cargar y Google lo penaliza.
- ✗ **Aclarar colores de texto a ojo.** El contraste está auditado bajo la norma de
  accesibilidad WCAG AA; cualquier ajuste de color debe recalcular ese contraste.
- ✗ **Quitar las salvaguardas de `arcondec-motion.js`**: el respeto a la preferencia
  de movimiento reducido, el revelado forzoso al llegar al final de la página y la
  salida limpia cuando la biblioteca de animación no carga. Existen para que el
  contenido jamás quede oculto a ningún visitante.
- ✗ **Borrar o renombrar páginas por fuera del generador** — las etiquetas de idioma
  y el mapa del sitio quedarían apuntando a páginas inexistentes. (Si ocurre, el
  verificador lo detecta.)
- ✗ **Borrar `CLAUDE.md`**, el archivo de reglas que protege el proyecto cuando se
  trabaja con asistentes de IA.

---

## 11. Solución de problemas

| Síntoma | Causa probable y solución |
|---|---|
| Cambié un texto y no se ve en el navegador | Falta regenerar: `python3 tools/build.py`. Después, recargar el navegador forzando la caché: Cmd+Shift+R |
| Mi cambio desapareció solo | Se había editado el HTML generado y alguien regeneró el sitio. Rehacer el cambio, esta vez en el archivo de `tools/` que corresponda (capítulo 6) |
| `build.py` termina con `SyntaxError` | Al editar un archivo `.py` quedó una comilla sin cerrar o se borró una coma. El mensaje de error indica la línea exacta. Si el texto nuevo lleva comillas por dentro, usar comillas tipográficas (« » o “ ”) |
| `check.py` reporta «… roto» | Un enlace o una imagen apunta a un archivo que no existe (habitualmente, un nombre mal escrito). Corregir la ruta o colocar el archivo que falta |
| `check.py` reporta «sin hreflang» o «sin canonical» | Existe una página creada por fuera del generador. Las páginas nuevas se añaden siempre a través de `tools/` |
| La página «brinca» al cargar una imagen nueva | Faltó medir: `python3 tools/measure_images.py` y regenerar |
| `measure_images.py` falla con `No module named PIL` | Falta la biblioteca de imágenes: `pip3 install Pillow` (una sola vez) |
| Hice `git push` pero el sitio publicado no cambia | Esperar 1–2 minutos. Si persiste, revisar el panel de Vercel por si el despliegue falló. Y recordar la caché de imágenes: una imagen reemplazada con el mismo nombre puede tardar en refrescarse (ver 6.5) |
| Las animaciones no se mueven | Comprobar si el sistema operativo tiene activada la preferencia «reducir movimiento» — en ese caso el sitio se muestra estático a propósito, por accesibilidad |
| Quiero que un bloque concreto no se anime | Añadirle el atributo `data-arc-motion="off"` — en el archivo fuente de `tools/`, nunca en el HTML generado |
| Necesito volver a una versión anterior | Todo el historial está en git. Pedirle a la IA: «muéstrame el historial con `git log` y revierte el commit X», o consultarlo en la pestaña *Commits* de GitHub |

---

## 12. Referencia rápida

La tabla que resuelve el 90 % de los casos: qué archivo tocar para cada cambio.

| Quiero cambiar… | Archivo | Después |
|---|---|---|
| Texto o título de un servicio | `tools/content.py` → `SERVICES` (ES **y** EN) | generar + verificar |
| Teléfono, correo, dirección, redes, WhatsApp | `tools/content.py` → `CONTACT`, `SOCIAL`, `WHATSAPP` | generar + verificar |
| Nosotros, proyectos, contacto, empleo, blog | `tools/pages.py` (ES **y** EN) | generar + verificar |
| Textos de la página de inicio | `tools/home_i18n.js` (`es:` **y** `en:`) | generar + verificar |
| Estructura de la página de inicio | `tools/home_source.html` | generar + verificar |
| Título SEO, meta descripción, keywords | Campos `title`, `meta`, `keywords` en `content.py` / `pages.py` | generar + verificar |
| Menú, pie de página, SEO global | `tools/layout.py` | generar + verificar |
| Dominio de producción | `BASE_URL` en `tools/layout.py` + panel de Vercel | generar + verificar |
| Una imagen | `assets/images/arcondec/…` | medir + generar + verificar |
| Estilos (colores, espaciados) | `assets/css/arcondec.css` | recargar navegador |
| Animaciones | `assets/js/arcondec-motion.js` | recargar navegador |

**Los comandos, siempre en este orden:**

```bash
python3 tools/build.py      # 1. generar
python3 tools/check.py      # 2. verificar → "Sin problemas."
git add -A && git commit -m "descripción del cambio" && git push    # 3. publicar
```

---

## 13. Glosario

| Término | Significado |
|---|---|
| **Build / generar** | Ejecutar `tools/build.py` para que el generador reconstruya las 28 páginas a partir de los archivos de contenido |
| **Caché** | Memoria del navegador que guarda archivos ya descargados para no volver a pedirlos. Acelera el sitio; explica por qué a veces un cambio «no se ve» hasta forzar la recarga (Cmd+Shift+R) |
| **Canonical** | Etiqueta invisible que declara la dirección oficial de una página, para que Google no la confunda con un duplicado |
| **CLS** | *Cumulative Layout Shift*: el «brinco» de una página mientras carga. Google lo mide y lo penaliza; las dimensiones de imagen declaradas lo evitan |
| **CMS** | Sistema de gestión de contenidos (p. ej. WordPress): un panel web para editar un sitio. Este proyecto no usa uno, por las razones del capítulo 2.2 |
| **Commit** | Un cambio confirmado en el historial de git, con autor, fecha y descripción. La unidad de la bitácora del proyecto |
| **Despliegue (deploy)** | La publicación del sitio. Aquí es automática: Vercel publica cada push a GitHub en 1–2 minutos |
| **Generador** | `tools/build.py`: el programa que construye las 28 páginas a partir del contenido. La pieza central del proyecto |
| **Git** | El sistema de control de versiones: lleva el historial completo del proyecto y permite volver a cualquier estado anterior |
| **GitHub** | El servicio en la nube donde vive la copia principal del repositorio |
| **hreflang** | Etiquetas que informan a Google de que una página tiene versión en otro idioma, y dónde está |
| **HTML** | El formato de las páginas web. En este proyecto, el HTML es *producto generado*: nunca se edita a mano |
| **JSON-LD / datos estructurados** | Fichas invisibles en cada página que describen a la empresa, sus servicios y su ubicación en el formato que los buscadores y las IA leen directamente |
| **Meta descripción** | El par de líneas que Google muestra bajo el título de un resultado. Se redacta por página y por idioma (campo `meta`) |
| **Push** | Subir los commits locales a GitHub (`git push`). En este proyecto, subir es publicar |
| **Repositorio** | La carpeta del proyecto bajo control de git: el código, el contenido y todo su historial |
| **SEO** | Optimización para motores de búsqueda: todo lo que hace que el sitio aparezca bien posicionado en Google (capítulo 7) |
| **Template / plantilla** | El diseño base comercial (*aball*) sobre el que se construyó el sitio. Sus archivos no se modifican (regla de oro n.º 2) |
| **Terminal** | La aplicación donde se escriben las órdenes (`Terminal` en macOS). Aquí solo se usan los comandos listados en este manual |
| **Vercel** | El servicio que aloja y sirve el sitio publicado, conectado al repositorio de GitHub |
| **Verificador** | `tools/check.py`: el control de calidad que revisa enlaces, SEO y estructura antes de publicar |
| **WCAG AA** | Norma internacional de accesibilidad web. El contraste de colores del sitio está auditado bajo ella |

---

<div align="center">

© Grupo Arcondec S.A. de C.V. · Documento técnico elaborado por [JectCode](https://github.com/Juanescanar23)

</div>
