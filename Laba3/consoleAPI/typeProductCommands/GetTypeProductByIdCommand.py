from data.repository.TypeProductRepository import TypeProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class GetTypeProductByIdCommand(BaseCommand):
    def __init__(self, typeProductRepository: TypeProductRepository):
        super().__init__()
        self.typeProductRepository = typeProductRepository
        self.name = 'get_type_product_by_id'
        self.description = 'Получение типа товара по id'
        self.args = [
            Argument(name='id', description='идентификатор типа')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        typeProduct = self.typeProductRepository.getById(params[0])
        print(f'Получен тип: {typeProduct}\n')