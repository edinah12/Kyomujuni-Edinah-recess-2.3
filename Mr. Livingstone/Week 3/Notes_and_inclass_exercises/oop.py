#creating a class
class Dog:
    #creating a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #creating a method
    def bark(self):
        return "Woof!"

    #creating another method
    def get_info(self):
        return f"{self.name} is {self.age} years old."