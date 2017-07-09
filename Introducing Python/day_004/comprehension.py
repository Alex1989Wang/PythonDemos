
# list comprehension
# a comprehension is a compact way of creating a python data structure from one
# or more iterators.

list_comprehension = [number for number in range(0,9) if number % 2 == 0]
print(list_comprehension)

# dictionary comprehension
word = "letter"
count_dic = {letter : word.count(letter) for letter in word}
print(count_dic)

# 
