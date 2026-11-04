/**
 * S2R Competency gate (4 Nov 2026)
 * Loaded on participant unit pages. When the facilitator has opened this unit, the participant first
 * completes any outstanding Competency Self-Rating or Unit Feedback form.
 * The check sits on top of the unit lock. If it cannot run, the unit stays open, so a fault never blocks a class.
 * Use: <script src="/s2r-competency-gate.js" data-unit="3"></script>
 */
(function () {
  'use strict';
  var script = document.currentScript;
  var unit = script ? parseInt(script.getAttribute('data-unit'), 10) : 0;
  if (!unit) return;
  function page() { return location.pathname.split('/').pop(); }
  function run(tries) {
    if (!window.S2R || typeof S2R.context !== 'function' || !S2R._client) {
      if (tries > 0) setTimeout(function () { run(tries - 1); }, 200);
      return;
    }
    S2R.context().then(function (ctx) {
      if (!ctx || ctx.role !== 'participant') return null;
      return S2R._client.rpc('competency_gate', { p_cohort_id: ctx.cohortId, p_unit_no: unit }).then(function (r) {
        if (r.error || !r.data || !r.data.blocked) return;
        var target = 'competency.html?view=' + (r.data.need === 'self' ? 'self' : 'unit&unit=' + r.data.unit_no) +
          '&return=' + encodeURIComponent(page());
        location.replace(target);
      });
    }).catch(function () { /* unit stays open */ });
  }
  run(25);
})();
