"""Unit 2 review, 5 October 2026: apply the approved text changes to the participant and
facilitator files (codes B1-B9, C1-C13, W1-W8, D1, D2 in
"Claude outputs/Unit 2 - Review notes and proposed text.docx").

Usage: python3 apply_u02_review.py <folder with the two html files> [--write]

Every change is an exact text replacement that must match the expected number of times,
or the script stops without writing anything. Line endings (CRLF) and encoding (UTF-8) are kept.
No id, onclick, href, lens_id, save call or script logic is touched; the only script change is
the text of the SUMMARY array (one more block).
"""
import sys, os

NL = "\r\n"
P, F = "unit2_m1_lens1_p.html", "unit2_m1_lens1_f.html"

HERO_OLD = "This unit builds the master definition of strategy, the 3W1H framework, and produces two integrated outputs — a Strategic Intent Statement and a Success in Practice narrative — through collective executive co-creation."
HERO_NEW = "This unit builds the master definition of strategy and the 3W1H framework, and produces a Success in Practice (SiP) statement — a Headline and a Storyline — through collective executive co-creation."
FORCES_OLD = "the Value Triad, STAKEHOLDERS, and NAVIGATING — each with a named failure mode when absent."
FORCES_NEW = "the Value Triad, STAKEHOLDERS, NAVIGATING, and THE FORCES — each with a named failure mode when absent."
SIX = "across six groups: Process Components, Strategic Intent Dimensions (3W1H), Value Lifecycle, Operating Environment, Strategy Engine, and Strategic Chain."
SURFACED_OLD = "The collective exercise surfaced convergence — where all perspectives aligned; tension — where they contradicted or competed; missing dimensions — where no leader adequately described the future state; and dominant bias — where one functional perspective over-represented the narrative."
LAST_OLD = " The integration produced one shared Strategic Intent Statement and one co-owned SiP — the destination anchor for the next stage of the S2R® process.'}"
PRODUCED = "The integration produced one shared, co-owned SiP statement — the destination anchor for the next stage of the S2R® process."
GENERIC_PA = '<div class="fac-note-full"><div class="fac-note-full-label">&#128203; PARTICIPANT ACTIVITY</div><p>Participants complete this activity in their own file. The content below is for your preparation.</p></div>'

