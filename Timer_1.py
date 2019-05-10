import time as t

class MyTimer:
    # start timer
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()开始计时！"
        print('start')
    #stop timer
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("stop")
    #internal method, count the runnnig time
    def _calc(self):
        self.lasted = []
        self.prompt = "totally running time"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        print(self.prompt)
    #为下一轮计算初始化变量
        self.begin = 0
        self.end = 0

    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "have not start"
        self.lasted = []
        self.begin = 0
        self.end = 0




