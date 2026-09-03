# -*- coding: utf-8 -*-
"""Generador del sitio de Grupo Arcondec.

    python3 tools/build.py

Lee los textos de content.py y pages.py, y escribe las paginas HTML en la raiz
del repositorio. El resultado es HTML estatico puro: Vercel lo sirve tal cual,
sin paso de build en el despliegue.

IMPORTANTE: las paginas generadas se sobrescriben en cada ejecucion. Si hay que
corregir un texto, se corrige en content.py / pages.py y se vuelve a ejecutar,
no editando el HTML a mano.
"""

import hashlib
import json
import pathlib
import re
import sys
from urllib.parse import quote

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import pages as P  # noqa: E402
from content import (  # noqa: E402
    CONTACT,
    PRIVACY_PDF,
    LIST_DC,
    LIST_IE,
    SERVICES,
    WHATSAPP,
)
from layout import (  # noqa: E402
    BASE_URL,
    ROUTES,
    SITEMAP_ROUTES,
    UI,
    body_open,
    commitment_band,
    e,
    footer,
    head,
    header,
    page_banner,
    sales_mail,
    url,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Dimensiones reales de cada imagen, precalculadas con tools/measure_images.py.
# Se leen de disco para no exigir Pillow en cada build.
_TAMANOS = json.loads((ROOT / "tools/image_sizes.json").read_text(encoding="utf-8"))
IMG = "/assets/images/arcondec"


def dims(src):
    """Devuelve width/height reales de la imagen para evitar saltos de maquetación.

    Declarar 1600x1200 en una foto que mide 1600x838 hace que el navegador
    reserve el hueco con la proporción equivocada y lo corrija al cargar: el
    atributo empeora el CLS en lugar de evitarlo.
    """
    par = _TAMANOS.get(src)
    return 'width="%d" height="%d"' % tuple(par) if par else ""


_HUELLAS = {}
_ASSET_RE = re.compile(r'(src|href)="(/assets/(?:css|js)/[^"?#]+)"')


def _huella(ruta):
    """Ocho caracteres del hash del archivo, o None si no está en disco."""
    if ruta not in _HUELLAS:
        archivo = ROOT / ruta.lstrip("/")
        try:
            digest = hashlib.sha1(archivo.read_bytes()).hexdigest()[:8]
        except OSError:
            digest = None
        _HUELLAS[ruta] = digest
    return _HUELLAS[ruta]


def versionar(html):
    """Pone el hash del contenido en la URL de cada CSS y JS.

    vercel.json sirve `assets/css` y `assets/js` con `max-age=3600`, así que tras
    un despliegue un visitante recurrente podía pasarse hasta una hora con el HTML
    nuevo y los estilos viejos —el sitio parecía no haber cambiado—. Con el hash
    en la URL, cada versión estrena dirección y el navegador la pide en cuanto
    llega; mientras el archivo no cambie, la caché larga sigue trabajando igual.
    Las imágenes y las fuentes se quedan como están: no cambian nunca.
    """

    def sustituye(m):
        atributo, ruta = m.group(1), m.group(2)
        digest = _huella(ruta)
        if not digest:
            return m.group(0)
        return '%s="%s?v=%s"' % (atributo, ruta, digest)

    return _ASSET_RE.sub(sustituye, html)


def write(path, content):
    dest = ROOT / path.lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(versionar(content), encoding="utf-8")
    return dest


# ==========================================================================
# PAGINA DE SERVICIO
# ==========================================================================
def render_service(svc, lang):
    c = svc[lang]
    key = "srv-" + svc["key"]
    photos = ["%s/servicios/%s-%d.jpg" % (IMG, svc["key"], n) for n in svc["photos"]]
    t = UI[lang]

    # Viñetas de "Servicios especializados" con el modelo de tarjeta de
    # services-2.html del template: círculo con icono, título y el punteado.
    ICONOS_SPEC = [
        "fal fa-bolt", "fal fa-cogs", "fal fa-drafting-compass",
        "fal fa-clipboard-check", "fal fa-shield-check", "fal fa-server",
        "fal fa-network-wired", "fal fa-tools", "fal fa-battery-bolt",
        "fal fa-project-diagram",
    ]
    items = "\n".join(
        """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="service-2-item arc-spec text-center mt-30 animated wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="%dms">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>"""
        % ((n % 3) * 150, ICONOS_SPEC[n % len(ICONOS_SPEC)], e(x), (n % 6) + 1)
        for n, x in enumerate(c["list"])
    )

    benefits = "\n".join(
        """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="service-2-item text-center mt-30 animated wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="%dms">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <p>%s</p>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>"""
        % (n * 150, icon, e(title), e(text), n + 4)
        for n, ((title, text), icon) in enumerate(
            zip(c["benefits"], ["fal fa-headset", "fal fa-bolt", "fal fa-shield-check"])
        )
    )

    gallery = "\n".join(
        """                <div class="col-lg-4 col-md-6">
                    <div class="portfolio-style-2-item portfolio-style-3-item mt-30">
                        <img src="%s" alt="%s" loading="lazy" %s>
                    </div>
                </div>"""
        % (src, e("%s — Grupo Arcondec" % c["h1"]), dims(src))
        for src in photos
    )

    # Enlaces al resto de servicios, para que ninguna pagina sea un callejon sin salida
    others = "\n".join(
        """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <a class="service-2-item arc-spec text-center mt-30" href="%s">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </a>
                </div>"""
        % (url("srv-" + o["key"], lang), o["icon"], e(o[lang]["nav"]), (n % 6) + 1)
        for n, o in enumerate(o for o in SERVICES if o["key"] != svc["key"])
    )

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": c["h1"],
        "name": c["title"],
        "description": c["meta"],
        "provider": {"@type": "Organization", "name": "Grupo Arcondec S.A. de C.V."},
        "areaServed": {"@type": "Country", "name": "México"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": c["list_title"],
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": x}}
                for x in c["list"]
            ],
        },
    }

    body = """
    <main id="contenido">

    <!--====== INTRO ======-->

    <section class="about-2-area about-11-area pt-90 pb-60">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="about-2-content about-11-content mt-30">
                        <span class="service-eyebrow">{eyebrow}</span>
                        <h2 class="title">{intro_h2}</h2>
                        <p>{intro}</p>
                        <a class="main-btn main-btn-3 mt-30" href="{contact}">{contact_label}</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="about-2-thumb about-11-thumb mt-30">
                        <div class="thumb text-right">
                            <img src="{photo1}" alt="{alt}" %s>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--====== SERVICIOS ESPECIALIZADOS ======-->

    <section class="service-area service-page-area pb-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{list_title}</h2>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center arc-service-grid">
{items}
            </div>
        </div>
    </section>

    <!--====== BENEFICIOS ======-->

    <section class="service-area service-page-area arc-soft-area pt-90 pb-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{benefits_title}</h2>
                        <div class="text">
                            <p>{benefits_intro}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center arc-service-grid">
{benefits}
            </div>
        </div>
    </section>

    <!--====== GALERÍA ======-->

    <section class="portfolio-style-3-area pt-90 pb-90">
        <div class="container">
            <div class="row">
{gallery}
            </div>
        </div>
    </section>

    <!--====== CTA ======-->

    <section class="pb-90">
        <div class="container">
            <div class="arc-cta">
                <div class="row align-items-center">
                    <div class="col-lg-8">
                        <h2 class="title h3">{cta_title}</h2>
                        <p>{cta_text}</p>
                    </div>
                    <div class="col-lg-4 text-lg-right">
                        <a class="main-btn" href="{wa}" target="_blank" rel="noopener">{advisor}</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--====== OTROS SERVICIOS ======-->

    <section class="service-area service-page-area arc-soft-area pt-90 pb-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{others_title}</h2>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center arc-service-grid">
{others}
            </div>
        </div>
    </section>

    </main>
""".format(
        eyebrow=e(c["tagline"]),
        intro_h2=e(c["intro_h2"]),
        intro=e(c["intro"]),
        contact=url("contact", lang),
        contact_label=e(t["nav_contact"]),
        photo1=photos[0],
        alt=e(c["h1"]),
        list_title=e(c["list_title"]),
        items=items,
        benefits_title=e(c["benefits_title"]),
        benefits_intro=e(c["benefits_intro"]),
        benefits=benefits,
        gallery=gallery,
        cta_title=e(c["cta_title"]),
        cta_text=e(c["cta_text"]),
        wa=WHATSAPP,
        advisor=e(t["advisor"]),
        others_title=e("Otros servicios" if lang == "es" else "Other services"),
        others=others,
    )

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image=photos[0],
            extra_ld=faq_ld,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(lang=lang, title=c["h1"], crumb=c["nav"], bg=photos[0])
        + '\n    <p class="service-lead-strip">%s</p>\n' % e(c["lead"])
        + body
        + commitment_band(lang)
        + footer(lang=lang, key=key)
    )


