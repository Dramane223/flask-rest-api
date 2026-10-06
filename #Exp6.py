#Exp6
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

print("Dataset:")
print(df.head())

# Basic information
print("\nDataset Information:")
print(df.info())

# Pivot table
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Category",
    aggfunc="sum"
)

print("\nPivot Table:")
print(pivot)

# Visualization
pivot.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Query-based search
query = input("\nEnter category to search: ")

result = df[df["Category"].astype(str).str.contains(
    query, case=False, na=False
)]

print("\nSearch Results:")
print(result)