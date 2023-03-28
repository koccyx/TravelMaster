import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from backend.ticket import Ticket




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








