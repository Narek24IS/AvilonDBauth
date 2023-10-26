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
                self.select_cars()
            case _:
                show_error_message("Ошибка", "Такой таблицы не существует")



    def select_cars(self) -> None:
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
        self.new_window.resize(550, 280)
        # Обновление содержимого окна
        self.new_window.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = AdminWindow()
    main_window.select_cars()
    main_window.show()
