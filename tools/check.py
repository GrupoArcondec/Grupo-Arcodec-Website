# -*- coding: utf-8 -*-
"""Comprobacion del sitio generado.

    python3 tools/check.py

Revisa, sobre los archivos HTML del repositorio:
  · que todo href/src interno exista en disco
  · que cada pagina tenga un unico <h1>, title, description y canonical
  · que las etiquetas hreflang apunten a paginas que existen
  · que las imagenes lleven alt

Sale con codigo 1 si encuentra algun problema, para poder usarlo en CI.
"""

import pathlib
import re
import sys
from html.parser import HTMLParser

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from layout import BASE_URL  # noqa: E402  (fuente única del dominio)

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {"tools", "assets"}

# La 404 es noindex y no forma parte del sitio indexable: se le exigen enlaces
# sanos y alt en las imagenes, pero no canonical, hreflang ni h1 unico.
SEO_EXEMPT = {"404.html"}

# <h2 class="title" data-delay="0.6s"Texto</h2>  ->  falta el '>' de cierre.
# Ancla en un atributo entrecomillado completo seguido de letra (no de espacio ni '>').
MALFORMED_TAG = re.compile(
    r"<([a-zA-Z][a-zA-Z0-9]*)\b[^<>]*?=\s*\"[^\"]*\"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ¿¡0-9]"
)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.refs = []          # (atributo, valor)
        self.h1 = 0
        self.title = None
        self._in_title = False
        self.description = None
        self.canonical = None
        self.alternates = []
        self.imgs_sin_alt = 0
        self.lang = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            if a.get("name") == "description":
                self.description = a.get("content")
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            if rel == "canonical":
                self.canonical = a.get("href")
            elif rel == "alternate" and a.get("hreflang"):
                self.alternates.append(a["href"])
            if a.get("href"):
                self.refs.append(("href", a["href"]))
        elif tag == "img":
            if a.get("src"):
                self.refs.append(("src", a["src"]))
            # alt="" es lo correcto en iconos decorativos: indica al lector de
            # pantalla que los ignore. Lo que no debe faltar es el atributo.
            if "alt" not in a:
                self.imgs_sin_alt += 1
        elif tag == "script" and a.get("src"):
            self.refs.append(("src", a["src"]))
        elif tag == "a" and a.get("href"):
            self.refs.append(("href", a["href"]))
        elif tag == "iframe" and a.get("src"):
            self.refs.append(("src", a["src"]))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data


def html_files():
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS:
            continue
        yield p


def local_target(ref):
    """Devuelve la ruta local a comprobar, o None si el enlace es externo."""
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:", "javascript:")):
        return None
    ref = ref.split("#")[0].split("?")[0]
    if not ref:
        return None
    if ref.startswith("/"):
        return ROOT / ref.lstrip("/")
    return None  # todo el sitio usa rutas absolutas desde la raiz


def main():
    problems = []
    advice = []  # avisos SEO no bloqueantes: se muestran pero no fallan el build
    checked = 0

    for path in html_files():
        rel = path.relative_to(ROOT)
        page = Page()
        page.feed(path.read_text(encoding="utf-8"))
        checked += 1

        for attr, ref in page.refs:
            target = local_target(ref)
            if target is not None and not target.exists():
                problems.append("%s -> %s roto (%s)" % (rel, ref, attr))

        seo = str(rel) not in SEO_EXEMPT
        if seo and page.h1 != 1:
            problems.append("%s tiene %d <h1> (debe haber exactamente 1)" % (rel, page.h1))

        # Etiqueta de apertura mal cerrada: <h2 class="x"Texto</h2>. El navegador
        # se traga el texto como si fueran atributos y el titular desaparece.
        # Señal inequívoca: un valor de atributo entrecomillado COMPLETO seguido
        # de una letra en vez de un espacio o del '>' de cierre.
        raw = path.read_text(encoding="utf-8")
        for m in MALFORMED_TAG.finditer(raw):
            problems.append(
                "%s: etiqueta <%s> sin '>' de cierre — %s…"
                % (rel, m.group(1), raw[m.start():m.start() + 70].replace("\n", " "))
            )

        # Un encabezado vacío casi siempre delata markup roto
        for m in re.finditer(r"<(h[1-6])\b[^>]*>(.*?)</\1>", raw, re.S):
            if not re.sub(r"<[^>]+>", "", m.group(2)).strip():
                problems.append("%s: <%s> vacío" % (rel, m.group(1)))
        if not (page.title or "").strip():
            problems.append("%s sin <title>" % rel)
        if seo and not (page.description or "").strip():
            problems.append("%s sin meta description" % rel)
        if seo and not page.canonical:
            problems.append("%s sin canonical" % rel)
        if seo and len(page.alternates) < 2:
            problems.append("%s sin hreflang ES/EN" % rel)
        for alt in page.alternates:
            if alt.startswith(BASE_URL):
                target = ROOT / alt[len(BASE_URL):].lstrip("/")
                if not target.exists():
                    problems.append("%s: hreflang apunta a %s, que no existe" % (rel, alt))
        if page.imgs_sin_alt:
            problems.append("%s: %d imagen(es) sin atributo alt" % (rel, page.imgs_sin_alt))
        if not page.lang:
            problems.append("%s sin atributo lang en <html>" % rel)

        # Longitudes recomendadas en resultados de Google: title <=60 visibles,
        # description 70-160. Son consejos de redaccion, no errores.
        if seo:
            t = (page.title or "").strip()
            d = (page.description or "").strip()
            if len(t) > 65:
                advice.append("%s: title de %d caracteres (ideal <=60): %s…" % (rel, len(t), t[:50]))
            if len(d) > 165:
                advice.append("%s: description de %d caracteres (ideal <=160)" % (rel, len(d)))
            elif d and len(d) < 70:
                advice.append("%s: description de %d caracteres (ideal >=70)" % (rel, len(d)))

    print("Páginas revisadas: %d" % checked)
    if advice:
        print("\nAvisos SEO (no bloquean):")
        for a in advice:
            print("  ~ %s" % a)
    if problems:
        print("\nProblemas encontrados (%d):" % len(problems))
        for p in problems:
            print("  · %s" % p)
        sys.exit(1)
    print("Sin problemas.")


if __name__ == "__main__":
    main()
