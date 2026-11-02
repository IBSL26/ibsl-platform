/**
 * S2R Participant Profiles — the cohort's profiles for facilitators and the admin (2 Nov 2026).
 * Usage: S2RProfiles.open(client, cohortId, cohortName); S2RProfiles.booklet(...) prints the cohort booklet. Data: get_cohort_participant_profiles()
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
  /* The cohort booklet: a cover, then the profiles group by group, printed from its own window (A4). */
  function bookTitle(n) { return String(n || 'Cohort').replace(/^CESI_Wom[ae]n_/i, 'CESI Women Cohort_') + ' Booklet'; }
  async function booklet(client, cohortId, cohortName) {
    var w = window.open('', '_blank');
    if (!w) { alert('Your browser blocked the booklet window. Allow pop-ups for this site, then try again.'); return; }
    var title = bookTitle(cohortName), logo = new URL('logo.png', location.href).href;
    w.document.open();
    w.document.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>' + esc(title) + '</title>' +
      '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">' +
      '<style>@page{size:A4;margin:18mm 16mm;}*{box-sizing:border-box;margin:0;padding:0;}body{font-family:Montserrat,Arial,sans-serif;color:#1c1c1c;background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact;}' +
      '.bar{position:sticky;top:0;display:flex;gap:14px;align-items:center;flex-wrap:wrap;padding:12px 18px;background:#1a3a2a;color:#fff;font-size:12px;}' +
      '.bar button{background:#c9a84c;color:#1c1c1c;border:0;padding:10px 18px;font:700 10px Montserrat,Arial,sans-serif;letter-spacing:2px;text-transform:uppercase;border-radius:2px;cursor:pointer;}.bar button[disabled]{opacity:.5;cursor:wait;}' +
      '.sheet{max-width:178mm;margin:0 auto;padding:10mm 0;}' +
      '.cover{min-height:245mm;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:2px solid #1a3a2a;border-top:8px solid #c9a84c;padding:20mm;break-after:page;page-break-after:always;}' +
      '.cover img{width:42mm;margin-bottom:14mm;}.cover .k{font-size:10px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#8a6d1f;}' +
      '.cover h1{font-family:"Cormorant Garamond",Georgia,serif;font-size:34pt;font-weight:500;color:#1a3a2a;margin:6mm 0;line-height:1.15;}.cover .s{font-size:11pt;color:#444;}' +
      'h2{font-family:"Cormorant Garamond",Georgia,serif;font-size:20pt;font-weight:500;color:#1a3a2a;border-bottom:2px solid #c9a84c;padding-bottom:2mm;margin:8mm 0 2mm;break-after:avoid;page-break-after:avoid;}' +
      '.grp{break-before:page;page-break-before:always;}.grp.first{break-before:auto;page-break-before:auto;}' +
      '.m{display:flex;gap:6mm;padding:5mm 0;border-bottom:1px solid #d9d2bd;break-inside:avoid;page-break-inside:avoid;}.m img,.m .ph{width:35mm;height:45mm;object-fit:cover;flex-shrink:0;border:1px solid #c9a84c;background:#f5f2e8;}' +
      '.n{font-size:13pt;font-weight:600;color:#1a3a2a;}.r{font-size:9pt;font-weight:700;letter-spacing:.5px;color:#8a6d1f;margin-top:1mm;}.b{font-size:9.5pt;line-height:1.6;margin-top:2.5mm;white-space:pre-wrap;overflow-wrap:anywhere;}' +
      '.foot{font-size:8pt;color:#666;text-align:center;margin-top:8mm;}@media print{.bar{display:none;}.sheet{padding:0;max-width:none;}.cover{min-height:255mm;}}' +
      '</style></head><body><div class="bar"><button type="button" id="go" disabled>Print booklet</button><span id="note">Loading the profiles…</span></div><div class="sheet" id="sheet"></div></body></html>');
    w.document.close();
    var note = w.document.getElementById('note'), go = w.document.getElementById('go'), sheet = w.document.getElementById('sheet');
    try {
      var res = await client.rpc('get_cohort_participant_profiles', { p_cohort_id: cohortId });
      if (res.error) throw res.error;
      var all = res.data || [], rows = all.filter(function (r) { return r.bio || r.photo_path; }), urls = {};
      var paths = rows.map(function (r) { return r.photo_path; }).filter(Boolean);
      if (paths.length) {
        var su = await client.storage.from('participant_photos').createSignedUrls(paths, 3600);
        (su.data || []).forEach(function (r) { if (r.signedUrl) urls[r.path] = r.signedUrl; });
      }
      var html = '<div class="cover"><img src="' + esc(logo) + '" alt="IBSL"><div class="k">Institute of Behavioural Strategy &amp; Leadership</div><h1 contenteditable="true">' + esc(title) +
        '</h1><div class="s">Certified Enterprise Strategy Integrator</div><div class="foot">© 2026 Institute of Behavioural Strategy &amp; Leadership. Strategy2Results® and S2R® are trade marks of IBSL. All rights reserved.</div></div>';
      var last = null, open = false, n = 0;
      rows.forEach(function (r) {
        var g = r.team_name || 'Participants';
        if (g !== last) {
          if (open) html += '</div>';
          html += '<div class="grp' + (n === 0 ? ' first' : '') + '"><h2>' + esc(g) + '</h2>'; open = true; last = g; n++;
        }
        var u = urls[r.photo_path];
        html += '<div class="m">' + (u ? '<img alt="" src="' + esc(u) + '">' : '<div class="ph"></div>') + '<div><div class="n">' + esc(r.full_name) + '</div>' +
          (r.exec_role ? '<div class="r">' + esc(r.exec_role) + '</div>' : '') + (r.bio ? '<div class="b">' + esc(r.bio) + '</div>' : '') + '</div></div>';
      });
      if (open) html += '</div>';
      sheet.innerHTML = html;
      var left = all.length - rows.length;
      var imgs = [].slice.call(sheet.querySelectorAll('img'));
      await Promise.all(imgs.map(function (i) { return i.complete ? null : new Promise(function (d) { i.onload = i.onerror = d; }); }));
      note.textContent = rows.length + ' profile' + (rows.length === 1 ? '' : 's') + ' in this booklet.' +
        (left ? ' ' + left + ' left out: no bio or photo yet.' : '') + ' Click the title on the cover to change it.';
      go.disabled = !rows.length;
      go.onclick = function () { w.print(); };
    } catch (e) {
      console.error('[profiles] booklet failed:', e);
      note.textContent = 'The booklet could not load. Please close this window and try again.';
    }
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  window.S2RProfiles = { open: open, booklet: booklet };
})();
