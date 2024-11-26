from datetime import datetime, timedelta, timezone
from lib.db import pool
class HomeActivities:
  def run():
    sql = "SELECT * FROM activities;"
    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
        json = cur.fetchall()
        print(json)
        return json