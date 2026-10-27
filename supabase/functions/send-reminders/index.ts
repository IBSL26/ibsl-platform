// send-reminders — the hourly reminder run. Called by the database scheduler (pg_cron), never by a person.
//
// Each run does three things, and each item is sent once only:
//   1. Session reminder: the day before a live session, an email to every active cohort member
//      (participants and facilitators) with the date, time and Join session button.
//      Sent 1 to 26 hours before the start, for sessions already sent to the cohort more than a day
//      ahead. A session whose time changes gets a fresh reminder.
//   2. Blueprint reminder: 3 days before the Capstone S2R Blueprint submission deadline, an email to every member
//      of each Capstone team in the cohort, with the team's agreed-sections count.
//   3. Missed-session alert: one email to the IBSL admin inbox listing the participants marked absent
//      since the last run, with a pointer to the drafted check-ins in the admin console.
//
// Secrets: RESEND_API_KEY, SB_SERVICE_ROLE_KEY (same as the other email functions) and CRON_SECRET
// (a random value also written into the scheduler job, so nobody else can trigger a run).

import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const RESEND_API_KEY       = Deno.env.get('RESEND_API_KEY')!
const SUPABASE_URL         = Deno.env.get('SUPABASE_URL')!
const SUPABASE_SERVICE_KEY = Deno.env.get('SB_SERVICE_ROLE_KEY')!
const CRON_SECRET          = Deno.env.get('CRON_SECRET') || ''
const PORTAL_URL           = 'https://ibslportal.netlify.app'
const FROM_ADDRESS         = 'IBSLeadership S2R Portal <noreply@mail.ibsleadership.com>'
const ADMIN_INBOX          = 'projects@ibsleadership.com'

const DISPLAY_OFFSET_MIN = 120       // email text shows GMT+2
const DISPLAY_TZ_LABEL   = 'GMT+2'
const SESSION_WINDOW_H   = 26        // remind when the session starts within this many hours
const SESSION_MIN_H      = 1         // ...but not in the last hour
const BLUEPRINT_DAYS     = 3         // remind this many days before the Blueprint deadline
const SEND_GAP_MS        = 600

