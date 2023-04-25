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

    def __changePasswordButtonClicked(self):
        self.login = self.loginInChangePassword.text()
        self.oldPassword = self.oldPasswordInChangePassword.text()
        self.newPassword = self.newPasswordInChangePassword.text()
        self.repeatNewPassword = self.repeatNewPasswordInChangePassword.text()

        if (self.login == '' or self.oldPassword == '' or self.newPassword == '' or self.repeatNewPassword == ''):
            self.__fillError()
            return

        if (self.newPassword != self.repeatNewPassword):
            self.__passwordError()
            return

        exist = False
        tempBase = UserBase()

        for user in tempBase.showBaseDict():
            if (user['login'] == self.login and user['������'] == self.oldPassword):
                exist = True

        if (exist == False):
            self.__ticketDoesntExist()
            return


        self.base = UserBase()
        num = 0
        for user in tempBase.showBaseDict():
            if (user['login'] == self.login and user['������'] == self.oldPassword):
                user['������'] = self.newPassword
                tNewUser = User(user['���'], user['�������'], user['��������'], user['login'], user['������'], user['E-mail'])
                self.base.changeElement(tNewUser, num)
            num += 1

    def __ticketDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "������", "������������ � ����� ������� �� ����������.", QMessageBox.StandardButton.Ok)

    def __passwordError(self):
        self.msgbox = QMessageBox.warning(self, "������", '���� "����� ������" �� ������������� ���� "��������� ����� ������".', QMessageBox.StandardButton.Ok)

    def __fillError(self):
        self.msgbox = QMessageBox.warning(self, "������", "�� ��� ���� ���������.", QMessageBox.StandardButton.Ok)