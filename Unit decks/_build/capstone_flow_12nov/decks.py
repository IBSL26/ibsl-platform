# Deck notes, 12 Nov 2026: the Our Position close becomes a pointer to the group's company overview.
import zipfile, re, os, json, glob, shutil, html
ROOT=os.path.expanduser('~/mnt/ibsl-platform')
BK=os.path.join(ROOT,'Claude outputs/Backups/Capstone flow 12 Nov')
OUT=os.path.join(ROOT,'Claude outputs/Review files/Capstone flow 12 Nov')
NEW=('Point the groups to their company overview. Say: "Your company overview, just above the group record bar, shows your company, '
     'your trigger, your three problems and your central problem statement. Every part of this work is done for that company and its central problem."')
OLDRX=re.compile(r'Close the group work with Our Position\..*?guides the assessors through (?:your|the group\u2019s|the group\'s) work\."',re.S)
for f in sorted(glob.glob(os.path.join(BK,'decks','*.pptx'))):
    n=os.path.basename(f); num=n[5:7]
    zin=zipfile.ZipFile(f); out=os.path.join(OUT,'decks',n); zout=zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED)
    hits=0
    for it in zin.infolist():
        data=zin.read(it.filename)
        if re.match(r'ppt/notesSlides/notesSlide\d+\.xml$',it.filename) and b'Our Position' in data:
            x=data.decode('utf-8')
            for m in list(re.finditer(r'<a:p>(?:(?!</a:p>).)*?Our Position(?:(?!</a:p>).)*?</a:p>',x,flags=re.S))[::-1]:
                p=m.group(0)
                txt=html.unescape(''.join(re.findall(r'<a:t>([^<]*)</a:t>',p)))
                if not OLDRX.search(txt): raise SystemExit('unexpected para in '+n+': '+txt[:200])
                newtxt=OLDRX.sub(NEW,txt)
                ppr=re.search(r'<a:pPr[^>]*/>|<a:pPr[^>]*>.*?</a:pPr>',p,flags=re.S)
                rpr=re.search(r'<a:rPr[^>]*/>|<a:rPr[^>]*>.*?</a:rPr>',p,flags=re.S)
                np='<a:p>'+(ppr.group(0) if ppr else '')+'<a:r>'+(rpr.group(0) if rpr else '')+'<a:t>'+html.escape(newtxt,quote=False)+'</a:t></a:r></a:p>'
                x=x[:m.start()]+np+x[m.end():]; hits+=1
            data=x.encode('utf-8')
        zout.writestr(it,data)
    zout.close()
    # manifest
    mf=os.path.join(BK,'manifests','unit-%s.manifest.json'%num); raw=open(mf,encoding='utf-8').read(); d=json.loads(raw); mh=0
    for s in d['slides']:
        if isinstance(s.get('notes'),str) and OLDRX.search(s['notes']): s['notes']=OLDRX.sub(NEW,s['notes']); mh+=1
    m=re.match(r'\{\n( +)"',raw); ind=len(m.group(1)) if m else None
    open(os.path.join(OUT,'manifests','unit-%s.manifest.json'%num),'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=ind))
    # verify
    z=zipfile.ZipFile(out); bad=[k for k in z.namelist() if k.startswith('ppt/') and b'Our Position' in z.read(k)]
    print(n[:12],'notes paras',hits,'manifest',mh,'left',bad,'testzip',z.testzip())
