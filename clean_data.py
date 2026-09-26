import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("raw_data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()

# ==========================================
# 2. CHECK DATA QUALITY
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==========================================
# 3. CLEAN DATA
# ==========================================

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(1)
df["Price"] = df["Price"].fillna(df["Price"].median())
df["City"] = df["City"].fillna("Unknown")

# Convert Date to proper date format
df["Date"] = pd.to_datetime(df["Date"])

# Create Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nCleaned Data:")
print(df)

# ==========================================
# 4. SAVE CLEANED DATA
# ==========================================

df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")

# ==========================================
# 5. BUSINESS ANALYSIS
# ==========================================

print("\n--- BUSINESS ANALYSIS ---")

print("Total Sales:", df["Total_Sales"].sum())
print("Average Sale:", df["Total_Sales"].mean())

print("\nSales by Product:")
print(df.groupby("Product")["Total_Sales"].sum())

print("\nSales by City:")
print(df.groupby("City")["Total_Sales"].sum())

# ==========================================
# 6. SALES VISUALIZATION
# ==========================================

product_sales = df.groupby("Product")["Total_Sales"].sum()

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("sales_by_product.png")

plt.show()

print("\nSales visualization saved successfully!")
# ==========================================
# SALES BY CITY VISUALIZATION
# ==========================================

city_sales = df.groupby("City")["Total_Sales"].sum()

city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("sales_by_city.png")

plt.show()

print("\nCity-wise sales visualization saved successfully!")
# ==========================================
# SALES SUMMARY DASHBOARD
# ==========================================

total_sales = df["Total_Sales"].sum()
average_sale = df["Total_Sales"].mean()

top_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

top_city = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .idxmax()
)

print("\n--- SALES SUMMARY ---")
print("Total Sales:", total_sales)
print("Average Sale:", average_sale)
print("Top Product:", top_product)
print("Top City:", top_city)
# ==========================================
# CREATE DASHBOARD IMAGE
# ==========================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Product Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()
product_sales.plot(kind="bar", ax=axes[0])

axes[0].set_title("Sales by Product")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Total Sales")

# City Sales
city_sales = df.groupby("City")["Total_Sales"].sum()
city_sales.plot(kind="bar", ax=axes[1])

axes[1].set_title("Sales by City")
axes[1].set_xlabel("City")
axes[1].set_ylabel("Total Sales")

plt.suptitle("Customer Sales Analysis Dashboard", fontsize=16)

plt.tight_layout()
plt.savefig("sales_summary.png")

plt.show()

print("\nDashboard saved successfully!")