x = 7 #根据题意，x的最小可能值为7，先从7开始尝试。
i = 1 #开始循环
flag = 0 # 先标记一个false

while i <= 17:#循环尝试不超过100次。
    if (x%2 == 1) and (x%3 == 2) and (x % 5 == 4) and (x % 6 ==5):
        flag = 1 #如果x满足上列条件，就打印X；如果不满足，就根据循环重新为x赋值，每循环一次，系数+1.即i+1.直到满足。
    else:
        x = 7 * (i + 1) #x为7的倍数是必然成立的，因此可作为基础条件。但7的倍数不一定满足if所列条件，因此需要不断尝试，直到满足。
    i += 1
if flag == 1: #此处是比较确认，不是为flag赋值，因此要使用==。
    print("阶梯数是：", x)
else:
    print("在程序限定的范围内找不到答案") #如果我们将循环的次数改为16次，就没有答案。

