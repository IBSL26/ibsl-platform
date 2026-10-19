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
    ('No solutions yet', 'Describe the problem and the broad capability needs. Your group develops its detailed responses in the units that follow.'),
]
AREAS = [
    ('design', 'Strategy design', 'Difficulties with strategic clarity, intent, choices and priorities.'),
    ('execution', 'Strategy execution', 'Difficulties with people alignment, accountability, performance management and delivery.'),
    ('sustain', 'Sustaining performance', 'Difficulties with organisational culture, systems, leadership practices and maintaining improvements.'),
]
CHECKS = [
    'Every member contributed real-world observations during the group activity.',
    'The simulated company feels credible and reflects shared professional realities.',
    'All four Charter questions are answered.',
    'Strategy design, execution and performance sustainability challenges are described in everyday language.',
    'The Charter describes the problem and broad capability needs, without prescribing the detailed S2R® solution.',
]
# Step 1 to 4 entries: id, label, question, placeholder, kind
S1 = [('company', 'Simulated company name', 'The name your group agrees for the organisation it will lead throughout CESI. It is used throughout your Capstone Blueprint.', 'The name of your simulated company...', 'in'),
      ('sector', 'Sector or industry', 'The sector or industry your simulated company operates in.', 'The sector or industry...', 'in'),
      ('size', 'Approximate size', 'The approximate number of employees, and other indicators of scale such as sites, countries or annual turnover.', 'Employees, sites, countries, turnover...', 'in'),
      ('activity', 'Main activity or service', 'What your simulated company does or provides.', 'The main activity or service...', 'ta'),
      ('results', 'Our strategy-to-results reality', 'What results are falling short? Give a few credible indications of underperformance.', 'The results falling short, with indications of underperformance...', 'ta')]
S2 = [('challenges', '1 · Challenges experienced', 'What challenges have we experienced? Identify recurring strategy design, execution and performance sustainability problems from members’ professional environments.', 'The recurring challenges your group has experienced...'),
      ('manifest', '2 · How these challenges manifest', 'How do these challenges manifest? Describe the observable behaviours, management practices, performance gaps and organisational conditions.', 'What can be seen in behaviours, practices, performance gaps and conditions...'),
      ('consequences', '3 · Consequences for results and culture', 'What consequences do they create? Explain how these challenges undermine organisational results and culture.', 'How results and culture are undermined...'),
      ('capabilities', '4 · Capabilities to strengthen', 'What capabilities need to be strengthened? Identify the broad organisational capabilities that require attention, without prescribing detailed solutions yet.', 'The broad organisational capabilities that require attention...')]
S4 = [('problem', 'Our central organisational problem', 'One clear paragraph describing the simulated company’s disappointing results, the recurring difficulties your group has observed and the broad capabilities that appear to need strengthening.', 'The shared challenge your executive team will explore through CESI...'),
      ('sources', 'Our sources of experience', 'Briefly explain which types of professional experience shaped your simulated company. Disclose no confidential details.', 'The types of professional experience behind your simulated company...')]

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

