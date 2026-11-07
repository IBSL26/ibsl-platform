// suggest-marks — a suggested mark for each skill (Unit 1) or key reflection (Units 2 to 12),
// worked out by Claude from the participant's answers against the marking descriptions.
// The facilitator still chooses the mark; this only shows a suggestion beside it.
//
// Called from the facilitator review (dashboard_F.html) with
//   { submission_id, scale: 'skill' | 'reflection', items: [{ id, question, keys: [...], evidenced, developing? }] }
// Only a facilitator, lead facilitator or admin of the submission's cohort may call it
// (checked through get_reflection_marks with the caller's own login).
// Suggestions are kept in public.mark_suggestions and reused until the answers change.
//
// Secrets: ANTHROPIC_API_KEY. SUPABASE_URL, SUPABASE_ANON_KEY and SUPABASE_SERVICE_ROLE_KEY are provided by Supabase.

import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const ANTHROPIC_API_KEY    = Deno.env.get('ANTHROPIC_API_KEY') || ''
const SUPABASE_URL         = Deno.env.get('SUPABASE_URL')!
const SUPABASE_ANON_KEY    = Deno.env.get('SUPABASE_ANON_KEY')!
const SUPABASE_SERVICE_KEY = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') || Deno.env.get('SB_SERVICE_ROLE_KEY')!
const MODEL = 'claude-sonnet-5-5'

const cors = {
  'Access-Control-Allow-Origin':  '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}
function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { ...cors, 'Content-Type': 'application/json' } })
}

type Item = { id: string; question?: string; keys: string[]; notevidenced?: string; evidenced?: string; developing?: string }

const SKILL_MARKS = ['not_evidenced', 'evidenced', 'developing_others']
const REF_MARKS   = ['full', 'part', 'none', 'blank']

async function sha(text: string) {
  const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text))
  return Array.from(new Uint8Array(b)).map((x) => x.toString(16).padStart(2, '0')).join('')
}

