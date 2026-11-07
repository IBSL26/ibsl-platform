// WS5 Phase-6 verification harness (no external deps).
// Runs the VERBATIM client logic from dashboard_f.html against a minimal DOM
// stub with real synthetic events, and replicates the get_participant_final_score
// SQL arithmetic with worked examples.
//
// NOTE: true network→DB end-to-end (the actual UPDATE of submissions.score) is
// prod-only and requires the migration applied + a push, both of which the user
// owns. This harness verifies everything verifiable without those.

let pass = 0, fail = 0;
function check(name, got, want) {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  console.log((ok ? 'PASS' : 'FAIL') + '  ' + name + '  -> got ' + JSON.stringify(got) +
              (ok ? '' : '  (want ' + JSON.stringify(want) + ')'));
  ok ? pass++ : fail++;
}

// ── Minimal DOM stub ─────────────────────────────────────────────────────────
function makeEl(id) {
  return {
    id, value: '', disabled: false, _h: {},
    addEventListener(t, fn) { (this._h[t] = this._h[t] || []).push(fn); },
    dispatch(t) { (this._h[t] || []).forEach(fn => fn({ stopPropagation() {} })); }
  };
}
const scoreInput = makeEl('scoreInputBox');
const primaryBtn = makeEl('commitPrimaryBtn');
const _registry = { scoreInputBox: scoreInput };
const document = { getElementById: id => _registry[id] || null };

// ── VERBATIM gating logic copied from dashboard_f.html buildFeedbackSection ──
function ws5ScoreIsValid() {
  const raw = scoreInput.value.trim();
  if (raw === '' || !/^\d+$/.test(raw)) return false;  // integers only
  const n = Number(raw);
  return n >= 0 && n <= 100;
}
function ws5SyncCommitEnabled() {
  primaryBtn.disabled = !ws5ScoreIsValid();
}
scoreInput.addEventListener('input', ws5SyncCommitEnabled);
ws5SyncCommitEnabled();   // initial state

// ── TEST 1: button gating via real synthetic 'input' events ──────────────────
console.log('\n── TEST 1: commit-button gating (synthetic input events) ──');
check('initial empty -> button disabled', primaryBtn.disabled, true);
const cases = [
  ['50', false], ['0', false], ['100', false],   // valid -> enabled (disabled=false)
  ['', true], ['101', true], ['-5', true],        // invalid -> disabled
  ['3.5', true], ['abc', true], ['  75  ', false],// trims; integers only
  ['050', false],                                 // leading zero ok (=50)
];
for (const [val, wantDisabled] of cases) {
  scoreInput.value = val;
  scoreInput.dispatch('input');                   // fire the real handler
  check("value '" + val + "' -> disabled=" + wantDisabled, primaryBtn.disabled, wantDisabled);
}

// ── TEST 2: p_score reaches review_submission (VERBATIM extraction) ──────────
console.log('\n── TEST 2: score plumbed into review_submission rpc payload ──');
let captured = null;
const supabaseClient = { rpc: (name, params) => { captured = { name, params }; return { data: { ok: true }, error: null }; } };
function commitWithScore(submissionId, feedbackBody, unlockNext) {
  // VERBATIM from commitReview()
  const scoreEl = document.getElementById('scoreInputBox');
  let pScore = null;
  if (scoreEl && /^\d+$/.test(scoreEl.value.trim())) {
    const sv = Number(scoreEl.value.trim());
    if (sv >= 0 && sv <= 100) pScore = sv;
  }
  return supabaseClient.rpc('review_submission', {
    p_submission_id: submissionId, p_feedback: feedbackBody, p_unlock_next: unlockNext, p_score: pScore
  });
}
for (const [val, wantScore] of [['87', 87], ['0', 0], ['100', 100], ['', null], ['101', null], ['9.5', null]]) {
  scoreInput.value = val;
  commitWithScore('sub-1', 'good work', true);
  check("input '" + val + "' -> rpc p_score", captured.params.p_score, wantScore);
}
check('rpc target + existing params preserved', [captured.name, 'p_feedback' in captured.params, captured.params.p_unlock_next],
      ['review_submission', true, true]);

