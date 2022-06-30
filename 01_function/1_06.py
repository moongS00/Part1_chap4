# 등비수열의 값과 합을 출력


def printLine(a1, r, n):
    k = a1
    sum = a1
    for i in range(1, n + 1):
        print(f'{i}번째 항의 값: {k}')
        print(f'{i}번째 항까지의 합: {sum}')
        k *= r
        sum += k

ma1 = int(input('a1 입력 : '))
md = int(input('공비 입력 : '))
mn = int(input('n 입력 : '))

printLine(ma1, md, mn)