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


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, mail):
        self.__mail = mail

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


    def buyTicket(self, ticket):
        ticket.amount -= 1
        self.__ticketCart.append(ticket)
        print(ticket.amount)

    def delTicket(self, num):
        self.__ticketCart.pop(num)

    def getExactTicket(self, num):
        return self.__ticketCart[num]

    def showTicketCartDict(self):
        self.__ticketCartDict = []
        for ticket in self.__ticketCart:
            self.__ticketCartDict.append(ticket.createDict())
        return self.__ticketCartDict

    @property
    def ticketCart(self):
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


if __name__ == '__main__':
    b = User('Alex', 'Pivko', 'Nikizhov', 'alex2009', 'dsadsa', 'alex40@mail.com')
    print(b.mail)








