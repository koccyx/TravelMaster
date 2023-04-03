import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget
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

        self.changeFrame.hide()
        self.deleteFrame.hide()
        self.addFrame.hide()

        self.changeButton.clicked.connect(lambda _: self.changeFrame.show())
        self.changeButton.clicked.connect(lambda _: self.deleteFrame.hide())
        self.changeButton.clicked.connect(lambda _: self.addFrame.hide())
        self.changeFrameButton.clicked.connect(lambda _: self.changeFrame.hide())
        self.changeFrameButton.clicked.connect(self.change_clicked)
        self.changeFrameButton.clicked.connect(self.number.clear)
        self.changeFrameButton.clicked.connect(self.name.clear)
        self.changeFrameButton.clicked.connect(self.lastName.clear)
        self.changeFrameButton.clicked.connect(self.surName.clear)
        self.changeFrameButton.clicked.connect(self.login.clear)
        self.changeFrameButton.clicked.connect(self.password.clear)
        self.changeFrameButton.clicked.connect(self.mail.clear)

        self.deleteButton.clicked.connect(lambda _: self.deleteFrame.show())
        self.deleteButton.clicked.connect(lambda _: self.addFrame.hide())
        self.deleteButton.clicked.connect(lambda _: self.changeFrame.hide())
        self.deleteFrameButton.clicked.connect(lambda _: self.deleteFrame.hide())
        self.deleteFrameButton.clicked.connect(self.delete_clicked)
        self.deleteFrameButton.clicked.connect(self.change.clear)

        self.addButton.clicked.connect(lambda _: self.addFrame.show())
        self.addButton.clicked.connect(lambda _: self.changeFrame.hide())
        self.addButton.clicked.connect(lambda _: self.deleteFrame.hide())
        self.addFrameButton.clicked.connect(lambda _: self.addFrame.hide())
        self.addFrameButton.clicked.connect(self.add_clicked)
        self.addFrameButton.clicked.connect(self.addName.clear)
        self.addFrameButton.clicked.connect(self.addsecondName.clear)
        self.addFrameButton.clicked.connect(self.addSurName.clear)
        self.addFrameButton.clicked.connect(self.addLogin.clear)
        self.addFrameButton.clicked.connect(self.addPassword.clear)
        self.addFrameButton.clicked.connect(self.addMail.clear)

    def delete_clicked(self):
        num = int(self.change.text()) - 1
        self.base.delElement(num)
        self.__loadData()

    def add_clicked(self):
        tName = self.addName.text()
        tSecondname = self.addsecondName.text()
        tSurname = self.addSurName.text()
        tLogin = self.addLogin.text()
        tPassword = self.addPassword.text()
        tMail = self.addMail.text()
        tNewUser = User(tName, tSecondname, tSurname, tLogin, tPassword, tMail)
        self.base.addElement(tNewUser)
        self.__loadData()

    def change_clicked(self):
        tNumber = int(self.number.text()) - 1
        tName = self.name.text()
        tSecondname = self.lastName.text()
        tSurname = self.surName.text()
        tLogin = self.login.text()
        tPassword = self.password.text()
        tMail = self.mail.text()
        tNewUser = User(tName, tSecondname, tSurname, tLogin, tPassword, tMail)
        self.base.changeElement(tNewUser, tNumber)
        self.__loadData()

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











