from data.repository.TypeProductRepository import TypeProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class UpdateProductCommand(BaseCommand):
    def __init__(self, typeProductRepository: TypeProductRepository):
        self.typeProductRepository = typeProductRepository
        self.name = 'update_type_product'
        self.description = 'Обновление типа товара'
        self.args = [
            Argument(name='prev_id', description='идентификатор типа, который нужно обновить'),
            Argument(name='new_name', description='новое название для типа товара')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        typeProduct = self.typeProductRepository.getById(params[0])
        typeProduct.typeName = params[1]
        self.typeProductRepository.update(typeProduct)
        print(f'тип Обновлен: {typeProduct}')