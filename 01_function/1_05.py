# 등차수열의 n번째 값과 합을 출력하는 함수


def printLine(a1, d, n):
    k = a1
    sum = a1
    for i in range(1, n + 1):
        print(f'{i}번째 항의 값: {k}')
        print(f'{i}번째 항까지의 합: {sum}')
        k += d
        sum += k



ma1 = int(input('a1 입력 : '))
md = int(input('공차 입력 : '))
mn = int(input('n 입력 : '))

printLine(ma1, md, mn)
