#using the math module

import pandas

#create a simple data frame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}

print(data)
df = pandas.DataFrame(data)
print(df)

#how to show built-in modules
#print(dir(pandas))

#how to make use of the zip function
names = ['Alice', 'Bob', 'Charlie', 'David']
#ages = [25, 30, 35, 40]
#zipped = list(zip(names, ages))
#print(zipped)

#use the zip function to create a marksheet
#make it in the format of "name has a score of marks"

marks = [85, 90, 78, 92]
for name, mark in zip(names, marks):
    print(f"{name} has a score of {mark}")