# 비행기 티켓 영수증 출력 함수
c_price = 18000
i_price = 25000
a_price = 50000
dis = 0.5

def airplane(c1, c2, i1, i2, a1, a2):

    cp = c1 * c_price
    cp_dc = int(c2 * c_price * dis)
    ip = i1 * i_price
    ip_dc = int(i2 * i_price * dis)
    ap = a1 * a_price
    ap_dc = int(a2 * a_price * dis)

    total_count = c1 + c2 + i1 + i2 + a1 + a2
    total_price = cp + cp_dc + ip + ip_dc + ap + ap_dc

    print('='*60)
    print('유아 {}명 요금 : {}원'.format(c1, format(cp, ',')))
    print('유아 할인 대상 {}명 요금 : {}원'.format(c2, format(cp_dc, ',')))

    print('소아 {}명 요금 : {}원'.format(i1, format(ip, ',')))
    print('소아 할인 대상 {}명 요금 : {}원'.format(i2, format(ip_dc, ',')))

    print('성인 {}명 요금 : {}원'.format(a1, format(ap, ',')))
    print('성인 할인 대상 {}명 요금 : {}원'.format(a2, format(ap_dc, ',')))
    print('='*60)
    print(f'Total: {total_count}명')
    print('TotalPrice: {}원'.format(format(total_price, ',')))
    print('='*60)



print('childPrice(24개월 미만)\t:\t{}'.format(c_price, ','))
print('infantPrice(만12세 미만)\t:\t{}'.format(i_price, ','))
print('adultPrice(만12세 이후)\t:\t{}'.format(a_price, ','))
print('국가 유공자 및 장애우 할인\t:\t{}%'.format(dis*100))

mc1 = int(input('유아 입력 : '))
mc2 = int(input('할인대상유아 입력 : '))
mi1 = int(input('소아 입력 : '))
mi2 = int(input('할인대상 소아 입력 : '))
ma1 = int(input('성인 입력 : '))
ma2 = int(input('할인대상 성인 입력 : '))

airplane(mc1, mc2, mi1, mi2, ma1, ma2)


