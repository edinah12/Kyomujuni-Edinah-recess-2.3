import matplotlib.pyplot as plt

class_A = [40, 50, 60, 70, 80]
class_B = [45, 55, 65, 75, 90]

students = [1,2,3,4,5]

plt.scatter(students, class_A, label="Class A")
plt.scatter(students, class_B, label="Class B")

plt.xlabel("Student Number")
plt.ylabel("Marks")

plt.legend()

plt.show()