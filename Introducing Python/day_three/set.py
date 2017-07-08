# set convertion 
letters = 'letters'
letter_set = set(letters)
print(letter_set)

dictionary = {'jiang' : 'wang', 
        'chun' : 'wen',}
set_from_dict = set(dictionary)
print(set_from_dict)

list_names = ['jiang', 'wang', 
        'chun', 'wen',]
set_from_list = set(list_names)
print(set_from_list)

# empty set 
empty_set = set()
print(empty_set)

# combinations
drinks = {'martini' : {'vodka', 'vermouth'}, 
        'black russian' : {'cream', 'kahlua'},
        'white russian' : {'cream', 'kahlua', 'vodka'}, 
        'screwdriver' : {'orange juice', 'vodka'}}
for name, contents in drinks.items() :
    print(name, contents)
    if 'vodka' in contents : 
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

black_russ = drinks['black russian']
white_russ = drinks['white russian']
print(black_russ.issubset(white_russ))
print(black_russ < white_russ)
print(black_russ.difference(white_russ))
