# -*- coding: utf-8 -*-
"""Unit 1 part 6.2 · The Problem Charter (19 Oct 2026).
   Builds unit1_P.html, unit1_F.html, capstone_P.html, dashboard_A.html, dashboard_F.html and build_collection.js
   from the files before the change. Every cut checks that it finds its place exactly once and stops on a miss.
   Usage: python3 build_pc.py <in folder> <out folder>"""
import sys, os, io
SRC, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))

EOL = {}
def rd(name):
    with open(os.path.join(SRC, name), encoding='utf-8', newline='') as f: t = f.read()
    EOL[name] = '\r\n' if '\r\n' in t else '\n'
    return t.replace('\r\n', '\n')
def wr(name, text):
    if '\r' in text: raise SystemExit('STOP · stray CR in ' + name)
    with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f: f.write(text.replace('\n', EOL[name]))
def rep(text, old, new, label):
    n = text.count(old)
    if n != 1: raise SystemExit('STOP · %s · found %d times' % (label, n))
    return text.replace(old, new)

ROLES = ['CEO', 'CFO', 'COO', 'CHRO', 'CTO', 'CMO', 'CCO', 'CPO', 'CRO', 'CSO']
CHALLENGE_Q = 'How can an organisation strengthen its capability to design strategy, execute it through people and performance systems, and sustain results through the appropriate organisational environment?'
RULES = [
    ('Real experience, no confidential detail', 'Use your actual professional experiences as inspiration. Remove identifying and confidential details.'),
    ('Observable problems', 'Write about observable organisational problems. Distinguish what people have seen from what they assume causes it.'),
    ('No solutions yet', 'Describe the problem. Your group develops its detailed responses in the units that follow.'),
]
AREAS = [
    ('design', 'Strategy design', 'Difficulties with strategic clarity, intent, choices and priorities.'),
    ('execution', 'Strategy execution', 'Difficulties with people alignment, accountability, performance management and delivery.'),
    ('sustain', 'Sustaining performance', 'Difficulties with organisational culture, systems, leadership practices and maintaining improvements.'),
]
MF = [('behaviours', 'Observable behaviours', 'What people did, or failed to do, that others could see.'),
      ('practices', 'Management practices', 'How managers planned, decided, reviewed and followed through.'),
      ('conditions', 'Organisational conditions', 'The structures, systems, resources and culture people worked within.')]
CHECKS = [
    'Every member contributed real-world observations during the group activity.',
    'The simulated company feels credible and reflects shared professional realities.',
    'The challenges, how they manifested and their consequences for results are described in everyday language across strategy design, strategy execution and sustaining performance.',
    'The Charter describes the problem without prescribing the detailed S2R® solution.',
]
S1 = [('company', 'Simulated company name', 'The name your group agrees for the organisation it will lead throughout CESI. It is used throughout your Capstone Blueprint.', 'The name of your simulated company...', 'in'),
      ('sector', 'Sector or industry', 'The sector or industry your simulated company operates in.', 'The sector or industry...', 'in'),
      ('size', 'Approximate size', 'The approximate number of employees, and other indicators of scale such as sites, countries or annual turnover.', 'Employees, sites, countries, turnover...', 'in'),
      ('activity', 'Main activity or service', 'What your simulated company does or provides.', 'The main activity or service...', 'ta')]

def field(fid, label, q, ph, kind='ta'):
    box = ('<input type="text" class="pc-in" id="pc_%s" data-pc="%s" maxlength="160" placeholder="%s">' % (fid, fid, ph)) if kind == 'in' else \
          ('<textarea class="pc-ta" id="pc_%s" data-pc="%s" placeholder="%s"></textarea>' % (fid, fid, ph))
    return '<div class="pc-f"><label class="pc-l" for="pc_%s">%s</label><div class="pc-q">%s</div>%s</div>' % (fid, label, q, box)

