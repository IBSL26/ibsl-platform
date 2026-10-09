# -*- coding: utf-8 -*-
"""Unit 5 amendments of 9 October 2026 — participant file, on Carol's word.
Usage: python3 amend2_p.py <participant file written by amend_p.py> <new file>
Run it from this folder: it reads u5c_content.py, u5b_content.py, u5_content.py and u5c.css.
Chain: file before the three-way match -> build_p.py -> amend_p.py -> amend2_p.py.
Every change is an exact replacement that must match the number of times given, or the build stops. Line endings (CRLF) and UTF-8 are kept."""
import sys, os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import u5b_content as B
import u5c_content as D
import u5_content as C
src, out = sys.argv[1], sys.argv[2]
def read(name): return open(os.path.join(HERE, name), 'rb').read().decode('utf-8').replace('\r\n', '\n')
h = open(src, 'rb').read().decode('utf-8')
assert h.count('\r\n') == h.count('\n'), 'expected CRLF line endings'
h = h.replace('\r\n', '\n')
h0 = h
def rep(old, new, count=1):
    global h
    n = h.count(old)
    assert n == count, 'expected %d match(es), found %d: %s' % (count, n, old[:110])
    h = h.replace(old, new)
def cut(start, end, new):
    global h
    assert h.count(start) == 1 and h.count(end) == 1, (h.count(start), h.count(end), start[:60])
    i, j = h.index(start), h.index(end)
    assert i < j
    h = h[:i] + new + h[j:]
def how(title, steps, *closes):
    return ('<div class="u5-how"><div class="u5-how-h">' + title + '</div><ol>' + ''.join('<li>' + s + '</li>' for s in steps) + '</ol>' +
            ''.join('<p>' + c + '</p>' for c in closes if c) + '</div>\n')
dumps = lambda x: json.dumps(x, ensure_ascii=False, separators=(',', ':'))

# ── 0. CSS ────────────────────────────────────────────────────────────────────────────────────────
i = h.index('</style>')
h = h[:i] + read('u5c.css') + h[i:]

# ── 1. Part 3.1: the participant scores first; one instruction block ───────────────────────────────
cut('  <h4>How the profile is read</h4>\n',
    '  <div class="ref-block" style="margin-top:18px;"><div class="ref-label">&#x270E; Reflection &mdash; OCEAVL</div>',
    '  ' + how(D.OC_TITLE_P, D.OC_STEPS_P, D.OC_EVERY, B.OC_CLOSE) +
    '  <h4>Your assessment</h4>\n  <div id="ocGrid"></div>\n  <div id="ocProfile"></div>\n  <div id="ocConf"></div>\n'
    '  <h4>' + D.OC_DIMS_H + '</h4>\n  <p>' + D.OC_DIMS_P + '</p>\n' + D.oceavl_dims())
# the scoring grid: one row for each dimension, with what the dimension covers
rep("""  host.innerHTML='<div class="u5-oc"><div class="u5-oc-row"><div class="u5-oc-g">'+OC.map(function(d,j){
    return '<div><label for="oc_s_'+j+'">'+u5esc(d.name)+'</label><select class="u5-sel" id="oc_s_'+j+'" onchange="ocIn('+j+',this.value)">'+
      '<option value="0">&mdash;</option>'+[1,2,3,4,5].map(function(v){return '<option value="'+v+'"'+(U5.oc[j]===v?' selected':'')+'>'+v+'</option>';}).join('')+'</select></div>';
  }).join('')+'</div></div></div>';""",
    """  host.innerHTML='<div class="u5-oc">'+OC.map(function(d,j){
    return '<div class="u5-oc-r"><label for="oc_s_'+j+'"><span class="u5-oc-n">'+u5esc(d.name)+'</span><span class="u5-oc-d">'+u5esc(d.desc)+'</span></label><select class="u5-sel" id="oc_s_'+j+'" onchange="ocIn('+j+',this.value)">'+
      '<option value="0">Select a score</option>'+[1,2,3,4,5].map(function(v){return '<option value="'+v+'"'+(U5.oc[j]===v?' selected':'')+'>'+OC_SCALE[v]+'</option>';}).join('')+'</select></div>';
  }).join('')+'</div>';""")
rep("var OC_NAME='OCEAVL · My Scores';", "var OC_NAME='OCEAVL · My Scores';\nvar OC_SCALE=" + dumps({str(k): v for k, v in D.OC_SCALE.items()}) + ";")

