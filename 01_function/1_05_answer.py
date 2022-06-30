# 등차수열의 n번째 값과 합을 출력하는 함수
# 등차수열 공식: an = a1 + (n-1) * d
# 등차수열 합 공식: sn = n * (a1 + an) / 2

# 뒤의 등비수열도 동일하게 푼다
# 등비수열 공식: an = a1 * r^(n-1)
# 등비수열 합 공식: sn = a1 * (1-r^n) / (1-r)

def swquenceCal(n1, d, n):

    valueN = 0;
    sumN = 0

    i = 1
    while i <= n:
        if i == 1:
            valueN = n1
            sumN += valueN
            print(f'{i}번째 항의 값: {valueN}')
            print(f'{i}번째 항까지의 합: {sumN}')

            i += 1
            continue

        valueN += d
        sumN += valueN
        print(f'{i}번째 항의 값: {valueN}')
        print(f'{i}번째 항까지의 합: {sumN}')

        i += 1

ma1 = int(input('a1 입력 : '))
md = int(input('공차 입력 : '))
mn = int(input('n 입력 : '))

swquenceCal(ma1, md, mn)