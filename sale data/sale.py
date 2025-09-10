import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "sale.csv"   # Change if needed
df = pd.read_csv(file_path)

# Create figure for multiple charts
plt.figure(figsize=(18, 12))

# 1. Line Chart - Total Sales per Year
plt.subplot(3, 2, 1)
yearly_sales = df.groupby("Year")["Sales"].sum()
plt.plot(yearly_sales.index, yearly_sales.values, marker="o", color="blue")
plt.title("Total Sales per Year")
plt.xlabel("Year")
plt.ylabel("Sales ($)")

# 2. Bar Chart - Total Sales per Month
plt.subplot(3, 2, 2)
monthly_sales = df.groupby("Month")["Sales"].sum()
plt.bar(monthly_sales.index, monthly_sales.values, color="orange")
plt.title("Total Sales per Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

# 3. Bar Chart - Sales by Region
plt.subplot(3, 2, 3)
region_sales = df.groupby("Region")["Sales"].sum()
plt.bar(region_sales.index, region_sales.values, color=["red","green","blue","purple"])
plt.title("Total Sales by Region")
plt.ylabel("Sales ($)")

# 4. Pie Chart - Profit Contribution by Product
plt.subplot(3, 2, 4)
product_profit = df.groupby("Product")["Profit"].sum()
plt.pie(product_profit.values, labels=product_profit.index, autopct="%1.1f%%", startangle=90)
plt.title("Profit Contribution by Product")

# 5. Line Chart - Yearly Profit Trend
plt.subplot(3, 2, 5)
yearly_profit = df.groupby("Year")["Profit"].sum()
plt.plot(yearly_profit.index, yearly_profit.values, marker="s", linestyle="--", color="green")
plt.title("Total Profit per Year")
plt.xlabel("Year")
plt.ylabel("Profit ($)")

# 6. Scatter Plot - Sales vs Profit
plt.subplot(3, 2, 6)
plt.scatter(df["Sales"], df["Profit"], c=df["Year"], cmap="viridis", s=40, alpha=0.6)
plt.colorbar(label="Year")
plt.title("Sales vs Profit")
plt.xlabel("Sales ($)")
plt.ylabel("Profit ($)")

# Adjust layout
plt.tight_layout()

# Save output
plt.savefig("all_sales_charts.png")
plt.show()
