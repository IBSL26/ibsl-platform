# -*- coding: utf-8 -*-
"""Capstone Blueprint, Unit 2 section aligned with the rebuilt Unit 2 (Carol, 5 Oct 2026).

  python3 patch_capstone.py <capstone_P.html as it stood on 28 Sept> <new file>

1. Unit 2 boxes: 2A Strategy Architecture, 2B Strategy Intent Statement, 2C-2F the four SiP statements.
   Maturity gaps, SiP Headline and SiP Storyline leave the Blueprint.
2. The confirmed outputs are brought in from the member's own Unit 2 page (lens_responses, u2m1_lens1).
   PULL is built to take further units as they are rebuilt.
The database counts the boxes of a section before it can be sent: run capstone_unit2_boxes.sql (8 -> 6).
"""
import sys, io

SRC, OUT = sys.argv[1], sys.argv[2]
raw = io.open(SRC, encoding='utf-8', newline='').read()
assert raw.count('\r\n') == raw.count('\n'), 'expected CRLF throughout'
s = raw.replace('\r\n', '\n')

def rep(a, b):
    global s
    assert s.count(a) == 1, (a[:70], s.count(a))
    s = s.replace(a, b)

# ── 1. Unit 2 boxes ──
rep("""      ['2A','Strategic Intent Statement','State what [Case] pursues, why, how and by when, in a single agreed statement.'],
      ['2B','Maturity gaps and corrective actions','Name the three areas of strategic maturity where [Case] falls furthest short of its ambition. For each, state the corrective action the executive team commits to.'],
      ['2C','SiP · Customer Experience & Value','Describe what customers observe and experience when [Case] has reached its intended future position.'],
      ['2D','SiP · Operational Capability','Describe the operational capability [Case] demonstrates at its intended future position.'],
      ['2E','SiP · People & Culture','Describe how [Case]’s people work, behave and lead at its intended future position.'],
      ['2F','SiP · Enterprise Value','Describe the value [Case] creates for its shareholders and stakeholders at its intended future position.'],
      ['2G','SiP Headline','One sentence stating the destination that every leader in [Case] can repeat.'],
      ['2H','SiP Storyline','Describe [Case] at its destination, written as if it already exists.']
    ]},""",
"""      ['2A','Strategy Architecture','Set out the strategy architecture of [Case] under its five headings: Strategic Position, Strategic Model, Value Architecture, Strategic Navigation and Strategy Discipline.'],
      ['2B','Strategy Intent Statement','State the strategic ambition of [Case] in one crisp statement that carries WHAT, WHY, HOW and WHEN.'],
      ['2C','SiP · Customer Experience & Value','State what customers and other value recipients see and experience when the Strategy Intent of [Case] succeeds.'],
      ['2D','SiP · Operational Capability & Execution Rhythm','State what is visible in how [Case] operates and executes when its Strategy Intent succeeds.'],
      ['2E','SiP · People & Culture Dynamics','State what is visible in how the people of [Case] understand, decide and behave when its Strategy Intent succeeds.'],
      ['2F','SiP · Enterprise Value Creation','State how [Case] benefits across its success metrics when its Strategy Intent succeeds.']
    ]},""")

# ── 2. What each section brings in from its unit page ──
rep("""  var BY_KEY = {}; BLUEPRINT.forEach(function(s){ BY_KEY[s.key] = s; });
""",
"""  var BY_KEY = {}; BLUEPRINT.forEach(function(s){ BY_KEY[s.key] = s; });

  // === Outputs brought in from the member's own unit page (added unit by unit as the units are rebuilt). ===
  // Each row: Blueprint box, response key on the unit page, name in that page's list of confirmed outputs.
  var PULL = {
    u2: { lens:'u2m1_lens1', rows:[
      ['2A','arch_output','Strategy Architecture'],
      ['2B','intent_statement','Strategy Intent Statement'],
      ['2C','sip_d1_st','SiP · Customer Experience & Value'],
      ['2D','sip_d2_st','SiP · Operational Capability & Execution Rhythm'],
      ['2E','sip_d3_st','SiP · People & Culture Dynamics'],
      ['2F','sip_d4_st','SiP · Enterprise Value Creation']
    ]}
  };
""")

rep("""  var S = { mode:'participant', cohortId:null, uid:null, data:null, bp:null, caseName:'', openKeys:{}, dirty:{} };""",
    """  var S = { mode:'participant', cohortId:null, uid:null, data:null, bp:null, caseName:'', openKeys:{}, dirty:{}, pulled:{} };""")

# ── 3. Bring the confirmed outputs in on first opening of an empty Draft ──
rep("""    document.getElementById('root').innerHTML = html;
    restoreDirty();
  }
""",
"""    document.getElementById('root').innerHTML = html;
    restoreDirty();
    autoPull();
  }
""")

# ── 4. Section notes and the button ──
rep("""    if (st === 'locked') h += '<p class="sec-note">Opens when every team member has completed Unit ' + def.unit + '.</p>';""",
    """    if (st === 'locked') h += '<p class="sec-note">Opens when every team member has completed Unit ' + def.unit + '.' + (PULL[sec.key] ? ' Your confirmed outputs from Unit ' + def.unit + ' are then brought in.' : '') + '</p>';
    if (editable && PULL[sec.key]) h += '<div class="pull no-print"><p class="sec-note">Your confirmed outputs from Unit ' + def.unit + ' are brought in from your Unit ' + def.unit + ' page. Read them as a team, then send for team confirmation.</p>' +
      '<button class="btn" onclick="capPull(\\'' + sec.key + '\\')">Bring in from my Unit ' + def.unit + ' page</button></div>';""")

