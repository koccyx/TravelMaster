import datetime as dt
import pandas as pd


class Ticket:
    def __init__(self, id, beginPoint, endPoint, price, hours=0, minutes=0): #write date like(Y/M/D/H/Min)
        self.__id = id
        self.__beginPoint = beginPoint
        self.__endPoint = endPoint
        self.__price = price
        self.__date = dt.time(hour=hours, minute=minutes)
        self.__exactDay = dt.date(year=2023,month=1, day=1)

    @property
    def exactDay(self):
        return self.__exactDay

    @exactDay.setter
    def exactDay(self,date):
        self.__exactDay = dt.time(hour=int(date[0]), minute=int(date[1]))

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self,time):
        self.__date = dt.date(hour=int(time[0]), minute=int(time[1]))

    @property
    def id(self):
        return self.__id

    @id.setter
    def date(self, id):
        self.__id = id


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

    @beginPoint.getter
    def beginPoint(self):
        return self.__beginPoint

    def createDict(self):
        return {'id': self.__id,
                'Начало маршрута' : self.__beginPoint,
                'Конец маршрута' : self.__endPoint,
                'Цена' : self.__price,
                'Время' : (f'{self.__date.hour}:{self.__date.minute}')}



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
