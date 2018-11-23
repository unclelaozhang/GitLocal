score = int(input('请输入一个分数：'))
if 80 > score >= 60:
    print("c")
elif 90 > score >= 80:
    print('b')
elif 60 > score >= 0:
    print('d')
elif 100 >= score >= 90:
    print('a')
else:
    print("输入错误")