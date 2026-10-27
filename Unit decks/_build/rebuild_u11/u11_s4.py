# -*- coding: utf-8 -*-
"""Unit 11 Section 4 · Integration (HTML). Text in u11_s4a.py."""
from u11_content import acc, det, tbl
from u11_s2 import box, ul
from u11_s4a import *

def tbln(h, rows, cls=''):
    def tr(r):
        tot = r[0].isupper()
        return '<tr%s>%s</tr>' % (' class="u11-tot"' if tot else '', ''.join('<td>%s</td>' % (c.title() if (k == 0 and tot) else c) for k, c in enumerate(r)))
    return ('<div class="u11-scroll"><table class="u11-tbl u11-tbln %s"><thead><tr>%s</tr></thead><tbody>\n' % (cls, ''.join('<th>%s</th>' % x for x in h))
            + '\n'.join(tr(r) for r in rows) + '\n</tbody></table></div>')
def formula(*lines): return '<div class="u11-f">%s</div>' % ''.join('<p>%s</p>' % x for x in lines)
def ci(label, text): return '<div class="hbox"><div class="u11-ci">%s</div><p>%s</p></div>' % (label, text)

def section4(fac):
    o = ['<div class="slo-box"><div class="slo-box-label">Section learning outcomes</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % x for x in LO)]
    o.append(acc('4.1 &mdash; Grounding People Performance Through Leadership Accountability',
      '<p>Organisational health is shaped by the cultural conditions leaders establish and reinforce within their teams. The extent to which employees experience trust, clarity, commitment and accountability influences how they behave, collaborate and contribute to performance.</p>\n'
      '<p>Every executive therefore has a responsibility to understand the health of their function and identify where prevailing cultural norms may be undermining people performance. Organisational health also extends beyond individual functions: employees interact across departments, and behaviours reinforced by one leadership team can strengthen or weaken performance elsewhere.</p>\n'
      '<p>Sustaining organisational health requires both functional accountability and collective executive responsibility. To fulfil this responsibility, each CXO should periodically examine the organisational health of their function against the Five Observable Health Traits, identify cultural vulnerabilities and quantify associated people-performance losses.</p>\n'
      '<p>To strengthen objectivity and minimise leadership bias, the Organisational Health Thermometer is circulated to individual employees within each function. Employees independently assess the cultural conditions they experience. Their responses are consolidated into a functional health score, which the responsible executive receives for interpretation, investigation of cultural vulnerabilities and quantification of associated people-performance losses.</p>\n'
      '<p>This integrated approach forms the Cross-CXO Health Architecture: a structured mechanism connecting functional leadership accountability with collective responsibility for organisational health and sustained people performance. A quarterly assessment and review rhythm allows leaders to examine changes and reinforce healthy cultural practices.</p>\n'
      '<h4 class="u11-h">Two Levels of Leadership Accountability</h4>\n' + tbln(['Level', 'Leadership responsibility', 'Output'], LEVELS), True))
    traits = '\n'.join(det('Trait %d &mdash; %s (Maximum 20)' % (k + 1, n),
        '<table class="u11-tbl u11-stmt"><thead><tr><th>#</th><th>Statement</th><th>Score</th></tr></thead><tbody>%s<tr class="u11-tot"><td></td><td>Trait %d Total</td><td>__ / 20</td></tr></tbody></table>' % (
        ''.join('<tr><td>%d</td><td>%s</td><td>1&ndash;5</td></tr>' % (j + 1, s) for j, s in enumerate(st)), k + 1), k == 0) for k, (n, st) in enumerate(TRAITS))
    o.append(acc('4.2 &mdash; The Organisational Health Thermometer',
      '<p>The Organisational Health Thermometer provides a common instrument for assessing the five traits of organisational health. To strengthen objectivity and minimise leadership bias, individual employees should be involved in assessing the organisational health of their function. The thermometer is circulated to employees, allowing each person to independently rate the 20 statements based on their experience of the prevailing cultural conditions. Individual assessments are subsequently consolidated to produce the overall functional health score and a score for each trait. The functional leader receives the consolidated results and remains accountable for interpreting the findings, investigating vulnerabilities and quantifying associated people-performance losses.</p>\n'
      '<h4 class="u11-h">Individual Employee Assessment &mdash; Organisational Health Thermometer</h4>\n'
      '<p>Each employee independently rates the 20 statements on a frequency scale from 1 (Never) to 5 (Always). Each trait contains four statements (maximum 20 points), producing an overall individual score out of 100. The individual ratings inform the confidential consolidated functional assessment and are completed by each employee independently.</p>\n'
      '<table class="u11-tbl u11-scale"><thead><tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th></tr></thead><tbody><tr><td>Never</td><td>Rarely</td><td>Sometimes</td><td>Usually</td><td>Always</td></tr></tbody></table>\n'
      + traits + '\n<div class="u11-total">Individual employee total score: ______ / 100</div>\n'
      '<h4 class="u11-h">Reading Your Temperature</h4>\n' + tbln(['Score', 'Temperature', 'What It Signals'], TEMP) + '\n'
      + box('Assessment safeguard', 'Employee responses should be collected confidentially. Executives receive consolidated function-level results only; individual responses remain unidentifiable. Small teams require appropriate aggregation to protect confidentiality.'),
      meta='Select each trait to open its statements'))
    o.append(acc('4.3 &mdash; From Individual Assessments to Functional Health Scores',
      '<p>After employees independently submit their thermometer responses, the assessments are consolidated by function. For each trait, add the valid individual trait totals and divide by the number of valid responses. Add the five functional trait averages to obtain the functional score out of 100. The leader receives this consolidated score and the trait-level results; the scores come from the employees’ assessments.</p>\n'
      + formula('Functional Trait Score = Sum of Individual Trait Totals ÷ Number of Valid Responses', 'Functional Health Score (/100) = Sum of Five Functional Trait Scores (/20 each)') + '\n'
      '<h4 class="u11-h">Worked Example: Operations Function</h4>\n'
      '<p>An organisation has 250 employees, including 100 in Operations. The thermometer is circulated individually to Operations employees; 85 employees submit independent assessments (85% participation). Their responses are consolidated, and the COO receives the resulting functional and trait-level scores.</p>\n'
      + tbln(['Trait', 'Q1 /20', 'Q2 /20', 'Change', 'Signal to investigate'], OPS) + '\n'
      '<p>Operations moves from Healthy &amp; Thriving (80) to Caution Zone (52). Minimal Politics and High Morale show the largest declines. The COO should examine observable behaviour, relevant people-performance evidence and the Organisational Health Pyramid, using Section 3 debiasing techniques to challenge initial assumptions. The thermometer signals vulnerability; cause and monetary loss require separate evidence.</p>'))
    o.append(acc('4.4 &mdash; Quantifying the People-Performance Losses',
      '<p>The COO investigates whether the identified health vulnerabilities are associated with measurable losses in the five categories introduced in Section 2. The following estimates are illustrative for a 12-week quarter and a 100-person Operations function.</p>\n'
      + tbln(['Hidden cost', 'Evidence / assumption', 'Calculation', 'Q2 exposure'], LOSS) + '\n'
      '<p>These estimates require evidence supporting the link to organisational health, appropriate cost assumptions and reconciliation of overlapping categories before being treated as verified losses. The leader should distinguish observed losses from assumptions and potential exposure.</p>\n'
      '<h4 class="u11-h">Functional Health Position</h4>\n' + tbl('Measure', 'Operations Q2', POSITION)))
    o.append(acc('4.5 &mdash; Consolidating Functional Health into an Enterprise Position',
      '<p>Each executive receives the consolidated assessment for their function, examines vulnerabilities and quantifies associated losses. EXCO brings the functional positions together to establish an enterprise view of organisational health and its implications for people performance.</p>\n'
      + tbln(['Function', 'CXO', 'Employees', 'Q1 /100', 'Q2 /100', 'Change', 'Q2 gross exposure'], ENT) + '\n'
      '<p class="u11-note">*Illustrative enterprise scores above are headcount-weighted, assuming equal response rates across functions. In actual reporting, calculate the enterprise average using the number of valid employee responses per function; report response rates and headcount separately.</p>\n'
      + formula('Enterprise Health Score = Σ (Functional Score × Valid Responses) ÷ Total Valid Responses') + '\n'
      '<p>Illustrative Q2 headcount-weighted calculation: [(82 × 20) + (72 × 40) + (80 × 30) + (52 × 100) + (70 × 60)] ÷ 250 = 65.28 ≈ 65.3 /100. The corresponding Q1 result is 79.76 ≈ 79.8 /100.</p>\n'
      '<p>The enterprise is Stable but Uneven, and the Operations function is in the Caution Zone. EXCO should review both the enterprise score and each function’s trait profile so that significant local vulnerabilities remain visible behind the average.</p>\n'
      '<p>The R566,500 figure is an illustrative sum of functional gross exposures; overlapping costs within or across functions must be reconciled before establishing a defensible enterprise loss estimate.</p>'))
    o.append(acc('4.6 &mdash; Sustaining the Cross-CXO Health Architecture',
      '<p>Organisational health requires consistent leadership attention because cultural conditions develop through repeated behaviours and experiences. Each quarter, the thermometer is circulated to individual employees in each function for independent assessment. The responses are consolidated confidentially and each CXO receives the functional health score and trait-level results. The executive interprets the findings, investigates cultural vulnerabilities and quantifies associated people-performance losses. EXCO then consolidates the functional positions to understand enterprise health and shared priorities for strengthening people performance.</p>'))
    if fac:
        o.append('<div class="fac-note-full"><div class="fac-note-full-label">&#9670; %s</div>\n<p>%s</p><ol class="u11-ol">%s</ol>\n</div>' % (REF_TITLE, REF_INTRO_F, ''.join('<li>%s</li>' % q for q in REF_Q)))
    else:
        flds = ''.join('<label class="fld-label">%s</label><textarea class="ref-ta" style="min-height:56px;" data-fkey="ref7" data-fidx="%d" oninput="syncFieldDebounced(\'ref7\')"></textarea>' % (q, k) for k, q in enumerate(REF_Q))
        o.append('<div class="ref-block"><div class="ref-label">&#x270E; %s</div><p class="u11-note" style="font-style:normal;">%s</p>%s'
                 '<textarea id="ref7" style="display:none;"></textarea><div class="ref-saved reflection-saved" id="ref7-saved"></div><button class="ref-save" onclick="fldSaveBtn(this,\'ref7\')">Save</button></div>' % (REF_TITLE, REF_INTRO_P, flds))
    o.append(ci('Section Closing Insight', CLOSING))
    o.append(ci('Transition to Section 5 &mdash; Application: In Practice', TRANSITION if fac else TRANSITION_P))
    return '\n'.join(o) + '\n'

def css(fac):
    c = 'var(--gold)' if fac else 'var(--teall)'
    return ('.u11-tbln td{font-size:12.5px;}\n.u11-tbln td:first-child{width:auto;}\n.u11-tot td{font-weight:700;color:rgba(255,255,255,.9)!important;border-top:1px solid rgba(255,255,255,.2);}\n'
            '.u11-stmt td:first-child{width:6%%;text-align:center;}.u11-stmt td:last-child{width:14%%;white-space:nowrap;color:rgba(255,255,255,.45);}\n'
            '.u11-scale{table-layout:fixed;}.u11-scale th,.u11-scale td{text-align:center;padding:8px 4px!important;}.u11-scale td:first-child{width:auto;}\n'
            '.u11-total{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:%s;margin:12px 0 4px;}\n'
            '.u11-f{border-left:3px solid %s;background:rgba(255,255,255,.03);padding:10px 14px;margin:12px 0;}\n.u11-f p{font-size:13px;color:rgba(255,255,255,.85);margin:4px 0;font-weight:600;}\n'
            '@media (max-width:600px){.u11-tbln{min-width:520px;}.u11-scale td{font-size:10.5px;}}\n') % (c, c)

FIELD_SPEC = '  ref7:[%s],\n' % ','.join('{l:"%s",k:"text"}' % l for l in REF_LABELS)
