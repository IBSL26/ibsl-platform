# Capstone flow, 12 Nov 2026: Our Position removed; company, trigger and problem statement carried into Units 3-12;
# Units 9/10 Charter drop-downs; Unit 2 wording; Capstone strategy summary from agreed outputs.
import re, os, sys
ROOT=os.path.expanduser('~/mnt/ibsl-platform')
SRC=os.path.join(ROOT,'Claude outputs/Backups/Capstone flow 12 Nov/pages')
OUT=os.path.join(ROOT,'Claude outputs/Review files/Capstone flow 12 Nov/pages')
os.makedirs(OUT,exist_ok=True)
log=[]
def rd(n): return open(os.path.join(SRC,n),encoding='utf-8',newline='').read()
def wr(n,t): open(os.path.join(OUT,n),'w',encoding='utf-8',newline='').write(t)
def rep(t,a,b,n=1,name=''):
    c=t.count(a)
    if c!=n: raise SystemExit('COUNT %s: expected %d got %d for %r'%(name,n,c,a[:90]))
    return t.replace(a,b)
def eol(t): return '\r\n' if '\r\n' in t else '\n'

UNITS={'unit2_m1_lens2':3,'unit2_m1_lens3':4,'unit3_m1_lens4':5,'unit3_m1_lens5':6,'unit3_m1_lens6':7,
       'unit3_m2_lens7':8,'unit3_m2_lens8':9,'unit4_m1_lens9':10,'unit4_m1_lens10':11,'unit4_m2_lens11':12}
# What this unit's Capstone work does for the company's central problem (participant, then facilitator voice).
WHY={3:'you turn your Success in Practice from Unit 2 into the Objectives and Key Results that will resolve your central problem',
     4:'you test the conditions your Key Results from Unit 3 depend on, so your direction holds as you resolve your central problem',
     5:'you build the case for the change your people must make to deliver your Key Results and resolve your central problem',
     6:'you set up how one of your Key Results is delivered and managed, from each function\u2019s contribution to the CEO\u2019s scorecard, so progress on your central problem is tracked',
     7:'you set the expectations for two contributions from your Unit 6 Contribution Map, so the people who deliver them own your progress on your central problem',
     8:'you set the review discipline that shows early when progress on your central problem slips, and how you recover it',
     9:'you take one of the three problems in your Problem Charter, link it to a Key Result from Unit 7, and clear what is blocking it',
     10:'you set the organisational conditions (environment, systems, resources and governance) your company needs to deliver its strategic commitments and resolve its central problem',
     11:'you measure the health of your organisation and what poor health is costing it, and build the culture that will hold the resolution of your central problem',
     12:'you bring your Key Result and its WARD from Unit 6, your ESRG scan from Unit 10 and your health position from Unit 11 into three lines of sight, quarter by quarter, to show whether your company is resolving its central problem and holding the result'}
FAC={3:'the group turns its Success in Practice from Unit 2 into the Objectives and Key Results that will resolve the company\u2019s central problem',
     4:'the group tests the conditions its Key Results from Unit 3 depend on, so its direction holds as the company resolves its central problem',
     5:'the group builds the case for the change the company\u2019s people must make to deliver its Key Results and resolve its central problem',
     6:'the group sets up how one of its Key Results is delivered and managed, from each function\u2019s contribution to the CEO\u2019s scorecard, so progress on the central problem is tracked',
     7:'the group sets the expectations for two contributions from its Unit 6 Contribution Map, so the people who deliver them own the company\u2019s progress on its central problem',
     8:'the group sets the review discipline that shows early when progress on the central problem slips, and how the company recovers it',
     9:'the group takes one of the three problems in its Problem Charter, links it to a Key Result from Unit 7, and clears what is blocking it',
     10:'the group sets the organisational conditions (environment, systems, resources and governance) the company needs to deliver its strategic commitments and resolve its central problem',
     11:'the group measures the health of the organisation and what poor health is costing it, and builds the culture that will hold the resolution of the company\u2019s central problem',
     12:'the group brings its Key Result and its WARD from Unit 6, its ESRG scan from Unit 10 and its health position from Unit 11 into three lines of sight, quarter by quarter, to show whether the company is resolving its central problem and holding the result'}
