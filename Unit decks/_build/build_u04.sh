#!/bin/sh
# Builds the Unit 4 deck in one go (cloud workspace). Usage: sh build_u04.sh <out folder>
# Before: python3 rebuild_u04/export_deck_data.py u04_data.json  ·  python3 shoot_reflections_u04.py <PREVIEW participant page> reflections/u04
set -e
OUT="$1"; mkdir -p "$OUT"
node unit04.js "$OUT/u04_base.pptx"
python3 add_reflection_slides.py "$OUT/u04_base.pptx" reflections/u04/spec.json "$OUT/u04_refl.pptx"
python3 format_notes_u03.py "$OUT/u04_refl.pptx" "$OUT/Unit 04 - Direction Integrity (ABCV-MBT).pptx"
python3 lint_notes.py "$OUT/Unit 04 - Direction Integrity (ABCV-MBT).pptx"
