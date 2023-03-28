import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6 import uic
sys.path.append('..')
from backend.ticket import Ticket


class RegistrationOrLogin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/RoL.ui', self)
        self.setWindowTitle('Логин или регистрация')
        self.loginButton.clicked.connect(self.openLoginWindow)
        self.registrationButton.clicked.connect(self.openRegistrationForm)

    def openLoginWindow(self):
        self.loginApp = LoginFrom()
        self.loginApp.show()
        self.close()

    def openRegistrationForm(self):
        self.registrationApp = RegistrationFrom()
        self.registrationApp.show()
        self.close()


class LoginFrom(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/LoginForm.ui', self)
        self.setWindowTitle('Вход')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

class RegistrationFrom(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/registration.ui', self)
        self.setWindowTitle('Регистрация')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.registrationButton.clicked.connect(self.printText)

    def printText(self):
        print(self.passwordInput.text())


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




