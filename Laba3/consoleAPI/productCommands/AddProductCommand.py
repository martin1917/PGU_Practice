from data.repository.ColorRepository import ColorRepository
from data.repository.TypeProductRepository import TypeProductRepository
from entity.Product import Product
from data.repository.ProductRepository import ProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class AddProductCommand(BaseCommand):
    def __init__(
            self, 
            productRepository: ProductRepository, 
            colorRepository: ColorRepository, 
            typeProductRepository: TypeProductRepository):
        super().__init__()
        self.productRepository = productRepository
        self.colorRepository = colorRepository
        self.typeProductRepository = typeProductRepository        
        self.name = 'add_product'
        self.description = 'Добавление товара'
        self.args = [
            Argument(name='name', description='название товара'),
            Argument(name='price', description='цена товара'),
            Argument(name='type_id', description='id типа товара'),
            Argument(name='availability', description='Наличие в магазине'),
            Argument(name='color_id', description='id цвета')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return
        
        color = self.colorRepository.getById(params[4])
        typeProduct = self.typeProductRepository.getById(params[2])
        product = Product(params[0], params[1], typeProduct, params[3], color)
        productId = self.productRepository.add(product)
        product.id = productId
        print(f'Добавлен товар: {product}')