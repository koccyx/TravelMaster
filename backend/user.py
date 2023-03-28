import pandas as pd

class User:
    USER_BASE = []
    def __init__(self, firstName, lastName, surname, login, password, mail) :
        self.__firstName = firstName
        self.__lastName = lastName
        self.__surname = surname
        self.__login = login
        self.__mail = mail
        self.__password = password
        self.__ticketCart = []

    def __del__(self):
        pass

    def buyTicket(self, ticket):
        self.__ticketCart.append(ticket)

    def getTicketCart(self):
        return self.__ticketCart

    def createDict(self):
        return {'Имя' :self.__firstName,
                'Фамилия' : self.__lastName,
                'Отчество' : self.__surname,
                'login' : self.__login,
                'Пароль' : self.__password,
                'E-mail' : self.__mail,}

    def save(self):
        temp = pd.read_excel('backend/data/users.xlsx', index_col=0).to_dict('records')
        temp.append(self.createDict())
        temp = pd.DataFrame(temp)
        temp.to_excel('backend/data/users.xlsx')











