import sys
import os
from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class RegistrationFrom(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/registration.ui', self)
        self.setWindowTitle('Регистрация')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.registrationButton.clicked.connect(self.printText)

    def printText(self):
        print(self.passwordInput.text())
