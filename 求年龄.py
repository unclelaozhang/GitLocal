
"""有5个人坐在一起，
问第五个人多少岁？
他说比第4个人大2岁。
问第4个人岁数，
他说比第3个人大2岁。
问第三个人，
又说比第2人大两岁。
问第2个人，
说比第一个人大两岁。
最后问第一个人，他说是10岁。
请问第五个人多大？"""


def age(n):
    if n == 1:
        return 10
    else:
        return age(n - 1) + 2


print('哈哈，我知道了，第五个人的年龄是 %d 岁，啵啵脆！' % age(5))


def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1) + 2

print('The fifth guy is %d'  % age(5))
