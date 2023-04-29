import sys
import os
from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6 import uic
import pandas as pd
from backend.user import User
from backend.userBase import UserBase
from userPanel import UserMenu
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class RegistrationFrom(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/registration.ui', self)
        self.setWindowTitle('Регистрация')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.registrationButton.clicked.connect(self.createNewUser)#passwordInput.text()
        self.backButton.clicked.connect(self.__goBack)

    def __goBack(self):
        from registretionOrLogin import RegistrationOrLogin
        self.backWidget = RegistrationOrLogin()
        self.backWidget.show()
        self.close()

    def openUserPanel(self,user):
        self.userPanel = UserMenu(user)
        self.userPanel.show()
        self.close()

    def createNewUser(self):
        newUser = User(self.nameInput.text(), self.secondNameInput.text(), self.surnameInput.text(), self.loginInput.text(), self.passwordInput.text(), self.emailInput.text())

        tempBase = UserBase()


        for user in tempBase.showBaseDict():
            if user['Имя'] == self.nameInput.text() and user['Фамилия'] == self.secondNameInput.text() and user['Отчество'] == self.nameInput.text():
                self.errorsLabel1.setText('Пользователь с таким')
                self.errorsLabel2.setText('именем уже существует')
                print('this user is already exist')
                return
            elif user['login'] == self.loginInput.text():
                self.errorsLabel1.setText('Пользователь с таким')
                self.errorsLabel2.setText('логином уже существует')
                print('Invalid login')
                return
            elif user['E-mail'] == self.emailInput.text():
                self.errorsLabel1.setText('Пользователь с такой')
                self.errorsLabel2.setText('почтой уже существует')
                print('Invalid e-mail')
                return

        tempBase.addElement(newUser)
        self.openUserPanel(newUser)
        print('registration confirmed')


