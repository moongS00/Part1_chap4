# 공과금총액과 수입 대비 공과금 비율 계산

inc = int(input('수입 입력 :'))
b1 = int(input('수도요금 입력 :'))
b2 = int(input('전기요금 입력 :'))
b3 = int(input('가스요금 입력 :'))

import bill

bill.calBill(b1, b2, b3, inc)