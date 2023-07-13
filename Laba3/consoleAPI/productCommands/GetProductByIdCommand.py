from data.repository.ProductRepository import ProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class GetProductByIdCommand(BaseCommand):
    '''Команда по получению товара по id'''
    def __init__(self, productRepository: ProductRepository):
        super().__init__()
        self.productRepository = productRepository     
        self.name = 'get_product_by_id'
        self.description = 'Получение товара по id'
        self.args = [
            Argument(name='id', description='идентификатор товара')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return
        
        product = self.productRepository.getById(params[0])
        print(f'Получен товар: {product}\n')