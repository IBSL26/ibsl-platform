/**
 * S2R Participant Profiles — the cohort's profiles for facilitators and the admin (2 Nov 2026).
 * Usage: S2RProfiles.open(client, cohortId, cohortName). Data: get_cohort_participant_profiles()
 * (migrations/participant_profiles.sql). Photos sit in the private participant_photos bucket.
 * © 2026 IBSLeadership. All rights reserved. S2R® and Strategy2Results® are registered trademarks.
 */
(function () {
  'use strict';
  var CSS = '.spf-o{position:fixed;inset:0;z-index:9000;background:rgba(5,15,9,.82);display:flex;align-items:flex-start;justify-content:center;overflow-y:auto;padding:40px 16px;}' +
    '.spf-d{width:100%;max-width:860px;background:#1c2a1e;border:1px solid rgba(201,168,76,.35);border-top:3px solid #c9a84c;border-radius:4px;padding:28px 30px;font-family:Montserrat,sans-serif;color:rgba(255,255,255,.85);}' +
    '.spf-h{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:14px;}' +
    '.spf-k{font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#c9a84c;}' +
    '.spf-t{font-family:"Cormorant Garamond",Georgia,serif;font-size:1.7rem;font-weight:400;color:#fff;margin-top:4px;}' +
    '.spf-x{background:none;border:1px solid rgba(201,168,76,.55);color:#c9a84c;font:700 10px Montserrat,sans-serif;letter-spacing:2px;text-transform:uppercase;padding:9px 16px;border-radius:2px;cursor:pointer;}' +
    '.spf-g{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#c9a84c;margin:22px 0 4px;}' +
    '.spf-m{display:flex;gap:16px;padding:14px 0;border-top:1px solid rgba(201,168,76,.2);}' +
    '.spf-m img,.spf-ph{width:70px;height:90px;object-fit:cover;flex-shrink:0;border:1px solid rgba(201,168,76,.35);border-radius:2px;background:rgba(255,255,255,.05);}' +
    '.spf-n{font-size:14px;font-weight:600;color:#fff;}.spf-r{font-size:11px;font-weight:600;color:#c9a84c;margin-top:2px;}' +
    '.spf-b{font-size:12px;line-height:1.65;margin-top:6px;white-space:pre-wrap;overflow-wrap:anywhere;}.spf-e{font-size:13px;line-height:1.7;}';
  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function close() { var o = document.getElementById('spfO'); if (o) o.parentNode.removeChild(o); }
  async function open(client, cohortId, cohortName) {
    close();
    if (!document.getElementById('spfCss')) { var st = document.createElement('style'); st.id = 'spfCss'; st.textContent = CSS; document.head.appendChild(st); }
    var o = document.createElement('div');
    o.className = 'spf-o'; o.id = 'spfO';
    o.innerHTML = '<div class="spf-d" role="dialog" aria-label="Participant profiles"><div class="spf-h"><div><div class="spf-k">' + esc(cohortName || 'Cohort') +
      '</div><div class="spf-t">Participant profiles</div></div><button type="button" class="spf-x" id="spfX">Close</button></div><div id="spfB" class="spf-e">Loading…</div></div>';
    document.body.appendChild(o);
    o.addEventListener('click', function (e) { if (e.target === o || e.target.id === 'spfX') close(); });
    var box = document.getElementById('spfB');
    try {
      var res = await client.rpc('get_cohort_participant_profiles', { p_cohort_id: cohortId });
      if (res.error) throw res.error;
      var rows = res.data || [], urls = {};
      var paths = rows.map(function (r) { return r.photo_path; }).filter(Boolean);
      if (paths.length) {
        var su = await client.storage.from('participant_photos').createSignedUrls(paths, 3600);
        (su.data || []).forEach(function (r) { if (r.signedUrl) urls[r.path] = r.signedUrl; });
      }
      if (!rows.length) { box.textContent = 'No participants in this cohort yet.'; return; }
      var last = null, html = '';
      rows.forEach(function (r, i) {
        var g = r.team_name || 'Not yet in a group';
        if (i === 0 || g !== last) { html += '<div class="spf-g">' + esc(g) + '</div>'; last = g; }
        var u = urls[r.photo_path];
        html += '<div class="spf-m">' + (u ? '<img alt="" src="' + esc(u) + '">' : '<div class="spf-ph"></div>') +
          '<div><div class="spf-n">' + esc(r.full_name) + '</div><div class="spf-r">' + esc(r.exec_role || 'Position not yet chosen') + '</div>' +
          '<div class="spf-b">' + esc(r.bio || 'Bio not yet added.') + '</div></div></div>';
      });
      box.innerHTML = html;
    } catch (e) {
      console.error('[profiles] load failed:', e);
      box.textContent = 'The profiles could not load. Please try again.';
    }
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  window.S2RProfiles = { open: open };
})();
