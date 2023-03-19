import pandas as pd
from ticket import Ticket

class Base:
    def __init__(self):
        self.__link = 0
        self.__base = pd.read_excel("../data/tickets.xlsx", index_col=0).to_dict('records')

    def printBase(self):
        print(self.__base)

    def __save(self):
        temp = self.__base
        temp = pd.DataFrame(temp)
        temp.to_excel("../data/tickets.xlsx")


    def delElement(self, num):
        self.__base.pop(num)
        self.__save()



