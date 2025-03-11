import pandas as pd
import matplotlib.pyplot as plt

# Load updated work order data
work_orders = pd.read_csv("data/updated_work_orders.csv")

# Count number of work orders per asset type
maintenance_counts = work_orders["Task"].value_counts()

# Display top maintenance tasks
print("Top Maintenance Tasks:\n", maintenance_counts)

# Plot maintenance tasks distribution
plt.figure(figsize=(8, 5))
maintenance_counts.plot(kind="bar", color='skyblue', edgecolor='black')
plt.title("Maintenance Task Distribution")
plt.xlabel("Task Type")
plt.ylabel("Number of Work Orders")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.show()
