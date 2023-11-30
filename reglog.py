import sys
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel
from PyQt6 import QtCore

from reglog_ui import Ui_MainWindow
from Car_window import CarWindow
from Market_window import MarkWindow
from database import db


class Registration(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText('')
        self.label_2.setText('Регистрация')
        self.lineEdit.setPlaceholderText('Введите Логин')
        self.lineEdit_2.setPlaceholderText('Введите Пароль')
        self.pushButton.setText('Регистрация')
        self.pushButton_2.setText('Вход')
        self.add_roles_to_cb()
        self.setWindowTitle('Регистрация')

        self.pushButton.pressed.connect(self.reg)
        self.pushButton_2.pressed.connect(self.login)

        self.db = db
        self.query:QSqlQuery = QSqlQuery()

    def add_roles_to_cb(self):
        self.role_label = QLabel(self.centralwidget)
        self.role_label.setText('Выберите роль')
        self.role_label.setStyleSheet("color: white;")
        self.role_label.setGeometry(QtCore.QRect(25, 20, 110, 30))

        self.roles_cb = QComboBox(self.centralwidget)
        self.roles_cb.addItem('car', 'car')
        self.roles_cb.
        self.roles_cb.addItem('market', 'market')
        self.roles_cb.setGeometry(QtCore.QRect(25, 50, 110, 30))
        self.roles_cb.setStyleSheet("color: white;")

    def login(self):
        self.login = Login()
        self.login.show()
        self.hide()

    def reg(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        user_role = self.roles_cb.currentText()

        if len(user_login) == 0:
            self.label.setText('Поле логина не должно быть пустым!')
            return

        if len(user_password) == 0:
            self.label.setText('Поле пароля не должно быть пустым!')
            return

        self.query.exec(f'SELECT login FROM users WHERE login="{user_login}"')
        self.query.first()
        if self.query.value(0) is None:
            self.query.exec(f'INSERT INTO users '
                            f'VALUES ("{user_login}", "{user_password}", "{user_role}")')
            self.label.setText(f'Аккаунт {user_login} успешно зарегистрирован!')
        else:
            self.label.setText('Такой пользователь уже зарегистрирован!')


class Login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.label.setText('')
        self.label_2.setText('Логин')
        self.lineEdit.setPlaceholderText('Введите логин')
        self.lineEdit_2.setPlaceholderText('Введите пароль')
        self.pushButton.setText('Вход')
        self.pushButton_2.setText('Регистрация')
        self.setWindowTitle('Вход')

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.reg)

        self.query:QSqlQuery = QSqlQuery()
        self.db = db


    def reg(self):
        self.reg = Registration()
        self.reg.show()
        self.hide()

    def login(self):
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            self.label.setText('Поле логина не должно быть пустым!')
            return

        if len(user_password) == 0:
            self.label.setText('Поле пароля не должно быть пустым!')
            return

        self.query.exec(f'SELECT login, password, role FROM users WHERE login="{user_login}"')
        if self.query.first():
            role = self.query.value(2)
            check_pass = self.query.value(1) == user_password
            print(role)
            if check_pass:
                match role:
                    case 'car':
                        self.label.setText('Успешная авторизация!')
                        new_window = CarWindow() # Здесь вставляете свой класс,
                                                 # который отвечает за новое окно для данной роли
                        new_window.show()
                    case 'market':
                        self.label.setText('Успешная авторизация!')
                        new_window = MarkWindow() # Здесь вставляете свой класс,
                                                  # который отвечает за новое окно для данной роли
                        new_window.show()
                    case _:
                        self.label.setText('Ошибка авторизации!')
            else:
                self.label.setText('Неправильный пароль!')
        else:
            self.label.setText('Нет такого пользователя!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Login()
    main_window.show()
    sys.exit(app.exec())