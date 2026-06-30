#they are inbuilt

#np.array() function converts a python lists, tuples or sequence into array

import numpy as np
# array1 = np.array([1, 2, 3, 4, 5])
# print(array1)

# #np.zeros() - creates an array filled with zeros
# array2 = np.zeros((4, 5))
# print(array2)

# #random function - generates random numbers in an array
# array3 = np.random.rand (4, 5)
# # or (array3 = np.random.random((4, 5)))

# print(array3)

# #mathematical and statistical functions
# array4 = np.array([[1, 2, 3], [4, 5, 6]])
# total = np.sum(array4)
# print(total)

#np.arange() - creates an array with a range of numbers
array3 = np.arange(1, 10)
print(array3)

#np.linspace() creates evenly spaced numbers over a specified range
#syntax np.linspace(start, stop, number_of_values)
# start = 0 → begin at 0
# stop = 10 → end at 10
# 5 → create 5 numbers in between (including start and stop)
array4 = np.linspace(0,10,5)
print(array4)