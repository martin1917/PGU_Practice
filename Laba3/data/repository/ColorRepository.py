from data.SQLiteConnector import SQLiteConnector
from entity.Color import Color


class ColorRepository:
    def __init__(self, connector: SQLiteConnector) -> None:
        self.connector = connector

    def getById(self, colorId: int) -> Color:
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM color WHERE id = ?""", (colorId, ))
        receivedId, colorName = cur.fetchone()
        color = Color(colorName)
        color.id = receivedId
        return color

    def add(self, color: Color) -> int:
        if color.id == -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""INSERT INTO color (color_name) VALUES (?)""", (color.colorName, ))
            conn.commit()
            return cur.lastrowid
        
        return -1

    def delete(self, colorId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("""DELETE FROM color WHERE id = ?""", (colorId, ))
        conn.commit()

    def update(self, updatedColor: Color):
        if updatedColor.id != -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("""UPDATE color SET color_name = ? WHERE id = ?""", (updatedColor.colorName, updatedColor.id, ))
            conn.commit()