def team_html():
    opts = '<option value="">&ndash; role &ndash;</option>' + ''.join('<option>%s</option>' % r for r in ROLES)
    rows = ''.join('<span class="pc-team-n">%d</span><select class="pc-sel" id="pc_role_%d" data-pc="role_%d" aria-label="Executive role %d">%s</select>'
                   '<input type="text" class="pc-in" id="pc_name_%d" data-pc="name_%d" maxlength="120" placeholder="Member name" aria-label="Member name %d">' % (i + 1, i, i, i + 1, opts, i, i, i + 1) for i in range(10))
    return ('<div class="pc-f"><span class="pc-l">Simulated executive team</span>'
            '<div class="pc-q">Record each member of your group and the executive role assigned to them for the rest of CESI. There is space for up to ten roles; leave unused rows empty. Each role is held by one member.</div>'
            '<div class="pc-team"><span></span><span class="pc-team-h">Executive role</span><span class="pc-team-h">Member</span>' + rows + '</div></div>')

def next_btn(i, label):
    return '<div class="pc-btnrow"><button type="button" class="pc-b" onclick="pcStep(%d)">%s &rarr;</button></div>' % (i, label)

def q1():
    h = '<div class="pc-qh">1 · Challenges experienced</div><div class="pc-q">What challenges have you experienced? List at least four recurring challenges in each area.</div><div class="pc-grid3">'
    for a in AREAS:
        rows = ''.join('<div class="pc-li"><span>%d</span><input type="text" class="pc-in" id="pc_ch_%s_%d" data-pc="ch_%s_%d" maxlength="240" placeholder="%s"></div>'
                       % (j + 1, a[0], j, a[0], j, 'Challenge %d%s' % (j + 1, '' if j < 4 else ' (optional)')) for j in range(6))
        h += '<div class="pc-f pc-area"><span class="pc-l">%s</span><div class="pc-q">%s</div>%s</div>' % (a[1], a[2], rows)
    return h + '</div>'

def q2():
    h = '<div class="pc-qh">2 · How these challenges manifested</div><div class="pc-q">How did or have these challenges manifested? Describe at least two scenarios for each.</div>'
    for m in MF:
        rows = ''.join('<div class="pc-li"><span>%d</span><textarea class="pc-ta pc-ta-s" id="pc_mf_%s_%d" data-pc="mf_%s_%d" placeholder="%s"></textarea></div>'
                       % (j + 1, m[0], j, m[0], j, 'Scenario %d%s' % (j + 1, '' if j < 2 else ' (optional)')) for j in range(3))
        h += '<div class="pc-f"><span class="pc-l">%s</span><div class="pc-q">%s</div>%s</div>' % (m[1], m[2], rows)
    return h

CQ = [('design', 'Strategy design', 'How have unclear strategic intent, choices or priorities cost the organisation results?', 'The results lost through unclear intent, choices and priorities...'),
      ('execution', 'Strategy execution', 'How have gaps in people alignment, accountability, performance management or delivery cost the organisation results?', 'The results lost through gaps in alignment, accountability and delivery...'),
      ('sustain', 'Sustaining performance', 'How have culture, systems, leadership practices or improvements that did not last cost the organisation results over time?', 'The results lost because performance and improvements were not sustained...')]

def q3():
    h = '<div class="pc-qh">3 · Consequences for results</div><div class="pc-q">What consequences have they created? Explain how these challenges have undermined organisational results.</div>'
    for c in CQ:
        h += '<div class="pc-f"><label class="pc-l" for="pc_cq_%s">Consequences in %s</label><div class="pc-q">%s</div><textarea class="pc-ta" id="pc_cq_%s" data-pc="cq_%s" placeholder="%s"></textarea></div>' % (c[0], c[1].lower(), c[2], c[0], c[0], c[3])
    return h

