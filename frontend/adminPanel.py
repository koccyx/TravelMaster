import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget
from PyQt6 import uic
from backend.base import Base
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

        self.deleteButton.clicked.connect(lambda _: self.deleteFrame.show())
        self.deleteButton.clicked.connect(lambda _: self.addFrame.hide())
        self.deleteButton.clicked.connect(lambda _: self.changeFrame.hide())
        self.deleteFrameButton.clicked.connect(lambda _: self.deleteFrame.hide())

        self.addButton.clicked.connect(lambda _: self.addFrame.show())
        self.addButton.clicked.connect(lambda _: self.changeFrame.hide())
        self.addButton.clicked.connect(lambda _: self.deleteFrame.hide())
        self.addFrameButton.clicked.connect(lambda _: self.addFrame.hide())

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











