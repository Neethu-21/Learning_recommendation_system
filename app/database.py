import sqlite3
import os

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "student_profiles.db"
)

def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        student_id INTEGER,
        career_goal TEXT,
        study_time TEXT,
        weak_subject TEXT,
        roadmap TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
    
def save_recommendation(
    student_name,
    student_id,
    career_goal,
    study_time,
    weak_subject,
    roadmap
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO student_history
    (
        student_name,
        student_id,
        career_goal,
        study_time,
        weak_subject,
        roadmap
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        student_name,
        student_id,
        career_goal,
        study_time,
        weak_subject,
        roadmap
    ))

    conn.commit()
    conn.close()
    
def get_history():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        student_name,
        career_goal,
        study_time,
        weak_subject,
        created_at
    FROM student_history
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows