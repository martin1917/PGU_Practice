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