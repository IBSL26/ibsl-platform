/* S2R® Portal — progressive mark accumulation (18 Nov 2026)
   Reads the units array from get_participant_final_score and renders the
   unit-by-unit build-up of the final mark. Shared by the participant portal,
   the facilitator dashboard and the admin reports. */
(function () {
  if (window.S2RMarks) return;

  var CSS =
    '.s2rm{margin-top:16px;font-family:Montserrat,sans-serif;font-size:12px;}' +
    '.s2rm summary{cursor:pointer;font-weight:600;letter-spacing:.5px;color:#c9a84c;padding:6px 0;list-style:revert;}' +
    '.s2rm-key{font-size:11px;opacity:.65;margin:6px 0 10px;line-height:1.5;}' +
    '.s2rm table{width:100%;border-collapse:collapse;}' +
    '.s2rm th{font-size:10px;font-weight:600;letter-spacing:1px;text-transform:uppercase;opacity:.6;text-align:left;padding:6px 4px;border-bottom:1px solid rgba(128,128,128,.3);}' +
    '.s2rm td{padding:7px 4px;border-bottom:1px solid rgba(128,128,128,.15);vertical-align:top;}' +
    '.s2rm .n{text-align:right;white-space:nowrap;}' +
    '.s2rm tr.pending td{opacity:.45;}' +
    '.s2rm tr.mod td{font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;opacity:.7;padding-top:12px;}' +
    '.s2rm tr.total td{font-weight:700;border-bottom:none;padding-top:10px;}';

  function injectCss() {
    if (document.getElementById('s2rm-css')) return;
    var s = document.createElement('style');
    s.id = 's2rm-css';
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  function esc(v) {
    return String(v === null || v === undefined ? '' : v)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  // One decimal place, with whole numbers shown plainly (25%, 18.3%).
  function pct(n) {
    var v = Math.round(Number(n) * 10) / 10;
    return (v % 1 === 0 ? v.toFixed(0) : v.toFixed(1)) + '%';
  }

  // Programme total: rounded down to one decimal, so a total just under 80% never shows as 80%.
  function total(n) {
    var v = Math.floor(Number(n || 0) * 10 + 1e-9) / 10;
    return (v % 1 === 0 ? v.toFixed(0) : v.toFixed(1)) + '%';
  }

  var MODULE_NAMES = { 2: 'Direction', 3: 'Influence', 4: 'Grounding' };

  function units(d) {
    return (d && Array.isArray(d.units)) ? d.units : [];
  }

  // Percentage of the final mark earned so far in one module (null when none scored).
  function moduleEarned(d, m) {
    var total = 0, any = false;
    var count = units(d).filter(function (u) { return Number(u.module) === Number(m); }).length || 1;
    units(d).forEach(function (u) {
      if (Number(u.module) === Number(m) && u.score !== null && u.score !== undefined) {
        total += Number(u.score) * (25 / count) / 100; any = true;   // exact share, so 3 x 8.33 adds to 25
      }
    });
    return any ? total : null;
  }

  // Map lens_id -> unit row, for the unit cards.
  function byLens(d) {
    var map = {};
    units(d).forEach(function (u) { map[u.lens_id] = u; });
    return map;
  }

  function table(d) {
    var list = units(d);
    if (!list.length) return '';
    injectCss();
    var scored = Number(d.units_scored_count || 0);
    var total = Number(d.units_total || list.length);
    var rows = '', lastModule = null;
    list.forEach(function (u) {
      if (u.module !== lastModule) {
        lastModule = u.module;
        rows += '<tr class="mod"><td colspan="4">Module ' + esc(u.module) + ' &middot; ' +
          esc(MODULE_NAMES[u.module] || '') + ' &middot; 25%</td></tr>';
      }
      var has = u.earned !== null && u.earned !== undefined;
      rows += '<tr' + (has ? '' : ' class="pending"') + '>' +
        '<td>Unit ' + esc(u.unit_no) + ' &middot; ' + esc(u.title) + '</td>' +
        '<td class="n">' + (has ? esc(u.score) + ' / 100' : 'Not yet marked') + '</td>' +
        '<td class="n">' + (has ? '+' + pct(u.earned) : 'up to ' + pct(u.weight)) + '</td>' +
        '<td class="n">' + (has ? pct(u.cumulative) : '') + '</td>' +
        '</tr>';
    });
    var capHas = d.capstone_earned_pct !== null && d.capstone_earned_pct !== undefined;
    rows += '<tr class="mod"><td colspan="4">Capstone &middot; 25%</td></tr>' +
      '<tr' + (capHas ? '' : ' class="pending"') + '>' +
        '<td>Capstone Blueprint</td>' +
        '<td class="n">' + (capHas ? esc(d.capstone_avg) + ' / 100' : 'Scored after the Blueprint Showcase') + '</td>' +
        '<td class="n">' + (capHas ? '+' + pct(d.capstone_earned_pct) : 'up to 25.00%') + '</td>' +
        '<td class="n">' + (capHas ? pct(d.final_pct) : '') + '</td>' +
      '</tr>' +
      '<tr class="total"><td>Final mark to date</td><td></td><td></td><td class="n">' + pct(d.final_pct || 0) + '</td></tr>';

    return '<details class="s2rm">' +
      '<summary>Mark accumulation &middot; ' + scored + ' of ' + total + ' units marked</summary>' +
      '<div class="s2rm-key">Each marked unit adds its share to the final mark: a unit in Modules 2 and 4 carries up to 8.33%, a unit in Module 3 up to 5%, and the Capstone up to 25%. Certification requires 80% or more, with the Capstone scored.</div>' +
      '<table><thead><tr><th>Unit</th><th class="n">Mark</th><th class="n">Adds</th><th class="n">Running total</th></tr></thead>' +
      '<tbody>' + rows + '</tbody></table></details>';
  }

  window.S2RMarks = { table: table, moduleEarned: moduleEarned, byLens: byLens, pct: pct, total: total };
})();
