#순열 공식 : nPr = n! / (n-r)!
import math
def VarPermutation(n, r):
    res = math.factorial(n) / math.factorial(n - r)
    print(f'{n}P{r} 개수 : {res}')


from itertools import permutations    # 순열 경우 조합을 구해주는 함수가 들어있음

def ListPermutation(n, r):
    pList = list(permutations(n, r))
    print(f'{len(n)}P{r} 개수 : {len(pList)}')

    for n in permutations(n, r):
        print(n, end='')



