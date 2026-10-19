#!/usr/bin/env bash
#
# Publica el sitio en arcondec.mx (hosting propio, Plesk/IIS sobre Windows).
#
#   ./tools/deploy.sh            compila, revisa y sube
#   ./tools/deploy.sh --dry-run  muestra qué subiría, sin tocar el servidor
#
# Requisitos (una sola vez):
#
#   1. brew install lftp
#
#   2. Guardar la contraseña SFTP en el Llavero de macOS. Se teclea una vez
#      y queda cifrada; este script nunca la escribe en disco ni la imprime:
#
#         security add-generic-password -a arcondec.sftp -s arcondec-sftp -w
#
#      (pide la contraseña y no la muestra al escribirla)
#
# Qué NO toca en el servidor: deploy.sh solo SUBE. Nunca borra nada remoto.
# Es deliberado: en httpdocs conviven carpetas que no son del sitio
# (Firma/, Marketing/, TarjetasPresentacion/, los PDF, y los restos del
# sitio .aspx anterior). Un --delete las barrería y rompería las firmas de
# correo del equipo y los QR impresos. Para borrar algo remoto, se hace a
# mano y a conciencia.

set -euo pipefail

HOST="208.109.37.131"
USUARIO="arcondec.sftp"
LLAVERO="arcondec-sftp"
REMOTO="/httpdocs"

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"

SECO=""
[[ "${1:-}" == "--dry-run" ]] && SECO="--dry-run"

echo "──────────────────────────────────────────────"
echo " 1/3  Compilando"
echo "──────────────────────────────────────────────"
python3 tools/build.py | tail -2

echo
echo "──────────────────────────────────────────────"
echo " 2/3  Revisando"
echo "──────────────────────────────────────────────"
# check.py devuelve 1 cuando hay avisos de redacción (títulos largos, etc.).
# Esos no bloquean. Solo se detiene el deploy si hay enlaces rotos.
python3 tools/check.py > /tmp/arcondec-check.txt 2>&1 || true
tail -1 /tmp/arcondec-check.txt
if grep -q " roto " /tmp/arcondec-check.txt; then
    echo
    echo "⚠️  Hay enlaces rotos:"
    grep " roto " /tmp/arcondec-check.txt | head -5
    echo
    read -r -p "¿Subir de todas formas? [s/N] " r
    [[ "$r" =~ ^[sS]$ ]] || { echo "Cancelado."; exit 1; }
fi

echo
echo "──────────────────────────────────────────────"
echo " 3/3  Subiendo a $HOST:$REMOTO"
echo "──────────────────────────────────────────────"

CLAVE="$(security find-generic-password -s "$LLAVERO" -w 2>/dev/null)" || {
    echo "No encontré la contraseña en el Llavero."
    echo "Guárdala una vez con:"
    echo "  security add-generic-password -a $USUARIO -s $LLAVERO -w"
    exit 1
}

# --only-newer     solo sube lo que cambió (149 MB no se suben cada vez)
# --parallel=4     cuatro transferencias a la vez
# --no-perms       IIS no usa permisos de Unix; intentar aplicarlos da error
# sin --delete     ver la nota de arriba
lftp -u "$USUARIO","$CLAVE" "sftp://$HOST" <<EOF
set sftp:auto-confirm yes
set net:max-retries 3
set net:timeout 20
mirror --reverse --only-newer --parallel=4 --no-perms $SECO \
    --exclude-glob tools/ \
    --exclude-glob .git/ \
    --exclude-glob .github/ \
    --exclude-glob "untitled folder/" \
    --exclude-glob "*.md" \
    --exclude-glob .htaccess \
    --exclude-glob vercel.json \
    --exclude-glob web.config.completo \
    --exclude-glob .DS_Store \
    --exclude-glob .gitignore \
    --exclude-glob LICENSE \
    --exclude-glob .deploy.env \
    . $REMOTO
bye
EOF

unset CLAVE

echo
if [[ -n "$SECO" ]]; then
    echo "✓ Simulación terminada. No se subió nada."
else
    echo "✓ Publicado — https://arcondec.mx"
    echo
    echo "  Comprobaciones rápidas:"
    echo "    curl -sI https://arcondec.mx/            | head -1"
    echo "    curl -sI https://arcondec.mx/Nosotros.aspx | head -2"
fi
