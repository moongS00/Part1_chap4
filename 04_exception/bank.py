class ExceptionshortMoney(Exception):
    def __init__(self, mm, wm):
        super().__init__(f'잔고부족!!, 잔액: {mm}, 출금액: {wm}')




import random


class Bank:

    def __init__(self):
        self.accounts = {}

    def addAccount(self, privateBank):   # 내가 등록한 은행을 리스틍에 추가
        self.accounts[privateBank.account_no] = privateBank

    def isAccount(self, ano):    # 계좌번호가 이미 존재하는 지 확인
        return ano in self.accounts

    def doDeposit(self, ano, m):  # 예금
        pb = self.accounts[ano]
        pb.totalMoney += m

    def doWithdraw(self, ano, m):  # 출금
        pb = self.accounts[ano]
        if pb.totalMoney - m < 0:
            raise ExceptionshortMoney(pb.totalMoney, m)
        else:
            pb.totalMoney -= m


class PrivateBank:   # 개인계좌 만들기(은행명, 이름만 넣으면 계좌번호와 잔액은 자동으로 생성됨)
    def __init__(self, bank, account_name):
        self.bank = bank
        self.account_name = account_name

        while True:
            newAccountno = random.randint(10000, 99999)
            if bank.isAccount(newAccountno):             # 계좌번호가 안겹치도록 하는 작업
                continue
            else:
                self.account_no = newAccountno
                break

        self.totalMoney = 0
        bank.addAccount(self)                               # 내 통장 개설 후 은행에 등록

    def printBankInfo(self):
        print('-'*40)
        print(f'account_name : {self.account_name}')
        print(f'account_no : {self.account_no}')
        print(f'TotalMoney : {self.totalMoney}원')
        print('-' * 40)



