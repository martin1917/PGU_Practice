from data.repository.TypeProductRepository import TypeProductRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class DeleteTypeProductCommand(BaseCommand):
    def __init__(self, typeProductRepository: TypeProductRepository):
        self.typeProductRepository = typeProductRepository
        self.name = 'delete_type_product'
        self.description = 'Удаление типа товара'
        self.args = [
            Argument(name='id', description='идентификатор типа')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        self.typeProductRepository.delete(params[0])
        print('Тип удален:')