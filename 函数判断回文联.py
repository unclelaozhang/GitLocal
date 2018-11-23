# 方法一
# def palindrome(string):
#     list1 = list(string)
#     list2 = reversed(list1)
#     if list1 == list(list2):
#         return '是回文联'
#     else:
#         return '不是回文联'
#
# test = input('请在此输入您的对联：')
# print(palindrome(test))

#方法二
# def palindrome(string):
#     length = len(string)
#     last = length - 1
#     #length //= 2
#     flag = 1
#     for each in range(length):
#         if string[each] != string[last]:
#             flag = 0
#         last = last - 1
#
#     if flag == 1:
#         return 1
#     else:
#         return 0
# string = input('请输入一句话：')
# if palindrome(string) == 1:
#     print('是回文联')
# else:
#     print('不是回文联')
# def palindrome(n,start,end):
#     if start > end:
#         return 1
#     else:
#         return palindrome(n,start+1, end-1) if n[start]
# == n[end] else 0


