from entity.Product import Product
from entity.TypeProduct import TypeProduct
from entity.Color import Color
from data.SQLiteConnector import SQLiteConnector


class ProductRepository:
    def __init__(self, connector: SQLiteConnector) -> None:
        self.connector = connector

    def getAll(self) -> list[Product]:
        conn = self.connector.connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                p.id AS 'product_id', 
                p.product_name AS 'product_name', 
                p.price AS 'product_price', 
                tp.id AS 'type_id', 
                tp.type_name AS 'type_name',  
                p.availability AS 'product_availability', 
                c.id AS 'color_id',
                c.color_name AS 'color_name' 
            FROM product p
            JOIN type_product tp ON p.type_id = tp.id 
            JOIN color c ON p.color_id = c.id""")

        allProducts = []
        for row in cur.fetchall():
            receivedId, productName, price, typeProductId, typeProductName, availability, colorId, colorName = row

            typeProduct = TypeProduct(typeProductName)
            typeProduct.id = typeProductId

            color = Color(colorName)
            color.id = colorId

            product = Product(productName, price, typeProduct, availability, color)
            product.id = receivedId
            
            allProducts.append(product)

        return allProducts

    
    def getById(self, productId: int) -> Product:
        conn = self.connector.connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                p.id AS 'product_id', 
                p.product_name AS 'product_name', 
                p.price AS 'product_price', 
                tp.id AS 'type_id', 
                tp.type_name AS 'type_name',  
                p.availability AS 'product_availability', 
                c.id AS 'color_id',
                c.color_name AS 'color_name' 
            FROM product p
            JOIN type_product tp ON p.type_id = tp.id 
            JOIN color c ON p.color_id = c.id
            WHERE p.id = (?)""", (productId, ))

        result = cur.fetchone()

        if result is None:
            return None

        receivedId, productName, price, typeProductId, typeProductName, availability, colorId, colorName = result

        typeProduct = TypeProduct(typeProductName)
        typeProduct.id = typeProductId

        color = Color(colorName)
        color.id = colorId

        product = Product(productName, price, typeProduct, availability, color)
        product.id = receivedId

        return product
    
    def add(self, product: Product) -> int:
        if product.id == -1:
            conn = self.connector.connect()
            cur = conn.cursor()

            typeId = product.typeProduct.id
            if typeId == -1:
                cur.execute("""INSERT INTO type_product (type_name) VALUES (?)""", (product.typeProduct.typeName, ))
                typeId = cur.lastrowid

            colorId = product.color.id
            if colorId == -1:
                cur.execute("""INSERT INTO color (color_name) VALUES (?)""", (product.color.colorName, ))
                colorId = cur.lastrowid
            
            params = (product.productName, product.price, typeId, product.availability, colorId, )
            cur.execute("""
                INSERT INTO product 
                (product_name, price, type_id, availability, color_id) 
                VALUES 
                (?, ?, ?, ?, ?)""", params)

            conn.commit()
            return cur.lastrowid

        return -1
    
    def delete(self, productId: int):
        conn = self.connector.connect()
        cur = conn.cursor()
        cur.execute("""DELETE FROM product WHERE id = ?""", (productId, ))
        conn.commit()
    
    def update(self, updatedProduct: Product):
        if updatedProduct.id != -1 and updatedProduct.typeProduct.id != -1 and updatedProduct.color.id != -1:
            conn = self.connector.connect()
            cur = conn.cursor()

            paramsForColor = (updatedProduct.color.colorName, updatedProduct.color.id, )
            cur.execute("""UPDATE color SET color_name = ? WHERE id = ?""", paramsForColor)

            paramsForTypeProduct = (updatedProduct.typeProduct.typeName, updatedProduct.typeProduct.id, )
            cur.execute("""UPDATE type_product SET type_name = ? WHERE id = ?""", paramsForTypeProduct)
            
            paramsForProduct = (
                updatedProduct.productName, 
                updatedProduct.price,
                updatedProduct.typeProduct.id, 
                updatedProduct.availability, 
                updatedProduct.color.id,
                updatedProduct.id,)
            
            cur.execute("""
                UPDATE product SET 
                    product_name = ?,
                    price = ?,
                    type_id = ?,
                    availability = ?,
                    color_id = ?
                WHERE id = ? """, paramsForProduct)
            
            conn.commit()