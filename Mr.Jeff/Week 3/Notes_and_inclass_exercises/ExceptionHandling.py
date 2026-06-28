# #EXCEPTION HANDLING
# #EXAMPLES
# '''
# division by zero
# file not found
# index out of range
# invalid input

# '''
# #code, try,catch, finally
#  #try block
 
# try:
#         num1 = int(input("Enter a number: "))
#         num2 = int(input("Enter another number: "))
#         result = num1 / num2
#         print(f"The result of {num1} divided by {num2} is: {result}")

# except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
# except ValueError:
#         print("Error: Please enter valid integers.")
# except Exception as e:
#         print(f"An unexpected error occurred: {e}")
# finally:
#         print("Execution completed.")
        
        #finally block is always executed regardless of whether an exception occurred or not. It is often used for cleanup actions, such as closing files or releasing resources.
        
        #lab reading a file
        
# try:
#     file = open('student.json')
#     print(file.read())
# except FileNotFoundError:
#     print("Error: The file 'student.json' was not found.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("File operation completed.")
    
#     #real world example
#     #ATM withdrawal system
    
#     class InsufficientFundsError(Exception):
#         pass
#     balance = 2000000
#     wihdraw = int(input("Enter the amount to withdraw: "))
#     try:
#         if wihdraw > balance:
#             raise InsufficientFundsError("Error: Insufficient funds for this withdrawal.")
#         else:
#             balance -= wihdraw
#             print(f"Withdrawal successful. New balance: {balance}")
#     except InsufficientFundsError as error:
#         print(error)
#     except Exception as error:
#         print(f"An unexpected error occurred: {error}")
        
        #exercise 3: write a custom exception for a ugandan to drive a car, must be 18 years or older
class InvalidAgeError(Exception):
        pass

age = int(input("Enter your age: "))
try:
        if age < 18:
            raise InvalidAgeError("Error: You must be at least 18 years old to drive a car in Uganda.")
        else:
            print("You are eligible to drive a car in Uganda.")
except InvalidAgeError as error:
        print(error)
except Exception as error:
        print(f"An unexpected error occurred: {error}")
        
        #debugging
        #what is debugging?
        #common errors
        #syntax error
        #runtime error
        #logical error
        