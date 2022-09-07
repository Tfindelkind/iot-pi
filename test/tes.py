import psycopg2
import datetime
from datetime import datetime, timezone

conn = psycopg2.connect(database="iot-pi",
                        host="192.168.178.221",
                        user="iot-pi",
                        password="iot-pi",
                        port="5432")

cursor = conn.cursor()

cursor.execute("SELECT * FROM telemetry")

for r in cursor.fetchall():
  print (r)

dt = datetime.now(timezone.utc)
#sql_insert_query = 'INSERT INTO telemetry(pv_dc_power1, pv_dc_power2, timestamp) VALUES (%s, %s, now)'

