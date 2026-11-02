from flask import Flask, request, redirect, send_from_directory, jsonify
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "placement.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)
        conn.execute("""
            INSERT OR IGNORE INTO users (email, password, role)
            VALUES (?, ?, ?)
        """, ("recruiter@demo.com", "demo123", "Recruiter"))

        conn.execute("""
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL,
                mobile TEXT NOT NULL,
                dob TEXT,
                gender TEXT,
                location TEXT,
                qualification TEXT NOT NULL,
                college TEXT NOT NULL,
                university TEXT,
                passing_year INTEGER NOT NULL,
                percentage REAL NOT NULL,
                backlogs INTEGER NOT NULL,
                technology TEXT NOT NULL,
                secondary_skills TEXT,
                skill_level TEXT,
                preferred_location TEXT,
                status TEXT NOT NULL
            )
        """)


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    role = request.form.get("role", "").strip()

    with get_db() as conn:
        user = conn.execute(
            "SELECT id FROM users WHERE email=? AND password=? AND role=?",
            (email, password, role)
        ).fetchone()

    if user:
        return redirect("/dashboard.html")

    return "Invalid login details", 401


@app.route("/save-candidate", methods=["POST"])
def save_candidate():
    fields = [
        "full_name", "email", "mobile", "dob", "gender", "location",
        "qualification", "college", "university", "passing_year",
        "percentage", "backlogs", "technology", "secondary_skills",
        "skill_level", "preferred_location", "status"
    ]

    data = {field: request.form.get(field, "").strip() for field in fields}

    required = [
        "full_name", "email", "mobile", "qualification", "college",
        "passing_year", "percentage", "backlogs", "technology", "status"
    ]
    missing = [field for field in required if not data[field]]
    if missing:
        return "Missing required fields: " + ", ".join(missing), 400

    try:
        data["passing_year"] = int(data["passing_year"])
        data["percentage"] = float(data["percentage"])
        data["backlogs"] = int(data["backlogs"])
    except ValueError:
        return "Passing year, percentage, and backlogs must be numeric.", 400

    with get_db() as conn:
        conn.execute("""
            INSERT INTO candidates (
                full_name, email, mobile, dob, gender, location,
                qualification, college, university, passing_year,
                percentage, backlogs, technology, secondary_skills,
                skill_level, preferred_location, status
            )
            VALUES (
                :full_name, :email, :mobile, :dob, :gender, :location,
                :qualification, :college, :university, :passing_year,
                :percentage, :backlogs, :technology, :secondary_skills,
                :skill_level, :preferred_location, :status
            )
        """, data)

    return redirect("/candidates.html?success=1")


@app.route("/api/candidates", methods=["GET"])
def api_candidates():
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM candidates ORDER BY id DESC"
        ).fetchall()

    return jsonify([dict(row) for row in rows])


@app.route("/api/candidates/<int:candidate_id>", methods=["DELETE"])
def delete_candidate(candidate_id):
    with get_db() as conn:
        cursor = conn.execute(
            "DELETE FROM candidates WHERE id=?",
            (candidate_id,)
        )

    if cursor.rowcount == 0:
        return jsonify({"error": "Candidate not found"}), 404

    return jsonify({"message": "Candidate deleted"})


@app.route("/<path:page>")
def pages(page):
    file_path = os.path.join(BASE_DIR, page)
    if page.endswith(".html") and os.path.isfile(file_path):
        return send_from_directory(BASE_DIR, page)
    return "Page Not Found", 404


@app.route("/css/<path:filename>")
def css(filename):
    return send_from_directory(os.path.join(BASE_DIR, "css"), filename)


@app.route("/js/<path:filename>")
def js(filename):
    return send_from_directory(os.path.join(BASE_DIR, "js"), filename)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)