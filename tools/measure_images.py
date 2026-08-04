# -*- coding: utf-8 -*-
"""Regenera tools/image_sizes.json con las dimensiones reales de cada imagen.

    pip3 install Pillow   (solo la primera vez)
    python3 tools/measure_images.py

Hay que ejecutarlo cada vez que se agrega o se reemplaza una imagen en
assets/images/. build.py lee el JSON para escribir width/height reales en cada
<img> y evitar saltos de maquetación (CLS). Si una imagen no está en el JSON,
la página se genera igual, solo que ese <img> va sin dimensiones.
"""

import json
import pathlib

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

sizes = {}
for p in sorted((ROOT / "assets/images").rglob("*")):
    if p.suffix.lower() in EXTS:
        with Image.open(p) as im:
            sizes["/" + p.relative_to(ROOT).as_posix()] = list(im.size)

out = ROOT / "tools/image_sizes.json"
out.write_text(json.dumps(sizes, indent=1), encoding="utf-8")
print("%d imágenes medidas -> %s" % (len(sizes), out.relative_to(ROOT)))
