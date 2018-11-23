temp = input('请输入一个整数：')
number = int(temp)
i = 10          # 循环的初始数值为 1
while number:  # number值为10则循环10次，为5则循环5次。
    print(i)
    i = i - 1  # 每次循环在原数值的基础上+1
    number = number - 1

