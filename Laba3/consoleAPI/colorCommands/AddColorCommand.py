from entity.Color import Color
from data.repository.ColorRepository import ColorRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class AddColorCommand(BaseCommand):
    def __init__(self, colorRepository: ColorRepository):
        super().__init__()
        self.colorRepository = colorRepository
        self.name = 'add_color'
        self.description = 'Добавление цвета'
        self.args = [
            Argument(name='name', description='название цвета')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        color = Color(params[0])
        self.colorRepository.add(color)
        print(f'Добавлен цвет: {color}')