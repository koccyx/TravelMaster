from backend.base import Base
from backend.user import User

class UserBase(Base):
    def __init__(self):
        super().__init__('backend/data/users.xlsx')
        self._objectBase = [User(person.get('Имя'), person.get('Фамилия'), person.get('Отчество'),
                                  person.get('login'), person.get('Пароль'), person.get('E-mail')) for person in self._base]

    @property
    def objecBase(self):
        return self._objectBase


if __name__ == '__main__':
    a = UserBase()
    a.printObjects()
