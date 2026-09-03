# -*- coding: utf-8 -*-
"""Cabecera, pie y envoltorio HTML compartidos por todas las paginas.

El markup es el del template aball (index-12) tal cual; aqui solo se rellenan
los textos y los enlaces. Los estilos de marca viven en assets/css/arcondec.css.

Todas las URLs son absolutas desde la raiz del sitio (/servicios/...), asi que
no dependen de la profundidad del archivo que las escribe.
"""

import html
import json
import pathlib

import pages as _P

from content import (
    COMMIT_TEXT,
    CONTACT,
    LOGIN_URL,
    PRIVACY_PDF,
    SERVICES,
    SOCIAL,
    WHATSAPP,
)

# Dominio de produccion. Se usa para canonical, hreflang, Open Graph y JSON-LD.
# Si el sitio se publica en otro dominio, cambiar SOLO esta linea.
#
# OJO: apuntaba a https://www.arcondec.mx, que es el SITIO ANTIGUO y sigue vivo.
# Las 28 rutas de este sitio devuelven 404 alli, asi que todos los canonical y
# hreflang señalaban a paginas inexistentes de otro dominio: Google habria
# descartado el sitio entero. Ahora apunta al despliegue real.
BASE_URL = "https://grupo-arcondec.vercel.app"

# --------------------------------------------------------------------------
# Mapa de rutas: clave -> URL en cada idioma.
# Es la unica fuente de verdad de los enlaces internos y de las etiquetas
# hreflang, de modo que ES y EN nunca se descoordinan.
# --------------------------------------------------------------------------
ROUTES = {
    "home": {"es": "/index.html", "en": "/en/index.html"},
    "about": {"es": "/nosotros.html", "en": "/en/about.html"},
    "projects": {"es": "/proyectos.html", "en": "/en/projects.html"},
    "careers": {"es": "/vacantes.html", "en": "/en/careers.html"},
    "services": {"es": "/servicios.html", "en": "/en/services.html"},
    "blog": {"es": "/blog.html", "en": "/en/blog.html"},
    "contact": {"es": "/contacto.html", "en": "/en/contact.html"},
}
for _s in SERVICES:
    ROUTES["srv-" + _s["key"]] = {
        "es": "/servicios/%s.html" % _s["slug"]["es"],
        "en": "/en/services/%s.html" % _s["slug"]["en"],
    }

# Una ruta por proyecto, generada desde su `slug`. Agregar un proyecto a
# pages.HUBS le da URL, canonical y hreflang sin tocar nada más aquí.
#
# SITEMAP_ROUTES es el subconjunto que sí se anuncia a los buscadores: excluye
# los proyectos con `publicado: False`. Las rutas siguen existiendo en ROUTES
# —si no, head() no podría construir el canonical de esas páginas— pero no se
# listan. Es la contraparte del `noindex` que head() les pone.
_PROJECT_KEYS = []
for _h in _P.HUBS:
    _key = "prj-" + _h["slug"]["es"]
    _PROJECT_KEYS.append(_key)
    ROUTES[_key] = {
        "es": "/proyectos/%s.html" % _h["slug"]["es"],
        "en": "/en/projects/%s.html" % _h["slug"]["en"],
    }

_UNLISTED = {
    "prj-" + _h["slug"]["es"] for _h in _P.HUBS if not _h.get("publicado")
}
SITEMAP_ROUTES = {k: v for k, v in ROUTES.items() if k not in _UNLISTED}

