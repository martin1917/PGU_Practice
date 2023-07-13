from data.repository.ColorRepository import ColorRepository
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class UpdateColorCommand(BaseCommand):
    '''Команда по обновлению цвета'''
    def __init__(self, colorRepository: ColorRepository):
        super().__init__()
        self.colorRepository = colorRepository
        self.name = 'update_color'
        self.description = 'Обновление цвета'
        self.args = [
            Argument(name='prev_id', description='идентификатор цвета, который нужно обновить'),
            Argument(name='new_name', description='новое название')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        color = self.colorRepository.getById(params[0])
        color.colorName = params[1]
        self.colorRepository.update(color)
        print(f'Цвет обновлен: {color}\n')