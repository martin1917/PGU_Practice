from SQLiteConnector import SQLiteConnector
from entity.Subject import Subject


def getSubjectsWithCourseworkAndSelfwork(connector: SQLiteConnector, teacherFIO: str) -> list[Subject]:
    '''
        Получить все дисциплин для преподавателя, 
        по которым предусмотрена курсовая работа 
        и самостоятельная работа
    '''
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