from abc import ABCMeta
from abc import abstractmethod

class AbsDictionary(mataclass=ABCMeta):

    def __init__(self):
        self.wordDic = {}

    @abstractmethod
    def registWord(self, w1, w2):
        pass

    @abstractmethod
    def removeWord(self, w1):
        pass

    @abstractmethod
    def updateWord(self, w1, w2):
        pass

    @abstractmethod
    def searchWord(self, w1):
        pass





class KortoEng(AbsDictionary):
    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KortoEng] registWord() : {w1} to {w2}')
        self.wordDic[w1] = w2


    def removeWord(self, w1):
        print(f'[KortoEng] removeWord() : {w1}')
        del self.wordDic[w1]


    def updateWord(self, w1, w2):
        print(f'[KortoEng] updateWord() : {w1} to {w2}')
        self.wordDic[w1] = w2


    def searchWord(self, w1):
        print(f'[KortoEng] searchWord() : {w1}')
        return self.wordDic[w1]

    def printWords(self):
        for k in self.wordDic.keys():
            print(f'{k}: {self.wordDic[k]}')


class KortoJpa(AbsDictionary):
    def __init__(self):
        super().__init__()

    def registWord(self, w1, w2):
        print(f'[KortoJpa] registWord() : {w1} to {w2}')
        self.wordDic[w1] = w2


    def removeWord(self, w1):
        print(f'[KortoJpa] removeWord() : {w1}' )
        del self.wordDic[w1]


    def updateWord(self, w1, w2):
        print(f'[KortoJpa] updateWord() : {w1} to {w2}')
        self.wordDic[w1] = w2


    def searchWord(self, w1):
        print(f'[KortoJpa] searchWord() : {w1}')
        return self.wordDic[w1]

    def printWords(self):
        for k in self.wordDic.keys():
            print(f'{k}: {self.wordDic[k]}')