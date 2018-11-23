# trypassword = "guess"
# password = "ILOVEYOU"
# times = 3
# while (trypassword != password)  and times > 0:
#     trypassword = input('please enter password here：')
#     times = times - 1
#     if trypassword == password:
#         print('密码正确，进入程序......')
#     elif (trypassword != password)  and (times == 2):
#         print('密码输入错误，您还有2次机会！')
#     elif (trypassword != password)  and (times == 1):
#         print('密码输入错误，您还有1次机会')
#     elif (trypassword != password) and (times == 0):
#         print("您尝试的次数过多，账号已锁定，请联系您的系统管理员处理！")

# count = 3
# password = "Iloveyou"
#
# while count:
#     psd = input('please enter password here:')
#     if psd == password:
#         print("password is correct,loading......")
#         break
#     elif '*' in psd:
#         print("'*' is not allowed in password,you have", count, 'chances remain.')
#         continue
#     else:
#         print('wrong password', count - 1, "chances remain")
#     count = count - 1

count = 3
password = "Iloveyou"
while count:
    psd = input("pls enter your password here:")
    if psd == password:
        print('password correct, please wait \nloading........')
        break
    elif '*' in psd:
        print("'*'is not allowed,you have", count, "chances remained.please retry")
        continue
    else:
        print('wrong password,you have', count - 1 ,'chances remain,please retry')
    count = count - 1