rep(""".box-i{font-size:12px;color:rgba(255,255,255,.55);line-height:1.6;margin-bottom:8px;}
""",
""".box-i{font-size:12px;color:rgba(255,255,255,.55);line-height:1.6;margin-bottom:8px;}
.pull{border-left:2px solid var(--gold);padding:2px 0 4px 14px;margin:6px 0 16px;}
.pull .sec-note{margin:0 0 10px;}
""")

# ── 5. The bring-in functions ──
rep("""  // Discard this section's unsaved text and fetch the latest.
""",
"""  // === Bring confirmed outputs in from the member's own unit page ===
  function sectionEmpty(sec){
    var c = (sec && sec.content) || {};
    for (var k in c){ if (String(c[k] || '').trim() !== '') return false; }
    return true;
  }
  function readUnitOutputs(key){
    var cfg = PULL[key];
    var keys = cfg.rows.map(function(r){ return r[1]; }).concat(['confirmed_items']);
    return sb.from('lens_responses').select('response_key,value')
      .eq('profile_id', S.uid).eq('lens_id', cfg.lens).in('response_key', keys).then(function(res){
        if (res.error){ console.error('[capstone] bring in:', res.error); return null; }
        var v = {}; (res.data || []).forEach(function(r){ v[r.response_key] = r.value; });
        var conf = v.confirmed_items;
        if (typeof conf === 'string'){ try { conf = JSON.parse(conf); } catch (e){ conf = []; } }
        if (!Array.isArray(conf)) conf = [];
        var ready = [], missing = [];
        cfg.rows.forEach(function(r){
          var t = (typeof v[r[1]] === 'string') ? v[r[1]].trim() : '';
          if (t && conf.indexOf(r[2]) !== -1) ready.push({ box:r[0], text:t, name:r[2] }); else missing.push(r[2]);
        });
        return { ready:ready, missing:missing };
      });
  }
  function boxTa(key, box){ return document.querySelector('textarea.box-ta[data-sec="' + key + '"][data-box="' + box + '"]'); }
  function fillBoxes(key, ready){
    var n = 0;
    ready.forEach(function(o){
      var ta = boxTa(key, o.box);
      if (ta && ta.value !== o.text){ ta.value = o.text; window.capInput(ta); n++; }
    });
    return n;
  }

  // First opening of an empty Draft: bring the full confirmed set in and save it as the team's draft.
  function autoPull(){
    if (S.mode !== 'participant' || !S.bp || S.bp.locked) return;
    (S.bp.sections || []).forEach(function(sec){
      var key = sec.key;
      if (!PULL[key] || S.pulled[key] || statusOf(sec) !== 'draft' || S.dirty[key] || !sectionEmpty(sec)) return;
      S.pulled[key] = true;
      readUnitOutputs(key).then(function(o){
        if (!o || o.missing.length || S.dirty[key] || !boxTa(key, PULL[key].rows[0][0])) return;
        if (!fillBoxes(key, o.ready)) return;
        doSave(key).then(function(r){
          S.dirty[key] = false;
          S.openKeys[key] = true;
          reload().then(function(){
            if (r && r.ok) showMsg(key, 'Brought in from your Unit ' + BY_KEY[key].unit + ' page and saved as a draft. Read the text as a team, then send for team confirmation.', 'ok');
          });
        });
      });
    });
  }

  // The button: bring in again from this member's unit page.
  window.capPull = function(key){
    if (!PULL[key] || S.mode !== 'participant') return;
    var unit = BY_KEY[key].unit;
    setBusy(key, true);
    readUnitOutputs(key).then(function(o){
      setBusy(key, false);
      if (!o){ showMsg(key, 'Could not read your Unit ' + unit + ' page. Please try again.', 'err'); return; }
      var missingText = o.missing.length ? ' Not yet confirmed on your Unit ' + unit + ' page: ' + o.missing.join(', ') + '. Confirm there, then bring in again.' : '';
      if (!o.ready.length){ showMsg(key, 'Nothing is confirmed on your Unit ' + unit + ' page yet. Confirm your outputs there, then bring them in again.', 'err'); return; }
      var replaces = o.ready.some(function(x){ var ta = boxTa(key, x.box); return ta && ta.value.trim() !== '' && ta.value.trim() !== x.text; });
      if (replaces && !window.confirm('Replace the text in these boxes with the confirmed outputs from your Unit ' + unit + ' page?')) return;
      var n = fillBoxes(key, o.ready);
      showMsg(key, (n ? 'Brought in from your Unit ' + unit + ' page: ' + o.ready.map(function(x){ return x.box; }).join(', ') + '. Save the draft or send for team confirmation.'
                      : 'The boxes already match your Unit ' + unit + ' page.') + missingText, o.missing.length ? 'err' : 'ok');
    });
  };

  // Discard this section's unsaved text and fetch the latest.
""")

io.open(OUT, 'w', encoding='utf-8', newline='').write(s.replace('\n', '\r\n'))
print('capstone page written:', len(s), 'chars')