def step3():
    h = ('<div class="pc-qh">1 · The challenges you will address</div><div class="pc-q">Your choices come from your shared experience. Each drop-down list holds the challenges your group recorded for that area in Step 2, question 1. Choose the three challenges in each area your simulated executive team will address in the Strategy2Results® programme.</div><div class="pc-grid3">')
    for a in AREAS:
        h += ('<div class="pc-f pc-area"><span class="pc-l">%s <em class="pc-pickn" id="pc_pickn_%s"></em></span><div id="pc_pick_%s"></div>'
              '<div class="pc-note" id="pc_pickmsg_%s" style="display:none;"></div></div>') % (a[1], a[0], a[0], a[0])
    h += '</div>'
    h += ('<div class="pc-qh">2 · Our central organisational problem</div>'
          '<div class="pc-f"><div class="pc-q">Synthesise the shared experience your group recorded in Step 2 and the nine challenges you have chosen above. Determine the central problem your simulated executive team will address in the Strategy2Results® programme, in strategy design, strategy execution and sustaining performance.</div>'
          '<textarea class="pc-ta" id="pc_problem" data-pc="problem" style="min-height:120px;" placeholder="The central problem your executive team will address..."></textarea></div>')
    return h

def participant_62():
    s1 = ''.join(field(*f) for f in S1[:1]) + team_html() + ''.join(field(*f) for f in S1[1:])
    cards = ''.join('<div class="pc-card"><div class="pc-card-h">%s</div><p>%s</p></div>' % r for r in RULES)
    checks = ''.join('<li>%s</li>' % c for c in CHECKS)
    return (
'<div class="acc open">\n'
'<div class="acc-h" onclick="tA(this)"><span class="acc-t">6.2 — The Problem Charter</span><div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">Capstone Work</span><div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div></div>\n'
'<div class="acc-b cb">\n'
'<p>Your group now creates the organisation it will lead as an executive team for the rest of CESI. You combine the experiences each member brought to the programme into one simulated company that is experiencing disappointing results or difficulty translating its strategic intentions into outcomes, and you set out its challenge in a Problem Charter. From Unit 2 onwards, your group builds the S2R® Capability Blueprint for this company, one section at a time, as each unit is taught.</p>\n'
'<div class="hbox"><p><strong>The challenge question:</strong> ' + CHALLENGE_Q + '</p></div>\n'
'<div class="pc-how"><div class="pc-how-h">How 6.2 works</div><ol>'
'<li>Your group creates its simulated company and records its simulated executive team (Step 1).</li>'
'<li>Each member shares the recurring organisational challenges they have encountered or observed in their work. Your group sets out its shared reality: the challenges in strategy design, strategy execution and sustaining performance, how they manifested and the consequences they created (Step 2).</li>'
'<li>Your group chooses the three challenges in each area it will address and determines its central organisational problem (Step 3).</li>'
'<li>Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</li>'
'<li>In the Charter record you read your group&rsquo;s Charter and select Confirm. Your confirmed Charter becomes Section 1 of your team&rsquo;s Capstone Blueprint.</li>'
'</ol></div>\n'
'<div class="pc-how-h" style="margin-top:4px;">Three ground rules</div>\n'
'<div class="pc-cards">' + cards + '</div>\n'
'<div id="pcTool">\n'
'<div class="pc-tabs"><div class="pc-tab on" onclick="pcStep(0)">Step 1 · Company</div><div class="pc-tab" onclick="pcStep(1)">Step 2 · Shared reality</div><div class="pc-tab" onclick="pcStep(2)">Step 3 · Central problem</div><div class="pc-tab" onclick="pcStep(3)">Charter record</div></div>\n'
'<div class="pc-panel on"><div class="pc-step-h">Step 1 — Create your simulated company</div><p class="pc-step-p">Agree on an organisation name, its industry or sector, its approximate size and its main activity or service. Then record your simulated executive team.</p>' + s1 + next_btn(1, 'Step 2') + '</div>\n'
'<div class="pc-panel"><div class="pc-step-h">Step 2 — Our shared reality</div><p class="pc-step-p">Each member shares relevant experiences. Together, identify the recurring patterns and set out the shared reality of your simulated company.</p>' + q1() + q2() + q3() + next_btn(2, 'Step 3') + '</div>\n'
'<div class="pc-panel"><div class="pc-step-h">Step 3 — Our central problem</div><p class="pc-step-p">Synthesise your shared reality into the problem your executive team will address through CESI.</p>' + step3() + next_btn(3, 'Charter record') + '</div>\n'
'<div class="pc-panel"><div class="pc-step-h">The Charter record</div><p class="pc-step-p">Read your group&rsquo;s Charter against the checks below. When every entry is complete, select Confirm. Your confirmed Charter feeds boxes 1A to 1H of your team&rsquo;s Capstone Blueprint, and the name of your simulated company is used throughout your Blueprint.</p>'
'<ul class="pc-checks">' + checks + '</ul><div id="pcRec"></div></div>\n'
'</div>\n'
'</div></div>\n')

