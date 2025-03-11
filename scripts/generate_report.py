import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Load data
assets = pd.read_csv("data/updated_assets.csv")
work_orders = pd.read_csv("data/updated_work_orders.csv")

# Count assets by condition
condition_counts = assets["Condition"].value_counts()

# Create a bar chart for asset conditions
plt.figure(figsize=(7, 5))
condition_counts.plot(kind="bar", color=["green", "orange", "red"], edgecolor='black')
plt.title("Asset Condition Distribution")
plt.xlabel("Condition")
plt.ylabel("Number of Assets")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.savefig("reports/asset_condition_chart.png")  # Save chart

# Create a PDF Report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(190, 10, "Asset Management Report", ln=True, align="C")
pdf.ln(10)

# Add asset condition statistics
pdf.set_font("Arial", "B", 12)
pdf.cell(190, 10, "Asset Condition Summary:", ln=True)
pdf.set_font("Arial", "", 12)
for condition, count in condition_counts.items():
    pdf.cell(190, 8, f"{condition}: {count} assets", ln=True)

pdf.ln(10)
pdf.cell(190, 10, "Work Order Summary:", ln=True)
pdf.set_font("Arial", "", 12)
work_order_status = work_orders["Status"].value_counts()
for status, count in work_order_status.items():
    pdf.cell(190, 8, f"{status}: {count} work orders", ln=True)

# Add the chart image
pdf.ln(10)
pdf.image("reports/asset_condition_chart.png", x=40, w=120)

# Save the PDF report
pdf.output("reports/asset_management_report.pdf")
print("Report generated successfully!")
