// send-session-email — emails a cohort about a live session.
//
// Called from the admin dashboard (Cohort detail → Live sessions) with
//   { session_id: "<uuid>", kind: "invite" | "update" | "cancel" | "recording" }
// Only a signed-in admin may call it. One email goes to each active member of the
// cohort (participants and facilitators). invite / update carry a calendar file.
// On success the session is stamped as sent, which is what makes it show on the
// participant portal and the facilitator dashboard.
//
// Secrets used (same as send-invitation-email): RESEND_API_KEY, SB_SERVICE_ROLE_KEY.
// SUPABASE_URL and SUPABASE_ANON_KEY are provided by Supabase.

import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const RESEND_API_KEY       = Deno.env.get('RESEND_API_KEY')!
const SUPABASE_URL         = Deno.env.get('SUPABASE_URL')!
const SUPABASE_ANON_KEY    = Deno.env.get('SUPABASE_ANON_KEY')!
const SUPABASE_SERVICE_KEY = Deno.env.get('SB_SERVICE_ROLE_KEY')!
const PORTAL_URL           = 'https://ibslportal.netlify.app'
const FROM_ADDRESS         = 'IBSLeadership S2R Portal <noreply@mail.ibsleadership.com>'

// Time zone used for the date and time written in the email text.
// The calendar file converts to each person's own zone.
const DISPLAY_OFFSET_MIN = 120       // minutes ahead of GMT
const DISPLAY_TZ_LABEL   = 'GMT+2'

const SEND_GAP_MS = 600              // pause between emails (Resend rate limit)

type Kind = 'invite' | 'update' | 'cancel' | 'recording'

const cors = {
  'Access-Control-Allow-Origin':  '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}
function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status, headers: { ...cors, 'Content-Type': 'application/json' },
  })
}

const MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
const DOW = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
const pad = (n: number) => (n < 10 ? '0' : '') + n
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms))

function esc(s: unknown): string {
  return String(s ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;')
}
// Date parts in the display zone (shift, then read as UTC).
function local(d: Date) {
  const s = new Date(d.getTime() + DISPLAY_OFFSET_MIN * 60000)
  return {
    day:  `${DOW[s.getUTCDay()]} ${s.getUTCDate()} ${MON[s.getUTCMonth()]} ${s.getUTCFullYear()}`,
    time: `${pad(s.getUTCHours())}:${pad(s.getUTCMinutes())}`,
  }
}
function icsStamp(d: Date) {
  return `${d.getUTCFullYear()}${pad(d.getUTCMonth() + 1)}${pad(d.getUTCDate())}T` +
         `${pad(d.getUTCHours())}${pad(d.getUTCMinutes())}${pad(d.getUTCSeconds())}Z`
}
function icsText(s: string) {
  return s.replace(/\\/g, '\\\\').replace(/;/g, '\\;').replace(/,/g, '\\,').replace(/\r?\n/g, '\\n')
}
// Calendar lines may be at most 75 bytes; longer lines continue on the next line after a space.
function icsFold(line: string) {
  const enc = new TextEncoder()
  const out: string[] = []
  let cur = '', bytes = 0
  for (const ch of line) {
    const n = enc.encode(ch).length
    if (bytes + n > 73) { out.push(cur); cur = ' '; bytes = 1 }
    cur += ch; bytes += n
  }
  out.push(cur)
  return out.join('\r\n')
}
function base64(s: string) {
  const bytes = new TextEncoder().encode(s)
  let bin = ''
  for (const b of bytes) bin += String.fromCharCode(b)
  return btoa(bin)
}

interface SessionRow {
  id: string; cohort_id: string; title: string; unit_no: number | null
  starts_at: string; duration_minutes: number; teams_url: string
  will_record: boolean; recording_url: string | null; notes: string | null
  status: string; ical_sequence: number; changed_since_sent: boolean
  last_sent_at: string | null; recording_sent_at: string | null
}

function buildIcs(s: SessionRow, cohortName: string) {
  const start = new Date(s.starts_at)
  const end   = new Date(start.getTime() + s.duration_minutes * 60000)
  const desc  = [
    `Strategy2Results® live session for ${cohortName}.`,
    `Join: ${s.teams_url}`,
    s.will_record ? 'This session will be recorded.' : '',
    s.notes || '',
  ].filter(Boolean).join('\n\n')
  const lines = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//IBSLeadership//S2R Portal//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    `UID:${s.id}@ibslportal.netlify.app`,
    `SEQUENCE:${s.ical_sequence}`,
    `DTSTAMP:${icsStamp(new Date())}`,
    `DTSTART:${icsStamp(start)}`,
    `DTEND:${icsStamp(end)}`,
    `SUMMARY:${icsText(s.title)}`,
    `DESCRIPTION:${icsText(desc)}`,
    'LOCATION:Microsoft Teams',
    `URL:${s.teams_url}`,
    'STATUS:CONFIRMED',
    'BEGIN:VALARM',
    'TRIGGER:-PT15M',
    'ACTION:DISPLAY',
    'DESCRIPTION:Live session starts in 15 minutes',
    'END:VALARM',
    'END:VEVENT',
    'END:VCALENDAR',
  ]
  return lines.map(icsFold).join('\r\n') + '\r\n'
}

