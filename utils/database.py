import sqlite3

conn = sqlite3.connect("database/moderation.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS punishments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    moderator_id INTEGER,
    action TEXT,
    reason TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def log_punishment(user_id, mod_id, action, reason):
    cur.execute(
        "INSERT INTO punishments (user_id, moderator_id, action, reason) VALUES (?,?,?,?)",
        (user_id, mod_id, action, reason)
    )
    conn.commit()

def get_history(user_id):
    cur.execute(
        "SELECT action, reason, timestamp FROM punishments WHERE user_id=?",
        (user_id,)
    )
    return cur.fetchall()
