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