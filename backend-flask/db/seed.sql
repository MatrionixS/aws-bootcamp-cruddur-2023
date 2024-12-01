-- this file was manually created
INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Serhii Rusyn', 'serhii_rusyn' ,'MOCK')

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'serhii_rusyn' LIMIT 1),
    'Hello Rosia, Yak sya mayesh',
    current_timestamp + interval '10 day'
  )