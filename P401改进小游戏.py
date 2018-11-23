import random
secret = random.randint(1, 10)
guess = 0
print("来，猜猜看！我心里想的数字是几？", end="")
times = 5
while (guess != secret) and (times > 0):
    temp = input("来，在这儿输入：")
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print('恭喜你，答对了！')
        print('答对也是白答，没有奖金的喽！')
    else:
        if guess > secret:
            print('大了大了')
        else:
            print('小了小了', end="")
        if times > 0:
            print("再来一次!", end="")
        else:
            print('机会用完喽，下次再玩吧')
print('游戏结束，欢迎下次再玩儿')
