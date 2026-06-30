#   Nump arras suppor varoious mahemaivcal operaions . his can be achieved on individual elemebns or beween muliple arras

import numpy as np

w = np.array([[3, 7], [5, 10]])

p = np.array([[2, 4], [6, 8]])

# print("adding 2 to every element in the array:\n", w+2)

# print("subtracting 2 from every element in the array:\n", p-2)

# #array sum: adding two arrays together
# print("array sum: \n", w+p)

#sum of all array elements
print("sum of all elements in w:\n", w.sum)
print("sum of all elements in p:\n", np.sum(p))