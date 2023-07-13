from entity.Subject import Subject
from SQLiteConnector import SQLiteConnector


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