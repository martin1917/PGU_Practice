from pathlib import Path
import sqlite3
import csv


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

def saveSimpleObjectsInCsv(path: str, datas: list):
    '''
        Сохранить простые объекты в csv файл

        Параметры:
            path (str): путь до csv файла

            datas (list): список объектов для сохранения
    '''
    with open(path, mode='a+', encoding='utf-8') as file:
        for data in datas:
            keys = [
                attr 
                for attr in dir(data) 
                if not attr.startswith('__')]

            values = [
                str(getattr(data, attr)) 
                for attr in dir(data) 
                if not attr.startswith('__')]
            
            fileWriter = csv.writer(file, delimiter = ',', lineterminator='\r')
            file.seek(0)
            tmp = file.readline()[:-1]
            if tmp != ','.join(keys):
                fileWriter.writerow(keys)

            fileWriter.writerow(values)

def loadSimpleObjectsFromCsv(path: str) -> list[dict]:
    '''
        Загрузить простые объекты из csv файла

        Параметры:
            path (str): путь до csv файла

        Return:
            список объектов, считанных из csv файла
    '''
    myFile = Path(path)
    if myFile.is_file():
        with open(path, encoding='utf-8') as rFile:
            file_reader = csv.reader(rFile, delimiter = ",")
            keys, rows = [], []
            count = 0
            for row in file_reader:
                if count == 0: keys = row
                else: rows.append(row)
                count += 1
            
            return [dict(zip(keys, row)) for row in rows]
    
    return None