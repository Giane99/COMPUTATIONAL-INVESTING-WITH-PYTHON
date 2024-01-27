# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:44:47 2024

@author: giane
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

sp500_futures=yf.download('ES=F')
print(sp500_futures)
      
#daily log returns

prices=sp500_futures['Adj Close']
log_ret=np.log(prices/prices.shift(1))

#add log returns to the dataset
sp500_futures['daily_log_return']=log_ret

#annualized log return
annualized_ret=sp500_futures['daily_log_return'].mean()*252

print(sp500_futures)
print(annualized_ret)

