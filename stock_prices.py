# -*- coding: utf-8 -*-
"""stock prices

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jk9kQxoCSzIzuw-9cJ2pNbP5KI63NjTB
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd # mport the pandas library as pd
# %matplotlib inline
import matplotlib.pyplot as plt # mport the pandas library as pd

data = pd.read_pickle('/content/stock_data.pkl') # This line reads data
stocks = ['AAPL', 'GOOG', 'TSLA']

# plots the 'Adj Close' prices from the data DataFrame for the selected stocks
data['Adj Close'].plot(figsize=(12, 6))
plt.title('Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(stocks)
plt.show()

# Check if a MultiIndex is being used
# checks if the index of the DataFrame data is a MultiIndex and stores the result in the is_multi_index variable.
is_multi_index = isinstance(data.index, pd.MultiIndex)

if is_multi_index:
    print("A MultiIndex is being used in this data.")
else:
    print("A MultiIndex is not being used in this data.")

aapl_closing_price = data['Close']['AAPL'] # line extracts the closing price data for Apple (AAPL) and stores it in the aapl_closing_price variable.

# Plot the closing price of AAPL
plt.figure(figsize=(12, 6))
aapl_closing_price.plot(label='AAPL Close Price')
plt.title('AAPL Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid()
plt.show()

# Select the last row (yesterday's data) and extract the closing prices
closing_prices_yesterday = data.iloc[-1]['Adj Close']

# Print the closing prices for all three stocks
print("Closing Prices for Yesterday:")
print(closing_prices_yesterday)

# Extract a smaller DataFrame containing only TSLA data
tsla_data = data.xs('TSLA', axis=1, level=1)

# Print the smaller DataFrame
print("TSLA Data:")
print(tsla_data)

