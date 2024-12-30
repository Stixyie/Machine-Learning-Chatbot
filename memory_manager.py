import sqlite3
from datetime import datetime

class MemoryManager:
    def __init__(self):
        self.conn = sqlite3.connect('bot_memory.db')
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                user_message TEXT,
                bot_response TEXT,
                timestamp DATETIME
            )
        ''')
        self.conn.commit()
    
    def store_interaction(self, user_id, message, response):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO interactions (user_id, user_message, bot_response, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (user_id, message, response, datetime.now()))
        self.conn.commit()
    
    def get_context(self, user_id, limit=10):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT user_message, bot_response FROM interactions
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (user_id, limit))
        return cursor.fetchall()