def fac(s): return s
def p_line(u): return '<p><strong>Our company.</strong> Your group does this work for the company in your Problem Charter: '+WHY[u]+'. Your company overview, just above the group record bar, shows your company, your trigger, your three problems and your central problem statement.</p>'
def f_line(u): return '<p><strong>Our company.</strong> Each group does this work for the company in its Problem Charter: '+FAC[u]+'. The participant page shows the group\u2019s company overview, with its trigger, three problems and central problem statement, just above the group record bar.</p>'

def drop_pos_block(t,name):
    L=t.split(eol(t)) if eol(t)=='\r\n' else t.split('\n')
    i=next(k for k,l in enumerate(L) if 'acc-t">Our Position<' in l)
    s=i-1
    if L[s].strip()!='<div class="acc open">': raise SystemExit('OPEN '+name+': '+L[s])
    e=next(k for k in range(i+1,len(L)) if L[k].strip()=='</div></div></div>')
    del L[s:e+1]
    return eol(t).join(L)

def insert_how(t,line,name):
    i=t.find('How Section 5 works')
    nxt=re.compile(r'</(div|strong)>').search(t,i)
    if nxt.group(1)=='div': k=nxt.end()
    else: k=t.find('</p>',nxt.end())+4
    return t[:k]+line+t[k:]

for base,u in UNITS.items():
    for side in 'pf':
        n=base+'_'+side+'.html'; t=rd(n); E=eol(t)
        t=drop_pos_block(t,n)
        if side=='p':
            t,c=re.subn(r'stand:\{mount:"twStand",hint:"(?:[^"\\]|\\.)*"\},','',t)
            if c!=1: raise SystemExit('stand cfg '+n)
            t=insert_how(t,p_line(u),n)
            k=t.rindex('</body>'); t=t[:k]+'<script src="s2r-charter.js"></script>'+E+t[k:]
        else:
            if 'How Section 5 works' in t: t=insert_how(t,f_line(u),n)
            else:
                h=t.find('Section 5 · Application — In Practice'); k=t.find('<div class="slo-box">',h); k=t.find('</ul></div>',k)+len('</ul></div>')
                t=t[:k]+E+'<div class="fac-note-full"><div class="fac-note-full-label">&#9670; FACILITATOR GUIDANCE — Our company</div>'+f_line(u)+'</div>'+t[k:]
        if 'Our Position' in t or 'twStand' in t: raise SystemExit('left '+n)
        if side=='p' and n=='unit3_m2_lens8_p.html':
            t=rep(t,'<li>Your group selects one challenge from its Problem Charter and links','<li>Your group selects one of the three problems in its Problem Charter and links')
            t=rep(t,'<li>The original work-based challenge selected from its Problem Charter.</li>','<li>The problem selected from its Problem Charter.</li>')
            t=rep(t,'Your group&rsquo;s Problem Charter holds the challenges your executive team committed to address. Select one that remains relevant',
                    'Your group&rsquo;s Problem Charter names the three problems your executive team committed to address, one in each of strategy design, strategy execution and sustaining performance. Select the one that remains relevant')
            t=rep(t,'Select the challenge from your group&rsquo;s Problem Charter.','Select the problem from your group&rsquo;s Problem Charter.')
            t=rep(t,'Select the challenge from your group\u2019s Problem Charter.','Select the problem from your group\u2019s Problem Charter.')
            t=rep(t,'&ndash; select a challenge &ndash;','&ndash; select a problem &ndash;')
            t=rep(t,"'\\u2013 select a challenge \\u2013'","'\\u2013 select a problem \\u2013'")
            t=rep(t,"Your group\\u2019s challenges appear here once every member has agreed your group\\u2019s Problem Charter.","Your group\\u2019s three problems appear here once every member has agreed your group\\u2019s Problem Charter.")
            t=rep(t,'Your group selected a challenge from its Problem Charter,','Your group selected a problem from its Problem Charter,')
            a=t.index("if(c1.indexOf('Problem Charter \\u00b7 Challenges We Will Address')>=0){")
            b=t.index("u9Opts(u9el('u9_ch_challenge')",a)
            new=("if(c1.indexOf('Problem Charter \\u00b7 Challenges We Will Address')>=0){"+E+
                 "      /* The three problems the group selected, one per area (Problem Charter, 12 Nov 2026). */"+E+
                 "      var pa={};String(u1.pc_address||'').split(/\\n\\s*\\n/).forEach(function(b){var m=/^\\s*(Strategy design|Strategy execution|Sustaining performance):[ \\t]*(.+)$/m.exec(b);if(m&&m[2].trim())pa[m[1]]=m[2].trim();});"+E+
                 "      ['Strategy design','Strategy execution','Sustaining performance'].forEach(function(a){if(pa[a])groups.push([a,[[pa[a],pa[a]]]]);});"+E+
                 "    }"+E+"    ")
            t=t[:a]+new+t[b:]
            t=rep(t,'Problem Charter (u1_foundations, __pc_work pick/ch)','Problem Charter (u1_foundations, pc_address: the three problems)')
        if side=='f' and n=='unit3_m2_lens8_f.html':
            t=rep(t,'<li>Each group selects one challenge from its Problem Charter and links','<li>Each group selects one of the three problems in its Problem Charter and links')
            t=rep(t,'<li>The original work-based challenge selected from its Problem Charter.</li>','<li>The problem selected from its Problem Charter.</li>')
            t=rep(t,'Each group selects one challenge from its Problem Charter that remains relevant','Each group selects the one of its three Problem Charter problems that remains relevant')
            t=rep(t,'The group selects the challenge from its Problem Charter.','The group selects the problem from its Problem Charter.')
            t=rep(t,'and chose the challenges its executive team would address','and selected the three problems its executive team would address, one in each area')
        if side=='p' and n=='unit4_m1_lens9_p.html':
            a=t.index('if(conf.indexOf("Problem Charter · Challenges We Will Address")>=0){var w=r.__pc_work||{};')
            endm='if(out.length)groups.push(["Challenges we will address · "+a[1],out]);});}'
            b=t.index(endm,a)+len(endm)
            new=('if(conf.indexOf("Problem Charter · Challenges We Will Address")>=0){var pa={};String(r.pc_address||"").split(/\\n\\s*\\n/).forEach(function(b){var m=/^\\s*(Strategy design|Strategy execution|Sustaining performance):[ \\t]*(.+)$/m.exec(b);if(m&&m[2].trim())pa[m[1]]=m[2].trim();});'+E+
                 '    ["Strategy design","Strategy execution","Sustaining performance"].forEach(function(a){if(pa[a])groups.push(["Our problem · "+a,[pa[a]]]);});}')
            t=t[:a]+new+t[b:]
            t=rep(t,'(central problem, then the challenges the group will address)','(central problem, then the three problems, one per area)')
        wr(n,t); log.append(n)

