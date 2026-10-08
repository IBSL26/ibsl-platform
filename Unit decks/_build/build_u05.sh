#!/bin/sh
# Builds the Unit 5 deck in one go (cloud workspace). Usage: sh build_u05.sh <out folder>
# Before: python3 rebuild_u05/export_deck_data.py <participant page> <facilitator page> u05_data.json
#         python3 shoot_reflections_u05.py <PREVIEW participant page> u05_data.json reflections/u05
set -e
OUT="$1"; mkdir -p "$OUT"
node unit05.js "$OUT/u05_base.pptx"
python3 add_reflection_slides.py "$OUT/u05_base.pptx" reflections/u05/spec.json "$OUT/u05_refl.pptx"
python3 format_notes_u03.py "$OUT/u05_refl.pptx" "$OUT/Unit 05 - Aligning Heart & Mind.pptx"
python3 lint_notes.py "$OUT/Unit 05 - Aligning Heart & Mind.pptx"
