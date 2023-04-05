from base import Base


class TicketBase(Base):
    def __init__(self):
        super().__init__('backend/data/tickets.xlsx')
        from ticket import Ticket
        self._objectBase = [Ticket(ticket.get('id'), ticket.get('Начало маршрута'),ticket.get('Конец маршрута'),ticket.get('Цена'), ticket.get('Дата')) for ticket in self._base]


if __name__ == '__main__':
    from ticket import Ticket
    a = Ticket(2, 'Klg', 'RostovSki', 3000, 2010, 4, 10, 10, 10)
    print(a.createDict())