def participant_62():
    s1 = ''.join(field(*f) for f in S1[:1]) + team_html() + ''.join(field(*f) for f in S1[1:])
    s2 = ''.join(field(f[0], f[1], f[2], f[3]) for f in S2)
    s3 = ''.join(field(a[0], a[1], a[2], 'The challenges of your simulated company in ' + a[1].lower() + '...') for a in AREAS)
    s4 = ''.join(field(f[0], f[1], f[2], f[3]) for f in S4)
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
'<li>Each member shares the recurring organisational challenges they have encountered or observed in their work. Your group answers the four Charter questions (Step 2), combines its experiences into one shared organisational reality (Step 3) and states its central organisational problem (Step 4).</li>'
'<li>Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.</li>'
'<li>In the Charter record you read your group&rsquo;s Charter and select Confirm. Your confirmed Charter becomes Section 1 of your team&rsquo;s Capstone Blueprint.</li>'
'</ol></div>\n'
'<div class="pc-how-h" style="margin-top:4px;">Three ground rules</div>\n'
'<div class="pc-cards">' + cards + '</div>\n'
'<div id="pcTool">\n'
'<div class="pc-tabs"><div class="pc-tab on" onclick="pcStep(0)">Step 1 · Company</div><div class="pc-tab" onclick="pcStep(1)">Step 2 · Four questions</div><div class="pc-tab" onclick="pcStep(2)">Step 3 · Shared reality</div><div class="pc-tab" onclick="pcStep(3)">Step 4 · Central problem</div><div class="pc-tab" onclick="pcStep(4)">Charter record</div></div>\n'
'<div class="pc-panel on"><div class="pc-step-h">Step 1 — Create your simulated company</div><p class="pc-step-p">Agree on an organisation name, its industry or sector, its approximate size, its main activity or service and a few realistic examples of disappointing results. Then record your simulated executive team.</p>' + s1 + next_btn(1, 'Step 2') + '</div>\n'
'<div class="pc-panel"><div class="pc-step-h">Step 2 — Answer the four Charter questions</div><p class="pc-step-p">Each member shares relevant experiences. Together, identify the recurring patterns and answer the four questions for your simulated company.</p>' + s2 + next_btn(2, 'Step 3') + '</div>\n'
'<div class="pc-panel"><div class="pc-step-h">Step 3 — Combine your experiences into a shared organisational reality</div><p class="pc-step-p">Bring your examples together across three everyday areas: challenges in designing strategy, challenges in executing strategy through people and performance, and challenges in sustaining performance through the organisational environment. You do not need to know the DIG Framework at this stage.</p>' + s3 + next_btn(3, 'Step 4') + '</div>\n'
'<div class="pc-panel"><div class="pc-step-h">Step 4 — State the central organisational problem</div><p class="pc-step-p">State the shared challenge your executive team will explore through CESI, and the experience behind it.</p>' + s4 + next_btn(4, 'Charter record') + '</div>\n'
'<div class="pc-panel"><div class="pc-step-h">The Charter record</div><p class="pc-step-p">Read your group&rsquo;s Charter against the checks below. When every entry is complete, select Confirm. Your confirmed Charter feeds boxes 1A to 1K of your team&rsquo;s Capstone Blueprint, and the name of your simulated company is used throughout your Blueprint.</p>'
'<ul class="pc-checks">' + checks + '</ul><div id="pcRec"></div></div>\n'
'</div>\n'
'</div></div>\n')

