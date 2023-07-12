from entity.Subject import Subject
from SQLiteConnector import SQLiteConnector


def getSubjectsWithCourseworkAndSelfwork(connector: SQLiteConnector, teacherFIO: str) -> list[Subject]:
    conn = connector.connect()
    cur = conn.cursor()

    params = (teacherFIO, 1, 1, )
    cur.execute("""
        SELECT 
            s.id,
            s.name,
            s.count_lectures,
            s.count_practices,
            s.there_is_coursework,
            s.there_is_selfwork
        FROM teacher t 
        JOIN subject s ON t.subject_id = s.id
        WHERE 
            t.FIO = ? and 
            s.there_is_coursework = ? and 
            s.there_is_selfwork = ?""", params)
    
    subjects = []
    for row in cur.fetchall():
        subject = Subject(row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])) 
        subject.id = int(row[0])
        subjects.append(subject)

    return subjects

def getSubjectWithLike(connector: SQLiteConnector, like: str) -> list[Subject]:
    conn = connector.connect()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM subject WHERE name LIKE \'{like}\'')

    subjects = []
    for row in cur.fetchall():
        subject = Subject(row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])) 
        subject.id = int(row[0])
        subjects.append(subject)

    return subjects


if __name__ == '__main__':
    DB_PATH = './Laba4/db/laba4_db.db'
    connector = SQLiteConnector(DB_PATH)

    res1 = getSubjectsWithCourseworkAndSelfwork(connector, 'Иванов И.И.')
    for row in res1: print(row)

    print('=' * 75)

    res2 = getSubjectWithLike(connector, '%т%')
    for row in res2: print(row)
