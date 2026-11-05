/* S2R® Competency block (5 Nov 2026). The competency a unit develops, shown under Key learning outcomes on the
   participant and facilitator pages. Wording matches the S2R® Competency Framework.
   Load with <script defer src="/s2r-competency-block.js" data-unit="N" data-mode="facilitator">; participant pages leave out data-mode. */
(function () {
  var C = {
    1: ['Behavioural Strategic Decision-Making', 'The competent leader recognises how bias, emotion and functional perspective shape strategic choices. They bring diverse executive views together to reach sound enterprise judgement.', ['Identify cognitive and functional bias in strategic decisions', 'Examine a strategic issue from each executive perspective', 'Apply institutional practices that build collective intelligence']],
    2: ['Strategy Formulation', 'The competent leader designs a coherent strategy and gives the organisation one shared picture of success. Leaders across functions interpret it consistently and use it to guide decisions.', ['Define a Strategy Architecture and create shared understanding of organisational position and direction', 'Crystallise a Strategy Intent Statement', 'Translate intent to future success and create one vision of Success in Practice']],
    3: ['Strategy Translation and Goal Setting', 'The competent leader turns strategic ambition into enterprise priorities and measurable results. Every priority has a clear line of sight to the intended future.', ['Apply KISS to decide what to keep, improve, start and stop', 'Translate KISS decisions into Objectives and Key Results', 'Connect Key Results to Success in Practice']],
    4: ['Strategic Validation and Risk Assessment', 'The competent leader tests strategic choices against customer reality, competitive conditions and critical assumptions. Weaknesses surface while direction can still be corrected.', ['Test Key Results against Arena, Boundaries, Competition and Value Proposition', 'Recognise role-based ABCV blind spots and assign who verifies them', 'Recognise the Industry Illusion traps of familiarity, exclusion and complacency']],
    5: ['Change Leadership and People Alignment', 'The competent leader builds the understanding and commitment that strategy needs from people. They lead change through readiness, resistance and adoption so that new behaviours last.', ['Use the OCEAVL Assessment to adapt how you lead change', 'Lead change through the 4 Checks of Mind, Heart, Hands and Habit and move people from compliance to commitment', 'Align the leadership team to lead change with one voice']],
    6: ['Performance Management', 'The competent leader connects enterprise results to the contributions of people and the organisation. Performance arrangements then support strategy, accountability and sound decisions.', ['Build an S2R® Contribution Map™ from a Key Result', 'Apply the FACES Framework to drive collective success', 'Align your performance scorecard to your contribution to Key Results']],
    7: ['Accountability and Expectation Setting', 'The competent leader establishes jointly owned expectations and secures commitment across functions. Dependencies and enabling conditions are agreed, so that delivery has clear ownership.', ['Establish expectations through clarity, capability and commitment', 'Map the Expectations Chain and the enabling promises it depends on', 'Conduct an Alignment Dialogue using the GROW model']],
    8: ['Performance Measurement and Recovery', 'The competent leader interprets performance evidence with balanced judgement and acts on it early. Meaningful progress is separated from activity, and execution stays on course.', ['Lead an Enterprise Performance Intelligence Circle', 'Recover performance through Review–Realign–Restore and the Accountability Loop', 'Diagnose measurement fractures across functions']],
    9: ['Execution Problem Solving', 'The competent leader diagnoses what is constraining people and organisational performance, and separates symptoms from causes. They mobilise a coordinated response that restores the flow of execution.', ['Diagnose the Seven Performance Clogs and your function’s part in them', 'Select the right Strategic Unclogging Lever', 'Run the Unclogging Cycle across people and organisational performance']],
    10: ['Organisational Capability Development', 'The competent leader configures the Environment, Systems, Resources and Governance that strategy needs. The organisation gains the capacity to deliver its commitments consistently.', ['Assess ESRG conditions and correct for executive bias', 'Interpret ESRG results by execution capability', 'Translate ESRG results into alignment interventions through cross-functional review']],
    11: ['Culture and Organisational Health', 'The competent leader diagnoses organisational health and its effect on strategic performance. They set the behavioural standards and cultural norms that strengthen it.', ['Diagnose organisational health and strengthen its weakest trait', 'Quantify people-performance losses', 'Build a Cultural Operating Code']],
    12: ['Sustainable Performance', 'The competent leader builds lasting institutional capability that outlives short-term results. They keep enterprise performance in continuous sight and act early when it begins to drift.', ['Maintain the Three Lines of Sight, read through WARD', 'Detect Performance Gravity and early drift', 'Apply KISS to the sustaining decisions of each quarter']]
  };
  window.S2R_COMPETENCY = C;
  var me = document.currentScript, c = me && C[me.getAttribute('data-unit')];
  if (!c) return;
  var fac = me.getAttribute('data-mode') === 'facilitator';
  function esc(s) { return String(s).replace(/[&<>"]/g, function (x) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[x]; }); }
  function run() {
    var bar = null;
    document.querySelectorAll('.klo-label').forEach(function (l) { if (/^Key learning outcomes$/i.test(l.textContent.trim())) bar = l.parentNode; });
    if (!bar || document.querySelector('.cmp-bar')) return;
    var st = document.createElement('style');
    st.textContent = '.cmp-bar{margin-top:14px;padding-top:12px;border-top:1px solid rgba(26,122,106,.25);}' +
      '.cmp-label{display:block;font-size:12px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#1a7a6a;margin-bottom:6px;}' +
      '.cmp-name{font-size:15px;font-weight:700;color:#fff;margin-bottom:4px;}' +
      '.cmp-text{font-size:13px;line-height:1.6;color:rgba(255,255,255,.75);margin-bottom:10px;}' +
      '.cmp-skills{display:flex;flex-wrap:wrap;gap:8px;}';
    document.head.appendChild(st);
    var d = document.createElement('div');
    d.className = 'cmp-bar';
    d.innerHTML = '<span class="cmp-label">' + (fac ? 'Competency being developed' : 'Competency you are developing') + '</span>' +
      '<div class="cmp-name">' + esc(c[0]) + '</div><div class="cmp-text">' + esc(c[1]) + '</div>' +
      '<div class="cmp-skills">' + c[2].map(function (s) { return '<span class="klo">' + esc(s) + '</span>'; }).join('') + '</div>';
    bar.parentNode.insertBefore(d, bar.nextSibling);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
