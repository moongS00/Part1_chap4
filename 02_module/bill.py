
def calBill(b1, b2, b3, income):
    total_bill = b1 + b2 + b3
    pro = (total_bill/income) * 100
    tb = format(total_bill, ',')
    print(f'공과금 : {tb}')
    print(f'공과금 비율 : {pro}%')