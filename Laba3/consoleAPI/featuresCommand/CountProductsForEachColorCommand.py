from feature.countProductsForEachColor import countProductsForEachColor
from data.SQLiteConnector import SQLiteConnector
from consoleAPI.Command import BaseCommand


class CountProductsForEachColorCommand(BaseCommand):
    def __init__(self, connector: SQLiteConnector):
        super().__init__()
        self.connector = connector
        self.name = 'count_products_for_each_color_command'
        self.description = 'посчитать количество товаров для каждого цвета'
    
    def handle(self, params: list[str]):
        if len(params) != len(self.args):
            print('Передано неверное кол-во параметров')
            return

        result = countProductsForEachColor(self.connector)
        for row in result: print(f'{row[0]}: {row[1]}')
        print()