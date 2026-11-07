/**
 * S2R Facilitator Capstone view (7 Nov 2026).
 * Usage: S2RFacCapstone.open(client, cohortId, cohortName).
 * Per group: the progress of each Capstone section (units the facilitator teaches; a lead facilitator: all),
 * the scribe, and who has and has not agreed. "Read the Blueprint" opens capstone_P.html read-only (facTeam mode).
 * No marks, comments, editing or printing. Data: get_facilitator_capstone() (migrations/facilitator_capstone_view.sql).
 * © 2026 IBSLeadership. All rights reserved. S2R® and Strategy2Results® are registered trademarks.
 */
(function () {
  'use strict';
  var TITLES = { 1: 'Behavioural Strategy Fundamentals', 2: 'Strategy Visioning & Success in Practice (SiP)', 3: 'SiP KISS Mapping & OKR Definition',
    4: 'Direction Integrity (ABCV-MBT)', 5: 'Aligning Heart & Mind', 6: 'Performance Management Setup', 7: 'Establishing Performance Expectations',
    8: 'Performance Measurement', 9: 'Strategic Unclogging', 10: 'ESRG Alignment', 11: 'Culture Reinforcement & Organisational Health', 12: 'Sustaining Performance' };
  var CSS = '.sfc-o{position:fixed;inset:0;z-index:9000;background:rgba(5,15,9,.82);display:flex;align-items:flex-start;justify-content:center;overflow-y:auto;padding:40px 16px;}' +
    '.sfc-d{width:100%;max-width:980px;background:#1c2a1e;border:1px solid rgba(201,168,76,.35);border-top:3px solid #c9a84c;border-radius:4px;padding:28px 30px;font-family:Montserrat,sans-serif;color:rgba(255,255,255,.85);}' +
    '.sfc-h{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:10px;}' +
    '.sfc-k{font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#c9a84c;}' +
    '.sfc-t{font-family:"Cormorant Garamond",Georgia,serif;font-size:1.7rem;font-weight:400;color:#fff;margin-top:4px;}' +
    '.sfc-x,.sfc-r{background:none;border:1px solid rgba(201,168,76,.55);color:#c9a84c;font:700 10px Montserrat,sans-serif;letter-spacing:2px;text-transform:uppercase;padding:9px 16px;border-radius:2px;cursor:pointer;}' +
    '.sfc-r{background:#c9a84c;color:#1c2a1e;}' +
    '.sfc-n{font-size:12px;line-height:1.6;color:rgba(255,255,255,.7);margin-bottom:6px;}' +
    '.sfc-g{border-top:1px solid rgba(201,168,76,.25);padding:18px 0 6px;}' +
    '.sfc-gh{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:6px;}' +
    '.sfc-gn{font-size:15px;font-weight:600;color:#fff;}.sfc-gm{font-size:11px;color:rgba(255,255,255,.6);margin-top:2px;}' +
    '.sfc-tb{width:100%;border-collapse:collapse;font-size:12px;margin-top:8px;}' +
    '.sfc-tb th{text-align:left;font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#c9a84c;padding:6px 8px;border-bottom:1px solid rgba(201,168,76,.3);}' +
    '.sfc-tb td{padding:8px;border-bottom:1px solid rgba(255,255,255,.07);vertical-align:top;line-height:1.5;color:rgba(255,255,255,.85);overflow-wrap:anywhere;}' +
    '.sfc-s{display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 8px;border-radius:2px;white-space:nowrap;}' +
    '.sfc-s.ok{background:rgba(125,219,163,.15);color:#7ddba3;}.sfc-s.wait{background:rgba(243,196,90,.15);color:#f3c45a;}' +
    '.sfc-s.prog{background:rgba(140,180,255,.15);color:#a9c4ff;}.sfc-s.none{background:rgba(255,255,255,.06);color:rgba(255,255,255,.5);}' +
    '.sfc-p{color:#f3a3a3;}' +
    '@media (max-width:640px){.sfc-o{padding:16px 8px;}.sfc-d{padding:20px 14px;}.sfc-tb{font-size:11px;}.sfc-tb th,.sfc-tb td{padding:6px 4px;}.sfc-s{white-space:normal;letter-spacing:0;}.sfc-tb th:nth-child(3),.sfc-tb td:nth-child(3){display:none;}}';
  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function fmt(iso) { if (!iso) return ''; var d = new Date(iso); return isNaN(d.getTime()) ? '' : d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }); }
  function close() { var o = document.getElementById('sfcO'); if (o) o.parentNode.removeChild(o); }

  function stateOf(sec) {
    var waiting = sec.version > 0 && (sec.not_yet || []).length > 0;
    if (waiting) return { cls: 'wait', text: 'Waiting for agreement' };
    if (sec.agreed) return { cls: 'ok', text: 'In the Blueprint' };
    if (sec.scribe || sec.version > 0) return { cls: 'prog', text: 'In progress' };
    return { cls: 'none', text: 'Not started' };
  }
  function detailOf(sec) {
    var bits = [];
    if (sec.version > 0 && (sec.not_yet || []).length) {
      bits.push('Not yet agreed: <span class="sfc-p">' + sec.not_yet.map(esc).join(', ') + '</span>');
      if ((sec.agreed_by || []).length) bits.push('Agreed: ' + sec.agreed_by.map(esc).join(', '));
    } else if (sec.agreed && sec.agreed_at) {
      bits.push('Agreed by all · ' + esc(fmt(sec.agreed_at)));
    } else if (sec.scribe && !sec.version) {
      bits.push('Scribe chosen; nothing written yet');
    }
    return bits.join('<br>') || '—';
  }

  function teamHtml(t, cohortId) {
    var secs = t.sections || [];
    var done = secs.filter(function (s) { return s.agreed; }).length;
    var h = '<div class="sfc-g"><div class="sfc-gh"><div><div class="sfc-gn">' + esc(t.team_name) + '</div>' +
      '<div class="sfc-gm">' + (t.members || []).map(function (m) { return esc(m.full_name); }).join(' · ') + '</div>' +
      '<div class="sfc-gm">' + done + ' of ' + secs.length + ' sections in the Blueprint</div></div>' +
      '<button type="button" class="sfc-r" data-team="' + esc(t.team_id) + '">Read the Blueprint</button></div>';
    h += '<table class="sfc-tb"><thead><tr><th>Unit</th><th>Status</th><th>Scribe</th><th>Agreement</th></tr></thead><tbody>';
    secs.forEach(function (s) {
      var st = stateOf(s);
      h += '<tr><td>Unit ' + s.unit + ' · ' + esc(TITLES[s.unit] || '') + '</td><td><span class="sfc-s ' + st.cls + '">' + st.text + '</span></td>' +
        '<td>' + esc(s.scribe || '—') + '</td><td>' + detailOf(s) + '</td></tr>';
    });
    return h + '</tbody></table></div>';
  }

  async function open(client, cohortId, cohortName) {
    close();
    if (!document.getElementById('sfcCss')) { var st = document.createElement('style'); st.id = 'sfcCss'; st.textContent = CSS; document.head.appendChild(st); }
    var o = document.createElement('div');
    o.className = 'sfc-o'; o.id = 'sfcO';
    o.innerHTML = '<div class="sfc-d" role="dialog" aria-label="Capstone progress"><div class="sfc-h"><div><div class="sfc-k">' + esc(cohortName || 'Cohort') +
      '</div><div class="sfc-t">Capstone S2R® Blueprint · Group progress</div></div><button type="button" class="sfc-x" id="sfcX">Close</button></div>' +
      '<div class="sfc-n">Shows the units you facilitate. Use it to see where a group needs support. The Blueprint is read-only here and is assessed by the panel.</div>' +
      '<div id="sfcB" class="sfc-n">Loading…</div></div>';
    document.body.appendChild(o);
    o.addEventListener('click', function (e) {
      if (e.target === o || e.target.id === 'sfcX') { close(); return; }
      var b = e.target.closest && e.target.closest('.sfc-r');
      if (b && b.getAttribute('data-team')) {
        location.href = 'capstone_P.html?facTeam=' + encodeURIComponent(b.getAttribute('data-team')) + '&cohort=' + encodeURIComponent(cohortId);
      }
    });
    var box = document.getElementById('sfcB');
    try {
      var res = await client.rpc('get_facilitator_capstone', { p_cohort_id: cohortId });
      if (res.error) throw res.error;
      var teams = res.data || [];
      if (!teams.length) { box.textContent = 'No Capstone groups in this cohort yet.'; return; }
      box.className = '';
      box.innerHTML = teams.map(function (t) { return teamHtml(t, cohortId); }).join('');
    } catch (e) {
      console.error('[fac-capstone] load failed:', e);
      box.textContent = 'The Capstone progress could not load. Please try again.';
    }
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  window.S2RFacCapstone = { open: open };
})();