def facilitator_62():
    rules = ''.join('<div class="pc-card"><div class="pc-card-h">%s</div><p>%s</p></div>' % r for r in RULES)
    steps = [
        ('Step 1 — Create your simulated company', 'Organisation name, sector or industry, approximate size and main activity or service. The simulated executive team: each member and the executive role assigned to them, up to ten roles, each role held by one member.'),
        ('Step 2 — Our shared reality', '1. Challenges experienced: at least four recurring challenges in each of strategy design, strategy execution and sustaining performance. · 2. How these challenges manifested: at least two scenarios each for observable behaviours, management practices and organisational conditions. · 3. Consequences for results in each of the three areas.'),
        ('Step 3 — Our central problem', '1. The three challenges in each area the executive team will address in the programme, chosen from drop-down lists of the challenges the group recorded in Step 2. · 2. The central organisational problem: the group&rsquo;s synthesis of its shared experience across strategy design, strategy execution and sustaining performance.'),
        ('The Charter record', 'Each member reads the group&rsquo;s Charter and selects Confirm. The confirmed Charter feeds boxes 1A to 1H of the team&rsquo;s Capstone Blueprint.'),
    ]
    rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % s for s in steps)
    return (
'<div class="acc">\n'
'<div class="acc-h" onclick="tA(this)"><span class="acc-t">6.2 — The Problem Charter</span><div style="display:flex;align-items:center;gap:10px"><span class="acc-meta">Capstone Work</span><div class="arr"><svg viewBox="0 0 12 12"><polyline points="2,4 6,8 10,4"/></svg></div></div></div>\n'
'<div class="acc-b cb">\n'
'<div class="fac-note"><div class="fac-note-label">&#9670; FACILITATOR GUIDANCE — Section 6.2</div>'
'<p><strong>Purpose:</strong> Each group creates the simulated company it will lead as an executive team for the rest of CESI and writes its Problem Charter. The confirmed Charter becomes Section 1 of the group&rsquo;s Capstone Blueprint. From Unit 2 onwards, every section of the Blueprint is built for this company.</p>'
'<p><strong>Before the session:</strong> The groups are set in the Admin Console before Unit 1 opens. Each participant brings examples of recurring organisational challenges from their own work. No group meeting is required before the programme.</p>'
'<p><strong>Introducing the Charter:</strong> Post the challenge question in the chat and take participants through the three ground rules. Then send the groups to their break-out rooms.</p>'
'<p><strong>Your role:</strong> Guide how the work is completed. The Charter is Capstone work and is assessed independently at the capstone.</p></div>\n'
'<div class="fac-note"><div class="fac-note-label">&#9670; PARTICIPANT ACTIVITY — 6.2</div><ol style="margin:6px 0 0 18px;">'
'<li>In Step 1, the group agrees its simulated company: its name, sector or industry, approximate size and main activity or service. It records its simulated executive team: each member and the executive role assigned to them, up to ten roles.</li>'
'<li>In Step 2, each member shares their examples. The group lists at least four recurring challenges in each of strategy design, strategy execution and sustaining performance; describes at least two scenarios each for the observable behaviours, management practices and organisational conditions through which the challenges manifested; and sets out the consequences for results in each area.</li>'
'<li>In Step 3, the group chooses, from drop-down lists of its own Step 2 challenges, the three challenges in each area it will address in the programme, and determines its central organisational problem from its shared experience.</li>'
'<li>The group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page, in the session or after it.</li>'
'<li>In the Charter record, each member reads the Charter and selects Confirm. The confirmed Charter feeds Section 1 of the team&rsquo;s Capstone Blueprint, where the team confirms it together.</li>'
'</ol></div>\n'
'<div class="hbox"><p><strong>The challenge question:</strong> ' + CHALLENGE_Q + '</p></div>\n'
'<h4>Three ground rules</h4>\n<div class="pc-cards">' + rules + '</div>\n'
'<h4>The three steps</h4>\n<div class="pc-tw"><table class="pc-tbl"><thead><tr><th>Step</th><th>What the group agrees</th></tr></thead><tbody>' + rows + '</tbody></table></div>\n'
'</div></div>\n')

