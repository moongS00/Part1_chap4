m_name = input('이름 입력: ')
m_mail = input('메일 주소 입력: ')
m_pw = input('비밀번호 입력: ')
m_addr = input('주소 입력: ')
m_phone = input('연락처 입력: ')


import login
try:
    login.checkInput(m_name, m_mail, m_pw, m_addr, m_phone)
    new_m = login.registMember(m_name, m_mail, m_pw, m_addr, m_phone)  # 에러가 나지 않은 경우
    new_m.printMemberInfo()
except login.Empty as e:
    print(e)
