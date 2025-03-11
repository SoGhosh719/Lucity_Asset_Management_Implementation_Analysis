import pandas as pd

# Load asset and work order data
assets = pd.read_csv("data/assets.csv")
work_orders = pd.read_csv("data/work_orders.csv")

# Display first few rows of each dataset
print("Assets Data:")
print(assets.head())

print("\nWork Orders Data:")
print(work_orders.head())

# Get summary statistics
print("\nAsset Condition Counts:")
print(assets["Condition"].value_counts())

print("\nWork Order Status Counts:")
print(work_orders["Status"].value_counts())