EDITS = {P: [
  ("D1", HERO_OLD, HERO_NEW),
  ("B1", '<span class="acc-meta">7 Concepts · Click to expand each</span>', '<span class="acc-meta">9 Concepts · Click to expand each</span>'),
  ("B4", '  <div id="w1hPanelsP"></div>' + NL,
         '  <div id="w1hPanelsP"></div>' + NL + '  <p style="margin-top:16px;">Without a clear strategic intent, every strategy discussion reverts to function-level interpretation. Strategic intent is the decision filter through which all other choices pass.</p>' + NL),
  ("C1", "The team is positioned inside the future.", "You and your leadership team stand inside the future."),
  ("B2", '  <div class="quote"><p>"If our strategic intent is sound',
         '  <p>The SiP narrative is anchored in four SiP dimensions: <strong>Customer Experience &amp; Value · Operational Capability &amp; Execution Rhythm · People &amp; Culture Dynamics · Enterprise Value Creation</strong>.</p>' + NL + '  <div class="quote"><p>"If our strategic intent is sound'),
  ("C2", "Leaders repeat it in meetings, town halls, and board discussions.", "You repeat it in meetings, town halls, and board discussions."),
  ("C3", "Leaders describe an operating reality they intend to build.", "You describe an operating reality you intend to build."),
  ("C4+D1", "<p>The Strategic Intent Statement and SiP are co-created by the leadership team. This is a strategic requirement.</p>",
            "<p>You and your leadership team co-create strategic intent and the SiP statement. This is a strategic requirement.</p>"),
  ("C4", "<li><strong>Leaders agree on the destination</strong> through genuine shared construction.</li>", "<li><strong>You agree on the destination</strong> through genuine shared construction.</li>"),
  ("B5", "<li><strong>Collective ownership is built</strong> — the only ownership that sustains during execution pressure.</li>" + NL + "  </ul>" + NL,
         "<li><strong>Collective ownership is built</strong> — the only ownership that sustains during execution pressure.</li>" + NL + "  </ul>" + NL + "  <p>When you take part in shaping the SiP statement, strategy moves from individual interpretation to shared strategic imagination.</p>" + NL),
  ("B6", '  <div class="ph-tabs" id="engTabsP">', '  <p>Strategy is the output of three interlocked components that must run simultaneously.</p>' + NL + '  <div class="ph-tabs" id="engTabsP">'),
  ("C5", "helping leaders see how their individual functions contribute to the collective outcome.", "helping you see how your function contributes to the collective outcome."),
  ("C6", "These are the specific signals that tell an executive team whether the strategy is working in that domain.", "These are the specific signals that tell you and your executive team whether the strategy is working in that domain."),
  ("C7", "<p>The executive team uses the Strategy Maturity Assessment results from Section 4 to identify the most critical corrective actions required.", "<p>Use your Strategy Maturity Assessment results from Section 4 to identify the most critical corrective actions required."),
  ("C7", "The corrective actions identified here become the inputs into your SiP Application Table below.", "The corrective actions you identify here become the inputs into your SiP Application Table in 5.2."),
  ("D2+C8", "<p>Using the corrective actions defined above, each CXO now describes all four SiP dimensions from the perspective of their assigned executive role. Write in the",
            "<p>In 4.3 you gave your first description. Here you refine it, after the assessment results and your corrective actions.</p>" + NL + "  <p>Using the corrective actions you defined in 5.1, describe all four SiP dimensions from the perspective of your assigned executive role. Write in the"),
  ("C9+D1", "These two outputs — from every CXO — will be integrated by the facilitator to produce one shared Strategic Intent Statement and one co-owned SiP that represents the collective executive view.",
            "Your facilitator will integrate these two outputs, from every role in the group, into one shared SiP statement that represents the collective executive view."),
  ("D2+C10", "<p>Following the completion of all CXO perspectives, the facilitator leads a structured synthesis to identify the four dimensions of the collective view. Record your observations from this synthesis below.</p>",
             "<p>This records the final synthesis. It builds on the first reading taken in 4.3.</p>" + NL + "  <p>When every role has contributed, your facilitator leads a structured synthesis of the collective view. Record what you observe under the four headings below.</p>"),
  ("C11", "Which of the four SiP dimensions was inadequately described by any CXO? What is the collective blind spot?", "Which of the four SiP dimensions did no role describe adequately? What is the collective blind spot?"),
  ("C12", "What does this tell the team about their strategic blind spots?", "What does this tell you, as a team, about your strategic blind spots?"),
  ("B1", FORCES_OLD, FORCES_NEW),
  ("C13", "body:'The executive team completed the 26-area Strategy Maturity Assessment " + SIX + " Each leader described the four SiP dimensions from their assigned role\\'s perspective in the present tense of the future. " + SURFACED_OLD + LAST_OLD,
          "body:'You completed the 26-area Strategy Maturity Assessment " + SIX + " You described the four SiP dimensions from your assigned role\\'s perspective in the present tense of the future. " + SURFACED_OLD.replace("where no leader adequately", "where no role adequately") + "'}," + NL
          + "  {arc:'Application — In Practice',t:'What Was Applied',body:'You converted your assessment results into corrective actions across the four SiP dimensions. You then described the four dimensions from your assigned role as the organisation operates once those gaps are closed, and distilled your view into a SiP Headline and a SiP Storyline. With your facilitator you recorded the points of convergence, the points of tension, the missing dimensions and the dominant bias. " + PRODUCED + "'}"),
], F: [
  ("D1", HERO_OLD, HERO_NEW),
  ("D1", "a Strategic Intent Statement and a Success in Practice narrative co-created by the leadership team.", "a SiP statement — a Headline and a Storyline — co-created by the leadership team."),
  ("W2", "across all three sections.", "across all three parts."),
  ("B1", '<span class="acc-meta">7 Concepts · Click to expand each</span>', '<span class="acc-meta">9 Concepts · Click to expand each</span>'),
  ("W1", "FACILITATOR GUIDANCE — Section 1</div>", "FACILITATOR GUIDANCE — Section 1.1</div>"),
  ("B1", "Directing participants through the 7 concepts:", "Directing participants through the 9 concepts:"),
  ("B1", "Which of these seven concepts is least visible", "Which of these nine concepts is least visible"),
  ("W3", "<strong>Thinking &amp; Logic</strong> (OUTPUT concept) and <strong>Process</strong> (structured container).", "<strong>Thinking &amp; Logic</strong> (the cognitive engine) and <strong>Process</strong> (the structured container)."),
  ("W1", "FACILITATOR GUIDANCE — Section 2</div>", "FACILITATOR GUIDANCE — Section 1.2</div>"),
  ("W1", "FACILITATOR GUIDANCE — Section 3</div>", "FACILITATOR GUIDANCE — Section 1.3</div>"),
  ("W4", "After section 1.3, pause before moving to Intelligence.", "After 1.3, pause before moving to Intelligence."),
  ("B3", "The SiP narrative is anchored into four observable domains: ", "The SiP narrative is anchored in four SiP dimensions: "),
  ("W5", "everything in the Integration section section is designed", "everything in the Integration section is designed"),
  ("D1", "<p>The Strategic Intent Statement and SiP are co-created by the leadership team. This is a strategic requirement.</p>", "<p>Strategic intent and the SiP statement are co-created by the leadership team. This is a strategic requirement.</p>"),
  ("D1", "When executives participate in shaping both outputs, strategy moves", "When executives participate in shaping the SiP statement, strategy moves"),
  ("D1", "what they are building today — the Intent Statement and SiP — will serve", "what they are building today — the SiP statement — will serve"),
  ("W6", "<p><strong>The existing facilitator guidance below applies here:</strong> After each leader describes their SiP perspective in the Integration section, ask the room which Flammable their perspective risks creating. Naming the imbalance explicitly is what prevents it from taking hold.</p>", ""),
  ("W6", 'ask the room: "Which of these four flammables does this perspective risk creating?" Name the imbalance explicitly.</p></div>', 'ask the room: "Which of these four flammables does this perspective risk creating?" Name the imbalance explicitly; naming it is what prevents it from taking hold.</p></div>'),
  ("B7", "<strong>Section intent:</strong> This is the production section. Everything in Awareness, Intelligence, and Extrapolating has been preparation for this. Four activities run in sequence: understanding executive role biases, completing the Strategy Maturity Assessment, contributing individual SiP narratives, and synthesising toward collective outputs. Allow sufficient time — this is the core deliverable of Unit 2.</p>",
         "<strong>Section intent:</strong> Section 4 moves the group from understanding to contribution. Three activities run in sequence: understanding executive role perspectives, completing the Strategy Maturity Assessment, and contributing individual SiP narratives. Allow sufficient time; Section 5 builds directly on what is produced here.</p>"),
  ("B7", "<p><strong>Sequencing the four activities:</strong></p><ul><li><strong>4.1</strong>", "<p><strong>Sequencing the three activities:</strong></p><ul><li><strong>4.1</strong>"),
  ("B7", "<li><strong>Summary</strong> — Unit Summary debrief (8–10 min): What this unit produced</li>", ""),
  ("B7", "<em>Suggested total section time: 55–75 minutes.</em>", "<em>Suggested total section time: 45–62 minutes.</em>"),
  ("W7", "collective draft.</em></p></div>" + GENERIC_PA, "collective draft.</em></p></div>"),
  ("W7", '  <div class="fac-note"><div class="fac-label">&#9670; FACILITATOR GUIDANCE</div><p>After all leaders complete, lead a structured synthesis: identify convergence (where all align), tension (where perspectives compete), missing dimensions (where no leader adequately described the future state), and dominant bias (which functional perspective over-represents the narrative).</p></div>' + NL, ""),
  ("B9", "SiP Headline &amp; Storyline (10–15 min): Individual contribution, then group synthesis", "SiP Headline &amp; Storyline (15–20 min): Individual contribution, then group synthesis"),
  ("B9", "<em>Suggested total section time: 55–80 minutes.</em>", "<em>Suggested total section time: 60–85 minutes.</em>"),
  ("W7", "Suggested time: 20–30 minutes.</em></p></div>" + GENERIC_PA, "Suggested time: 20–30 minutes.</em></p></div>"),
  ("D2", "  <p>Each executive leader describes the four SiP dimensions from the perspective of their assigned role.", "  <p>In 4.3 each leader gave a first description. Here each leader refines it, after the assessment results and the corrective actions.</p>" + NL + "  <p>Each executive leader describes the four SiP dimensions from the perspective of their assigned role."),
  ("D1", "<p>Individual contributions from each CXO are synthesised here into one shared Strategic Intent Statement and one co-owned SiP Headline and Storyline.</p>", "<p>Individual contributions from each CXO are synthesised here into one shared, co-owned SiP statement: a Headline and a Storyline.</p>"),
  ("W8", "lead the group through a structured analysis of the four dimensions below.", "lead the group through a structured analysis under the four headings below."),
  ("D2+W8", "  <p>The facilitator leads a structured synthesis to identify the four dimensions of the emerging collective view across all CXO contributions.</p>", "  <p>This records the final synthesis. It builds on the first reading taken in 4.3.</p>" + NL + "  <p>The facilitator leads a structured synthesis of the emerging collective view across all CXO contributions, under four headings.</p>"),
  ("W8", "Which SiP dimensions were inadequately described by any CXO. The collective blind spot.", "Which SiP dimensions no role described adequately. The collective blind spot."),
  ("B8", "read each of the four sections aloud", "read each of the five blocks aloud"),
  ("B1", FORCES_OLD, FORCES_NEW),
  ("B8", SURFACED_OLD + LAST_OLD,
         SURFACED_OLD + "'}," + NL + "  {arc:'Application — In Practice',t:'What Was Applied',body:'The assessment results were converted into corrective actions across the four SiP dimensions. Each leader then described the four dimensions from the assigned role as the organisation operates once those gaps are closed, and distilled that view into a SiP Headline and a SiP Storyline. The Integration Summary recorded the points of convergence, the points of tension, the missing dimensions and the dominant bias. " + PRODUCED + "'}"),
]}


def main(folder, write):
    results = {}
    for name, edits in EDITS.items():
        path = os.path.join(folder, name)
        s = open(path, encoding="utf-8", newline="").read()
        assert "\r\n" in s and "\n" not in s.replace("\r\n", ""), f"{name}: expected CRLF line endings throughout"
        for code, old, new in edits:
            n = s.count(old)
            if n != 1:
                sys.exit(f"{name} [{code}]: expected 1 match, found {n}: {old[:90]!r}")
            s = s.replace(old, new)
        assert "\n" not in s.replace("\r\n", ""), f"{name}: a bare line feed crept in"
        results[name] = (path, s, len(edits))
    for name, (path, s, n) in results.items():
        if write:
            open(path, "w", encoding="utf-8", newline="").write(s)
        print(f"{name}: {n} replacements {'written' if write else 'checked (dry run)'}")


if __name__ == "__main__":
    main(sys.argv[1], "--write" in sys.argv)
