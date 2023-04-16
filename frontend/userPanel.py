import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget, QMessageBox
from PyQt6 import uic
from backend.ticketBase import TicketBase
from backend.user import User
import datetime
sys.path.insert(1, os.path.join(sys.path[0], '..'))


class UserMenu(QWidget):
    def __init__(self, user):
        super().__init__()
        uic.loadUi('frontend/ui/userMenu.ui', self)
        self.setWindowTitle('Меню пользователя')

        self.user = user

        for i in range(6):
            self.ticketTable.setColumnWidth(i,130)

        self.__downloadBaseFromExcel()

        self.__loadTicketData()

        self.buyFrame.hide()
        self.pdfFrame.hide()
        self.returnFrame.hide()
        self.filterFrame.hide()

        self.buyButtonFrame.clicked.connect(self.__showBuyFrame)
        self.buyButton.clicked.connect(self.__ticketBuyButtonClicked)
        self.monthSpinBox.setMinimum(1)
        self.daySpinBox.setMinimum(1)
        self.monthSpinBox.setMaximum(12)
        self.daySpinBox.setMaximum(31)
        self.monthSpinBox.valueChanged.connect(self.__setRange)

        self.pdfButtonFrame.clicked.connect(self.__showPdfFrame)
        self.pdfButton.clicked.connect(self.__pdfButtonClicked)

        self.returnButtonFrame.clicked.connect(self.__showReturnFrame)
        self.returnButton.clicked.connect(self.__ticketReturnButtonClicked)

        self.filterButtonFrame.clicked.connect(self.__showFilterFrame)
        self.applyFilterButton.clicked.connect(self.__ticketFilterButtonClicked)

    def __setRange(self):
        if (self.monthSpinBox.value() == 2):
            self.daySpinBox.setMaximum(28)
            return
        if (self.monthSpinBox.value() < 8 and self.monthSpinBox.value() % 2 == 1):
            self.daySpinBox.setMaximum(31)
            return
        if (self.monthSpinBox.value() >= 8 and self.monthSpinBox.value() % 2 == 0):
            self.daySpinBox.setMaximum(31)
            return
        self.daySpinBox.setMaximum(30)


    def __showFilterFrame(self):
        self.filterFrame.show()
        self.buyFrame.hide()
        self.pdfFrame.hide()
        self.returnFrame.hide()
        #self.cancelFilterButton.clicked.connect(self.__downloadBaseFromExcel)
        self.cancelFilterButton.clicked.connect(self.filterFrame.hide)
        self.cancelFilterButton.clicked.connect(self.__loadTicketData)
        self.cancelFilterButton.clicked.connect(self.__clearFilterFrame)

    def __downloadBaseFromExcel(self):
        self.ticketBase = TicketBase()

    def __clearFilterFrame(self):
        self.departureText.clear()
        self.destinationText.clear()
        self.downtoPriceFilter.clear()
        self.uptoPriceFilter.clear()

    def __showBuyFrame(self):
        self.buyFrame.show()
        self.filterFrame.hide()
        self.pdfFrame.hide()
        self.returnFrame.hide()
        self.buyButton.clicked.connect(self.buyTicketID.clear)
        self.buyButton.clicked.connect(self.buyFrame.hide)

    def __showReturnFrame(self):
        self.returnFrame.show()
        self.filterFrame.hide()
        self.pdfFrame.hide()
        self.buyFrame.hide()
        self.returnButton.clicked.connect(self.returnTicketID.clear)
        self.returnButton.clicked.connect(self.returnFrame.hide)

    def __showPdfFrame(self):
        self.pdfFrame.show()
        self.filterFrame.hide()
        self.returnFrame.hide()
        self.buyFrame.hide()
        self.pdfButton.clicked.connect(self.pdfTicketID.clear)
        self.pdfButton.clicked.connect(self.pdfFrame.hide)

    def __ticketFilterButtonClicked(self):
        self.__filterByDeparture()
        self.__filterByDestination()
        self.__filterByPrice()
        self.__loadTicketData()
        self.__downloadBaseFromExcel()

    def __filterByDeparture(self):
        if (self.departureText.text() == ''):
            return
        i = 0
        while i < len(self.ticketBase.showBaseDict()):
            if (self.ticketBase.showBaseDict()[i]['Начало маршрута'] != self.departureText.text()):
                del self.ticketBase.showBaseDict()[i]
            else:
                i += 1

    def __filterByDestination(self):
        if (self.destinationText.text() == ''):
            return

        i = 0
        while i < len(self.ticketBase.showBaseDict()):
            if (self.ticketBase.showBaseDict()[i]['Конец маршрута'] != self.destinationText.text()):
                del self.ticketBase.showBaseDict()[i]
            else:
                i += 1

    def __filterByPrice(self):
        if (self.downtoPriceFilter.text() == '' and self.uptoPriceFilter.text() == ''):
            return

        try:
            if (self.comboBox.currentText() == ''):
                temp1 = int(self.downtoPriceFilter.text())
                temp2 = int(self.uptoPriceFilter.text())
                return
            self.__filterByPriceType('плацкарта', 1)
            self.__filterByPriceType('купе', 2)
            self.__filterByPriceType('СВ', 3)
        except ValueError:
            self.downtoPriceFilter.clear()
            self.uptoPriceFilter.clear()
            self.returnTicketID.clear()
            self.__invalidInput()

    def __filterByPriceType(self, typeTicket, index):
        if (self.comboBox.currentText() == str(typeTicket)):
            if (self.downtoPriceFilter.text() != '' and self.uptoPriceFilter.text() != ''):
                i = 0
                while i < len(self.ticketBase.showBaseDict()):
                    if not(int(self.downtoPriceFilter.text()) <= int(self.ticketBase.showBaseDict()[i]['Цена'])*index <= int(self.uptoPriceFilter.text())):
                        del self.ticketBase.showBaseDict()[i]
                    else:
                        i += 1
            elif (self.downtoPriceFilter.text() != ''):
                i = 0
                while i < len(self.ticketBase.showBaseDict()):
                    if int(self.downtoPriceFilter.text()) > int(self.ticketBase.showBaseDict()[i]['Цена'])*index:
                        del self.ticketBase.showBaseDict()[i]
                    else:
                        i += 1
            else:
                i = 0
                while i < len(self.ticketBase.showBaseDict()):
                    if int(self.ticketBase.showBaseDict()[i]['Цена'])*index > int(self.uptoPriceFilter.text()):
                        del self.ticketBase.showBaseDict()[i]
                    else:
                        i += 1

    def __pdfButtonClicked(self):
        try:
            idExist = False
            for i in range(len(self.user.ticketCart)):
                if int(self.user.ticketCart[i].id) == int(self.pdfTicketID.text()):
                    idExist = True
            if (int(self.pdfTicketID.text()) < 1 or idExist == False):
                self.__ticketDoesntExist()
                self.pdfTicketID.clear()
                return
            print("Success")
        except  ValueError:
            self.pdfTicketID.clear()
            self.__invalidInput()


    def __ticketBuyButtonClicked(self):
        try:
            idExist = False
            for ticket in self.ticketBase.objectBase:
                if int(ticket.id) == int(self.buyTicketID.text()):
                    idExist = True
            if (int(self.buyTicketID.text()) < 1 or idExist == False):
                self.__ticketDoesntExist()
                self.buyTicketID.clear()
                self.monthSpinBox.setValue(1)
                self.daySpinBox.setValue(1)
                return
            for ticket in self.ticketBase.objectBase:
                if int(ticket.id) == int(self.buyTicketID.text()):
                    ticket.exactDay = [str(self.monthSpinBox.value()), str(self.daySpinBox.value())]
                    self.user.buyTicket(ticket)
            self.__loadTicketCartData()
            print(self.user.ticketCart)
        except  ValueError:
            self.monthSpinBox.setValue(1)
            self.daySpinBox.setValue(1)
            self.__invalidInput()

    def __ticketDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Билета с таким номером не существует.", QMessageBox.StandardButton.Ok)

    def __invalidInput(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Некорректный ввод.", QMessageBox.StandardButton.Ok)

    def __ticketReturnButtonClicked(self):
        try:
            idExist = False
            for i in range(len(self.user.ticketCart)):
                if int(self.user.ticketCart[i].id) == int(self.returnTicketID.text()):
                    idExist = True
            if (int(self.returnTicketID.text()) < 1 or idExist == False):
                self.__ticketDoesntExist()
                self.returnTicketID.clear()
                return
            for i in range(len(self.user.ticketCart)):
                if int(self.returnTicketID.text()) == int(self.user.ticketCart[i].id):
                    self.user.delTicket(i)
                    break
            self.__loadTicketCartData()
        except ValueError:
            self.returnTicketID.clear()
            self.__invalidInput()

    def __loadTicketData(self):
        self.ticketTable.setRowCount(len(self.ticketBase.showBaseDict()))
        row = 0
        for ticket in self.ticketBase.showBaseDict():
                print(ticket)
                self.ticketTable.setItem(row, 0, QTableWidgetItem(str(ticket.get('id', 'Данные отсутствуют'))))
                self.ticketTable.setItem(row, 1, QTableWidgetItem(ticket.get('Начало маршрута', 'Данные отсутствуют')))
                self.ticketTable.setItem(row, 2, QTableWidgetItem(ticket.get('Конец маршрута', 'Данные отсутствуют')))
                self.ticketTable.setItem(row, 3, QTableWidgetItem(str(ticket.get('Время', 'Данные отсутствуют'))))
                self.ticketTable.setItem(row, 4, QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют'))))
                self.ticketTable.setItem(row, 5 , QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют')*2)))
                self.ticketTable.setItem(row, 6 , QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют')*3)))
                row += 1

    def __loadTicketCartData(self):
        self.ticketCartTable.setRowCount(len(self.user.showTicketCartDict()))
        row = 0
        for ticket in self.user.showTicketCartDict():
                print(ticket)
                self.ticketCartTable.setItem(row, 0, QTableWidgetItem(str(ticket.get('id', 'Данные отсутствуют'))))
                self.ticketCartTable.setItem(row, 1, QTableWidgetItem(ticket.get('Начало маршрута', 'Данные отсутствуют')))
                self.ticketCartTable.setItem(row, 2, QTableWidgetItem(ticket.get('Конец маршрута', 'Данные отсутствуют')))
                self.ticketCartTable.setItem(row, 3, QTableWidgetItem(str('/'.join([str(self.ticketBase.objectBase[row].exactDay).split('-')[1], str(self.ticketBase.objectBase[row].exactDay).split('-')[2]]))))
                self.ticketCartTable.setItem(row, 4, QTableWidgetItem(str(ticket.get('Время', 'Данные отсутствуют'))))
                self.ticketCartTable.setItem(row, 5 , QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют'))))
                row += 1




