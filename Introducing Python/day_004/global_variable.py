
animal = "fruitbat"
print(id(animal))

def change_local():
    global animal
    animal = "eagle"
    print("Inside " + change_local.__name__ + ": " + animal)
    print("Locals:", locals())
    print("Globals:", globals())

change_local()
print("Global print animal:", animal)
