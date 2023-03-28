import sys
import os
from PyQt6.QtWidgets import  QWidget, QLineEdit
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from backend.user import User
import pandas as pd




class LoginFrom(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/LoginForm.ui', self)
        self.setWindowTitle('Вход')
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.inputButton.clicked.connect(self.checkLogin)

    def checkLogin(self):

        temp = pd.read_excel('backend/data/users.xlsx', index_col=0).to_dict('records')

        for user in temp:
            if user['login'] == self.loginInput.text() and user['Пароль'] == self.passwordInput.text():
                self.errorLabel1.setText('Отлично')
                self.errorLabel2.setText('')
                return
            elif user['login'] == self.loginInput.text() and user['Пароль'] != self.passwordInput.text():
                self.errorLabel1.setText('Вы ввели')
                self.errorLabel2.setText('неправильный пароль')
                return
            else:
                self.errorLabel1.setText('Нет пользователя')
                self.errorLabel2.setText('с таким именем')




