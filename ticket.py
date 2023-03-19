import datetime as dt

class Ticket:
    def __init__(self, beginPoint, endPoint, price, date = dt.datetime.now()):
        self.__beginPoint = beginPoint
        self.__endPoint = endPoint
        self.__price = price
        self.__date = date

    def getDate(self):
        return self.__date

    def getBeginPoint (self):
        return self.__beginPoint

    def getEndPoint (self):
        return self.__endPoint

    def getPrice (self):
        return self.__price

    def setBeginPoint (self, BeginPoint):
        self.__beginPoint = BeginPoint

    def setEndPoint (self, EndPoint):
        self.__endPoint = EndPoint

    def setPrice (self, price):
        self.__price = price

    def createDict(self):
        return {'Начало маршрута' : self.__beginPoint,
                'Конец маршрута' : self.__endPoint,
                'Цена' : self.__price}



