import pandas as pd

# Load datasets
assets = pd.read_csv("data/updated_assets.csv")
work_orders = pd.read_csv("data/work_orders.csv")

# Define maintenance tasks based on condition
maintenance_tasks = {
    "Poor": "Urgent Repair",
    "Fair": "Routine Maintenance"
}

# Identify assets needing maintenance
new_work_orders = []
for index, row in assets.iterrows():
    if row["Condition"] in maintenance_tasks:
        new_work_orders.append({
            "Order_ID": work_orders["Order_ID"].max() + len(new_work_orders) + 1,
            "Asset_ID": row["Asset_ID"],
            "Task": maintenance_tasks[row["Condition"]],
            "Status": "Pending",
            "Assigned_To": "Auto-Scheduler",
            "Completion_Date": None
        })

# Convert new work orders to DataFrame
new_work_orders_df = pd.DataFrame(new_work_orders)

# Append new work orders to existing ones
updated_work_orders = pd.concat([work_orders, new_work_orders_df], ignore_index=True)

# Save updated work orders
updated_work_orders.to_csv("data/updated_work_orders.csv", index=False)
print("New work orders assigned and saved!")
