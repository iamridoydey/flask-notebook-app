from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from config import Config
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# --- Auto create database if missing ---
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
        note TEXT,
        completed BOOLEAN DEFAULT FALSE
    );
    """
    with engine.begin() as conn:
        conn.execute(text(create_table_sql))

@app.route("/", methods=["GET"])
def home():
    return {"Message": "This is flask notebook api"}

@app.route("/health", methods=["GET"])
def health():
    return {"status": "Health is okay"}

@app.route("/notes", methods=["GET"])
def get_notes():
    with engine.begin() as conn:
        result = conn.execute(text("SELECT id, note, completed FROM notes"))
        notes = [{"id": row.id, "note": row.note, "completed": row.completed} for row in result]
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json(silent=True) or {}
    note = data.get("note")
    if not note:
        return jsonify({"error": "note is required"}), 400
    with engine.begin() as conn:
        result = conn.execute(
            text("INSERT INTO notes (note, completed) VALUES (:note, :completed)"),
            {"note": note, "completed": False}
        )
        new_id = result.lastrowid
    return jsonify({"id": new_id, "note": note, "completed": False}), 201

@app.route("/notes/<int:note_id>", methods=["PUT"])
def toggle_note(note_id):
    data = request.get_json(silent=True) or {}
    completed = data.get("completed", False)
    with engine.begin() as conn:
        result = conn.execute(
            text("UPDATE notes SET completed=:completed WHERE id=:id"),
            {"completed": completed, "id": note_id}
        )
        if result.rowcount == 0:
            return jsonify({"error": "note not found"}), 404
    return jsonify({"id": note_id, "completed": completed}), 200


@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    with engine.begin() as conn:
        result = conn.execute(
            text("DELETE FROM notes WHERE id=:id"),
            {"id": note_id}
        )
        if result.rowcount == 0:
            return jsonify({"error": "note not found"}), 404
    return jsonify({"message": f"Note {note_id} deleted"}), 200


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
