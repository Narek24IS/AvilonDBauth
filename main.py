import sys
from PyQt6.QtWidgets import QApplication
from password_window import User, PasswordWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PasswordWindow()
    main_window.show()
    sys.exit(app.exec())