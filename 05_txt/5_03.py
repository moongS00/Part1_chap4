# 1. 사용자가 입력한 숫자의 약수 기록하기
'''
n = int(input('0보다 큰 정수 입력 : '))
d = []


for i in range(1, n+1):
    if n % i == 0:
        d.append(i)
    else:
        continue

if len(d) > 0:
    try:
        with open('C:/pythonEX/txt/divisor.txt', 'a') as f:
            f.write(f'{n}의 약수 : {d} \n')

    except Exception as e:
        print(e)

    else:
        print('divisor write complete!')

'''



# 2. 사용자가 입력한 숫자까지의 소수 기록하기

num = int(input('0보다 큰 정수 입력 : '))
p = []


for i in range(2, num+1):
    flag = True
    for n in range(2, i):
        if i % n == 0:
            flag = False
            break

    if flag:
        p.append(i)

if len(p) > 0:
    try:
        with open('C:/pythonEX/txt/prime.txt', 'a') as f:
            f.write(f'{num}까지의 소수 : {p} \n')

    except Exception as e:
        print(e)

    else:
        print('prime write complete!')







