from data.SQLiteConnector import SQLiteConnector
from entity.TypeProduct import TypeProduct


class TypeProductRepository:
    def __init__(self, connector: SQLiteConnector) -> None:
        self.connector = connector

    def getById(self, typeId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM type_product WHERE id = ?""", (typeId, ))
        result = cur.fetchone()

        if result is None:
            return None

        receivedId, typeName = result
        typeProduct = TypeProduct(typeName)
        typeProduct.id = receivedId
        return typeProduct

    def add(self, typeProduct: TypeProduct) -> int:
        if typeProduct.id == -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""INSERT INTO type_product (type_name) VALUES (?)""", (typeProduct.typeName, ))
            conn.commit()
            return cur.lastrowid

        return -1

    def delete(self, typeProductId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute("""DELETE FROM type_product WHERE id = ?""", (typeProductId, ))
        conn.commit()

    def update(self, updatedTypeProduct: TypeProduct):
        if updatedTypeProduct.id != -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("""UPDATE type_product SET type_name = ? WHERE id = ?""", (updatedTypeProduct.typeName, updatedTypeProduct.id, ))
            conn.commit()