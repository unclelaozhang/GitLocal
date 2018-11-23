#如果一个3位数等于其各位数之的立方和，则称这个数为水仙花数。例如：153 =1**3+5**3+3**3，153就是一个水仙花数。

for x in range(101,1000):
    sum = 0
    temp = x
    while temp:
        sum = sum + (temp%10)**3
        temp //= 10
    if sum == x:
        print(x)

