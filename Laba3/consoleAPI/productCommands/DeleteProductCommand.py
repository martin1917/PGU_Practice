from data.repository.ProductRepository import ProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.BaseCommand import BaseCommand


class DeleteProductCommand(BaseCommand):
    '''Команда по удалению товара'''
    def __init__(self, productRepository: ProductRepository):
        super().__init__()
        self.productRepository = productRepository     
        self.name = 'delete_product'
        self.description = 'Удаление товара'
        self.args = [
            Argument(name='id', description='идентификатор товара')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return
        
        self.productRepository.delete(params[0])
        print('Товар удален\n')