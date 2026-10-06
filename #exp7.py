#exp7
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

print("Dataset:")
print(df.head())

# Histogram
df["Age"].plot(kind="hist", bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.boxplot(df["Salary"].dropna())
plt.title("Salary Boxplot")
plt.ylabel("Salary")
plt.show()

# Scatter plot
plt.scatter(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# Correlation heatmap
numeric_df = df.select_dtypes(include="number")
correlation = numeric_df.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\nCorrelation Matrix:")
print(correlation)