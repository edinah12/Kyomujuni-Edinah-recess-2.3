#lab activity 2:mathematical function
#square number
def square_number():
    num=5
    square=num*num
    print(square)

#exercise 2
    #recangle area with input from user
def rectangle_area():
    length=int(input("Enter the length of the rectangle: "))
    breadth=int(input("Enter the breadth of the rectangle: "))
    area=length*breadth
    print(area)

#what is a parameter in a function
#parameter is a variable that is used to pass information
#variables passed inside the function definition

#what is an argument in a function
#argument is the actual value that is passed to the function when it is called
#actual values passed to a function

#a function with a single parameter
def greet(name):
    print("Hello, " + name + "! Welcome to the world of programming.")

greet("Alice")  # Calling the function with an argument

#a function with multiple parameters

#exercise 2
#creae a funcion that uses a function to display student information
#diaplay Name, age, course, student number
#take input from the user for each of these parameters and display the information in a formatted way

def get_student_info():
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    course = input("Enter the student's course: ")
    student_number = input("Enter the student's number: ")
    return name, age, course, student_number

def display_student_info(name, age, course, student_number):
    print("\n--- Student Information ---")
    print("Name: " + name)
    print("Age: " + str(age))
    print("Course: " + course)
    print("Student Number: " + student_number)

# Example usage
student_name, student_age, student_course, student_num = get_student_info()
display_student_info(student_name, student_age, student_course, student_num)

#exe 3 create a function that calculates the area of a circle
import math
def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

# Example usage
circle_radius = float(input("Enter the radius of the circle: "))
circle_area = calculate_circle_area(circle_radius)
print("The area of the circle is:", circle_area)

#exe4 write a program demonstrating the difference between local and global variables
global_variable = "I am a global variable"
def demonstrate_variables():
    local_variable = "I am a local variable"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

demonstrate_variables()