# Exp5
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numerical values with median
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Outlier detection using IQR
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    df = df[
        (df[col] >= Q1 - 1.5 * IQR) &
        (df[col] <= Q3 + 1.5 * IQR)
    ]

# Normalization
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Grouping and aggregation
print("\nGrouped Data:")
print(df.groupby("Category")[num_cols].mean())

# Machine learning
X = df.drop("Target", axis=1)
y = df["Target"]

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nModel Accuracy:")
print(accuracy_score(y_test, predictions))

print("\nPreprocessed Data:")
print(df)