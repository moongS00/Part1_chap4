#순열 계산 모듈 만들기

import permutation as pt

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))
print(f'{numN}P{numR}: {pt.VarPermutation(numN, numR)}')

livar = [1, 2, 3, 4, 5, 6, 7, 8]
rvar = 3
pt.ListPermutation(livar, rvar)
