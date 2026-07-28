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


def write(path, content):
    dest = ROOT / path.lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")
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
            og_image="%s/servicios/proele-1.jpg" % IMG,
            extra_ld=ld,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang, title=c["h1"], crumb=c["title"],
            bg="%s/servicios/proele-1.jpg" % IMG,
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
    values = "\n".join(
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
        for n, (title, text, icon) in enumerate(c["values"])
    )

    body = """
    <main id="contenido">

    <!--====== HISTORIA ======-->

    <section class="about-2-area about-11-area pt-90 pb-60">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="about-2-content about-11-content mt-30">
                        <span class="service-eyebrow">{lead}</span>
                        <h2 class="title">{history_title}</h2>
{history}
                        <a class="main-btn main-btn-3 mt-30" href="{projects}">{projects_label}</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="about-2-thumb about-11-thumb mt-30">
                        <div class="thumb text-right">
                            <img src="{img}/rh/historia.jpg" alt="{alt_historia}" %s>
                        </div>
                        <div class="thumb-2 ml-80">
                            <img src="{img}/rh/img-1.jpg" alt="{alt_equipo}" %s>
                            <div class="box">
                                <h3 class="title"><span>30</span>+</h3>
                                <span>{years}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--====== QUÉ NOS DISTINGUE ======-->

    <section class="pb-90">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="arc-panel text-center">
                        <h2 class="title h3">{distinct_title}</h2>
                        <p>{distinct}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--====== VALORES ======-->

    <section class="arc-soft-area pt-90 pb-90">
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

    <!--====== QUÉ HACEMOS ======-->

    <section class="arc-soft-area pt-90 pb-90">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="arc-panel arc-links mt-30">
                        <h2 class="title h4">{ie_title}</h2>
                        <ul>
{ie_items}
                        </ul>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="arc-panel arc-links mt-30">
                        <h2 class="title h4">{dc_title}</h2>
                        <ul>
{dc_items}
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    </main>
""".format(
        lead=e(c["lead"]),
        history_title=e(c["history_title"]),
        history=history,
        projects=url("projects", lang),
        projects_label=e(t["nav_projects"]),
        img=IMG,
        alt_historia=e(c["alt_historia"]),
        alt_equipo=e(c["alt_equipo"]),
        years=e(c["years_label"]),
        distinct_title=e(c["distinct_title"]),
        distinct=e(c["distinct"]),
        values_title=e(c["values_title"]),
        values=values,
        ie_title=e(LIST_IE[lang]["title"]),
        ie_items="\n".join(
            '                            <li><i class="fal fa-check"></i> %s</li>' % e(x)
            for x in LIST_IE[lang]["items"]
        ),
        dc_title=e(LIST_DC[lang]["title"]),
        dc_items="\n".join(
            '                            <li><i class="fal fa-check"></i> %s</li>' % e(x)
            for x in LIST_DC[lang]["items"]
        ),
    )

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image="%s/rh/historia.jpg" % IMG,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(lang=lang, title=c["h1"], crumb=c["eyebrow"], bg="%s/rh/historia.jpg" % IMG)
        + body
        + commitment_band(lang)
        + footer(lang=lang, key=key)
    )


# ==========================================================================
# PROYECTOS
# ==========================================================================
def render_projects(lang):
    c = P.PROJECTS[lang]
    key = "projects"

    stats = "\n".join(
        """                <div class="col-lg-3 col-md-6 col-sm-6">
                    <div class="overview-counter-item text-center mt-30">
                        <span class="arc-counter-pre">%s</span>
                        <h3 class="title"><span class="arc-count" data-count="%s">0</span>+</h3>
                        <p>%s</p>
                    </div>
                </div>"""
        % (e(pre), value, e(label))
        for value, label, pre in c["stats"]
    )

    # La leyenda va siempre visible (no solo en :hover): en movil no hay hover
    # y el nombre del hub es informacion, no decoracion.
    hubs = "\n".join(
        """                <div class="col-lg-4 col-md-6">
                    <div class="arc-project mt-30">
                        <div class="arc-project-thumb">
                            <img src="%s/proyectos/%s" alt="%s, %s" loading="lazy" %s>
                        </div>
                        <div class="arc-project-caption">
                            <h3 class="title h5">%s</h3>
                            <span>%s</span>
                        </div>
                    </div>
                </div>"""
        % (IMG, img, e(name), e(loc), dims("%s/proyectos/%s" % (IMG, img)), e(name), e(loc))
        for name, loc, img in P.HUBS
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
                "item": {"@type": "Place", "name": name, "address": loc},
            }
            for i, (name, loc, _) in enumerate(P.HUBS)
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

    <!--====== RESULTADOS ======-->

    <section class="pt-90 pb-60">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="arc-panel text-center">
                        <h2 class="title h3">{results_title}</h2>
                        <p>{results}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--====== HUBS ======-->

    <section class="portfolio-style-3-area pb-90">
        <div class="container">
            <div class="row">
{hubs}
            </div>
        </div>
    </section>

    </main>
