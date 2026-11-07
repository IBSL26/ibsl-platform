// WS5.3 Phase-6 verification (no external deps).
// Extracts the reconciled renderFinalScoreSummary from dashboard_F.html and
// feeds it flat-shape get_participant_final_score JSON, plus static checks that
// the panel left the lens-review view and is wired once per roster row.

import fs from 'node:fs';

let pass = 0, fail = 0;
function check(name, cond, extra) {
  console.log((cond ? 'PASS' : 'FAIL') + '  ' + name + (cond ? '' : '   ' + (extra || '')));
  cond ? pass++ : fail++;
}

const file = fs.readFileSync(new URL('../dashboard_F.html', import.meta.url), 'utf8');

// ── Extract the real renderFinalScoreSummary ─────────────────────────────────
const s = file.indexOf('function renderFinalScoreSummary(');
const e = file.indexOf('// ─── COLLAPSIBLE SECTION WRAPPER', s);
const renderFinalScoreSummary = new Function('escapeHtml',
  file.slice(s, e) + '\nreturn renderFinalScoreSummary;'
)(x => x);

function renderToHtml(d) {
  const mount = { innerHTML: '', style: {} };
  renderFinalScoreSummary(mount, d);
  return mount.innerHTML;
}

// ── (a) fully-scored participant ─────────────────────────────────────────────
console.log('\n── (a) fully-scored (flat shape) ──');
const aHtml = renderToHtml({ unit2_avg: 85, unit3_avg: 90, unit4_avg: 100, capstone_avg: null,
  capstone_pending: true, final_pct: 68.75, certified: false, unscored_lens_count: 0 });
check('(a) three unit averages render',
      aHtml.includes('85 / 100') && aHtml.includes('90 / 100') && aHtml.includes('100 / 100'), aHtml);
check('(a) final % renders', aHtml.includes('68.75%'));
check('(a) NOT the old degraded "Not yet scored" text', !aHtml.includes('Not yet scored'));
check('(a) no "in progress" when fully scored', !aHtml.includes('in progress'));
check('(a) capstone Pending + Not-yet-certified badge',
      aHtml.includes('Pending') && aHtml.includes('not-certified') && aHtml.includes('>Not yet certified<'));

// certified-true sample proves badge path
const certHtml = renderToHtml({ unit2_avg: 95, unit3_avg: 95, unit4_avg: 95, capstone_avg: null,
  capstone_pending: true, final_pct: 90, certified: true, unscored_lens_count: 0 });
check('badge flips to Certified when certified:true', certHtml.includes('is-certified') && certHtml.includes('>Certified<'));

// ── (b) partial participant ──────────────────────────────────────────────────
console.log('\n── (b) partial (flat shape) ──');
const bHtml = renderToHtml({ unit2_avg: 80, unit3_avg: null, unit4_avg: null, capstone_avg: null,
  capstone_pending: true, final_pct: 20, certified: false, unscored_lens_count: 2 });
check('(b) null unit avgs render "in progress" (x2)', (bHtml.match(/in progress/g) || []).length === 2, bHtml);
check('(b) scored unit still shows number', bHtml.includes('80 / 100'));
check('(b) unscored-count note shown', bHtml.includes('2 reviewed lenses not yet scored'));
check('(b) no stale nested-shape reads (unit_averages)', !bHtml.includes('undefined'));

// ── (c) panel removed from the lens-review view ──────────────────────────────
console.log('\n── (c) panel no longer in lens-review view ──');
check('(c) old per-submission loader name fully retired', !file.includes('loadFinalScoreSummary'));
check('(c) review-view finalScoreEl creation gone', !file.includes('finalScoreEl'));
check('(c) review view documents the move', file.includes('WS5.3: the certification-progress panel moved OUT'));

// ── (d) wired once per participant row, with the right IDs ────────────────────
console.log('\n── (d) one panel per participant row, correct IDs ──');
check('(d) mount div lives in the participant notes panel',
      file.includes('participant-cert-summary final-score-summary'));
check('(d) loaded with p.participant_id + cohortId from the row',
      file.includes("loadParticipantFinalScore(p.participant_id, cohortId, panel.querySelector('.participant-cert-summary'))"));
check('(d) loader calls RPC with those params',
      /p_profile_id:\s*profileId/.test(file) && /p_cohort_id:\s*cohortId/.test(file));
// exactly one mount + one load call (one panel per row, not per lens)
check('(d) exactly one cert mount + one load call',
      (file.match(/participant-cert-summary final-score-summary/g) || []).length === 1 &&
      (file.match(/loadParticipantFinalScore\(p\.participant_id/g) || []).length === 1);

console.log('\n──────────────────────────────────────────────');
console.log('TOTAL: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
