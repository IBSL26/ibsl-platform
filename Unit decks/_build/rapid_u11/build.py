import copy, sys
from pptx import Presentation
SRC="Unit 10 - ESRG Alignment - Rapid Class.pptx"
OUT="Unit 11 - Culture Reinforcement & Organisational Health - Rapid Class.pptx"
p=Presentation(SRC)
tmpl=list(p.slides)
R="{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
def dup(i):
    src=tmpl[i-1]
    new=p.slides.add_slide(src.slide_layout)
    for sh in list(new.shapes): sh._element.getparent().remove(sh._element)
    bg=src._element.cSld.bg
    if bg is not None:
        nb=copy.deepcopy(bg)
        for node in nb.iter():
            rid=node.get(R+"embed")
            if rid:
                rel=src.part.rels[rid]; node.set(R+"embed",new.part.relate_to(rel._target,rel.reltype))
        new._element.cSld.insert(0,nb)
    for el in src.shapes._spTree.iterchildren():
        tag=el.tag.split('}')[1]
        if tag in('nvGrpSpPr','grpSpPr'): continue
        e=copy.deepcopy(el)
        for node in e.iter():
            for att in (R+"embed",R+"link"):
                rid=node.get(att)
                if rid:
                    rel=src.part.rels[rid]
                    node.set(att,new.part.relate_to(rel._target,rel.reltype))
        new.shapes._spTree.append(e)
    return new
def texts(s):
    return [sh for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
def put(sh,*parts):
    para=sh.text_frame.paragraphs[0]
    for extra in sh.text_frame.paragraphs[1:]: extra._p.getparent().remove(extra._p)
    runs=para.runs
    for k,r in enumerate(runs):
        r.text=parts[k] if k<len(parts) else ""
    for r in runs[len(parts):]: r._r.getparent().remove(r._r)
def fill(s,vals):
    t=texts(s); assert len(t)==len(vals),(len(t),len(vals),[x.text_frame.text[:30] for x in t])
    for sh,v in zip(t,vals):
        put(sh,*(v if isinstance(v,tuple) else (v,)))
def notes(s,txt):
    tf=s.notes_slide.notes_text_frame; tf.text=txt
exec(open("_build/rapid_u11/content.py",encoding="utf-8").read())
n=len(tmpl)
for spec in SLIDES:
    s=dup(spec[0]); fill(s,spec[1]); notes(s,spec[2])
# remove template slides
lst=p.slides._sldIdLst
for sid in list(lst)[:n]:
    p.part.drop_rel(sid.get(R+"id")); lst.remove(sid)
p.save(OUT); print("saved",len(p.slides._sldIdLst))
