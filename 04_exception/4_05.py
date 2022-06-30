import bank

koreaBank = bank.Bank()


new_account_name = input('통장 개설을 위한 예금주 입력 : ')
my_account = bank.PrivateBank(koreaBank, new_account_name)
my_account.printBankInfo()


while True:
    sn = int(input('1.입금\t2.출금\t3.종료\t'))
    if sn == 1:
        m = int(input('입금액 입력 : '))
        koreaBank.doDeposit(my_account.account_no, m)
        my_account.printBankInfo()

    elif sn == 2:
        m = int(input('출금액 입력 : '))
        try:
            koreaBank.doWithdraw(my_account.account_no, m)
            my_account.printBankInfo()
        except bank.ExceptionshortMoney as e:
            print(e)

        finally:
            my_account.printBankInfo()

    elif sn == 3:
        print('Bye~')
        break

    else:
        print('잘못 입력했습니다. 다시 입력해주세요')
