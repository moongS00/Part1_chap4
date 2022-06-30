import time


def writeDiary(u, f, d):    # u: url / f: 파일명
    lt = time.localtime()
    time_str = time.strftime('%Y-%m-%d %I:%M:%S %p', lt)


    file_path = u + f
    with open(file_path, 'a') as f:
        f.write(f'[{time_str}] {d}\n')



def readDiary(u, f):
    file_path = u + f
    datas = []
    with open(file_path, 'r') as f:
        datas = f.readlines()

        return datas
