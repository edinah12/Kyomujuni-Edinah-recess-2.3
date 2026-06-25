#when a class inherits from more than one base class, it is called multiple inheritance. In Python, a class can inherit from multiple base classes by specifying them in parentheses after the class name.
#diamond problem-occurs when two classes inherit from a common base class and another class inherits from both
#if a method is over ridden in the immediate classes, ambiguity arises about which class method the derived class should use
#method resolution order (MRO)- determines the order in which base classes are searched when looking for an attribute in multiple inheritance.
#it follows linearization rule

class Class1:
    def w(self):
        print("Method from class 1")
        
class Class2(Class1):
    def w(self):
        print("Method from class 2")
                
class Class3(Class1):
    def w(self):
        print("Method from class 3")
                        
class Class4(Class2,Class3):
    pass
                        
obj=Class4()
obj.w()

print(Class4.__mro__)