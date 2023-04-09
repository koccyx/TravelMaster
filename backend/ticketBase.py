from backend.base import Base
from backend.ticket import Ticket

class TicketBase(Base):
    def __init__(self):
        super().__init__('backend/data/tickets.xlsx')

        self.__objectBase = [Ticket(ticket.get('id'), ticket.get('Начало маршрута'),ticket.get('Конец маршрута'),ticket.get('Цена'), ticket.get('Дата')) for ticket in self._base]

    @property
    def objectBase(self):
        return self.__objectBase

    

if __name__ == '__main__':
    from ticket import Ticket
    a = Ticket(2, 'Klg', 'RostovSki', 3000, 2010, 4, 10, 10, 10)
    print(a.createDict())


