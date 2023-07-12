from data.SQLiteConnector import SQLiteConnector
from abc import ABCMeta, abstractmethod


class BaseCommand:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.name = ''
        self.description = ""
        self.args = []    
    
    @abstractmethod
    def handle(self, params: list[str]):
        """Обработчик команды"""

    def __str__(self) -> str:
        params = list(map(lambda arg: f'[{arg.name}]', self.args))
        s = f'{self.description}: {self.name} {" ".join(params)}\n'
        if len(self.args) != 0:
            for arg in self.args:
                s += f'  * {arg}\n'

        return s