# Unit 2: the How box line and nothing else.
n='unit2_m1_lens1_p.html'; t=rd(n)
t=rep(t,'Answer the three questions of each SiP domain, write one statement for each domain,','Answer the two questions of each SiP domain, write one statement for each domain,')
wr(n,t); log.append(n)

# s2r-tasks.js: Unit 2 boxes match the build.
n='s2r-tasks.js'; t=rd(n)
a=t.index("    lens1:[ // Unit 2"); b=t.index("    lens2:[ // Unit 3")
t=t[:a]+("    lens1:[ // Unit 2\n"
 "      {how:'How to complete 5.1',t:B('In this step you complete 2 parts:','answer the 14 elements, one question each, against your problem statement; then the scribe brings them together under five headings and your group edits them.')},\n"
 "      {how:'How to complete 5.2',t:B('In this step you complete 1 entry:','your Strategy Intent Statement, in one or two sentences.')},\n"
 "      {how:'How to complete 5.3',t:B('In this step you complete 3 parts:','answer the two questions in each of the four domains; write one statement per domain; then write your one Success in Practice statement.')},\n"
 "      {how:'How to complete the Group record',t:B('In this part you complete 1 task:','read your group record, then select Agree.')}],\n")+t[b:]
wr(n,t); log.append(n)

# s2r-team.js: Our Position switched off for every unit.
n='s2r-team.js'; t=rd(n)
t=rep(t," *     stand: { mount:'twStand', hint:'...' }      // optional: the group's Our Position statement (28 Oct 2026)\n","")
a=t.index("      if(cfg.stand){\n        var base=cfg.complete;"); b=t.index("      T.cfg=cfg;",a)
t=t[:a]+"      /* Our Position removed from every unit (12 Nov 2026). */\n      if(cfg.stand){cfg=Object.assign({},cfg);delete cfg.stand;}\n"+t[b:]
wr(n,t); log.append(n)

