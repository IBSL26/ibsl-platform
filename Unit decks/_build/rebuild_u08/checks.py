import sys,re,subprocess,tempfile,os
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',newline='').read()
    scripts=re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>',t,re.S)
    for i,s in enumerate(scripts):
        p=tempfile.mktemp(suffix='.js');open(p,'w').write(s)
        r=subprocess.run(['node','--check',p],capture_output=True,text=True)
        if r.returncode: print(f,'script',i,'FAIL',r.stderr[:400])
    body=re.sub(r'<(script|style)\b.*?</\1>','',t,flags=re.S)
    print(f,'scripts',len(scripts),'div open',len(re.findall(r'<div\b',body)),'close',body.count('</div>'),'</script>',t.count('</script>'),'<script',len(re.findall(r'<script\b',t)),'CR-only LF',('\n' in t.replace('\r\n','')))
