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