# ==========================================================================
# SERVICIOS (índice) — modelo services-2.html del template aball
# ==========================================================================
def render_services_index(lang):
    c = P.SERVICES_INDEX[lang]
    key = "services"

    # Rejilla de tarjetas idéntica a la del template: col-lg-4 col-md-6 col-sm-6
    # con .service-2-item, icono en círculo, título, texto y el punteado .service-dot.
    cards = []
    for n, svc in enumerate(SERVICES):
        sc = svc[lang]
        cards.append(
            """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <a class="service-2-item text-center mt-30 animated wow fadeInUp" href="%s" data-wow-duration="1000ms" data-wow-delay="%dms">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <p>%s</p>
                        <span class="service-more">%s <i class="fal fa-arrow-right"></i></span>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </a>
                </div>"""
            % (
                url("srv-" + svc["key"], lang),
                (n % 3) * 150,
                svc["icon"],
                e(sc["nav"]),
                e(sc["lead"]),
                e(c["more"]),
                (n % 6) + 1,
            )
        )

    ld = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": c["h1"],
        "numberOfItems": len(SERVICES),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": svc[lang]["nav"],
                "url": BASE_URL + url("srv-" + svc["key"], lang),
            }
            for i, svc in enumerate(SERVICES)
        ],
    }

    body = """
    <main id="contenido">

    <!--====== INTRO ======-->

    <section class="pt-90 pb-30">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-9">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{intro_title}</h2>
                        <div class="text">
                            <p>{intro}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--====== SERVICIOS ======-->

    <section class="service-area service-page-area pb-100">
        <div class="container">
            <div class="row justify-content-center arc-service-grid">
{cards}
            </div>
        </div>
    </section>

    </main>
""".format(intro_title=e(c["intro_title"]), intro=e(c["intro"]), cards="\n".join(cards))

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image="%s/servicios/proele-7.jpg" % IMG,
            extra_ld=ld,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang, title=c["h1"], crumb=c["title"],
            bg="%s/servicios/proele-7.jpg" % IMG,
        )
        + '\n    <p class="service-lead-strip">%s</p>\n' % e(c["lead"])
        + body
        + commitment_band(lang)
        + footer(lang=lang, key=key)
    )


# ==========================================================================
# NOSOTROS
# ==========================================================================
def render_about(lang):
    c = P.ABOUT[lang]
    key = "about"
    t = UI[lang]

    history = "\n".join("                        <p>%s</p>" % e(p) for p in c["history"])

    # "Qué nos distingue" adopta el lenguaje de tarjeta de las páginas de
    # servicio (.service-2-item): mismo componente, para que Nosotros se lea
    # como parte de la misma familia visual que Servicios. Sin párrafo por
    # tarjeta —no hay una frase propia por palabra clave en el contenido
    # original—, así que usa la variante "arc-spec" (icono + título).
    DISTINCT_ICONS = ["fal fa-handshake", "fal fa-bullseye-arrow", "fal fa-binoculars"]
    distinct_cards = "\n".join(
        """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="service-2-item arc-spec text-center mt-30">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>"""
        % (DISTINCT_ICONS[n % len(DISTINCT_ICONS)], e(k), (n % 6) + 1)
        for n, k in enumerate(c["distinct_keywords"])
    )

    # Propósito/Meta/Visión dejan la banda oscura de manifiesto por el mismo
    # lenguaje de tarjeta .service-2-item: icono en círculo + título + texto.
    MV_ICONS = {"meta": "fal fa-bullseye-arrow", "vision": "fal fa-eye"}
    def _mv_card(n, key, title, text):
        return (
            """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="service-2-item text-center mt-30">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <p>%s</p>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>"""
            % (MV_ICONS[key], e(title), e(text), (n % 6) + 1)
        )

    mv_cards = "\n".join([
        _mv_card(0, "meta", c["meta_title"], c["meta_text"]),
        _mv_card(1, "vision", c["vision_title"], c["vision"]),
    ])

    # Valores: en es, cada renglón es (letra, resto de la palabra) y la letra
    # arma el acróstico IDEAS. En en no hay acróstico que traducir, así que el
    # marcador es solo la primera letra de la palabra completa. La letra vive
    # en el mismo círculo que llevaría un ícono fa en cualquier otra tarjeta
    # .service-2-item — incluye el mismo lenguaje visual, cambia el contenido
    # del círculo. La palabra completa es el título; no es texto duplicado
    # para quien usa lector de pantalla porque la letra va aria-hidden.
    def _value_card(n, v):
        if isinstance(v, tuple):
            letter, rest = v
            mark = e(letter)
            full = e(letter + rest)
        else:
            mark = e(v[0])
            full = e(v)
        return (
            """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="service-2-item arc-spec text-center mt-30">
                        <div class="icon"><span class="arc-mv-letter" aria-hidden="true">%s</span></div>
                        <h3 class="title">%s</h3>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>"""
            % (mark, full, (n % 6) + 1)
        )

    values = "\n".join(_value_card(n, v) for n, v in enumerate(c["values"]))

    # Certificaciones: la misma tarjeta .service-2-item de Servicios
    # (icono en círculo + título + párrafo), no ya la insignia con sello
    # propia. El campo `icon` llevaba definido desde antes sin usarse; el
    # quinto valor (sello tipográfico) ya no hace falta con este lenguaje.
    certs = "\n".join(
        """                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="service-2-item text-center mt-30">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <p><strong>%s.</strong> %s</p>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>"""
        % (icon, e(name), e(scope), e(text), (n % 6) + 1)
        for n, (name, scope, text, icon, _seal) in enumerate(c["certs"])
    )

    body = """
    <main id="contenido">

    <!--====== 1 · HISTORIA ======-->

    <section class="arc-about-story">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="arc-story-copy">
                        <span class="arc-story-year" aria-hidden="true">1991</span>
                        <span class="service-eyebrow">{history_eyebrow}</span>
                        <h2 class="arc-h2">{history_title}</h2>
{history}
                        <a class="main-btn main-btn-3 mt-30" href="{projects}">{projects_label}</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="arc-story-media mt-30">
                        <div class="arc-story-frame">
                            <img src="{img}/rh/historia-3.jpg" alt="{alt_historia}" {dims_historia}>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--====== 2 · PROPÓSITO, META Y VISIÓN ======-->
    <!-- Mismo lenguaje que Servicios: título+intro centrados y grid de
         tarjetas .service-2-item. La banda oscura de manifiesto se dejó por
         consistencia con el resto del sitio. -->

    <section class="service-area service-page-area arc-soft-area pt-90 pb-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <span class="service-eyebrow">{purpose_title}</span>
                        <h2 class="title">{purpose}</h2>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center arc-service-grid">
{mv_cards}
            </div>
        </div>
    </section>

    <!--====== 2b · VALORES ======-->

    <section class="service-area service-page-area pt-90 pb-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{values_title}</h2>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center arc-service-grid">
{values}
            </div>
        </div>
    </section>

    <!--====== 3 · QUÉ NOS DISTINGUE ======-->
    <!-- Mismo lenguaje que las páginas de Servicios: título+intro centrados
         (.section-title-9) y grid de tarjetas .service-2-item, para que
         Nosotros se lea como parte de la misma familia visual del sitio. -->

    <section class="service-area service-page-area arc-soft-area pt-90 pb-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{distinct_title}</h2>
                        <div class="text">
                            <p>{distinct_intro}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center arc-service-grid">
{distinct_cards}
            </div>
        </div>
    </section>

    <!--====== 4 · CERTIFICACIONES ======-->

    <section class="service-area service-page-area pt-90 pb-100">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{certs_title}</h2>
                        <div class="text">
                            <p>{certs_lead}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center arc-service-grid">
{certs}
            </div>
        </div>
    </section>

    </main>
""".format(
        history_title=e(c["history_title"]),
        history_eyebrow=e(c["history_eyebrow"]),
        history=history,
        projects=url("projects", lang),
        projects_label=e(t["nav_projects"]),
        img=IMG,
        alt_historia=e(c["alt_historia"]),
        dims_historia=dims("%s/rh/historia-3.jpg" % IMG),
        mv_cards=mv_cards,
        purpose_title=e(c["purpose_title"]),
        purpose=e(c["purpose"]),
        distinct_title=e(c["distinct_title"]),
        distinct_intro=e(c["distinct_quote"] + " " + c["distinct_rest"]),
        distinct_cards=distinct_cards,
        values_title=e(c["values_title"]),
        values=values,
        certs_title=e(c["certs_title"]),
        certs_lead=e(c["certs_lead"]),
        certs=certs,
    )

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image="%s/rh/historia-2.jpg" % IMG,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(lang=lang, title=c["h1"], crumb=c["eyebrow"], bg="%s/rh/historia-2.jpg" % IMG)
        + body
        + commitment_band(lang)
        + footer(lang=lang, key=key)
    )

