import datetime as dt
from user import User
from base import Base


class Ticket:
    def __init__(self, id, beginPoint, endPoint, price, startYear, startMonth, startDay, startHours, startMins, endYear, endMonth, endDay, endHours, endMins):
        self.__id = id
        self.__beginPoint = beginPoint
        self.__endPoint = endPoint
        self.__price = price
        self.__dateStart = dt.datetime(startYear, startMonth, startDay, startHours, startMins)
        self.__dateEnd = dt.datetime(endYear, endMonth, endDay, endHours, endMins)
        self._tickets = []


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, year, month, day, hours, mins):
        self.__date = dt.datatime(year, month, day, hours, mins)

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
    def beginPoint(self):
        return self.__beginPoint

    @beginPoint.setter
    def beginPoint(self, beginPoint):
        self.__beginPoint = beginPoint


    def createDict(self):
        return {'id': self.__id,
                'Начало маршрута' : self.__beginPoint,
                'Конец маршрута' : self.__endPoint,
                'Цена' : self.__price}



if __name__ == '__main__':
    a = Ticket(1, 'Klg', 'Rostov', 3000, 2010, 4, 10, 10, 10, 2010, 4, 12, 12, 20)
    base = Base('data/tickets.xlsx')
    base.addElement(a.createDict())
    print(base.showBaseDict())
    a.price = 500
    alex = User('Alex', 'hiam', 'alexov', 'alex1', 'alex2', 'alex@mail.ru')
    # alex.buyTicket(a)
    # print(alex.getExactTicket(0).price)
    # a.price = 9000
    # print(a.date)
