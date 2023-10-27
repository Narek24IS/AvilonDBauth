from typing import Union
from PyQt6.QtWidgets import QWidget, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QApplication, QPushButton, \
    QHBoxLayout, QLineEdit, QFrame
from DBConnect import DBConnect
from addit_windows import show_error_message
from env_data import login, password, db_name
import sys


class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_content()
        self.new_window.exec()

    def create_content(self) -> None:
        # Окно
        self.new_window = QDialog(self)
        self.new_window.setWindowTitle('Окно админа')
        self.new_window.resize(550, 230)

        # Таблицы
        self.table_widget = QTableWidget()
        self.db = DBConnect(login, password, db_name)

        # Кнопка
        self.get_button = QPushButton('Get')
        self.get_button.clicked.connect(self.process_request)

        # Поле ввода
        self.req = QLineEdit()

        # Компоновка кнопки и поля
        self.frame = QFrame()
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.get_button)
        self.hlayout.addWidget(self.req)
        self.frame.setLayout(self.hlayout)

        # Общая компоновка
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table_widget)
        self.layout.addWidget(self.frame)
        self.new_window.setLayout(self.layout)

    def process_request(self) -> None:
        request = self.req.text()

        match request.lower():
            case 'car':
                self.select_all(request)
            case _:
                show_error_message("Ошибка", "Такой таблицы не существует")

    def select_all(self, table_name:str) -> None:
        # Получение результата запроса
        table:list = self.db.get_full_table(table_name.lower())
        if not table:
            show_error_message("Ошибка", "Такой таблицы не существует")
            return
        results = [x.get_info() for x in table]

        # Количество столбцов и строк
        row = len(results)
        col = len(results[0])
        self.table_widget.setRowCount(row)
        self.table_widget.setColumnCount(col)

        # Заголовок
        column_headers = table[0].get_headers()
        self.table_widget.setHorizontalHeaderLabels(column_headers)
        self.table_widget.horizontalHeader().setStretchLastSection(True)

        # Изменение размера окна под таблицу
        height = 90+row*35 # 80 - button, 35 - 1 row
        str_rows = [(str(cell) for cell in line) for line in results]
        max_row = sum(max((len(st) for st in col)) for col in zip(*str_rows))+col
        max_header = len(' '.join((str(x) for x in column_headers)))+col
        width = max(max_row, max_header)*9+100
        self.new_window.resize(width, height)

        # Заполнение таблицы
        for row, result in enumerate(results):
            for column, value in enumerate(result):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, column, item)

        # Изменение размеров строк и столбцов
        self.table_widget.resizeColumnsToContents()
        # self.table_widget.resizeRowsToContents()

        # Обновление содержимого окна
        self.new_window.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = AdminWindow()
    main_window.show()
