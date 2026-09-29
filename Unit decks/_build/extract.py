import re,json,sys,copy
from bs4 import BeautifulSoup, NavigableString
BLOCK={'p','li','h1','h2','h3','h4','h5','h6','tr','div','br','dt','dd','ul','ol','table','section','blockquote','summary','details','label','button','span_block'}
JUNK=re.compile(r'^(▼|▾|▲|×|Save Reflection|Save|✓ Saved.*|Print Exercise|Save Portfolio Artefact|✓ Portfolio artefact saved.*|Save Commitment|Copy to Clipboard|Email to Self|Print / Save as PDF|—|›|‹)$')
def txt(el):
    el=copy.copy(el)
    for x in el.find_all(['script','style','textarea','input','select','button','svg']): x.decompose()
    for x in el.find_all(True):
        if x.name in ('td','th'): x.append(' | ')
        if x.name in BLOCK: x.insert_before('\n'); x.insert_after('\n')
    t=el.get_text()
    lines=[re.sub(r'\s+',' ',l).strip(' |') for l in t.split('\n')]
    out=[]
    for l in lines:
        l=l.strip()
        if not l or JUNK.match(l) or re.match(r'^←.*|.*→$',l): continue
        if out and out[-1]==l: continue
        out.append(l)
    return out
def isnote(x): return x.name and any('fac-note' in c or c=='fac-box' for c in (x.get('class') or []))
def parts_of(body):
    res=[]; lead={'guidance':[],'content':[]}
    for ch in body.children:
        if isinstance(ch,NavigableString): continue
        cls=ch.get('class') or []
        if 'acc' in cls:
            t=ch.select_one('.acc-t'); m=ch.select_one('.acc-meta'); b=ch.select_one('.acc-b') or ch
            b=copy.copy(b)
            notes=[n for n in b.find_all(isnote) if not n.find_parent(isnote)]
            g=[]
            for n in notes: g.append(txt(n)); n.decompose()
            ta=[]
            res.append({'title':t.get_text(' ',strip=True) if t else '', 'meta':m.get_text(' ',strip=True) if m else '', 'guidance':g, 'content':txt(b)})
        elif 'mod-nav' in cls: continue
        elif isnote(ch) or ch.find(isnote):
            if isnote(ch): lead['guidance'].append(txt(ch))
            else:
                c=copy.copy(ch)
                for n in [n for n in c.find_all(isnote) if not n.find_parent(isnote)]: lead['guidance'].append(txt(n)); n.decompose()
                lead['content']+=txt(c)
        else:
            if any(k in ' '.join(cls) for k in ('slo-box','lo-box','fac-obj')): continue
            lead['content']+=txt(ch)
    return lead,res
def prompts(el):
    out=[]
    for ta in el.find_all('textarea'):
        box=ta.find_parent(lambda x: x.name=='div' and any(k in ' '.join(x.get('class') or []) for k in ('ref','port','reflection','commit','cm-','app','kiss','coc','field','step')))
        if box is None: box=ta.parent
        t=' '.join(txt(box))
        ph=re.sub(r'\s+',' ',ta.get('placeholder') or '').strip()
        if len(ph)>30 and 'thoughts here' not in ph.lower() and ph not in t: t=(t+' — '+ph).strip(' —')
        if t and t not in out: out.append(t)
    return out
def load(path, side):
    s=BeautifulSoup(open(path,encoding='utf-8').read(),'html.parser')
    js='\n'.join(x.get_text() for x in s.find_all('script') if not x.get('src'))
    head={'top':txt(s.select_one('.unit-hero') or s.body)[:12]}
    klo=[li.get_text(' ',strip=True) for li in s.select('.klo li')] or [x.get_text(' ',strip=True) for x in s.select('.klo')]
    secs=[]
    for mp in s.select('.mod-panel, div.mod'):
        hero=mp.select_one('.mod-hero'); body=mp.select_one('.mod-body') or mp
        lab=mp.select_one('.mod-hero-label, .mod-badge'); h2=mp.select_one('.mod-hero h2, .mod-title'); sub=hero.select_one('p:not(.mod-hero-label)') if hero else None
        slo=[li.get_text(' ',strip=True) for li in mp.select('.slo-box li, .lo-box li, .fac-obj li')]
        lead,parts=parts_of(body)
        if side=='p':
            for p,acc in zip(parts,[a for a in body.children if not isinstance(a,NavigableString) and 'acc' in (a.get('class') or [])]):
                p['prompts']=prompts(acc)
            lead['prompts']=[]
        secs.append({'label':lab.get_text(' ',strip=True) if lab else '', 'h2':h2.get_text(' ',strip=True) if h2 else '', 'sub':sub.get_text(' ',strip=True) if sub else '', 'slo':slo,'lead':lead,'parts':parts})
    return {'klo':klo,'sections':secs,'js':js,'top':head}
if __name__=='__main__':
    base=sys.argv[1]; out=sys.argv[2]
    F=load(f'src/{base}_f.html' if not base.startswith('unit1') else 'src/unit1_F.html','f')
    P=load(f'src/{base}_p.html' if not base.startswith('unit1') else 'src/unit1_P.html','p')
    json.dump({'F':{k:v for k,v in F.items() if k!='js'},'P':{k:v for k,v in P.items() if k!='js'}},open(out+'.json','w'),ensure_ascii=False,indent=0)
    open(out+'.js.txt','w').write(F['js']+'\n//=====P=====\n'+P['js'])
    # readable outline
    L=[]
    L.append('TOP: '+' / '.join(F['top']['top']))
    L.append('KLO: '+' || '.join(F['klo']))
    for i,sec in enumerate(F['sections']):
        L.append(f'\n#### F[{i}] {sec["label"]} | {sec["h2"]} | {sec["sub"]}')
        if sec['slo']: L.append('SLO: '+' || '.join(sec['slo']))
        for g in sec['lead']['guidance']: L.append('  G> '+' ¶ '.join(g))
        if sec['lead']['content']: L.append('  C> '+' ¶ '.join(sec['lead']['content']))
        for j,p in enumerate(sec['parts']):
            L.append(f'  ## part[{j}] {p["title"]} ({p["meta"]})')
            for g in p['guidance']: L.append('    G> '+' ¶ '.join(g))
            L.append('    C> '+' ¶ '.join(p['content']))
    for i,sec in enumerate(P['sections']):
        L.append(f'\n#### P[{i}] {sec["label"]} | {sec["h2"]} | {sec["sub"]}')
        for j,p in enumerate(sec['parts']):
            L.append(f'  ## part[{j}] {p["title"]} ({p["meta"]})  PROMPTS: '+' || '.join(p.get('prompts',[])))
    open(out+'.txt','w').write('\n'.join(L))
    print(out, len('\n'.join(L)))
