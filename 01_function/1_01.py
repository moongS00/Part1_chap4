# 산술연산 계산기 만들기
def cal(type, n1, n2):
    if type == 1:
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))

    elif type == 2:
        print('{} - {} = {}'.format(n1, n2, (n1 - n2)))

    elif type == 3:
        print('{} * {} = {}'.format(n1, n2, (n1 * n2)))

    elif type == 4:
        print('{} / {} = {}'.format(n1, n2, (n1 / n2)))

    elif type == 5:
        print('{} % {} = {}'.format(n1, n2, (n1 % n2)))

    elif type == 6:
        print('{} // {} = {}'.format(n1, n2, (n1 // n2)))

    elif type == 7:
        print('{} ** {} = {}'.format(n1, n2, (n1 ** n2)))

    elif type == 8:
        print('Bye~')


t = int(input('1.덧셈\t2.뺄셈\t3.곱셈\t4.나눗셈\t5.나머지\t6.몫\t7.제곱승\t8.종료\t'))
n1 = float(input('첫 번째 숫자 입력: '))
n2 = float(input('두 번째 숫자 입력: '))

cal(t, n1, n2)
