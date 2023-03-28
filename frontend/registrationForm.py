import sys
import os
from PyQt6.QtWidgets import QWidget, QLineEdit
from PyQt6 import uic
import pandas as pd
from backend.user import User
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class RegistrationFrom(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/registration.ui', self)
        self.setWindowTitle('Регистрация')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.registrationButton.clicked.connect(self.createNewUser)#passwordInput.text()

    def createNewUser(self):
        newUser = User(self.nameInput.text(), self.secondNameInput.text(), self.surnameInput.text(), self.loginInput.text(), self.passwordInput.text(), self.emailInput.text())

        temp = pd.read_excel('backend/data/users.xlsx', index_col=0).to_dict('records')

        for user in temp:
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

        newUser.save()
        print('registration confirmed')


