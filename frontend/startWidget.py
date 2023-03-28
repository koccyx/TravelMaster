import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from registretionOrLogin import RegistrationOrLogin

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/check.ui', self)
        self.setWindowTitle('Выбор пользователя')
        self.userButton.clicked.connect(self.openRoLWindow)

    def openRoLWindow(self):
        self.app2 = RegistrationOrLogin()
        self.app2.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    newApp = myApp()
    newApp.show()

    sys.exit(app.exec())


