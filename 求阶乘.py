# def factorial(n):
#     result = n
#     for i in range(1, n):
#         result = result * i
#     return  result
#
# number = int(input("请输入一个正整数："))
# result = factorial(number)
#
# print("%d的阶乘是%d" % (number,result))

def recursion(n):
    if n == 1:
        return n
    else:
        return n * recursion(n-1)
number = int(input("请输入一个正整数："))
result = recursion(number)

print("%d的阶乘是%d" % (number,result))

