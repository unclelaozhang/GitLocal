temp = input('请输入一个年份')
while not temp.isdigit():
    temp = input("抱歉，你的输入有误，请输入一个整数：")
year = int(temp)
times = 5
if year/400 == int(year/400):
    print(temp + '是闰年')
else:
    if (year/4 == int(year/4)) and (year/100 != int(year/100)):
        print(temp + '是闰年')
    else:
        print(temp + '不是闰年')

I think I have forgotten the learning 