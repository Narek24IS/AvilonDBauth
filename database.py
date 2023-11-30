import sys

from PyQt6.QtSql import QSqlQuery, QSqlDatabase


def db_connect(db_name:str = 'MyDatabase') -> QSqlDatabase:
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_name)
    query = QSqlQuery()

    if not db.open():
        print(f"Database Error: {db.lastError().databaseText()}")
        sys.exit(1)

    query.exec('''CREATE TABLE IF NOT EXISTS users(
                login TEXT,
                password TEXT,
                role TEXT
            )''')

    return db


db = db_connect('AvilonN')