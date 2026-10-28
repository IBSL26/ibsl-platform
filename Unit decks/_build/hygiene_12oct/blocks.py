import re
VOID={'br','img','input','hr','meta','link','source','wbr','area','col','embed','param','track'}
TAG=re.compile(r'<!--.*?-->|<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>',re.S)
def skip_raw(t,i,name):
    j=t.lower().find('</'+name,i); return j
def children(t,start):
    """start = index of an opening <div ...>. Returns (end_index_after_close, [(s,e) of direct children incl. text chunks])."""
    m=TAG.match(t,start); assert m and m.group(2).lower()=='div'
    depth=1; i=m.end(); kids=[]; cs=None
    while True:
        m=TAG.search(t,i)
        if not m: raise Exception('unclosed')
        if m.group(0).startswith('<!--'):
            if depth==1: kids.append((m.start(),m.end()))
            i=m.end(); continue
        close,name,selfc=m.group(1),m.group(2).lower(),m.group(3)
        if name in ('script','style') and not close:
            j=skip_raw(t,m.end(),name); k=t.find('>',j)+1
            if depth==1: kids.append((m.start(),k))
            i=k; continue
        if close:
            depth-=1
            if depth==1 and cs is not None: kids.append((cs,m.end())); cs=None
            if depth==0: return m.end(),kids
        elif name not in VOID and not selfc:
            if depth==1: cs=m.start()
            depth+=1
        else:
            if depth==1: kids.append((m.start(),m.end()))
        i=m.end()
def mods(t):
    return [(m.start(),m.group(1)) for m in re.finditer(r'<div\b[^>]*\bid="(mod\d+)"',t)]
