import sqlite3

DB_NAME = "itgenie.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        policy_name TEXT NOT NULL,
        policy_type TEXT NOT NULL,
        purpose TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
