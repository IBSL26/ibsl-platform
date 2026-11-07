// WS5.5 verification — Fix 2 (roster dot hover tooltip) + Fix 3 (printed report
// lens score). Mirrors the exact logic added to dashboard_F.html / collection.html.

let pass = 0, fail = 0;
const check = (name, cond, detail) => {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + (detail ? '  → ' + detail : '')); }
};

// ─── Fix 2a: build score map + attach to lens_states (dashboard_F.html) ─────
// submissions rows ordered ascending by submitted_at; latest write wins.
function attachScores(participants, lensRows) {
  const scoreByKey = {};
  lensRows.forEach(function(r) {
    if (r) scoreByKey[r.profile_id + '|' + r.lens_id] = r.score;  // asc → latest wins
  });
  participants.forEach(function(p) {
    if (!Array.isArray(p.lens_states)) return;
    p.lens_states.forEach(function(ls) {
      const sc = scoreByKey[p.participant_id + '|' + ls.lens_id];
      if (typeof sc === 'number') ls.score = sc;
    });
  });
  return participants;
}

console.log('\nFix 2a — attach per-lens scores (profile_id ↔ participant_id, latest-wins):');
const participants = [{
  participant_id: 'prof-1',
  lens_states: [
    { lens_id: 'foundations', unit: 1, status: 'completed' },   // never scored
    { lens_id: 'u2-a',       unit: 2, status: 'completed' },     // scored 85
    { lens_id: 'u3-a',       unit: 3, status: 'submitted' },     // reviewed, no score
    { lens_id: 'u4-a',       unit: 4, status: 'completed' },     // revised: 70 then 90
    { lens_id: 'locked-x',   unit: 2, status: 'locked' }         // no submission
  ]
}];
const lensRows = [
  { profile_id: 'prof-1', lens_id: 'foundations', score: null, submitted_at: '2026-05-01' },
  { profile_id: 'prof-1', lens_id: 'u2-a',        score: 85,   submitted_at: '2026-05-02' },
  { profile_id: 'prof-1', lens_id: 'u3-a',        score: null, submitted_at: '2026-05-03' },
  { profile_id: 'prof-1', lens_id: 'u4-a',        score: 70,   submitted_at: '2026-05-04' }, // earlier
  { profile_id: 'prof-1', lens_id: 'u4-a',        score: 90,   submitted_at: '2026-05-09' }  // latest
];
attachScores(participants, lensRows);
const byId = {};
participants[0].lens_states.forEach(ls => byId[ls.lens_id] = ls);
check('scored lens gets numeric score', byId['u2-a'].score === 85);
check('Foundations (null) gets NO score attached', !('score' in byId['foundations']));
check('reviewed-but-unscored (null) gets NO score', !('score' in byId['u3-a']));
check('revised lens uses LATEST submission score (90, not 70)', byId['u4-a'].score === 90);
check('locked lens (no submission) gets NO score', !('score' in byId['locked-x']));

// ─── Fix 2b: tooltip suffix in lensDotEl (dashboard_F.html) ─────────────────
function capitalize(s){ return s ? s.charAt(0).toUpperCase()+s.slice(1) : s; }
function dotTooltip(lensState) {
  const status = String(lensState.status || 'locked').toLowerCase();
  const scoreSuffix = (typeof lensState.score === 'number') ? ' · Score: ' + lensState.score + ' / 100' : '';
  return (lensState.lens_title || lensState.lens_id) + ' — ' + capitalize(status) + scoreSuffix;
}
console.log('\nFix 2b — dot hover tooltip:');
let t = dotTooltip({ lens_title: 'Self-Awareness', status: 'completed', score: 85 });
console.log('   →', t);
check('scored dot shows "· Score: 85 / 100"', t.includes(' · Score: 85 / 100'));
t = dotTooltip({ lens_title: 'Foundations', status: 'completed' });
console.log('   →', t);
check('unscored/Foundations dot has NO score suffix', !t.includes('Score'));
t = dotTooltip({ lens_id: 'u2-a', status: 'completed', score: 0 });
console.log('   →', t);
check('score of 0 still shows (typeof number)', t.includes('· Score: 0 / 100'));

// ─── Fix 3: printed-report sub line (collection.html) ───────────────────────
function subLine(latest) {
  var dt = latest.submitted_at;  // fmtDate already applied upstream; pass formatted
  var subText = dt ? ("Submitted "+dt) : "";
  if(typeof latest.score==="number"){ subText += (subText ? " · " : "") + "Score: "+latest.score+" / 100"; }
  return subText;
}
console.log('\nFix 3 — printed report "Submitted [date]" line:');
let s = subLine({ submitted_at: '29 May 2026', score: 85 });
console.log('   →', s);
check('scored lens: "Submitted 29 May 2026 · Score: 85 / 100"', s === 'Submitted 29 May 2026 · Score: 85 / 100');
s = subLine({ submitted_at: '29 May 2026', score: null });
console.log('   →', s);
check('Foundations/unscored (null): date only, no "· Score"', s === 'Submitted 29 May 2026');
s = subLine({ submitted_at: '29 May 2026' });
console.log('   →', s);
check('score absent (undefined): date only', s === 'Submitted 29 May 2026');
s = subLine({ submitted_at: '1 Jun 2026', score: 0 });
console.log('   →', s);
check('score 0: shows "· Score: 0 / 100"', s === 'Submitted 1 Jun 2026 · Score: 0 / 100');

console.log('\n──────────────────────────────');
console.log('PASS: ' + pass + '   FAIL: ' + fail);
process.exit(fail ? 1 : 0);
