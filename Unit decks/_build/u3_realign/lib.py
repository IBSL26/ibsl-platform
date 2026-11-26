from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
G='1A5C2C';L='EEF4EF';GOLD='C6A24C';DK='0F3B1C';TX='1F2A22';W='FFFFFF';DK2='131C15';CR='E7E5D6';GD2='CDAB49'
def rgb(h):return RGBColor.from_string(h)
def box(s,x,y,w,h,fill,line=None,rad=0.03):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    sh.adjustments[0]=rad
    sh.fill.solid();sh.fill.fore_color.rgb=rgb(fill)
    sh.line.color.rgb=rgb(line or fill);sh.line.width=Pt(1);sh.shadow.inherit=False
    sh.text_frame.text='';return sh
def txt(s,x,y,w,h,paras,size=24,color=TX,bold=False,italic=False,font='Calibri',anchor='t',align='l'):
    tb=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=tb.text_frame;tf.word_wrap=True
    for m in ('margin_left','margin_right','margin_top','margin_bottom'):setattr(tf,m,0)
    tf.vertical_anchor={'t':MSO_ANCHOR.TOP,'m':MSO_ANCHOR.MIDDLE,'b':MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(paras,str):paras=[paras]
    for i,p in enumerate(paras):
        para=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        para.alignment={'l':PP_ALIGN.LEFT,'c':PP_ALIGN.CENTER}[align]
        runs=p if isinstance(p,list) else [(p,{})]
        for t,o in runs:
            r=para.add_run();r.text=t;f=r.font
            f.size=Pt(o.get('size',size));f.bold=o.get('bold',bold);f.italic=o.get('italic',italic)
            f.name=o.get('font',font);f.color.rgb=rgb(o.get('color',color))
        if i>0:para.space_before=Pt(6)
    return tb
def title(s,t):return txt(s,0.6,0.42,12.1,0.9,t,size=36,color=G,bold=True,font='Cambria',anchor='m')
def bar(s,t,y=6.15):
    box(s,0.6,y,12.13,0.85,DK,rad=0.12);txt(s,0.9,y,11.6,0.85,t,size=24,color=W,italic=True,anchor='m')
def notes(s,t):s.notes_slide.notes_text_frame.text=t
