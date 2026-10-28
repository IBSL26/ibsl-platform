# -*- coding: utf-8 -*-
# Consistency build 28 Oct: module header, section sub-lines (U1-4), Closing Insight + Transition boxes,
# unit hand-offs, Learning Journey tables. Idempotent: skips a file that already carries data-cr.
import re,os,sys,html
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from c1 import *; from c2 import *; from c3 import *
os.chdir(os.path.expanduser('~/mnt/ibsl-platform'))
U={1:('unit1_P.html','unit1_F.html'),2:('unit2_m1_lens1_p.html','unit2_m1_lens1_f.html'),3:('unit2_m1_lens2_p.html','unit2_m1_lens2_f.html'),4:('unit2_m1_lens3_p.html','unit2_m1_lens3_f.html'),5:('unit3_m1_lens4_p.html','unit3_m1_lens4_f.html'),6:('unit3_m1_lens5_p.html','unit3_m1_lens5_f.html'),7:('unit3_m1_lens6_p.html','unit3_m1_lens6_f.html'),8:('unit3_m2_lens7_p.html','unit3_m2_lens7_f.html'),9:('unit3_m2_lens8_p.html','unit3_m2_lens8_f.html'),10:('unit4_m1_lens9_p.html','unit4_m1_lens9_f.html'),11:('unit4_m1_lens10_p.html','unit4_m1_lens10_f.html')}
NM={1:'Orientation: Overview',2:'Awareness: What',3:'Intelligence: Why',4:'Extrapolating: Where',5:'Integration: Collective',6:'Application: In Practice'}
def sname(u,n): return NM[n] if u==1 else NM[n+1]
CSS=(".s2r-cr{background:rgba(26,122,106,.07);border:1px solid rgba(26,122,106,.2);border-radius:3px;padding:16px 20px;margin:14px 0;}"
".s2r-cr-h{font-family:'Montserrat',sans-serif;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#22a08a;margin-bottom:6px;}"
".s2r-cr p{font-size:14px;color:rgba(255,255,255,.82);line-height:1.85;margin:0;}"
".s2r-lj{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px;}"
".s2r-lj th,.s2r-lj td{text-align:left;padding:8px 10px;border-bottom:1px solid rgba(255,255,255,.08);vertical-align:top;color:rgba(255,255,255,.75);line-height:1.6;}"
".s2r-lj th{font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:#c9a84c;}\n")
LOG=[]
def T(x): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',x))).strip()
def pk(v,F): return (v[1] if F else v[0]) if isinstance(v,tuple) else v
def box(u,label,text):
    if u==11: return '<div class="hbox" data-cr="1"><div class="u11-ci">%s</div><p>%s</p></div>\n'%(label,text)
    return '<div class="s2r-cr" data-cr="1"><div class="s2r-cr-h">%s</div><p>%s</p></div>\n'%(label,text)
