data = '1000, zhang, male'
My_dict = {}
(My_dict['id'], My_dict['name'], My_dict['sex']) = data.split(',')
print(My_dict)

print('ID: ' + My_dict['id'])
print('Name: ' + My_dict['name'])
print('Sex: ' + My_dict['sex'])