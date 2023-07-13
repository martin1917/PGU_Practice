from query.getSubjectWithLike import getSubjectWithLike
from query.getSubjectsWithCourseworkAndSelfwork import getSubjectsWithCourseworkAndSelfwork
from entity.Subject import Subject
from SQLiteConnector import SQLiteConnector

if __name__ == '__main__':
    DB_PATH = './Laba4/db/laba4_db.db'
    connector = SQLiteConnector(DB_PATH)

    res1 = getSubjectsWithCourseworkAndSelfwork(connector, 'Иванов И.И.')
    for row in res1: print(row)

    print('=' * 75)

    res2 = getSubjectWithLike(connector, '%т%')
    for row in res2: print(row)
