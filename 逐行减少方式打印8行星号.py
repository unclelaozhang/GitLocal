temp = input('请输入一个整数:')
number = int(temp)
while number:  # number=循环的次数=输入的数值
    i = number - 1  # 每循环一次即从输入数值中减少一次;子循环的初始值为number -1;
    while i:  # 循环i次
        print(' ', end = '') # 打印空格，不换行
        i = i - 1
    j = number # 循环次数=输入的数值
    while j:
        print('*', end = '')
        j = j - 1
    print()
    number = number - 1