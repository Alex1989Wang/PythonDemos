def first_python_function():
    print("I'm the first python function to be created.")

first_python_function()

# key word arguments
def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)
print_kwargs(wine = "melot", 
        entree = "mutton", 
        dessert = "macaroon")


# doc string 
def doc_help():
    '''The doc string explain what the function does
    and you should write one for every function you write.'''
    print("Test doc string")
print(help(doc_help))

# everything is an object in python
# this includes numbers, strings, tuples, lists, 
# dictionaries and functions

# functions are first-class citizens in Python.
# generator
def my_range(frist=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
print(my_range)
print(my_range(1,5))

# decorator
def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@square_it
@document_it
def add_ints(a, b):
    return a + b

@document_it
@square_it
def add_ints_two(a, b):
    return a + b

print(add_ints(3, 5))
print(add_ints_two(3, 5))
