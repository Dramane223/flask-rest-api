#exp8
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import autocorrelation_plot

# Load dataset
df = pd.read_csv("time_series.csv")

# Convert date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set date as index
df.set_index("Date", inplace=True)

# Select time-series column
series = df["Sales"]

# Original time series
plt.figure(figsize=(10, 5))
plt.plot(series)
plt.title("Original Time Series")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# Rolling mean
rolling_mean = series.rolling(window=7).mean()

plt.figure(figsize=(10, 5))
plt.plot(series, label="Original")
plt.plot(rolling_mean, label="7-Day Rolling Mean")
plt.title("Rolling Window Analysis")
plt.legend()
plt.show()

# Trend decomposition
decomposition = seasonal_decompose(
    series,
    model="additive",
    period=7
)

decomposition.plot()
plt.show()

# Autocorrelation
plt.figure(figsize=(10, 5))
autocorrelation_plot(series)
plt.title("Autocorrelation")
plt.show()