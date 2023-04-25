import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from registretionOrLogin import RegistrationOrLogin
from adminPanel import AdminMenu

class myApp(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('frontend/ui/check.ui', self)
        self.setWindowTitle('Вид работы c программой')


        self.userButton.clicked.connect(self.openRoLWindow)
        self.adminButton.clicked.connect(self.openAdminPanel)

    def openRoLWindow(self):
        self.registrationWidget = RegistrationOrLogin()
        self.registrationWidget.show()
        self.close()

    def openAdminPanel(self):
        self.adminWidget = AdminMenu()
        self.adminWidget.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    newApp = myApp()
    newApp.show()

    sys.exit(app.exec())


