list1 = ['1.just do it', '2.一切皆有可能', '3.让编程改变世界', '4.impossible is nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼c工作室', '1.耐克']
list3 = []
for slogan in list1:
    for name in list2:
        if slogan[0] == name[0]:
            list3.append(name + ":" + slogan[2:])
for each in list3:
    print(each)



#list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
#for each in list3:
    #print(each)



# list3 = []
# for slogan in list1:
#     for name in list2:
#         if slogan[0] == name[0]:
#             list3.append(name + ':' + slogan[2:])
# print(list3)