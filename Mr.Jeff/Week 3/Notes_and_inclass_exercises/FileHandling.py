# #example read a student.txt file

# #recommended method
# # #with automatically closes the file after the block of code is executed

# # with open('student.txt', 'r') as file:
    
# #     #read one line at a time
# #     for line in file:
# #         print(line.strip())  #strip removes the newline character at the end of each line
        
#         #lab exercise 1: write a file with the content 'i love phone programming' first line,
#         #'i am becoming a data scientist' , second line, save our file as report.txt
        
# import csv
# import json


# with open('report.txt', 'w') as report_file:
#         report_file.write('I love phone programming\n')
#         report_file.write('I am becoming a data scientist\n')

# print("report.txt file created successfully.")

# with open('report.txt', 'a') as report_file:
#     report_file.write('I am also interested in machine learning.\n')
#     print("Additional content added to report.txt successfully.")
    
#     #real world example
#     #attendance system
#     #live demo
    
#     name = input("Enter student : ")
#     with open('attendance.txt', 'a') as attendance_file:
#         attendance_file.write(name + '\n')
#         print(f"{name} has been marked present.")
        
#         #open csv file
#         with open('data.csv', 'r') as csv_file:
#             reader = csv.reader(csv_file)
#             for row in reader:
#                 print(row)
                
import json

student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science"
}

with open('student.json', 'w') as json_file:
    json.dump(student, json_file, indent=4)
    
print('JSON file successfully created')

#
                    