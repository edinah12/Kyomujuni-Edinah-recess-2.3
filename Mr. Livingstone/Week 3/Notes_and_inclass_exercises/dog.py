#define a class with a class keyword
#class keword class name:
class Dog:
    #define an attribute for my class
    name = "Buddy"
    name1 = "Max"
    #an object is a specific instance of a class
    # it can have its own attributes and methods and parameters
    #multiple objects can be created using the same class
# multiple objects can be created using the same class

# create an object from class
dog1 = Dog()

# accessing the attributes of the object
print(dog1.name)  # output: Buddy
print(dog1.name1)  # output: Max

#how to apply the __init__() method to create a constructor for the class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        

