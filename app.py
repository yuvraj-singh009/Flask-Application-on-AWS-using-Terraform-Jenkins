import os
import pymysql
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database configuration
db_config = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DB", "flask_app_db"),
    "cursorclass": pymysql.cursors.DictCursor,
}


def get_connection():
    return pymysql.connect(**db_config)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def hello():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT message FROM messages")
    messages = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", messages=messages)


@app.route("/submit", methods=["POST"])
def submit():
    new_message = request.form.get("new_message")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO messages (message) VALUES (%s)",
        (new_message,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": new_message})

@app.route('/health')
def health():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return jsonify({'status': 'healthy'}), 200
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)