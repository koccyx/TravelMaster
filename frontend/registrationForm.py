from msilib.schema import File
import sys
import os
from PyQt6.QtWidgets import QWidget, QLineEdit, QMessageBox
from PyQt6 import uic
import pandas as pd
from backend.user import User
from backend.userBase import UserBase
from userPanel import UserMenu
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import json


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

    def writeToJson(self, filename):
        with open(filename, 'r') as file:
            users = json.load(file)
        users[str(self.loginInput.text())] = []
        users = json.dumps(users, ensure_ascii = False)
        users = json.loads(str(users))
        with open(filename, 'w') as file:
            json.dump(users, file, indent = 4)

    def __fillError(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Не все поля заполнены.", QMessageBox.StandardButton.Ok)

    def createNewUser(self):
        if str(self.nameInput.text()) == '' or str(self.secondNameInput.text()) == '' or str(self.surnameInput.text()) == '' or str(self.loginInput.text()) == '' or str(self.passwordInput.text()) == '' or str(self.emailInput.text()) == '':
            self.__fillError()
            return
        else:
            newUser = User(str(self.nameInput.text()), str(self.secondNameInput.text()), str(self.surnameInput.text()), str(self.loginInput.text()), str(self.passwordInput.text()), str(self.emailInput.text()))

            tempBase = UserBase()


            for user in tempBase.showBaseDict():
                if str(user['Имя']) == str(self.nameInput.text()) and str(user['Фамилия']) == str(self.secondNameInput.text()) and str(user['Отчество']) == str(self.nameInput.text()):
                    self.errorsLabel1.setText('Пользователь с таким')
                    self.errorsLabel2.setText('именем уже существует')
                    return
                elif str(user['login']) == str(self.loginInput.text()):
                    self.errorsLabel1.setText('Пользователь с таким')
                    self.errorsLabel2.setText('логином уже существует')
                    return
                elif str(user['E-mail']) == str(self.emailInput.text()):
                    self.errorsLabel1.setText('Пользователь с такой')
                    self.errorsLabel2.setText('почтой уже существует')
                    return

            tempBase.addElement(newUser)
            self.writeToJson('backend/Tickets.json')
            self.openUserPanel(newUser)

        



