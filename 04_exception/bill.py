g1Price = 1200; g2Price = 1000; g3Price = 800
g4Price = 2000; g5Price = 900

def formatNumber(n):
    return format(n, ',')

def cal(*gcs):

    gcsDic = {}
    ag = {}

    for idx, gc in enumerate(gcs):
        try:
            gcsDic[f'g{idx+1}'] = int(gc)

        except Exception as e:
            ag[f'g{idx+1}'] = gc
            print(e)

    tp = 0
    for g in gcsDic.keys():
        tp += globals()[f'{g}Price'] * gcsDic[g]

    print('-' * 20)
    print(f'총 구매 금액 : {formatNumber(tp)}원')
    print('-' * 5 + '미결제 항목' + '-' * 5)
    for g in ag.keys():
        print(f'상품 : {g}, \t 구매 개수 :{ag[g]}')
    print('-' * 20)
