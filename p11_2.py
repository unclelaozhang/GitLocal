import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def Move(self):
        #这里主要演示类的继承机制,就不考虑检查场景边界和移动方向的问题
        #假设所有鱼都是一路向西游
        self.x -= 1
        print('我的位置是：', self.x, self.y)

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有得吃^_^')
            self.hungry = False
        else:
            print("太撑了，吃不下！")

