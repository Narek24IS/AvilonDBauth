from dataclasses import dataclass

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSplitter
from Admin_window import AdminWindow
from User2_window import WindowForUser2

@dataclass
class User:
    username: str
    password: str
    role: str


class PasswordWindow(QWidget):
    def __init__(self):
        # noinspection PyArgumentList
        super().__init__()

        self.__users:list[User] = [User("admin", "admin", "Admin"),
                              User("user", "user", "User")]

        self.setWindowTitle('Авторизация')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel('Имя пользователя:')
        self.username_input = QLineEdit()
        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton('Войти')
        self.login_button.clicked.connect(self.check_password)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(QSplitter(Qt.Orientation.Vertical))
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_password(self):
        username = self.username_input.text()
        password = self.password_input.text()

        for user in self.__users:
            if username == user.username and password == user.password:
                self.open_window(user.role)
                return
        self.show_error_message('Ошибка авторизации', 'Неверное имя пользователя или пароль')

    def open_window(self, role):
        match role:
            case 'Admin':
                self.close()
                window = AdminWindow()
                window.show()
            case 'User':
                self.close()
                window = WindowForUser2()
                window.show()
            case _:
                self.show_error_message('Ошибка', 'Неизвестная роль пользователя')

    @classmethod
    def show_error_message(cls, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()