function answerOf(v: unknown): string {
  if (typeof v === 'string') return v.trim()
  if (v === null || v === undefined) return ''
  return JSON.stringify(v)
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors })
  try {
    const auth = req.headers.get('Authorization') || ''
    const body = await req.json().catch(() => ({}))
    const submissionId = String(body.submission_id || '')
    const scale = body.scale === 'skill' ? 'skill' : 'reflection'
    const items: Item[] = Array.isArray(body.items) ? body.items.slice(0, 16) : []
    if (!submissionId || !items.length) return json({ ok: false, error: 'bad_input' }, 400)

    // Access: the caller's own login must be allowed to mark this submission.
    const userClient = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, { global: { headers: { Authorization: auth } } })
    const access = await userClient.rpc('get_reflection_marks', { p_submission_id: submissionId })
    if (access.error) return json({ ok: false, error: 'access_denied' }, 403)

    // The submission, read with the caller's own login (the same call the review page makes).
    const bundle = await userClient.rpc('get_submission_for_review', { p_submission_id: submissionId })
    if (bundle.error) console.error('[suggest-marks] get_submission_for_review:', bundle.error.message)
    const payload = bundle.data && bundle.data.submission && bundle.data.submission.payload
    if (!payload) return json({ ok: false, error: 'not_found' }, 404)
    const responses = payload.responses || {}
    const admin = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY, { auth: { autoRefreshToken: false, persistSession: false } })

    const blocks = items.map((it) => {
      const answers = (it.keys || []).map((k) => ({ key: k, text: answerOf(responses[k]) }))
      return { ...it, answers }
    })
    const hash = await sha(scale + JSON.stringify(blocks))

    const cached = await admin.from('mark_suggestions').select('answers_hash, result').eq('submission_id', submissionId).eq('scale', scale).maybeSingle()
    if (cached.error) console.error('[suggest-marks] cache read:', cached.error.message)
    if (cached.data && cached.data.answers_hash === hash) return json({ ok: true, suggestions: cached.data.result, cached: true })

    if (!ANTHROPIC_API_KEY) return json({ ok: false, error: 'no_key' }, 503)

    const rules = scale === 'skill'
      ? 'For each skill choose exactly one mark:\n' +
        '- "not_evidenced": the answers match the Not evidenced description, do not show what the Evidenced description says, or are blank.\n' +
        '- "evidenced": the answers show what the Evidenced description says.\n' +
        '- "developing_others": the answers show the Evidenced description and also the Developing others description.\n'
      : 'For each reflection choose exactly one mark:\n' +
        '- "full" (Fully evidenced): the answer meets the Fully evidenced description.\n' +
        '- "part" (Partly evidenced): it answers part of the question, or stays general without reference to the participant\'s own organisation, team or work.\n' +
        '- "none" (Not evidenced): it is written but does not address the question.\n' +
        '- "blank" (Not answered): it is empty.\n'

    const material = blocks.map((b) =>
      `### Item ${b.id}\n` +
      (b.question ? `Skill or question: ${b.question}\n` : '') +
      (b.notevidenced ? `Not evidenced description: ${b.notevidenced}\n` : '') +
      (b.evidenced ? `${scale === 'skill' ? 'Evidenced' : 'Fully evidenced'} description: ${b.evidenced}\n` : '') +
      (b.developing ? `Developing others description: ${b.developing}\n` : '') +
      'Participant answers:\n' +
      b.answers.map((a) => `- [${a.key}] ${a.text || '(not answered)'}`).join('\n')
    ).join('\n\n')

    const prompt =
      'You are assisting a facilitator who marks reflections in the CESI programme (IBSL, Strategy2Results). ' +
      'Read the participant\'s answers and suggest a mark for each item, judged only against that item\'s own question and descriptions. ' +
      'The facilitator decides the final mark.\n\n' + rules +
      '\nGive a reason of no more than 30 words for each, in British English, naming what the answers do or do not show. ' +
      'Address the facilitator, and refer to the participant as "the participant".\n' +
      'Reply with JSON only, in this form: {"items":[{"id":"<item id>","mark":"<mark>","reason":"<reason>"}]}\n\n' + material

    const r = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'x-api-key': ANTHROPIC_API_KEY, 'anthropic-version': '2023-06-01', 'content-type': 'application/json' },
      body: JSON.stringify({ model: MODEL, max_tokens: 1500, messages: [{ role: 'user', content: prompt }] }),
    })
    if (!r.ok) { const d = (await r.text()).slice(0, 300); console.error('[suggest-marks] model:', r.status, d); return json({ ok: false, error: 'model_error', status: r.status, detail: d }, 502) }
    const out = await r.json()
    const text = (out.content || []).map((c: { text?: string }) => c.text || '').join('')
    const m = text.match(/\{[\s\S]*\}/)
    if (!m) return json({ ok: false, error: 'bad_reply' }, 502)
    const parsed = JSON.parse(m[0])
    const allowed = scale === 'skill' ? SKILL_MARKS : REF_MARKS
    const result: Record<string, { mark: string; reason: string }> = {}
    for (const x of parsed.items || []) {
      const id = String(x.id)
      if (!items.some((it) => String(it.id) === id)) continue
      if (!allowed.includes(String(x.mark))) continue
      result[id] = { mark: String(x.mark), reason: String(x.reason || '').slice(0, 300) }
    }

    const saved = await admin.from('mark_suggestions').upsert({ submission_id: submissionId, scale, answers_hash: hash, result, created_at: new Date().toISOString() })
    if (saved.error) console.error('[suggest-marks] cache write:', saved.error.message)
    return json({ ok: true, suggestions: result, cached: false })
  } catch (e) {
    console.error('[suggest-marks] error:', String(e))
    return json({ ok: false, error: 'server_error', detail: String(e).slice(0, 300) }, 500)
  }
})
