import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget, QMessageBox
from PyQt6 import uic
from backend.base import Base
from backend.user import User
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class AdminMenu(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/adminMenu.ui', self)
        self.setWindowTitle('Меню администратора')

        for i in range(6):
            self.userTable.setColumnWidth(i,130)

        self.base = Base('backend/data/users.xlsx')

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
        self.deletionButtonFrame.clicked.connect(self.userNumberToDelete.clear)

        self.showAddFrame()
        self.additionButtonFrame.clicked.connect(lambda _: self.additionFrame.hide())
        self.additionButtonFrame.clicked.connect(self.addClicked)
        self.additionButtonFrame.clicked.connect(self.__clearAdditionFrame)

    def deleteClicked(self):
        if (self.userNumberToDelete.text() == ''):
            return
        tNumber = int(self.userNumberToDelete.text()) - 1
        self.base.delElement(tNumber)
        self.__loadData()

    def addClicked(self):
        tName = self.newName.text()
        tSurname = self.newSurname.text()
        tFatherName = self.newFatherName.text()
        tLogin = self.newLogin.text()
        tPassword = self.newPassword.text()
        tMail = self.newMail.text()
        tNewUser = User(tName, tSurname, tFatherName, tLogin, tPassword, tMail)
        self.base.addElement(tNewUser)
        self.__loadData()

    def changeClicked(self):
        if (self.userNumberToChange.text() == ''):
            return
        tNumber = int(self.userNumberToChange.text()) - 1
        tName = self.changedName.text()
        tSurname = self.changedSurname.text()
        tFatherName = self.changedFatherName.text()
        tLogin = self.changedLogin.text()
        tPassword = self.changedPassword.text()
        tMail = self.changedMail.text()
        tNewUser = User(tName, tSurname, tFatherName, tLogin, tPassword, tMail)
        self.base.changeElement(tNewUser, tNumber)
        self.__loadData()

    def completionFieldsInChangeFrame(self):
        try:
            if (len(self.base.showBaseDict()) >= int(self.userNumberToChange.text()) and int(self.userNumberToChange.text()) > 0):
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
                self.userDoesntExist()
                self.__clearChangingFrame()
        except ValueError:
            if (self.userNumberToChange.text() == ''):
                return
            self.invalidInput()
            self.__clearChangingFrame()

    def userDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Пользователя не существует.", QMessageBox.StandardButton.Ok)
        

    def invalidInput(self):
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

        # self.deleteButton.clicked.connect(deleteInterface)





        # self.deleteButton.clicked.connect(lambda _: self.number.show())

    # def deleteInterface():
    #         self.

    def __loadData(self):
        self.userTable.setRowCount(len(self.base.showBaseDict()))
        row = 0
        for person in self.base.showBaseDict():
                self.userTable.setItem(row, 0, QTableWidgetItem(person.get('Имя', 'Данные отсутствуют')))
                self.userTable.setItem(row, 1, QTableWidgetItem(person.get('Фамилия', 'Данные отсутствуют')))
                self.userTable.setItem(row, 2, QTableWidgetItem(person.get('Отчество', 'Данные отсутствуют')))
                self.userTable.setItem(row, 3, QTableWidgetItem(person.get('login', 'Данные отсутствуют')))
                self.userTable.setItem(row, 4, QTableWidgetItem(person.get('Пароль', 'Данные отсутствуют')))
                self.userTable.setItem(row, 5, QTableWidgetItem(person.get('E-mail', 'Данные отсутствуют')))
                row += 1