def render_projects(lang):
    c = P.PROJECTS[lang]
    key = "projects"

    stats = "\n".join(
        """                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="overview-counter-item text-center mt-30">
                        <span class="arc-counter-pre">%s</span>
                        <h3 class="title">+<span class="arc-count" data-count="%s">0</span></h3>
                        <p>%s</p>
                    </div>
                </div>"""
        % (e(pre), value, e(label))
        for value, label, pre in c["stats"]
    )

    # La leyenda va siempre visible (no solo en :hover): en movil no hay hover
    # y el nombre del hub es informacion, no decoracion.
    # La tarjeta se envuelve en <a> solo cuando el proyecto está publicado.
    # Mientras no tenga información real sigue siendo una tarjeta informativa
    # sin enlace: nadie llega a una página vacía.
    def _tarjeta(h):
        name, loc, img = h["nombre"], h.get("ubicacion", ""), h["foto"]
        interior = """                        <div class="arc-project-thumb">
                            <img src="%s/proyectos/%s" alt="%s, %s" loading="lazy" %s>
                        </div>
                        <div class="arc-project-caption">
                            <h3 class="title h5">%s</h3>
                            <span>%s</span>
                        </div>""" % (
            IMG, img, e(name), e(loc),
            dims("%s/proyectos/%s" % (IMG, img)), e(name), e(loc),
        )
        if h.get("publicado"):
            cuerpo = ('<a class="arc-project is-link mt-30" href="%s">\n%s\n'
                      '                    </a>'
                      % (url("prj-" + h["slug"]["es"], lang), interior))
        else:
            cuerpo = ('<div class="arc-project mt-30">\n%s\n'
                      '                    </div>' % interior)
        return ('                <div class="col-lg-4 col-md-6">\n'
                '                    %s\n                </div>' % cuerpo)

    hubs = "\n".join(
        _tarjeta(h) for h in P.HUBS
    )

    ld = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": c["h1"],
        "numberOfItems": len(P.HUBS),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "item": {"@type": "Place", "name": h["nombre"],
                         "address": h.get("ubicacion", "")},
            }
            for i, h in enumerate(P.HUBS)
        ],
    }

    body = """
    <main id="contenido">

    <!--====== CIFRAS ======-->

    <section class="arc-soft-area pt-90 pb-60">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{stats_title}</h2>
                    </div>
                </div>
            </div>
            <div class="row">
{stats}
            </div>
        </div>
    </section>

    <!--====== HUBS ======-->

    <section class="portfolio-style-3-area pt-100 pb-90">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center mb-50">
                        <span class="service-eyebrow">{hubs_eyebrow}</span>
                        <h2 class="title">{hubs_title}</h2>
                        <div class="text">
                            <p>{hubs_intro}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
{hubs}
            </div>
        </div>
    </section>

    </main>
""".format(
        stats_title=e(c["stats_title"]),
        stats=stats,
        hubs_eyebrow=e(c["hubs_eyebrow"]),
        hubs_title=e(c["hubs_title"]),
        hubs_intro=e(c["hubs_intro"]),
        hubs=hubs,
    )

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image="%s/proyectos/arcondec-propyectos-banner.jpg" % IMG,
            extra_ld=ld,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang,
            title=c["h1"],
            crumb=c["eyebrow"],
            bg="%s/proyectos/arcondec-propyectos-banner.jpg" % IMG,
        )
        + '\n    <p class="service-lead-strip">%s</p>\n' % e(c["lead"])
        + body
        + commitment_band(lang)
        + footer(
            lang=lang, key=key, extra_scripts=("/assets/js/arcondec-counters.js",)
        )
    )


