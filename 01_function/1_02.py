# 이동거리와 이동 시간을 반환하는 함수
# 거리 = 속도 * 시간

def getDistance(speed, hour, minute):
    return speed * (hour + minute / 60)


def getTime(speed, distance):
    time = distance / speed
    h = int(time)
    m = (time - int(time)) * 60

    return [h,m]


print('-'*60)
s = float(input('속도(km/h)입력 : '))
h = float(input('시간(h)입력 : '))
m = float(input('시간(m)입력 : '))
d = getDistance(s, h, m)
print(f'{s}(km/h)속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리: {d}(km)')
print('-'*60)


print('-'*60)
s = float(input('속도(km/h)입력 : '))
d = float(input('거리(km)입력 : '))
t = getTime(s, d)
print(f'{s}(km/h)속도로 {m}(km) 이동한 시간 : {t[0]}(h)시간 {t[1]}(m)분')
print('-'*60)