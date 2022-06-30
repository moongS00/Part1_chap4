def getSale(gs):
    count = len(gs)
    price = 0
    if count == 1:
        rate = 5

    elif count == 2:
        rate = 10

    elif count == 3:
        rate = 15

    elif count == 4:
        rate = 20

    elif count >= 5:
        rate = 25

    print(f'할인율(%) : {rate}')

    for i in range(0, len(gs)):
        price += gs[i]

    final_price = int(price - price * (rate/100))
    fp = format(final_price, ',')

    print(f'합계 : {fp}원')