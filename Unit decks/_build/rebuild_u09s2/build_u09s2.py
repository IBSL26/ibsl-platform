# -*- coding: utf-8 -*-
"""Unit 9 · Section 2 rework (19 Oct 2026). Surgical edits on the live pages.
Usage: python3 build_u09s2.py <live p> <live f> <out p> <out f>
Section 1: old 1.2 split into 1.2 (with the old 2.1 argument and its reflection ref3), 1.3, 1.4, 1.5; old 1.2.1 removed.
Section 2: new title and opening narrative; 2.1 Three Disciplines and 2.2 Seven Levers, each with people/organisational performance cards.
Section 4: 4.2-4.4 become 4.2 The Unclogging Cycle (REVIEW, REALIGN, RESTORE, The Unclogging Record); 4.5 becomes 4.3.
Section 5: 5.1 drop-downs (Problem Charter challenges; Unit 7 Objectives and Key Results); numbered clog options; 5.4 Simulate the Unclogging Cycle."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from u9s2_content import *

def rd(x): return open(x, encoding='utf-8', newline='').read()
def once(s, old, new):
    n = s.count(old); assert n == 1, 'expected once (%d): %s' % (n, old[:90]); return s.replace(old, new)
def div_end(s, i):
    d = 0
    for m in re.finditer(r'<div\b|</div>', s[i:]):
        d += 1 if m.group() == '<div' else -1
        if d == 0: return i + m.end()
    raise AssertionError('no div end')
def det_end(s, i):
    d = 0
    for m in re.finditer(r'<details\b|</details>', s[i:]):
        d += 1 if m.group() == '<details' else -1
        if d == 0: return i + m.end()
    raise AssertionError('no details end')
def acc_span(s, title):
    assert s.count(title) == 1, 'title count %d: %s' % (s.count(title), title)
    t = s.find(title); a = [m.start() for m in re.finditer(r'<div class="acc(?: open)?"', s[:t])][-1]
    return a, div_end(s, a)
def cb_parts(acc):
    i = acc.find('<div class="acc-b"><div class="cb">'); assert i >= 0
    cs = i + len('<div class="acc-b">'); ce = div_end(acc, cs); be = div_end(acc, i)
    return acc[cs + len('<div class="cb">'):ce - len('</div>')], acc[ce:be - len('</div>')]
def det_inner(s, summary):
    k = s.find('<summary class="u9-sub">' + summary); assert k >= 0, summary
    d = s.rfind('<details', 0, k); e = det_end(s, d)
    blk = s[d:e]; b = blk.find('<div class="u9-det-b">') + len('<div class="u9-det-b">')
    return blk[b:-len('</div></details>')], e
ARR = '<div class="arr"><svg viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg></div>'
def acc_html(title, meta, body, tail='', op=False):
    if not body.endswith('\n'): body += '\n'
    return ('<div class="acc%s">\n<div class="acc-h" onclick="tA(this)"><div><div class="acc-t">%s</div><div class="acc-meta">%s</div></div>%s</div>\n'
            '<div class="acc-b"><div class="cb">\n%s</div>%s</div></div>\n') % (' open' if op else '', title, meta, ARR, body, tail)
def det_html(summary, inner):
    if not inner.endswith('\n'): inner += '\n'
    return '<details class="u9-det"><summary class="u9-sub">%s</summary><div class="u9-det-b">\n%s</div></details>\n' % (summary, inner)

CSS = ('.u9-open{margin:6px 0 22px;}.u9-open p{font-size:14px;line-height:1.85;color:rgba(255,255,255,.78);margin:0 0 12px;}'
       '.lever-body .u9-lv-how{margin-top:10px;}.lever-body .u8v-hc{margin:10px 0 4px;}.step-panel .u8v-hc{margin:4px 0 16px;}\n')

def build(s, v):
    s = s.replace('</style>', CSS + '</style>', 1)
    # ── Section 1 ──
    if v == 'f': s = once(s, S1_GUIDE_OLD, S1_GUIDE_NEW)
    a21, e21 = acc_span(s, '2.1 &mdash; Clogs Are Design Signals')
    old21 = s[a21:e21]
    if v == 'p':
        r = old21.find('<div class="ref-block"><div class="ref-label">&#x270E; Reflection &mdash; Where Is Your System Not Yet Ready?')
        ref3 = old21[r:div_end(old21, r)]
        assert 'id="ref3"' in ref3
    a, e = acc_span(s, '1.2 &mdash; The 7-Clog Diagnostic Map')
    inner, tail = cb_parts(s[a:e])
    U, _ = det_inner(inner, 'Understanding Where Performance Becomes Constrained')
    C, _ = det_inner(inner, 'The Seven Performance Clogs')
    L, _ = det_inner(inner, '1.2.2 &mdash;')
    W, we = det_inner(inner, '1.2.3 &mdash;')
    rest = inner[we:]
    assert 'Closing Diagnostic Principle' in rest and '1.2.1' not in rest
    new = (acc_html(S1_PARTS['u'][0], S1_PARTS['u'][1], S1_OPEN + U + ('\n' + ref3 + '\n' if v == 'p' else ''), ('\n' + S1_REF3_PA) if v == 'f' else '')
           + '\n' + acc_html(S1_PARTS['c'][0], S1_PARTS['c'][1], C)
           + '\n' + acc_html(S1_PARTS['l'][0], S1_PARTS['l'][1], L)
           + '\n' + acc_html(S1_PARTS['w'][0], S1_PARTS['w'][1], W + rest.strip('\n'), tail))
    s = s[:a] + new + s[e:]
    # ── Section 2 ──
    s = once(s, '<h2>Why Clogs Are Predictable Features of Execution</h2>', '<h2>%s</h2>' % S2_H2)
    s = once(s, '<p>Understanding why execution friction is the inevitable consequence of system misalignment &mdash; and introducing the 7 Strategic Unclogging Levers as the leadership toolkit for restoring execution flow.</p>', '<p>%s</p>' % S2_SUB)
    if v == 'f':
        for st, nw in ((S2_GUIDE_P2_OLD_START, S2_GUIDE_P2_NEW), (S2_GUIDE_P3_OLD_START, S2_GUIDE_P3_NEW)):
            assert s.count(st) == 1, st
            i = s.find(st); j = s.find('</p>', i) + 4; s = s[:i] + nw + s[j:]
    a, e = acc_span(s, '2.1 &mdash; Clogs Are Design Signals')
    s = s[:a] + S2_OPEN + '\n' + s[e:].lstrip('\n')
    a, e = acc_span(s, '2.2 &mdash; Three Disciplines of Execution Engineering')
    acc = s[a:e]
    acc = acc.replace('2.2 &mdash; Three Disciplines of Execution Engineering', '2.1 &mdash; Three Disciplines of Execution Engineering')
    panels = [m.start() for m in re.finditer(r'<div class="step-panel( active)?">', acc)]
    assert len(panels) == 3
    for k in (2, 1, 0):
        st = panels[k]; en = div_end(acc, st)
        num, nm, h5, old_ps, new_ps, ppl, org, close = DISCIPLINES[k]
        body = ('<h5>%s</h5>\n' % h5) + ''.join('<p>%s</p>\n' % x for x in old_ps + new_ps) + cards(ppl, org) + '\n' + (('<p>%s</p>\n' % close) if close else '')
        open_tag = acc[st:acc.find('>', st) + 1]
        acc = acc[:st] + open_tag + '\n' + body + '</div>' + acc[en:]
    s = s[:a] + acc + s[e:]
    a, e = acc_span(s, '2.3 &mdash; The 7 Strategic Unclogging Levers')
    acc = s[a:e].replace('2.3 &mdash; The 7 Strategic Unclogging Levers', '2.2 &mdash; The 7 Strategic Unclogging Levers')
    g = acc.find('<div class="lever-grid">'); ge = div_end(acc, g)
    grid = '<div class="lever-grid">\n'
    for i, (n, nm, role, summ, why, how, ppl, org) in enumerate(LEVERS):
        grid += ('\n  <div class="lever-card" onclick="toggleLever(this)"%s>\n'
                 '    <div class="lever-head"><div class="lever-meta"><div class="lever-num">Lever %s</div><div class="lever-name">%s</div><div class="lever-role">%s</div></div><div class="lever-arr">&#9660;</div></div>\n'
                 '    <div class="lever-bar"></div>\n'
                 '    <div class="lever-body"><p>%s</p><div class="lever-why">%s</div><p class="u9-lv-how"><strong>How it works.</strong> %s</p>%s</div>\n'
                 '  </div>\n') % (' style="grid-column:1/-1;"' if i == 6 else '', n, nm, role, summ, why, how, cards(ppl, org))
    grid += '\n</div>'
    acc = acc[:g] + grid + acc[ge:]
    s = s[:a] + acc + s[e:]
    # ── Section 3 reference ──
    s = s.replace('(part 1.2.2)', '(part 1.4)')
    # ── Section 4 ──
    s = once(s, S4_41_OLD, S4_41_NEW)
    if v == 'f': s = once(s, S4_GUIDE_OLD, S4_GUIDE_NEW)
    a2, e2 = acc_span(s, '4.2 &mdash; REVIEW: Establish the Performance Reality')
    a3, e3 = acc_span(s, '4.3 &mdash; REALIGN: Establish Collective Executive Ownership')
    a4, e4 = acc_span(s, '4.4 &mdash; RESTORE: Activate the Seven Unclogging Levers')
    assert s[e2:a3].strip() == '' and s[e3:a4].strip() == ''
    (rv, t2), (ra, t3), (rs, t4) = cb_parts(s[a2:e2]), cb_parts(s[a3:e3]), cb_parts(s[a4:e4])
    rv = once(rv, '<div class="u9-done"><strong>REVIEW is complete when', S4_REVIEW_CARDS + '\n<div class="u9-done"><strong>REVIEW is complete when')
    rv = rv.rstrip('\n') + '\n' + S4_REC_LINES[0] + '\n'
    ra = once(ra, 'so individuals and teams can deliver their contributions?</p></div>', 'so individuals and teams can deliver their contributions?</p>' + S4_REALIGN_PEOPLE_ADD + '</div>')
    ra = once(ra, 'so the enterprise can produce the intended result?</p></div>', 'so the enterprise can produce the intended result?</p>' + S4_REALIGN_ORG_ADD + '</div>')
    ra = ra.rstrip('\n') + '\n' + S4_REC_LINES[1] + '\n'
    rs = rs.rstrip('\n') + '\n' + S4_RESTORE_CARDS + '\n' + S4_REC_LINES[2] + '\n'
    body = S4_INTRO + det_html(S4_SUBS[0], rv) + det_html(S4_SUBS[1], ra) + det_html(S4_SUBS[2], rs) + S4_RECORD
    s = s[:a2] + acc_html(S4_TITLE, S4_META, body, t2 + t3 + t4) + s[e4:]
    s = once(s, S4_WE_OLD, S4_WE_NEW)
    # ── Section 5 ──
    d = S5[v]
    for k in ('how1', 'how3', 'intro'): s = once(s, d[k + '_old'], d[k + '_new'])
    s = once(s, S5_OUT_OLD, S5_OUT_NEW)
    if v == 'f':
        s = once(s, S5_GUIDE_OLD, S5_GUIDE_NEW)
        s = once(s, S5_CLOSE_OLD, S5_CLOSE_NEW)
        s = once(s, '<span>State the challenge as the group originally understood it.</span>', '<span>The group selects the challenge from its Problem Charter.</span>')
        s = once(s, '<b>Strategic connection</b><span>Which strategic Objective and Key Result or KPI developed during CESI does this challenge affect?</span>', '<b>Strategic connection</b><span>The group selects the strategic Objective and Key Result the challenge affects.</span>')
    else:
        i = s.find('<div class="u9-h">Your group&rsquo;s Key Results from Unit 7, for reference</div>'); assert i > 0
        j = s.find('<p>Use existing Capstone performance information', i); assert j > i
        s = s[:i] + '<div class="u9-tagline">Group response</div>\n' + S5_P51_FIELDS + s[j:]
        si = s.find('<select class="u9-sel" id="u9_cl_clog"'); se = s.find('</select>', si)
        sel = s[si:se]
        for n, c in enumerate(['Structural Misfit', 'Capability Gaps', 'Decision Bottlenecks', 'Misaligned Metrics &amp; Incentives', 'Cultural Resistance', 'Technology / Infrastructure Lag', 'Leadership Avoidance']):
            sel = once(sel, '<option>%s</option>' % c, '<option value="%s">%02d · %s</option>' % (c, n + 1, c))
        s = s[:si] + sel + s[se:]
    s = once(s, S5_54_OLD, S5_54_NEW)
    i = s.find(S5_54_NEW); mm = re.compile(r'<div class="acc-b"><div class="cb">\r?\n').search(s, i); assert mm and mm.start() - i < 400; j = mm.end()
    s = s[:j] + d['s54'] + s[j:]
    # ── Section 5 script (participant) ──
    if v == 'p':
        s = once(s, '["ch_challenge", "Selected original challenge", "p1", false, "t", "The challenge, as your group first described it...", "State the challenge as your group originally understood it."], ["ch_link", "Strategic connection", "p1", false, "t", "The Objective, and the Key Result or KPI it affects...", "Which strategic Objective and Key Result or KPI developed during CESI does this challenge affect?"]',
                    '["ch_challenge", "Selected original challenge", "p1", false, "s", [], "Select the challenge from your group\u2019s Problem Charter."], ["ch_link", "Strategic connection", "p1", false, "s", [], "Which strategic Objective and Key Result does this challenge affect?"]')
        s, n = re.subn(r"Part 5\.1 shows the group's Unit 7 Key Results for reference(\r?\n)   \(u3m1_lens6, __ex_work o1_kr/o1_owner/o2_kr/o2_owner\)\.",
                       lambda m: "Part 5.1 offers two drop-downs: the challenges of the group's" + m.group(1) + "   Problem Charter (u1_foundations, __pc_work pick/ch) and its Unit 7 Objectives and Key Results (u3m1_lens6, __ex_work o1_obj/o1_kr/o2_obj/o2_kr).", s); assert n == 1
        s = once(s, "function u9Fill(){U9F.forEach(function(f){var el=u9el('u9_'+f[0]);if(el)el.value=U9.w[f[0]]||'';});}",
                    "function u9Fill(){U9F.forEach(function(f){var el=u9el('u9_'+f[0]);if(!el)return;var v=U9.w[f[0]]||'';"
                    "if(el.tagName==='SELECT'&&v&&![].some.call(el.options,function(o){return o.value===v;})){var o=document.createElement('option');o.value=v;o.textContent=v;el.appendChild(o);}el.value=v;});}")
        i = s.find("/* The group's Unit 7 Key Results, read only, for reference in part 5.1. */"); j = s.find('function u9Init(', i); assert 0 < i < j
        s = s[:i] + U9_EARLIER_JS + s[j:]
    # ── Unit Summary ──
    if v == 'p':
        for arc, txt in SUM_P.items():
            s, n = re.subn(r'(\{arc:"%s &mdash;[^"]*",title:"[^"]*",body:")[^"]*(")' % arc, lambda m: m.group(1) + txt + m.group(2), s); assert n == 1, arc
    else:
        for arc, txt in SUM_F.items():
            s, n = re.subn(r'(>%s — [A-Za-z ]+</div><p style="[^"]*">)[^<]*(</p>)' % arc, lambda m: m.group(1) + txt + m.group(2), s); assert n == 1, arc
    return s

U9_EARLIER_JS = r"""/* Part 5.1 drop-downs: the challenges of the group's Problem Charter, and the group's Unit 7 Objectives and Key Results. */
function u9Opts(sel,groups,saved,ph){
  if(!sel)return;
  var vals=[],h='<option value="">'+ph+'</option>';
  groups.forEach(function(g){var o=g[1].map(function(x){vals.push(x[1]);return '<option value="'+u9esc(x[1])+'">'+u9esc(x[0])+'</option>';}).join('');h+=g[0]?'<optgroup label="'+u9esc(g[0])+'">'+o+'</optgroup>':o;});
  if(saved&&vals.indexOf(saved)<0)h+='<option value="'+u9esc(saved)+'">'+u9esc(saved)+'</option>';
  sel.innerHTML=h;sel.value=saved||'';
}
function u9Note(id,text){var n=u9el(id);if(!n)return;n.textContent=text||'';n.style.display=text?'block':'none';}
async function u9Earlier(){
  if(!window.S2R)return;
  try{
    var u1=await S2R.loadAll('u1_foundations')||{},c1=Array.isArray(u1.confirmed_items)?u1.confirmed_items:[],w1=u1.__pc_work||{},groups=[];
    if(c1.indexOf('Problem Charter \u00b7 Challenges We Will Address')>=0){
      [['design','Strategy design'],['execution','Strategy execution'],['sustain','Sustaining performance']].forEach(function(a){
        var list=(w1.ch&&Array.isArray(w1.ch[a[0]])?w1.ch[a[0]]:[]).map(function(x){return String(x||'').trim();}).filter(Boolean),out=[];
        (w1.pick&&Array.isArray(w1.pick[a[0]])?w1.pick[a[0]]:[]).forEach(function(x){x=String(x||'').trim();if(x&&list.indexOf(x)>=0&&out.indexOf(x)<0)out.push(x);});
        if(out.length)groups.push([a[1],out.map(function(x,i){return [(i+1)+'. '+x,x];})]);
      });
    }
    u9Opts(u9el('u9_ch_challenge'),groups,U9.w.ch_challenge||'','\u2013 select a challenge \u2013');
    u9Note('u9ChNote',groups.length?'':'Your group\u2019s challenges appear here once every member has agreed your group\u2019s Problem Charter.');
    var u7=await S2R.loadAll('u3m1_lens6')||{},c7=Array.isArray(u7.confirmed_items)?u7.confirmed_items:[],w7=u7.__ex_work||{},krs=[];
    if(c7.indexOf('Expectations \u00b7 Start With the Future')>=0)[1,2].forEach(function(n){
      var o=String(w7['o'+n+'_obj']||'').trim(),k=String(w7['o'+n+'_kr']||'').trim();
      if(k){var t=(o?'Objective: '+o+' \u00b7 ':'')+'Key Result: '+k;krs.push([t,t]);}
    });
    u9Opts(u9el('u9_ch_link'),krs.length?[['',krs]]:[],U9.w.ch_link||'','\u2013 select an Objective and Key Result \u2013');
    u9Note('u9KrNote',krs.length?'':'Your group\u2019s Objectives and Key Results appear here once every member has agreed your group\u2019s Unit 7 record.');
  }catch(e){console.warn('[unit3_m2_lens8_p] earlier units not loaded',e);}
}
"""

if __name__ == '__main__':
    sp, sf, op, of = sys.argv[1:5]
    p = build(rd(sp), 'p'); f = build(rd(sf), 'f')
    open(op, 'w', encoding='utf-8', newline='').write(p)
    open(of, 'w', encoding='utf-8', newline='').write(f)
    print('built', len(p), len(f))
