/* S2R® Unit 1 marking sheet (7 Nov 2026). Shown to the participant on their Unit 1 page and in the
   Learning Portfolio once the facilitator has selected Mark as reviewed. Data: get_u1_sheet(). */
(function () {
  var SKILLS = ['Identify cognitive and functional bias in strategic decisions',
                'Examine a strategic issue from each executive perspective',
                'Apply institutional practices that build collective intelligence'];
  var SECTIONS = { 1: '1 · Orientation', 2: '2 · Awareness', 3: '3 · Intelligence', 4: '4 · Extrapolating', 5: '5 · Integration' };
  // [key, reflection, skill index (-1: not marked)]
  var ROWS = [['r_m1_intent', 'Intent', -1], ['r_m2_bs', 'Behavioural Strategy', 0], ['r_m2_sys', 'System 1 vs System 2', 0],
              ['r_m2_elephant', 'The Elephant Problem', 1], ['r_m2_bias', 'Bias Families', 0], ['r_m3_cxo', 'Executive Role Translation', 1],
              ['r_m3_cost', 'Hidden Costs', 0], ['r_m4_phase', 'Phases of Strategy', 0], ['r_m4_climate', 'Emotional Climate', 2],
              ['r_m4_principles', 'Six Principles', 2], ['r_m5_integration', 'Integration', 1], ['r_m5_pillars', 'Three Pillars', 2],
              ['r_m5_practices', 'Institutional Practices', 2]];
  var LABELS = { not_evidenced: 'Not evidenced', evidenced: 'Evidenced', developing_others: 'Evidenced and developing others' };

  function render(client, profileId, cohortId, mount, opts) {
    opts = opts || {};
    if (!client || !profileId || !cohortId || !mount) return;
    Promise.resolve(client.rpc('get_u1_sheet', { p_profile_id: profileId, p_cohort_id: cohortId })).then(function (r) {
      if (!r || r.error || !r.data) return;
      var marks = r.data.marks || {}, answered = r.data.answered || [];
      var line = opts.dark ? 'rgba(255,255,255,.15)' : '#ddd';
      var head = opts.dark ? 'rgba(201,168,76,.6)' : '#c9a84c';
      var wrap = document.createElement('div');
      wrap.style.cssText = 'margin:16px 0;';
      var h = document.createElement(opts.dark ? 'div' : 'div');
      h.className = opts.headingClass || '';
      h.style.cssText = opts.headingClass ? '' : 'font-weight:700;margin-bottom:6px;';
      h.textContent = opts.heading || 'Your marking sheet';
      wrap.appendChild(h);
      if (opts.sub !== false) {
        var p = document.createElement('div');
        p.style.cssText = 'font-size:12px;opacity:.8;margin-bottom:8px;';
        p.textContent = 'Each reflection, the skill it evidences and your facilitator’s judgement of the evidence.';
        wrap.appendChild(p);
      }
      var t = document.createElement('table');
      t.style.cssText = 'width:100%;border-collapse:collapse;font-size:12px;line-height:1.5;';
      var tr0 = document.createElement('tr');
      ['Section', 'Reflection', 'Skill', 'Skill evidence'].forEach(function (x) {
        var th = document.createElement('th');
        th.textContent = x;
        th.style.cssText = 'text-align:left;padding:6px 8px;border-bottom:1px solid ' + head + ';font-weight:700;';
        tr0.appendChild(th);
      });
      t.appendChild(tr0);
      ROWS.forEach(function (row) {
        var k = row[0], si = row[2], n = (k.match(/^r_m(\d+)_/) || [])[1];
        var mark = si < 0 ? 'Opening reflection, not marked'
          : (answered.indexOf(k) < 0 ? 'Not answered' : (LABELS[marks[k]] || 'Not judged'));
        var tr = document.createElement('tr');
        [SECTIONS[n] || '', row[1], si < 0 ? '—' : SKILLS[si], mark].forEach(function (x, ci) {
          var td = document.createElement('td');
          td.textContent = x;
          td.style.cssText = 'padding:6px 8px;border-bottom:1px solid ' + line + ';vertical-align:top;' + (ci === 3 ? 'font-weight:600;' : '');
          tr.appendChild(td);
        });
        t.appendChild(tr);
      });
      wrap.appendChild(t);
      mount.innerHTML = '';
      mount.appendChild(wrap);
    }, function () {});
  }
  window.S2R_U1_SHEET = { render: render };
})();
