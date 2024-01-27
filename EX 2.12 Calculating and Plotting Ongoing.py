# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:26:05 2024

@author: giane
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

sp500_futures=yf.download('ES=F')
prices=sp500_futures['Adj Close']
daily_log_ret=np.log(prices/prices.shift(1))
sp500_futures['Cumulative Returns']=daily_log_ret.cumsum()-1
rolling_max=sp500_futures['Cumulative Returns'].cummax()
sp500_futures['Drawdown']=rolling_max-sp500_futures['Cumulative Returns']

fig,ax=plt.subplots()
ax.fill_between(sp500_futures.index,sp500_futures['Drawdown'],color='r',alpha=0.3)
ax . plot ( sp500_futures ['Cumulative Returns'], label ='Cumulative Returns')
ax.set_title('Cumulative Returns on Ongoing Drawdown')
ax.set_xlabel('Date')
ax.set_ylabel('Returns')
ax.legend()
plt.plot