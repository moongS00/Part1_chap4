# 조합 계산 모듈 만들기
import combination as cb

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))
# logPrint = False 로 하면 로그는 출력되지 않음
print(f'{numN}C{numR}: {cb.getCombination(numN, numR, logPrint=False)}')


livar = [1, 2, 3, 4, 5, 6, 7, 8]
rvar = 5
cb.getCombi(livar, rvar)