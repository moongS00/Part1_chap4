import random
import prime as pm

primenumbers = []

n = 0
while n < 10:
    rn = random.randint(2, 1000)
    if rn not in primenumbers:
        try:
            pm.isPrime(rn)
        except pm.NoPrimeException as e:
            print(e)
            continue

        except pm.PrimeException as e:
            print(e)
            primenumbers.append(rn)

    else:
        print(f'{rn} is overlap number.')
        continue

    n += 1


print(f'primenumbers : {primenumbers}')