# ==========================================================================
# DETALLE DE PROYECTO
# --------------------------------------------------------------------------
# Una sola plantilla para los 16 hubs. Todo cambio de maquetación se hace aquí
# y se propaga a las 32 páginas (16 ES + 16 EN) al correr build.py.
#
# Regla de oro: cada bloque se dibuja solo si trae datos. Un proyecto del que
# solo se sabe el nombre y la ubicación produce una página corta pero completa,
# sin huecos ni encabezados sueltos sobre secciones vacías. Así se pueden ir
# llenando los proyectos de uno en uno sin tocar código.
# ==========================================================================
def render_project(hub, lang, anterior, siguiente):
    c = P.PROJECT_UI[lang]
    key = "prj-" + hub["slug"]["es"]
    nombre = hub["nombre"]
    ubicacion = hub.get("ubicacion", "")
    foto = "%s/proyectos/%s" % (IMG, hub["foto"])

    # ======================================================================
    # COLUMNA IZQUIERDA — el relato
    # ======================================================================
    relato = []

    if hub.get("titulo"):
        relato.append('                        <h2 class="title arc-case-title">%s</h2>'
                      % e(hub["titulo"]))
    # Imagen destacada, justo debajo del título y antes de cualquier texto.
    # Va en su propio campo y no reutiliza `foto` —que es el fondo del banner—
    # para poder cambiar una sin tocar la otra, como ya se hace en el resto
    # del sitio.
    if hub.get("imagen"):
        relato.append(
            '                        <figure class="arc-case-figure">\n'
            '                            <img src="%s/proyectos/%s" alt="%s" %s>\n'
            "                        </figure>"
            % (IMG, hub["imagen"], e(hub.get("imagen_alt") or nombre),
               dims("%s/proyectos/%s" % (IMG, hub["imagen"])))
        )

    if hub.get("subtitulo"):
        relato.append('                        <p class="arc-case-lead">%s</p>'
                      % e(hub["subtitulo"]))

    for parrafo in hub.get("descripcion", []):
        relato.append("                        <p>%s</p>" % e(parrafo))

    if hub.get("reto"):
        relato.append('                        <h3 class="title h4 arc-case-h">%s</h3>'
                      % e(c["reto_title"]))
        relato.append("                        <p>%s</p>" % e(hub["reto"]))

    # Cada disciplina es un párrafo con su nombre en negritas: dentro de un
    # artículo se lee mejor así que como rejilla de tarjetas, que competiría
    # visualmente con la columna de datos de la derecha.
    if hub.get("solucion"):
        relato.append('                        <h3 class="title h4 arc-case-h">%s</h3>'
                      % e(c["solucion_title"]))
        for disciplina, detalle in hub["solucion"]:
            relato.append(
                '                        <p class="arc-case-discipline">'
                "<strong>%s.</strong> %s</p>" % (e(disciplina), e(detalle))
            )

    if hub.get("galeria"):
        # Cada entrada puede ser el nombre del archivo a secas o una pareja
        # (archivo, texto alternativo). Con cuatro fotos repitiendo el mismo
        # alt, un lector de pantalla oye "HUB Apodaca" cuatro veces y no
        # aprende nada; describir cada una es lo que hace útil la galería.
        def _foto(entrada):
            if isinstance(entrada, (tuple, list)):
                archivo, alt = entrada
            else:
                archivo, alt = entrada, nombre
            return """                            <div class="col-md-6">
                                <div class="arc-project-thumb mt-30">
                                    <img src="%s/proyectos/%s" alt="%s" loading="lazy" %s>
                                </div>
                            </div>""" % (IMG, archivo, e(alt),
                                         dims("%s/proyectos/%s" % (IMG, archivo)))

        fotos = "\n".join(_foto(entrada) for entrada in hub["galeria"])
        relato.append(
            '                        <h3 class="title h4 arc-case-h">%s</h3>\n'
            '                        <div class="row">\n%s\n                        </div>'
            % (e(c["galeria_title"]), fotos)
        )

    # Sin nada que contar, la columna izquierda no se queda muda: se dice lo
    # único que se sabe con certeza —dónde está la obra— en vez de dejar un
    # bloque en blanco al lado de la columna de datos.
    if not relato:
        relato.append('                        <p class="arc-case-lead">%s</p>'
                      % e(ubicacion or nombre))

    # ======================================================================
    # COLUMNA DERECHA — los datos
    # ======================================================================
    aside = []

    # --- Ficha técnica ---
    # El cliente es el único campo con lógica propia: bajo NDA no se nombra,
    # se muestra "Cliente confidencial" y el sector queda como única pista.
    filas = []
    if hub.get("cliente"):
        filas.append((c["cliente"], hub["cliente"]))
    elif hub.get("sector"):
        filas.append((c["cliente"], c["cliente_nda"]))
    for campo in ("sector", "ubicacion_exacta", "tipo_obra", "superficie",
                  "capacidad", "duracion", "entrega", "certificacion"):
        if hub.get(campo):
            filas.append((c[campo], hub[campo]))

    if filas:
        celdas = "\n".join(
            """                            <div class="arc-fact">
                                <span class="arc-fact-label">%s</span>
                                <span class="arc-fact-value">%s</span>
                            </div>""" % (e(etiqueta), e(valor))
            for etiqueta, valor in filas
        )
        aside.append(
            """                    <div class="arc-aside-card">
                        <h3 class="title h5 arc-aside-title">%s</h3>
                        <div class="arc-facts">
%s
                        </div>
                    </div>""" % (e(c["sheet_title"]), celdas)
        )

    # --- Alcances ---
    if hub.get("alcances"):
        items = "\n".join(
            "                            <li>%s</li>" % e(a)
            for a in hub["alcances"]
        )
        aside.append(
            """                    <div class="arc-aside-card">
                        <h3 class="title h5 arc-aside-title">%s</h3>
                        <ul class="arc-scope">
%s
                        </ul>
                    </div>""" % (e(c["alcances_title"]), items)
        )

    # --- Resultados ---
    if hub.get("resultados"):
        cifras = "\n".join(
            """                            <div class="arc-result">
                                <span class="arc-result-figure">%s</span>
                                <span class="arc-result-label">%s</span>
                            </div>""" % (e(cifra), e(etiqueta))
            for cifra, etiqueta in hub["resultados"]
        )
        aside.append(
            """                    <div class="arc-aside-card">
                        <h3 class="title h5 arc-aside-title">%s</h3>
                        <div class="arc-results">
%s
                        </div>
                    </div>""" % (e(c["resultados_title"]), cifras)
        )

    # Sin datos no hay barra lateral, y entonces el artículo ocupa el ancho
    # completo en vez de dejar media pantalla vacía a la derecha.
    if aside:
        ancho_relato = "col-lg-8"
        columna_datos = """                <div class="col-lg-4">
                    <aside class="arc-case-aside">
%s
                    </aside>
                </div>
""" % "\n".join(aside)
    else:
        ancho_relato = "col-lg-10"
        columna_datos = ""

    # La columna de datos va PRIMERO en el HTML, así que queda a la izquierda
    # y el artículo a la derecha. Al apilarse en móvil el orden se conserva:
    # ficha técnica arriba, relato debajo.
    articulo = """
    <section class="pt-90 pb-90">
        <div class="container">
            <div class="row justify-content-center">
%s                <div class="%s">
                    <article class="arc-case">
%s
                    </article>
                </div>
            </div>
        </div>
    </section>
""" % (columna_datos, ancho_relato, "\n".join(relato))

    # ======================================================================
    # Navegación entre proyectos, en su propia sección al pie
    # ======================================================================
    # Una página publicada nunca enlaza a una que no lo está: mandar a un
    # visitante a un proyecto vacío es peor que no ofrecerle el enlace. Pero
    # entre páginas sin publicar sí se enlaza, para poder recorrer y revisar
    # la maquetación completa antes de que haya contenido real.
    en_revision = not hub.get("publicado")

    def enlace(vecino, etiqueta, clase, flecha):
        if not vecino:
            return ""
        if not vecino.get("publicado") and not en_revision:
            return ""
        return """                <a class="arc-prevnext-link %s" href="%s">
                    <span class="arc-prevnext-arrow" aria-hidden="true">%s</span>
                    <span class="arc-prevnext-text">
                        <span class="arc-prevnext-label">%s</span>
                        <span class="arc-prevnext-name">%s</span>
                    </span>
                </a>""" % (clase, url("prj-" + vecino["slug"]["es"], lang),
                           flecha, e(etiqueta), e(vecino["nombre"]))

    navegacion = """
    <section class="arc-soft-area pt-60 pb-60">
        <div class="container">
            <div class="arc-prevnext">
%s
                <a class="arc-prevnext-all" href="%s">%s</a>
%s
            </div>
        </div>
    </section>
""" % (enlace(anterior, c["prev"], "is-prev", "←"), url("projects", lang),
       e(c["back"]), enlace(siguiente, c["next"], "is-next", "→"))

    body = '\n    <main id="main">\n' + articulo + navegacion + "\n    </main>\n"

    # JSON-LD: el proyecto se declara como obra realizada por Arcondec, que es
    # lo que un buscador puede entender de un caso de obra.
    ld = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": nombre,
        "about": ubicacion,
        "creator": {"@type": "Organization", "name": "Grupo Arcondec S.A. de C.V."},
    }

    return (
        head(
            lang=lang,
            key=key,
            title=nombre.title(),
            description=hub.get("subtitulo")
            or c["meta_tpl"] % (nombre.title(), ubicacion or "México"),
            og_image=foto,
            extra_ld=ld,
            noindex=not hub.get("publicado"),
        )
        + body_open()
        + header(lang=lang, key="projects")
        + page_banner(
            lang=lang,
            title=nombre,
            crumb=nombre.title(),
            parent=(c["crumb"], url("projects", lang)),
            bg=foto,
        )
        + body
        + commitment_band(lang)
        + footer(lang=lang, key=key)
    )



