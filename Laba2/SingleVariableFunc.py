from abc import ABCMeta, abstractmethod

class SingleVariableFunc:
    __metaclass__ = ABCMeta

    def __init__(self, name: str, desc: str) -> None:
        print('[INFO]: ВЫЗОВ БАЗОВОГО КОНСТРУКТОРА SingleVariableFunc()')
        self.__name = name
        """имя функции"""
        self.__desc = desc
        """описание функции"""
    
    @property
    def name(self):
        '''Полное имя функции (имя + словесное описание)'''
        return f'f(x) := {self.__name} - {self.__desc}'

    def getUsefulInfo(self) -> str:
        """
            Получить полезную 
            информацию по функции
        """
        return 'Нет полезной информации :('
    
    @abstractmethod
    def calc(self, x: float) -> float:
        """
            Вычислить значение функции
            
            Параметры
                x (float): Значение независимой переменной
        """
    
    @abstractmethod
    def getDerivative(self):
        """
            Получить экземпляр класса, 
            представляющего собой производную 
            текущего экземпляра
        """
