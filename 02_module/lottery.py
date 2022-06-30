
import random

def LotteryMatch(li):
    numbers = random.sample(range(1, 46), 7)
    machine = numbers[0:6]
    bonus = numbers[6]
    match = []
    
    for i in li:
        for j in numbers:
            if i == j:
                match.append(i)
            else:
                continue
    if len(match) == 0:
        print('아쉽숩니다. 다음 기회에~')
    else:
        print('{}개 맞았습니다! 축하합니다!'.format(len(match)))

    return [machine, bonus, li, match]
'''

numbers = random.sample(range(1, 45), 7)
machine = numbers[0:5]
bonus = numbers[6]
for i in numbers:
    print(i)

#print(machine)
#print(bonus)
'''