# ==========================================================================
# CONTACTO
# ==========================================================================
def render_contact(lang):
    c = P.CONTACT_PAGE[lang]
    key = "contact"

    def options(placeholder, values):
        out = ['<option value="">%s</option>' % e(placeholder)]
        out += ['<option value="%s">%s</option>' % (e(v), e(v)) for v in values]
        return "\n                                        ".join(out)

    def mail_items(pares):
        return "\n".join(
            '                            <li><span>%s:</span> <a href="mailto:%s">%s</a></li>'
            % (e(label), addr, addr)
            for label, addr in pares
        )

    # Los cuatro buzones, en una sola tarjeta y etiquetados por área: repartirlos
    # en dos paneles distintos obligaba a buscar en dos sitios.
    mails = mail_items(c["mails"])

    # Un número por línea, con su propio tel:. Antes «Oficina» anunciaba dos
    # números y marcaba solo el primero, y el móvil salía repetido en «Oficina» y
    # en «Celular». La fuente es content.py, la misma que la barra y el pie.
    phones = "\n".join(
        '                            <li><a href="tel:%s">%s</a></li>' % (tel, e(txt))
        for tel, txt in (
            (CONTACT["phone1_tel"], CONTACT["phone1"]),
            (CONTACT["phone2_tel"], CONTACT["phone2"]),
            (CONTACT["mobile_tel"], CONTACT["mobile"]),
        )
    )

    ld = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Grupo Arcondec S.A. de C.V.",
        "image": BASE_URL + "/assets/images/arcondec/brand/logo.png",
        "telephone": "+52-81-1934-1192",
        "email": CONTACT["mail_info"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CONTACT["street"],
            "addressLocality": CONTACT["city"],
            "addressRegion": CONTACT["region"],
            "postalCode": CONTACT["zip"],
            "addressCountry": "MX",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 25.7124378, "longitude": -100.3761168},
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "09:00",
            "closes": "18:00",
        },
    }

    body = """
    <main id="contenido">

    <!--====== DOS BLOQUES: FORMULARIO Y VÍAS DIRECTAS ======-->
    <!--
        Un solo bloque de contacto con dos mitades, y el mapa grande al cierre.

        El orden del DOM pone las vías directas PRIMERO y `order-lg-*` las manda a
        la derecha en escritorio. Así en el móvil, donde las columnas se apilan, se
        llega a un teléfono en la primera pantalla en vez de detrás de los nueve
        campos del formulario (antes: 2,8 pantallas de scroll), y en escritorio se
        lee lo de siempre: formulario a la izquierda, datos a la derecha.

        La columna de datos es más corta que el formulario —700px frente a 1100—,
        así que se queda pegada al hacer scroll en vez de dejar 400px de blanco al
        lado del botón de envío, que fue el problema del primer intento.
    -->

    <section class="arc-soft-area pt-90 pb-90">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title h3">{direct_title}</h2>
                        <div class="text"><p>{direct_text}</p></div>
                    </div>
                </div>
            </div>
            <div class="row">

                <div class="col-lg-5 order-lg-2">
                    <div class="arc-contact-aside">

                        <div class="arc-panel arc-links mt-30">
                            <h3 class="title h4">{call_title}</h3>
                            <p>{call_note}</p>
                            <ul>
{phones}
                            </ul>
                            <p class="arc-hours">{hours_text}</p>
                        </div>

                        <div class="arc-panel arc-links mt-30">
                            <h3 class="title h4">{wa_title}</h3>
                            <p>{wa_note}</p>
                            <a class="main-btn" href="{wa}" target="_blank" rel="noopener">{wa_btn}</a>
                        </div>

                        <div class="arc-panel arc-links mt-30">
                            <h3 class="title h4">{mail_title}</h3>
                            <p>{mail_note}</p>
                            <ul>
{mails}
                            </ul>
                        </div>

                    </div>
                </div>

                <div class="col-lg-7 order-lg-1">
                    <div class="contact-us-box mt-30">
                        <h2 class="title h3">{form_title}</h2>
                        <p>{form_note}</p>
                        <p class="form-required-note">{required_note}</p>
                        <form action="mailto:{sales}" method="post" enctype="text/plain" class="mt-30" aria-label="{form_title}">
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-name">{f_name} <span class="req">*</span></label>
                                        <input id="f-name" type="text" name="nombre" autocomplete="name" required aria-required="true">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-email">{f_email} <span class="req">*</span></label>
                                        <input id="f-email" type="email" name="correo" autocomplete="email" required aria-required="true">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-phone">{f_phone}</label>
                                        <input id="f-phone" type="tel" name="telefono" autocomplete="tel" inputmode="numeric" maxlength="10" pattern="[0-9]{{10}}" title="{phone_hint}">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-company">{f_company}</label>
                                        <input id="f-company" type="text" name="empresa" autocomplete="organization">
                                    </div>
                                </div>
                                <!-- El motivo va a ancho completo: es la pregunta que
                                     de verdad cualifica, y así las siete casillas
                                     forman filas completas sin dejar ninguna huérfana
                                     (antes «Giro» se quedaba solo con 269px de hueco). -->
                                <div class="col-md-12">
                                    <div class="input-box mt-20">
                                        <label for="f-reason">{f_reason_label} <span class="req">*</span></label>
                                        <select id="f-reason" name="motivo" required aria-required="true">
                                        {reasons}
                                        </select>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-state">{f_state_label}</label>
                                        <select id="f-state" name="estado" autocomplete="address-level1">
                                        {states}
                                        </select>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-sector">{f_sector_label} <span class="req">*</span></label>
                                        <select id="f-sector" name="giro" required aria-required="true">
                                        {sectors}
                                        </select>
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <div class="input-box mt-20">
                                        <label for="f-message">{f_message} <span class="req">*</span></label>
                                        <textarea id="f-message" name="mensaje" rows="5" required aria-required="true"></textarea>
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <p class="form-legal mt-20">{legal_pre}<a href="{privacy_url}" target="_blank" rel="noopener">{privacy_label}</a>{legal_post}</p>
                                    <div class="input-box mt-20">
                                        <button class="main-btn" type="submit">{f_submit}</button>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!--====== MAPA ======-->
    <!--
        El mapa vivía dentro de un panel de la columna lateral: 300px de alto en
        una caja de 420px de ancho, donde no se distinguen ni las calles.
        Fondo blanco, no arc-soft-area: va detrás de la banda del formulario, que
        ya es suave, y dos bandas iguales seguidas suman sus rellenos y dejan un
        hueco muerto en medio (el mismo fallo que había en Nosotros).
    -->

    <section class="pt-90 pb-90">
        <div class="container">
            <!-- La dirección y el botón van en el encabezado, no en un panel
                 aparte: así el mapa se queda con todo el ancho y la sección es un
                 solo bloque en vez de dos. -->
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <h2 class="title">{map_title}</h2>
                        <div class="text">
                            <p>{addr_text}</p>
                            <p class="arc-hours">{hours_text}</p>
                        </div>
                        <a class="main-btn mt-20" href="{maps}" target="_blank" rel="noopener">{directions_btn}</a>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <div class="contact-map mt-40">
                        <iframe title="{map_iframe_title}" src="https://www.google.com/maps?q=Grupo+Arcondec+Monterrey&amp;output=embed" width="100%" height="520" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>

    </main>
""".format(
        form_title=e(c["form_title"]),
        form_note=e(c["form_note"]),
        required_note=e(c["required_note"]),
        direct_title=e(c["direct_title"]),
        direct_text=e(c["direct_text"]),
        hours_text=e(c["hours_text"]),
        call_title=e(c["call_title"]),
        call_note=e(c["call_note"]),
        phones=phones,
        wa=WHATSAPP,
        wa_title=e(c["wa_title"]),
        wa_note=e(c["wa_note"]),
        wa_btn=e(c["wa_btn"]),
        mail_note=e(c["mail_note"]),
        map_iframe_title=e("%s — %s" % (c["map_title"], c["addr_text"])),
        directions_btn=e(c["directions_btn"]),
        sales=sales_mail(lang),
        f_name=e(c["f_name"]),
        f_email=e(c["f_email"]),
        f_phone=e(c["f_phone"]),
        phone_hint=e(c["phone_hint"]),
        f_company=e(c["f_company"]),
        f_state_label=e(c["f_state_label"]),
        states=options(c["f_state"], P.MX_STATES),
        f_reason_label=e(c["f_reason_label"]),
        reasons=options(c["f_reason"], c["reasons"]),
        f_sector_label=e(c["f_sector_label"]),
        sectors=options(c["f_sector"], c["sectors"]),
        f_message=e(c["f_message"]),
        legal_pre=e(c["legal_pre"]),
        privacy_url=PRIVACY_PDF,
        privacy_label=e(c["legal_privacy"]),
        legal_post=e(c["legal_post"]),
        f_submit=e(c["f_submit"]),
        maps=CONTACT["maps"],
        addr_text=e(c["addr_text"]),
        phone_title=e(c["phone_title"]),
        p1t=CONTACT["phone1_tel"],
        phone_office=e(c["phone_office"]),
        mt=CONTACT["mobile_tel"],
        phone_mobile=e(c["phone_mobile"]),
        mail_title=e(c["mail_title"]),
        mails=mails,
        map_title=e(c["map_title"]),
    )

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            extra_ld=ld,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang, title=c["h1"], crumb=c["eyebrow"],
            bg="%s/secciones/arcondec-banner-contacto.jpg" % IMG,
        )
        # Sin la franja de entradilla: en Contacto sobraba. El banner ya dice a
        # qué se viene y justo debajo está el título del bloque de contacto, así
        # que eran tres frases seguidas antes de la primera acción. En el resto de
        # páginas (servicios, proyectos, blog…) se mantiene.
        + body
        + footer(lang=lang, key=key)
    )


