#Bar charts display categorical data using rectangular barswhose lengths are proportional to the valuesthey represent.
#these are plotted vertically or horizontally. Bar charts are used to compare different categories of data. Each bar represents a category, and the height or length of the bar corresponds to the value of that category.

# simple Bar chart
import matplotlib.pyplot as plt

w  = ["Makanga", "Martha", "Oren", "Josephine", "Moses",]
z = [10, 20, 30, 40,15]

plt.bar(w, z)
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()