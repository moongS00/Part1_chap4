import  diary

members = {}

uri = 'C:/pythonEX/txt/'

def printMembers():
    for m in members.keys():
        print(f'ID : {m}, PW : {members[m]}')




while True:
    sn = int(input('1.회원가입 2.한줄일기쓰기 3.일기보기 4.종료 '))

    if sn == 1:
        mid = input('input ID : ')
        mpw = input('input PW : ')
        members[mid] = mpw
        printMembers()

    elif sn == 2:
        mid = input('input ID : ')
        mpw = input('input PW : ')

        if mid in members and members[mid] == mpw:
            print('login success!!')
            file_name = 'myDiary_' + mid + '.txt'
            data = input('오늘 하루 인상깊은 일을 기록하세요 : ')
            diary.writeDiary(uri, file_name, data)

        else:
            print('login fail!!')
            printMembers()


    elif sn == 3:
        mid = input('input ID : ')
        mpw = input('input PW : ')

        if mid in members and members[mid] == mpw:
            print('login success!!')
            file_name = 'myDiary_' + mid + '.txt'
            datas = diary.readDiary(uri, file_name)
            for d in datas:
                print(d, end='')

        else:
            print('login fail!!')
            printMembers()


    elif sn == 4:
        print('Bye~')
        break

