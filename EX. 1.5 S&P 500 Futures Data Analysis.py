# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:07:12 2024

@author: giane
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ticker = 'ES=F'
data = yf.download(ticker)

sp500data = pd.DataFrame(data)
print(sp500data.head())
print(sp500data.describe())

prices = sp500data['Adj Close']
print(prices)

arithmetic_returns = (prices - prices.shift(1)) / prices.shift(1)
log_returns = np.log(prices / prices.shift(1))


cumu_arithmetic_return = np.cumsum(arithmetic_returns)
cumu_log_return = np.exp(np.cumsum(log_returns)) - 1

plt.plot(cumu_arithmetic_return, linestyle='--', color='r', label='Arithmetic Returns')
plt.plot(cumu_log_return, linestyle='--', color='b', label='Logarithmic Returns')
plt.title('Comparison between logarithmic and arithmetical returns')
plt.xlabel('Year')
plt.ylabel('Cumulative Returns')

plt.show()
