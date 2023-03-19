import pandas as pd
import numpy as np
from ticket import Ticket
arr = []
for i in range(10):
    arr.append(Ticket('Omsk', 'London', 10000))

ticketAlbum = [i.createDict() for i in arr]
ticketAlbumDf = pd.DataFrame(ticketAlbum)
ticketAlbumDf.index = [int(i) for i in range(1,len(ticketAlbumDf) + 1)]
ticketAlbumDf.to_excel('./albums.xlsx')
myDf = pd.read_excel("./albums.xlsx", index_col=0)


# print(myDf.shape) len

# print(myDf.size)

print(myDf.loc[3]['Цена'])

# print(ticketAlbumDf)


# name = ['take', 'that', 'shit']
# year = [2001, 2002, 1932]
# albumsDict = {'album' : name, 'year' : year}
# albumsDf = pd.DataFrame(albumsDict)

# albumsDf.index = [int(i) for i in range(1,len(albumsDf) + 1)]

# # print(len(albumsDf))

# albumsCapitalDf = pd.DataFrame([{'album': 'Point of entry',
#                                 'year' : 1923},
#                                 {'album': 'I love poetry',
#                                 'year' : 1989}],
#                                 columns=['year', 'album'])
# albumsDf.to_csv('albums.csv', index=True)

