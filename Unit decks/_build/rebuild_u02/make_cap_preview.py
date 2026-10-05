# -*- coding: utf-8 -*-
"""Stand-alone PREVIEW copy of capstone_P.html, for opening by double-click.
Usage: python3 make_cap_preview.py <capstone_P.html> <mock supabase js> <output file>
A stand-in replaces the database: one sample team, sample text, Unit 2 section open. Nothing is saved. Never commit or upload it."""
import sys, json
src, mock, out = sys.argv[1:4]
p = open(src, 'rb').read().decode('utf-8')
ext = '<script src="supabase.umd.js"></script>'
assert p.count(ext) == 1
SAMPLE = {
 'arch_output': 'Strategic Position\nWHAT: Sample text. The value the organisation has chosen to create and its field of play.\nWHY: Sample text. The rationale for those choices.\n\nStrategic Model\nHOW: Sample text. The operating model, capabilities and mechanisms.\nWHEN: Sample text. The timing and sequencing.\n\nValue Architecture\nSample text.\n\nStrategic Navigation\nSample text.\n\nStrategy Discipline\nSample text.',
 'intent_statement': 'Sample Strategy Intent Statement, as typed and confirmed in 4.2 of Unit 2.',
 'sip_d1_st': 'Sample statement 1, as typed and confirmed in 4.3 of Unit 2.',
 'sip_d2_st': 'Sample statement 2, as typed and confirmed in 4.3 of Unit 2.',
 'sip_d3_st': 'Sample statement 3, as typed and confirmed in 4.3 of Unit 2.',
 'sip_d4_st': 'Sample statement 4, as typed and confirmed in 4.3 of Unit 2.',
 'confirmed_items': ['Strategy Architecture', 'Strategy Intent Statement', 'SiP · Customer Experience & Value',
                     'SiP · Operational Capability & Execution Rhythm', 'SiP · People & Culture Dynamics', 'SiP · Enterprise Value Creation', 'Success in Practice'],
}
M = {'lr': SAMPLE, 'log': [], 'n': 1, 'open': True, 'boxCount': 6, 'sec': {'status': 'draft', 'content': {}, 'updated_at': None, 'conf': []}}
js = open(mock, encoding='utf-8').read()
js = js.replace("'Impactis Consulting'", "'Sample Case Organisation'").replace("'Case brief text.'", "'Sample brief text.'") \
       .replace("'Team Baobab'", "'Sample Team'").replace("'Carol Lupiya'", "'You'").replace("'Brian Lupiya'", "'Team member two'")
assert 'Lupiya' not in js and 'Impactis' not in js
inline = '<script>\nwindow.__MOCK=' + json.dumps(M, ensure_ascii=False) + ';\n' + js + '</script>'
assert '</script>' not in js
p = p.replace(ext, inline.replace('\n', '\r\n'))
p = p.replace('<title>IBSL | Capstone — Blueprint Showcase</title>', '<title>PREVIEW · Capstone</title>')
BAR = ('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
       'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · Capstone page · sample team and sample text · nothing is saved · not the live portal</div>')
i = p.rindex('</body>'); p = p[:i] + BAR + '\r\n' + p[i:]
open(out, 'wb').write(p.encode('utf-8'))
print('written', out, len(p))
