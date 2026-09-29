-- Login fix 2 (29 Sept 2026): reuse a pending confirmation token for 24 hours
-- so an email that has already arrived keeps working when a later email is blocked.
-- Same name, arguments and return type as the current function: grants are kept.

CREATE OR REPLACE FUNCTION public.request_device_confirmation(p_fingerprint text, p_device_label text)
 RETURNS text
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'public', 'extensions'
AS $function$
DECLARE
  v_user_id uuid;
  v_token text;
BEGIN
  v_user_id := auth.uid();
  IF v_user_id IS NULL THEN
    RAISE EXCEPTION 'Not authenticated';
  END IF;

  -- Reuse a pending token issued in the last 24 hours
  SELECT confirmation_token INTO v_token
  FROM public.trusted_devices
  WHERE user_id = v_user_id
    AND fingerprint = p_fingerprint
    AND status = 'pending_confirmation'
    AND confirmation_token IS NOT NULL
    AND created_at > now() - interval '24 hours';

  IF v_token IS NOT NULL THEN
    UPDATE public.trusted_devices
    SET device_label = p_device_label
    WHERE user_id = v_user_id AND fingerprint = p_fingerprint;
    RETURN v_token;
  END IF;

  -- Otherwise issue a new token (unchanged behaviour)
  v_token := encode(gen_random_bytes(24), 'hex');

  INSERT INTO public.trusted_devices (user_id, fingerprint, device_label, status, confirmation_token)
  VALUES (v_user_id, p_fingerprint, p_device_label, 'pending_confirmation', v_token)
  ON CONFLICT (user_id, fingerprint)
  DO UPDATE SET
    confirmation_token = EXCLUDED.confirmation_token,
    device_label = EXCLUDED.device_label,
    status = 'pending_confirmation',
    created_at = now();

  RETURN v_token;
END;
$function$;

-- Check (read-only): should return true
-- select pg_get_functiondef('public.request_device_confirmation(text,text)'::regprocedure) like '%Reuse a pending token%';
