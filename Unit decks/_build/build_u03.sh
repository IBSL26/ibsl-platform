#!/bin/sh
# Builds the Unit 3 deck in one go (cloud workspace). Usage: sh build_u03.sh <out folder>
set -e
OUT="$1"; mkdir -p "$OUT"
node unit03.js "$OUT/u03_base.pptx"
python3 add_reflection_slides.py "$OUT/u03_base.pptx" reflections/u03/spec.json "$OUT/u03_refl.pptx"
python3 format_notes_u03.py "$OUT/u03_refl.pptx" "$OUT/Unit 03 - SiP KISS Mapping & OKR Definition.pptx"
python3 lint_notes.py "$OUT/Unit 03 - SiP KISS Mapping & OKR Definition.pptx"
