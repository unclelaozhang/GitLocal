# temp = input('please type a No:')
# number = int(temp)
# while number:
#     i = number - 1
#     while i:
#         print(' ', end = "")
#         i = i - 1
#     j = number
#     while j:
#         print("*", end = "")
#         j = j - 1
#     print()
#     number = number - 1

temp = input('please type a no:')
number = int(temp)
while number:
    i = number - 1
    while i:
        print(" ", end = "")
        i = i - 1
    j = number
    while j:
        print("*", end = '')
        j = j - 1
    print()
    number = number - 1