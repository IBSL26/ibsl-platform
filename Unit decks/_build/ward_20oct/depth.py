import sys,re
from html.parser import HTMLParser
VOID={'br','img','input','meta','link','hr','source','wbr','col','area','base','embed','param','track'}
class P(HTMLParser):
    def __init__(s):super().__init__();s.st=[];s.marks={}
    def handle_starttag(s,tag,a):
        a=dict(a)
        if tag in VOID:return
        s.st.append((tag,a.get('id'),a.get('class')))
    def handle_endtag(s,tag):
        if tag in VOID:return
        for i in range(len(s.st)-1,-1,-1):
            if s.st[i][0]==tag: del s.st[i:]; return
    def handle_data(s,d):
        for k in sys.argv[2:]:
            if k in d and k not in s.marks: s.marks[k]=[x[1] or x[2] for x in s.st if x[0]=='div'][-9:]
p=P();p.feed(open(sys.argv[1],encoding='utf-8').read())
for k,v in p.marks.items(): print(repr(k),len(v),v)
