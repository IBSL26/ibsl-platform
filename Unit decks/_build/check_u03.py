"""Checks on the Unit 3 deck against the two Unit 3 pages. Usage: python3 check_u03.py <deck.pptx> <participant.html> <facilitator.html>
1. No slide text below 24pt. 2. Every slide has notes that open with a bold heading. 3. The outcomes, reflection prompts,
part titles, opening question and alignment-test questions in the deck are word for word on the pages."""
import sys, re, html, json, subprocess
from pptx import Presentation
from pptx.util import Pt
from pptx.oxml.ns import qn
deck, P, F = sys.argv[1:4]
def plain(path):
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'<script.*?</script>|<style.*?</style>', lambda m: m.group(0) if 'KISS_DOMAINS' in m.group(0) or 'SUMMARY' in m.group(0) else ' ', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t)).replace('\\u2019', '’').replace("\\'", "'")
    return re.sub(r'\s+', ' ', t).replace('’', "'")
tp, tf = plain(P), plain(F)
prs = Presentation(deck); bad = 0
for i, s in enumerate(prs.slides, 1):
    for sh in s.shapes:
        if not sh.has_text_frame: continue
        for para in sh.text_frame.paragraphs:
            for r in para.runs:
                sz = r.font.size
                if sz is None:
                    d = para._p.find(qn('a:pPr'))
                    continue
                if sz < Pt(24): bad += 1; print(f'slide {i}: {sz.pt}pt "{r.text[:40]}"')
    nt = s.notes_slide.notes_text_frame
    first = nt.paragraphs[0]
    if not (first.runs and first.runs[0].font.bold): bad += 1; print(f'slide {i}: notes do not open with a bold heading')
print('slides:', len(prs.slides), '· size/notes problems:', bad)
data = json.loads(subprocess.run(['node', '-e', 'const r=require("./u03_notes.js")(require("./enrich/u03_rebuild.json"));console.log(JSON.stringify({KLO:r.KLO,SLOS:r.SLOS,REFL:r.REFL,Q:r.OPENING_Q,T:r.TEST4}))'], capture_output=True, text=True, check=True).stdout)
miss = 0
def need(label, text, where=('p', 'f')):
    global miss
    k = re.sub(r'\s+', ' ', text).replace('’', "'")
    for w in where:
        if k not in (tp if w == 'p' else tf): miss += 1; print(f'NOT ON {"participant" if w=="p" else "facilitator"} page · {label}: {text[:90]}')
for t in data['KLO']: need('key learning outcome', t)
for k, v in data['SLOS'].items():
    for t in v: need(f'section {k} outcome', t)
for k, t in data['REFL'].items(): need(f'reflection {k}', t, ('p',))
need('opening question', data['Q'])
for t in data['T']: need('alignment test', t)
titles = ['Translating Success in Practice into Action', 'KISS: Keep · Improve · Start · Stop', 'The KISS Reflection Table: Four SiP Domains', 'OKR Anatomy: Objectives & Key Results',
  'Six Steps: From KISS Output to Enterprise OKRs', 'The Danger of Moving Too Fast', 'Turning Intent into Action: The Strategy2Results® Sequence', 'Natural OKR Emphasis Across Leadership Functions',
  'Translating SiP to KISS', 'Translating KISS to OKRs: The Six Steps', 'Strategy Airport', 'What is KISS Framing & OKR Definition?', 'Why the KISS-to-OKR Sequence Matters', 'Where do OKR Hot Zones Appear?',
  'Building Collective Intelligence: From SiP to KISS to Enterprise OKRs', 'Strategy Airport: From Strategic Imagination to Operational Clearance',
  'Find Themes', 'Inspiring Objectives', 'Define Key Results', 'Alignment Test', 'Enterprise Priority', 'Priority Matrix', 'Baggage Check', 'Flight Plan',
  'Competing definitions of success across functions', 'Fragmented measurement systems that cannot be integrated', 'Slow decision-making due to misaligned incentives',
  'Disconnected Targets', 'Fragmented Efforts', 'The Activity Trap', 'Protect what is already working', 'Strengthen what is partially working', 'Introduce what does not yet exist', 'Eliminate what contradicts the SiP']
for t in titles: need('title or term', t)
print('alignment problems:', miss)
