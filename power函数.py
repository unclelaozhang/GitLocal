# def power(x,y):
#     return x ** y
#
# print(power(3,-1))
#
# def pw(x,n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(pw(3,-1)) #这个函数不能正确计算负次方

#编写一个递规的算法
def power(x, y):
    if y:
        return x *power(x,y-1)
    else:
        return 1

print(power(3,2))