# ==========================================================================
# TRABAJA CON NOSOTROS
# ==========================================================================
def render_careers(lang):
    c = P.CAREERS[lang]
    key = "careers"

    why = "\n".join(
        """                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="service-2-item text-center mt-30 animated wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="%dms">
                        <div class="icon"><i class="%s"></i></div>
                        <h3 class="title">%s</h3>
                        <p>%s</p>
                        <div class="service-dot">
                            <img src="/assets/images/service-dot-2.png" alt="">
                            <div class="item">
                                <img src="/assets/images/icon/service-icon-%d.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>"""
        % (n * 150, icon, e(title), e(text), n + 1)
        for n, (title, text, icon) in enumerate(c["why"])
    )

    policy = "\n".join(
        '                            <li><i class="fal fa-check"></i> %s</li>' % e(x)
        for x in c["policy_list"]
    )

    vacancies = "\n".join(
        """                <details class="arc-vacancy">
                    <summary class="arc-vacancy-head">
                        <span class="arc-vacancy-title">%s</span>
                        <span class="arc-vacancy-meta">%s</span>
                        <span class="arc-vacancy-icon" aria-hidden="true"></span>
                    </summary>
                    <div class="arc-vacancy-body">
                        <p><strong>%s:</strong> %s</p>
                        <p><strong>%s:</strong> %s</p>
                        <form class="arc-vacancy-form" action="https://formspree.io/f/meaqkkoo" method="POST" enctype="multipart/form-data">
                            <input type="hidden" name="vacante" value="%s">
                            <input type="hidden" name="_subject" value="Postulación: %s">
                            <div class="arc-vacancy-fields">
                                <input type="text" name="nombre" placeholder="%s" required>
                                <input type="email" name="email" placeholder="%s" required>
                                <label class="arc-vacancy-file">
                                    <span>%s</span>
                                    <input type="file" name="cv" accept=".pdf,.doc,.docx" required>
                                </label>
                                <button type="submit" class="main-btn">%s</button>
                            </div>
                            <p class="arc-vacancy-note">%s</p>
                        </form>
                    </div>
                </details>"""
        % (
            e(v["title"]),
            e(v["meta"]),
            e(c["req_label"]),
            e(v["req"]),
            e(c["func_label"]),
            e(v["func"]),
            e(v["title"]),
            e(v["title"]),
            e(c["name_placeholder"]),
            e(c["email_placeholder"]),
            e(c["cv_label"]),
            e(c["apply_btn"]),
            e(c["apply_note"]),
        )
        for v in P.VACANCIES
    )

    subject = "Vacante" if lang == "es" else "Job application"

    body = """
    <main id="contenido">

    <section class="about-2-area about-11-area pt-90 pb-60">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="about-2-content about-11-content mt-30">
                        <h2 class="title">{why_title}</h2>
                        <p>{why_text}</p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="about-2-thumb about-11-thumb mt-30">
                        <div class="thumb text-right">
                            <img src="{img}/rh/arcondec_vacantes_equipo.jpg" alt="{why_title}" {dims_equipo}>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="arc-soft-area pt-100 pb-90">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="section-title-9 text-center">
                        <span class="service-eyebrow">{vacancies_eyebrow}</span>
                        <h2 class="title">{vacancies_title}</h2>
                        <div class="text">
                            <p>{vacancies_intro}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-lg-11">
                    <div class="arc-vacancies">
{vacancies}
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="pt-90 pb-90">
        <div class="container">
            <div class="row justify-content-center arc-service-grid">
{why}
            </div>
        </div>
    </section>

    <section class="pt-40 pb-130">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="arc-panel">
                        <span class="service-eyebrow">{policy_eyebrow}</span>
                        <h2 class="title h3">{policy_title}</h2>
                        <p>{policy_text}</p>
                        <ul class="mt-20">
{policy}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="pb-90">
        <div class="container">
            <div class="arc-cta">
                <div class="row align-items-center">
                    <div class="col-lg-8">
                        <h2 class="title h3">{cta_title}</h2>
                        <p>{cta_text}</p>
                    </div>
                    <div class="col-lg-4 text-lg-right">
                        <a class="main-btn" href="mailto:{rh}?subject={subject}">{cta_btn}</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    </main>
""".format(
        why_title=e(c["why_title"]),
        why_text=e(c["why_text"]),
        img=IMG,
        dims_equipo=dims("%s/rh/arcondec_vacantes_equipo.jpg" % IMG),
        vacancies_eyebrow=e(c["vacancies_eyebrow"]),
        vacancies_title=e(c["vacancies_title"]),
        vacancies_intro=e(c["vacancies_intro"]),
        vacancies=vacancies,
        why=why,
        policy_eyebrow=e(c["policy_eyebrow"]),
        policy_title=e(c["policy_title"]),
        policy_text=e(c["policy_text"]),
        policy=policy,
        cta_title=e(c["cta_title"]),
        cta_text=e(c["cta_text"]),
        rh=CONTACT["mail_rh"],
        subject=quote(subject),
        cta_btn=e(c["cta_btn"]),
    )

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image="%s/rh/arcondec_vacantes_banner.jpg" % IMG,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang,
            title=c["h1"],
            crumb=c["eyebrow"],
            bg="%s/rh/arcondec_vacantes_banner.jpg" % IMG,
        )
        + '\n    <p class="service-lead-strip">%s</p>\n' % e(c["lead"])
        + body
        + commitment_band(lang)
        + footer(lang=lang, key=key)
    )