CSS_P = open(os.path.join(HERE, 'pc.css'), encoding='utf-8').read()
JS_P = open(os.path.join(HERE, 'pc_p.js'), encoding='utf-8').read()

# ───────── unit1_P.html ─────────
p = rd('unit1_P.html')
i = p.find('</style>'); p = p[:i] + CSS_P + p[i:]
p = rep(p, '<p>The Self Reflection Bias Assessment and Portfolio Artefact</p>', '<p>The Self Reflection Bias Assessment, the Problem Charter and Portfolio Artefact</p>', 'P hero')
p = rep(p, '<div class="acc open">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">Unit Closing Reflection — Portfolio Artefact</span>',
        participant_62() + '<div class="acc open">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">Unit Closing Reflection — Portfolio Artefact</span>', 'P insert 6.2')
p = rep(p, "    var responses=await S2R.loadAll('u1_foundations');\n", "    var responses=await S2R.loadAll('u1_foundations');\n    if(typeof pcInit==='function')pcInit(responses);\n", 'P load hook')
# the tool script, as its own block before </body>
i = p.rfind('</body>'); assert p.find('</html>', i) > 0; p = p[:i] + '<script>\n' + JS_P + '</script>\n' + p[i:]
wr('unit1_P.html', p)

# ───────── unit1_F.html ─────────
f = rd('unit1_F.html')
CSS_F = open(os.path.join(HERE, 'pc_f.css'), encoding='utf-8').read()
i = f.find('</style>'); f = f[:i] + CSS_F + f[i:]
f = rep(f, '<p>The Distortion Lab and the Self Reflection Bias Assessment</p>', '<p>The Distortion Lab, the Self Reflection Bias Assessment and the Problem Charter</p>', 'F hero')
f = rep(f, 'and then in a personal self-assessment (Section 6.1). Do not skip the simulation.',
        'then in a personal self-assessment (Section 6.1), and finally in the group&rsquo;s Problem Charter (Section 6.2), which opens the Capstone. Do not skip the simulation.', 'F section intent')
f = rep(f, '<div class="acc">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">Unit Summary</span>',
        facilitator_62() + '<div class="acc">\n<div class="acc-h" onclick="tA(this)"><span class="acc-t">Unit Summary</span>', 'F insert 6.2')
wr('unit1_F.html', f)

