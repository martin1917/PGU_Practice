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
    def __init__(self, id: int, colorName: str):
        self.id = id
        self.colorName = colorName

class TypeProduct:
    def __init__(self, id: int, typeName: str):
        self.id = id
        self.typeName = typeName

class Product:
    def __init__(
            self, 
            id: int, 
            productName: str, 
            price: float, 
            typeProduct: TypeProduct, 
            availability: int, 
            color: Color):
        self.id = id
        self.productName = productName
        self.price = price
        self.typeProduct = typeProduct
        self.availability = availability
        self.color = color
