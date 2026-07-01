import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Customer data
customers = pd.DataFrame({
    "Age": [25, 35, 45, 30, 50],
    "Income": [30000, 50000, 70000, 40000, 90000],
    "Monthly_Spend": [500, 900, 1500, 700, 2000],
    "Visits": [5, 8, 12, 6, 15]
})


# Calculate correlation
correlation = customers.corr()


# Create heatmap
sns.heatmap(
    correlation,
    annot=True
)

plt.title("Customer Spending Correlation Heatmap")

plt.show()