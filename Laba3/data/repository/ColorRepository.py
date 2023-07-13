from data.SQLiteConnector import SQLiteConnector
from entity.Color import Color


class ColorRepository:
    def __init__(self, connector: SQLiteConnector) -> None:
        self.connector = connector

    def getAll(self) -> list[Color]:
        '''получить все цвета'''
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM color""")

        colors = []
        for row in cur.fetchall():
            color = Color(row[1])
            color.id = row[0]
            colors.append(color)
            
        return colors

    def getById(self, colorId: int) -> Color:
        '''получить цвет по id'''
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM color WHERE id = ?""", (colorId, ))
        result = cur.fetchone()

        if result is None:
            return None
        
        receivedId, colorName = result
        color = Color(colorName)
        color.id = receivedId
        return color

    def add(self, color: Color) -> int:
        '''добавить цвет'''
        if color.id == -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""INSERT INTO color (color_name) VALUES (?)""", (color.colorName, ))
            conn.commit()
            return cur.lastrowid
        
        return -1

    def delete(self, colorId: int):
        '''удалить цвет по id'''
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("""DELETE FROM color WHERE id = ?""", (colorId, ))
        conn.commit()

    def update(self, updatedColor: Color):
        '''обновить цвет'''
        if updatedColor.id != -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("""UPDATE color SET color_name = ? WHERE id = ?""", (updatedColor.colorName, updatedColor.id, ))
            conn.commit()