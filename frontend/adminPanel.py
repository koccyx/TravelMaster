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


class AdminMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('frontend/ui/adminMenu.ui', self)
        self.setWindowTitle('Меню администратора')

        for i in range(6):
            self.userTable.setColumnWidth(i,130)

        self.base = UserBase()

        self.ticketBase = TicketBase()

        self.__loadData()
        self.__loadTicketData()

        self.changedFrame.hide()
        self.deletionFrame.hide()
        self.additionFrame.hide()
        self.deleteFrame.hide()
        self.addFrame.hide()

        self.__showChangeFrame()

        self.__showDeleteFrame()

        self.__showAddFrame()

        self.__showAdditionFrame()

        self.__showDelFrame()

        self.delButton.clicked.connect(self.__delBUttonClicked)
        self.addButton.clicked.connect(self.__addTicket)

    def __deleteClicked(self):
        try:
            if len(self.base.showBaseDict()) >= int(self.userNumberToDelete.text()) and int(self.userNumberToDelete.text()) > 0:
                tNumber = int(self.userNumberToDelete.text()) - 1
                self.base.delElement(tNumber)
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

    def __changeClicked(self):
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

    def __completionFieldsInChangeFrame(self):
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

    def __userDoesntExist(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Пользователя не существует.", QMessageBox.StandardButton.Ok)


    def __invalidInput(self):
        self.msgbox = QMessageBox.warning(self, "Ошибка", "Некорректный ввод.", QMessageBox.StandardButton.Ok)

    def __showDelFrame(self):
        self.deleteFrameButton.clicked.connect(lambda _: self.deleteFrame.show())
        self.deleteFrameButton.clicked.connect(lambda _: self.addFrame.hide())

    def __showAdditionFrame(self):
        self.addFrameButton.clicked.connect(lambda _: self.addFrame.show())
        self.deleteFrameButton.clicked.connect(lambda _: self.deleteFrame.hide())

    def __showChangeFrame(self):
        self.changedButton.clicked.connect(lambda _: self.changedFrame.show())
        self.changedButton.clicked.connect(lambda _: self.deletionFrame.hide())
        self.changedButton.clicked.connect(lambda _: self.additionFrame.hide())
        self.changedButtonFrame.clicked.connect(lambda _: self.changedFrame.hide())
        self.changedButtonFrame.clicked.connect(self.__changeClicked)
        self.changedButtonFrame.clicked.connect(self.__clearChangingFrame)
        self.userNumberToChange.textChanged.connect(self.__completionFieldsInChangeFrame)

    def __showDeleteFrame(self):
        self.deletionButton.clicked.connect(lambda _: self.deletionFrame.show())
        self.deletionButton.clicked.connect(lambda _: self.additionFrame.hide())
        self.deletionButton.clicked.connect(lambda _: self.changedFrame.hide())
        self.deletionButtonFrame.clicked.connect(lambda _: self.deletionFrame.hide())
        self.deletionButtonFrame.clicked.connect(self.__deleteClicked)
        self.deletionButtonFrame.clicked.connect(self.__clearDeletionFrame)

    def __showAddFrame(self):
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
                self.userTable.setItem(row, 0, QTableWidgetItem(person.get('Имя', 'Данные отсутствуют')))
                self.userTable.setItem(row, 1, QTableWidgetItem(person.get('Фамилия', 'Данные отсутствуют')))
                self.userTable.setItem(row, 2, QTableWidgetItem(person.get('Отчество', 'Данные отсутствуют')))
                self.userTable.setItem(row, 3, QTableWidgetItem(person.get('E-mail', 'Данные отсутствуют')))
                self.userTable.setItem(row, 4, QTableWidgetItem(person.get('login', 'Данные отсутствуют')))
                self.userTable.setItem(row, 5, QTableWidgetItem(person.get('Пароль', 'Данные отсутствуют')))
                row += 1

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

    def __delBUttonClicked(self):
        self.ticketBase.delElement(int(self.delTicketID.text()))
        self.__loadTicketData();

    def __addTicket(self):
        newTicket = Ticket(int(self.idLine.text()), self.startLine.text(), self.endLine.text(), int(self.priceLine.text()), hours=int(self.timeHoursLine.text()), minutes=int(int(self.timeMinutesLine.text())))

        self.ticketBase.addElement(newTicket)
        self.__loadTicketData()
