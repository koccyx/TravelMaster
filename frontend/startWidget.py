import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from registretionOrLogin import RegistrationOrLogin

class myApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/check.ui', self)
        self.setWindowTitle('Вид работы с программой')
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