UI = {
    "es": {
        "login": "Iniciar sesión",
        # Rótulos del menú: cortos, de una palabra. El botón amarillo y el de la
        # franja CTA usan "cta_contact", que sí va en imperativo.
        "nav_about": "Nosotros",
        "nav_projects": "Proyectos",
        "nav_services": "Servicios",
        "nav_careers": "Vacantes",
        "nav_blog": "Blog",
        "nav_contact": "Contacto",
        "cta_contact": "Contáctanos",
        "home": "Inicio",
        "advisor": "Habla con un asesor",
        "foot_company": "Compañía",
        "foot_ie": "Ingeniería eléctrica",
        "foot_dc": "Centro de datos",
        "news_title": "Suscríbete a nuestro boletín para recibir novedades.",
        "news_ph": "Escribe tu correo…",
        "news_btn": "Únete",
        "privacy": "Aviso de privacidad",
        "copy": "Grupo Arcondec S.A. de C.V. Copyright © 2026 | Todos los derechos Reservados",
        "duns": "Certificación Dun & Bradstreet",
        "back_top": "Volver arriba",
        "skip": "Saltar al contenido",
        "nav_label": "Navegación principal",
        "lang_other": "English",
    },
    "en": {
        "login": "Login",
        "nav_about": "About",
        "nav_projects": "Projects",
        "nav_services": "Services",
        "nav_careers": "Careers",
        "nav_blog": "Blog",
        "nav_contact": "Contact",
        "cta_contact": "Contact Us",
        "home": "Home",
        "advisor": "Speak with an advisor",
        "foot_company": "Company",
        "foot_ie": "Electrical Engineering",
        "foot_dc": "Data Center",
        "news_title": "Subscribe to our newsletter to receive updates.",
        "news_ph": "Enter email…",
        "news_btn": "Join us",
        "privacy": "Privacy Notice",
        "copy": "Grupo Arcondec S.A. de C.V. Copyright © 2026 | All rights reserved",
        "duns": "Dun & Bradstreet Certification",
        "back_top": "Back to top",
        "skip": "Skip to content",
        "nav_label": "Main navigation",
        "lang_other": "Español",
    },
}


def e(text):
    """Escapa texto para insertarlo en el HTML."""
    return html.escape(str(text), quote=True)


def url(key, lang):
    return ROUTES[key][lang]


def sales_mail(lang):
    return CONTACT["mail_sales_es"] if lang == "es" else CONTACT["mail_sales_en"]


# --------------------------------------------------------------------------
# <head>
# --------------------------------------------------------------------------
# Dimensiones reales de cada imagen (tools/measure_images.py) — aqui solo para
# declarar el tamano del og:image, que acelera el primer compartido del enlace.
_OG_SIZES = json.loads(
    (pathlib.Path(__file__).parent / "image_sizes.json").read_text(encoding="utf-8")
)


