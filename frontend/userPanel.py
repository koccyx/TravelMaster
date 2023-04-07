import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget, QMessageBox
from PyQt6 import uic
from backend.ticketBase import TicketBase
from backend.user import User
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class UserMenu(QWidget):
    def __init__(self, user):
        super().__init__()
        uic.loadUi('frontend/ui/userMenu.ui', self)
        self.setWindowTitle('Меню пользователя')

        self.user = user

        for i in range(6):
            self.ticketTable.setColumnWidth(i,130)

        self.ticketBase = TicketBase()

        self.__loadData()

        self.buyFrame.hide()

        self.buyButton.clicked.connect(lambda _ : self.buyFrame.show())

        self.frameBuyButton.clicked.connect(self.__ticketBuy)

    def __ticketBuy(self):
        for ticket in self.ticketBase.objectBase:
            if int(ticket.id) == int(self.buyLine.text()):
                print('yep')
                self.user.buyTicket(ticket)
        print(self.user.ticketCart)



    def __loadData(self):
        self.ticketTable.setRowCount(len(self.ticketBase.showBaseDict()))
        row = 0
        for ticket in self.ticketBase.showBaseDict():
                print(ticket)
                self.ticketTable.setItem(row, 0, QTableWidgetItem(str(ticket.get('id', 'Данные отсутствуют'))))
                self.ticketTable.setItem(row, 1, QTableWidgetItem(ticket.get('Начало маршрута', 'Данные отсутствуют')))
                self.ticketTable.setItem(row, 2, QTableWidgetItem(ticket.get('Конец маршрута', 'Данные отсутствуют')))
                self.ticketTable.setItem(row, 3, QTableWidgetItem(ticket.get('Дата', 'Данные отсутствуют')))
                self.ticketTable.setItem(row, 4, QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют'))))
                row += 1