def heros(s): return [m.start() for m in re.finditer(r'<div class="mod-hero[" ]',s)]
def navs(s): return [m.start() for m in re.finditer(r'<div class="mod-nav',s)]
for u,(fp,ff) in U.items():
  for F,fn in ((False,fp),(True,ff)):
    s=open(fn,encoding='utf-8',newline='').read()
    if 'data-cr="1"' in s: LOG.append((fn,'skip: already built')); continue
    crlf='\r\n' in s; s=s.replace('\r\n','\n')
    off=1 if F else 0
    nsec=6 if u==1 else 5
    if u!=11 and '.s2r-cr{' not in s:
        i=s.find('</style>'); s=s[:i]+CSS+s[i:]
    # 1 header
    if u<=9:
        paras,_=HEAD[u][1 if F else 0],None
        m=list(re.finditer(r'<(p|div) class="unit-desc">.*?</\1>\n?',s,flags=re.S))
        new=''.join('<p class="unit-desc" data-cr="1">%s</p>\n'%p for p in paras)
        if m:
            a,b=m[0].start(),m[-1].end(); s=s[:a]+new+s[b:]
        else:
            i=s.find('</div>',s.find('class="unit-sub"'))+6; s=s[:i]+'\n'+new+s[i:]
        mod=HEAD[u][2]
        klo='<div class="klo-bar" data-cr="1">\n<span class="klo-label">Module learning outcomes</span>\n'+''.join('<span class="klo">%s</span>\n'%x for x in MLO[mod])+'</div>\n'
        i=s.find('<div class="klo-bar">'); s=s[:i]+klo+s[i:]
        LOG.append((fn,'header',len(m)))
    # 2 hero sub-lines and Unit 1 headings
    if u<=4:
        for n in range(1,nsec+1):
            h=heros(s)[n-1+off]; e=s.find('<div class="mod-body',h)
            reg=s[h:e]
            if u==1 and n in H2U1: reg=re.sub(r'(<h2[^>]*>).*?(</h2>)',lambda m:m.group(1)+H2U1[n]+m.group(2),reg,count=1,flags=re.S)
            if n in SUB[u]:
                hi=reg.find('</h2>'); pre,post=reg[:hi],reg[hi:]
                post,k=re.subn(r'(<p[^>]*>).*?(</p>)',lambda m:m.group(1)+pk(SUB[u][n],F)+m.group(2),post,count=1,flags=re.S)
                reg=pre+post; LOG.append((fn,'sub',n,k))
            s=s[:h]+reg+s[e:]
    # 3 remove old boxes now standardised
    if u==9:
        s,k=re.subn(r'<div class="hbox" style="margin-top:6px;"><div class="u9-ex-h">Closing Insight</div>.*?</p></div>\n?','',s,flags=re.S); LOG.append((fn,'u9 old box',k))
    if u==10:
        s,k=re.subn(r'<div class="hbox"><p><strong>Closing insight:</strong>.*?</div>\n?','',s,flags=re.S); LOG.append((fn,'u10 old boxes',k))
    # 4 final-section boxes (insert first: it sits after everything)
    fin=''
    if u in CI and nsec in CI[u]: fin+=box(u,'Section Closing Insight',pk(CI[u][nsec],F))
    fin+=box(u,HAND[u][0],pk(HAND[u][1],F))
    if F: i=navs(s)[-1]
    else:
        i=s.find('<div class="acc" id="feedback-acc"')
        c=s.rfind('<!--',0,i)
        if c>0 and s[c:i].count('\n')<=1 and '-->' in s[c:i]: i=c
    s=s[:i]+fin+s[i:]
    # 5 section boxes, last to first
    for n in range(nsec-1,0,-1):
        add=''
        if u in CI and n in CI[u]: add+=box(u,'Section Closing Insight',pk(CI[u][n],F))
        if u in TR and n in TR[u]: add+=box(u,'Transition to Section %d &mdash; %s'%(n+1,sname(u,n+1)),pk(TR[u][n],F))
        if not add: continue
        i=navs(s)[n-1+off]; s=s[:i]+add+s[i:]
    # 6 Learning Journey (facilitator)
    if F and u<=10:
        rows=''
        for n in range(1,nsec+1):
            h=heros(s)[n]; e=s.find('<div class="mod-body',h); reg=s[h:e]
            hi=reg.find('<h2'); lab=T(reg[:hi]).replace('Section ','',1)
            mp=re.search(r'</h2>.*?<p[^>]*>(.*?)</p>',reg,flags=re.S)
            rows+='<tr><td>%s</td><td>%s</td></tr>\n'%(lab.replace(' · ',' · ',1),T(mp.group(1)) if mp else T(re.search(r'<h2[^>]*>(.*?)</h2>',reg,flags=re.S).group(1)))
        lj='<div class="fac-note-full" data-cr="1"><div class="fac-note-full-label">&#9670; Learning Journey</div>\n<table class="s2r-lj"><thead><tr><th>Section</th><th>Focus</th></tr></thead><tbody>\n'+rows+'</tbody></table>\n</div>\n'
        key='&#9670; Facilitation Orientation</div>' if u==10 else '&#9670; Unit Intent</div>'
        k=s.find(key); i=s.find('<div class="fac-note-full',k+10); s=s[:i]+lj+s[i:]
        LOG.append((fn,'LJ rows',rows.count('<tr>')))
    if F and u==11:
        rows=''.join('<tr><td>%s</td><td>%s</td></tr>\n'%r for r in U11LJ)
        s,k=re.subn(r'(&#9670; Learning Journey</div>\s*<table class="u11-tbl"><thead>.*?</thead><tbody>\n).*?(</tbody>)',lambda m:m.group(1)+rows+m.group(2),s,count=1,flags=re.S)
        s=s.replace('<table class="u11-tbl"><thead><tr><th>Section</th><th>Focus</th></tr></thead><tbody>\n<tr><td>1 · Awareness','<table class="u11-tbl" data-cr="1"><thead><tr><th>Section</th><th>Focus</th></tr></thead><tbody>\n<tr><td>1 · Awareness',1)
        LOG.append((fn,'U11 LJ',k))
    if crlf: s=s.replace('\n','\r\n')
    open(fn,'w',encoding='utf-8',newline='').write(s)
    LOG.append((fn,'written'))
for l in LOG: print(l)