# ==========================================================================
# BLOG (indice)
# ==========================================================================
def render_blog(lang):
    c = P.BLOG[lang]
    key = "blog"

    cards = "\n".join(
        """                <div class="col-lg-4 col-md-6">
                    <div class="article-2-item article-11-item mt-30">
                        <div class="article-thumb">
                            <img src="%s/blog/%s" alt="%s" loading="lazy" %s>
                        </div>
                        <div class="article-content">
                            <h2 class="title">%s</h2>
                            <p>%s</p>
                            <span class="article-soon">%s</span>
                        </div>
                    </div>
                </div>"""
        % (IMG, a["img"], e(a[lang][0]), dims("%s/blog/%s" % (IMG, a["img"])), e(a[lang][0]), e(a[lang][1]), e(c["soon"]))
        for a in P.ARTICLES
    )

    body = """
    <main id="contenido">

    <section class="article-2-area article-11-area pt-90 pb-90">
        <div class="container">
            <div class="row">
{cards}
            </div>
        </div>
    </section>

    </main>
""".format(cards=cards)

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image="%s/blog/%s" % (IMG, P.ARTICLES[0]["img"]),
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang,
            title=c["h1"],
            crumb=c["eyebrow"],
            bg="%s/blog/%s" % (IMG, P.ARTICLES[0]["img"]),
        )
        + '\n    <p class="service-lead-strip">%s</p>\n' % e(c["lead"])
        + body
        + commitment_band(lang)
        + footer(lang=lang, key=key)
    )


# ==========================================================================
# INICIO — se genera a partir de tools/home_source.html
# ==========================================================================
def render_home(lang, i18n):
    """Toma el HTML original del inicio (con marcas data-i18n) y lo convierte en
    una pagina de un solo idioma: sustituye los textos, fija los enlaces internos
    y elimina el conmutador por JavaScript."""
    src = (ROOT / "tools/home_source.html").read_text(encoding="utf-8")
    key = "home"
    dic = i18n[lang]

    # 1) Textos marcados con data-i18n
    def swap_text(m):
        open_tag, attrs, inner, close = m.group(1), m.group(2), m.group(3), m.group(4)
        km = re.search(r'data-i18n="([^"]+)"', attrs)
        if not km or km.group(1) not in dic:
            return m.group(0)
        return "%s%s>%s%s" % (open_tag, attrs, e(dic[km.group(1)]), close)

    src = re.sub(
        r"(<(?:h1|h2|h3|h4|h5|h6|p|span|a|li|div|button)\b)([^>]*\bdata-i18n=\"[^\"]+\"[^>]*)>(.*?)(</(?:h1|h2|h3|h4|h5|h6|p|span|a|li|div|button)>)",
        swap_text,
        src,
        flags=re.S,
    )

    # 2) Placeholders traducidos
    def swap_ph(m):
        km = m.group(1)
        return 'placeholder="%s"' % e(dic.get(km, "")) if km in dic else m.group(0)

    src = re.sub(r'placeholder="[^"]*"\s+data-i18n-placeholder="([^"]+)"', swap_ph, src)

    # 3) Enlaces al sitio viejo -> paginas internas nuevas
    for route, patterns in HOME_LINK_MAP.items():
        for pat in patterns:
            src = src.replace('href="%s"' % pat, 'href="%s"' % url(route, lang))

    # 3.b) El nav del inicio viene del HTML original, donde "Servicios" era un
    #      ancla muerta (href="#") y el <li> no llevaba marca de desplegable.
    #      Se apunta a la página índice y se marca para que salga la flecha.
    src = re.sub(
        r'<a class="nav-link" href="#"(\s[^>]*)?>',
        '<a class="nav-link" href="%s"\\1>' % url("services", lang),
        src,
    )
    src = re.sub(
        r'<li class="nav-item">(\s*<a class="nav-link"[^>]*>[^<]*</a>\s*<ul class="sub-menu">)',
        r'<li class="nav-item arc-has-sub">\1',
        src,
    )

    # 4) El atributo data-href-en llevaba el destino en inglés (p. ej.
    #    mailto:sales@arcondec.mx). Se ELIMINABA sin aplicarlo, así que la
    #    portada EN mostraba "sales@" pero enlazaba a "ventas@". Se aplica
    #    primero y solo después se limpia.
    if lang == "en":
        src = re.sub(
            r'href="[^"]*"((?:\s+[a-zA-Z-]+="[^"]*")*?)\s+data-href-en="([^"]+)"',
            lambda m: 'href="%s"%s' % (m.group(2), m.group(1)),
            src,
        )

    # Limpieza de los restos del sistema i18n por JavaScript
    src = re.sub(r'\s+data-i18n(?:-placeholder)?="[^"]*"', "", src)
    src = re.sub(r'\s+data-href-en="[^"]*"', "", src)
    src = src.replace(
        '    <!--====== i18n ES/EN Arcondec ======-->\n'
        '    <script src="assets/js/arcondec-i18n.js"></script>\n',
        "",
    )

    # 5) Rutas de assets absolutas desde la raiz (la version EN vive en /en/)
    src = re.sub(r'(src|href)="assets/', r'\1="/assets/', src)

    # 6) El <head> y el conmutador de idioma se rehacen con el sistema comun
    body = src.split("</head>", 1)[1]
    body = body.replace(
        '<a class="lang-switch active" href="#" data-lang="es">ESP</a> | '
        '<a class="lang-switch" href="#" data-lang="en">EN</a>',
        '<a class="lang-switch%s" href="%s" hreflang="es" lang="es">ESP</a> | '
        '<a class="lang-switch%s" href="%s" hreflang="en" lang="en">EN</a>'
        % (
            " active" if lang == "es" else "",
            url(key, "es"),
            " active" if lang == "en" else "",
            url(key, "en"),
        ),
    )
    # El bloque <style> del original ya vive en assets/css/arcondec.css
    body = re.sub(r"\s*<style>.*?</style>", "", body, flags=re.S)

    # El hero es un slider de dos diapositivas y cada una traia un <h1>.
    # Google espera un unico H1 por pagina: la segunda pasa a <h2> conservando
    # la clase .title, asi que el aspecto no cambia.
    seen_h1 = [False]

    def demote(m):
        if not seen_h1[0]:
            seen_h1[0] = True
            return m.group(0)
        # El '>' que cierra la etiqueta de apertura va aquí: sin él el navegador
        # interpreta el titular como atributos y el texto desaparece.
        return "<h2" + m.group(1) + ">" + m.group(2) + "</h2>"

    body = re.sub(r"<h1([^>]*)>(.*?)</h1>", demote, body, flags=re.S)

    # El contenido principal necesita un landmark <main> para lectores de pantalla
    body = body.replace(
        '    <!--====== HERO PART START ======-->',
        '    <main id="contenido">\n\n    <!--====== HERO PART START ======-->',
        1,
    )
    body = body.replace(
        '    <!--====== FOOTER PART START ======-->',
        '    </main>\n\n    <!--====== FOOTER PART START ======-->',
        1,
    )

    # 6.b) La cabecera del original era otra copia divergente: marcaba "Sobre
    #      nosotros" como activo en la portada, usaba href relativo en el logo y
    #      no cambiaba ventas@ por sales@ en inglés. Se sustituye por la común.
    ini = body.find('<header class="header-area')
    fin = body.find("</header>")
    if ini == -1 or fin < ini:
        raise SystemExit("No se encontró la cabecera en home_source.html")
    body = body[:ini] + header(lang=lang, key=key).strip("\n") + body[fin + len("</header>"):]

    # 7) El pie del HTML original era una copia del compartido y ya había
    #    divergido (sus teléfonos y correos no eran enlaces). Se recorta y se
    #    usa footer() de layout.py, de modo que el pie sea idéntico en las 28
    #    páginas y solo haya un sitio donde mantenerlo.
    corte = body.find("<!--====== FOOTER PART START ======-->")
    if corte == -1:
        raise SystemExit("No se encontró el inicio del pie en home_source.html")
    body = body[:corte] + footer(lang=lang, key=key).lstrip("\n")

    return (
        head(
            lang=lang,
            key=key,
            title=dic["pageTitle"].split("—")[1].strip() if "—" in dic["pageTitle"] else dic["pageTitle"],
            description=dic["metaDesc"],
            keywords=(
                "ingeniería eléctrica, data center, infraestructura crítica, Monterrey, México, Grupo Arcondec"
                if lang == "es"
                else "electrical engineering, data center, critical infrastructure, Monterrey, Mexico, Grupo Arcondec"
            ),
            og_image="/assets/images/hero-bg-2-opt.jpg",
        )
        + body
    )


