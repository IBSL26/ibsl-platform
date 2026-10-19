import re,sys
def read(x): return open(x,'rb').read().decode('utf-8')
BAR=('<div style="position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#c9a84c;color:#111811;font-family:Arial,sans-serif;font-size:12px;'
     'font-weight:700;letter-spacing:.5px;text-align:center;padding:7px 12px;">PREVIEW COPY · %s · not the live portal</div>')
pin,fin,team,mock,pout,fout,label=sys.argv[1:8]
p=read(pin)
ext='<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>\r\n<script src="/s2r-save.js"></script>\r\n<script src="/s2r-team.js"></script>'
assert p.count(ext)==1
p=p.replace(ext,'<script>\n'+read(mock)+'</script>\n<script>\n'+read(team)+'</script>')
p=re.sub(r'<title>[^<]*</title>','<title>PREVIEW · %s — Participant</title>'%label,p,count=1)
i=p.rindex('</body>'); p=p[:i]+(BAR%(label+' participant page · two-member sample group · your entries stay in this browser only'))+'\r\n'+p[i:]
f=read(fin)
m=re.search(r'<script src="https://cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2"></script>\r\n<script>\r\n\(function\(\)\{[\s\S]*?\}\)\(\);\r\n</script>\r\n',f)
assert m and 'can_facilitate_lens' in m.group(0)
f=f[:m.start()]+f[m.end():]
f=re.sub(r'<title>[^<]*</title>','<title>PREVIEW · %s — Facilitator</title>'%label,f,count=1)
i=f.rindex('</body>'); f=f[:i]+(BAR%(label+' facilitator page'))+'\r\n'+f[i:]
open(pout,'wb').write(p.encode('utf-8')); open(fout,'wb').write(f.encode('utf-8'))
