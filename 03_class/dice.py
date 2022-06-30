import random

class Dice:
    def __init__(self):
        self.cNum = 0
        self.uNum = 0

    def setCnum(self):
        print('[Dice] setCnum()')
        self.cNum = random.randint(1, 6)
        return self.cNum

    def setUnum(self):
        print('[Dice] setUnum()')
        self.uNum = random.randint(1, 6)
        return self.uNum

    def startGame(self):
        print('[Dice] startGame()')
        self.setCnum()
        self.setUnum()


    def printResult(self):
        print('[Dice] printResult()')

        if self.cNum == 0 or self.uNum == 0:
            print('주사위 숫자 선정 전 입니다.')
        else:
            if self.cNum > self.uNum:
                print(f'컴퓨터 VS 유저 : {self.cNum} VS {self.uNum} >> 컴퓨터 승!!')

            elif self.cNum < self.uNum:
                print(f'컴퓨터 VS 유저 : {self.cNum} VS {self.uNum} >> 유저 승!!')

            elif self.cNum == self.uNum:
                print(f'컴퓨터 VS 유저 : {self.cNum} VS {self.uNum} >> 무승부!!')