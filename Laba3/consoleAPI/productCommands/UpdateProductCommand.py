from data.repository.ColorRepository import ColorRepository
from data.repository.TypeProductRepository import TypeProductRepository
from data.repository.ProductRepository import ProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.BaseCommand import BaseCommand


class UpdateProductCommand(BaseCommand):
    '''Команда по обновлению товара'''
    def __init__(
            self, 
            productRepository: ProductRepository, 
            colorRepository: ColorRepository, 
            typeProductRepository: TypeProductRepository):
        super().__init__()
        self.productRepository = productRepository
        self.colorRepository = colorRepository
        self.typeProductRepository = typeProductRepository        
        self.name = 'update_product'
        self.description = 'Обновление товара'
        self.args = [
            Argument(name='prev_id', description='идентификатор товара, который нужно обновить'),
            Argument(name='new_name', description='новое название товара'),
            Argument(name='new_price', description='новая цена товара'),
            Argument(name='new_type_id', description='новый id типа товара'),
            Argument(name='new_availability', description='новое значение для \'наличие в магазине\''),
            Argument(name='new_color_id', description='новый id цвета')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return
        
        color = self.colorRepository.getById(params[5])
        typeProduct = self.typeProductRepository.getById(params[3])
        product = self.productRepository.getById(params[0])

        product.productName = params[1]
        product.price = params[2]
        product.typeProduct = typeProduct
        product.availability = params[4]
        product.color = color
        self.productRepository.update(product)
        print(f'Товар обновлен: {product}\n')