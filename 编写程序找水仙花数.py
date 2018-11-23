"""如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153=1**3+5**3+3**3，
因此153是一个水仙花数。编写一个程序，找出所有的水仙花数"""

# def Narcissus():
#     for each in range(100,1000):
#         temp = each
#         sum = 0
#         while temp:
#             sum = sum + (temp%10) ** 3
#             temp = temp // 10 #地板除
#
#         if sum == each:
#             print(each,end='\t')
#
# print('所有的水仙花数分别是：',end='')
# Narcissus()

# print([(x*100 + y*10 + z) for x in range(1,10) for y in range(10) for z in range(10)
#        if(x**3 + y**3 + z**3 == x*100 + y*10 + z )])

# for x in range(1,10):
#     for y in range(10):
#         for z in range(10):
#             if x**3 + y**3 + z**3 == x*100 + y*10 + z:
#                 print(x*100 + y*10 + z)
#


def Narcissus():
    for x in range(1, 10):
        for y in range(10):
            for z in range(10):
                if x**3 + y**3 + z**3 == x*100 + y*10 + z:
                    print(x*100 + y*10 + z)
Narcissus()
