from entity.Color import Color
from data.utils import loadSimpleObjectsFromCsv
from consoleAPI.Argument import Argument
from consoleAPI.BaseCommand import BaseCommand


class LoadAllColorsFromCsvCommand(BaseCommand):
    '''Команда для загрузки всех цветов из csv файла'''
    def __init__(self):
        super().__init__()
        self.name = 'load_all_colors'
        self.description = 'Загрузить все цвета из csv файла'
        self.args = [
            Argument(name='path', description='путь к файлу')
        ]
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return
        
        objects = loadSimpleObjectsFromCsv(params[0])

        if objects is None:
            print(f'файла по пути {params[0]} не существует')
            return

        for obj in objects:
            color = Color(obj['colorName'])
            color.id = int(obj['id'])
            print(color)