# ───────── capstone_P.html ─────────
c = rd('capstone_P.html')
c = rep(c, "  // === Blueprint structure (approved wording). [Case] is replaced with the cohort's case name. ===\n  var BLUEPRINT = [\n",
"  // === Blueprint structure (approved wording). [Case] is replaced with the team's simulated company (box 1A). ===\n  var BLUEPRINT = [\n"
"    { key:'u1', unit:1, title:'Problem Charter', boxes:[\n"
"      ['1A','Simulated company','The name of your group’s simulated company. It is used throughout your Blueprint.'],\n"
"      ['1B','Simulated executive team','Each member of the executive team of [Case] and the executive role they hold.'],\n"
"      ['1C','Our organisation','The sector or industry, approximate size and main activity or service of [Case].'],\n"
"      ['1D','Challenges experienced','The recurring challenges [Case] has experienced in strategy design, strategy execution and sustaining performance.'],\n"
"      ['1E','How they manifested','The observable behaviours, management practices and organisational conditions through which the challenges of [Case] manifested.'],\n"
"      ['1F','Consequences for results','How the challenges have undermined the results of [Case] in strategy design, strategy execution and sustaining performance.'],\n"
"      ['1G','The challenges we will address','The three challenges in each area the executive team of [Case] will address in the programme.'],\n"
"      ['1H','Our central organisational problem','The central problem the executive team of [Case] will address through CESI.']\n"
"    ]},\n", 'C blueprint u1')
c = rep(c, "  var PULL = {\n", "  var PULL = {\n"
"    u1: { lens:'u1_foundations', rows:[\n"
"      ['1A','pc_company','Problem Charter · Simulated Company'],\n"
"      ['1B','pc_team','Problem Charter · Executive Team'],\n"
"      ['1C','pc_org','Problem Charter · Our Organisation'],\n"
"      ['1D','pc_challenges','Problem Charter · Challenges Experienced'],\n"
"      ['1E','pc_manifest','Problem Charter · How They Manifested'],\n"
"      ['1F','pc_consequences','Problem Charter · Consequences'],\n"
"      ['1G','pc_address','Problem Charter · Challenges We Will Address'],\n"
"      ['1H','pc_problem','Problem Charter · Central Organisational Problem']\n"
"    ]},\n", 'C pull u1')
c = rep(c, "function caseText(t){ return esc(t).split('[Case]').join(esc(S.caseName || 'your case organisation')); }",
        "function caseText(t){ return esc(t).split('[Case]').join(esc(S.caseName || 'your simulated company')); }\n"
        "  // The team's simulated company: box 1A of its Problem Charter.\n"
        "  function teamCompany(){ var l = (S.bp && S.bp.sections) || []; for (var i = 0; i < l.length; i++){ if (l[i].key === 'u1' && l[i].content && String(l[i].content['1A'] || '').trim()) return String(l[i].content['1A']).trim(); } return ''; }", 'C caseText')
c = rep(c, "      S.caseName = (S.data.brief && S.data.brief.case_name) || '';\n      if (S.data.access_open !== true){\n        fatal('Capstone not open yet', 'The capstone opens when Unit 2 opens.');",
        "      S.caseName = teamCompany();\n      if (S.data.access_open !== true){\n        fatal('Capstone not open yet', 'The capstone opens when Unit 1 opens.');", 'C participant case')
c = rep(c, "        S.caseName = (S.bp && S.bp.brief && S.bp.brief.case_name) || '';", "        S.caseName = teamCompany();", 'C admin case')
c = rep(c, "Your team is the executive leadership team of your case organisation. This Blueprint",
        "Your team is the executive leadership team of your simulated company. This Blueprint", 'C header intro')
c = rep(c, "      h += '<h2>' + esc(b.case_name) + '</h2>';\n", "", 'C brief card name')
c = rep(c, "h += '<p class=\"muted\" style=\"margin-bottom:16px;\">' + agreed + ' of 11 sections agreed.</p>';",
        "h += '<p class=\"muted\" style=\"margin-bottom:16px;\">' + agreed + ' of 12 sections agreed.</p>';", 'C agreed count')
