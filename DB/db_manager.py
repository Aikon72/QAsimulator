import psycopg2
from contextlib import closing

with psycopg2.connect(
    host="192.168.1.100",
    database="qa_simulator_db",
    user="Prog852",
    password="pass258"
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version()")
        print(cur.fetchone())
    # Автоматический коммит при успехе
    # Автоматический роллбэк при исключении