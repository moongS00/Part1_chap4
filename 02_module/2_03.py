import lottery

if __name__ == '__main__':
    lo = []
    for i in range(1,6):
        a = int(input('번호(1~45) 입력 : '))
        lo.append(a)

    res = lottery.LotteryMatch(lo)
    print(f'기계 번호 : {res[0]}')
    print(f'보너스 번호 : {res[1]}')
    print(f'선택 번호 : {res[2]}')
    print(f'일치 번호 : {res[3]}')