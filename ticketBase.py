from ticket import Ticket
from base import Base

class TicketBase(Base):
    pass



a = TicketBase("data/tickets.xlsx")
b = Ticket('Dnepropetrovsk', 'Silik', 1900)
a.addElement(b)
# a.delElement(10)
