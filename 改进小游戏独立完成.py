import random
secret =random.randint(1,10)
times = 3
guess = 0
print("来，猜猜哥现在心里想的数字是几.", end="")
while (guess != secret) and (times > 0):
    temp = input('请在此处输入')
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print('恭喜你，答对了!')
        print('哼，答对也没有奖励哦')
    else:
        if guess > secret:
            print('大了大了')
        else:
            print('小了小了')
        if times > 0:
            print('再来一次，')
        else:
            print('对不起，机会用完喽')
print("游戏结束，谢谢参与！")
