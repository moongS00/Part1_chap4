# 두개의 수를 입력받아 공약수 기록하기
'''
num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

cm = []

for i in range(1, (num1+1)):
    if num1 % i == 0 and num2 % i == 0:
        cm.append(i)

if len(cm) > 0:
    try:
        with open('C:/pythonEX/txt/common.txt', 'a') as f:
            f.write(f'{num1}와 {num2}의 공약수 : {cm} \n')

    except Exception as e:
        print(e)

    else:
        print('common factor write complete!')

'''

# 최대공약수

num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

max_cm = 0

for i in range(1, (num1+1)):
    if num1 % i == 0 and num2 % i == 0:
        max_cm = i


try:
    with open('C:/pythonEX/txt/maxcm.txt', 'a') as f:
        f.write(f'{num1}와 {num2}의 최대공약수 : {max_cm} \n')

except Exception as e:
    print(e)

else:
    print('common factor write complete!')
