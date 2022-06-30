# 상품 구매에 따라 할인율이 결정되는 모듈 만들기

import discount as ds
if __name__ == '__main__':
    sh = []
    flag = True
    while flag:
        a = int(input('상품을 구매 하시겠어요? 1.구매 2.종료 '))
        if a == 1:
            p = int(input('상품 가격 입력 : '))
            sh.append(p)
            continue
        elif a == 2:
            res = ds.calTotalPrice(sh)
            flag = False

    print(f'할인율 : {res[0]}%')
    print(f'합계 : {res[1]}원')



#import sale
#sale.getSale(sh)


