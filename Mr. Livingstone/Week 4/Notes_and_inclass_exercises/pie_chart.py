import matplotlib.pyplot as plt

fruits = ["Apple", "Banana", "Orange", "Mango"]
students = [20, 30, 10, 40]

plt.pie(
    students,
    labels=fruits,
    autopct="%1.1f%%"
)

plt.title("Favorite Fruits")

plt.show()