import sqlite3

CREATE_COLOR_TABLE = """
    CREATE TABLE IF NOT EXISTS color(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        color_name nvarchar(128) NOT NULL
    );
"""

CREATE_TYPE_PRODUCT = """
    CREATE TABLE IF NOT EXISTS type_product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type_name nvarchar(128) NOT NULL
    );
"""

CREATE_PRODUCT = """
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name nvarchar(128) NOT NULL,
        price REAL NOT NULL,
        type_id INTEGER NOT NULL,
        availability INTEGER NOT NULL DEFAULT 0 CHECK(availability = 0 OR availability = 1),
        color_id INTEGER NOT NULL,
        
        FOREIGN KEY (type_id) REFERENCES type_product (id),
        FOREIGN KEY (color_id) REFERENCES color (id)
    );
"""

def create_schema(path: str):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(CREATE_COLOR_TABLE)
    cur.execute(CREATE_TYPE_PRODUCT)
    cur.execute(CREATE_PRODUCT)

class Color:
    def __init__(self, colorName: str):
        self.id = -1
        self.colorName = colorName

class TypeProduct:
    def __init__(self, typeName: str):
        self.id = -1
        self.typeName = typeName

class Product:
    def __init__(
            self, 
            productName: str, 
            price: float, 
            typeProduct: TypeProduct, 
            availability: int, 
            color: Color):
        self.id = -1
        self.productName = productName
        self.price = price
        self.typeProduct = typeProduct
        self.availability = availability
        self.color = color


class SQLiteConnector:
    def __init__(self, path: str):
        self.path = path
    
    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

class ColorRepository:
    def __init__(self, connector: SQLiteConnector) -> None:
        self.connector = connector

    def getById(self, colorId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM color WHERE id = ?""", (colorId, ))
        receivedId, colorName = cur.fetchone()
        color = Color(colorName)
        color.id = receivedId
        return color

    def add(self, color: Color):
        if color.id == -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""INSERT INTO color (color_name) VALUES (?)""", (color.colorName, ))
            conn.commit()

    def delete(self, colorId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""DELETE FROM color WHERE id = ?""", (colorId, ))
        conn.commit()

    def update(self, updatedColor: Color):
        if updatedColor.id != -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""UPDATE color SET color_name = ? WHERE id = ?""", (updatedColor.colorName, updatedColor.id, ))
            conn.commit()

class TypeProductRepository:
    def __init__(self, connector: SQLiteConnector) -> None:
        self.connector = connector

    def getById(self, typeId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM type_product WHERE id = ?""", (typeId, ))
        receivedId, typeName = cur.fetchone()
        typeProduct = TypeProduct(typeName)
        typeProduct.id = receivedId
        return typeProduct

    def add(self, typeProduct: TypeProduct):
        if typeProduct.id == -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""INSERT INTO type_product (type_name) VALUES (?)""", (typeProduct.typeName, ))
            conn.commit()

    def delete(self, typeProductId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""DELETE FROM type_product WHERE id = ?""", (typeProductId, ))
        conn.commit()

    def update(self, updatedTypeProduct: TypeProduct):
        if updatedTypeProduct.id != -1:
            conn = self.connector.connect()
            cur = conn.cursor()
            cur.execute("""UPDATE type_product SET type_name = ? WHERE id = ?""", (updatedTypeProduct.typeName, updatedTypeProduct.id, ))
            conn.commit()


if __name__ == '__main__':
    DB_PATH = './laba3_db.db'
    
    connector = SQLiteConnector(DB_PATH)
    colorRepo = ColorRepository(connector)
    typeProductRepo = TypeProductRepository(connector)