function buildEmail(kind: Kind, s: SessionRow, cohortName: string, firstName: string) {
  const start = new Date(s.starts_at)
  const end   = new Date(start.getTime() + s.duration_minutes * 60000)
  const a = local(start), b = local(end)
  const timeLine = `${a.time}–${b.time} (${DISPLAY_TZ_LABEL})`
  const cohort = `<strong style="color:#ffffff;">${esc(cohortName)}</strong>`

  let subject = '', heading = '', intro = '', introText = ''
  let buttonLabel = '', buttonUrl = '', footnote = '', footnoteText = ''

  if (kind === 'invite') {
    subject   = `Live session: ${s.title} · ${a.day}, ${a.time} (${DISPLAY_TZ_LABEL})`
    heading   = 'Your live session'
    intro     = `Your Strategy2Results® live session for ${cohort} is confirmed.`
    introText = `Your Strategy2Results® live session for ${cohortName} is confirmed.`
  } else if (kind === 'update') {
    subject   = `Updated: ${s.title} · ${a.day}, ${a.time} (${DISPLAY_TZ_LABEL})`
    heading   = 'Session details updated'
    intro     = `The details of your Strategy2Results® live session for ${cohort} have changed. The current details are below.`
    introText = `The details of your Strategy2Results® live session for ${cohortName} have changed. The current details are below.`
  } else if (kind === 'cancel') {
    subject   = `Cancelled: ${s.title} · ${a.day}`
    heading   = 'Session cancelled'
    intro     = `This Strategy2Results® live session for ${cohort} is cancelled. Please remove it from your calendar.`
    introText = `This Strategy2Results® live session for ${cohortName} is cancelled. Please remove it from your calendar.`
  } else {
    subject   = `Recording available: ${s.title}`
    heading   = 'Session recording'
    intro     = `The recording of this Strategy2Results® live session for ${cohort} is ready to watch.`
    introText = `The recording of this Strategy2Results® live session for ${cohortName} is ready to watch.`
  }

  if (kind === 'invite' || kind === 'update') {
    buttonLabel  = 'Join session'
    buttonUrl    = s.teams_url
    footnote     = `The attached calendar file adds this session to your calendar in your own time zone. The Join session button is also on your <a href="${PORTAL_URL}" style="color:#2a7a7a;">S2R® Portal</a> home page.`
    footnoteText = `The attached calendar file adds this session to your calendar in your own time zone. The Join session button is also on your S2R® Portal home page: ${PORTAL_URL}`
  } else if (kind === 'recording') {
    buttonLabel  = 'Watch recording'
    buttonUrl    = s.recording_url || ''
    footnote     = `The recording is for this cohort and its facilitators. Please keep the link within the group. It is also on your <a href="${PORTAL_URL}" style="color:#2a7a7a;">S2R® Portal</a> home page under Live sessions.`
    footnoteText = `The recording is for this cohort and its facilitators. Please keep the link within the group. It is also on your S2R® Portal home page under Live sessions: ${PORTAL_URL}`
  }

  const row = (label: string, value: string) =>
    `<tr><td style="padding:6px 16px 6px 0;font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,0.45);vertical-align:top;white-space:nowrap;">${label}</td>` +
    `<td style="padding:6px 0;font-size:14px;color:#ffffff;line-height:1.5;">${value}</td></tr>`

  const details =
    row('Session', esc(s.title)) +
    row('Date', a.day) +
    (kind === 'recording' ? '' : row('Time', timeLine)) +
    (kind === 'invite' || kind === 'update' ? row('Where', 'Microsoft Teams') : '')

  const recorded = (kind === 'invite' || kind === 'update') && s.will_record
    ? `<p style="margin:18px 0 0;font-size:13px;color:rgba(255,255,255,0.75);line-height:1.7;"><strong style="color:#ffffff;">This session will be recorded.</strong> The recording is shared with your cohort and facilitators, for anyone who misses the session and to help us improve delivery.</p>`
    : ''
  const notes = (kind === 'invite' || kind === 'update') && s.notes
    ? `<p style="margin:18px 0 0;font-size:13px;color:rgba(255,255,255,0.75);line-height:1.7;white-space:pre-wrap;">${esc(s.notes)}</p>`
    : ''
  const button = buttonUrl
    ? `<tr><td style="padding:28px 44px 8px;">
  <a href="${esc(buttonUrl)}" style="display:inline-block;background:#2a7a7a;color:#ffffff;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;text-decoration:none;padding:14px 28px;border-radius:3px;">${buttonLabel}</a>
</td></tr>`
    : ''
  const foot = buttonUrl
    ? `<tr><td style="padding:0 44px 32px;">
  <p style="margin:20px 0 0;padding-top:20px;border-top:1px solid rgba(201,168,76,0.15);font-size:11px;color:rgba(255,255,255,0.45);line-height:1.6;">${footnote}</p>
  <p style="margin:8px 0 0;font-size:11px;color:rgba(255,255,255,0.35);line-height:1.6;">
    If the button does not work, copy this link into your browser:<br>
    <a href="${esc(buttonUrl)}" style="color:#2a7a7a;word-break:break-all;">${esc(buttonUrl)}</a>
  </p>
</td></tr>`
    : `<tr><td style="padding:0 44px 32px;"></td></tr>`

  const html = `<!DOCTYPE html><html><head><meta charset="UTF-8"></head>
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
  <p style="margin:0;font-size:14px;color:rgba(255,255,255,0.75);line-height:1.7;">Hi ${esc(firstName)},</p>
  <p style="margin:16px 0 0;font-size:14px;color:rgba(255,255,255,0.75);line-height:1.7;">${intro}</p>
  <table cellpadding="0" cellspacing="0" style="margin:20px 0 0;">${details}</table>
  ${recorded}${notes}
</td></tr>
${button}
${foot}
<tr><td style="padding:20px 44px;background:rgba(0,0,0,0.2);">
  <p style="margin:0;font-size:10px;color:rgba(255,255,255,0.25);letter-spacing:1px;">© 2026 IBSLeadership · Strategy2Results® · S2R® Portal</p>
</td></tr>
</table></td></tr></table>
</body></html>`

  const text = [
    `Hi ${firstName},`,
    introText,
    `Session: ${s.title}\nDate: ${a.day}` + (kind === 'recording' ? '' : `\nTime: ${timeLine}`),
    (kind === 'invite' || kind === 'update') && s.will_record ? 'This session will be recorded. The recording is shared with your cohort and facilitators, for anyone who misses the session and to help us improve delivery.' : '',
    (kind === 'invite' || kind === 'update') && s.notes ? s.notes : '',
    buttonUrl ? `${buttonLabel}: ${buttonUrl}` : '',
    footnoteText,
    '© 2026 IBSLeadership · Strategy2Results® · S2R® Portal',
  ].filter(Boolean).join('\n\n')

  return { subject, html, text }
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

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors })
  try {
    // The caller must be a signed-in admin.
    const authHeader = req.headers.get('Authorization')
    if (!authHeader) return json({ ok: false, error: 'Please sign in again.' }, 401)

    const callerClient = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
      global: { headers: { Authorization: authHeader } },
    })
    const { data: { user }, error: userErr } = await callerClient.auth.getUser()
    if (userErr || !user) return json({ ok: false, error: 'Please sign in again.' }, 401)

    const { data: profile, error: profileErr } = await callerClient
      .from('profiles').select('role').eq('id', user.id).single()
    if (profileErr || !profile) return json({ ok: false, error: 'Profile not found.' }, 403)
    if (profile.role !== 'admin') return json({ ok: false, error: 'Only an admin can send session emails.' }, 403)

    const { session_id, kind } = await req.json() as { session_id?: string; kind?: Kind }
    if (!session_id) return json({ ok: false, error: 'No session was given.' }, 400)
    if (!kind || !['invite', 'update', 'cancel', 'recording'].includes(kind)) {
      return json({ ok: false, error: 'Unknown email type.' }, 400)
    }

    const admin = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY, {
      auth: { autoRefreshToken: false, persistSession: false },
    })

    const { data: session, error: sErr } = await admin
      .from('cohort_sessions').select('*').eq('id', session_id).maybeSingle()
    if (sErr) return json({ ok: false, error: sErr.message }, 500)
    if (!session) return json({ ok: false, error: 'Session not found.' }, 404)
    const s = session as SessionRow

    // The session must be in the right state for this email.
    if ((kind === 'invite' || kind === 'update') && s.status !== 'scheduled') {
      return json({ ok: false, error: 'This session is cancelled.' }, 400)
    }
    if (kind === 'update' && !s.last_sent_at) {
      return json({ ok: false, error: 'This session has not been sent to the cohort yet.' }, 400)
    }
    if (kind === 'cancel' && (s.status !== 'cancelled' || !s.last_sent_at)) {
      return json({ ok: false, error: 'Only a cancelled session that was sent to the cohort can have a cancellation emailed.' }, 400)
    }
    if (kind === 'recording' && (!s.recording_url || s.status !== 'scheduled')) {
      return json({ ok: false, error: 'Add the recording link first.' }, 400)
    }

    const { data: cohort, error: cErr } = await admin
      .from('cohorts').select('id, name, archived_at').eq('id', s.cohort_id).maybeSingle()
    if (cErr) return json({ ok: false, error: cErr.message }, 500)
    if (!cohort) return json({ ok: false, error: 'Cohort not found.' }, 404)
    if (cohort.archived_at) return json({ ok: false, error: 'This cohort is archived.' }, 400)

    // Recipients: every active member of the cohort (participants and facilitators).
    const { data: members, error: mErr } = await admin
      .from('cohort_memberships').select('profile_id').eq('cohort_id', s.cohort_id)
    if (mErr) return json({ ok: false, error: mErr.message }, 500)
    const ids = [...new Set((members || []).map((m: { profile_id: string }) => m.profile_id))]
    if (!ids.length) return json({ ok: false, error: 'This cohort has no members yet.' }, 400)

    const { data: people, error: pErr } = await admin
      .from('profiles').select('id, full_name, email, suspended, deactivated_at').in('id', ids)
    if (pErr) return json({ ok: false, error: pErr.message }, 500)

    const seen = new Set<string>()
    const recipients = (people || []).filter((p: { email?: string; suspended?: boolean; deactivated_at?: string | null }) => {
      const e = (p.email || '').trim().toLowerCase()
      if (!e || p.suspended || p.deactivated_at || seen.has(e)) return false
      seen.add(e)
      return true
    })
    if (!recipients.length) return json({ ok: false, error: 'No active members with an email address in this cohort.' }, 400)

    const attachIcs = kind === 'invite' || kind === 'update'
    const ics = attachIcs ? base64(buildIcs(s, cohort.name)) : ''

    let sent = 0
    const failed: string[] = []
    let firstError = ''
    for (let i = 0; i < recipients.length; i++) {
      const p = recipients[i] as { full_name?: string; email: string }
      const firstName = (p.full_name || '').trim().split(' ')[0] || 'there'
      const mail = buildEmail(kind, s, cohort.name, firstName)
      const payload: Record<string, unknown> = {
        from: FROM_ADDRESS,
        to: p.email,
        subject: mail.subject,
        html: mail.html,
        text: mail.text,
      }
      if (attachIcs) {
        payload.attachments = [{ filename: 'S2R-live-session.ics', content: ics, content_type: 'text/calendar; charset=utf-8; method=PUBLISH' }]
      }
      const r = await sendOne(payload)
      if (r.ok) sent++
      else { failed.push(p.email); if (!firstError) firstError = r.error; console.error('Resend error for', p.email, r.error) }
      if (i < recipients.length - 1) await sleep(SEND_GAP_MS)
    }

    if (sent === 0) {
      return json({ ok: false, error: firstError || 'No email could be sent.' }, 502)
    }

    // Stamp the session. This is what publishes it to the cohort's portal.
    const now = new Date().toISOString()
    const stamp: Record<string, unknown> =
      kind === 'recording' ? { recording_sent_at: now, last_sent_at: s.last_sent_at || now }
      : kind === 'cancel'  ? { changed_since_sent: false }
      :                      { last_sent_at: now, changed_since_sent: false }
    const { error: uErr } = await admin.from('cohort_sessions').update(stamp).eq('id', s.id)
    if (uErr) console.error('Stamp error:', uErr.message)

    // Activity log, under the admin's own name.
    const { error: lErr } = await callerClient.rpc('log_activity', {
      p_event_type: 'session_sent',
      p_event_detail: { session_id: s.id, title: s.title, kind, sent, failed: failed.length },
      p_cohort_id: s.cohort_id,
    })
    if (lErr) console.error('log_activity error:', lErr.message)

    return json({ ok: true, sent, failed, stamped: !uErr })
  } catch (err) {
    console.error('Edge function error:', (err as Error).message)
    return json({ ok: false, error: (err as Error).message || 'internal_error' }, 500)
  }
})
