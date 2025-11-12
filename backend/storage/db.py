import sqlite3
import os

class Database:
    def __init__(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            signal TEXT,
            bias TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
        self.conn.commit()

    def save_signal(self, symbol, signal, bias):
        self.conn.execute("INSERT INTO signals (symbol, signal, bias) VALUES (?, ?, ?)", (symbol, signal, bias))
        self.conn.commit()

    def is_connected(self):
        try:
            self.conn.execute("SELECT 1")
            return True
        except:
            return False
