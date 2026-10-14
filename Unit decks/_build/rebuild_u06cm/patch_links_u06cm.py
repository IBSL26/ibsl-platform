# -*- coding: utf-8 -*-
"""Unit 6 rework of 14 October 2026: the files linked to the Unit 6 pages.
Usage: python3 patch_links_u06cm.py <folder with capstone_P.html, dashboard_F.html, build_collection.js> <output folder>
capstone_P.html      Unit 6 has two boxes (was four): 6A S2R® Contribution Map™, 6B FACES application,
                     filled from the unit page's confirmed record (cm_map, cm_faces). Database: Claude outputs\\capstone_unit6_boxes_cm.sql.
dashboard_F.html     labels for the new reflections (ref13, ref14, ref15) and the Section 5 record; heading "Building the Enterprise PM System". Old labels stay.
build_collection.js  the Section 5 group work stays out of the Learning Portfolio. Then run: node build_collection.js"""
import sys, os
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
def patch(name, pairs):
    raw = open(os.path.join(src, name), 'rb').read().decode('utf-8')
    crlf = '\r\n' in raw
    t = raw.replace('\r\n', '\n')
    for a, b in pairs:
        assert t.count(a) == 1, (name, t.count(a), a[:90])
        t = t.replace(a, b)
    assert t.count('<script') == raw.count('<script') and t.count('</script>') == raw.count('</script>')
    open(os.path.join(out, name), 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8'))
    print(name, 'written,', len(pairs), 'changes')

cap = open(os.path.join(src, 'capstone_P.html'), encoding='utf-8').read().replace('\r\n', '\n')
i = cap.index("      ['6A','Performance scoring logic'"); j = cap.index("    ]},\n    { key:'u7'")
OLD_BOXES = cap[i:j]
NEW_BOXES = ("      ['6A','S2R® Contribution Map™','For one enterprise Key Result of [Case], set out what each contributing business function must deliver, what its people must deliver with the performance measure, and the ESRG conditions the organisation must provide with the measure or evidence of readiness.'],\n"
             "      ['6B','FACES application','For each business function in the Contribution Map of [Case], describe the practical management arrangement for each of the five FACES functions.']\n")
OLD_PULL = """    u6: { lens:'u3m1_lens5', rows:[
      ['6A','pm_scoring','PM Architecture · Scoring Logic'],
      ['6B','pm_faces','PM Architecture · FACES'],
      ['6C','pm_execution','PM Architecture · EXECUTION'],
      ['6D','pm_scorecards','PM Architecture · Scorecards']
    ]},"""
NEW_PULL = """    u6: { lens:'u3m1_lens5', rows:[
      ['6A','cm_map','Enterprise PM System · Contribution Map'],
      ['6B','cm_faces','Enterprise PM System · FACES Application']
    ]},"""
patch('capstone_P.html', [(OLD_BOXES, NEW_BOXES), (OLD_PULL, NEW_PULL)])
patch('dashboard_F.html', [
    ("      { name: 'Designing the PM Architecture', test: function (k) { return /^pm_(record|scoring|faces|execution|scorecards)$/i.test(k); } },\n",
     "      { name: 'Building the Enterprise PM System', test: function (k) { return /^cm_(record|map|faces)$/i.test(k); } },\n"
     "      { name: 'Designing the PM Architecture', test: function (k) { return /^pm_(record|scoring|faces|execution|scorecards)$/i.test(k); } },\n"),
    ("      ref12: 'Your Current PM System',\n      pm_record:",
     "      ref12: 'Your Current PM System',\n      ref13: 'Two Operating Systems',\n      ref14: 'Contributions in Your Organisation',\n      ref15: 'FACES in Your Organisation',\n"
     "      cm_record: 'Building the Enterprise PM System — record while the group works',\n"
     "      cm_map: 'Enterprise PM System · 5.1 · S2R® Contribution Map™ — confirmed',\n"
     "      cm_faces: 'Enterprise PM System · 5.2 · FACES Application — confirmed',\n      pm_record:"),
    ('12:"Your Current PM System"},', '12:"Your Current PM System",13:"Two Operating Systems",14:"Contributions in Your Organisation",15:"FACES in Your Organisation"},'),
])
patch('build_collection.js', [
    ("u3m1_lens5:/^(pm_(record|scoring|faces|execution|scorecards)$|confirmed_items$)/i",
     "u3m1_lens5:/^(pm_(record|scoring|faces|execution|scorecards)$|cm_(record|map|faces)$|confirmed_items$)/i"),
])
