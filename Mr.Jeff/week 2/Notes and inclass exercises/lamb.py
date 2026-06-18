#lambda functions
#define lambda funcions
square = lambda x: x ** 2
print(square(5))

def add(a, b):
    return a + b

print(add(5, 3))

add = lambda a, b: a + b

print(add(5, 3))

#lambda function syntax
#lambda arguments: expression

def factorial(n):
    #base case
    if n<=1:
        return 1
    
    else:
        return n* factorial(n-1)
    
    print(factorial(5))
    
    #method 2
    def factorial(n):
     if n<=1:
         return 1
    return n* factorial(n-1)
    print(factorial(5))
    
    #exe3 using fibonacci sequence get the first 10 fibonacci number in the range of 10
    #use recursive functions with the base and recursive cases
    
