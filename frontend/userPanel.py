import sys
import os
import copy
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget, QMessageBox
from PyQt6 import uic
from backend.ticketBase import TicketBase
from backend.user import User
import datetime
from backend.sendEmail import sendEmail
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from fpdf import *
#from fpdf2 import *


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
            pdf = FPDF(orientation="landscape")

            pdf.add_page()
            pdf.add_font('DejaVu', '', 'backend/font/DejaVuSansCondensed.ttf', uni = True)
            pdf.add_font('DejaVuBold', '', 'backend/font/DejaVuSerifCondensed-Bold.ttf', uni = 3)
            pdf.set_font('DejaVu', size = 25)
            pdf.cell(275, 10, txt = 'Электронный проездной документ', ln = 1, align = 'C')
            lineHeight = pdf.font_size
            pdf.ln(lineHeight)

            pdf.set_font('DejaVu', size = 15)
            pdf.cell(275, 10, txt = 'Данные о пользователе:', ln = 1, align = 'L')
            lineWeigth = pdf.epw / 4
            dataUser = [('Имя', 'Фамилия', 'Отчество', 'Логин'),
                        (str(self.user.firstName), str(self.user.lastName), str(self.user.surname), str(self.user.login))]
            i = 0
            firstIteration = True
            for row in dataUser:
                if (firstIteration == True):
                        pdf.set_font('DejaVuBold', size = 13)
                        firstIteration = False
                else:
                    pdf.set_font('DejaVu', size = 10)
                for datum in row:
                    pdf.multi_cell(lineWeigth, lineHeight, datum, border=1, ln=3, max_line_height=pdf.font_size)
                    i += 1
                    if (i == 4):
                        i = 0
                pdf.ln(lineHeight)

            sizes = [6/29*pdf.epw, 6/29*pdf.epw, 4/29*pdf.epw, 4/29*pdf.epw, 7/29*pdf.epw, 2/29*pdf.epw]
            for ticket in self.user.ticketCart:
                if (ticket.id == int(self.pdfTicketID.text())):
                    dataTicket = (str(ticket.beginPoint), str(ticket.endPoint), str('/'.join([str(ticket.exactDay).split('-')[1], str(ticket.exactDay).split('-')[2]])), str(ticket.createDict()['Время']), str(ticket.typeTicket), '3')
            data = [('Место отправления', 'Место прибытия', 'Дата отправления', 'Время отправления', 'Тип места', 'Место'),
                    dataTicket]
            i = 0
            pdf.ln(lineHeight)
            pdf.set_font('DejaVu', size = 15)
            pdf.cell(275, 10, txt = 'Данные о билете:', ln = 1, align = 'L')
            firstIteration = True
            for row in data:
                if (firstIteration == True):
                        pdf.set_font('DejaVuBold', size = 13)
                        firstIteration = False
                else:
                    pdf.set_font('DejaVu', size = 10)
                for datum in row:
                    pdf.multi_cell(sizes[i], lineHeight, datum, border=1, ln=3, max_line_height=pdf.font_size)
                    i += 1
                    if (i == 6):
                        i = 0
                pdf.ln(lineHeight)
            pdf.ln(lineHeight)

            pdf.set_font('DejaVu', size = 15)
            pdf.ln(2*lineHeight)

            if (str(ticket.typeTicket) == 'Плацкарт'):
                pdf.image('frontend/images/reservedSeat.png', x = 10, y = 100)
                pdf.cell(275, 10, txt = '   Вагон оборудован санитарным узлом, платным душем. Имеется кипяток, посуда и кофе на заказ.', ln = 1, align = 'L')

            if (str(ticket.typeTicket) == 'Купе'):
                pdf.image('frontend/images/coupe.png', x = 10, y = 100)
                pdf.cell(275, 10, txt = '   Вагон оборудован санитарным узлом, душем. Имеется кипяток, посуда и кофе на заказ. Утром вам подадут завтрак.', ln = 1, align = 'L')

            if (str(ticket.typeTicket) == 'СВ'):
                pdf.image('frontend/images/SV.png', x = 10, y = 100)
                pdf.cell(275, 10, txt = '   Вагон оборудован санитарным узлом, душем. Имеется кипяток, посуда и кофе на заказ.', ln = 1, align = 'L')
                pdf.cell(275, 10, txt = 'Предусмотрено 4-ёх разовое питание в вагоне-ресторане.', ln = 1, align = 'L')

            pdf.cell(275, 10, txt = 'Просим вас пребывать на место выезда поезда заранее (желательно за 15 минут).', ln = 1, align = 'L')
            pdf.cell(275, 10, txt = 'Не забудьте взять с собой документ, удостоверяющий вашу личность.', ln = 1, align = 'L')
            pdf.ln(2 * lineHeight)
            pdf.set_font('DejaVuBold', size = 25)
            pdf.cell(275, 10, txt = 'Счастливого пути!!!', ln = 1, align = 'C')
            pdf.image('frontend/images/delivery.png', x = 150, y = 182)

            pdf.output('./backend/Ticket.pdf')
            print("Success")
        except  ValueError:
            self.pdfTicketID.clear()
            self.__invalidInput()
        sendEmail('Биллетsss')


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
                    newTicket = copy.deepcopy(ticket)
                    newTicket.exactDay = [int(self.monthSpinBox.value()), int(self.daySpinBox.value())]
                    newTicket.typeTicket = str(self.typeTicketSpinBox.currentText())
                    if (newTicket.typeTicket == 'Купе'):
                        newTicket.price *= 2
                    elif (newTicket.typeTicket == 'СВ'):
                        newTicket.price *= 3

                    self.user.buyTicket(newTicket)
                    self.__loadTicketCartData()
                    self.monthSpinBox.setValue(1)
                    self.daySpinBox.setValue(1)
                    return
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
        print('-------st--------')
        for ticket in self.user.ticketCart:
            print(ticket)
            self.ticketCartTable.setItem(row, 0, QTableWidgetItem(str(ticket.id)))
            self.ticketCartTable.setItem(row, 1, QTableWidgetItem(ticket.beginPoint))
            self.ticketCartTable.setItem(row, 2, QTableWidgetItem(ticket.endPoint))
            print(ticket.exactDay)
            self.ticketCartTable.setItem(row, 3, QTableWidgetItem(str('/'.join([str(ticket.exactDay).split('-')[1], str(ticket.exactDay).split('-')[2]]))))
            self.ticketCartTable.setItem(row, 4, QTableWidgetItem(ticket.createDict()['Время']))
            self.ticketCartTable.setItem(row, 5 , QTableWidgetItem(str(ticket.price)))
            self.ticketCartTable.setItem(row, 6, QTableWidgetItem(str(ticket.createDict()['Тип билета'])))
            row += 1
        print('-------ed-------')



