import pandas as pd

# Load the data
df = pd.read_csv("raw_data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display basic information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing customer names
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")

# Fill missing quantity
df["Quantity"] = df["Quantity"].fillna(1)

# Fill missing price with median price
df["Price"] = df["Price"].fillna(df["Price"].median())

# Fill missing city
df["City"] = df["City"].fillna("Unknown")

# Convert Date to proper date format
df["Date"] = pd.to_datetime(df["Date"])

# Create Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nCleaned Data:")
print(df)
# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
# Basic Analysis

print("\n--- BUSINESS ANALYSIS ---")

print("Total Sales:", df["Total_Sales"].sum())

print("Average Sale:", df["Total_Sales"].mean())

print("\nSales by Product:")
print(df.groupby("Product")["Total_Sales"].sum())

print("\nSales by City:")
print(df.groupby("City")["Total_Sales"].sum())
import matplotlib.pyplot as plt

product_sales = df.groupby("Product")["Total_Sales"].sum()

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("sales_by_product.png")

plt.show()
# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
# Basic Business Analysis

print("\n--- BUSINESS ANALYSIS ---")

print("Total Sales:", df["Total_Sales"].sum())

print("Average Sale:", df["Total_Sales"].mean())

print("\nSales by Product:")
print(df.groupby("Product")["Total_Sales"].sum())

print("\nSales by City:")
print(df.groupby("City")["Total_Sales"].sum())
import matplotlib.pyplot as plt

# Sales by Product
product_sales = df.groupby("Product")["Total_Sales"].sum()

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("sales_by_product.png")

plt.show()