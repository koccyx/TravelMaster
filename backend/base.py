import pandas as pd

class Base:

    def __init__(self, link):
        self._link = link
        self._base = pd.read_excel(self._link, index_col=0).to_dict('records')

    def showBaseDict(self):
        return self._base

    def delElement(self, num):
        self._base.pop(num)
        self._save()

    def addElement(self, item):
        self._base.append(item.createDict())
        self._save()

    def _save(self):
        temp = self._base
        temp = pd.DataFrame(temp)
        temp.to_excel(self._link)





if __name__ == '__main__':
    base = Base('backend/data/users.xlsx')
    # print(base.showBaseDict()[1].get('Имяы', 'Данные отсутствуют'))
    for i in base.showBaseDict():
        print()
