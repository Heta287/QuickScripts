# Time Series Analysis and Forecasting Examples

'''
Notebook contains:
Simulated Time Series Data: Generating and visualizing time series data.
Decomposition: Demonstrating trend, seasonality, and residual decomposition using seasonal_decompose.
ARIMA Model: Fitting and forecasting using ARIMA.
Prophet Model: Time series forecasting with Facebook Prophet.
LSTM Forecasting: Implementing LSTM-based time series forecasting using TensorFlow.
Autocorrelation & Partial Autocorrelation: Visualizing ACF and PACF plots.
Moving Averages: Applying Simple and Exponential Moving Averages.
Stationarity Check: Performing stationarity tests with ADF.
'''

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from fbprophet import Prophet
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 1. Simulated Time Series Data
np.random.seed(42)
time = np.arange(100)
data = np.sin(0.1 * time) + 0.5 * np.random.randn(100)

# Create DataFrame
df = pd.DataFrame({'Time': time, 'Value': data})
df['Date'] = pd.date_range(start='2022-01-01', periods=len(df), freq='D')

# 2. Plot Time Series Data
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Value'], color='blue')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# 3. Decomposing Time Series
# Add trend and seasonality for demo purposes
df['Trend'] = df['Value'].rolling(window=10).mean()
df['Seasonal'] = df['Value'] - df['Trend']

# Decompose time series
result = seasonal_decompose(df['Value'], model='additive', period=12)

# Plot the decomposition
result.plot()
plt.show()

# 4. ARIMA Model
# Fit ARIMA model (p, d, q)
model_arima = ARIMA(df['Value'], order=(2, 1, 2))
model_fit = model_arima.fit()

# Forecast
forecast_arima = model_fit.forecast(steps=10)
print("ARIMA Forecast:", forecast_arima)

# Plot forecast
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Value'], label='Original')
plt.plot(pd.date_range(start=df['Date'].iloc[-1] + pd.Timedelta(days=1), periods=10, freq='D'),
         forecast_arima, color='red', label='ARIMA Forecast')
plt.title('ARIMA Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# 5. Prophet Model
df_prophet = df[['Date', 'Value']].rename(columns={'Date': 'ds', 'Value': 'y'})
model_prophet = Prophet()
model_prophet.fit(df_prophet)

# Make future predictions
future_dates = model_prophet.make_future_dataframe(periods=10)
forecast_prophet = model_prophet.predict(future_dates)

# Plot Prophet Forecast
model_prophet.plot(forecast_prophet)
plt.title('Prophet Forecast')
plt.show()

# 6. LSTM for Time Series Forecasting
# Data Preprocessing for LSTM
def create_sequences(data, seq_length):
    sequences = []
    labels = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i + seq_length])
        labels.append(data[i + seq_length])
    return np.array(sequences), np.array(labels)

# Normalize Data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[['Value']])

# Create sequences
seq_length = 10
X, y = create_sequences(scaled_data, seq_length)

# Reshape for LSTM [samples, time steps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build LSTM Model
model_lstm = Sequential([
    LSTM(50, activation='relu', input_shape=(seq_length, 1)),
    Dense(1)
])

model_lstm.compile(optimizer='adam', loss='mse')
model_lstm.fit(X, y, epochs=100, verbose=0)

# Forecasting using LSTM
X_input = scaled_data[-seq_length:].reshape((1, seq_length, 1))
lstm_forecast = []
for _ in range(10):
    next_value = model_lstm.predict(X_input)
    lstm_forecast.append(next_value[0][0])
    X_input = np.append(X_input[:, 1:, :], [[next_value]], axis=1)

# Inverse scale forecast
lstm_forecast = scaler.inverse_transform(np.array(lstm_forecast).reshape(-1, 1))

# Plot LSTM Forecast
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Value'], label='Original')
plt.plot(pd.date_range(start=df['Date'].iloc[-1] + pd.Timedelta(days=1), periods=10, freq='D'),
         lstm_forecast, color='green', label='LSTM Forecast')
plt.title('LSTM Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# 7. Autocorrelation and Partial Autocorrelation Plots
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plot_acf(df['Value'], lags=20, ax=plt.gca())
plt.title('Autocorrelation')

plt.subplot(1, 2, 2)
plot_pacf(df['Value'], lags=20, ax=plt.gca())
plt.title('Partial Autocorrelation')

plt.tight_layout()
plt.show()

# 8. Moving Averages (SMA and EMA)
# Simple Moving Average
df['SMA_10'] = df['Value'].rolling(window=10).mean()

# Exponential Moving Average
df['EMA_10'] = df['Value'].ewm(span=10, adjust=False).mean()

# Plot SMA and EMA
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Value'], label='Original Data')
plt.plot(df['Date'], df['SMA_10'], label='SMA 10', color='red')
plt.plot(df['Date'], df['EMA_10'], label='EMA 10', color='green')
plt.title('Moving Averages')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# 9. Stationarity Check (Augmented Dickey-Fuller Test)
from statsmodels.tsa.stattools import adfuller

result_adf = adfuller(df['Value'].dropna())
print(f'ADF Statistic: {result_adf[0]}')
print(f'p-value: {result_adf[1]}')

if result_adf[1] < 0.05:
    print("Time series is stationary")
else:
    print("Time series is non-stationary")
