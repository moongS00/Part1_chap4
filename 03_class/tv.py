class NormalTv:
    def __init__(self, inch = 32, color = 'black', r = 'Full-HD'):
        self.inch = inch
        self.color = color
        self.resolution = r
        self.smartTv = 'off'
        self.aiTv = 'off'

    def turnOn(self):
        print('TV power On!')

    def turnOff(self):
        print('TV power Off!')

    def printTvInfo(self):
        print(f'inch : {self.inch}inch')
        print(f'color : {self.color}')
        print(f'resolution : {self.resolution}')
        print(f'smartTv : {self.smartTv}')
        print(f'aiTv : {self.aiTv}')


class Tv4K(NormalTv):
    def __init__(self, inch, color, r = '4k'):
        super().__init__(inch, color, r)   #상속받은 속성값을 변경

    def setSmartTv(self, s):
        self.smartTv = s


class Tv8K(NormalTv):
    def __init__(self, inch, color, r = '8k'):
        super().__init__(inch, color, r)

    def setSmartTv(self, s):
        self.smartTv = s

    def serAiTv(self, a):
        self.aiTv = a