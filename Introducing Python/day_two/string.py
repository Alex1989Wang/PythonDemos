
#string slicing 
name = 'Penny'
new_name = 'H' + name[1:]
print(new_name)

new_new_name = name[:3] + 'hehe' + name[-1:]
print(new_new_name)

name_backward = name[-1::-1]
print(name_backward)

print(len(name_backward))
print(len(''))

# string split example
string_to_split = 'like hello, world, i think i like you'
split_strings = string_to_split.split(',')
print(split_strings)

# string join 
join_string = ','.join(split_strings)
print(join_string)

# string manipulation 
print(string_to_split.rfind('like'))
print(string_to_split.count('like'))
print(string_to_split.isalnum())
print(string_to_split.strip('like'))
print(string_to_split.title())
print(string_to_split.center(30)) #will be effective in interactive mode
print(string_to_split.rjust(30)) #will be effective in interactive mode

# watch out for substution 
print(string_to_split.replace('o', 'oh my God'))
