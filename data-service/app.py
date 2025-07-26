from flask import Flask, jsonify
import redis
import psycopg2
import time
import os

app = Flask(__name__)

# Redis config
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
cache = redis.Redis(host=redis_host, port=redis_port)

# PostgreSQL config
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "users")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

def connect_db_with_retry(retries=5, delay=3):
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS
            )
            return conn
        except Exception as e:
            print(f"DB connection failed (attempt {attempt+1}): {e}")
            time.sleep(delay)
    raise Exception("Failed to connect to DB after retries.")

@app.route('/user/<string:name>')
def get_user(name):
    cached = cache.get(name)
    if cached:
        return jsonify({"name": name, "cached": True, "info": cached.decode('utf-8')})

    try:
        conn = connect_db_with_retry()
        cur = conn.cursor()
        cur.execute("SELECT info FROM users WHERE name = %s", (name,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            data = row[0]
            cache.set(name, data)
            return jsonify({"name": name, "cached": False, "info": data})
        else:
            return jsonify({"error": f"User '{name}' not found in database"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

