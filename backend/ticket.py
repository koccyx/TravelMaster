import datetime as dt

class Ticket:
    def __init__(self, beginPoint, endPoint, price, date = dt.datetime.now()):
        self.__beginPoint = beginPoint
        self.__endPoint = endPoint
        self.__price = price
        self.__date = date


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

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
        return {'Начало маршрута' : self.__beginPoint,
                'Конец маршрута' : self.__endPoint,
                'Цена' : self.__price}



if __name__ == '__main__':
    a = Ticket('Klg', 'Rostov', 1000)
    a.price = 9000
    print(a.price)
