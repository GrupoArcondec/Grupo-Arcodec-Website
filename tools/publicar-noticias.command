#!/bin/zsh
# Publica en Vercel lo que está en esta carpeta: verifica, guarda en git y despliega.
# Doble clic desde Finder, o en Terminal:  zsh tools/publicar-noticias.command
cd "$(dirname "$0")/.." || exit 1
echo "Carpeta: $(pwd)"
echo "\n1/3  Verificando el sitio…"
if ! python3 tools/check.py | tail -3; then
  echo "\ncheck.py reportó problemas. No se publicó nada."; read "?Presiona Enter para cerrar."; exit 1
fi
echo "\n2/3  Guardando los cambios en git…"
git add -A -- . ':!AGENTS.md'
git commit -m "Noticias: publicación del $(date +%Y-%m-%d)" || echo "(no había cambios nuevos que guardar)"
echo "\n3/3  Publicando en Vercel…"
npx vercel --prod --yes
echo "\nListo. Revisa https://arcondec.vercel.app/blog.html"
read "?Presiona Enter para cerrar."
