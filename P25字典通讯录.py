#定义一个字典，内容是一个通讯簿。
contact_book = {
    'zhang_zhengjun':{
        'first_name':'zhengjun',
        'last_name':'zhang',
        'telephone':'075583469465',
        'mobile':13632922312,
        },
    'wu_mingshi':{
        'first_name':'mingshi',
        'last_name':'wu',
        'telephone':'0769888888',
        'moblie':'138888888',
        }
    }
#欢迎词
print('\n|---欢迎进入通讯录程序---|',)
action = True
while action:
    print('\n|---1:查询联系人资料 ---|',
          "\n|---2:插入新的联系人 ---|",
          '\n|---3:删除已有联系人 ---|',
          '\n|---4:退出通讯录程序 ---|',
          '\n|---5:打印所有联系人----|')
    order = input('请输入相关的指令代码：')
    #编写一段用于查询字典的代码：
    if order not in ['1','2','3','4','5']:
    # if order != '1' and order != '2' and order != '3' and order != "4" and order != '5':
        print("您的输入有误，请选择以下指令代码:")
    if order == '1':
        q = input('请输入联系人姓名：')
        if q not in contact_book:
            print("您查询的联系人不存在")
        else:
            print('\n',q)
            for name, value in contact_book[q].items():
                print('\t',name,':', value)
    #编写一段用于插入字典的代码：
    if order == '2':
        name = input("请输入联系人姓名：")
        while name in contact_book.keys():
            print(name, '已在通讯录中')
            for usrname, usrinfo in contact_book[name].items():
                print(usrname,usrinfo)
            if input('是否修改用户资料（yes/no): ') == 'yes':
                contact_book[name]['telephone'] = input('请输入座机号码：')
                contact_book[name]['mobile'] = input('请输入手机号码：')
                print(contact_book[name].items())
                break
            else:
                name = input("请重新输入联系人姓名或选择退出（退出请输入数字'4'）")
                if name == '4':
                    print("\n|---感谢使用通讯录程序 ---|")
                    exit()
                else:
                    break
        first_name = input('请输入名：')
        last_name = input("请输入姓：")
        telephone = input("请输入座机号码：")
        mobile = input('请输入手机号码：')
        contact_book[name] = {
            'first_name': first_name,
            "last_name": last_name,
            'telephone': telephone,
            'mobile': mobile,
        }
    #编写一段用于删除字典信息的代码：
    if order == '3':
        name = input('请输入要删除的联系人姓名：')
        if name in contact_book:
            del contact_book[name]
        else:
            print('您输入的联系人不存在。')
        #编写一段用于退出的代码
    if order == '4':
        print("\n|---感谢使用通讯录程序 ---|")
        exit()
    if order == '5':
        for name, info in contact_book.items():
            print(name)
            for detail, contacts in info.items():
                print(detail, contacts)

