import sys
import os
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from loginForm import LoginFrom
from registrationForm import RegistrationFrom



class RegistrationOrLogin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/RoL.ui', self)
        self.setWindowTitle('Логин или регистрация')
        self.loginButton.clicked.connect(self.openLoginWindow)
        self.registrationButton.clicked.connect(self.openRegistrationForm)
        self.backButton.clicked.connect(self.goBack)



    def goBack(self):
        from startWidget import myApp
        self.backWidget = myApp()
        self.backWidget.show()
        self.close()

    def openLoginWindow(self):
        self.loginWidget = LoginFrom()
        self.loginWidget.show()
        self.close()

    def openRegistrationForm(self):
        self.registrationWidget = RegistrationFrom()
        self.registrationWidget.show()
        self.close()

