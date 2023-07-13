class Subject:
    def __init__(
            self, 
            name: str, 
            count_lectures: int, 
            count_practices: int, 
            there_is_coursework: int, 
            there_is_selfwork: int):
        self.id = -1
        self.name = name
        self.count_lectures = count_lectures
        self.count_practices = count_practices
        self.there_is_coursework = there_is_coursework
        self.there_is_selfwork = there_is_selfwork
    
    def __str__(self) -> str:
        s = f'id: {self.id};'
        s += f'Название: {self.name};'
        s += f'КоличествоЛекций: {self.count_lectures};'
        s += f'КоличествоПрактик: {self.count_practices};'
        s += f'Курсовая: {self.there_is_coursework};'
        s += f'Самостоятельная: {self.there_is_selfwork};'
        return f'Дисциплина: {{{s}}}'