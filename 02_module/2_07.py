

from arithmetic import basic_operator as bo
from arithmetic import developer_operator as do

from shape import circle_area as ca
from shape import tri_squa_area as taa

a1 = float(input('숫자1 입력 : '))
a2 = float(input('숫자2 입력 : '))

bo.add(a1, a2)
bo.sub(a1, a2)
bo.div(a1, a2)
bo.mul(a1, a2)

do.mod(a1,a2)
do.flo(a1,a2)
do.exp(a1,a2)

width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))
taa.triArea(width, height)
taa.squaArea(width, height)
r = float(input('반지름 입력 : '))
ca.cirArea(r)