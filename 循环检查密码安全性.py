# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
met = 1
while met:
    password = input('please enter your password here:')
    length = len(password)
    while length == 0 or password.isspace():
        print("your enter is empty or space.", end = ' ')
        password = input('please re-enter your password here:')
        length = len(password)

    if length <= 8:
        len_flag = 1
    elif length < 16:
        len_flag = 2
    else:
        len_flag = 3

    flag_con = 0
    for each in password:
        if each in symbols:
            flag_con += 1
            break
    for each in password:
        if each in chars:
            flag_con += 1
            break
    for each in password:
        if each in nums:
            flag_con += 1
            break
    if password[0] in chars:
        flag_con += 1

    while 1:
        print("your password security level is:", end=" ")
        if len_flag == 1 or flag_con == 1:
            print('lower')
            print('''please update your password follow the rules below:
                          1.there must be 3 classes char group
                          2.char first
                          3.more than 16 chars''')
        elif len_flag ==2 or flag_con ==3:
            print("middle")
            print('''please update your password follow the rules below:
                          1.there must be 3 classes char group
                          2.char first
                          3.more than 16 chars''')
        else:
            print('High')
            print('good,keep it on ')
            met = 0
        break