c = rep(c, "        '<p class=\"crit\"><strong>Direction</strong> (Units 2–4)",
        "        '<p class=\"crit\"><strong>Problem Charter</strong> (Unit 1): how fully the Blueprint answers the central problem and builds the capabilities the Charter names.</p>' +\n        '<p class=\"crit\"><strong>Direction</strong> (Units 2–4)", 'C criteria charter')
wr('capstone_P.html', c)

# ───────── dashboard_A.html ─────────
a = rd('dashboard_A.html')
a = rep(a, '              <label class="capstone-brief-field"><span class="filter-group__label">Case</span>\n                <input type="text" id="capBriefCase" maxlength="160" placeholder="e.g. Company X or Mining sector"></label>\n', '', 'A case field')
a = rep(a, "      ['capBriefCase','capBriefText','capBriefDue','capBriefShowcase','capBriefVenue'].forEach(", "      ['capBriefText','capBriefDue','capBriefShowcase','capBriefVenue'].forEach(", 'A clear list')
a = rep(a, "      document.getElementById('capBriefCase').value = b.case_name || '';\n", "", 'A load case')
a = rep(a, "      const caseName = (document.getElementById('capBriefCase').value || '').trim();\n", "", 'A read case')
a = rep(a, "      if (!caseName) { if (msg) msg.textContent = 'Enter the case name.'; document.getElementById('capBriefCase').focus(); return; }\n", "", 'A require case')
a = rep(a, "        p_case_name: caseName,\n", "        p_case_name: null,\n", 'A send case')
a = rep(a, "' of 11 agreed</span>'", "' of 12 agreed</span>'", 'A agreed count')
a = rep(a, '<!-- Capstone build: cohort brief (case, brief text, dates), shown on participants\' capstone page -->',
        '<!-- Capstone build: cohort brief (brief text, dates), shown on participants\' capstone page. Each team names its own simulated company in its Problem Charter (Unit 1, part 6.2). -->', 'A comment')
wr('dashboard_A.html', a)

# ───────── dashboard_F.html ─────────
d = rd('dashboard_F.html')
d = rep(d, "      port_3: 'Development Priority'\n    },\n    u2m1_lens2: {",
"      port_3: 'Development Priority',\n"
"      pc_record: 'Problem Charter — record while the group works',\n"
"      pc_company: 'Problem Charter · Simulated Company — confirmed',\n"
"      pc_team: 'Problem Charter · Simulated Executive Team — confirmed',\n"
"      pc_org: 'Problem Charter · Our Organisation — confirmed',\n"
"      pc_challenges: 'Problem Charter · Challenges Experienced — confirmed',\n"
"      pc_manifest: 'Problem Charter · How They Manifested — confirmed',\n"
"      pc_consequences: 'Problem Charter · Consequences for Results — confirmed',\n"
"      pc_address: 'Problem Charter · The Challenges We Will Address — confirmed',\n"
"      pc_problem: 'Problem Charter · Central Organisational Problem — confirmed',\n"
"      confirmed_items: 'Confirmed by the group'\n    },\n    u2m1_lens2: {", 'F labels u1')
d = rep(d, "      { name: 'The Strategic Unclogging Clinic', test:",
        "      { name: 'The Problem Charter',      test: function (k) { return /^pc_(record|company|team|org|challenges|manifest|consequences|address|problem)$/i.test(k); } },\n      { name: 'The Strategic Unclogging Clinic', test:", 'F family')
wr('dashboard_F.html', d)

# ───────── build_collection.js ─────────
b = rd('build_collection.js')
b = rep(b, "'  var CAPSTONE_KEYS={ u2m1_lens1:", "'  var CAPSTONE_KEYS={ u1_foundations:/^(pc_|confirmed_items$)/i, u2m1_lens1:", 'B capstone keys')
wr('build_collection.js', b)
print('built')
