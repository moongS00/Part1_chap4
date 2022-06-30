#회원가입 클래스와 회원정보를 관리하는 클래스를 만들고, 회원가입 로그인 기능을 구현해보자

# 회원 1명의 ID, PW를 갖고 있는 클래스
class Member:
    def __init__(self, i, p):
        self.id = i
        self.pw = p

# 모든 회원들을 관리하는 클래스
class MemberResitory:

    def __init__(self):
        self.members = {}   # 딕셔너리형으로 선언 (아이디가 키값, 비번이 VALUE)


    def addMember(self, m):
        self.members[m.id] = m.pw


    def loginMember(self, i, p):
        isMember = i in self.members  # 아이디가 존재하는 경우

        if isMember and self.members[i] == p:  #아이디가 존재 & 비밀번호 맞음
            print(f'{i}: 로그인 성공!')
        else:
            print(f'{i}:로그인 실패!')

    def removeMember(self, i, p):
        del self.members[i]

    def printMembers(self):
        for mk in self.members.keys():
            print(f'ID: {mk}')
            print(f'PW: {self.members[mk]}')