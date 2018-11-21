import random

times = 3
secret = random.randint(1,10)

print('..........i love laozhang........')
guess = 0
print('guess the no I\'m thinking.')

while guess != secret and times > 0:
    temp = input()

    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print('NB')
        else:
            if guess > secret:
                print("bigger")
            else:
                print('smaller')
            if times > 1:
                print("once again")
            else:
                print("no chance any more")
    else:
        print("please enter a no.")

    times = times - 1
print("Game over")