# ── 2. Section 4: the old 4.3 becomes 4.1, with the old 4.1 as notes inside it; 4.2 follows ────────
HEAD = '<div class="acc%s">\n<div class="acc-h" onclick="tA(this)">\n  <span class="acc-t">%s</span>'
s1 = HEAD % (' open', '4.1 &mdash; The Converging Zone: What Collective Intelligence Creates')
s2 = HEAD % (' open', '4.2 &mdash; Collective Intelligence Across the Leadership Team')
s3 = HEAD % ('', '4.3 &mdash; Leading Change with One Voice')
end = '<div class="mod-nav">\n  <button class="btn prev" onclick="showMod(2,null)">'
for s in (s1, s2, s3, end): assert h.count(s) == 1, s[-60:]
i1, i2, i3, ie = h.index(s1), h.index(s2), h.index(s3), h.index(end)
assert i1 < i2 < i3 < ie
a1, a2, a3 = h[i1:i2], h[i2:i3], h[i3:ie]
g0 = '  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:16px 0;">'
g1 = '  <div class="ref-block"><div class="ref-label">&#x270E; Reflection</div>\n    <label class="wp-label" style="margin-top:0;" for="ref8">'
assert a1.count(g0) == 1 and a1.count(g1) == 1
grid = a1[a1.index(g0):a1.index(g1)]
assert grid.count('<div') == grid.count('</div>') and 'With Collective Intelligence' in grid and 'Without Collective Intelligence' in grid
p1 = ('  <p>The 4 Checks describe what one group of people needs from you. Most changes reach a group through several leaders at once. People hear from you, watch your fellow leaders, and compare. '
      'Where you differ, the group takes the difference as the real message.</p>\n')
p2 = '  <p>In the Converging Zone, your leadership team makes four commitments that no single function can make alone. Each one protects a check. Expand each commitment.</p>\n'
assert a3.count(p1 + p2) == 1
n1 = a3.replace(s3, HEAD % (' open', '4.1 &mdash; ' + D.T41)).replace(
    p1 + p2, p1 + '  <div class="chg-h">' + D.ONE_H + '</div>\n  <p>' + D.ONE_P + '</p>\n' + grid + '  <div class="chg-h">' + D.FOUR_H + '</div>\n' + p2)
assert '<span class="acc-meta">' + D.T41_META + '</span>' in n1 and 'id="ref15"' in n1
h = h[:i1] + n1 + a2 + h[ie:]

# ── 3. Part 4.2 in plain words ────────────────────────────────────────────────────────────────────
rep('  <p style="margin-bottom:14px;">Click your own role first. Then explore the roles most closely connected to yours.</p>\n  <p>' + B.HOT_INTRO_P + '</p>\n', D.teach42('p'))
for n in range(10):
    old = B.role_detail(n, 'p', C.role_detail(n, 'p')); rep(old, D.role_detail2(n, 'p', old))

# ── 4. Section 5: the group states its Shift, Stake and Step, then the ACE-IT behaviours it expects from the leadership team ──
#    (Carol, 9 October, fourth round). The cue-and-trigger toolkit, the personal watch list and the 30-Day Behavioural Commitment have left.
import u5d_content as E
G3, GA = E.guide_3s(h), E.guide_ace(h)        # the page's own lesson text from parts 1.3.1 and 1.3.4
rep('  <h2>' + B.T5 + '</h2>\n  <p>' + B.HERO5_P + '</p>', '  <h2>' + E.T5 + '</h2>\n  <p>' + E.HERO_P + '</p>')
rep('<div class="u5-how"><div class="u5-how-h">' + B.SEC5_HOW_H + '</div><ul>' + ''.join('<li>' + x + '</li>' for x in B.SEC5_HOW_P) + '</ul></div>\n\n', E.how_box('p'))
u3box = ('<div class="u5-u3">\n<div class="chg-h" style="margin-top:6px;">From Unit 3 &middot; your group&rsquo;s confirmed Start and Stop lists</div>\n<div id="u5KissP"></div>\n'
         '<div class="u5-btnrow"><button type="button" class="u5-b" onclick="u5Bring(true)">Bring in from my Unit 3 page</button></div>\n<div class="u5-note" id="u5BringMsg" style="display:none;"></div>\n</div>\n')
