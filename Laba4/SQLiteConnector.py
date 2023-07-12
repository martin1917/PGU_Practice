import sqlite3


class SQLiteConnector:
    def __init__(self, path: str):
        self.path = path
    
    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)