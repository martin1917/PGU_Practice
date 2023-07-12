import sqlite3


def createSchemaSQLite(dbPath: str, scriptPath: str):
    '''
        Создание таблиц в базе данных

        Параметры:
            dbPath (str): путь к бд

            scriptPath (str): путь к SQL скрипту
    '''
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    with open(scriptPath) as file:
        sql = file.read()
        cur.executescript(sql)