assert h.count(E.GROUP_P) == 1 and h.count(u3box) == 1
s5 = ('<div class="step-tabs">\n'
      '  <div class="step-tab active" onclick="showSP(\'m\',this)"><div class="step-num">Step 1</div><div class="step-name">' + E.STEP_NAMES[0] + '</div></div>\n'
      '  <div class="step-tab" onclick="showSP(1,this)"><div class="step-num">Step 2</div><div class="step-name">' + E.STEP_NAMES[1] + '</div></div>\n'
      '</div>\n\n<div class="step-panel active" id="spm">\n' + E.GROUP_P + how('Capstone work &middot; How to complete Step 1 &middot; The 3S Check', E.STEP1_HOW_P) + u3box +
      '<div class="chg-h">Your group&rsquo;s Shift, Stake and Step</div>\n' + ''.join(E.card_3s(g, 'p') for g in G3) +
      '<div class="u5-btnrow"><button type="button" class="u5-b ok" onclick="u5Step(1)">Go to Step 2 &middot; ' + E.STEP_NAMES[1] + ' &rarr;</button></div>\n</div>\n\n'
      '<div class="step-panel" id="sp1">\n' + how('Capstone work &middot; How to complete Step 2 &middot; ACE-IT', E.STEP2_HOW_P) +
      '<div class="chg-h">' + E.TEAM_OC_H + '</div>\n<div id="u5TeamOc"><div class="u5-from"><i>' + E.TEAM_OC_WAIT + '</i></div></div>\n'
      '<div class="u5-btnrow"><button type="button" class="u5-b" onclick="u5TeamOc(true)">Read my team&rsquo;s profile again</button></div>\n'
      '<div class="chg-h">The behaviours your group expects from the leadership team</div>\n' + ''.join(E.card_ace(g, 'p') for g in GA) + '<div id="kitOutP"></div>\n')
cut('<div class="step-tabs">', '<div class="hbox" style="margin-top:18px;"><p><strong>Unit Outcome:</strong>', s5)
rep(B.OUTCOME_TAIL_P, E.OUTCOME_TAIL_P)
rep('<li>' + E.SLO5_1_OLD + '</li>', '<li>' + E.SLO5_1_NEW + '</li>')

# ── 5. Script ─────────────────────────────────────────────────────────────────────────────────────
js_a = '/* ── Section 5 · the Alignment Toolkit: Your Watch List (me) and Team Alignment Plan (team) ───── */'
js_b = "document.addEventListener('DOMContentLoaded',function(){\n  U5.oc=ocBlank();\n  var k=u5el('u5KissP');if(k)k.innerHTML=u5KissHtml('','');\n  u5DrawAll();\n});"
assert h.count(js_a) == 1 and h.count(js_b) == 1 and h.index(js_a) < h.index(js_b)
new_js = (read('u5d_p.js').strip('\n').replace('/*FIELDS*/[]', dumps([list(f) for f in E.FIELDS])).replace('/*NAMES*/[]', dumps(E.NAMES)).replace('/*REC*/{}', dumps(E.REC_H))
          .replace("/*WAIT*/''", dumps(E.TEAM_OC_WAIT)).replace("/*NONE*/''", dumps(E.TEAM_OC_NONE)))
assert '/*' + 'FIELDS' not in new_js and '</script' not in new_js
h = h[:h.index(js_a)] + new_js + h[h.index(js_b) + len(js_b):]
rep('var CHECKS=' + dumps(B.CHECKS) + ';\n', '')
rep('var KIT=' + dumps(B.KIT_JS) + ';\n', '')
rep("var KIT_NAMES=CHECKS.map(function(c){return 'Alignment Plan · '+c.name;});\nvar KIT_KEYS=CHECKS.map(function(c){return 'kit_'+c.id;});\n", '')
rep("var U5={conf:[],ready:false,oc:[],me:{},team:{}};", "var U5={conf:[],ready:false,oc:[],s5:{}};")
rep("   Section 5 · Step 2: Your Watch List (individual, Portfolio work). Saves as the participant works.\n"
    "   Section 5 · Step 3: Team Alignment Plan (group, Capstone work). Confirm writes the four \"Alignment Plan · …\" names into confirmed_items.\n"
    "   An edit after confirmation takes the names out again. The Unit 3 Start and Stop lists are read only. */",
    "   Section 5: the 3S Check and ACE-IT for the group's strategy (group, Capstone work). Confirm writes the two \"Alignment Plan · …\" names into confirmed_items.\n"
    "   An edit after confirmation takes the names out again. The Unit 3 Start and Stop lists and the team's OCEAVL profile are read only. */")
# routines with their meanings: in the data, on the profile and on the printed copy
rep('var OC=' + dumps(B.OCEAVL) + ';', 'var OC=' + dumps(D.OCEAVL2) + ';')
rep("""        '<div class="u5-lv-g"><div><b>Risk</b>'+u5esc(x.g.risk)+'</div><div><b>Response</b>'+u5esc(x.g.resp)+'</div><div><b>Routines</b>'+u5esc(x.g.rout)+'</div></div></div>';""",
    """        '<div class="u5-lv-g u5-lv-g2"><div><b>Risk</b>'+u5esc(x.g.risk)+'</div><div><b>Response</b>'+u5esc(x.g.resp)+'</div></div>'+
        '<div class="u5-rt"><b>""" + D.ROUT_H + """</b><ul>'+x.g.rd.map(function(r){return '<li><strong>'+u5esc(r[0])+'.</strong> '+u5esc(r[1])+'</li>';}).join('')+'</ul></div></div>';""")
