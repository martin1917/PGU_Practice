from entity.Color import Color
from entity.TypeProduct import TypeProduct


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
    
    def __str__(self) -> str:
        s = f'id: {self.id};'
        s += f'название: {self.productName};'
        s += f'цена: {self.price};'
        s += f'тип: {self.typeProduct.typeName};'
        s += f'наличие в магазине: {self.availability};'
        s += f'цвет: {self.color.colorName}'
        return f'Product {{{s}}}'