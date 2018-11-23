成绩 = input('请在此处输入您的分数：')
分数 = int(成绩)
if 分数<0 or 分数>100:
    print("输入错误")
elif 分数>= 90:
    print('您的成绩为A等')
elif 分数>= 80:
    print('您的成绩为B等')
elif 分数 >= 70:
    print('您的成绩为C等')
elif 分数 >= 60:
    print('你的成绩为D等')
else:
    print('您的成绩让人伤心')

