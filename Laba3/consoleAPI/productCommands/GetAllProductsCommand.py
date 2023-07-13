from data.repository.ProductRepository import ProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class GetAllProductsCommand(BaseCommand):
    '''Команда по получению всех товаров'''
    def __init__(self, productRepository: ProductRepository):
        super().__init__()
        self.productRepository = productRepository     
        self.name = 'get_all_products'
        self.description = 'Получение всех товаров'
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return
        
        allProducts = self.productRepository.getAll()
        for product in allProducts: print(f'{product}\n')