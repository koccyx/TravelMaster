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
        self.login = str(self.loginInChangePassword.text())
        self.oldPassword = str(self.oldPasswordInChangePassword.text())
        self.newPassword = str(self.newPasswordInChangePassword.text())
        self.repeatNewPassword = str(self.repeatNewPasswordInChangePassword.text())

        if (self.login == '' or self.oldPassword == '' or self.newPassword == '' or self.repeatNewPassword == ''):
            self.__fillError()
            return

        if (self.newPassword != self.repeatNewPassword):
            self.__passwordError()
            return

        exist = False
        tempBase = UserBase()

        for user in tempBase.showBaseDict():
            if (str(user['login']) == self.login and str(user['Пароль']) == self.oldPassword):
                exist = True
                break

        if (exist == False):
            self.__userDoesntExist()
            return


        self.base = UserBase()
        num = 0
        for user in tempBase.showBaseDict():
            if (str(user['login']) == self.login and str(user['Пароль']) == self.oldPassword):
                user['Пароль'] = self.newPassword
                tNewUser = User(str(user['Имя']), str(user['Фамилия']), str(user['Отчество']), str(user['login']), str(user['Пароль']), str(user['E-mail']))
                self.base.changeElement(num, 'Пароль', self.newPassword)
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