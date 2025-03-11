import pandas as pd

# Load datasets
assets = pd.read_csv("data/assets.csv")
work_orders = pd.read_csv("data/work_orders.csv")

# Define condition updates based on completed tasks
condition_updates = {
    "Resurface Road": "Excellent",
    "Leak Repair": "Good",
    "Bulb Replacement": "Excellent",
    "Structural Check": "Good",
    "Sewer Cleaning": "Good"
}

# Iterate through completed work orders and update asset conditions
for index, row in work_orders.iterrows():
    if row["Status"] == "Completed":
        asset_id = row["Asset_ID"]
        task = row["Task"]
        if task in condition_updates:
            assets.loc[assets["Asset_ID"] == asset_id, "Condition"] = condition_updates[task]

# Save updated asset data
assets.to_csv("data/updated_assets.csv", index=False)
print("Asset conditions updated and saved!")
