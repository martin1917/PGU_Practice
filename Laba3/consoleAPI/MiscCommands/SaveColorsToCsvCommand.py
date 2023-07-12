from data.repository.ColorRepository import ColorRepository
from data.utils import saveSimpleObjectsInCsv
from consoleAPI.Argument import Argument
from consoleAPI.Command import BaseCommand


class SaveColorsToCsvCommand(BaseCommand):
    def __init__(self, colorRepository: ColorRepository):
        super().__init__()
        self.colorRepository = colorRepository
        self.name = 'save_all_colors'
        self.description = 'Сохранить все цвета в csv файл'
        self.args = [
            Argument(name='path', description='путь к файлу')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        colors = self.colorRepository.getAll()
        saveSimpleObjectsInCsv(params[0], colors)
        print(f'Цвета сохранены в файл {params[0]}')