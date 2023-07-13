from query.getSubjectWithLike import getSubjectWithLike
from query.getSubjectsWithCourseworkAndSelfwork import getSubjectsWithCourseworkAndSelfwork
from SQLiteConnector import SQLiteConnector

if __name__ == '__main__':
    DB_PATH = './Laba4/db/laba4_db.db'
    connector = SQLiteConnector(DB_PATH)

    '''
        Получить список всех дисциплин преподавателя «Иванов И.И.», 
        по которым предусмотрена курсовая работа и 
        самостоятельная работа.
    '''
    res1 = getSubjectsWithCourseworkAndSelfwork(connector, 'Иванов И.И.')
    for row in res1: print(row)

    print('=' * 75)

    # Получить все дисциплины, в чьем названии встречается буква «П».
    res2 = getSubjectWithLike(connector, '%т%')
    for row in res2: print(row)
