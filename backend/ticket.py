import datetime as dt
import pandas as pd


class Ticket:
    def __init__(self, id, beginPoint, endPoint, price, hours=0, minutes=0, typeTicket = 'Плацкарт', amount=200): #write date like(Y/M/D/H/Min)
        self.__id = id
        self.__beginPoint = beginPoint
        self.__endPoint = endPoint
        self.__price = price
        self.__date = dt.time(hour=hours, minute=minutes)
        self.__exactDay = dt.date(year=2023,month=1, day=1)
        self.__place = ''
        self.__typeTicket = typeTicket
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def exactDay(self):
        return self.__exactDay

    @exactDay.setter
    def exactDay(self,date):
        self.__exactDay = dt.date(year=2023,month=int(date[0]), day=int(date[1]))

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self,time):
        self.__date = dt.time(hour=int(time[0]), minute=int(time[1]))
        self.__date = dt.time(hour=time[0], minute=time[1])

    @property
    def id(self):
        return self.__id

    @id.setter
    def date(self, id):
        self.__id = id

    @property
    def place(self):
        return self.__place

    @place.setter
    def date(self, place):
        self.__place = place

    @property
    def beginPoint (self):
        return self.__beginPoint

    @beginPoint.setter
    def beginPoint (self, beginPoint):
        self.__beginPoint = beginPoint

    @property
    def price (self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def endPoint(self):
        return self.__endPoint

    @endPoint.setter
    def endPoint(self, endPoint):
        self.__endPoint = endPoint

    @property
    def typeTicket(self):
        return self.__typeTicket

    @typeTicket.setter
    def typeTicket(self, typeTicket):
        self.__typeTicket = typeTicket

    def createDict(self):
        return {'id': self.__id,
                'Начало маршрута' : self.__beginPoint,
                'Конец маршрута' : self.__endPoint,
                'Цена' : self.__price,
                'Время' : (f'{self.__date.hour}:{self.__date.minute}'),
                'Тип билета' : self.__typeTicket,
                'amount' : self.amount}



if __name__ == '__main__':
    pass
    # a = Ticket(2, 'Klg', 'RostovSkiRaen', 3000, '2010/4/10/12/35')
    # print(a.createDict().get('Дата').split('/'))
    # base = TicketBase()

    # # temp = pd.read_excel('backend/data/tickets.xlsx', index_col=0).to_dict('records')
    # # print(temp[0].get('Дата').split('/'))

    # base.addElement(a)
    # print(base.showBaseDict())
    # a.price = 500
    # alex = User('Alex', 'hiam', 'alexov', 'alex1', 'alex2', 'alex@mail.ru')
