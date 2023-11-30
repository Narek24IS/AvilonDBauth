import sys
from contextlib import contextmanager
from PyQt6 import QtCore
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QMessageBox

from addit_windows import show_error_message


class DBConnect:
    def __init__(self, db_name:str='Avilon', login:str='root', password:str='root',
                 host:str='localhost', port:int=3306):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setUserName(login)
        db.setPassword(password)
        db.setDatabaseName(db_name)
        db.setHostName(host)
        db.setPort(port)

        if not db.open():
            QMessageBox.critical(
                None,
                "App Name - Error!",
                "Database Error: %s" % db.lastError().databaseText(),
                )
            # show_error_message('Ошибка подключения', db.lastError().databaseText())
            sys .exit(1)

    def get_query(self):
        return QSqlQuery()

    # def get_full_table(self, table_name:str) -> list[Car]:
    #     with self.__session_scope() as s:
    #         match table_name.lower():
    #             case 'brand' | 'brands':
    #                 return s.query(Brand).all()
    #             case 'car' | 'cars':
    #                 return s.query(Car).all()
    #             case 'company' | 'result' | 'results' | 'company results' | 'company result':
    #                 return s.query(Company_Results).all()
    #             case 'employee' | 'employees':
    #                 return s.query(Employee).all()
    #             case 'position' | 'positions':
    #                 return s.query(Position).all()
    #             case 'salary' | 'payment' | 'payments' | 'salary payment' | 'salary payments':
    #                 return s.query(Salary_payment).all()
    #             case 'sale' | 'sales':
    #                 return s.query(Sales).all()
    #             case _:
    #                 return []
    #
    # def test(self):
    #     with self.__session_scope() as s:
    #         s.query(Sales).all()

if __name__ == '__main__':
    db = DBConnect('AvilonN', 'hikinari', '68ee3e138', host='localhost', port=3306)
    # db("create table sportsmen(id int primary key, "
    #    "firstname varchar(20), lastname varchar(20))")
