"""Agrega noticias al inicio de tools/news.py y su análisis a tools/news_analysis.py.

Uso (desde la raíz del repositorio):  python3 add_news.py noticias.json
noticias.json es una lista de objetos con: key, img, published, date, source, link,
caption (opcional: [es, en]), es (5 textos), en (5 textos), analysis_es y analysis_en
(3 pares [título, texto] cada uno).
"""
import json
import pathlib
import sys

q = lambda x: json.dumps(x, ensure_ascii=False)
items = json.load(open(sys.argv[1], encoding='utf-8'))

np_ = pathlib.Path('tools/news.py')
ns = np_.read_text(encoding='utf-8')
ap = pathlib.Path('tools/news_analysis.py')
an = ap.read_text(encoding='utf-8')
if 'NEWS = [\n' not in ns or 'ANALYSIS = {\n' not in an:
    sys.exit('La estructura de news.py o news_analysis.py cambió; revisar a mano.')

news_txt = ''
ana_txt = ''
for it in items:
    if 'key="%s"' % it['key'] in ns or 'key=%s' % q(it['key']) in ns:
        sys.exit('La clave ya existe: ' + it['key'])
    for lang in ('es', 'en'):
        if len(it[lang]) != 5 or len(it['analysis_' + lang]) != 3:
            sys.exit('%s: se esperan 5 textos y 3 secciones de análisis en %s' % (it['key'], lang))
    cap = ''
    if it.get('caption'):
        cap = '\n         caption=(%s, %s),' % (q(it['caption'][0]), q(it['caption'][1]))
    news_txt += '    dict(key=%s, img=%s, published=%s, date=%s, source=%s, link=%s,%s\n         es=(%s),\n         en=(%s)),\n' % (
        q(it['key']), q(it['img']), q(it['published']), q(it['date']), q(it['source']), q(it['link']), cap,
        ', '.join(q(x) for x in it['es']), ', '.join(q(x) for x in it['en']))
    fmt = lambda L: '[\n' + ',\n'.join('   (%s, %s)' % (q(t), q(x)) for t, x in L) + ']'
    ana_txt += " %s: {\n  'es': %s,\n  'en': %s\n },\n" % (q(it['key']), fmt(it['analysis_es']), fmt(it['analysis_en']))

np_.write_text(ns.replace('NEWS = [\n', 'NEWS = [\n' + news_txt, 1), encoding='utf-8')
ap.write_text(an.replace('ANALYSIS = {\n', 'ANALYSIS = {\n' + ana_txt, 1), encoding='utf-8')
for it in items:
    print('%s | título ES %d, EN %d (máx. 43) | resumen ES %d, EN %d (70 a 160)' % (
        it['key'], len(it['es'][0]), len(it['en'][0]), len(it['es'][1]), len(it['en'][1])))