rep("""<p><b>Routines:</b> '+u5esc(x.g.rout)+'</p>';}).join('')""",
    """<p><b>Routines:</b></p>'+x.g.rd.map(function(r){return '<p>&bull; <b>'+u5esc(r[0])+'.</b> '+u5esc(r[1])+'</p>';}).join('');}).join('')""")
m = re.search(r'var SUMMARY=(\[.*?\]);\n', h, re.S); S = json.loads(m.group(1)); assert len(S) == 5
assert S[3]['body'].count(D.SUMMARY_P4_OLD) == 1; S[3]['body'] = S[3]['body'].replace(D.SUMMARY_P4_OLD, D.SUMMARY_P4_NEW)
assert S[4]['body'] == B.SUMMARY_P5; S[4]['body'] = E.SUMMARY_P5
h = h[:m.start()] + 'var SUMMARY=' + json.dumps(S, ensure_ascii=False) + ';\n' + h[m.end():]
rep('var KEYS=["ref1","ref2","ref3","ref4","ref5","ref6","ref8","ref9","ref10","ref11","ref12","ref13","ref15","ref16","syn_30day"];',
    'var KEYS=["ref1","ref2","ref3","ref4","ref5","ref6","ref9","ref10","ref11","ref12","ref13","ref15","ref16"];')

# ── 6. Checks, then write with CRLF ───────────────────────────────────────────────────────────────
assert h.count('<script') == h.count('</script>') == h0.count('<script')
body = lambda t: re.sub(r'<script.*?</script>', ' ', re.sub(r'<style.*?</style>', ' ', t, flags=re.S), flags=re.S)
b0, b1 = body(h0), body(h)
assert b1.count('<div') == b1.count('</div>'), 'div balance %d / %d' % (b1.count('<div'), b1.count('</div>'))
ids0 = re.findall(r'\bid="([^"]+)"', b0); ids1 = re.findall(r'\bid="([^"]+)"', b1)
assert len(ids1) == len(set(ids1)), 'an id is used twice'
assert set(ids0) - set(ids1) == {'ref8', 'ref8-saved', 'kitMe', 'kitTeam', 'sp0', 'syn_30day', 'syn_30day-saved'}, set(ids0) - set(ids1)
assert set(ids1) - set(ids0) == {'u5TeamOc'} | {'s5_' + f[0] for f in E.FIELDS}, set(ids1) - set(ids0)
for k in ('lens_id', 'href=', 'showMod(', 'u3m1_lens4'):
    assert h.count(k) == h0.count(k), (k, h0.count(k), h.count(k))
titles = [re.sub(r'&mdash;', '—', t) for t in re.findall(r'<span class="acc-t">([^<]+)</span>', b1)]
assert [t.split(' — ')[0] for t in titles if t[0].isdigit()] == ['1.1', '1.2', '1.3', '1.3.1', '1.3.2', '1.3.3', '1.3.4', '2.1', '2.2', '2.3', '3.1', '4.1', '4.2'], titles
i_g, i_d = b1.index('id="ocGrid"'), b1.index('<details class="u5-dim">')
assert b1.index(D.OC_TITLE_P) < i_g < b1.index('id="ocConf"') < i_d < b1.index('id="ref16"'), 'order of part 3.1'
assert b1.count('<details class="u5-dim">') == 7 and b1.count('How the profile is read') == 0 and b1.count('<div class="u5-rt">') == 21 and b1.count('<li><strong>') >= 63
vis = re.sub(r'<[^>]+>', ' ', b1)
for bad in (r'\blens(es)?\b', r'Save to Portfolio', r'pre-?work', r'automat', r'\b\d+\s*(–|-|&ndash;)?\s*\d*\s*minutes\b', r'facilitation question', r'\bAsk:', r'\bSay:',
            r'rather than', r'instead of', r'in place of', r'Burning Platform', r'High Flammable', r'(?<![\d.])1\.[4-7]\b', r'(?<![\d.])3\.3\b', r'(?<![\d.])4\.3\b', r'Change Transition Map', r'Plenary Synthesis',
            r'COMPASS', r'leverage (zone|point)', r'Change Readiness', r'readiness scan', r'worked scan', r'inclined to set off', r'under each check', r'Alignment Toolkit in Section 5',
            r'Heart · SCARF', r'Hands · STAT', r'four tools', r'watch list', r'Step 3', r'30.Day Behavioural Commitment', r'Save Commitment', r'The (Mind|Heart|Hands|Habit) check fails', r'likely trigger', r'two cues', r'Team Alignment Plan', r'surface for our strategy', r'Alignment Toolkit'):
    assert not re.search(bad, vis, re.I), 'found on the page: ' + bad
open(out, 'wb').write(h.replace('\n', '\r\n').encode('utf-8'))
print('participant file written:', out, len(h))
