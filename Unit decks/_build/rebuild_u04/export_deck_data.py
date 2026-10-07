# -*- coding: utf-8 -*-
"""Writes the Unit 4 content the deck needs to a JSON file, from u4_content.py (the same content the two pages are built from),
so the deck and the pages cannot drift apart. Usage: python3 export_deck_data.py <out.json>"""
import sys, json, re, html
import u4_content as C
def clean(x):
    if isinstance(x, str): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip()
    if isinstance(x, (list, tuple)): return [clean(v) for v in x]
    if isinstance(x, dict): return {k: clean(v) for k, v in x.items()}
    return x
D = dict(CHECKPOINTS=C.CHECKPOINTS, HEAD_Q=C.HEAD_Q, OVERVIEW_Q=C.OVERVIEW_Q, DEPTHS=C.DEPTHS, BOUNDARY_KINDS=C.BOUNDARY_KINDS, VP_TESTS=C.VP_TESTS, MBT2=C.MBT2,
         ARENA_QUOTE=C.ARENA_QUOTE, STEPS=C.STEPS, STEP_Q=C.STEP_Q, STEP_MBT=C.STEP_MBT, WORKED_KR=C.WORKED_KR, WORKED_SIP=C.WORKED_SIP,
         EXAMPLES=[dict(t=C.kr_by_id(i)['t'], **{k: C.kr_by_id(i)[k] for k in 'abcv'}) for i in C.EXAMPLE_KRS],
         TRAPS=C.TRAPS, II_BOUNDARY=C.II_BOUNDARY, GAME=C.GAME, MINES=C.MINES, ILLUS=C.ILLUS, SLO=C.SLO)
json.dump(clean(D), open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('written', sys.argv[1])
