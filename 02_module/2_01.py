# 과목별 점수를 입력하면 합격 여부를 출력하는 모듈 만들기
# 평균 60이상 합격, 과락 40

a1 = int(input('과목1 점수 입력: '))
a2 = int(input('과목2 점수 입력: '))
a3 = int(input('과목3 점수 입력: '))
a4 = int(input('과목4 점수 입력: '))
a5 = int(input('과목5 점수 입력: '))

import score

score.scoreCal(a1, a2, a3, a4, a5)


