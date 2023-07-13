class Argument:
    def __init__(self, name: str, description: str):
        '''
            Параметры:
                name (str): имя аргумента

                description (str): описание аргумента
        '''
        self.name = name
        self.description = description
    
    def __str__(self) -> str:
        return f'{self.name} - {self.description}'