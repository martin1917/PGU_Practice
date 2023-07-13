from data.SQLiteConnector import SQLiteConnector
from entity.TypeProduct import TypeProduct


class TypeProductRepository:
    def __init__(self, connector: SQLiteConnector):
        self.connector = connector

    def getById(self, typeId: int):
        '''получить тип товара по id'''
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM type_product 
            WHERE id = ?""", (typeId, ))
        result = cur.fetchone()

        if result is None:
            return None

        receivedId, typeName = result
        typeProduct = TypeProduct(typeName)
        typeProduct.id = receivedId
        return typeProduct

    def add(self, typeProduct: TypeProduct) -> int:
        '''добавить тип товара'''
        if typeProduct.id == -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO type_product 
                (type_name) 
                VALUES (?)""", (typeProduct.typeName, ))
            conn.commit()
            return cur.lastrowid

        return -1

    def delete(self, typeProductId: int):
        '''удалить тип товара по id'''
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        params = (typeProductId, )
        cur.execute("""DELETE FROM type_product WHERE id = ?""", params)
        conn.commit()

    def update(self, updatedTypeProduct: TypeProduct):
        '''обновить тип товара'''
        if updatedTypeProduct.id != -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")

            params = (updatedTypeProduct.typeName, updatedTypeProduct.id, )
            cur.execute("""
                UPDATE type_product SET 
                    type_name = ? 
                WHERE id = ?""", params)
            
            conn.commit()