""".format(
        stats_title=e(c["stats_title"]),
        stats=stats,
        results_title=e(c["results_title"]),
        results=e(c["results"]),
        hubs=hubs,
    )

    return (
        head(
            lang=lang,
            key=key,
            title=c["title"],
            description=c["meta"],
            keywords=c["keywords"],
            og_image="%s/proyectos/arcondec-monterrey-01.jpg" % IMG,
            extra_ld=ld,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang,
            title=c["h1"],
            crumb=c["eyebrow"],
            bg="%s/proyectos/arcondec-monterrey-01.jpg" % IMG,
        )
        + '\n    <p class="service-lead-strip">%s</p>\n' % e(c["lead"])
        + body
        + commitment_band(lang)
        + footer(
            lang=lang, key=key, extra_scripts=("/assets/js/arcondec-counters.js",)
        )
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

    mails = "\n".join(
        '                            <li><span>%s:</span> <a href="mailto:%s">%s</a></li>'
        % (e(label), addr, addr)
        for label, addr in c["mails"]
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

    <section class="pt-90 pb-90">
        <div class="container">
            <div class="row">

                <div class="col-lg-7">
                    <div class="contact-us-box mt-30">
                        <h2 class="title h3">{form_title}</h2>
                        <p>{form_text}</p>
                        <form action="mailto:{sales}" method="post" enctype="text/plain" class="mt-30">
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-name">{f_name}</label>
                                        <input id="f-name" type="text" name="nombre" autocomplete="name" required>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-email">{f_email}</label>
                                        <input id="f-email" type="email" name="correo" autocomplete="email" required>
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
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-state">{f_state_label}</label>
                                        <select id="f-state" name="estado">
                                        {states}
                                        </select>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-reason">{f_reason_label}</label>
                                        <select id="f-reason" name="motivo" required>
                                        {reasons}
                                        </select>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="input-box mt-20">
                                        <label for="f-sector">{f_sector_label}</label>
                                        <select id="f-sector" name="giro" required>
                                        {sectors}
                                        </select>
                                    </div>
                                </div>
                                <div class="col-md-12">
                                    <div class="input-box mt-20">
                                        <label for="f-message">{f_message}</label>
                                        <textarea id="f-message" name="mensaje" rows="5" required></textarea>
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

                <div class="col-lg-5">
                    <div class="arc-panel mt-30">
                        <h2 class="title h4">{addr_title}</h2>
                        <p><a href="{maps}" target="_blank" rel="noopener">{addr_text}</a></p>
                    </div>
                    <div class="arc-panel mt-30">
                        <h2 class="title h4">{phone_title}</h2>
                        <ul>
                            <li><a href="tel:{p1t}">{phone_office}</a></li>
                            <li><a href="tel:{mt}">{phone_mobile}</a></li>
                        </ul>
                    </div>
                    <div class="arc-panel mt-30">
                        <h2 class="title h4">{mail_title}</h2>
                        <ul>
{mails}
                        </ul>
                    </div>
                    <div class="arc-panel mt-30">
                        <h2 class="title h4">{map_title}</h2>
                        <div class="contact-map">
                            <iframe title="{map_title}" src="https://www.google.com/maps?q=Grupo+Arcondec+Monterrey&amp;output=embed" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    </main>
""".format(
        form_title=e(c["form_title"]),
        form_text=e(c["form_text"]),
        sales=sales_mail(lang),
        f_name=e(c["f_name"]),
        f_email=e(c["f_email"]),
        f_phone=e(c["f_phone"]),
        phone_hint=e(c["phone_hint"]),
        f_company=e(c["f_company"]),
        f_state_label=e(c["f_state"]),
        states=options(c["f_state"], P.MX_STATES),
        f_reason_label=e(c["f_reason"]),
        reasons=options(c["f_reason"], c["reasons"]),
        f_sector_label=e(c["f_sector"]),
        sectors=options(c["f_sector"], c["sectors"]),
        f_message=e(c["f_message"]),
        legal_pre=e(c["legal_pre"]),
        privacy_url=PRIVACY_PDF,
        privacy_label=e(c["legal_privacy"]),
        legal_post=e(c["legal_post"]),
        f_submit=e(c["f_submit"]),
        addr_title=e(c["addr_title"]),
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
            bg="%s/secciones/centro-datos-arcondec.jpg" % IMG,
        )
        + '\n    <p class="service-lead-strip">%s</p>\n' % e(c["lead"])
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
                            <img src="{img}/rh/empledado.jpg" alt="{why_title}" %s>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="arc-soft-area pt-90 pb-90">
        <div class="container">
            <div class="row justify-content-center arc-service-grid">
{why}
            </div>
        </div>
    </section>

    <section class="pb-90">
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
            og_image="%s/rh/empledado.jpg" % IMG,
        )
        + body_open()
        + header(lang=lang, key=key)
        + page_banner(
            lang=lang, title=c["h1"], crumb=c["eyebrow"], bg="%s/rh/empledado.jpg" % IMG
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
                            <h3 class="title">%s</h3>
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
def render_sitemap(urls, base):
    body = "\n".join(
        "  <url>\n    <loc>%s%s</loc>\n    <changefreq>monthly</changefreq>\n"
        "    <priority>%s</priority>\n  </url>" % (base, u, "1.0" if u == "/index.html" else "0.8")
        for u in urls
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % body
    )


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

    all_urls = [r[l] for r in ROUTES.values() for l in ("es", "en")]
    write("/sitemap.xml", render_sitemap(sorted(all_urls), BASE_URL))
    write(
        "/robots.txt",
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE_URL,
    )

    for p in written:
        print("  %s" % p.relative_to(ROOT))
    print("\n%d páginas + sitemap.xml + robots.txt" % len(written))


if __name__ == "__main__":
    main()
