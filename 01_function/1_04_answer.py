# 1.
'''
def factorial(n):
    if n == 1:
        return n

    return n * factorial(n - 1)


# 함수 안에서 자기 자신을 부르는 것을 '재귀 함수' 라고 한다

num = int(input('input number : '))
print(format(factorial(num), ','))
'''

# 2.
#단리
def singleRate(m, t, r):
    total_money = 0
    total_rate_money = 0

    for i in rage(t):
        total_rate_money += m * (r * 0.01)

    total_money = m + total_rate_money
    return int(total_money)

#월복리
def multiRate(m, t, r):
    t = t * 12
    rpm =(r / 12) * 0.01

    totalMoney = m

    for i in range(t):
        totalMoney += totalMoney * rpm

    return int(totalMoney)