// ── TEST 3: get_participant_final_score arithmetic (replicates the SQL) ──────
console.log('\n── TEST 3: unit averaging + final % (replicates the RPC SQL) ──');
const round2 = x => Math.round((x + Number.EPSILON) * 100) / 100;   // half-up, like pg numeric round
function finalScore(subs) {
  // subs: [{unit, review_status, score}]  (score null = unscored)
  const scored = subs.filter(s => [2,3,4].includes(s.unit) && s.review_status === 'reviewed');
  const avg = u => {
    const v = scored.filter(s => s.unit === u && s.score !== null).map(s => s.score);
    return v.length ? v.reduce((a,b)=>a+b,0) / v.length : null;
  };
  const u2 = avg(2), u3 = avg(3), u4 = avg(4);
  const comp = a => round2((a ?? 0) * 0.25);
  const finalPct = round2((u2 ?? 0)*0.25 + (u3 ?? 0)*0.25 + (u4 ?? 0)*0.25 + 0 /*capstone null*/);
  return {
    unit_averages: { '2': u2===null?null:round2(u2), '3': u3===null?null:round2(u3), '4': u4===null?null:round2(u4) },
    unit_components: { '2': comp(u2), '3': comp(u3), '4': comp(u4) },
    capstone: null, capstone_pending: true,
    final_pct: finalPct,
    certified: (finalPct >= 80) && false,   // capstone null -> always false
    unscored_lens_count: scored.filter(s => s.score === null).length
  };
}

// Scenario A: mixed, with non-integer avg + two unscored reviewed lenses
const A = finalScore([
  {unit:1, review_status:'reviewed', score:null},          // unit 1 excluded entirely
  {unit:2, review_status:'reviewed', score:80},
  {unit:2, review_status:'reviewed', score:91},            // u2 avg 85.5
  {unit:2, review_status:'reviewed', score:null},          // unscored (counts)
  {unit:3, review_status:'reviewed', score:86},            // u3 avg 86
  {unit:4, review_status:'reviewed', score:100},
  {unit:4, review_status:'reviewed', score:null},          // unscored (counts)
  {unit:4, review_status:'submitted', score:null},         // not reviewed -> ignored
]);
// hand-computed: u2=85.5(comp21.38) u3=86(comp21.5) u4=100(comp25) final=67.88 unscored=2
check('A.unit_averages', A.unit_averages, {'2':85.5,'3':86,'4':100});
check('A.unit_components', A.unit_components, {'2':21.38,'3':21.5,'4':25});
check('A.final_pct', A.final_pct, 67.88);
check('A.certified', A.certified, false);
check('A.unscored_lens_count', A.unscored_lens_count, 2);
check('A.unit-1 excluded (no effect)', A.unit_averages['2'] !== null, true);

// Scenario B: all units perfect -> caps at 75 without capstone, still not certified
const B = finalScore([
  {unit:2, review_status:'reviewed', score:100},
  {unit:3, review_status:'reviewed', score:100},
  {unit:4, review_status:'reviewed', score:100},
]);
check('B.final_pct (max without capstone)', B.final_pct, 75);
check('B.certified (capstone null blocks)', B.certified, false);

// Scenario C: a unit with no scored reviewed submissions -> null avg, 0 component
const C = finalScore([
  {unit:2, review_status:'reviewed', score:100},
  {unit:3, review_status:'reviewed', score:100},
  // unit 4: nothing scored
]);
check('C.unit_averages.4 null', C.unit_averages['4'], null);
check('C.unit_components.4 zero', C.unit_components['4'], 0);
check('C.final_pct', C.final_pct, 50);

console.log('\n──────────────────────────────────────────────');
console.log('TOTAL: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
