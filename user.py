class User:
    USER_BASE = []
    def __init__(self, firstName, lastName, surname, mail, password) :
        self.__firstName = firstName
        self.__lastName = lastName
        self.__surname = surname
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
                'E-mail' : self.__mail,
                'Пароль' : self.__password}



# def main():
#     oleg = User('Oleg', 'Baranov', 'Yurevich', 'oleg@mail.com', 'eeez boy')
#     b1 = Ticket('Rostov', 'Moscow', 1900)
#     oleg.buyTicket(b1)
#     print(oleg.getTicketCart()[0].getPrice())


# if __name__ == '__main__':
#     main()





