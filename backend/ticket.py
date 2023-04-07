import datetime as dt
import pandas as pd


class Ticket:
    def __init__(self, id, beginPoint, endPoint, price, date): #write date like(Y/M/D/H/Min)
        self.__id = id
        self.__beginPoint = beginPoint
        self.__endPoint = endPoint
        self.__price = price
        date = date.split('/')
        self.__date = dt.datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]))

    @property
    def id(self):
        return self.__id

    @id.setter
    def date(self, id):
        self.__id = id



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
                'Цена' : self.__price,
                'Дата' : (f'{self.__date.year}/{self.__date.month}/{self.__date.day}/{self.__date.hour}/{self.__date.minute}')}



if __name__ == '__main__':
    a = Ticket(2, 'Klg', 'RostovSkiRaen', 3000, '2010/4/10/12/35')
    print(a.createDict().get('Дата').split('/'))
    base = TicketBase()

    # temp = pd.read_excel('backend/data/tickets.xlsx', index_col=0).to_dict('records')
    # print(temp[0].get('Дата').split('/'))

    base.addElement(a)
    print(base.showBaseDict())
    a.price = 500
    alex = User('Alex', 'hiam', 'alexov', 'alex1', 'alex2', 'alex@mail.ru')
