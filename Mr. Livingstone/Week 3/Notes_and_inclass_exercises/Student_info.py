#define object level attributes
#define two methods
#print
# Define a class (object level attributes)
class Student:

    # Constructor - defines object attributes
    def __init__(self, name, age):
        self.name = name      # object level attribute
        self.age = age        # object level attribute

    # Method 1
    def introduce(self):
        print("My name is", self.name)

    # Method 2
    def show_age(self):
        print("I am", self.age, "years old")


# Create an object
student1 = Student("Timothy", 20)

# Print object attributes
print(student1.name)
print(student1.age)

# Call methods
student1.introduce()
student1.show_age()