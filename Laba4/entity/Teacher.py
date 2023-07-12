class Teacher:
    def __init__(
            self, 
            FIO: str, 
            subjectId: int):
        self.id = -1
        self.FIO = FIO
        self.subjectId = subjectId
    
    def __str__(self) -> str:
        s = f'id: {self.id};ФИО: {self.FIO};ID_Дисциплины: {self.subjectId}'
        return f'Преподаватель: {{{s}}}'