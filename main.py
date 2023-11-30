import sys
from PyQt6.QtWidgets import QApplication
from reglog import Login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Login()
    main_window.show()
    sys.exit(app.exec())