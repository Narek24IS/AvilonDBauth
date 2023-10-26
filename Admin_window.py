import sys

from PyQt6.QtWidgets import QWidget, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QApplication
from ORMModels import Car, Brand
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from DBConnect import DBConnect


class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Создание окна
        self.new_window = QDialog(self)
        self.new_window.setWindowTitle('Окно админа')
        self.new_window.setGeometry(300, 300, 500, 200)
        # Создание таблицы
        self.table_widget = QTableWidget()
        self.layout = QVBoxLayout()
        self.db = DBConnect('hikinari', '68ee3e138', 'AvilonN')

        self.layout.addWidget(self.table_widget)
        self.new_window.setLayout(self.layout)

        self.new_window.exec()

    def select_cars(self):
        # Получение результата запроса
        results = [x.get_info() for x in self.db.get_cars()]

        # Количество столбцов и строк
        self.table_widget.setRowCount(len(results))
        self.table_widget.setColumnCount(len(results[0])-1)
        # Заголовок
        column_headers = ['brand', 'model', 'complectation', 'fuel', 'year',
                          'price', 'color']
        self.table_widget.setHorizontalHeaderLabels(column_headers)
        # Заполнение таблицы
        for row, result in enumerate(results):
            for column, value in enumerate(result[1:]):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, column, item)
        # Изменение размеров строк и столбцов
        self.table_widget.resizeColumnsToContents()
        # self.table_widget.resizeRowsToContents()
        # Изменение размера окна под таблицу


        self.table_widget.updateGeometries()
        print(self.table_widget.sizeHint().width(), self.table_widget.sizeHint().height())
        # 1 строка - 30 пикселей
        self.new_window.resize(550, 230)
        self.new_window.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = AdminWindow()
    main_window.select_cars()
    main_window.show()
