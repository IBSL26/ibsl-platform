# -*- coding: utf-8 -*-
"""Move the Capstone group work of Units 1 and 3 to 9 to the shared group record (19 October 2026).
The group chooses a scribe for each assignment; only the scribe types; the entries appear on every
member's page; each member selects Agree; when every member has agreed, the work's names go into every
member's confirmed list (the Capstone checks them, as before). Saved keys and the Capstone link do not change.

usage: python3 team_patch.py <in folder> <out folder>
"""
import sys, os, re

def rd(p): return open(p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
def wr(p, s): open(p, 'w', encoding='utf-8', newline='').write(s.replace('\n', '\r\n'))
def once(s, old, new, label=''):
    n = s.count(old)
    assert n == 1, (label, n, old[:100])
    return s.replace(old, new)

SCRIPT_TAG = ('<script src="/s2r-save.js"></script>', '<script src="/s2r-save.js"></script>\n<script src="/s2r-team.js"></script>')
BAR = '<div id="twBar"></div>\n'

def helper_guard(names, keyre, out_fn):
    """Lines placed at the top of the page's save helper."""
    return ("  if(k==='confirmed_items'){var _ts=window.S2RTeam&&S2RTeam.status(),_own=(Array.isArray(val)?val:[]).filter(function(n){return %s.indexOf(n)<0;});"
            "if(!_own.length)return true;val=_own.concat(_ts&&_ts.all_agreed?%s:[]);}\n"
            "  else if(window.S2RTeam&&%s.test(k)){var _ok=S2RTeam.save(k,val);if(_ok&&!/^__tw_out/.test(k))%s();return _ok;}\n") % (names, names, keyre, out_fn)

# ── per unit ─────────────────────────────────────────────────────────────────
UNITS = [
  dict(f='unit1_P.html', lens="'u1_foundations'", helper='async function pcsave(k,val){\n', names='PC_NAMES',
       keyre=r'/^(__pc_work$|pc_(record|company|team|org|challenges|manifest|consequences|address|problem)$)/',
       out='pcTeamOut', open_fn='pcOpen',
       out_body="if(pcOpen().length)return;S2RTeam.save('pc_record',pcRecord());PCP.forEach(function(p){S2RTeam.save(p[1],pcText(p[1]));});",
       complete="function(){var o=pcOpen();return o.length?o.join('; '):'';}",
       remote="function(r){pcInit(r);}", lock="['pcTool']", attach_after='    if(typeof pcInit===\'function\')pcInit(responses);\n',
       confirm='pcConfirm', msg="pcmsg", recdraw='pcRecDraw', mount='<div id="pcTool">'),
  dict(f='unit2_m1_lens3_p.html', lens='U4_LENS', helper='async function u4save(k,val){\n', names='MB_NAMES',
       keyre=r'/^(__mbt_work$|mbt_(record|arena|bound|comp|value)$)/', out='u4TeamOut', open_fn='mbOpen',
       out_body="if(!mbAll().length||mbOpen().length)return;for(var n=0;n<4;n++)S2RTeam.save(MB_KEYS[n],mbText(n));S2RTeam.save('mbt_record',mbRecordText());",
       complete="function(){if(!mbAll().length)return 'bring in your Unit 3 Key Results';var o=mbOpen();return o.length?o.map(function(x){return 'Key Result '+mbId(x.i,x.j);}).join('; '):'';}",
       remote="function(r){u4Init(r);}", lock="['mod4']", init='function u4Init(responses){\n', confirm='mbConfirm', msg="u4msg", msgid="'mbMsg'", recdraw='renderMB'),
  dict(f='unit3_m1_lens4_p.html', lens='U5_LENS', helper='async function u5save(k,val){\n', names='S5_NAMES',
       keyre=r'/^(__align_work$|kit_(team|mind|habit)$)/', out='u5TeamOut', open_fn='s5Open',
       out_body="if(s5Open().length)return;S2RTeam.save('kit_team',s5Text('mind')+'\\n\\n'+s5Text('habit'));S2RTeam.save('kit_mind',s5Text('mind'));S2RTeam.save('kit_habit',s5Text('habit'));",
       complete="function(){var o=s5Open();return o.length?o.join(', '):'';}",
       remote="function(r){u5Init(r);}", lock="['mod4']", init='function u5Init(responses){\n', confirm='s5Confirm', msg="u5msg", msgid="'kitMsg'", recdraw='s5RecDraw'),
]
for n, pre, work, rec, recfn in [(6, 'cm', '__cm_work', 'cm_record', 'u6RecordText'), (7, 'ex', '__ex_work', 'ex_record', 'u7Record'),
                                  (8, 'rd', '__rd_work', 'rd_record', 'u8Record'), (9, 'uc', '__uc_work', 'uc_record', 'u9Record')]:
    f = {6: 'unit3_m1_lens5_p.html', 7: 'unit3_m1_lens6_p.html', 8: 'unit3_m2_lens7_p.html', 9: 'unit3_m2_lens8_p.html'}[n]
    UNITS.append(dict(f=f, lens='U%d_LENS' % n, helper='async function u%dsave(k,val){\n' % n, names='U%d_NAMES' % n,
        keyre=r'/^(%s$|%s_)/' % (work, pre), out='u%dTeamOut' % n, open_fn='u%dOpen' % n,
        out_body="if(u%dOpen().length)return;S2RTeam.save('%s',%s());U%dP.forEach(function(p){S2RTeam.save(p[3],u%dText(p[0]));});" % (n, rec, recfn, n, n),
        complete="function(){var o=u%dOpen();return o.length?o.join('; '):'';}" % n,
        remote="function(r){u%dInit(r);}" % n, lock="['mod4']", init='function u%dInit(responses){\n' % n,
        confirm='u%dConfirm' % n, msg='u%dmsg' % n, msgid="'u%dMsg'" % n, recdraw='u%dRecDraw' % n))

def team_block(u):
    return ('/* ── Shared group record (19 Oct 2026): the scribe types, every member agrees (s2r-team.js) ── */\n'
            'function %(out)s(){if(!window.S2RTeam||!S2RTeam.isScribe())return;%(out_body)s}\n'
            'var _twOn=false;\n'
            'function twAttach(){if(_twOn||!window.S2RTeam)return;_twOn=true;S2RTeam.attach({lens:%(lens)s,mount:\'twBar\',lock:%(lock)s,names:%(names)s,complete:%(complete)s,onRemote:%(remote)s});}\n') % u

def confirm_body(u):
    msgcall = ('%s(\'Before you agree, complete: \'+_o+\'.\')' % u['msg']) if u['f'] == 'unit1_P.html' else ('%s(%s,\'Before you agree, complete: \'+_o+\'.\')' % (u['msg'], u['msgid']))
    return ('async function %s(){\n'
            '  var _o=window.S2RTeam?(%s)():\'\';\n'
            '  if(_o){%s();%s;return;}\n'
            '  if(!window.S2RTeam){return;}\n'
            '  if(S2RTeam.isScribe()){%s();await S2RTeam.flush();}\n'
            '  await S2RTeam.agree();\n'
            '  %s();\n'
            '}\n') % (u['confirm'], u['complete'], u['recdraw'], msgcall, u['out'], u['recdraw'])

def replace_function(s, name, new):
    i = s.index('async function %s(' % name)
    j = s.index('\n}\n', i) + 3
    return s[:i] + new + s[j:]

def patch_unit(s, u):
    s = once(s, *SCRIPT_TAG, label=u['f'] + ' script')
    s = once(s, u['helper'], u['helper'] + helper_guard(u['names'], u['keyre'], u['out']), label=u['f'] + ' helper')
    s = replace_function(s, u['confirm'], confirm_body(u))
    # the team block goes right before the confirm function
    i = s.index('async function %s(' % u['confirm'])
    s = s[:i] + team_block(u) + s[i:]
    if 'init' in u:
        j = s.index(u['init']); k = s.index('\n}\n', j)
        s = s[:k] + '\n  twAttach();' + s[k:]
    else:
        s = once(s, u['attach_after'], u['attach_after'] + '    twAttach();\n', label=u['f'] + ' attach')
    if 'mount' in u:
        s = once(s, u['mount'], BAR + u['mount'], label=u['f'] + ' mount')
    else:
        s = mount_after_scribe(s)
    return s

def mount_after_scribe(s):
    i = s.index('acts as scribe')
    k = s.rfind('<div class="step-tabs"', 0, i); p = s.rfind('class="step-panel', 0, i)
    if k >= 0 and p > k and i - k < 20000 and s.rfind('id="mod', 0, i) < k:
        return s[:k] + BAR + s[k:]
    j = s.index('\n', i) + 1
    return s[:j] + BAR + s[j:]

# ── Unit 3 (two parts, one group record) ─────────────────────────────────────
def patch_u3(s):
    s = once(s, *SCRIPT_TAG, label='u3 script')
    names = "KISS_NAMES.concat([N_PRI,N_OKR])"
    keyre = r'/^(kex_|kiss_(keep|improve|start|stop)$|sip_d\d_st$|__okr_work$|okr_drafts$|ent_priorities$|ent_okrs$)/'
    s = once(s, 'async function u3save(k,val){\n', 'async function u3save(k,val){\n' + helper_guard('U3_TW_NAMES()', keyre, 'u3TeamOut'), label='u3 helper')
    complete = "function(){var o=[];if(kissFilled()<16)o.push('all sixteen KISS boxes');return o.concat(okrProblems()).join(' ');}"
    block = ('/* ── Shared group record (19 Oct 2026): the scribe types, every member agrees (s2r-team.js) ── */\n'
             'function U3_TW_NAMES(){return ' + names + ';}\n'
             'function u3TeamOut(){if(!window.S2RTeam||!S2RTeam.isScribe())return;'
             'if(kissFilled()===16){for(var x=0;x<KISS_EL.length;x++)S2RTeam.save(KISS_OUT[x],kissCompose(KISS_EL[x][0]));}'
             'if(!okrProblems().length){S2RTeam.save(\'ent_priorities\',okrPriText());S2RTeam.save(\'ent_okrs\',okrOkrText());}}\n'
             'var _twOn=false;\n'
             'function twAttach(){if(_twOn||!window.S2RTeam)return;_twOn=true;S2RTeam.attach({lens:LENS,mount:\'twBar\',lock:[\'mod4\'],names:U3_TW_NAMES(),complete:' + complete +
             ',onRemote:function(r){Object.keys(r).forEach(function(k){if(r[k]!==null&&r[k]!==undefined)U3.v[k]=r[k];});U3.conf=Array.isArray(r.confirmed_items)?r.confirmed_items.slice():[];okrLoad(r.__okr_work);u3RenderAll();}});}\n')
    s = replace_function(s, 'kissConfirm', 'async function kissConfirm(){\n  if(kissFilled()<16){u3msg(\'kissMsg\',\'Complete all sixteen boxes first. Where your group finds nothing for a box, record "None identified".\');return;}\n  u3msg(\'kissMsg\',\'All sixteen boxes are complete. Your group agrees the whole record in 5.2.\',\'ok\');\n}\n')
    s = replace_function(s, 'okrConfirm', 'async function okrConfirm(){\n  var _o=(' + complete + ')();\n  if(_o){u3msg(\'okrMsg\',_o);return;}\n  if(!window.S2RTeam)return;\n  if(S2RTeam.isScribe()){await okrSaveNow();u3TeamOut();await S2RTeam.flush();}\n  await S2RTeam.agree();\n  renderOkrOut();renderKissConfirm();\n}\n')
    i = s.index('async function kissConfirm('); s = s[:i] + block + s[i:]
    s = mount_after_scribe(s)
    s = once(s, "    okrLoad(responses['__okr_work']);\n    u3RenderAll();\n", "    okrLoad(responses['__okr_work']);\n    u3RenderAll();\n    twAttach();\n", label='u3 attach')
    s = once(s, 'onclick="kissConfirm()">✓ Confirm KISS map</button>', 'onclick="kissConfirm()">Check the KISS map</button>', label='u3 kiss btn')
    s = once(s, 'onclick="okrConfirm()">✓ Confirm Enterprise Priorities and OKRs</button>', 'onclick="okrConfirm()">Agree</button>', label='u3 okr btn')
    return s

# ── Wording ─────────────────────────────────────────────────────────────────
P_SCRIBE = 'Your group chooses its scribe for this work in the group record bar. The scribe types what your group agrees, and the entries appear on every member&rsquo;s page.'
F_SCRIBE = 'The group chooses its scribe for this work. The scribe types what the group agrees, and the entries appear on every member&rsquo;s page.'
WORDS = [
  # participant
  ('Your group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.', P_SCRIBE),
  ('Your group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page. Then select Confirm. Your confirmed record feeds your team&rsquo;s Capstone Blueprint.',
   P_SCRIBE + ' Then each member selects Agree. When every member has agreed, your record feeds your team&rsquo;s Capstone Blueprint.'),
  # facilitator
  ('The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page of the participant file, in the session or after it.', F_SCRIBE),
  ('The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page of the participant file.', F_SCRIBE),
  ('The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page, in the session or after it.', F_SCRIBE),
  ('The group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page, in the session or after it.', F_SCRIBE),
  ('The group agrees each entry and one member acts as scribe. Every member types the agreed entries into their own page, then selects Confirm. The confirmed record feeds the team&rsquo;s Capstone Blueprint.',
   F_SCRIBE + ' Each member then selects Agree. When every member has agreed, the record feeds the team&rsquo;s Capstone Blueprint.'),
  ('The group agrees each entry and one member acts as scribe. Every member then types the agreed entries into their own page and selects Confirm in part 5.6.',
   F_SCRIBE + ' Each member then selects Agree in part 5.6.'),
  ('The group agrees each entry and one member acts as scribe; every member types the agreed entries into their own page. Both confirmed outputs feed the team\'s Capstone Blueprint.',
   F_SCRIBE.replace('&rsquo;', "'") + ' When every member has agreed, both outputs feed the team\'s Capstone Blueprint.'),
  ('One member acts as scribe; every member types the agreed entries into their own page.', 'The group chooses its scribe; the entries appear on every member&rsquo;s page.'),
  # select Confirm → Agree
  ('and select Confirm. Your confirmed record feeds your team&rsquo;s Capstone Blueprint.', 'and select Agree. When every member has agreed, your record feeds your team&rsquo;s Capstone Blueprint.'),
  ('and select Confirm. Your confirmed record feeds your team’s Capstone Blueprint.', 'and select Agree. When every member has agreed, your record feeds your team’s Capstone Blueprint.'),
  ('In the Charter record you read your group&rsquo;s Charter and select Confirm. Your confirmed Charter becomes Section 1 of your team&rsquo;s Capstone Blueprint.',
   'In the Charter record you read your group&rsquo;s Charter and select Agree. When every member has agreed, your Charter becomes Section 1 of your team&rsquo;s Capstone Blueprint.'),
  ('When every entry is complete, select Confirm. Your confirmed Charter feeds boxes', 'When every entry is complete, select Agree. When every member has agreed, your Charter feeds boxes'),
  ('Each member reads the group&rsquo;s Charter and selects Confirm. The confirmed Charter feeds', 'Each member reads the group&rsquo;s Charter and selects Agree. When every member has agreed, the Charter feeds'),
  ('In the Charter record, each member reads the Charter and selects Confirm. The confirmed Charter feeds', 'In the Charter record, each member reads the Charter and selects Agree. When every member has agreed, the Charter feeds'),
  # JS strings on the record
  ("'Before you confirm, complete: '", "'Before you agree, complete: '"),
  ("Not saved. Check your connection, then select Confirm again.", "Not saved. Check your connection, then select Agree again."),
  ("(conf?'Confirmed &#10003;':'Confirm')", "(conf?'Agreed &#10003;':'Agree')"),
  ('Confirmed &middot; into your Capstone', 'Agreed by every member &middot; into your Capstone'),
  ('>Not yet confirmed<', '>Not yet agreed by every member<'),
  # remaining "select Confirm" wording, unit by unit
  ('<h4>Confirm Your KISS Map</h4>', '<h4>Read Your KISS Map</h4>'),
  ('<h4>Confirm and Print</h4>', '<h4>Agree and Print</h4>'),
  ('read the map across the four domains as a group and confirm it. Your confirmed KISS map is the source for 5.2.', 'read the map across the four domains as a group. Your KISS map is the source for 5.2.'),
  ('read your five-step record together, confirm your Enterprise Priorities and Enterprise OKRs, then print the record.', 'read your group record together, select Agree, then print the record.'),
  ('Read your record, then select Confirm. Select Print for a copy.', 'Read your record, then select Agree. Select Print for a copy.'),
  ('select Confirm. Your confirmed work feeds boxes 4A to 4D of your team&rsquo;s Capstone Blueprint. An edit after confirmation sets the record back to not yet confirmed.',
   'select Agree. When every member has agreed, your work feeds boxes 4A to 4D of your team&rsquo;s Capstone Blueprint. An edit after agreement clears the agreements, and every member agrees again.'),
  ('each participant selects Confirm. Print gives a copy of the record.', 'each participant selects Agree. Print gives a copy of the record.'),
  ('Each participant reads the record and selects Confirm.', 'Each participant reads the record and selects Agree.'),
  ('Each participant then selects Confirm. This is Capstone work, and the confirmed record feeds', 'Each participant then selects Agree. This is Capstone work, and when every member has agreed the record feeds'),
  ('Read your record at the foot of this step, then select Confirm.', 'Read your record at the foot of this step, then select Agree.'),
  ('You then select Confirm. This is Capstone work, and your confirmed record feeds', 'You then select Agree. This is Capstone work, and when every member has agreed your record feeds'),
  ('Before you confirm, check that:', 'Before you agree, check that:'),
  ('read your group&rsquo;s record and select Confirm.', 'read your group&rsquo;s record and select Agree.'),
  ('Your page saves as you type. When both activities are complete, each member reads the record and selects Confirm. The confirmed record feeds',
   'The scribe&rsquo;s entries save as they are typed. When both activities are complete, each member reads the record and selects Agree. When every member has agreed, the record feeds'),
  ('Each participant reads the group’s record at the foot of Section 5 and selects Confirm.', 'Each participant reads the group’s record at the foot of Section 5 and selects Agree.'),
  ('and selects Confirm. The confirmed record feeds the team’s', 'and selects Agree. When every member has agreed, the record feeds the team’s'),
  ('Online: the scribe types the agreed entries; every member then types them into their own page.', 'Online: the scribe types the agreed entries, and they appear on every member&rsquo;s page.'),
  ('and selects Confirm. The confirmed record feeds', 'and selects Agree. When every member has agreed, the record feeds'),
  ('Read the record and Confirm', 'Read the record and Agree'),
  ('When every entry is complete, select Confirm. Your confirmed record feeds', 'When every entry is complete, select Agree. When every member has agreed, your record feeds'),
  ('Confirm your group’s ', 'Agree your group’s '),
  ('The confirmed record feeds', 'The agreed record feeds'),
  ('Your group’s confirmed record feeds', 'Your group’s agreed record feeds'),
]

def words(s):
    for a, b in WORDS:
        s = s.replace(a, b)
    return s

def main(src, dst):
    os.makedirs(dst, exist_ok=True)
    for u in UNITS:
        s = rd(os.path.join(src, u['f']))
        s = words(patch_unit(s, u))
        wr(os.path.join(dst, u['f']), s)
    s = rd(os.path.join(src, 'unit2_m1_lens2_p.html')); wr(os.path.join(dst, 'unit2_m1_lens2_p.html'), words(patch_u3(s)))
    for f in ['unit1_F.html', 'unit2_m1_lens2_f.html', 'unit2_m1_lens3_f.html', 'unit3_m1_lens4_f.html', 'unit3_m1_lens5_f.html',
              'unit3_m1_lens6_f.html', 'unit3_m2_lens7_f.html', 'unit3_m2_lens8_f.html']:
        wr(os.path.join(dst, f), words(rd(os.path.join(src, f))))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
