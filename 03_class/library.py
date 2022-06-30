class Book:
    def __init__(self, name, price, isbn):
        self.bname = name
        self.bprice = price
        self.bisbn = isbn


class BookRepository(Book):
    def __init__(self):
        self.bDic = {}

    def regisBook(self, b):
        self.bDic[b.bisbn] = b

    def removeBook(self, isbn):
        del self.bDic[isbn]

    def printBooksinfo(self):
        for isbn in self.bDic.keys():
            b = self.bDic[isbn]
            print(f'{b.bname}, {b.bprice}, {b.bisbn}')

    def printBookinfo(self, isbn):
        if isbn in self.bDic:
            b = self.bDic[isbn]
            print(f'{b.bname}, {b.bprice}, {b.bisbn}')
        else:
            print('책이 없습니다')


