#有红、黄、蓝三种颜色的球，其中红球3个，黄球3个，绿球6个。先将这12个球混合放在一个盒子中，从中任意摸出8个球，
# 编程计算出球的各种颜色搭配。

# red = 3
# yellow = 3
# green = 6
# balls = red + yellow + green
#
# print('red\tyellow\tgreen')
# for red in range(1,4):
#     for yellow in range(1,4):
#         for green in range(2,7):
#             if red + yellow +green == 8:
#                 print(red,'\t',yellow,'\t',green)

print('red\tyellow\tgreen')
for red in range(1,4):
    for yellow in range(1,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                print(red,'\t', yellow,'\t\t',green)