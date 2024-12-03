import uuid
from datetime import datetime, timedelta, timezone
from lib.db import pool, query_wrap_object, query_wrap_array

class CreateActivity:
  def run(message, user_handle, ttl, logger):
    model = {
      'errors': None,
      'data': None
    }
    now = datetime.now(timezone.utc).astimezone()
    if model['errors']:
      model['data'] = {
        'handle':  user_handle,
        'message': message
      }   
    else:
      expires_at = now.isoformat()
      create_activities(message, expires_at, logger)
      uuid = get_user_uuid()
      model['data'] = {
        'uuid': uuid,
        'display_name': user_handle,
        'handle':  user_handle,
        'message': message,
        'created_at': now.isoformat(),
        'expires_at': expires_at
      }
    return model

def create_activities(message, expires_at, logger):
    user_uuid = get_user_uuid()
    logger.info(message)
    logger.info(user_uuid)
    sql = f"""
    INSERT INTO activities(
      user_uuid, message, expires_at
    )
    VALUES(
    '{user_uuid["uuid"]}',
    '{message}',
    '{expires_at}');
    """
    with pool.connection() as conn:
          with conn.cursor() as cur:
            cur.execute(sql)

    
def get_user_uuid():
  query = """
  SELECT
      users.uuid
    FROM public.users
    """
  sql = query_wrap_object(query)
  with pool.connection() as conn:
    with conn.cursor() as cur:
      cur.execute(sql)
      json = cur.fetchone()
      print(json)
      return json[0]