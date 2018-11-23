#打印100以内的奇数之和

# sum = 0
# n = 1
# while n <= 99:
#     sum = sum + n
#     n = n + 2
# print(sum)

#打印100以内的偶数之和
sum = 0
n= 0
while n <= 100:
    sum = sum + n
    n = n + 2
print(sum)

#利用循环依次打印LIST中的内容：
L = ['Bart', 'Lisa', 'Adam']

for x in L:
    print("hello,",x)

#打印1到100的整数：
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
#打印1到10的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

