# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:09:33 2024

@author: giane
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

sp500_futures = yf.download('ES=F')
prices = sp500_futures['Adj Close']

# Calculate daily log return
log_ret = np.log(prices / prices.shift(1))

# Add a column to the dataframe
sp500_futures['Log_Returns'] = log_ret


# Find the number of bins for the histogram
n_bins=50

# Create the histogram using cleaned data
plt.hist(sp500_futures['Log_Returns'], color='r', bins=n_bins)
plt.axvline(sp500_futures['Log_Returns'].mean(),color='b', linewidth=5)
plt.title('S&P500 Log Returns')
plt.xlabel('Log Returns')
plt.ylabel('Frequency')
plt.yscale('log')
# Show the plot
plt.show()
