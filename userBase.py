from user import User
from base import Base

class UserBase(Base):
    pass

a = UserBase("data/users.xlsx")
b = User('Nikita', 'Petrov', 'Devidovich', 'demid@gmial.com', 'nekita_1992')
a.addElement(b)



