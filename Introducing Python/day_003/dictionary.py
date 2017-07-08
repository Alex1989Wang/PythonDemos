
names_dict = {'Jiang' : 'Wang', 
        'Chun' : 'Wen',}
other_names = {'Michelle' : 'Wen', 
        'Alex' : 'Wang',}
names_dict.update(other_names)
print(names_dict)
print(names_dict['Jiang'])
del names_dict['Jiang']
# print(names_dict['Jiang']) #cause an exception
name_existed = 'Jiang' in names_dict
print(name_existed)

# delete all items
other_names.clear()
print(other_names)

# special get function 
print(other_names.get('Jiang'))
print(other_names.get('Jiang', 'Not existed'))
print(names_dict.keys())

# python 3 vs. python 2 
print(list(names_dict.values()))