def facilitator_62():
    rules = ''.join('<div class="pc-card"><div class="pc-card-h">%s</div><p>%s</p></div>' % r for r in RULES)
    steps = [
        ('Step 1 — Create your simulated company', 'Organisation name, sector or industry, approximate size, main activity or service, and a few realistic examples of disappointing results (the strategy-to-results reality). The simulated executive team: each member and the executive role assigned to them, up to ten roles, each role held by one member.'),
        ('Step 2 — Answer the four Charter questions', '1. What challenges have we experienced? · 2. How do these challenges manifest? · 3. What consequences do they create for results and culture? · 4. What capabilities need to be strengthened?'),
        ('Step 3 — Combine experiences into a shared organisational reality', 'Strategy design: strategic clarity, intent, choices and priorities. · Strategy execution: people alignment, accountability, performance management and delivery. · Sustaining performance: organisational culture, systems, leadership practices and maintaining improvements.'),
        ('Step 4 — State the central organisational problem', 'One clear paragraph: the disappointing results, the recurring difficulties observed and the broad capabilities that appear to need strengthening. Then the sources of experience, with no confidential details.'),
        ('The Charter record', 'Each member reads the group&rsquo;s Charter and selects Confirm. The confirmed Charter feeds boxes 1A to 1K of the team&rsquo;s Capstone Blueprint.'),
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
'<li>In Step 1, the group agrees its simulated company: its name, sector or industry, approximate size, main activity or service and the results falling short. It records its simulated executive team: each member and the executive role assigned to them, up to ten roles.</li>'
'<li>In Step 2, each member shares their examples and the group answers the four Charter questions.</li>'
'<li>In Step 3, the group combines its experiences across strategy design, strategy execution and sustaining performance.</li>'
'<li>In Step 4, the group states its central organisational problem and its sources of experience.</li>'
'<li>The group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page, in the session or after it.</li>'
'<li>In the Charter record, each member reads the Charter and selects Confirm. The confirmed Charter feeds Section 1 of the team&rsquo;s Capstone Blueprint, where the team confirms it together.</li>'
'</ol></div>\n'
'<div class="hbox"><p><strong>The challenge question:</strong> ' + CHALLENGE_Q + '</p></div>\n'
'<h4>Three ground rules</h4>\n<div class="pc-cards">' + rules + '</div>\n'
'<h4>The four steps</h4>\n<div class="pc-tw"><table class="pc-tbl"><thead><tr><th>Step</th><th>What the group agrees</th></tr></thead><tbody>' + rows + '</tbody></table></div>\n'
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
"      ['1D','Our strategy-to-results reality','The results [Case] is falling short on, with credible indications of underperformance.'],\n"
"      ['1E','Challenges experienced','The recurring strategy design, execution and performance sustainability challenges [Case] experiences.'],\n"
"      ['1F','How they manifest','The observable behaviours, management practices, performance gaps and organisational conditions at [Case].'],\n"
"      ['1G','Consequences for results and culture','How these challenges undermine the results and culture of [Case].'],\n"
"      ['1H','Capabilities to strengthen','The broad organisational capabilities [Case] must strengthen.'],\n"
"      ['1I','Shared organisational reality','The challenges of [Case] across strategy design, strategy execution and sustaining performance.'],\n"
"      ['1J','Our central organisational problem','The shared challenge the executive team of [Case] explores through CESI.'],\n"
"      ['1K','Our sources of experience','The types of professional experience that shaped [Case].']\n"
"    ]},\n", 'C blueprint u1')
c = rep(c, "  var PULL = {\n", "  var PULL = {\n"
"    u1: { lens:'u1_foundations', rows:[\n"
"      ['1A','pc_company','Problem Charter · Simulated Company'],\n"
"      ['1B','pc_team','Problem Charter · Executive Team'],\n"
"      ['1C','pc_org','Problem Charter · Our Organisation'],\n"
"      ['1D','pc_reality','Problem Charter · Strategy-to-Results Reality'],\n"
"      ['1E','pc_challenges','Problem Charter · Challenges Experienced'],\n"
"      ['1F','pc_manifest','Problem Charter · How They Manifest'],\n"
"      ['1G','pc_consequences','Problem Charter · Consequences'],\n"
"      ['1H','pc_capabilities','Problem Charter · Capabilities to Strengthen'],\n"
"      ['1I','pc_shared','Problem Charter · Shared Organisational Reality'],\n"
"      ['1J','pc_problem','Problem Charter · Central Organisational Problem'],\n"
"      ['1K','pc_sources','Problem Charter · Sources of Experience']\n"
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
"      pc_reality: 'Problem Charter · Strategy-to-Results Reality — confirmed',\n"
"      pc_challenges: 'Problem Charter · Challenges Experienced — confirmed',\n"
"      pc_manifest: 'Problem Charter · How They Manifest — confirmed',\n"
"      pc_consequences: 'Problem Charter · Consequences for Results and Culture — confirmed',\n"
"      pc_capabilities: 'Problem Charter · Capabilities to Strengthen — confirmed',\n"
"      pc_shared: 'Problem Charter · Shared Organisational Reality — confirmed',\n"
"      pc_problem: 'Problem Charter · Central Organisational Problem — confirmed',\n"
"      pc_sources: 'Problem Charter · Sources of Experience — confirmed',\n"
"      confirmed_items: 'Confirmed by the group'\n    },\n    u2m1_lens2: {", 'F labels u1')
d = rep(d, "      { name: 'The Strategic Unclogging Clinic', test:",
        "      { name: 'The Problem Charter',      test: function (k) { return /^pc_(record|company|team|org|reality|challenges|manifest|consequences|capabilities|shared|problem|sources)$/i.test(k); } },\n      { name: 'The Strategic Unclogging Clinic', test:", 'F family')
wr('dashboard_F.html', d)

# ───────── build_collection.js ─────────
b = rd('build_collection.js')
b = rep(b, "'  var CAPSTONE_KEYS={ u2m1_lens1:", "'  var CAPSTONE_KEYS={ u1_foundations:/^(pc_|confirmed_items$)/i, u2m1_lens1:", 'B capstone keys')
wr('build_collection.js', b)
print('built')
