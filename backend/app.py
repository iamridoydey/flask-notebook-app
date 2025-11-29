from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from config import Config
import pymysql

app = Flask(__name__)
# --- Auto create database if missing---
conn = pymysql.connect(
    host=Config.MYSQL_HOST,
    user=Config.MYSQL_USER,
    password=Config.MYSQL_PASSWORD,
    port=Config.MYSQL_PORT
)

cur = conn.cursor()
cur.execute(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DB}")
conn.commit()
cur.close()
conn.close()

DATABASE_URL = f"mysql+pymysql://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{Config.MYSQL_DB}"
engine = create_engine(DATABASE_URL, future=True)

def init_db():
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS notes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        note TEXT
    );
    """
    with engine.begin() as conn:
        conn.execute(text(create_table_sql))

@app.route("/", methods=["GET"])
def home():
    return {"Message": "I love you Prite & this is first flask app"}
@app.route("/health", methods=["GET"])
def health():
    return {"status": "Health is okay"}

@app.route("/notes", methods=["GET"])
def get_notes():
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT id, note FROM notes")).all()
        return jsonify([{"id": r.id, "note": r.note} for r in rows])

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json(silent=True) or {}
    note = data.get("note")
    if not note:
        return jsonify({"error": "note is required"}), 400
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO notes (note) VALUES (:note)"), {"note": note})
    return jsonify({"note": note}), 201

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
