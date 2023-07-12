from entity.Color import Color
from data.repository.ColorRepository import ColorRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class DeleteColorCommand(BaseCommand):
    def __init__(self, colorRepository: ColorRepository):
        super().__init__()
        self.colorRepository = colorRepository
        self.name = 'delete_color'
        self.description = 'Удаление цвета'
        self.args = [
            Argument(name='id', description='идентификатор цвета')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        self.colorRepository.delete(params[0])
        print('Цвет удален\n')