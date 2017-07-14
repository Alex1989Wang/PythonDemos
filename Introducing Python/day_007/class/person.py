class Person():
    def __init__(self, name):
        """The initialization of person"""
        self.name = name

    def say_name(self):
        """print the name of the person"""
        print("Hello, my name is", self.name)

class Employee(Person):
    def __init__(self, name, company):
        """The initilization of an employee"""
        super().__init__(name)
        self.company = company

    def print_info(self):
        self.say_name()
        print("\nI work in", self.company)

    def say_name(self):
        """Override parent class sya_name"""
        print("Hello from class Employee. Your name is:", self.name)
