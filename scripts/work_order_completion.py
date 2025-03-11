import pandas as pd
import matplotlib.pyplot as plt

# Load work orders
work_orders = pd.read_csv("data/updated_work_orders.csv")

# Count completed vs pending work orders
status_counts = work_orders["Status"].value_counts()

# Display summary
print("Work Order Completion Status:\n", status_counts)

# Pie chart of work order statuses
plt.figure(figsize=(6, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=["green", "red", "orange"], startangle=140)
plt.title("Work Order Completion Status")
plt.show()
