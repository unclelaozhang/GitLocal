name = input('请输入要查询的用户名：')
score = [['张三', 85],['李四', 92],['王五', 87],['赵六', 95],['王二麻子', 100]]

IsFind = False

for each in score:
    if name in each:
        print(name, '的分数是', each[1])
        IsFind = True
        break
if IsFind == False:
    print('查找的数据不存在')