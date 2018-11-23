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

#定义密码使用的字符范围
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums ='0123456789'
password = input('请输入您要设置的密码：')

#判断密码长度
length = len(password)
while password.isspace() or length == 0:
	password = input('您输入的密码为空（或空格），请重新输入：')
	length = len(password)
if length <= 8:
	flag_len = 1
elif length <= 16:
	flag_len = 2
else:
	flag_len = 3
flag_con = 0
#判断是否包含特殊字符
for each in password:
	if each in symbols:
		flag_con += 1
		break
#判断是否包含字母
for each in password:
	if each in chars:
		flag_con += 1
		break
#判断是否包含数字
for each in password:
	if each in nums:
		flag_con += 1
		break
print(flag_con)
while 1:
	print('您的密码安全级别评定为：', end = ' ')
	if flag_len == 1 or  flag_con == 1:
		print('低')
	elif flag_con == 2 or flag_len == 2:
		print('中')
	else:
		print('高')
		print('请继续保持')
		break
	print('''请按以下方式提升您的密码安全级别：
	\t1.密码必须由数字、字母及特殊字符三种组合
	\t2.密码只能由字母开头
	\t3.密码长度不能低于16位''')
	break





