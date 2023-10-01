import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import ParameterGrid
from keras.optimizers import Adam
from math import sqrt
import datetime as dt
import requests
import pytz


message2 = {
    'content': 'Hello, World!'
}

# Discord API authorization header
header = {
    'Authorization': 'OTMyNzI3Mjg3MzcwMTEzMDM2.GWRIaI.xHwbzEURzI-1TyRCufUdGOoeHoV8IY4C-enlk8'
}

# send the post request to discord API
r = requests.post(f"https://discord.com/api/v9/channels/8/messages", data=message2, headers=header)



# Check the response status code and content
print("Response Status Code:", r.status_code)
print("Response Content:", r.text)

exit()


# Function to fetch stock data
def fetch_stock_data(tickers):
    stock_data = {}
    for ticker in tickers:
        stock_data[ticker] = yf.download(ticker, period='365', interval='1d')
    return stock_data

# Function to calculate percentage changes
def calculate_percentage_changes(stock_data):
    pct_changes = {}
    for ticker, df in stock_data.items():
        pct_changes[ticker] = df['Close'].pct_change()
    return pct_changes

# Function to train the model
def train_model(params, X_train, y_train):
    lstm_units = params['lstm_units']
    batch_size = params['batch_size']
    epochs = params['epochs']
    dropout_rate = params['dropout_rate']
    learning_rate = params['learning_rate']

    model = Sequential()
    model.add(LSTM(units=lstm_units, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(dropout_rate))
    model.add(LSTM(units=lstm_units))
    model.add(Dropout(dropout_rate))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    return model

# Function to evaluate the model
def evaluate_model(model, X_val, y_val):
    y_pred = model.predict(X_val)
    mse = mean_squared_error(y_val, y_pred)
    mae = mean_absolute_error(y_val, y_pred)
    rmse = sqrt(mse)
    return mse, mae, rmse

# Fetch stock data
stock_tickers = ['AAPL', 'MSFT', 'AMZN', 'META', 'TSLA', 'UNH', 'JNJ', 'JPM', 'HD', 'BAC', 'PG', 'MA', 'DIS', 'VZ',
                 'CMCSA', 'ADBE', 'ABT', 'ABBV', 'ACN', 'AMD', 'NVDA', 'GOOGL', 'GOOG', 'LLY', 'V', 'AVGO', 'CVX',
                 'MRK', 'COST', 'PEP', 'CSCO', 'CRM', 'TMO', 'MCD', 'PFE', 'ORCL', 'LIN', 'INTU', 'WFC', 'TXN', 'COP',
                 'CAT', 'PM']
stock_data = fetch_stock_data(stock_tickers)

# Calculate percentage changes
pct_changes = calculate_percentage_changes(stock_data)

# Weight each stock according to the percentage of the spy it represents
stock_weights = {'AAPL': 0.0741, 'MSFT': 0.0647, 'AMZN': 0.0326, 'NVDA': 0.0318, 'GOOGL': 0.0213, 'GOOG': 0.0185,
                 'TSLA': 0.0175, 'META': 0.0174, 'UNH': 0.0117, 'LLY': 0.0116, 'JPM': 0.0114, 'V': 0.0106,
                 'JNJ': 0.0102, 'AVGO': 0.0096, 'PG': 0.0096, 'MA': 0.0092, 'HD': 0.0089, 'CVX': 0.0077, 'MRK': 0.0074,
                 'ABBV': 0.0069, 'ADBE': 0.0068, 'COST': 0.0064, 'PEP': 0.0064, 'CSCO': 0.0063, 'TMO': 0.0057,
                 'CRM': 0.0057, 'ACN': 0.0055, 'MCD': 0.0054, 'PFE': 0.0053, 'BAC': 0.0053, 'LIN': 0.0050,
                 'CMCSA': 0.0050, 'ORCL': 0.0049, 'AMD': 0.0047, 'ABT': 0.0047, 'INTU': 0.0041, 'WFC': 0.0041,
                 'TXN': 0.0041, 'DIS': 0.0039, 'COP': 0.0039, 'CAT': 0.0039, 'VZ': 0.0039, 'PM': 0.0039}

# Change percentages to make it equal to 1 so it will be weighted correctly
total = sum(stock_weights.values())
for key in stock_weights:
    stock_weights[key] = stock_weights[key] / total

# Convert to DataFrame and calculate average percentage changes
all_pct_changes_df = pd.DataFrame.from_dict(pct_changes)
weighted_pct_changes = all_pct_changes_df.mul(pd.Series(stock_weights), axis=1).sum(axis=1)
all_pct_changes = all_pct_changes_df.mean(axis=1)


# Download SPY and QQQ data
spy = yf.download('SPY', period='20d', interval='15m')
QQQ = yf.download('QQQ', period='20d', interval='15m')

# Get closes for SPY and QQQ
spy_close = spy['Close'].dropna()
QQQ_close = QQQ['Close'].dropna()

# Choose the stock you want to predict (For now, hardcoding it to QQQ_close)
stock = input('Enter 1 for QQQ, 2 for the market percentage: ')
if stock == '1':
    stock = QQQ_close
elif stock == '2':
    stock = all_pct_changes

# Data Scaling
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(stock.dropna().values.reshape(-1, 1))

# LSTM Data Preparation
look_back = 60
X, y = [], []
for i in range(look_back, len(scaled_data)):
    X.append(scaled_data[i - look_back:i, 0])
    y.append(scaled_data[i, 0])
X, y = np.array(X), np.array(y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Split Data
train_size = int(len(X) * 0.8)
X_train, X_test = X[0:train_size], X[train_size:len(X)]
y_train, y_test = y[0:train_size], y[train_size:len(y)]

# Validation Split
val_size = int(len(X_train) * 0.2)
X_val, y_val = X_train[-val_size:], y_train[-val_size:]
X_train, y_train = X_train[:-val_size], y_train[:-val_size]

# Hyperparameter grid
param_grid = {
    'lstm_units': [64, 128, 256],
    'batch_size': [32, 64, 128, 256],
    'epochs': [20, 30, 35, 40],
    'dropout_rate': [0.2, 0.3, 0.4],
    'learning_rate': [0.1, 0.01, 0.05, 0.001],
    'look_back': [60, 90, 120, 150, 180]
}

# Initialize variables for best metrics
best_metrics = {'mse': float('inf'), 'mae': float('inf'), 'rmse': float('inf')}
best_model = None
best_hyperparameters = None

# Set thresholds
threshold_mse = 0.01
threshold_mae = 0.03
threshold_rmse = 0.03

# Initialize other variables
iteration_count = 0
loop_count = 0





# import time
import time

# Grid Search
for params in ParameterGrid(param_grid):
    iteration_count += 1
    print(f"Current hyperparameter settings: {params}")
    # Print the parameters needed to exit the loop

    if loop_count > 20:
        loop_count = 0
        threshold_mse = (threshold_mse * 0.1) + threshold_mse
        print(f"Current threshold_mse: {threshold_mse}")
        threshold_mae = (threshold_mae * 0.1) + threshold_mae
        print(f"Current threshold_mae: {threshold_mae}")
        threshold_rmse = (threshold_rmse * 0.1) + threshold_rmse
        print(f"Current threshold_rmse: {threshold_rmse}")
        time.sleep(5)


    loop_count += 1

    model = train_model(params, X_train, y_train)
    mse, mae, rmse = evaluate_model(model, X_val, y_val)
    print(f"Current iteration: {iteration_count} of {len(ParameterGrid(param_grid))}\n")
    print(f"Current MSE: {mse}")
    print(f"Current threshold_mse: {threshold_mse}\n")
    print(f"Current MAE: {mae}")
    print(f"Current threshold_mae: {threshold_mae}\n")
    print(f"Current RMSE: {rmse}")
    print(f"Current threshold_rmse: {threshold_rmse}\n")

    # Calculate percentages the thresholds are of the metrics that are between 0 and 100
    mse_pct =  mse / threshold_mse* 100
    mae_pct = threshold_mae /mae * 100
    rmse_pct = rmse /threshold_rmse* 100

    print(f"Current mse_pct: {mse_pct}")
    print(f"Current mae_pct: {mae_pct}")
    print(f"Current rmse_pct: {rmse_pct}\n")
    time.sleep(5)

    if mse < threshold_mse and mae < threshold_mae and rmse < threshold_rmse:
        best_metrics['mse'] = mse
        best_metrics['mae'] = mae
        best_metrics['rmse'] = rmse
        best_model = model
        best_hyperparameters = params
        break





# Use the best model to make predictions
y_train_pred = best_model.predict(X_train)
y_val_pred = best_model.predict(X_val)
y_test_pred = best_model.predict(X_test)

# Inverse transform the predictions
y_train_pred_inv = scaler.inverse_transform(y_train_pred)
y_val_pred_inv = scaler.inverse_transform(y_val_pred)
y_test_pred_inv = scaler.inverse_transform(y_test_pred)

# Determine the index for plotting based on user choice
if stock is QQQ_close:
    plot_index = QQQ_close.index[look_back:train_size]
else:
    plot_index = weighted_pct_changes.index[look_back:train_size]

# Ensure that 'plot_index' and 'y_train' have the same shape
min_length = min(len(plot_index), len(y_train))
plot_index = plot_index[:min_length]
y_train = y_train[:min_length]




"""





# Plotting
plt.figure(figsize=(15, 6))

# Plot training data
plt.subplot(1, 3, 1)
plt.plot(plot_index, scaler.inverse_transform(y_train.reshape(-1, 1)), label='Train Data')
plt.plot(plot_index, y_train_pred_inv[:min_length], label='Train Prediction')
plt.legend()
plt.title('Training Data')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

"""

print("Best Hyperparameters:", best_hyperparameters)
print(f"Best Metrics: MSE - {best_metrics['mse']}, MAE - {best_metrics['mae']}, RMSE - {best_metrics['rmse']}")

print("Shape of QQQ_close.index[look_back:train_size]:", QQQ_close.index[look_back:train_size].shape)
print("Shape of y_train:", y_train.shape)
print("look_back:", look_back)
print("train_size:", train_size)





# INSPECTOR BUTTERS


# # Print the test metrics
# print("Test Metrics:")
# print("MSE:", mean_squared_error(y_test, y_test_pred))
# print("MAE:", mean_absolute_error(y_test, y_test_pred))
# print("RMSE:", np.sqrt(mean_squared_error(y_test, y_test_pred)))
# Message these to discord