# Capstone: xS boxes gone; summary drawn from the agreed outputs; 9A wording.
n='capstone_P.html'; t=rd(n)
t,c=re.subn(r",\n\s*\['\d+S','Our Position','[^']*','','stand'\]",'',t)
if c!=10: raise SystemExit('cap stand rows %d'%c)
t,c=re.subn(r",\n\s*\['\d+S','team_summary','Our Position'\]",'',t)
if c!=10: raise SystemExit('cap pull rows %d'%c)
t=rep(t,"['9A','Original challenge','The work-based challenge we selected, and the strategic Objective and Key Result or KPI it affects.']",
        "['9A','Original challenge','The problem from our Problem Charter we selected, and the strategic Objective and Key Result or KPI it affects.']")
a=t.index('  // "Our Strategy in Summary": the team\'s Our Position from every unit'); b=t.index('  function critTableHtml(){',a)
t=t[:a]+r'''  // "Our Strategy in Summary" (12 Nov 2026): the key outputs our team agreed in each unit, brought together from the Blueprint.
  var SUMMARY = { u1:['1C','1H'], u2:['2B','2G'], u3:['3E','3F'], u4:['4E'], u5:['5B'], u6:['6A'], u7:['7B'], u8:['8E'],
                  u9:['9B','9E'], u10:['10C'], u11:['11B','11E'], u12:['12A','12D'] };
  function standAllHtml(){
    var by = {}; (S.bp.sections || []).forEach(function(sec){ by[sec.key] = sec; });
    var h = '<div class="stand-all"><div class="sum-head">Our Strategy in Summary</div>' +
      '<p class="muted">Our strategy in one read: our company and its central problem, our direction, how we carry it through people and performance, and how we sustain the results, as our team agreed them in each unit.</p>';
    BLUEPRINT.forEach(function(d){
      if (S.mode === 'facilitator' && !by[d.key]) return;
      var m = MODULES[d.key]; if (m) h += '<div class="stand-mod">' + m[0] + ' · ' + m[1] + '</div>';
      var sec = by[d.key], content = (sec && sec.content) || {}, body = '';
      (SUMMARY[d.key] || []).forEach(function(id){
        var b = d.boxes.filter(function(x){ return x[0] === id; })[0]; if (!b) return;
        var v = String(content[id] || '').trim();
        body += '<div class="sum-l">' + esc(b[1]) + '</div>' +
          (v ? '<div class="sum-v fmt">' + (fmtU1(id, v, content) || fmtBox(v, b[4] === 'hl')) + '</div>' : '<div class="stand-v empty">Not yet agreed.</div>');
      });
      h += '<div class="stand-u"><div class="stand-t">Unit ' + d.unit + ' · ' + esc(d.title) + '</div>' + body + '</div>';
    });
    return h + '</div>';
  }
'''+t[b:]
t=rep(t,"    // Our Position leads the unit, so the assessor reads the team's position first.\n    def.boxes.filter(function(b){ return b[4] === 'stand'; }).forEach(drawBox);\n","")
t=rep(t,"    def.boxes.filter(function(b){ return b[4] !== 'stand'; }).forEach(drawBox);","    def.boxes.forEach(drawBox);")
t=rep(t,".stand-v.empty{color:rgba(255,255,255,.4);font-style:italic;}",
        ".stand-v.empty{color:rgba(255,255,255,.4);font-style:italic;}\n.sum-l{font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gold);margin:10px 0 4px;}\n.sum-v{font-size:13px;line-height:1.7;color:rgba(255,255,255,.88);}")
t=rep(t,"  .stand-v.empty{color:#888 !important;}","  .stand-v.empty{color:#888 !important;}\n  .sum-l{color:#a8862f !important;font-size:8pt;margin:8px 0 3px;}\n  .sum-v{color:#1f2a24 !important;font-size:10pt;line-height:1.55;}")
if 'Our Position' in t or 'team_summary' in t: raise SystemExit('cap left')
wr(n,t); log.append(n)
print('\n'.join(log)); print(len(log),'files')
