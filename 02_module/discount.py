#02번 강의 그대로
def calTotalPrice(gs):

    if len(gs) <= 0:
        print('구매 상품이 없습니다.')
        return

    rate = 25
    total_price = 0

    rates = {1:5, 2:10, 3:15, 4:20}

    if len(gs) in rates:
        rate = rates[len(gs)]

    for g in gs:
        total_price += g * (1 - rate/100)

    return [rate, int(total_price)]