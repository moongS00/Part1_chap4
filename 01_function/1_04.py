# 1. 재귀함수를 이용한 팩토리얼 함수 만들기
'''
def makeFactorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i

    return format(res, ',')


num = int(input('input number : '))
print(f'{makeFactorial(num)}')
'''

# 2. 단리/월복리 계산기 함수 만들기
def MoneyCal(money, term, rate):
    short = int(money + (money * rate/100 * term))

    mon_term = 12 * term
    mon_rate = (rate/100) / 12

    mondouble = int(money * ((1 + mon_rate) ** mon_term))

    print('[단리 계산기]')
    print('='*50)
    print('예치금\t:\t{}'.format(format(money, ',')))
    print(f'예치기간\t:\t{term}년')
    print(f'연 이율 \t:\t{rate}%')
    print('-'*50)
    print('{}년 후 총 수령액 : {}원'.format(term, format(short, ',')))
    print('='*50,'\n')

    print('[월복리 계산기]')
    print('=' * 50)
    print('예치금\t:\t{}'.format(format(money, ',')))
    print(f'예치기간\t:\t{term}년')
    print(f'연 이율 \t:\t{rate}%')
    print('-' * 50)
    print('{}년 후 총 수령액 : {}원'.format(term, format(mondouble, ',')))
    print('=' * 50)

m = int(input('예치금(원) : '))
t = int(input('기간(년) : '))
r = int(input('연 이율(%) : '))
MoneyCal(m, t, r)
