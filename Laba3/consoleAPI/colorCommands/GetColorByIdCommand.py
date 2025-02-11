from data.repository.ColorRepository import ColorRepository
from consoleAPI.Argument import Argument
from consoleAPI.BaseCommand import BaseCommand


class GetColorByIdCommand(BaseCommand):
    '''Команда по получению цвета по id'''
    def __init__(self, colorRepository: ColorRepository):
        super().__init__()
        self.colorRepository = colorRepository
        self.name = 'get_color_by_id'
        self.description = 'Получение цвета по id'
        self.args = [
            Argument(name='id', description='идентификатор цвета')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        print(f'{self.colorRepository.getById(params[0])}\n')