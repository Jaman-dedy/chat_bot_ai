import sqlite3

def create_connection():
    conn = sqlite3.connect("data/chat_history.db")
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY,
            user_message TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()

def save_message(conn, user_message, bot_response):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO chat_history (user_message, bot_response)
        VALUES (?, ?)
    """, (user_message, bot_response))
    conn.commit()

def load_chat_history(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT user_message, bot_response FROM chat_history")
    return cursor.fetchall()