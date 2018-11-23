# import random
# times = 3
# secret = random.randint(1, 10)
# guess = 0
# print("guess the no")
# while (guess != secret) and times > 0:
#     temp = input("please type a no you guessed ")
#     guess = int(temp)
#     times = times -1
#     if guess == secret:
#         print('good')
#     else:
#         if guess > secret:
#             print('bigger')
#         else:
#             print('smaller')
#         if times > 0:
#             print('once more')
#         else:
#             print('no chance any more')
# print('game over')


import random
secret = random.randint(1, 10)
times = 3
guess = 0
while (guess != secret) and times > 0:
    temp = input('please type a no')
    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print('good')
        else:
            if guess > secret:
                print('bigger')
            else:
                print("smaller")
            if times > 0:
                print("once again")
            else:
                print("no any more chance")
    else:
        print("输入有误，请重新输入一个整数")
    times = times - 1
print('game over')
