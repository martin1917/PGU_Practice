from entity.TypeProduct import TypeProduct
from data.repository.TypeProductRepository import TypeProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.BaseCommand import BaseCommand


class AddTypeProductCommand(BaseCommand):
    '''Команда по добавению типа товара'''
    def __init__(self, typeProductRepository: TypeProductRepository):
        super().__init__()
        self.typeProductRepository = typeProductRepository
        self.name = 'add_type_product'
        self.description = 'Добавление типа товара'
        self.args = [
            Argument(name='name', description='название типа')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        typeProduct = TypeProduct(params[0])
        typeProductId = self.typeProductRepository.add(typeProduct)
        typeProduct.id = typeProductId 
        print(f'Добавлен тип: {typeProduct}\n')