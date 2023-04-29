# coding=windows-1251
import sys
import os
from PyQt6.QtWidgets import  QWidget, QLineEdit, QMessageBox
from PyQt6 import uic
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from backend.user import User
from backend.userBase import UserBase
from userPanel import UserMenu





class ChangePassword(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/changePassword.ui', self)
        self.changePasswordButton.clicked.connect(self.__changePasswordButtonClicked)
        self.backButton.clicked.connect(self.close)
        
        self.oldPasswordInChangePassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.newPasswordInChangePassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.repeatNewPasswordInChangePassword.setEchoMode(QLineEdit.EchoMode.Password)

    def __changePasswordButtonClicked(self):
        self.login = self.loginInChangePassword.text()
        self.oldPassword = self.oldPasswordInChangePassword.text()
        self.newPassword = self.newPasswordInChangePassword.text()
        self.repeatNewPassword = self.repeatNewPasswordInChangePassword.text()
        self.backButton.clicked.connect(self.close)



        if (self.login == '' or self.oldPassword == '' or self.newPassword == '' or self.repeatNewPassword == ''):
            self.__fillError()
            return

        if (self.newPassword != self.repeatNewPassword):
            self.__passwordError()
            return

        exist = False
        tempBase = UserBase()

        for user in tempBase.showBaseDict():
            if (user['login'] == self.login and user['Пароль'] == self.oldPassword):
                exist = True

        if (exist == False):
            self.__userDoesntExist()
            return


        self.base = UserBase()
        num = 0
        for user in tempBase.showBaseDict():
            if (user['login'] == self.login and user['Пароль'] == self.oldPassword):
                user['Пароль'] = self.newPassword
                tNewUser = User(user['Имя'], user['Фамилия'], user['Отчество'], user['login'], user['Пароль'], user['E-mail'])
                self.base.changeElement(tNewUser, num)
            num += 1

        self.__access()
        self.close()

    def __userDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Пользователь с таким логином не существует.", QMessageBox.StandardButton.Ok)

    def __passwordError(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", 'Поле "Новый пароль" не соответствует полю "Повторить новый пароль".', QMessageBox.StandardButton.Ok)


    def __access(self):
        self.msgbox = QMessageBox.warning(self, "Изменение пароля", "Пароль изменён.", QMessageBox.StandardButton.Ok)
        
    def __fillError(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Не все поля заполнены.", QMessageBox.StandardButton.Ok)