/**
 * S2R Save Helper — Stage C.1
 *
 * Shared JavaScript library for all S2R® Portal lens pages.
 * Provides save/load/submit functions that persist participant responses
 * to the central Supabase filing cabinet instead of browser localStorage.
 *
 * Usage in lens HTML files:
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 *   <script src="/s2r-save.js"></script>
 *   <script>
 *     // On save:
 *     await S2R.save('u1_foundations', 'r_m1_intent', textareaValue);
 *     // On page load:
 *     const responses = await S2R.loadAll('u1_foundations');
 *     // On Send to Facilitator:
 *     await S2R.submit('u1_foundations');
 *   </script>
 *
 * © 2026 IBSLeadership. All rights reserved.
 * S2R® and Strategy2Results® are registered trademarks.
 */

(function() {
  'use strict';

  const SUPABASE_URL = 'https://tayrxqbrttlrdowrzobm.supabase.co';
  const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRheXJ4cWJydHRscmRvd3J6b2JtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY3ODAyOTUsImV4cCI6MjA5MjM1NjI5NX0.8eaQauK1GPI3OXyHLdRAfbSwLfaYLB3_amHt6FhZxG0';

  // Initialise Supabase client
  if (typeof supabase === 'undefined') {
    console.error('[S2R] Supabase library not loaded. Include the supabase-js CDN script BEFORE s2r-save.js.');
    return;
  }

  const client = supabase.createClient(SUPABASE_URL, SUPABASE_KEY, {
    auth: { autoRefreshToken: true, persistSession: true, detectSessionInUrl: false }
  });

  // Cache user context (profile_id + cohort_id) so we don't query every save
  let _ctx = null;
  let _ctxPromise = null;

  async function getContext() {
    if (_ctx) return _ctx;
    if (_ctxPromise) return _ctxPromise;

    _ctxPromise = (async () => {
      try {
        const { data: { session }, error: sessErr } = await client.auth.getSession();
        if (sessErr || !session) {
          console.warn('[S2R] No active session. Responses will not be saved.');
          return null;
        }
        const userId = session.user.id;

        // Get current cohort for this user (most recently joined active cohort)
        const { data: memberships, error: memErr } = await client
          .from('cohort_memberships')
          .select('cohort_id, role_in_cohort, joined_at, cohorts(id, name, status)')
          .eq('profile_id', userId)
          .order('joined_at', { ascending: false });

        if (memErr) {
          console.error('[S2R] Failed to look up cohort membership:', memErr);
          return null;
        }

        if (!memberships || memberships.length === 0) {
          console.warn('[S2R] User has no cohort membership. Responses will not be saved.');
          return null;
        }

        // Prefer an active cohort; fall back to most recent
        const active = memberships.find(m => m.cohorts && m.cohorts.status === 'active');
        const chosen = active || memberships[0];

        _ctx = {
          profileId: userId,
          cohortId: chosen.cohort_id,
          cohortName: chosen.cohorts ? chosen.cohorts.name : '(unknown)',
          role: chosen.role_in_cohort
        };
        console.log('[S2R] Ready:', _ctx.cohortName, '/', _ctx.role);
        return _ctx;
      } catch (err) {
        console.error('[S2R] Context init error:', err);
        return null;
      }
    })();

    return _ctxPromise;
  }

  /**
   * Save a single response (upsert).
   * @param {string} lensId - e.g. 'u1_foundations'
   * @param {string} responseKey - e.g. 'r_m1_intent'
   * @param {any} value - will be stored as JSONB
   * @returns {Promise<boolean>} true on success, false on failure
   */
  async function save(lensId, responseKey, value) {
    const ctx = await getContext();
    if (!ctx) return false;

    try {
      const { error } = await client
        .from('lens_responses')
        .upsert({
          profile_id: ctx.profileId,
          cohort_id: ctx.cohortId,
          lens_id: lensId,
          response_key: responseKey,
          value: value,
          updated_at: new Date().toISOString()
        }, {
          onConflict: 'profile_id,lens_id,response_key'
        });

      if (error) {
        console.error('[S2R] Save error for', responseKey, ':', error);
        return false;
      }
      return true;
    } catch (err) {
      console.error('[S2R] Save exception for', responseKey, ':', err);
      return false;
    }
  }

  /**
   * Load all responses for a lens.
   * @param {string} lensId
   * @returns {Promise<Object>} { responseKey: value, ... } or {} on failure
   */
  async function loadAll(lensId) {
    const ctx = await getContext();
    if (!ctx) return {};

    try {
      const { data, error } = await client
        .from('lens_responses')
        .select('response_key, value')
        .eq('profile_id', ctx.profileId)
        .eq('lens_id', lensId);

      if (error) {
        console.error('[S2R] Load error:', error);
        return {};
      }

      const out = {};
      (data || []).forEach(row => {
        out[row.response_key] = row.value;
      });
      return out;
    } catch (err) {
      console.error('[S2R] Load exception:', err);
      return {};
    }
  }

  /**
   * Submit a snapshot of all responses for a lens to the facilitator inbox.
   * @param {string} lensId
   * @returns {Promise<{ok: boolean, message: string}>}
   */
  async function submit(lensId) {
    const ctx = await getContext();
    if (!ctx) return { ok: false, message: 'Not signed in or no cohort assigned.' };

    try {
      // Fetch all current responses for this lens
      const responses = await loadAll(lensId);

      if (Object.keys(responses).length === 0) {
        return { ok: false, message: 'No responses to submit. Please complete at least one reflection first.' };
      }

      // Insert submission snapshot
      const { error } = await client
        .from('submissions')
        .insert({
          profile_id: ctx.profileId,
          cohort_id: ctx.cohortId,
          lens_id: lensId,
          payload: {
            responses: responses,
            submitted_at_client: new Date().toISOString()
          },
          review_status: 'pending'
        });

      if (error) {
        console.error('[S2R] Submit error:', error);
        return { ok: false, message: 'Submission failed. Please try again or contact info@ibsleadership.com.' };
      }

      return { ok: true, message: 'Submission received. Your facilitator will review it and respond.' };
    } catch (err) {
      console.error('[S2R] Submit exception:', err);
      return { ok: false, message: 'Something went wrong. Please try again.' };
    }
  }

  /**
   * Check if the helper is ready (user is signed in + has a cohort).
   * @returns {Promise<boolean>}
   */
  async function isReady() {
    const ctx = await getContext();
    return !!ctx;
  }

  /**
   * Get current context (read-only, useful for debugging).
   * @returns {Promise<Object|null>}
   */
  async function context() {
    return await getContext();
  }

  // Expose on window.S2R
  window.S2R = {
    save: save,
    loadAll: loadAll,
    submit: submit,
    isReady: isReady,
    context: context,
    // Also expose the client in case lens pages need advanced access
    _client: client
  };

  console.log('[S2R] Helper loaded. Waiting for first call to initialise context.');
})();
