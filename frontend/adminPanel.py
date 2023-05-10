import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QVBoxLayout, QTableWidgetItem, QWidget, QMessageBox
from PyQt6 import uic
from backend.userBase import UserBase
from backend.ticketBase import TicketBase
from backend.user import User
from backend.ticket import Ticket
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import json


class AdminMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/adminMenu.ui', self)
        self.setWindowTitle('Меню администратора')

        for i in range(6):
            self.userTable.setColumnWidth(i,130)

        self.base = UserBase()
        print(self.base.showBaseDict())
        print(type(self.base.showBaseDict()))
        print(len(self.base.showBaseDict()))
        print(str(self.base.showBaseDict()[0]['login']))
        self.users = self.read('backend/Tickets.json')
        self.ticketBase = TicketBase()

        self.__loadData()
        self.__loadTicketData()

        self.changedFrame.hide()
        self.deletionFrame.hide()
        self.additionFrame.hide()
        self.deletionTicketFrame.hide()
        self.additionTicketFrame.hide()

        self.__showChangeFrame()

        self.__showDeletetionFrame()

        self.__showAdditionFrame()

        self.__showAdditionTicketFrame()

        self.__showDeletetionTicketFrame()

    def __deleteClicked(self):
        try:
            if len(self.base.showBaseDict()) >= int(self.userNumberToDelete.text()) and int(self.userNumberToDelete.text()) > 0:
                tNumber = int(self.userNumberToDelete.text()) - 1
                del self.users[str(self.base.showBaseDict()[tNumber]['login'])]
                self.base.delElement(tNumber)
                self.write(self.users, 'backend/Tickets.json')
                self.users = self.read('backend/Tickets.json')
                self.__loadData()
            else:
                self.__userDoesntExist()
                self.__clearDeletionFrame()
        except ValueError:
            if (self.userNumberToDelete.text() == ''):
                return
            self.__invalidInput()
            self.__clearDeletionFrame()


    def __addClicked(self):
        tName = str(self.newName.text())
        if (tName == ''):
            self.__invalidInput()
            return
        tSurname = str(self.newSurname.text())
        if (tSurname == ''):
            self.__invalidInput()
            return
        tFatherName = str(self.newFatherName.text())
        if (tFatherName == ''):
            self.__invalidInput()
            return
        tLogin = str(self.newLogin.text())
        if (tLogin == ''):
            self.__invalidInput()
            return
        tPassword = str(self.newPassword.text())
        if (tPassword == ''):
            self.__invalidInput()
            return
        tMail = str(self.newMail.text())
        if (tMail == ''):
            self.__invalidInput()
            return
        tNewUser = User(tName, tSurname, tFatherName, tLogin, tPassword, tMail)
        self.base.addElement(tNewUser)
        self.users[tLogin] = []
        self.write(self.users, 'backend/Tickets.json')
        self.users = self.read('backend/Tickets.json')
        self.__loadData()

    def __changeClicked(self):
        if str(self.userNumberToChange.text()) == '':
            return
        tNumber = int(self.userNumberToChange.text()) - 1
        tName = str(self.changedName.text())
        if (tName == ''):
            self.__invalidInput()
            return
        tSurname = str(self.changedSurname.text())
        if (tSurname == ''):
            self.__invalidInput()
            return
        tFatherName = str(self.changedFatherName.text())
        if (tFatherName == ''):
            self.__invalidInput()
            return
        tLogin = str(self.changedLogin.text())
        if (tLogin == ''):
            self.__invalidInput()
            return
        tPassword = str(self.changedPassword.text())
        if (tPassword == ''):
            self.__invalidInput()
            return
        tMail = str(self.changedMail.text())
        if (tMail == ''):
            self.__invalidInput()
            return
        self.base.changeElement(tNumber, 'Имя', tName)
        self.base.changeElement(tNumber, 'Фамилия', tSurname)
        self.base.changeElement(tNumber, 'Отчество', tFatherName)
        self.base.changeElement(tNumber, 'login', tLogin)
        self.newLogin = tLogin
        self.base.changeElement(tNumber, 'Пароль', tPassword)
        self.base.changeElement(tNumber, 'E-mail', tMail)
        self.changeLoginInJSON()
        self.__loadData()

    def read(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def write(self, users, filename):
        users = json.dumps(users, ensure_ascii = False)
        users = json.loads(str(users))
        with open(filename, 'w') as file:
            json.dump(users, file, indent = 4)

    def changeLoginInJSON(self):
        tickets = self.users[self.pastLogin]
        del self.users[self.pastLogin]
        self.users[self.newLogin] = tickets
        self.write(self.users, 'backend/Tickets.json')
        self.users = self.read('backend/Tickets.json')

    def __completionFieldsInChangeFrame(self):
        try:
            print(len(self.base.showBaseDict()))
            if len(self.base.showBaseDict()) >= int(self.userNumberToChange.text()) and int(self.userNumberToChange.text()) > 0:
                tNumber = int(self.userNumberToChange.text()) - 1
                tName = str(self.base.showBaseDict()[tNumber]['Имя'])
                tSurname = str(self.base.showBaseDict()[tNumber]['Фамилия'])
                tFatherName = str(self.base.showBaseDict()[tNumber]['Отчество'])
                tLogin = str(self.base.showBaseDict()[tNumber]['login'])
                tPassword = str(self.base.showBaseDict()[tNumber]['Пароль'])
                tMail = str(self.base.showBaseDict()[tNumber]['E-mail'])
                self.pastLogin = tLogin
                self.changedName.setText(tName)
                self.changedSurname.setText(tSurname)
                self.changedFatherName.setText(tFatherName)
                self.changedLogin.setText(tLogin)
                self.changedPassword.setText(str(tPassword))
                self.changedMail.setText(tMail)
            else:
                self.__userDoesntExist()
                self.__clearChangingFrame()
        except ValueError:
            if (self.userNumberToChange.text() == ''):
                return
            self.__invalidInput()
            self.__clearChangingFrame()

    def __userDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Пользователя не существует.", QMessageBox.StandardButton.Ok)

    def __ticketDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Билета не существует.", QMessageBox.StandardButton.Ok)

    def __invalidInput(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Некорректный ввод.", QMessageBox.StandardButton.Ok)

    def __notAllPropertys(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Не все поля заполнены.", QMessageBox.StandardButton.Ok)

    def __showDeletetionTicketFrame(self):
        self.deletionTicketButton.clicked.connect(lambda _: self.deletionTicketFrame.show())
        self.deletionTicketButton.clicked.connect(lambda _: self.additionTicketFrame.hide())
        self.deletionTicketButtonFrame.clicked.connect(self.__deletionButtonClicked)
        self.deletionTicketButtonFrame.clicked.connect(self.deletionTicketFrame.hide)
        self.deletionTicketButtonFrame.clicked.connect(self.delTicketID.clear)

    def __showAdditionTicketFrame(self):
        self.additionTicketButton.clicked.connect(lambda _: self.additionTicketFrame.show())
        self.additionTicketButton.clicked.connect(lambda _: self.deletionTicketFrame.hide())
        self.additionTicketButtonFrame.clicked.connect(self.__additionTicket)
        self.additionTicketButtonFrame.clicked.connect(self.additionTicketFrame.hide)
        self.additionTicketButtonFrame.clicked.connect(self.__additionTicketClear)

    def __showChangeFrame(self):
        self.changedButton.clicked.connect(lambda _: self.changedFrame.show())
        self.changedButton.clicked.connect(lambda _: self.deletionFrame.hide())
        self.changedButton.clicked.connect(lambda _: self.additionFrame.hide())
        self.changedButtonFrame.clicked.connect(lambda _: self.changedFrame.hide())
        self.changedButtonFrame.clicked.connect(self.__changeClicked)
        self.changedButtonFrame.clicked.connect(self.__clearChangingFrame)
        self.userNumberToChange.textChanged.connect(self.__completionFieldsInChangeFrame)

    def __showDeletetionFrame(self):
        self.deletionButton.clicked.connect(lambda _: self.deletionFrame.show())
        self.deletionButton.clicked.connect(lambda _: self.additionFrame.hide())
        self.deletionButton.clicked.connect(lambda _: self.changedFrame.hide())
        self.deletionButtonFrame.clicked.connect(lambda _: self.deletionFrame.hide())
        self.deletionButtonFrame.clicked.connect(self.__deleteClicked)
        self.deletionButtonFrame.clicked.connect(self.__clearDeletionFrame)

    def __showAdditionFrame(self):
        self.additionButton.clicked.connect(lambda _: self.additionFrame.show())
        self.additionButton.clicked.connect(lambda _: self.changedFrame.hide())
        self.additionButton.clicked.connect(lambda _: self.deletionFrame.hide())
        self.additionButtonFrame.clicked.connect(lambda _: self.additionFrame.hide())
        self.additionButtonFrame.clicked.connect(self.__addClicked)
        self.additionButtonFrame.clicked.connect(self.__clearAdditionFrame)

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
                self.userTable.setItem(row, 0, QTableWidgetItem(str(person.get('Имя', 'Данные отсутствуют'))))
                self.userTable.setItem(row, 1, QTableWidgetItem(str(person.get('Фамилия', 'Данные отсутствуют'))))
                self.userTable.setItem(row, 2, QTableWidgetItem(str(person.get('Отчество', 'Данные отсутствуют'))))
                self.userTable.setItem(row, 3, QTableWidgetItem(str(person.get('E-mail', 'Данные отсутствуют'))))
                self.userTable.setItem(row, 4, QTableWidgetItem(str(person.get('login', 'Данные отсутствуют'))))
                self.userTable.setItem(row, 5, QTableWidgetItem(str(person.get('Пароль', 'Данные отсутствуют'))))
                row += 1

    def __loadTicketData(self):
        self.ticketTable.setRowCount(len(self.ticketBase.showBaseDict()))
        row = 0
        for ticket in self.ticketBase.showBaseDict():
            print(ticket)
            self.ticketTable.setItem(row, 0, QTableWidgetItem(str(ticket.get('id', 'Данные отсутствуют'))))
            self.ticketTable.setItem(row, 1, QTableWidgetItem(str(ticket.get('Начало маршрута', 'Данные отсутствуют'))))
            self.ticketTable.setItem(row, 2, QTableWidgetItem(str(ticket.get('Конец маршрута', 'Данные отсутствуют'))))
            self.ticketTable.setItem(row, 3, QTableWidgetItem(str(ticket.get('Время', 'Данные отсутствуют'))))
            self.ticketTable.setItem(row, 4, QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют'))))
            self.ticketTable.setItem(row, 5 , QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют')*2)))
            self.ticketTable.setItem(row, 6 , QTableWidgetItem(str(ticket.get('Цена', 'Данные отсутствуют')*3)))
            self.ticketTable.setItem(row, 7 , QTableWidgetItem(str(ticket.get('amount', 'Данные отсутствуют'))))
            row += 1

    def __deletionButtonClicked(self):
        try:
            tID = int(self.delTicketID.text())
            ticketExist = False
            for ticket in self.ticketBase.showBaseDict():
                if int(ticket['id']) == tID:
                    ticketExist = True
            if (not(ticketExist)):
                self.__ticketDoesntExist()
                self.delTicketID.clear()
                return
            i = 0
            for ticket in self.ticketBase.showBaseDict():
                if int(ticket['id']) == tID:
                    break
                else:
                    i += 1
            self.ticketBase.delElement(i)
            self.__loadTicketData()

        except ValueError:
            self.__invalidInput()
            self.delTicketID.clear()

    def __additionTicketClear(self):
        self.departure.clear()
        self.arrival.clear()
        self.priceReservedSeat.clear()
        self.quantityOfPlaces.clear()

    def __additionTicket(self):

        if (str(self.departure.text()) == '' or str(self.arrival.text()) == '' or str(self.priceReservedSeat.text()) == '' or str(self.quantityOfPlaces.text()) == ''):
            self.__notAllPropertys()
            self.__additionTicketClear()
            return

        try:
            tDeparture = str(self.departure.text())
            tArrival = str(self.arrival.text())
            tTime = str(self.time.time().toString('HH:mm'))
            tPriceReservedSeat = int(self.priceReservedSeat.text())
            tAmount = int(self.quantityOfPlaces.text())
            if tAmount < 1:
                self.__invalidInput()
                self.__additionTicketClear()
                return
            i = 1
            placeFind = False
            while (not(placeFind)):
                exist = True
                for ticket in self.ticketBase.showBaseDict():
                    if int(ticket['id']) == i:
                        i += 1
                        exist = False
                        break
                if (exist):
                    placeFind = True
            newTicket = Ticket(i, tDeparture, tArrival, tPriceReservedSeat, tTime, amount=tAmount)
            self.ticketBase.addElement(newTicket)
            self.__loadTicketData()
        except ValueError:
            self.__invalidInput()
            self.__additionTicketClear()