def head(*, lang, key, title, description, keywords="", og_image=None, extra_ld=None,
         noindex=False):
    """Cabecera con SEO completo: canonical, hreflang, Open Graph y JSON-LD.

    `noindex=True` marca la página como no indexable. Se usa en las páginas de
    proyecto que todavía no están publicadas: existen en disco para poder
    revisarlas, pero nadie las enlaza, no entran al sitemap y le dicen a Google
    que no las liste. Sin esto, una página con datos de relleno podría acabar
    indexada y compitiendo con el contenido real."""
    other = "en" if lang == "es" else "es"
    canonical = BASE_URL + url(key, lang)
    alt_url = BASE_URL + url(key, other)
    og_image = og_image or "/assets/images/arcondec/secciones/servicios-bg.jpg"
    full_title = "%s | Grupo Arcondec" % title

    og_w, og_h = _OG_SIZES.get(og_image, (None, None))
    og_dims = (
        '    <meta property="og:image:width" content="%d">\n'
        '    <meta property="og:image:height" content="%d">\n' % (og_w, og_h)
        if og_w
        else ""
    )

    ld = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Grupo Arcondec S.A. de C.V.",
        "alternateName": "Grupo Arcondec",
        "url": BASE_URL + "/",
        "logo": BASE_URL + "/assets/images/arcondec/brand/logo.png",
        "description": description,
        "foundingDate": "1991",
        "areaServed": "MX",
        "sameAs": [u for _, _, u in SOCIAL],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+52-81-1934-1192",
                "contactType": "customer service",
                "areaServed": "MX",
                "availableLanguage": ["Spanish", "English"],
            }
        ],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CONTACT["street"],
            "addressLocality": CONTACT["city"],
            "addressRegion": CONTACT["region"],
            "postalCode": CONTACT["zip"],
            "addressCountry": "MX",
        },
    }
    def _ld(obj):
        # json.dumps escapa para JSON, no para HTML: un "</script>" dentro de
        # cualquier texto cerraria el bloque y volcaria la pagina como texto.
        return json.dumps(obj, ensure_ascii=False, indent=2).replace("<", "\\u003c")

    blocks = [_ld(ld)]
    if key == "home":
        # WebSite: es lo que Google usa para mostrar el nombre del sitio en los
        # resultados en lugar del dominio.
        blocks.append(_ld({
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Grupo Arcondec",
            "alternateName": "Grupo Arcondec S.A. de C.V.",
            "url": BASE_URL + "/",
            "inLanguage": ["es-MX", "en"],
        }))
    else:
        # BreadcrumbList: la miga Inicio > Pagina que Google muestra bajo el
        # titulo del resultado, espejo de la miga visible del banner.
        blocks.append(_ld({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1,
                 "name": UI[lang]["home"], "item": BASE_URL + url("home", lang)},
                {"@type": "ListItem", "position": 2,
                 "name": title, "item": canonical},
            ],
        }))
    if extra_ld:
        blocks.append(_ld(extra_ld))
    ld_tags = "\n".join(
        '    <script type="application/ld+json">\n%s\n    </script>' % b for b in blocks
    )

    return """<!doctype html>
<html lang="{lang}">

<head>

    <!--====== Meta ======-->
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{kw}">
    <meta name="author" content="Grupo Arcondec S.A. de C.V.">
    <meta name="robots" content="{robots}">
    <meta name="theme-color" content="#1F439B">

    <title>{title}</title>

    <!--====== Canonical y versiones por idioma ======-->
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="es-MX" href="{es_url}">
    <link rel="alternate" hreflang="en" href="{en_url}">
    <link rel="alternate" hreflang="x-default" href="{es_url}">

    <!--====== Open Graph / Twitter ======-->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Grupo Arcondec">
    <meta property="og:locale" content="{locale}">
    <meta property="og:locale:alternate" content="{locale_alt}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:image:alt" content="{title}">
{og_dims}    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{og_image}">

    <!--====== Favicon ======-->
    <link rel="shortcut icon" href="/assets/images/arcondec/brand/favicon.ico" type="image/x-icon">

    <!--====== Estilos del template aball ======-->
    <link rel="stylesheet" href="/assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="/assets/css/font-awesome.min.css">
    <link rel="stylesheet" href="/assets/css/magnific-popup.css">
    <link rel="stylesheet" href="/assets/css/animate.min.css">
    <link rel="stylesheet" href="/assets/css/slick.css">
    <link rel="stylesheet" href="/assets/css/default.css">
    <link rel="stylesheet" href="/assets/css/style.css">

    <!--====== Piel de marca Arcondec ======-->
    <link rel="stylesheet" href="/assets/css/arcondec.css">

{ld}

</head>
""".format(
        lang=lang,
        desc=e(description),
        kw=e(keywords),
        robots=("noindex, nofollow" if noindex
                else "index, follow, max-image-preview:large"),
        title=e(full_title),
        canonical=canonical,
        es_url=BASE_URL + url(key, "es"),
        en_url=BASE_URL + url(key, "en"),
        locale="es_MX" if lang == "es" else "en_US",
        locale_alt="en_US" if lang == "es" else "es_MX",
        og_image=BASE_URL + og_image,
        og_dims=og_dims,
        ld=ld_tags,
    )


