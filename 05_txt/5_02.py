import time


def getTime():
    lt = time.localtime()
    st = time.strftime('%Y-%m-%d %I:%M:%S %p', lt)

    return st


while True:
    sn = int(input('1.입금\t2.출금\t3.종료\t'))

    if sn == 1 :
        money = int(input('입금액 입력 : '))
        with open('C:/pythonEX/txt/mon.txt', 'r') as f:
            m = f.read()

        with open('C:/pythonEX/txt/mon.txt', 'w') as f:
            f.write(str(int(m) + money))

        memo = input('입금 내역 입력 : ')
        with open('C:/pythonEX/txt/pocketMoney.txt', 'a') as f:
            f.write('-' * 50+'\n')
            f.write(f'{getTime()} \n')
            f.write(f'[입금] {memo} : {str(money)}원 \n')
            f.write(f'[잔액] {str(int(m) + money)}원\n')

        print('입금 완료!')
        print(f'기존 잔액: {m}원')
        print(f'입금 후 잔액: {int(m) + money}원')

    elif sn == 2:
        money = int(input('출금액 입력 : '))
        with open('C:/pythonEX/txt/mon.txt', 'r') as f:
            m = f.read()

        with open('C:/pythonEX/txt/mon.txt', 'w') as f:
            f.write(str(int(m) - money))

        memo = input('출금 내역 입력 : ')
        with open('C:/pythonEX/txt/pocketMoney.txt', 'a') as f:
            f.write('-' * 50 + '\n')
            f.write(f'{getTime()} \n')
            f.write(f'[출금] {memo} : {str(money)}원 \n')
            f.write(f'[잔액] {str(int(m) - money)}원\n')

        print('출금 완료!')
        print(f'기존 잔액: {m}원')
        print(f'출금 후 잔액: {int(m) - money}원')

    elif sn == 3:
        print('Bye~')
        break

    else:
        print('다시 입력하세요')


