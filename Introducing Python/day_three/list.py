
# pop function
name_list = ['Alex', 'Wang', 'Jiang', 'Chun']
print(name_list.index('Wang'))
name_popped = name_list.pop(0)
print(name_popped, name_list)
print(name_list.index('Wang'))
print('Chun' in name_list)

# list manipulation 
name_list_new_reference = name_list
new_list = name_list.copy()
new_new_list = list(name_list)
new_two_list = name_list[:]
name_list[0] = 'Changed'

print(name_list, name_list_new_reference, new_list, new_new_list)

# 
