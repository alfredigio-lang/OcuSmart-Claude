#!/bin/sh
# Rebuilds dist/ocusmart-skill.zip (uploadable skill for the Claude app) from ocusmart/skills/ocusmart
set -e
cd "$(dirname "$0")/ocusmart/skills"
rm -f ../../dist/ocusmart-skill.zip
zip -qr ../../dist/ocusmart-skill.zip ocusmart -x '*/__pycache__/*' '*.DS_Store'
