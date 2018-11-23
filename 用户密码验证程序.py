count = 3
password = 'laozhang'
while count:
    psd = input('please type your password:')
    if psd == password:
        print('correct, continue!')
        break
    elif "*" in psd:
        print("can't with * in password, you have", count, 'chance still')
        continue
    else:
        print('wrong password,you have', count - 1, 'chance still')

    count -= 1