# --------------------------------------------------------------------------
# Cabecera
# --------------------------------------------------------------------------
def header(*, lang, key):
    t = UI[lang]
    other = "en" if lang == "es" else "es"
    sub = "\n".join(
        '                                                <li><a href="%s"%s>%s</a></li>'
        % (url("srv-" + s["key"], lang), _active_attr(key, "srv-" + s["key"]), e(s[lang]["nav"]))
        for s in SERVICES
    )
    social = "\n".join(
        '                                    <li><a href="%s" target="_blank" rel="noopener" aria-label="%s"><i class="fab fa-%s"></i></a></li>'
        % (u, n, i)
        for i, n, u in SOCIAL
    )

    def nav(route, label):
        cls = " active" if key == route else ""
        return (
            '                                        <li class="nav-item%s">\n'
            '                                            <a class="nav-link" href="%s"%s>%s</a>\n'
            "                                        </li>"
            % (cls, url(route, lang), _active_attr(key, route), e(label))
        )

    services_active = " active" if key.startswith("srv-") or key == "services" else ""

    return """
    <a class="skip-link" href="#contenido">{skip}</a>

    <!--====== HEADER ======-->

    <header class="header-area header-2-area header-11-area">
        <div class="header-top">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="header-top-item">
                            <div class="info">
                                <ul>
                                    <li><img src="/assets/images/phone.svg" alt=""> <a href="tel:{p1t}">{p1}</a> / <a href="tel:{p2t}">{p2}</a></li>
                                    <li><img src="/assets/images/email.svg" alt=""> <a href="mailto:{mail}">{mail}</a> / <a href="mailto:{sales}">{sales}</a></li>
                                    <li><a href="{login_url}" target="_blank" rel="noopener">{login}</a></li>
                                    <li><a class="lang-switch{es_active}" href="{es_url}" hreflang="es" lang="es">ESP</a> | <a class="lang-switch{en_active}" href="{en_url}" hreflang="en" lang="en">EN</a></li>
                                </ul>
                            </div>
                            <div class="sicial">
                                <ul>
{social}
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="header-nav">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="navigation">
                            <nav class="navbar navbar-expand-lg navbar-light" aria-label="{nav_label}">

                                <a class="navbar-brand" href="{home}"><img src="/assets/images/arcondec/brand/logo-arcondec-white.png" alt="Grupo Arcondec"></a>

                                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                                    <span class="toggler-icon"></span>
                                    <span class="toggler-icon"></span>
                                    <span class="toggler-icon"></span>
                                </button>

                                <div class="collapse navbar-collapse sub-menu-bar" id="navbarSupportedContent">
                                    <ul class="navbar-nav ml-auto">
{nav_home}
{nav_about}
{nav_projects}
                                        <li class="nav-item arc-has-sub{services_active}">
                                            <a class="nav-link" href="{services_url}">{services}</a>
                                            <ul class="sub-menu">
{sub}
                                            </ul>
                                        </li>
{nav_blog}
{nav_careers}
{nav_contact}
                                        <li class="nav-item d-lg-none">
                                            <a class="nav-link" href="{login_url}" target="_blank" rel="noopener">{login}</a>
                                        </li>
                                        <li class="nav-item d-lg-none">
                                            <a class="nav-link lang-switch{es_active}" href="{es_url}" hreflang="es" lang="es">ESP</a>
                                        </li>
                                        <li class="nav-item d-lg-none">
                                            <a class="nav-link lang-switch{en_active}" href="{en_url}" hreflang="en" lang="en">EN</a>
                                        </li>
                                    </ul>
                                </div>


                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!--====== HEADER ENDS ======-->
""".format(
        skip=e(t["skip"]),
        nav_label=e(t["nav_label"]),
        p1=e(CONTACT["phone1"]),
        p2=e(CONTACT["phone2"]),
        p1t=CONTACT["phone1_tel"],
        p2t=CONTACT["phone2_tel"],
        mail=CONTACT["mail_info"],
        sales=sales_mail(lang),
        login_url=LOGIN_URL,
        login=e(t["login"]),
        es_url=url(key, "es"),
        en_url=url(key, "en"),
        es_active=" active" if lang == "es" else "",
        en_active=" active" if lang == "en" else "",
        social=social,
        home=url("home", lang),
        nav_home=nav("home", t["home"]),
        nav_about=nav("about", t["nav_about"]),
        nav_projects=nav("projects", t["nav_projects"]),
        services=e(t["nav_services"]),
        services_url=url("services", lang),
        services_active=services_active,
        sub=sub,
        nav_blog=nav("blog", t["nav_blog"]),
        nav_careers=nav("careers", t["nav_careers"]),
        nav_contact=nav("contact", t["nav_contact"]),
    )


def _active_attr(current, route):
    return ' aria-current="page"' if current == route else ""


# --------------------------------------------------------------------------
# Banner de pagina interior
# --------------------------------------------------------------------------
def page_banner(*, lang, title, crumb, bg=None, parent=None):
    """Banner a sangre completa con migas de pan.

    `parent` inserta un nivel intermedio y recibe (rótulo, URL). Sirve para las
    páginas que cuelgan de otra —un proyecto dentro de Proyectos— y hace que la
    ruta se lea completa: Inicio / Proyectos / HUB Apodaca. Sin él, las migas
    son de dos niveles, como en el resto del sitio.
    """
    # Diseño original del template: banner a sangre completa, sin tarjeta.
    style = ' style="background-image: url(%s);"' % bg if bg else ""
    intermedio = (
        '\n                                <li class="breadcrumb-item">'
        '<a href="%s">%s</a></li>' % (parent[1], e(parent[0]))
        if parent else ""
    )
    return """
    <!--====== TÍTULO DE PÁGINA ======-->

    <div class="page-title-area">
        <div class="section__bg"{style}></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="page-title-content text-center">
                        <h1 class="title">{title}</h1>
                        <nav aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item"><a href="{home}">{home_label}</a></li>{intermedio}
                                <li class="breadcrumb-item active" aria-current="page">{crumb}</li>
                            </ol>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!--====== TÍTULO DE PÁGINA ENDS ======-->
""".format(
        style=style,
        title=e(title),
        home=url("home", lang),
        home_label=e(UI[lang]["home"]),
        intermedio=intermedio,
        crumb=e(crumb),
    )


