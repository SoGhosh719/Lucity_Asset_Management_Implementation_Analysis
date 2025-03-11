import pandas as pd
import matplotlib.pyplot as plt

# Load asset data
assets = pd.read_csv("data/updated_assets.csv")

# Count assets by condition
condition_counts = assets["Condition"].value_counts()

# Display condition distribution
print("Asset Condition Distribution:\n", condition_counts)

# Bar chart for asset conditions
plt.figure(figsize=(7, 5))
condition_counts.plot(kind="bar", color=["green", "orange", "red"], edgecolor='black')
plt.title("Asset Condition Distribution")
plt.xlabel("Condition")
plt.ylabel("Number of Assets")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.show()
