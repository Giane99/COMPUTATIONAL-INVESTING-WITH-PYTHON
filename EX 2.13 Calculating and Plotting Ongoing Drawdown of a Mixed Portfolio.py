# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:50:55 2024

@author: giane
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis

sp500_futures = yf.download('ES=F')['Adj Close']
treasury_futures = yf.download('ZN=F')['Adj Close']

data = pd.DataFrame({'SP500': sp500_futures, 'Treasury': treasury_futures}).dropna()

# Daily log returns
data['SP500_ret'] = np.log(data['SP500'] / data['SP500'].shift(1))
data['Treasury_ret'] = np.log(data['Treasury'] / data['Treasury'].shift(1))

# Calculate portfolio returns: 60% SP500, 40% Treasury
data['Portfolio_ret'] = 0.6 * data['SP500_ret'] + 0.4 * data['Treasury_ret']

# Cumulative returns
data['SP500 Cum Ret'] = data['SP500_ret'].cumsum()
data['Treasury Cum Ret'] = data['Treasury_ret'].cumsum()
data['Portfolio Cum Ret'] = data['Portfolio_ret'].cumsum()

# Ongoing drawdown
rolling_max = data['Portfolio Cum Ret'].cummax()
data['Drawdown'] = rolling_max - data['Portfolio Cum Ret']

fig, ax = plt.subplots()
ax.fill_between(data.index, 0, -data['Drawdown'], color='red', alpha=0.3)  # Corrected the fill_between
ax.plot(data['Portfolio Cum Ret'], label='Portfolio Cumulative Returns')
ax.plot(data['SP500 Cum Ret'], label='S&P 500 Cumulative Returns', linestyle='-', linewidth=0.5)
ax.plot(data['Treasury Cum Ret'], label='10-Year Treasury Cumulative Returns', linestyle='--', linewidth=0.5)
ax.set_title('Portfolio Cumulative Returns and Ongoing Drawdown')
ax.set_xlabel('Date')
ax.set_ylabel('Returns / Drawdown')
ax.legend()
plt.show()

annaulized_return=data['Portfolio_ret']*252
print('Annualized Return: ', annaulized_return)
annualized_volatility=data['Portfolio_ret'].std()*np.sqrt(252)
print('Annualized Volatility: ', annualized_volatility)

skew=skew(data['Portfolio_ret'])
print('Skew: ',skew)
kurtosis=kurtosis(data['Portfolio_ret'])
print('Kurtosis: ', kurtosis)
