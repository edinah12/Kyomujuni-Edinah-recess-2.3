#every numpy array has a data type
import numpy as np

z = np.array([1, 2, 3, 4, 5])
print(z.dtype)

#USING A TUPLE AS A DATA TYPE
t = np.array([(1, 2), (3, 4)], dtype=[('x', int), ('y', int)])
print(t.dtype)

students = np.array(
    [
        ("John", 20, 85.5),
        ("Mary", 22, 90.0)
    ],
    dtype=[
        ("name", str),
        ("age", int),
        ("score", float)
    ]
)

print(students.dtype)

print(students.dtype['age'])
print(students.dtype['score'])
print(students.dtype['age'])
print(students.dtype['name'])