# --------------------------------------------------------------------------
# Pie
# --------------------------------------------------------------------------
def footer(*, lang, key, extra_scripts=()):
    t = UI[lang]
    ie = [s for s in SERVICES if s["group"] == "ie"]
    dc = [s for s in SERVICES if s["group"] == "dc"]

    def links(items):
        return "\n".join(
            '                                <li><a href="%s">%s</a></li>'
            % (url("srv-" + s["key"], lang), e(s[lang]["nav"]))
            for s in items
        )

    company = "\n".join(
        '                                <li><a href="%s">%s</a></li>' % (url(k, lang), e(label))
        for k, label in [
            ("about", t["nav_about"]),
            ("projects", t["nav_projects"]),
            ("careers", t["nav_careers"]),
            ("blog", t["nav_blog"]),
            ("contact", t["nav_contact"]),
        ]
    )
    social = "\n".join(
        '                            <li><a href="%s" target="_blank" rel="noopener" aria-label="%s"><i class="fab fa-%s"></i></a></li>'
        % (u, n, i)
        for i, n, u in SOCIAL
    )

    return """
    <!--====== PIE ======-->

    <footer class="footer-area footer-2-area">
        <div class="footer-2-top">
            <div class="container">
                <div class="row align-items-start">
                    <div class="col-lg-3">
                        <div class="footer-logo">
                            <a href="{home}"><img src="/assets/images/arcondec/brand/logo-arcondec-white.png" alt="Grupo Arcondec"></a>
                            <img class="duns" src="/assets/images/arcondec/brand/duns_v2.png" alt="{duns}">
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4">
                        <div class="footer-info">
                            <ul>
                                <li><img src="/assets/images/icon/footer-icon-4.png" alt=""> {address}</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4">
                        <div class="footer-info">
                            <ul>
                                <li><img src="/assets/images/icon/footer-icon-5.png" alt=""> <a href="tel:{p1t}">{p1}</a></li>
                                <li><a href="tel:{p2t}">{p2}</a> · <a href="tel:{mt}">{mobile}</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4">
                        <div class="footer-info">
                            <ul>
                                <li><img src="/assets/images/icon/footer-icon-6.png" alt=""> <a href="mailto:{mail}">{mail}</a></li>
                                <li><a href="mailto:{sales}">{sales}</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="footer-item">
                <div class="row">
                    <div class="col-lg-3 col-md-6 col-sm-6">
                        <div class="footer-list footer-list-11 mt-30">
                            <h2 class="title h4">{company_title}</h2>
                            <ul>
{company}
                                <li><a href="{login_url}" target="_blank" rel="noopener">{login}</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-6">
                        <div class="footer-list footer-list-11 mt-30">
                            <h2 class="title h4">{ie_title}</h2>
                            <ul>
{ie_links}
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-6">
                        <div class="footer-list footer-list-11 mt-30">
                            <h2 class="title h4">{dc_title}</h2>
                            <ul>
{dc_links}
                            </ul>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-6">
                        <div class="footer-newsletter-item footer-newsletter-item-11 mt-30">
                            <div class="dot">
                                <img src="/assets/images/icon/footer-newsletter-dot.png" alt="">
                            </div>
                            <h2 class="title h3">{news_title}</h2>
                            <form action="mailto:{sales}" method="post" enctype="text/plain">
                                <div class="input-box">
                                    <label class="sr-only" for="newsletter-email">{news_ph}</label>
                                    <input id="newsletter-email" type="email" name="email" autocomplete="email" placeholder="{news_ph}" required>
                                    <button class="main-btn-3" type="submit">{news_btn}</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <div class="footer-copyright footer-copyright-11 d-flex align-items-end">
                        <ul>
{social}
                        </ul>
                        <p><span>{copy}</span> | <a href="{privacy_url}" target="_blank" rel="noopener">{privacy}</a></p>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <!--====== PIE ENDS ======-->

    <!--====== WHATSAPP FLOTANTE ======-->

    <a class="whatsapp-float" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp Grupo Arcondec">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"><path fill="#ffffff" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg>
    </a>

    <!--====== BOTÓN SUBIR ======-->

    <button class="back-to-top back-to-top-11" type="button" aria-label="{back_top}">
        <i class="fal fa-angle-up" aria-hidden="true"></i>
    </button>

    <!--====== Scripts del template ======-->
    <script src="/assets/js/vendor/modernizr-3.6.0.min.js"></script>
    <script src="/assets/js/vendor/jquery-1.12.4.min.js"></script>
    <script src="/assets/js/bootstrap.min.js"></script>
    <script src="/assets/js/popper.min.js"></script>
    <script src="/assets/js/jquery.appear.min.js"></script>
    <script src="/assets/js/slick.min.js"></script>
    <script src="/assets/js/wow.js"></script>
    <script src="/assets/js/isotope.pkgd.min.js"></script>
    <script src="/assets/js/imagesloaded.pkgd.min.js"></script>
    <script src="/assets/js/jquery.magnific-popup.min.js"></script>
    <script src="/assets/js/main.js"></script>

    <!--====== Movimiento Arcondec (GSAP) ======-->
    <script src="/assets/js/vendor/gsap.min.js"></script>
    <script src="/assets/js/vendor/ScrollTrigger.min.js"></script>
    <script src="/assets/js/vendor/SplitText.min.js"></script>
    <script src="/assets/js/arcondec-motion.js"></script>
{extra_scripts}

</body>

</html>
""".format(
        home=url("home", lang),
        duns=e(t["duns"]),
        address=e(CONTACT["address"]),
        p1=e(CONTACT["phone1"]),
        p2=e(CONTACT["phone2"]),
        p1t=CONTACT["phone1_tel"],
        p2t=CONTACT["phone2_tel"],
        mt=CONTACT["mobile_tel"],
        mobile=e(CONTACT["mobile"]),
        mail=CONTACT["mail_info"],
        sales=sales_mail(lang),
        company_title=e(t["foot_company"]),
        company=company,
        login_url=LOGIN_URL,
        login=e(t["login"]),
        ie_title=e(t["foot_ie"]),
        ie_links=links(ie),
        dc_title=e(t["foot_dc"]),
        dc_links=links(dc),
        news_title=e(t["news_title"]),
        news_ph=e(t["news_ph"]),
        news_btn=e(t["news_btn"]),
        social=social,
        copy=e(t["copy"]),
        privacy_url=PRIVACY_PDF,
        privacy=e(t["privacy"]),
        wa=WHATSAPP,
        back_top=e(t["back_top"]),
        extra_scripts="\n".join(
            '    <script src="%s"></script>' % src for src in extra_scripts
        ),
    )


def body_open():
    return """
<body class="bg-white">

    <!-- LOADER -->
    <div class="preloader">
        <div class="lds-ellipsis">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>
    <!-- END LOADER -->
"""


def commitment_band(lang):
    """Franja azul con la frase de compromiso, presente en todo el sitio original."""
    t = UI[lang]
    return """
    <!--====== FRANJA DE COMPROMISO ======-->

    <div class="subscribe-area subscribe-11-area">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <div class="subscribe-item">
                        <h2 class="title h3">{title}</h2>
                        <span>{text}</span>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="subscribe-form subscribe-11-form text-lg-right text-left">
                        <ul>
                            <li><a class="main-btn" href="{contact}">{contact_label}</a></li>
                            <li><a class="main-btn main-btn-2" href="{wa}" target="_blank" rel="noopener">{btn}</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!--====== FRANJA DE COMPROMISO ENDS ======-->
""".format(
        title=e(
            "Agenda tu consulta con nuestros especialistas"
            if lang == "es"
            else "Schedule your consultation with our specialists"
        ),
        text=e(COMMIT_TEXT[lang]),
        contact=url("contact", lang),
        contact_label=e(t["cta_contact"]),
        wa=WHATSAPP,
        btn=e(t["advisor"]),
    )
