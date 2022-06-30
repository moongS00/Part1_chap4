def getCombination(n, r, logPrint = True):

    resP = 1
    resR = 1
    resC = 1

    for n in range(n, (n-r), -1):
        resP = resP * n
        if logPrint: print(f'resP : {resP}')

    for n in range(r, 0, -1):
        resR = resR * n
        if logPrint:print(f'resR : {resR}')

    resC = int(resP / resR)
    if logPrint:print(f'resC : {resC}')

    return resC



from itertools import combinations

def getCombi(ns, r):
    c_list = list(combinations(ns, r))
    print(f'{len(ns)}C{r}: {len(c_list)}')

    for n in combinations(ns, r):
        print(n, end=',')