import pandas as pd

class Base:

    def __init__(self, link):
        self._link = link
        self._base = pd.read_excel(self._link, index_col=0).to_dict('records')

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





