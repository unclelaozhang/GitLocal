def power(x,n):
    s = 1
    for i in range(n):
        s = s * x
    return s
y = power(2,4)
print(y)