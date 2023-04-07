import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget, QMessageBox
from PyQt6 import uic
from backend.userBase import UserBase
from backend.user import User
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class AdminMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/adminMenu.ui', self)
        self.setWindowTitle('Меню администратора')

        for i in range(6):
            self.userTable.setColumnWidth(i,130)

        self.base = UserBase()

        self.__loadData()

        self.changedFrame.hide()
        self.deletionFrame.hide()
        self.additionFrame.hide()

        self.showChangeFrame()
        self.changedButtonFrame.clicked.connect(lambda _: self.changedFrame.hide())
        self.changedButtonFrame.clicked.connect(self.changeClicked)
        self.changedButtonFrame.clicked.connect(self.__clearChangingFrame)
        self.userNumberToChange.textChanged.connect(self.completionFieldsInChangeFrame)

        self.showDeleteFrame()
        self.deletionButtonFrame.clicked.connect(lambda _: self.deletionFrame.hide())
        self.deletionButtonFrame.clicked.connect(self.deleteClicked)
        self.deletionButtonFrame.clicked.connect(self.__clearDeletionFrame)
        self.userNumberToDelete.textChanged.connect(self.completionFieldsInDeleteFrame)

        self.showAddFrame()
        self.additionButtonFrame.clicked.connect(lambda _: self.additionFrame.hide())
        self.additionButtonFrame.clicked.connect(self.addClicked)
        self.additionButtonFrame.clicked.connect(self.__clearAdditionFrame)

    def deleteClicked(self):
        try:
            if len(self.base.showBaseDict()) >= int(self.userNumberToDelete.text()) and int(self.userNumberToDelete.text()) > 0:
                tNumber = int(self.userNumberToDelete.text()) - 1
                self.base.delElement(tNumber)
                self.__loadData()
            else:
                self.__userDoesntExist()
                self.__clearDeleteFrame()
        except ValueError:
            if (self.userNumberToDelete.text() == ''):
                return
            self.__invalidInput()
            self.__clearDeleteFrame()


    def addClicked(self):
        tName = self.newName.text()
        if (tName == ''):
            self.__invalidInput()
            return
        tSurname = self.newSurname.text()
        if (tSurname == ''):
            self.__invalidInput()
            return
        tFatherName = self.newFatherName.text()
        if (tFatherName == ''):
            self.__invalidInput()
            return
        tLogin = self.newLogin.text()
        if (tLogin == ''):
            self.__invalidInput()
            return
        tPassword = self.newPassword.text()
        if (tPassword == ''):
            self.__invalidInput()
            return
        tMail = self.newMail.text()
        if (tMail == ''):
            self.__invalidInput()
            return
        tNewUser = User(tName, tSurname, tFatherName, tLogin, tPassword, tMail)
        self.base.addElement(tNewUser)
        self.__loadData()

    def changeClicked(self):
        if self.userNumberToChange.text() == '':
            return
        tNumber = int(self.userNumberToChange.text()) - 1
        tName = self.changedName.text()
        if (tName == ''):
            self.__invalidInput()
            return
        tSurname = self.changedSurname.text()
        if (tSurname == ''):
            self.__invalidInput()
            return
        tFatherName = self.changedFatherName.text()
        if (tFatherName == ''):
            self.__invalidInput()
            return
        tLogin = self.changedLogin.text()
        if (tLogin == ''):
            self.__invalidInput()
            return
        tPassword = self.changedPassword.text()
        if (tPassword == ''):
            self.__invalidInput()
            return
        tMail = self.changedMail.text()
        if (tMail == ''):
            self.__invalidInput()
            return
        tNewUser = User(tName, tSurname, tFatherName, tLogin, tPassword, tMail)
        self.base.changeElement(tNewUser, tNumber)
        self.__loadData()

    def completionFieldsInDeleteFrame(self):
        try:
            if len(self.base.showBaseDict()) >= int(self.userNumberToDelete.text()) and int(self.userNumberToDelete.text()) > 0:
                tNumber = int(self.userNumberToDelete.text())
            else:
                self.__userDoesntExist()
                self.__clearDeletionFrame()
        except ValueError:
            if (self.userNumberToDelete.text() == ''):
                return
            self.__invalidInput()
            self.__clearDeletionFrame()

    def completionFieldsInChangeFrame(self):
        try:
            if len(self.base.showBaseDict()) >= int(self.userNumberToChange.text()) and int(self.userNumberToChange.text()) > 0:
                tNumber = int(self.userNumberToChange.text()) - 1
                tName = self.base.showBaseDict()[tNumber]['Имя']
                tSurname = self.base.showBaseDict()[tNumber]['Фамилия']
                tFatherName = self.base.showBaseDict()[tNumber]['Отчество']
                tLogin = self.base.showBaseDict()[tNumber]['login']
                tPassword = self.base.showBaseDict()[tNumber]['Пароль']
                tMail = self.base.showBaseDict()[tNumber]['E-mail']
                self.changedName.setText(tName)
                self.changedSurname.setText(tSurname)
                self.changedFatherName.setText(tFatherName)
                self.changedLogin.setText(tLogin)
                self.changedPassword.setText(tPassword)
                self.changedMail.setText(tMail)
            else:
                self.__userDoesntExist()
                self.__clearChangingFrame()
        except ValueError:
            if (self.userNumberToChange.text() == ''):
                return
            self.__invalidInput()
            self.__clearChangingFrame()

    def userDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Пользователя не существует.", QMessageBox.StandardButton.Ok)


    def __invalidInput(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Некорректный ввод.", QMessageBox.StandardButton.Ok)

    def showChangeFrame(self):
        self.changedButton.clicked.connect(lambda _: self.changedFrame.show())
        self.changedButton.clicked.connect(lambda _: self.deletionFrame.hide())
        self.changedButton.clicked.connect(lambda _: self.additionFrame.hide())

    def showDeleteFrame(self):
        self.deletionButton.clicked.connect(lambda _: self.deletionFrame.show())
        self.deletionButton.clicked.connect(lambda _: self.additionFrame.hide())
        self.deletionButton.clicked.connect(lambda _: self.changedFrame.hide())

    def showAddFrame(self):
        self.additionButton.clicked.connect(lambda _: self.additionFrame.show())
        self.additionButton.clicked.connect(lambda _: self.changedFrame.hide())
        self.additionButton.clicked.connect(lambda _: self.deletionFrame.hide())

    def __clearChangingFrame(self):
        self.userNumberToChange.clear()
        self.changedName.clear()
        self.changedSurname.clear()
        self.changedFatherName.clear()
        self.changedLogin.clear()
        self.changedPassword.clear()
        self.changedMail.clear()

    def __clearAdditionFrame(self):
        self.newName.clear()
        self.newSurname.clear()
        self.newFatherName.clear()
        self.newLogin.clear()
        self.newPassword.clear()
        self.newMail.clear()

    def __clearDeletionFrame(self):
        self.userNumberToDelete.clear()

    def __loadData(self):
        self.userTable.setRowCount(len(self.base.showBaseDict()))
        row = 0
        for person in self.base.showBaseDict():
                self.userTable.setItem(row, 0, QTableWidgetItem(person.get('Имя', 'Данные отсутствуют')))
                self.userTable.setItem(row, 1, QTableWidgetItem(person.get('Фамилия', 'Данные отсутствуют')))
                self.userTable.setItem(row, 2, QTableWidgetItem(person.get('Отчество', 'Данные отсутствуют')))
                self.userTable.setItem(row, 3, QTableWidgetItem(person.get('E-mail', 'Данные отсутствуют')))
                self.userTable.setItem(row, 4, QTableWidgetItem(person.get('login', 'Данные отсутствуют')))
                self.userTable.setItem(row, 5, QTableWidgetItem(person.get('Пароль', 'Данные отсутствуют')))
                row += 1
