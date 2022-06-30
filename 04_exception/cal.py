def add(n1, n2):
    print('덧셈 연산')
    try:
        n1 = float(n1)
    except:
        print('n1은 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('n2는 숫자가 아닙니다.')
        return

    print(f'{n1} + {n2} = {n1 + n2}')

def sub(n1, n2):
    print('뺄셈 연산')
    try:
        n1 = float(n1)
    except:
        print('n1은 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('n2는 숫자가 아닙니다.')
        return

    print(f'{n1} - {n2} = {n1 - n2}')

def mul(n1, n2):
    print('곱셈 연산')
    try:
        n1 = float(n1)
    except:
        print('n1은 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('n2는 숫자가 아닙니다.')
        return

    print(f'{n1} * {n2} = {n1 * n2}')

def div(n1, n2):
    print('나눗셈 연산')
    try:
        n1 = float(n1)
    except:
        print('n1은 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('n2는 숫자가 아닙니다.')
        return

    try:
        print(f'{n1} / {n2} = {n1 / n2}')
    except:
        print('0으로 나눌 수 없습니다.')


def mod(n1, n2):
    print('나머지 연산')
    try:
        n1 = float(n1)
    except:
        print('n1은 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except:
        print('n2는 숫자가 아닙니다.')
        return

    try:
        print(f'{n1} % {n2} = {n1 % n2}')
    except ZeroDivisionError as e:
        print(e)
        print('0으로 나눌 수 없습니다.')


def flo(n1, n2):
    print('몫 연산')
    try:
        n1 = float(n1)
    except:
        print('n1은 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except ZeroDivisionError as e:
        print(e)
        print('n2는 숫자가 아닙니다.')
        return

    try:
        print(f'{n1} // {n2} = {n1 // n2}')
    except:
        print('0으로 나눌 수 없습니다.')


def exp(n1, n2):
    print('거듭제곱 연산')
    try:
        n1 = float(n1)
    except:
        print('n1은 숫자가 아닙니다.')
        return

    try:
        n2 = float(n2)
    except ZeroDivisionError as e:
        print(e)
        print('n2는 숫자가 아닙니다.')
        return

    print(f'{n1} ** {n2} = {n1 ** n2}')