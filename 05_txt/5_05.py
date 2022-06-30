
sh1 = 3
sh2 = 4
sh3 = 5
max_day = 0  #최대공약수

for i in range(1, (sh1 + 1)):
    if sh1 % i == 0 and sh2 % i == 0:
        max_day = i

min_day = (sh1 * sh2) // max_day   #최소공배수

new_day = min_day
for i in range(1, (new_day+1)):
    if new_day % i == 0 and sh3 % i == 0:
        max_day = i

min_day = (new_day * sh3) // max_day  # 3개 배의 최소 공배수

print(f'min_day : {min_day}')
print(f'max_day : {max_day}')


from datetime import datetime
from datetime import timedelta   #날짜 계산과 관련된 모듈

n = 1
base_time = datetime(2021, 1, 1, 10, 0, 0) # 시준 날짜, 시간을 임의로 지정 가능(2021년 1월 1일 10시 0분 0초)

with open('C:/pythonEX/txt/arrive.txt', 'a') as f:
    f.write(f'2021년 모든 선박 입항일\n')
    f.write(f'{base_time}\n')


next_time = base_time + timedelta(days=min_day)
while True:

    with open('C:/pythonEX/txt/arrive.txt', 'a') as f:
        f.write(f'{next_time}\n')

    next_time += timedelta(days=min_day)

    if next_time.year > 2021:
        break


