import member as mb

mems = mb.MemberResitory()

for i in range(3):
    od = input('아이디 입력: ')
    pw = input('비번 입력: ')

    mem = mb.Member(od, pw)
    mems.addMember(mem)

mems.printMembers()
''''''
mems.loginMember('dfkajfk#lkfdfn', '6840')
mems.removeMember('dfkajfk#lkfdfn', '6840')
mems.printMembers()