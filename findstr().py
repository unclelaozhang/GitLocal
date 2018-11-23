"""编写一个函数findstr(),该函数统计一个长度为2的子字符串在另一个字符串中出现的次数。例如：
假定输入的字符串为‘you cannot improve your past,but you can improve your future.
Once time is wasted,life is wasted.', 子字符串为'im',函数执行后打印‘子字母串在目标字符
串中共出现3次’"""
#
# def findstr(desstr, substr):
#     count = 0
#     length = len(desstr)
#     if substr not in desstr:
#         print('在目标字符串中未找到字符串')
#     else:
#         for each1 in range(length-1):
#             if desstr[each1] == substr[0] and desstr[each1+1] == substr[1]:
#                 count = count + 1
#         print('字符串在目标字符串中共出现%d次' % count)
# desstr = input('请输入目标字符串')
# substr = input('请输入子字符串（两个字符）')
# findstr(desstr, substr)

def findstr(desstr, substr):
    count = 0
    length = len(desstr)
    if substr not  in desstr:
        print("在目标字符串中未找到您输入的字符串")
    else:
        for each in range(length-1):
            if desstr[each] == substr[0]:
                if desstr[each + 1] == substr[1]:
                    count = count + 1
        print('字符串在目标字符串共出现%d次' % count)
desstr = input('请输入目标字符串')
substr = input('请输入子字符串')
findstr(desstr, substr)