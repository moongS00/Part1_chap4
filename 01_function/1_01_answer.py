def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def div(n1, n2):
    return n1 / n2

def mul(n1, n2):
    return n1 * n2

def mod(n1, n2):
    return n1 % n2

def flo(n1, n2):
    return n1 // n2

def exp(n1, n2):
    return n1 ** n2


while True:
    print('*'*60)
    type = int(input('1.덧셈\t2.뺄셈\t3.곱셈\t4.나눗셈\t5.나머지\t6.몫\t7.제곱승\t8.종료\t'))
    if type == 8:
        print('Bye~')
        break

    num1 = float(input('첫 번째 숫자 입력: '))
    num2 = float(input('두 번째 숫자 입력: '))

    if type == 1:
        print(f'{num1} + {num2} = {add(num1, num2)}')

    elif type == 2:
        print(f'{num1} - {num2} = {sub(num1, num2)}')

    elif type == 3:
        print(f'{num1} * {num2} = {mul(num1, num2)}')

    elif type == 4:
        print(f'{num1} / {num2} = {div(num1, num2)}')

    elif type == 5:
        print(f'{num1} % {num2} = {mod(num1, num2)}')

    elif type == 6:
        print(f'{num1} // {num2} = {flo(num1, num2)}')

    elif type == 7:
        print(f'{num1} ** {num2} = {exp(num1, num2)}')

    else:
        print('잘못 입력하셨습니다. 다시 입력하세요.')

    print('*'*60)

