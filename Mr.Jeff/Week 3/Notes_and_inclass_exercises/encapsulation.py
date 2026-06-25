# #lab 1
# #student
# class Student:
#     def __init__(self, name, age, student_number):
#         self.name = name
#         self.age = age
#         self.student_number = student_number
        
# student_1 = Student("John", 20, "12345")
        
# print(student_1.name)  # Output: John

# #access modifiers
# #phon suppors 3 access modifiers: public, protected, private
# #public: can be accessed from anywhere
# #protected: can be accessed within the class and its subclasses
# #private: can only be accessed within the class

# #example of access modifiers

# #employee example, name, salary, age
# #public: name

# class Employee:
#     def __init__(self):
#         self.name = "John"  # public attribute
        
# employee_1 = Employee()
# print(employee_1.name)  # Output: John

# #protected: salary

# class Employee:
#     def __init__(self):
       
#         self._salary = 50000  # protected attribute
        
# employee_1 = Employee()

# print(employee_1._salary)  # Output: 50000

# #private: age

# class Employee:
#     def __init__(self):
       
#         self.__age = 30  # private attribute
        
# employee_1 = Employee()


# print(employee_1._Employee__age)  # Output: 30 

# #exercise : create a class called car with brand, model, price; make brand public, model protected and price private, display all values appropriately
# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand  # public attribute
#         self._model = model  # protected attribute
#         self.__price = price  # private attribute
        
#     def display_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self._model}")
#         print(f"Price: {self.__price}")
        
        
# car_1 = Car("Toyota", "Camry", 25000)
# car_1.display_info()

# #data hiding
# #real world bank accoun, (balance, deposi)

# class BankAccount:
#     def __init__(self):
#         self.__balance = 1000000  # private attribute
        
#     def deposit(self, amount):
       
#             self.__balance += amount
           
#     def show_balance(self):
#         return self.__balance
        
# acc = BankAccount()
# acc.deposit(50000)
# acc.deposit(100000)
# print(acc.show_balance())

#exercise2: create a class MobileMoney , with attributes __balance, methods deposit, withdraw and check balance
#test your application to show balance after withdraw

# class MobileMoney:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def check_balance(self):
#         return self.__balance

# # Test the application
# mm = MobileMoney()
# mm.deposit(10000)
# mm.withdraw(5000)
# print(mm.check_balance())

#ABSRACION
#HIDES IMPLEMENTATION DETAILS FROM THE USER AND SHOWS ONLy ESSENIAL FEATURES OF AN OBJECT tO tHE USER

#lab activity 3
from abc import ABC, abstractmethod
from curses.ascii import SUB

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
       print("Vehicle started.")

    @abstractmethod
    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start(self):
        print("car started.")

    def stop(self):
        print("car stopped.")


car = Car("Toyota", "Camry")

car.start()
car.stop()

#exercise 3: using multiple abstract methods
#create an abstract for shapes, should have method area(), perimeter()
#create a rectangle and circle classes that implement these methods

from abc import ABC, abstractmethod
import math


# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Rectangle class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Testing

rectangle = Rectangle(10, 5)

circle = Circle(7)


print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

#inheritance
'''
PARENT CLASS: BASE CLASS, SUPER CLASS
CHILD CLASS: DERIVED CLASS, SUB CLASS
        
        '''
#PARENT CLASS
class person:
    def __init__(self, name):
                self.name = name

    def display_info(self):
        
        print(f"Hello, my name is {self.name}.")
        
        #
        class Student(person):
           def study(self):
                print(f"{self.name} is studying.")

           
        
        
