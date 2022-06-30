
class Empty(Exception):      # 에러 클래스
    def __init__(self, i):
        super().__init__(f'{i} is empty')


def checkInput(n, m, p, a, ph):   # 유효성 체크 함수, 비밀번호 길이, 아이디 형식 등도 조건에 넣을 수 있음

    if n == '':
        raise Empty('name')
    
    elif m == '':
        raise Empty('mail')

    elif p == '':
        raise Empty('password')

    elif a == '':
        raise Empty('address')

    elif ph == '':
        raise Empty('phone')



class registMember():                    # 회원가입 클래스
    def __init__(self, n, m, p, a, ph):
        self.m_name = n
        self.m_mail = m
        self.m_pw = p
        self.m_addr = a
        self.m_phone = ph
        print('Membership complete!!')

    def printMemberInfo(self):
        print(f'm_name : {self.m_name}')
        print(f'm_mail : {self.m_mail}')
        print(f'm_pw : {self.m_pw}')
        print(f'm_addr : {self.m_addr}')
        print(f'm_phone : {self.m_phone}')