# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:32:02 2024

@author: giane
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

sp500_futures=yf.download('ES=F')
price=sp500_futures['Adj Close']
daily_log_ret=np.log(price/price.shift(-1))
print(daily_log_ret)

#calculate daily volatility
volatility=daily_log_ret.std()
print(volatility)
#calculate annualized volatility
ann_volatility=volatility*np.sqrt(252)
print(ann_volatility)


max_log_ret = np.round(daily_log_ret.max(), 2)
min_log_ret = np.round(daily_log_ret.min(), 2)

n_bins = int((max_log_ret - min_log_ret) * 100)
plt.hist(daily_log_ret, color='r', bins=n_bins)
print(max_log_ret)
print(min_log_ret)
print(n_bins)

plt . axvline (daily_log_ret.mean() , color ='black', linestyle ='dashed'
, linewidth =2 , label =" Mean Return ")
for i in range (1 , 4) :
    plt . axvline ( daily_log_ret.mean() + i * volatility , color ='green', linestyle ='dashed', linewidth =1 , label =f"+{i} STD ")
    plt . axvline ( daily_log_ret.mean() - i * volatility , color ='r',    linestyle ='dashed', linewidth =1 , label =f" -{i} STD ")
# Show the plot
plt.title('S&P500 Log Returns Distribution with Standard Deviation Lines')
plt.xlabel('Log Returns')
plt.ylabel('Frequency')
plt.yscale('log')
plt.show()