import matplotlib.pyplot as plt

math = [50, 60, 70, 80, 90]
science = [45, 55, 65, 75, 85]

plt.boxplot([math, science],
            tick_labels=["Math", "Science"])

plt.ylabel("Marks")
plt.title("Math vs Science Marks")

plt.show()