HOME_LINK_MAP = {
    "about": ["https://arcondec.mx/Nosotros.aspx", "https://arcondec.mx/EN/About.aspx"],
    "projects": ["https://arcondec.mx/Proyectos.aspx", "https://arcondec.mx/EN/Projects.aspx"],
    "careers": ["https://arcondec.mx/Reclutamiento.aspx", "https://arcondec.mx/EN/Careers.aspx"],
    "blog": ["https://arcondec.mx/Blogs.aspx", "https://arcondec.mx/Blogs"],
    "contact": ["https://arcondec.mx/Contactanos.aspx", "https://arcondec.mx/EN/Contact.aspx"],
    "srv-proele": [
        "https://arcondec.mx/Servicios/proyectos-eléctricos-integrales.aspx",
        "https://arcondec.mx/EN/Services/PROYE.aspx",
    ],
    "srv-estel": [
        "https://arcondec.mx/Servicios/estudios-eléctricos-especializados.aspx",
        "https://arcondec.mx/EN/Services/ESTEL.aspx",
    ],
    "srv-corac": [
        "https://arcondec.mx/Servicios/soluciones-en-corriente-directa-dc.aspx",
        "https://arcondec.mx/EN/Services/CORAC.aspx",
    ],
    "srv-gespr": [
        "https://arcondec.mx/Servicios/gestión-integral-de-proyectos-eléctricos.aspx",
        "https://arcondec.mx/EN/Services/GESPR.aspx",
    ],
    "srv-cosdc": [
        "https://arcondec.mx/Servicios/construcción-de-data-center.aspx",
        "https://arcondec.mx/EN/Services/COSDC.aspx",
    ],
    "srv-civdc": [
        "https://arcondec.mx/Servicios/ingeniería-civil-para-data-center.aspx",
        "https://arcondec.mx/EN/Services/CIVDC.aspx",
    ],
    "srv-ingdc": [
        "https://arcondec.mx/Servicios/servicios-de-ingeniería-integral.aspx",
        "https://arcondec.mx/EN/Services/INGDC.aspx",
    ],
}


def load_home_i18n():
    """Lee los diccionarios ES/EN del antiguo arcondec-i18n.js para no reescribir
    a mano las 147 cadenas del inicio que ya estaban traducidas."""
    js = (ROOT / "tools/home_i18n.js").read_text(encoding="utf-8")
    out = {}
    for lang in ("es", "en"):
        m = re.search(r"\b%s:\s*\{(.*?)\n        \}" % lang, js, re.S)
        if not m:
            raise SystemExit("No se encontró el diccionario '%s' en home_i18n.js" % lang)
        dic = {}
        for km, vm in re.findall(r"(\w+):\s*'((?:[^'\\]|\\.)*)'", m.group(1)):
            dic[km] = vm.replace("\\'", "'").replace("\\\\", "\\")
        out[lang] = dic
    return out


# ==========================================================================
# SITEMAP + ROBOTS
# ==========================================================================
def render_sitemap(routes, base):
    """Sitemap con los pares de idioma anunciados (xhtml:link), como recomienda
    Google para sitios bilingues: cada URL declara su version ES y EN."""
    entries = []
    for pair in routes.values():
        alts = (
            '    <xhtml:link rel="alternate" hreflang="es-MX" href="%s%s"/>\n'
            '    <xhtml:link rel="alternate" hreflang="en" href="%s%s"/>\n'
            '    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>\n'
            % (base, pair["es"], base, pair["en"], base, pair["es"])
        )
        for u in (pair["es"], pair["en"]):
            entries.append(
                "  <url>\n    <loc>%s%s</loc>\n%s    <changefreq>monthly</changefreq>\n"
                "    <priority>%s</priority>\n  </url>"
                % (base, u, alts, "1.0" if u == "/index.html" else "0.8")
            )
    entries.sort()
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s\n</urlset>\n'
        % "\n".join(entries)
    )


# ==========================================================================
# 404 — Vercel sirve /404.html automaticamente para toda ruta inexistente.
# Pagina unica bilingue, noindex: no lleva canonical ni hreflang porque no es
# una pagina indexable (check.py la exime de esos requisitos).
# ==========================================================================
def render_404():
    return """<!doctype html>
<html lang="es">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex">
    <meta name="theme-color" content="#1F439B">
    <title>Página no encontrada | Grupo Arcondec</title>
    <link rel="shortcut icon" href="/assets/images/arcondec/brand/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="/assets/css/default.css">
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="stylesheet" href="/assets/css/arcondec.css">
    <style>
        .arc-404 { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 40px 20px; background: #1F439B; }
        .arc-404 img { width: 150px; margin-bottom: 40px; }
        .arc-404 h1 { color: #fff; font-size: 34px; margin-bottom: 12px; }
        .arc-404 p { color: rgba(255, 255, 255, .82); font-size: 17px; max-width: 480px; margin: 0 auto 8px; }
        .arc-404 .arc-404-en { margin-bottom: 32px; }
        .arc-404 a.arc-404-btn { display: inline-block; margin: 6px 8px; padding: 14px 32px; border-radius: 30px; background: #FFBB00; color: #132D67; font-weight: 700; text-decoration: none; }
        .arc-404 a.arc-404-btn.arc-404-alt { background: transparent; border: 2px solid rgba(255, 255, 255, .6); color: #fff; }
    </style>
</head>

<body>
    <main class="arc-404">
        <img src="/assets/images/arcondec/brand/logo-light.png" alt="Grupo Arcondec">
        <h1>Página no encontrada <span aria-hidden="true">(404)</span></h1>
        <p>La dirección que buscas no existe o cambió de lugar.</p>
        <p class="arc-404-en" lang="en">The page you are looking for does not exist or has moved.</p>
        <div>
            <a class="arc-404-btn" href="/index.html">Ir al inicio</a>
            <a class="arc-404-btn arc-404-alt" href="/en/index.html" lang="en">Go to homepage</a>
        </div>
    </main>
</body>

</html>
"""


# ==========================================================================
def main():
    from layout import BASE_URL, ROUTES

    written = []
    i18n = load_home_i18n()

    for lang in ("es", "en"):
        written.append(write(url("home", lang), render_home(lang, i18n)))
        written.append(write(url("about", lang), render_about(lang)))
        written.append(write(url("projects", lang), render_projects(lang)))
        written.append(write(url("contact", lang), render_contact(lang)))
        written.append(write(url("careers", lang), render_careers(lang)))
        written.append(write(url("services", lang), render_services_index(lang)))
        written.append(write(url("blog", lang), render_blog(lang)))
        for svc in SERVICES:
            written.append(
                write(url("srv-" + svc["key"], lang), render_service(svc, lang))
            )
        # Los vecinos se calculan aquí y no dentro de la plantilla para que
        # render_project no tenga que conocer la lista completa: recibe solo
        # el proyecto anterior y el siguiente, ya resueltos.
        # El recorrido es circular: del primero se va al último y del último al
        # primero, para que ninguna página del bucle quede con una pestaña sola.
        # El índice negativo de Python ya envuelve hacia atrás por sí solo.
        for i, hub in enumerate(P.HUBS):
            anterior = P.HUBS[i - 1]
            siguiente = P.HUBS[(i + 1) % len(P.HUBS)]
            written.append(
                write(
                    url("prj-" + hub["slug"]["es"], lang),
                    render_project(hub, lang, anterior, siguiente),
                )
            )

    write("/404.html", render_404())
    write("/sitemap.xml", render_sitemap(SITEMAP_ROUTES, BASE_URL))
    write(
        "/robots.txt",
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE_URL,
    )

    for p in written:
        print("  %s" % p.relative_to(ROOT))
    print("\n%d páginas + 404 + sitemap.xml + robots.txt" % len(written))


if __name__ == "__main__":
    main()