const HOUR = 3600000
const MON = ['January','February','March','April','May','June','July','August','September','October','November','December']
const DOW = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
const pad = (n: number) => (n < 10 ? '0' : '') + n
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } })
}
function esc(s: unknown): string {
  return String(s ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;')
}
function local(d: Date) {
  const s = new Date(d.getTime() + DISPLAY_OFFSET_MIN * 60000)
  return {
    day:  `${DOW[s.getUTCDay()]} ${s.getUTCDate()} ${MON[s.getUTCMonth()]}`,
    time: `${pad(s.getUTCHours())}:${pad(s.getUTCMinutes())}`,
  }
}
function firstName(full?: string | null) {
  return (full || '').trim().split(' ')[0] || 'there'
}

// The same email shell as the session invitations.
function shell(heading: string, firstLine: string, paras: string[], rows: [string, string][],
               button: { label: string; url: string } | null, foot: string) {
  const row = (label: string, value: string) =>
    `<tr><td style="padding:6px 16px 6px 0;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,0.45);vertical-align:top;white-space:nowrap;">${label}</td>` +
    `<td style="padding:6px 0;font-size:14px;color:#ffffff;line-height:1.5;">${value}</td></tr>`
  const p = (t: string) => `<p style="margin:16px 0 0;font-size:14px;color:rgba(255,255,255,0.75);line-height:1.7;">${t}</p>`
  const btn = button
    ? `<tr><td style="padding:28px 44px 8px;">
  <a href="${esc(button.url)}" style="display:inline-block;background:#2a7a7a;color:#ffffff;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;text-decoration:none;padding:14px 28px;border-radius:3px;">${button.label}</a>
</td></tr>`
    : ''
  const footRow = `<tr><td style="padding:0 44px 32px;">
  <p style="margin:20px 0 0;padding-top:20px;border-top:1px solid rgba(201,168,76,0.15);font-size:11px;color:rgba(255,255,255,0.45);line-height:1.6;">${foot}</p>
  ${button ? `<p style="margin:8px 0 0;font-size:11px;color:rgba(255,255,255,0.35);line-height:1.6;">If the button does not work, copy this link into your browser:<br><a href="${esc(button.url)}" style="color:#2a7a7a;word-break:break-all;">${esc(button.url)}</a></p>` : ''}
</td></tr>`
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#0d1f15;font-family:'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#0d1f15;padding:40px 20px;">
<tr><td align="center">
<table width="560" cellpadding="0" cellspacing="0" style="background:#1c2a1e;border:1px solid rgba(42,122,122,0.35);border-radius:6px;overflow:hidden;max-width:560px;width:100%;">
<tr><td style="background:#2a7a7a;padding:4px 0;"></td></tr>
<tr><td style="padding:36px 44px 0;">
  <p style="margin:0;font-size:10px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#2a7a7a;">S2R® Portal · IBSLeadership</p>
  <h1 style="margin:12px 0 0;font-size:28px;font-weight:300;color:#ffffff;font-family:Georgia,serif;">${heading}</h1>
</td></tr>
<tr><td style="padding:24px 44px 0;">
  <p style="margin:0;font-size:14px;color:rgba(255,255,255,0.75);line-height:1.7;">${firstLine}</p>
  ${paras.map(p).join('')}
  ${rows.length ? `<table cellpadding="0" cellspacing="0" style="margin:20px 0 0;">${rows.map(([a, b]) => row(a, b)).join('')}</table>` : ''}
</td></tr>
${btn}
${footRow}
<tr><td style="padding:20px 44px;background:rgba(0,0,0,0.2);">
  <p style="margin:0;font-size:10px;color:rgba(255,255,255,0.25);letter-spacing:1px;">© 2026 IBSLeadership · Strategy2Results® · S2R® Portal</p>
</td></tr>
</table></td></tr></table>
</body></html>`
}

async function sendOne(payload: Record<string, unknown>) {
  for (let attempt = 0; attempt < 2; attempt++) {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
    if (res.ok) return { ok: true, error: '' }
    const data = await res.json().catch(() => ({}))
    if (res.status === 429 && attempt === 0) { await sleep(1500); continue }
    return { ok: false, error: (data as { message?: string })?.message || `email_send_failed_${res.status}` }
  }
  return { ok: false, error: 'email_send_failed' }
}

type Person = { id: string; full_name?: string | null; email?: string | null; suspended?: boolean | null; deactivated_at?: string | null }
function activeUnique(people: Person[]) {
  const seen = new Set<string>()
  return people.filter((p) => {
    const e = (p.email || '').trim().toLowerCase()
    if (!e || p.suspended || p.deactivated_at || seen.has(e)) return false
    seen.add(e)
    return true
  })
}

// deno-lint-ignore no-explicit-any
type Db = any

// ── 1. Session reminders ────────────────────────────────────────────────────────────────
async function sessionReminders(db: Db, now: Date) {
  const out = { sessions: 0, emails: 0, failed: 0 }
  const from = new Date(now.getTime() + SESSION_MIN_H * HOUR).toISOString()
  const to   = new Date(now.getTime() + SESSION_WINDOW_H * HOUR).toISOString()
  const { data: rows, error } = await db.from('cohort_sessions')
    .select('id, cohort_id, title, starts_at, duration_minutes, teams_url, will_record, last_sent_at, reminder_for_start, status')
    .eq('status', 'scheduled').not('last_sent_at', 'is', null)
    .gt('starts_at', from).lte('starts_at', to)
  if (error) throw new Error('sessions: ' + error.message)

  for (const s of rows || []) {
    const start = new Date(s.starts_at)
    if (s.reminder_for_start && new Date(s.reminder_for_start).getTime() === start.getTime()) continue
    // The invite went out within the last day: it already serves as the reminder.
    if (new Date(s.last_sent_at).getTime() > start.getTime() - 24 * HOUR) {
      await db.from('cohort_sessions').update({ reminder_for_start: s.starts_at }).eq('id', s.id)
      continue
    }
    const { data: cohort } = await db.from('cohorts').select('name, archived_at').eq('id', s.cohort_id).maybeSingle()
    if (!cohort || cohort.archived_at) continue
    const { data: mem } = await db.from('cohort_memberships').select('profile_id').eq('cohort_id', s.cohort_id)
    const ids = [...new Set((mem || []).map((m: { profile_id: string }) => m.profile_id))]
    if (!ids.length) continue
    const { data: people } = await db.from('profiles').select('id, full_name, email, suspended, deactivated_at').in('id', ids)
    const recipients = activeUnique(people || [])

    const a = local(start), b = local(new Date(start.getTime() + s.duration_minutes * 60000))
    const subject = `Reminder: ${s.title} · ${a.day}, ${a.time} (${DISPLAY_TZ_LABEL})`
    let sent = 0
    for (let i = 0; i < recipients.length; i++) {
      const p = recipients[i]
      const name = firstName(p.full_name)
      const intro = `A reminder that your Strategy2Results® live session for <strong style="color:#ffffff;">${esc(cohort.name)}</strong> is coming up.`
      const html = shell('Your session is coming up', `Hi ${esc(name)},`, [intro],
        [['Session', esc(s.title)], ['Date', a.day], ['Time', `${a.time}–${b.time} (${DISPLAY_TZ_LABEL})`], ['Where', 'Microsoft Teams']],
        { label: 'Join session', url: s.teams_url },
        `The Join session button is also on your <a href="${PORTAL_URL}" style="color:#2a7a7a;">S2R® Portal</a> home page.` +
          (s.will_record ? ' This session will be recorded.' : ''))
      const text = [
        `Hi ${name},`,
        `A reminder that your Strategy2Results® live session for ${cohort.name} is coming up.`,
        `Session: ${s.title}\nDate: ${a.day}\nTime: ${a.time}–${b.time} (${DISPLAY_TZ_LABEL})\nWhere: Microsoft Teams`,
        `Join session: ${s.teams_url}`,
        `The Join session button is also on your S2R® Portal home page: ${PORTAL_URL}` + (s.will_record ? '\nThis session will be recorded.' : ''),
        '© 2026 IBSLeadership · Strategy2Results® · S2R® Portal',
      ].join('\n\n')
      const r = await sendOne({ from: FROM_ADDRESS, to: p.email, subject, html, text })
      if (r.ok) sent++; else { out.failed++; console.error('Session reminder failed for', p.email, r.error) }
      if (i < recipients.length - 1) await sleep(SEND_GAP_MS)
    }
    if (sent > 0 || !recipients.length) {
      await db.from('cohort_sessions').update({ reminder_for_start: s.starts_at }).eq('id', s.id)
    }
    out.sessions++; out.emails += sent
  }
  return out
}

// ── 2. Blueprint deadline reminders ───────────────────────────────────────────────────────
async function blueprintReminders(db: Db, now: Date) {
  const out = { cohorts: 0, emails: 0, failed: 0 }
  const to = new Date(now.getTime() + BLUEPRINT_DAYS * 24 * HOUR).toISOString()
  const { data: briefs, error } = await db.from('capstone_brief')
    .select('cohort_id, submission_due, reminder_for_due')
    .not('submission_due', 'is', null)
    .gt('submission_due', now.toISOString()).lte('submission_due', to)
  if (error) throw new Error('briefs: ' + error.message)

  for (const b of briefs || []) {
    const due = new Date(b.submission_due)
    if (b.reminder_for_due && new Date(b.reminder_for_due).getTime() === due.getTime()) continue
    const { data: cohort } = await db.from('cohorts').select('name, archived_at').eq('id', b.cohort_id).maybeSingle()
    if (!cohort || cohort.archived_at) continue
    const { data: teams } = await db.from('capstone_team').select('id, team_name').eq('cohort_id', b.cohort_id)
    const d = local(due)
    let sent = 0, reached = 0
    for (const t of teams || []) {
      const { data: mem } = await db.from('capstone_individual').select('profile_id').eq('team_id', t.id)
      const ids = [...new Set((mem || []).map((m: { profile_id: string }) => m.profile_id))]
      if (!ids.length) continue
      const { data: secs } = await db.from('capstone_blueprint_section').select('status').eq('team_id', t.id)
      const agreed = (secs || []).filter((x: { status: string }) => x.status === 'agreed').length
      const { data: people } = await db.from('profiles').select('id, full_name, email, suspended, deactivated_at').in('id', ids)
      const recipients = activeUnique(people || [])
      reached += recipients.length
      const subject = `Capstone S2R Blueprint due ${d.day}, ${d.time} (${DISPLAY_TZ_LABEL})`
      for (let i = 0; i < recipients.length; i++) {
        const p = recipients[i]
        const name = firstName(p.full_name)
        const paras = [
          `Your team’s Capstone S2R Blueprint is due on ${d.day} at ${d.time} (${DISPLAY_TZ_LABEL}). After that time the Blueprint becomes read-only.`,
          `Each Blueprint section is completed in Section 5 of its unit and comes into the Blueprint once every member of your team has agreed it.`,
        ]
        const html = shell('Your Capstone S2R Blueprint deadline', `Hi ${esc(name)},`, paras,
          [['Team', esc(t.team_name)], ['Cohort', esc(cohort.name)], ['Sections agreed', `${agreed} of 12`]],
          { label: 'Open the Capstone', url: `${PORTAL_URL}/capstone_P.html` },
          `The Capstone page on your <a href="${PORTAL_URL}" style="color:#2a7a7a;">S2R® Portal</a> shows which sections are agreed.`)
        const text = [
          `Hi ${name},`, ...paras,
          `Team: ${t.team_name}\nCohort: ${cohort.name}\nSections agreed: ${agreed} of 12`,
          `Open the Capstone: ${PORTAL_URL}/capstone_P.html`,
          '© 2026 IBSLeadership · Strategy2Results® · S2R® Portal',
        ].join('\n\n')
        const r = await sendOne({ from: FROM_ADDRESS, to: p.email, subject, html, text })
        if (r.ok) sent++; else { out.failed++; console.error('Blueprint reminder failed for', p.email, r.error) }
        await sleep(SEND_GAP_MS)
      }
    }
    // Stamp once at least one email went out (or there is nobody to send to), so a failed run tries again.
    if (sent > 0 || reached === 0) {
      await db.from('capstone_brief').update({ reminder_for_due: b.submission_due }).eq('cohort_id', b.cohort_id)
    }
    out.cohorts++; out.emails += sent
  }
  return out
}

// ── 3. Missed-session alert to the admin inbox ─────────────────────────────────────────────
async function missedSessionAlert(db: Db) {
  const { data: rows, error } = await db.from('session_checkins')
    .select('id, session_id, cohort_id, profile_id').eq('status', 'open').is('alert_emailed_at', null)
  if (error) throw new Error('check-ins: ' + error.message)
  if (!rows || !rows.length) return { alerted: 0 }

  const sessionIds = [...new Set(rows.map((r: { session_id: string }) => r.session_id))]
  const cohortIds  = [...new Set(rows.map((r: { cohort_id: string }) => r.cohort_id))]
  const profileIds = [...new Set(rows.map((r: { profile_id: string }) => r.profile_id))]
  const [{ data: ss }, { data: cs }, { data: ps }] = await Promise.all([
    db.from('cohort_sessions').select('id, title, starts_at').in('id', sessionIds),
    db.from('cohorts').select('id, name').in('id', cohortIds),
    db.from('profiles').select('id, full_name, email').in('id', profileIds),
  ])
  const S: Record<string, { title: string; starts_at: string }> = {}; (ss || []).forEach((x: { id: string; title: string; starts_at: string }) => S[x.id] = x)
  const C: Record<string, string> = {}; (cs || []).forEach((x: { id: string; name: string }) => C[x.id] = x.name)
  const P: Record<string, { full_name?: string; email?: string }> = {}; (ps || []).forEach((x: { id: string; full_name?: string; email?: string }) => P[x.id] = x)

  // Group: cohort → session → names
  const groups: Record<string, Record<string, string[]>> = {}
  for (const r of rows) {
    const g = (groups[r.cohort_id] ||= {})
    const who = P[r.profile_id]
    ;(g[r.session_id] ||= []).push((who && (who.full_name || who.email)) || 'Unknown participant')
  }
  const blocks: string[] = [], textBlocks: string[] = []
  for (const cid of Object.keys(groups)) {
    for (const sid of Object.keys(groups[cid])) {
      const s = S[sid]; const d = s ? local(new Date(s.starts_at)) : { day: '', time: '' }
      const names = groups[cid][sid].sort()
      blocks.push(`<p style="margin:18px 0 0;font-size:14px;color:#ffffff;line-height:1.6;"><strong>${esc(C[cid] || 'Cohort')}</strong> · ${esc(s ? s.title : 'Session')} · ${d.day}</p>` +
        `<p style="margin:4px 0 0;font-size:14px;color:rgba(255,255,255,0.75);line-height:1.7;">${names.map(esc).join('<br>')}</p>`)
      textBlocks.push(`${C[cid] || 'Cohort'} · ${s ? s.title : 'Session'} · ${d.day}\n${names.join('\n')}`)
    }
  }
  const n = rows.length
  const intro = `${n} participant${n === 1 ? ' was' : 's were'} marked absent from a live session. A check-in message is drafted for each one.`
  const html = shell('Missed sessions', 'Hello,', [intro, blocks.join('')], [],
    { label: 'Open the admin console', url: `${PORTAL_URL}/dashboard_A.html` },
    'Open the cohort in the admin console. Under Live sessions, each check-in can be read, edited and sent. Nothing goes to a participant until you press Send.')
  const text = ['Hello,', intro, textBlocks.join('\n\n'),
    `Open the admin console: ${PORTAL_URL}/dashboard_A.html`,
    'Open the cohort in the admin console. Under Live sessions, each check-in can be read, edited and sent. Nothing goes to a participant until you press Send.'].join('\n\n')
  const r = await sendOne({ from: FROM_ADDRESS, to: ADMIN_INBOX, subject: `Missed sessions: ${n} check-in${n === 1 ? '' : 's'} to send`, html, text })
  if (!r.ok) throw new Error('alert email: ' + r.error)
  const { error: uErr } = await db.from('session_checkins')
    .update({ alert_emailed_at: new Date().toISOString() }).in('id', rows.map((x: { id: string }) => x.id))
  if (uErr) console.error('Alert stamp error:', uErr.message)
  return { alerted: n }
}

Deno.serve(async (req) => {
  if (!CRON_SECRET || req.headers.get('x-cron-secret') !== CRON_SECRET) {
    return json({ ok: false, error: 'Not allowed.' }, 403)
  }
  const db = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY, { auth: { autoRefreshToken: false, persistSession: false } })
  const now = new Date()
  const result: Record<string, unknown> = { ok: true, ran_at: now.toISOString() }
  // Each part runs on its own, so one failure does not stop the others.
  for (const [key, fn] of [
    ['sessions', () => sessionReminders(db, now)],
    ['blueprint', () => blueprintReminders(db, now)],
    ['missed', () => missedSessionAlert(db)],
  ] as [string, () => Promise<unknown>][]) {
    try { result[key] = await fn() }
    catch (e) { result.ok = false; result[key] = { error: (e as Error).message }; console.error(key, (e as Error).message) }
  }
  return json(result, result.ok ? 200 : 500)
})
