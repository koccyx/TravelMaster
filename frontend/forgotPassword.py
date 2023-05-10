# coding=windows-1251
import sys
import os
from PyQt6.QtWidgets import  QWidget, QLineEdit, QMessageBox
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from backend.user import User
from backend.userBase import UserBase
from userPanel import UserMenu
import random





class ForgotPassword(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/forgotPassword.ui', self)
        self.backButton.clicked.connect(self.close)
        self.code = random.randint(1000, 10000)
        self.checkCode.setNum(self.code)

        self.access.clicked.connect(self.__accessClicked)

    def __accessClicked(self):
        if (self.enterLogin.text() == '') or (self.enterCode.text() == ''):
            self.__fillError()
            return

        try:
            tCode = int(self.enterCode.text())
            tLogin = str(self.enterLogin.text())
            exist = False
            tempBase = UserBase()

            for user in tempBase.showBaseDict():
                if (str(user['login']) == tLogin):
                    exist = True
                    break

            if (exist == False):
                self.__userDoesntExist()
                return

            if (tCode == self.code):
                self.base = UserBase()
                num = 0
                for user in tempBase.showBaseDict():
                    if (str(user['login']) == tLogin):
                        user['Пароль'] = '0000'
                        tNewUser = User(str(user['Имя']), str(user['Фамилия']), str(user['Отчество']), str(user['login']), str(user['Пароль']), str(user['E-mail']))
                        self.base.changeElement(num, 'Пароль', '0000')
                    num += 1
                self.__access()
                self.close()

            else:
                self.__enterCodeError()
                self.enterCode.clear()

        except ValueError:
            self.__invalidInput()
            self.enterCode.clear()
         
    def __access(self):
        self.msgbox = QMessageBox.warning(self, "Изменение пароля", "Пароль изменён на стандартный. Узнать его можете у администратора.", QMessageBox.StandardButton.Ok)

    def __userDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Пользователь с таким логином не существует.", QMessageBox.StandardButton.Ok)

    def __enterCodeError(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Неправильно введён код.", QMessageBox.StandardButton.Ok)

    def __invalidInput(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Некорректный ввод.", QMessageBox.StandardButton.Ok)

    def __fillError(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Не все поля заполнены.", QMessageBox.StandardButton.Ok)