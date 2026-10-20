# -*- coding: utf-8 -*-
import sys, os
root = sys.argv[1]
def patch(name, pairs):
    F = os.path.join(root, name)
    raw = open(F, 'rb').read(); crlf = b'\r\n' in raw
    t = raw.decode('utf-8').replace('\r\n', '\n')
    for a, b in pairs:
        assert t.count(a) == 1, (name, t.count(a), a[:80]); t = t.replace(a, b)
    open(F, 'wb').write((t.replace('\n', '\r\n') if crlf else t).encode('utf-8')); print(name, 'ok')
patch('capstone_P.html', [
 ("      ['6B','FACES application','For each business function in the Contribution Map of [Case], describe the practical management arrangement for each of the five FACES functions.']\n",
  "      ['6B','FACES application','For each business function in the Contribution Map of [Case], describe the practical management arrangement for each of the five FACES functions.'],\n      ['6C','WARD check-up','For the enterprise Key Result of [Case], set the waypoints, the alert that raises a red flag, the recovery for the individuals and for the organisational conditions, and the decider.']\n"),
 ("      ['8D','Leadership credibility','For eroding leadership credibility: the potential gap and the decision point for recovery, for the performance of individuals and for the organisational conditions.']\n",
  "      ['8D','Leadership credibility','For eroding leadership credibility: the potential gap and the decision point for recovery, for the performance of individuals and for the organisational conditions.'],\n      ['8E','WARD test','For the WARD check-up of [Case]: the red flag at one waypoint, what explains the gap in the performance of individuals and in the organisational conditions, and the recovery run.']\n"),
 ("      ['6B','cm_faces','Enterprise PM System · FACES Application']\n", "      ['6B','cm_faces','Enterprise PM System · FACES Application'],\n      ['6C','cm_ward','Enterprise PM System · WARD']\n"),
])
F = os.path.join(root, 'capstone_P.html'); t = open(F, encoding='utf-8').read().replace('\r\n','\n')
i = t.find("    u8: { lens:'u3m2_lens7', rows:["); j = t.find(']}', i); print(t[i:j+2])
patch('dashboard_F.html', [
 ("      cm_faces: 'Enterprise PM System · 5.2 · FACES Application — confirmed',\n", "      cm_faces: 'Enterprise PM System · 5.2 · FACES Application — confirmed',\n      cm_ward: 'Enterprise PM System · 5.3 · WARD Check-up — confirmed',\n"),
 ("      rd_credibility: 'Decision Points · Erodes Leadership Credibility — confirmed',\n", "      rd_credibility: 'Decision Points · Erodes Leadership Credibility — confirmed',\n      rd_ward: 'Decision Points · 5.2 · Testing Your WARD — confirmed',\n"),
])
patch('build_collection.js', [
 ("cm_(record|map|faces)$", "cm_(record|map|faces|ward)$"),
 ("rd_(record|warning|accountability|learning|credibility)$", "rd_(record|warning|accountability|learning|credibility|ward)$"),
])
patch('capstone_P.html', [("      ['8D','rd_credibility','Review Discipline · Leadership Credibility']\n", "      ['8D','rd_credibility','Review Discipline · Leadership Credibility'],\n      ['8E','rd_ward','Review Discipline · WARD Test']\n")])
